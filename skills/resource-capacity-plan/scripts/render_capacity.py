# MIT License
#
# Copyright (c) 2026 Thai Nghiem
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Render evidence-led capacity plans to offline HTML, SVG, JSON and CSV.

Python 3.11+ standard library. The renderer compares known person-level demand
with modeled availability. It never treats spare team hours as interchangeable
capacity, infers a staffing commitment, or silently converts unknown work to 0.
"""
import argparse
import base64
import csv
import html
import io
import json
import math
from pathlib import Path
import sys
import textwrap

PERSON_STATES = ('confirmed', 'proposed', 'unknown')
ALLOCATION_STATES = ('confirmed', 'proposed', 'unknown')
OPTION_STATES = ('open', 'proposed', 'approved', 'rejected')
COLORS = ('#d80b61', '#176b87', '#6f42a6', '#c26716', '#08766c', '#536581')


def esc(value):
    return html.escape(str(value), quote=True)


def _text(item, key, context, required=True):
    value = item.get(key)
    if not isinstance(value, str) or (required and not value.strip()):
        qualifier = 'nonempty ' if required else ''
        raise ValueError(f'{context} {key}: {qualifier}text required')


def _number(value, context, nullable=False):
    if nullable and value is None:
        return
    if type(value) not in (int, float) or not math.isfinite(float(value)) or value < 0:
        raise ValueError(f'{context}: finite nonnegative number required')


def validate(data):
    if not isinstance(data, dict):
        raise ValueError('Expected a capacity-plan snapshot object')
    for key in ('title', 'version', 'as_of', 'source', 'scope', 'state', 'period', 'unit'):
        _text(data, key, 'snapshot')
    if data['unit'] != 'hours':
        raise ValueError('unit must be hours; convert other measures explicitly before rendering')
    people = data.get('people')
    if not isinstance(people, list) or not people:
        raise ValueError('people must be a nonempty list')
    ids, allocation_ids = set(), set()
    for person in people:
        if not isinstance(person, dict):
            raise ValueError('Each person must be an object')
        for key in ('id', 'name', 'role', 'availability_source', 'timing_note', 'source'):
            _text(person, key, 'person')
        if person['id'] in ids:
            raise ValueError(f'duplicate person id: {person["id"]}')
        ids.add(person['id'])
        if person.get('availability_state') not in PERSON_STATES:
            raise ValueError(f'{person["id"]}: invalid availability_state')
        for key in ('gross_hours', 'leave_hours', 'overhead_hours'):
            _number(person.get(key), f'{person["id"]} {key}')
        if person['leave_hours'] + person['overhead_hours'] > person['gross_hours']:
            raise ValueError(f'{person["id"]}: leave plus overhead exceeds gross hours')
        skills = person.get('skills')
        if not isinstance(skills, list) or not skills or any(not isinstance(x, str) or not x.strip() for x in skills):
            raise ValueError(f'{person["id"]}: skills must be a nonempty text list')
        allocations = person.get('allocations')
        if not isinstance(allocations, list):
            raise ValueError(f'{person["id"]}: allocations must be a list')
        for allocation in allocations:
            if not isinstance(allocation, dict):
                raise ValueError(f'{person["id"]}: each allocation must be an object')
            for key in ('id', 'work', 'skill', 'window', 'source', 'note'):
                _text(allocation, key, f'{person["id"]} allocation', required=key != 'note')
            if allocation['id'] in allocation_ids:
                raise ValueError(f'duplicate allocation id: {allocation["id"]}')
            allocation_ids.add(allocation['id'])
            _number(allocation.get('hours'), f'{allocation["id"]} hours', nullable=True)
            if allocation.get('status') not in ALLOCATION_STATES:
                raise ValueError(f'{allocation["id"]}: invalid status')
            if allocation['status'] == 'unknown' and allocation['hours'] is not None:
                raise ValueError(f'{allocation["id"]}: unknown allocation hours must be null')
            if allocation['status'] == 'confirmed' and not allocation['source'].strip():
                raise ValueError(f'{allocation["id"]}: confirmed allocation requires a source')
    constraints = data.get('constraints', [])
    if not isinstance(constraints, list):
        raise ValueError('constraints must be a list')
    constraint_ids = set()
    for item in constraints:
        if not isinstance(item, dict):
            raise ValueError('Each constraint must be an object')
        for key in ('id', 'person_id', 'work', 'skill', 'window', 'conflict', 'consequence', 'status', 'source'):
            _text(item, key, 'constraint')
        if item['id'] in constraint_ids:
            raise ValueError(f'duplicate constraint id: {item["id"]}')
        constraint_ids.add(item['id'])
        if item['person_id'] not in ids:
            raise ValueError(f'{item["id"]}: person_id must reference people')
    options = data.get('options', [])
    if not isinstance(options, list):
        raise ValueError('options must be a list')
    option_ids = set()
    for item in options:
        if not isinstance(item, dict):
            raise ValueError('Each option must be an object')
        for key in ('id', 'label', 'hours_timing_changed', 'skill_basis', 'effect', 'authority', 'status', 'recalculated_result', 'note'):
            _text(item, key, 'option', required=key != 'note')
        if item['id'] in option_ids:
            raise ValueError(f'duplicate option id: {item["id"]}')
        option_ids.add(item['id'])
        if item['status'] not in OPTION_STATES:
            raise ValueError(f'{item["id"]}: invalid option status')
    presentation = data.get('presentation')
    if not isinstance(presentation, dict):
        raise ValueError('presentation is required')
    for key in ('eyebrow', 'headline', 'lede', 'insight_heading', 'decision'):
        _text(presentation, key, 'presentation')
    if presentation.get('default_person_id') not in ids:
        raise ValueError('default_person_id must reference people')
    points = presentation.get('insight_points')
    if not isinstance(points, list) or not points or any(not isinstance(x, str) or not x.strip() for x in points):
        raise ValueError('insight_points must be a nonempty text list')
    analysis = data.get('analysis')
    if not isinstance(analysis, dict):
        raise ValueError('analysis is required')
    for key in ('method', 'support_treatment', 'completeness'):
        _text(analysis, key, 'analysis')
    notes = data.get('notes', [])
    if not isinstance(notes, list) or any(not isinstance(x, str) for x in notes):
        raise ValueError('notes must be text entries')
    return data


def person_result(person):
    available = person['gross_hours'] - person['leave_hours'] - person['overhead_hours']
    known = sum(a['hours'] for a in person['allocations'] if a['hours'] is not None)
    unknown = sum(a['hours'] is None for a in person['allocations'])
    return {
        'available_hours': available,
        'known_demand_hours': known,
        'remaining_hours': available - known,
        'overload_hours': max(0, known - available),
        'load_percent': 100 * known / available if available else None,
        'unknown_allocations': unknown,
    }


def summary(data):
    rows = [person_result(p) for p in data['people']]
    return {
        'people': len(rows),
        'available_hours': sum(r['available_hours'] for r in rows),
        'known_demand_hours': sum(r['known_demand_hours'] for r in rows),
        'person_overload_hours': sum(r['overload_hours'] for r in rows),
        'overloaded_people': sum(r['overload_hours'] > 0 for r in rows),
        'unknown_allocations': sum(r['unknown_allocations'] for r in rows),
    }


def spreadsheet_text(value):
    text = '' if value is None else str(value)
    return "'" + text if isinstance(value, str) and text.startswith(('=', '+', '-', '@', '\t', '\r')) else text


def render_csv(data):
    validate(data)
    stream = io.StringIO(newline='')
    writer = csv.writer(stream, lineterminator='\n')
    writer.writerow(['person_id', 'person', 'role', 'skills', 'gross_hours', 'leave_hours', 'overhead_hours',
                     'available_hours', 'allocation_id', 'work', 'required_skill', 'window', 'hours',
                     'allocation_status', 'remaining_known_hours', 'overload_hours', 'unknown_allocations',
                     'availability_state', 'availability_source', 'allocation_source', 'note'])
    for person in data['people']:
        result = person_result(person)
        allocations = person['allocations'] or [{'id':'', 'work':'', 'skill':'', 'window':'', 'hours':None,
                                                  'status':'', 'source':'', 'note':''}]
        for allocation in allocations:
            values = [person['id'], person['name'], person['role'], '; '.join(person['skills']),
                      person['gross_hours'], person['leave_hours'], person['overhead_hours'], result['available_hours'],
                      allocation['id'], allocation['work'], allocation['skill'], allocation['window'], allocation['hours'],
                      allocation['status'], result['remaining_hours'], result['overload_hours'], result['unknown_allocations'],
                      person['availability_state'], person['availability_source'], allocation['source'], allocation['note']]
            writer.writerow([spreadsheet_text(value) for value in values])
    return stream.getvalue()


def _svg_text(x, y, value, size=13, fill='#13294b', weight='400', anchor=None):
    a = f' text-anchor="{anchor}"' if anchor else ''
    return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{fill}" font-weight="{weight}"{a}>{esc(value)}</text>'


def render_svg(data):
    validate(data)
    width, left, right = 1440, 360, 1320
    results = {p['id']: person_result(p) for p in data['people']}
    maximum = max(1, *(max(r['available_hours'], r['known_demand_hours']) for r in results.values()))
    row_height = 122
    height = 330 + row_height * len(data['people']) + 150
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
           f'<title id="title">{esc(data["title"])}</title>',
           f'<desc id="desc">Capacity plan for {esc(data["period"])}. Known demand is compared with each person’s modeled availability; unknown allocations remain visible.</desc>',
           '<defs><filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#0b1f40" flood-opacity=".10"/></filter></defs>',
           '<rect width="100%" height="100%" fill="#f5f7fb"/><rect width="12" height="100%" fill="#173b2d"/>',
           _svg_text(38, 42, data['presentation']['eyebrow'].upper(), 12, '#d80b61', '800'),
           _svg_text(38, 96, data['presentation']['headline'], 40, '#0c234b', '800'),
           _svg_text(38, 130, data['presentation']['lede'], 15, '#536581')]
    totals = summary(data)
    metrics = [('People', totals['people'], 'in supplied scope'), ('Available', f'{totals["available_hours"]:g} h', 'after leave + overhead'),
               ('Known demand', f'{totals["known_demand_hours"]:g} h', 'unknowns excluded'), ('Person overload', f'{totals["person_overload_hours"]:g} h', 'not netted across people'),
               ('Unknown work', totals['unknown_allocations'], 'allocation records')]
    for index, (label, value, note) in enumerate(metrics):
        x = 38 + index * 270
        out += [f'<g filter="url(#shadow)"><rect x="{x}" y="166" width="252" height="92" rx="14" fill="#fff" stroke="#ccd6e5"/>',
                _svg_text(x+16, 190, label.upper(), 10, '#667085', '800'), _svg_text(x+16, 223, value, 24, '#0c234b', '800'),
                _svg_text(x+16, 244, note, 10, '#667085'), '</g>']
    y = 314
    for person in data['people']:
        result = results[person['id']]
        out += [f'<g data-person="{esc(person["id"])}"><rect x="26" y="{y}" width="1388" height="108" rx="14" fill="#fff" stroke="#d4deeb"/>',
                f'<rect x="26" y="{y}" width="6" height="108" rx="3" fill="{"#d80b61" if result["overload_hours"] else "#08766c"}"/>',
                _svg_text(50, y+29, person['name'], 17, '#0c234b', '800'), _svg_text(50, y+50, person['role'], 11, '#536581'),
                _svg_text(50, y+72, ' · '.join(person['skills'])[:42], 10, '#667085')]
        bar_x, bar_w = left, right-left
        cursor = bar_x
        for index, allocation in enumerate(person['allocations']):
            if allocation['hours'] is None:
                continue
            w = allocation['hours'] / maximum * bar_w
            out.append(f'<rect x="{cursor}" y="{y+25}" width="{max(w, 1)}" height="34" rx="5" fill="{COLORS[index % len(COLORS)]}"/>')
            if w > 72:
                out.append(_svg_text(cursor+8, y+47, f'{allocation["work"][:19]} · {allocation["hours"]:g} h', 10, '#fff', '700'))
            cursor += w
        marker = bar_x + result['available_hours'] / maximum * bar_w
        out += [f'<line x1="{marker}" y1="{y+14}" x2="{marker}" y2="{y+70}" stroke="#0c234b" stroke-width="3" stroke-dasharray="5 3"/>',
                _svg_text(marker, y+88, f'available {result["available_hours"]:g} h', 10, '#0c234b', '700', 'middle'),
                _svg_text(width-42, y+42, f'{result["known_demand_hours"]:g} h demand', 12, '#0c234b', '700', 'end')]
        state = f'OVER {result["overload_hours"]:g} h' if result['overload_hours'] else f'SPARE {max(0,result["remaining_hours"]):g} h'
        if result['unknown_allocations']:
            state += f' + {result["unknown_allocations"]} UNKNOWN'
        out.append(_svg_text(width-42, y+66, state, 11, '#d80b61' if result['overload_hours'] else '#08766c', '800', 'end'))
        out.append('</g>')
        y += row_height
    footer = y + 20
    note_lines = textwrap.wrap(data['presentation']['decision'], 150, break_long_words=False)
    out += [_svg_text(38, footer, 'DECISION', 10, '#d80b61', '800')]
    for index, line in enumerate(note_lines[:3]):
        out.append(_svg_text(38, footer+24+index*18, line, 12, '#13294b', '600'))
    out += [_svg_text(38, footer+82, f'As of {data["as_of"]} · {data["state"]} · {data["analysis"]["method"][:165]}', 10, '#667085'), '</svg>']
    return ''.join(out)


def _safe_json(value):
    return json.dumps(value, ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c').replace('>', '\\u003e').replace('&', '\\u0026')


def _data_uri(text, media_type):
    encoded = base64.b64encode(text.encode('utf-8')).decode('ascii')
    return f'data:{media_type};base64,{encoded}'


def render_html(data, svg=None, csv_text=None):
    validate(data)
    svg = svg or render_svg(data)
    csv_text = csv_text or render_csv(data)
    page = r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title><style>
:root{--navy:#0c234b;--ink:#13294b;--muted:#60708a;--line:#cfdae9;--paper:#fff;--bg:#f3f6fa;--pink:#d80b61;--green:#08766c;--amber:#a25b00;--red:#b42318;--shadow:0 12px 30px rgba(12,35,75,.09)}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 Arial,sans-serif;border-left:10px solid #173b2d}button,input,select,textarea{font:inherit;color:inherit}button,.button{border:1px solid #b9c8dc;border-radius:12px;background:#fff;padding:11px 14px;font-weight:700;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;justify-content:center;gap:6px}button:hover,.button:hover{border-color:#778ba7}.primary{background:var(--navy);color:#fff;border-color:var(--navy)}.accent{border-color:var(--pink);color:#a60049;background:#fff5f9}.active{box-shadow:0 0 0 3px #ffb8d6;border-color:var(--pink)}button:focus-visible,.button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,[tabindex]:focus-visible{outline:3px solid #79a8e8;outline-offset:2px}.hero{padding:28px 32px 20px;display:grid;grid-template-columns:minmax(0,1fr) minmax(300px,640px);gap:28px;align-items:end}.eyebrow{text-transform:uppercase;color:var(--pink);font-weight:800;letter-spacing:2px;font-size:12px}.hero h1{font-size:clamp(32px,4vw,52px);line-height:1.02;margin:16px 0 0}.hero .lede{color:var(--muted);font-size:17px;text-align:right;margin:0}.metrics{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;padding:0 30px 18px}.metric{background:#fff;border:1px solid var(--line);border-radius:14px;padding:13px 15px;box-shadow:var(--shadow)}.metric small{display:block;color:var(--muted);font-weight:800;text-transform:uppercase;letter-spacing:.7px}.metric b{display:block;font-size:23px;margin-top:5px}.metric span{color:var(--muted);font-size:11px}.controls{margin:0 20px 16px;padding:16px 18px;background:#fff;border:1px solid var(--line);border-radius:18px;display:grid;grid-template-columns:minmax(200px,1.4fr) repeat(2,minmax(150px,.8fr)) auto auto;gap:12px;align-items:end;box-shadow:var(--shadow)}label{font-weight:800;font-size:12px;color:#536581;text-transform:uppercase;letter-spacing:.45px}input,select,textarea{display:block;width:100%;margin-top:5px;border:1px solid #b9c8dc;border-radius:10px;padding:10px 11px;background:#fff;min-height:42px}textarea{min-height:74px;resize:vertical}.control-actions{display:flex;gap:8px;flex-wrap:wrap}.scope{grid-column:1/-1;color:var(--muted);font-size:12px}.tabs{display:flex;gap:7px;margin:0 30px 13px;flex-wrap:wrap}.tab{border-radius:999px;padding:8px 13px}.view{margin:0 20px 18px;background:#fff;border:1px solid var(--line);border-radius:18px;box-shadow:var(--shadow);overflow:hidden}.view-head{padding:18px 20px;border-bottom:1px solid var(--line);display:flex;justify-content:space-between;gap:18px;align-items:start}.view-head h2{margin:0 0 3px;font-size:20px}.view-head p{margin:0;color:var(--muted)}.legend{display:flex;gap:12px;flex-wrap:wrap;color:var(--muted);font-size:11px}.swatch{display:inline-block;width:13px;height:13px;border-radius:3px;margin-right:4px;vertical-align:-2px}.chart{padding:8px 20px 20px}.person-row{display:grid;grid-template-columns:270px minmax(430px,1fr) 170px;gap:18px;align-items:center;padding:16px 0;border-bottom:1px solid #e3e9f1;cursor:pointer}.person-row:last-child{border-bottom:0}.person-row.edited{background:#fff7fb;margin:0 -20px;padding-left:20px;padding-right:20px}.identity b{font-size:16px}.identity small{display:block;color:var(--muted);margin-top:2px}.skill{display:inline-block;border:1px solid #ccd7e5;border-radius:999px;padding:2px 7px;margin:5px 4px 0 0;font-size:10px}.bar-shell{position:relative;padding:20px 0 24px}.bar-track{height:38px;background:#e9eef5;border-radius:9px;display:flex;overflow:hidden}.segment{height:100%;min-width:2px;display:flex;align-items:center;color:#fff;font-size:10px;font-weight:800;padding:0 8px;white-space:nowrap;overflow:hidden}.capacity-mark{position:absolute;top:7px;height:63px;border-left:3px dashed var(--navy)}.capacity-mark span{position:absolute;top:47px;transform:translateX(-50%);white-space:nowrap;font-size:10px;font-weight:800;background:#fff;padding:0 3px}.unknown-mark{margin-top:5px;color:var(--amber);font-weight:700;font-size:11px}.outcome{text-align:right}.outcome b{display:block;font-size:16px}.over{color:var(--red)}.spare{color:var(--green)}.outcome small{color:var(--muted)}.scroll{overflow:auto}.data-table{width:100%;border-collapse:collapse;min-width:1100px}.data-table th,.data-table td{padding:11px 12px;border-bottom:1px solid #dce4ef;text-align:left;vertical-align:top}.data-table th{position:sticky;top:0;background:#edf2f8;color:#536581;font-size:11px;text-transform:uppercase;letter-spacing:.4px}.data-table tbody tr{cursor:pointer}.data-table tbody tr:hover{background:#f6f9fd}.data-table tbody tr.edited{background:#fff2f8}.tag{display:inline-block;border:1px solid #ccd7e5;border-radius:999px;padding:3px 8px;font-size:10px;font-weight:800;margin:0 4px 4px 0}.tag.overload{background:#fff0f3;border-color:#f1a3bd;color:#a60049}.tag.unknown{background:#fff5de;border-color:#e5c17b;color:#744c0e}.cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;padding:18px}.evidence-card{border:1px solid var(--line);border-radius:14px;padding:15px;background:#fff}.evidence-card h3{margin:4px 0 8px}.evidence-card p{margin:5px 0;color:var(--muted)}.evidence-card small{color:var(--pink);font-weight:800}.detail{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(320px,.8fr);gap:18px;margin:0 20px 18px}.panel{background:#fff;border:1px solid var(--line);border-radius:18px;padding:18px 20px;box-shadow:var(--shadow)}.panel h2{margin:0 0 8px}.facts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}.fact{border:1px solid #d8e1ed;border-radius:11px;padding:10px}.fact small{display:block;text-transform:uppercase;color:var(--muted);font-size:9px;font-weight:800}.fact b{display:block;margin-top:4px}.alloc-list{margin-top:14px}.allocation{border-top:1px solid #e0e7f0;padding:10px 0}.allocation b{display:block}.allocation span{color:var(--muted);font-size:12px}.editor{border-top:5px solid var(--pink)}.editor[hidden]{display:none}.form-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.wide{grid-column:1/-1}.editor-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}.error{min-height:20px;color:var(--red);font-weight:700;margin:8px 0 0}.alloc-edit{border:1px solid #d4deeb;border-radius:12px;padding:10px;margin:10px 0;position:relative}.alloc-edit .remove{position:absolute;right:8px;top:8px;padding:5px 8px;color:var(--red)}.notice{margin:0 20px 18px;padding:14px 18px;border:1px solid #efc17c;background:#fff7e6;border-radius:14px;color:#69420b}.history{max-height:180px;overflow:auto;padding-left:19px;color:var(--muted)}.empty{padding:40px;text-align:center;color:var(--muted)}footer{padding:8px 30px 30px;color:var(--muted);font-size:11px}.mobile-label{display:none}
@media(max-width:900px){body{border-left-width:6px}.hero{grid-template-columns:1fr;padding:22px 18px 16px}.hero .lede{text-align:left}.metrics{grid-template-columns:repeat(2,1fr);padding:0 16px 15px}.controls{margin:0 10px 14px;grid-template-columns:1fr 1fr}.tabs{margin:0 16px 12px}.view,.detail{margin-left:10px;margin-right:10px}.person-row{grid-template-columns:190px minmax(360px,1fr) 130px}.chart{overflow-x:auto}.detail{grid-template-columns:1fr}.cards{grid-template-columns:1fr}.facts{grid-template-columns:repeat(2,1fr)}}
@media(max-width:520px){.metrics{grid-template-columns:1fr 1fr}.metric{padding:10px}.metric b{font-size:19px}.controls{grid-template-columns:1fr}.control-actions{grid-column:1}.view-head{display:block}.legend{margin-top:8px}.person-row{grid-template-columns:155px 350px 110px}.chart{padding-left:14px}.form-grid{grid-template-columns:1fr}.wide{grid-column:1}.facts{grid-template-columns:1fr}.hero h1{font-size:34px}.hero .lede{font-size:14px}}
@media print{body{border:0;background:#fff}.controls,.tabs,.editor,.editor-actions,#historyPanel{display:none!important}.view,.panel{box-shadow:none;margin:8px 0}.hero{padding:12px 0}.metrics{padding:0}.person-row{break-inside:avoid}.notice{margin:8px 0}}
</style></head><body>
<header class="hero"><div><div class="eyebrow">__EYEBROW__</div><h1>__HEADLINE__</h1></div><p class="lede">__LEDE__</p></header>
<section class="metrics" aria-label="Capacity summary"><div class="metric" data-metric="people"><small>People</small><b id="mPeople"></b><span>visible scope</span></div><div class="metric" data-metric="available"><small>Available</small><b id="mAvailable"></b><span>after leave + overhead</span></div><div class="metric" data-metric="known demand"><small>Known demand</small><b id="mDemand"></b><span>unknown work excluded</span></div><div class="metric" data-metric="person overload"><small>Person overload</small><b id="mOverload"></b><span>never netted across people</span></div><div class="metric" data-metric="unknown work"><small>Unknown work</small><b id="mUnknown"></b><span>allocation records</span></div></section>
<section class="controls" aria-label="Capacity controls"><label>Find person or work<input id="search" type="search" placeholder="Search name, role, skill or work"></label><label>Skill<select id="skill"><option value="">All skills</option></select></label><label>Assignment state<select id="status"><option value="">All states</option><option>confirmed</option><option>proposed</option><option>unknown</option></select></label><button id="overloads" class="accent" aria-pressed="false">Overloads only</button><div class="control-actions"><button id="editToggle">Edit local draft</button><button id="reset">Reset view</button><button id="print" class="primary">Print / PDF</button></div><div class="scope" id="scope" aria-live="polite"></div></section>
<nav class="tabs" aria-label="Capacity views"><button id="chartTab" class="tab active">Load chart</button><button id="tableTab" class="tab">Editable table</button><button id="constraintsTab" class="tab">Timing &amp; skills</button><button id="optionsTab" class="tab">Decision options</button></nav>
<section class="view" id="chartView"><div class="view-head"><div><h2>Person-level demand</h2><p>Each marker is that person’s modeled availability. Segments are known allocations on one common scale.</p></div><div class="legend"><span><i class="swatch" style="background:#0c234b"></i>availability marker</span><span><i class="swatch" style="background:#d80b61"></i>known demand segment</span><span>⚠ unknown hours</span></div></div><div class="chart" id="chart"></div></section>
<section class="view" id="tableView" hidden><div class="view-head"><div><h2>Capacity register</h2><p>Available = gross − leave − overhead. Known demand excludes allocations whose hours remain unknown.</p></div></div><div class="scroll"><table class="data-table" id="capacityTable"><thead><tr><th>Person / skill</th><th>Gross</th><th>Leave</th><th>Overhead</th><th>Available</th><th>Known demand</th><th>Remaining / overload</th><th>Unknown</th><th>Evidence</th></tr></thead><tbody></tbody></table></div></section>
<section class="view" id="constraintsView" hidden><div class="view-head"><div><h2>Skill and timing checks</h2><p>Period totals do not prove that the required person and skill are available in the required window.</p></div></div><div class="cards" id="constraints"></div></section>
<section class="view" id="optionsView" hidden><div class="view-head"><div><h2>Decision options</h2><p>Options remain proposals until the named authority approves real scope, timing or staffing changes.</p></div></div><div class="cards" id="options"></div></section>
<div class="notice" id="draftNotice" hidden><b>Local draft:</b> arithmetic and views are recalculated here. Skill/timing checks and option results come from the source snapshot and must be revalidated after edits.</div>
<section class="detail"><article class="panel" id="detail" tabindex="-1"><div id="detailSummary"></div><div class="facts" id="detailFacts"></div><div class="alloc-list" id="detailAllocations"></div></article>
<form class="panel editor" id="personEditor" hidden><h2>Edit selected person</h2><p>Changes stay in this browser until exported. Person and allocation IDs remain source-controlled.</p><div class="form-grid"><label>Name<input id="editName" required></label><label>Role<input id="editRole" required></label><label>Skills, comma separated<input id="editSkills" required></label><label>Availability state<select id="editAvailabilityState"><option>confirmed</option><option>proposed</option><option>unknown</option></select></label><label>Gross hours<input id="editGross" type="number" min="0" step="0.25" required></label><label>Leave hours<input id="editLeave" type="number" min="0" step="0.25" required></label><label>Overhead hours<input id="editOverhead" type="number" min="0" step="0.25" required></label><label>Availability evidence<input id="editAvailabilitySource" required></label><label class="wide">Timing note<textarea id="editTiming" required></textarea></label><label class="wide">Person source<textarea id="editPersonSource" required></textarea></label></div><h3>Allocations</h3><div id="allocationEditor"></div><button type="button" id="addAllocation">+ Add allocation</button><p class="error" id="editError" aria-live="polite"></p><div class="editor-actions"><button type="submit" class="primary" id="savePerson">Save local draft</button><button type="button" id="closeEditor">Close</button></div></form></section>
<section class="detail"><article class="panel"><h2>Evidence boundary</h2><p><b>Method:</b> __METHOD__</p><p><b>Support treatment:</b> __SUPPORT__</p><p><b>Completeness:</b> __COMPLETENESS__</p><p><b>Decision:</b> __DECISION__</p></article><article class="panel" id="historyPanel"><h2>Local history</h2><div class="editor-actions"><button id="undoEdit">Undo last edit</button><button id="discardDraft">Restore source snapshot</button></div><ol class="history" id="history"></ol></article></section>
<footer><div class="control-actions"><a class="button" id="fullSvg" download="capacity-plan.svg">Source SVG</a><a class="button" id="fullJson" download="capacity-plan.json">Source JSON</a><a class="button" id="fullCsv" download="capacity-plan.csv">Source CSV</a><button id="draftJson">Draft JSON</button><button id="draftCsv">Draft CSV</button><button id="visibleCsv">Visible draft CSV</button></div><p>Source exports preserve the embedded snapshot. Draft exports include local changes and do not imply approval or a live-system write.</p></footer>
<script>
const SOURCE_DATA=__DATA__,SOURCE_CSV=__CSV__,SOURCE_SVG=__SVG__,KEY='capacity-plan:'+SOURCE_DATA.title+':'+SOURCE_DATA.version;
const clone=x=>JSON.parse(JSON.stringify(x)),sourcePeople=Object.fromEntries(SOURCE_DATA.people.map(p=>[p.id,clone(p)]));let DATA=clone(SOURCE_DATA),selected=DATA.presentation.default_person_id,view='chart',onlyOver=false,editMode=false,editMessage='',HISTORY=[];
const $=q=>document.querySelector(q),e=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])),num=x=>Number(x),fmt=x=>Number(x).toLocaleString(undefined,{maximumFractionDigits:2}),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
const colors=['#d80b61','#176b87','#6f42a6','#c26716','#08766c','#536581'];
function result(p){let available=p.gross_hours-p.leave_hours-p.overhead_hours,known=p.allocations.reduce((s,a)=>s+(a.hours===null?0:a.hours),0),unknown=p.allocations.filter(a=>a.hours===null).length;return{available,known,remaining:available-known,overload:Math.max(0,known-available),load:available?known/available*100:null,unknown}}
function changed(){return DATA.people.filter(p=>!same(p,sourcePeople[p.id])).length}
function allSkills(){return [...new Set(DATA.people.flatMap(p=>[...p.skills,...p.allocations.map(a=>a.skill)]))].sort()}
function visible(){let q=$('#search').value.trim().toLowerCase(),skill=$('#skill').value,status=$('#status').value;return DATA.people.filter(p=>{let r=result(p),hay=[p.name,p.role,...p.skills,...p.allocations.flatMap(a=>[a.work,a.skill,a.window,a.source])].join(' ').toLowerCase();return(!q||hay.includes(q))&&(!skill||p.skills.includes(skill)||p.allocations.some(a=>a.skill===skill))&&(!status||p.availability_state===status||p.allocations.some(a=>a.status===status))&&(!onlyOver||r.overload>0)})}
function setupSkills(){let current=$('#skill').value;$('#skill').innerHTML='<option value="">All skills</option>'+allSkills().map(x=>`<option>${e(x)}</option>`).join('');$('#skill').value=allSkills().includes(current)?current:''}
function renderMetrics(rows){let rr=rows.map(result);$('#mPeople').textContent=rows.length;$('#mAvailable').textContent=fmt(rr.reduce((s,r)=>s+r.available,0))+' h';$('#mDemand').textContent=fmt(rr.reduce((s,r)=>s+r.known,0))+' h';$('#mOverload').textContent=fmt(rr.reduce((s,r)=>s+r.overload,0))+' h';$('#mUnknown').textContent=rr.reduce((s,r)=>s+r.unknown,0)}
function renderChart(rows){let max=Math.max(1,...DATA.people.map(p=>{let r=result(p);return Math.max(r.available,r.known)}));$('#chart').innerHTML=rows.length?rows.map(p=>{let r=result(p),cursor=0,segments=p.allocations.filter(a=>a.hours!==null).map((a,i)=>{let w=a.hours/max*100,html=`<span class="segment" title="${e(a.work)} · ${fmt(a.hours)} h · ${e(a.status)}" style="width:${w}%;background:${colors[i%colors.length]}">${w>11?e(a.work)+' · '+fmt(a.hours)+' h':''}</span>`;cursor+=w;return html}).join('');return`<article class="person-row ${same(p,sourcePeople[p.id])?'':'edited'}" tabindex="0" role="button" data-person-id="${e(p.id)}"><div class="identity"><b>${e(p.name)}</b><small>${e(p.role)} · ${e(p.availability_state)}</small>${p.skills.map(x=>`<span class="skill">${e(x)}</span>`).join('')}</div><div class="bar-shell"><div class="bar-track">${segments}</div><span class="capacity-mark" style="left:${r.available/max*100}%"><span>${fmt(r.available)} h available</span></span>${r.unknown?`<div class="unknown-mark">⚠ ${r.unknown} allocation${r.unknown===1?'':'s'} with unknown hours</div>`:''}</div><div class="outcome"><b class="${r.overload?'over':'spare'}">${r.overload?'Over '+fmt(r.overload)+' h':'Spare '+fmt(Math.max(0,r.remaining))+' h'}</b><small>${r.load===null?'load unavailable':fmt(r.load)+'% known load'}<br>${fmt(r.known)} h known demand</small></div></article>`}).join(''):'<div class="empty">No people match the current filters.</div>'}
function renderTable(rows){$('#capacityTable tbody').innerHTML=rows.map(p=>{let r=result(p);return`<tr tabindex="0" data-person-id="${e(p.id)}" class="${same(p,sourcePeople[p.id])?'':'edited'}"><td><b>${e(p.name)}</b><br>${e(p.role)}<br><small>${e(p.skills.join(' · '))}</small></td><td>${fmt(p.gross_hours)}</td><td>${fmt(p.leave_hours)}</td><td>${fmt(p.overhead_hours)}</td><td><b>${fmt(r.available)} h</b></td><td><b>${fmt(r.known)} h</b><br><small>${p.allocations.filter(a=>a.hours!==null).map(a=>e(a.work)+' '+fmt(a.hours)+' h').join('<br>')}</small></td><td>${r.overload?`<span class="tag overload">over ${fmt(r.overload)} h</span>`:`<span class="tag">spare ${fmt(Math.max(0,r.remaining))} h</span>`}</td><td>${r.unknown?`<span class="tag unknown">${r.unknown} unknown</span>`:'0'}</td><td>${e(p.availability_source)}<br><small>${e(p.timing_note)}</small></td></tr>`}).join('')}
function renderEvidence(){let people=Object.fromEntries(DATA.people.map(p=>[p.id,p]));$('#constraints').innerHTML=DATA.constraints.map(x=>`<article class="evidence-card"><small>${e(x.id)} · ${e(x.status)}</small><h3>${e(x.work)}</h3><p><b>${e(people[x.person_id].name)} · ${e(x.skill)} · ${e(x.window)}</b></p><p>${e(x.conflict)}</p><p><b>Consequence:</b> ${e(x.consequence)}</p><p><b>Source:</b> ${e(x.source)}</p></article>`).join('')||'<div class="empty">No explicit timing or skill checks supplied.</div>';$('#options').innerHTML=DATA.options.map(x=>`<article class="evidence-card"><small>${e(x.id)} · ${e(x.status)}</small><h3>${e(x.label)}</h3><p><b>Change:</b> ${e(x.hours_timing_changed)}</p><p><b>Skill basis:</b> ${e(x.skill_basis)}</p><p><b>Effect:</b> ${e(x.effect)}</p><p><b>Authority:</b> ${e(x.authority)}</p><p><b>Result:</b> ${e(x.recalculated_result)}</p>${x.note?`<p>${e(x.note)}</p>`:''}</article>`).join('')||'<div class="empty">No decision options supplied.</div>'}
function choose(id){selected=id;editMessage='';render();$('#detail').focus()}
function wireRows(){document.querySelectorAll('[data-person-id]').forEach(row=>{let go=()=>choose(row.dataset.personId);row.onclick=go;row.onkeydown=event=>{if(event.key==='Enter'||event.key===' '){event.preventDefault();go()}}})}
function renderDetail(){let p=DATA.people.find(x=>x.id===selected)||DATA.people[0];selected=p.id;let r=result(p),edited=!same(p,sourcePeople[p.id]);$('#detailSummary').innerHTML=`<span class="tag">${e(p.id)}</span><span class="tag">${e(p.availability_state)}</span>${edited?'<span class="tag overload">local draft</span>':''}<h2>${e(p.name)}</h2><p><b>${e(p.role)}</b> · ${e(p.skills.join(' · '))}</p><p>${e(p.timing_note)}</p><p><b>Availability evidence:</b> ${e(p.availability_source)}</p>`;$('#detailFacts').innerHTML=`<div class="fact"><small>Modeled available</small><b>${fmt(r.available)} h</b></div><div class="fact"><small>Known demand</small><b>${fmt(r.known)} h</b></div><div class="fact"><small>Remaining</small><b class="${r.overload?'over':'spare'}">${fmt(r.remaining)} h</b></div><div class="fact"><small>Person overload</small><b>${fmt(r.overload)} h</b></div><div class="fact"><small>Known load</small><b>${r.load===null?'Unavailable':fmt(r.load)+'%'}</b></div><div class="fact"><small>Unknown allocations</small><b>${r.unknown}</b></div>`;$('#detailAllocations').innerHTML='<h3>Allocations</h3>'+p.allocations.map((a,i)=>`<div class="allocation"><span class="tag" style="border-color:${colors[i%colors.length]}">${e(a.id)}</span><b>${e(a.work)} · ${a.hours===null?'hours unknown':fmt(a.hours)+' h'}</b><span>${e(a.skill)} · ${e(a.window)} · ${e(a.status)}<br>${e(a.source)}${a.note?'<br>'+e(a.note):''}</span></div>`).join('');$('#personEditor').hidden=!editMode;if(editMode&&($('#personEditor').dataset.personId!==p.id||!$('#personEditor').matches(':focus-within')))populateEditor(p);$('#editError').textContent=editMessage}
function allocEditor(a,isNew=false){return`<div class="alloc-edit" data-id="${e(a.id)}" data-new="${isNew?'true':'false'}"><button type="button" class="remove" aria-label="Remove allocation">Remove</button><div class="form-grid"><label>Allocation ID<input class="a-id" value="${e(a.id)}" ${isNew?'':'readonly'} required></label><label>State<select class="a-status">${['confirmed','proposed','unknown'].map(x=>`<option ${x===a.status?'selected':''}>${x}</option>`).join('')}</select></label><label class="wide">Work<input class="a-work" value="${e(a.work)}" required></label><label>Required skill<input class="a-skill" value="${e(a.skill)}" required></label><label>Window<input class="a-window" value="${e(a.window)}" required></label><label>Hours (blank only when unknown)<input class="a-hours" type="number" min="0" step="0.25" value="${a.hours===null?'':e(a.hours)}"></label><label>Evidence source<input class="a-source" value="${e(a.source)}" required></label><label class="wide">Note<textarea class="a-note">${e(a.note)}</textarea></label></div></div>`}
function wireAllocationEditor(){document.querySelectorAll('.alloc-edit .remove').forEach(button=>button.onclick=()=>button.closest('.alloc-edit').remove())}
function populateEditor(p){$('#personEditor').dataset.personId=p.id;$('#editName').value=p.name;$('#editRole').value=p.role;$('#editSkills').value=p.skills.join(', ');$('#editAvailabilityState').value=p.availability_state;$('#editGross').value=p.gross_hours;$('#editLeave').value=p.leave_hours;$('#editOverhead').value=p.overhead_hours;$('#editAvailabilitySource').value=p.availability_source;$('#editTiming').value=p.timing_note;$('#editPersonSource').value=p.source;$('#allocationEditor').innerHTML=p.allocations.map(a=>allocEditor(a)).join('');wireAllocationEditor()}
function editedPerson(){let source=DATA.people.find(p=>p.id===selected),allocations=[...document.querySelectorAll('.alloc-edit')].map(row=>{let raw=row.querySelector('.a-hours').value.trim(),hours=raw===''?null:Number(raw);return{id:row.querySelector('.a-id').value.trim(),work:row.querySelector('.a-work').value.trim(),skill:row.querySelector('.a-skill').value.trim(),window:row.querySelector('.a-window').value.trim(),hours,status:row.querySelector('.a-status').value,source:row.querySelector('.a-source').value.trim(),note:row.querySelector('.a-note').value.trim()}});return{id:source.id,name:$('#editName').value.trim(),role:$('#editRole').value.trim(),skills:$('#editSkills').value.split(',').map(x=>x.trim()).filter(Boolean),gross_hours:Number($('#editGross').value),leave_hours:Number($('#editLeave').value),overhead_hours:Number($('#editOverhead').value),availability_state:$('#editAvailabilityState').value,availability_source:$('#editAvailabilitySource').value.trim(),timing_note:$('#editTiming').value.trim(),source:$('#editPersonSource').value.trim(),allocations}}
function validateEdited(p){let texts=[p.name,p.role,p.availability_source,p.timing_note,p.source];if(texts.some(x=>!x)||!p.skills.length)return'Complete all person fields and provide at least one skill.';if([p.gross_hours,p.leave_hours,p.overhead_hours].some(x=>!Number.isFinite(x)||x<0))return'Hours must be finite, nonnegative numbers.';if(p.leave_hours+p.overhead_hours>p.gross_hours)return'Leave plus overhead cannot exceed gross hours.';let ids=new Set;for(let a of p.allocations){if(!a.id||!a.work||!a.skill||!a.window||!a.source)return'Complete every allocation field except note.';if(ids.has(a.id)||DATA.people.some(other=>other.id!==p.id&&other.allocations.some(x=>x.id===a.id)))return'Allocation IDs must be unique.';ids.add(a.id);if(a.hours!==null&&(!Number.isFinite(a.hours)||a.hours<0))return'Allocation hours must be nonnegative, or blank when unknown.';if(a.status==='unknown'&&a.hours!==null)return'Unknown allocations must leave hours blank.';if(a.status!=='unknown'&&a.hours===null)return'Confirmed or proposed allocations require hours.';}return''}
function renderHistory(){$('#history').innerHTML=HISTORY.length?HISTORY.slice().reverse().map(x=>`<li><b>${e(x.id)}</b> · ${e(x.at)}</li>`).join(''):'<li>No local edits in this browser.</li>';$('#undoEdit').disabled=!HISTORY.length;$('#discardDraft').disabled=!changed()&&!HISTORY.length}
function setView(){for(let name of ['chart','table','constraints','options']){$('#'+name+'View').hidden=view!==name;$('#'+name+'Tab').classList.toggle('active',view===name)}}
function render(){setupSkills();let rows=visible(),edits=changed();renderMetrics(rows);renderChart(rows);renderTable(rows);renderEvidence();renderDetail();renderHistory();setView();wireRows();$('#scope').textContent=`${rows.length} / ${DATA.people.length} people visible · ${rows.filter(p=>result(p).overload>0).length} overloaded in view · ${edits?edits+' locally edited':'no local draft changes'}`;$('#draftNotice').hidden=!edits}
function draftSnapshot(){let out=clone(DATA);out.local_draft={base_version:SOURCE_DATA.version,changed_people:changed(),history_entries:HISTORY.length,exported_at:new Date().toISOString(),notice:'Browser-local proposal; no assignment or availability approval is implied.'};return out}
function csvText(rows=DATA.people){let q=x=>{x=x??'';x=String(x);if(/^[=+\-@\t\r]/.test(x))x="'"+x;return/[",\n]/.test(x)?'"'+x.replaceAll('"','""')+'"':x},head=['person_id','person','role','skills','gross_hours','leave_hours','overhead_hours','available_hours','allocation_id','work','required_skill','window','hours','allocation_status','remaining_known_hours','overload_hours','unknown_allocations','availability_state','availability_source','allocation_source','note'],lines=[head];rows.forEach(p=>{let r=result(p),allocs=p.allocations.length?p.allocations:[{id:'',work:'',skill:'',window:'',hours:null,status:'',source:'',note:''}];allocs.forEach(a=>lines.push([p.id,p.name,p.role,p.skills.join('; '),p.gross_hours,p.leave_hours,p.overhead_hours,r.available,a.id,a.work,a.skill,a.window,a.hours,a.status,r.remaining,r.overload,r.unknown,p.availability_state,p.availability_source,a.source,a.note]))});return lines.map(row=>row.map(q).join(',')).join('\n')+'\n'}
function download(name,body,type){let a=document.createElement('a');a.href=URL.createObjectURL(new Blob([body],{type}));a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),500)}
function persist(){localStorage.setItem(KEY,JSON.stringify({people:DATA.people,history:HISTORY,selected}))}
function loadDraft(){try{let saved=JSON.parse(localStorage.getItem(KEY));if(saved&&Array.isArray(saved.people)&&saved.people.length===SOURCE_DATA.people.length&&saved.people.every(p=>sourcePeople[p.id])){DATA.people=saved.people;HISTORY=Array.isArray(saved.history)?saved.history.slice(-200):[];selected=sourcePeople[saved.selected]?saved.selected:selected}}catch(error){localStorage.removeItem(KEY)}}
$('#personEditor').addEventListener('submit',event=>{event.preventDefault();let index=DATA.people.findIndex(p=>p.id===selected),before=clone(DATA.people[index]),after=editedPerson(),error=validateEdited(after);if(error){editMessage=error;$('#editError').textContent=error;return}if(same(before,after)){editMessage='No changes to save.';$('#editError').textContent=editMessage;return}DATA.people[index]=after;HISTORY.push({id:after.id,before,after:clone(after),at:new Date().toISOString()});HISTORY=HISTORY.slice(-200);editMessage='Local draft saved. Arithmetic recalculated; source exports remain unchanged.';persist();render()});
$('#addAllocation').onclick=()=>{let p=DATA.people.find(x=>x.id===selected),n=1,id;do{id='LOCAL-'+p.id+'-'+n++}while(DATA.people.some(person=>person.allocations.some(a=>a.id===id))||[...document.querySelectorAll('.a-id')].some(x=>x.value===id));$('#allocationEditor').insertAdjacentHTML('beforeend',allocEditor({id,work:'',skill:p.skills[0]||'',window:DATA.period,hours:null,status:'unknown',source:'Local draft; evidence required',note:''},true));wireAllocationEditor()};
$('#editToggle').onclick=()=>{editMode=!editMode;editMessage=editMode?'Editing is local to this browser. Select a chart row or table row to change it.':'';render();if(editMode)$('#editName').focus()};$('#closeEditor').onclick=()=>{editMode=false;editMessage='';render()};
$('#undoEdit').onclick=()=>{let change=HISTORY.pop();if(!change)return;let index=DATA.people.findIndex(p=>p.id===change.id);DATA.people[index]=clone(change.before);selected=change.id;editMessage='Undid the last local change to '+change.id+'.';persist();render()};
$('#discardDraft').onclick=()=>{if(!confirm('Restore every person and allocation to the embedded source snapshot and clear local history?'))return;DATA.people=clone(SOURCE_DATA.people);HISTORY=[];selected=SOURCE_DATA.presentation.default_person_id;editMessage='Source snapshot restored; local history cleared.';localStorage.removeItem(KEY);render()};
for(let name of ['chart','table','constraints','options'])$('#'+name+'Tab').onclick=()=>{view=name;setView()};
for(let id of ['search','skill','status'])$('#'+id).addEventListener(id==='search'?'input':'change',render);$('#overloads').onclick=()=>{onlyOver=!onlyOver;$('#overloads').classList.toggle('active',onlyOver);$('#overloads').setAttribute('aria-pressed',String(onlyOver));render()};$('#reset').onclick=()=>{$('#search').value='';$('#skill').value='';$('#status').value='';onlyOver=false;$('#overloads').classList.remove('active');$('#overloads').setAttribute('aria-pressed','false');view='chart';render()};$('#print').onclick=()=>window.print();
$('#fullSvg').href=SOURCE_SVG;$('#fullJson').href='data:application/json;base64,'+btoa(unescape(encodeURIComponent(JSON.stringify(SOURCE_DATA,null,2)+'\n')));$('#fullCsv').href='data:text/csv;base64,'+btoa(unescape(encodeURIComponent(SOURCE_CSV)));$('#draftJson').onclick=()=>download('capacity-plan-local-draft.json',JSON.stringify(draftSnapshot(),null,2)+'\n','application/json');$('#draftCsv').onclick=()=>download('capacity-plan-local-draft.csv',csvText(),'text/csv');$('#visibleCsv').onclick=()=>download('capacity-plan-visible-draft.csv',csvText(visible()),'text/csv');document.addEventListener('keydown',event=>{if(event.key==='Escape'){if(editMode){editMode=false;editMessage='';render()}else $('#reset').click()}});loadDraft();render();
</script></body></html>'''
    replacements = {
        '__TITLE__': esc(data['title']), '__EYEBROW__': esc(data['presentation']['eyebrow']),
        '__HEADLINE__': esc(data['presentation']['headline']), '__LEDE__': esc(data['presentation']['lede']),
        '__METHOD__': esc(data['analysis']['method']), '__SUPPORT__': esc(data['analysis']['support_treatment']),
        '__COMPLETENESS__': esc(data['analysis']['completeness']), '__DECISION__': esc(data['presentation']['decision']),
        '__DATA__': _safe_json(data), '__CSV__': _safe_json(csv_text),
        '__SVG__': _safe_json(_data_uri(svg, 'image/svg+xml')),
    }
    for token, value in replacements.items():
        page = page.replace(token, value)
    return page


def demo():
    return validate({
        'title':'Capacity plan demo', 'version':'1.0', 'as_of':'2026-10-16',
        'source':'Fictional instructional inputs', 'scope':'One planning period and two named people',
        'state':'proposed', 'period':'19–30 October 2026', 'unit':'hours',
        'people':[
            {'id':'OMAR','name':'Omar','role':'Integration engineer','skills':['integration engineering'],
             'gross_hours':80,'leave_hours':8,'overhead_hours':16,'availability_state':'confirmed',
             'availability_source':'Team calendar snapshot C-14','timing_note':'Daily concurrency still requires review.',
             'source':'Fictional capacity record C-14',
             'allocations':[{'id':'A-1','work':'Relay delivery','skill':'integration engineering','window':'19–30 Oct','hours':48,'status':'proposed','source':'Relay estimate E-8','note':''},
                            {'id':'A-2','work':'Support rotation','skill':'production support','window':'19–30 Oct','hours':16,'status':'confirmed','source':'Support rota S-4','note':'Counted as demand, not overhead.'}]},
            {'id':'LENA','name':'Lena','role':'Security engineer','skills':['security assurance'],
             'gross_hours':40,'leave_hours':0,'overhead_hours':8,'availability_state':'confirmed',
             'availability_source':'Team calendar snapshot C-14','timing_note':'No evidence of integration-engineering substitution.',
             'source':'Fictional capacity record C-14',
             'allocations':[{'id':'A-3','work':'Relay security review','skill':'security assurance','window':'19–30 Oct','hours':20,'status':'proposed','source':'Relay estimate E-8','note':''}]}
        ],
        'constraints':[{'id':'C-1','person_id':'OMAR','work':'Relay pilot and support','skill':'integration engineering','window':'19–30 Oct','conflict':'Known demand exceeds modeled availability by 8 hours.','consequence':'Pilot work or support coverage requires an explicit decision.','status':'open','source':'C-14 and E-8'}],
        'options':[{'id':'O-1','label':'Transfer qualified support coverage','hours_timing_changed':'Move 8 support hours from Omar in this period.','skill_basis':'Named competent recipient and matching window required.','effect':'Restores Omar to 56 known demand hours; may load another person.','authority':'Support owner and resource manager','status':'proposed','recalculated_result':'Omar remaining 0 hours if the transfer is approved.','note':'No recipient is assumed.'}],
        'presentation':{'eyebrow':'Capacity decision','headline':'Find the constrained person','lede':'Compare complete demand with realistic availability, then test the skill and timing that the arithmetic cannot prove.','default_person_id':'OMAR','insight_heading':'Aggregate spare hours do not staff a specialist task','insight_points':['Omar is eight hours overloaded.','Lena’s spare hours are a different skill.'],'decision':'Choose an authorized scope, sequence or qualified coverage change for Omar’s eight-hour shortage.'},
        'analysis':{'method':'Known person-level demand compared with gross hours less leave and overhead; unknown demand is not entered as zero.','support_treatment':'Support is an allocation and is not deducted again as overhead.','completeness':'Fictional bounded exercise; other-project allocations would remain unknown until supplied.'},
        'notes':['Fictional instructional data; no staffing commitment is inferred.']})


def main(argv=None):
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', nargs='?')
    parser.add_argument('--demo', action='store_true')
    parser.add_argument('--output', help='Output stem without extension; omit to print SVG')
    args = parser.parse_args(argv)
    if args.demo == bool(args.input):
        parser.error('Provide exactly one input JSON or --demo')
    data = demo() if args.demo else validate(json.loads(Path(args.input).read_text(encoding='utf-8')))
    svg, csv_text = render_svg(data), render_csv(data)
    if not args.output:
        print(svg)
        return 0
    stem = Path(args.output)
    stem.parent.mkdir(parents=True, exist_ok=True)
    Path(str(stem)+'.json').write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    Path(str(stem)+'.svg').write_text(svg, encoding='utf-8')
    Path(str(stem)+'.html').write_text(render_html(data, svg, csv_text), encoding='utf-8')
    Path(str(stem)+'.csv').write_text(csv_text, encoding='utf-8', newline='')
    print('Wrote '+', '.join(str(stem)+suffix for suffix in ('.html','.svg','.json','.csv')))
    return 0


if __name__ == '__main__':
    sys.exit(main())
