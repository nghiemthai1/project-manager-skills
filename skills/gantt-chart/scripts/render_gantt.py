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

"""Render date-only schedule snapshots to offline HTML, SVG, JSON and CSV.

Python 3.11+ standard library. This is a reader, not a scheduling engine.
Intervals are [start, finish); dates and source layers are never rescheduled.
"""
import argparse
import base64
import csv
from datetime import date, timedelta
import html
import io
import json
from pathlib import Path
import re
import sys
import textwrap

LAYERS = ('comparison', 'forecast', 'actual')
COLORS = {'comparison': '#a6b1be', 'forecast': '#007969', 'actual': '#286645'}


def esc(value):
    return html.escape(str(value), quote=True)


def parse_date(value):
    if not isinstance(value, str) or len(value) != 10:
        raise ValueError('Dates must be ISO YYYY-MM-DD, without time or timezone conversion')
    parsed = date.fromisoformat(value)
    if parsed.isoformat() != value:
        raise ValueError('Noncanonical ISO date')
    return parsed


def validate(data):
    if not isinstance(data, dict):
        raise ValueError('Expected a snapshot object')
    for key in ('title', 'as_of', 'source', 'scope', 'version', 'comparison_label'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'{key}: nonempty text required; explicitly state unknown')
    if data.get('date_convention') != '[start, finish)':
        raise ValueError('This helper requires explicit [start, finish) date boundaries')
    if not isinstance(data.get('tasks'), list) or not isinstance(data.get('links'), list):
        raise ValueError('tasks and links must be lists')
    calendar = data.get('calendar', {})
    if not isinstance(calendar, dict):
        raise ValueError('calendar must be an object')
    if not isinstance(calendar.get('label'), str) or not calendar['label']:
        raise ValueError('Calendar label required')
    weekdays = calendar.get('working_weekdays')
    if not isinstance(weekdays, list) or not weekdays or any(type(n) is not int or n not in range(7) for n in weekdays):
        raise ValueError('Calendar working_weekdays needs integers 0=Monday through 6=Sunday')
    if len(set(weekdays)) != len(weekdays):
        raise ValueError('Duplicate working weekday')
    if not isinstance(calendar.get('holidays', []), list):
        raise ValueError('holidays must be a list')
    for day in calendar.get('holidays', []): parse_date(day)
    ids = set()
    for task in data['tasks']:
        if not isinstance(task, dict): raise ValueError('Task must be an object')
        for key in ('id', 'label', 'owner', 'source'):
            if not isinstance(task.get(key), str) or not task[key].strip():
                raise ValueError(f'Task {key} required; explicitly state unknown')
        if task['id'] in ids: raise ValueError('Duplicate task ID: '+task['id'])
        ids.add(task['id'])
        if task.get('kind') not in ('task', 'milestone', 'summary'):
            raise ValueError('kind must be task, milestone or summary')
        if task.get('parent') is not None and not isinstance(task['parent'], str):
            raise ValueError('parent must be a source ID or null')
        for layer in LAYERS:
            span = task.get(layer)
            if span is None: continue
            if not isinstance(span, dict): raise ValueError('Date layer must be object or null')
            for key in ('start', 'finish'):
                if span.get(key) is not None: parse_date(span[key])
            if span.get('start') and span.get('finish'):
                if span['finish'] < span['start']: raise ValueError(task['id']+': inverted interval')
                if task['kind'] == 'milestone' and span['finish'] != span['start']:
                    raise ValueError(task['id']+': milestone dates must coincide')
        progress = task.get('progress')
        if progress is not None:
            if not isinstance(progress, dict) or type(progress.get('percent')) not in (int, float) or not 0 <= progress['percent'] <= 100:
                raise ValueError('Progress must declare percent in 0..100')
            if not all(isinstance(progress.get(k), str) and progress[k].strip() for k in ('meaning', 'source')):
                raise ValueError('Progress needs meaning and evidence source')
    link_ids = set()
    for link in data['links']:
        if not isinstance(link, dict): raise ValueError('Link must be object')
        for key in ('id', 'from', 'to', 'source', 'lag_unit'):
            if not isinstance(link.get(key), str) or not link[key].strip(): raise ValueError('Link '+key+' required')
        if link['id'] in link_ids: raise ValueError('Duplicate link ID')
        link_ids.add(link['id'])
        if link.get('type') not in ('FS', 'SS', 'FF', 'SF'): raise ValueError('Unsupported relationship type')
        if type(link.get('lag')) not in (int, float) or not float('-inf') < link['lag'] < float('inf'):
            raise ValueError('Finite numeric lag required')
        if type(link.get('inferred')) is not bool: raise ValueError('Link inferred must be explicit boolean')
    if not isinstance(data.get('notes', []), list) or any(not isinstance(n, str) for n in data.get('notes', [])):
        raise ValueError('notes must be text entries')
    presentation = data.get('presentation')
    if presentation is not None:
        if not isinstance(presentation, dict):
            raise ValueError('presentation must be an object')
        for key in ('eyebrow', 'headline', 'lede', 'insight_heading', 'decision'):
            if not isinstance(presentation.get(key), str) or not presentation[key].strip():
                raise ValueError('presentation '+key+' must be nonempty text')
        if presentation.get('default_task_id') not in ids:
            raise ValueError('presentation default_task_id must reference a task')
        metrics = presentation.get('metrics')
        if not isinstance(metrics, list) or not metrics:
            raise ValueError('presentation metrics must be a nonempty list')
        for metric in metrics:
            if not isinstance(metric, dict) or any(not isinstance(metric.get(k), str) or not metric[k].strip() for k in ('label', 'value', 'note')):
                raise ValueError('Each presentation metric needs label, value and note')
        points = presentation.get('insight_points')
        if not isinstance(points, list) or any(not isinstance(point, str) or not point.strip() for point in points):
            raise ValueError('presentation insight_points must be text entries')
    analysis = data.get('analysis')
    if analysis is not None:
        if not isinstance(analysis, dict) or not isinstance(analysis.get('method'), str):
            raise ValueError('analysis needs a method string')
        forecast = analysis.get('forecast', {})
        if not isinstance(forecast, dict):
            raise ValueError('analysis forecast must be an object')
        critical = forecast.get('critical_task_ids', [])
        if not isinstance(critical, list) or any(task_id not in ids for task_id in critical):
            raise ValueError('analysis critical_task_ids must reference source tasks')
        facts = forecast.get('tasks', {})
        if not isinstance(facts, dict) or any(task_id not in ids or not isinstance(value, dict) for task_id, value in facts.items()):
            raise ValueError('analysis task facts must reference source tasks')
    return data


def diagnostics(data):
    result = []
    tasks = {t['id']: t for t in data['tasks']}
    for task in tasks.values():
        span = task.get('forecast') or {}
        if not span.get('start') or not span.get('finish'):
            result.append(task['id']+': forecast incomplete; retained without an invented bar')
        if task.get('parent') and task['parent'] not in tasks:
            result.append(task['id']+': parent outside this snapshot')
        for layer in LAYERS:
            pair = task.get(layer) or {}
            if bool(pair.get('start')) != bool(pair.get('finish')):
                result.append(task['id']+': partial '+layer+' interval; inspect source dates in table')
            if task['kind'] != 'milestone' and pair.get('start') and pair.get('start') == pair.get('finish'):
                result.append(task['id']+': zero-length '+layer+' task; not promoted to milestone')
    # Iterative traversal also works on snapshots larger than Python recursion depth.
    def cyclic(edges):
        degree = dict.fromkeys(tasks, 0); successors = {key: [] for key in tasks}
        for a, b in edges:
            if a in tasks and b in tasks: successors[a].append(b); degree[b] += 1
        queue = [key for key, n in degree.items() if n == 0]; seen = 0
        while queue:
            node = queue.pop(); seen += 1
            for child in successors[node]:
                degree[child] -= 1
                if degree[child] == 0: queue.append(child)
        return seen != len(tasks)
    if cyclic([(t['parent'], t['id']) for t in tasks.values() if t.get('parent')]):
        result.append('Hierarchy cycle: display order retained; no rollup calculated')
    if cyclic([(link['from'], link['to']) for link in data['links']]):
        result.append('Dependency cycle: snapshot is not a feasible computed schedule')
    for link in data['links']:
        if link['from'] not in tasks or link['to'] not in tasks:
            result.append(link['id']+': endpoint outside snapshot; link retained in register')
            continue
        a, b = tasks[link['from']].get('forecast') or {}, tasks[link['to']].get('forecast') or {}
        origin = a.get('finish' if link['type'][0] == 'F' else 'start')
        target = b.get('finish' if link['type'][1] == 'F' else 'start')
        if link['inferred']: result.append(link['id']+': relationship is inferred, not confirmed')
        if link['lag'] != 0 and link['lag_unit'] != 'calendar_days':
            result.append(link['id']+': lag retained; timing needs a calendar-aware scheduling engine')
        elif origin and target and (parse_date(target)-parse_date(origin)).days < link['lag']:
            result.append(link['id']+': forecast violates the stated relationship; no dates changed')
    return result


def span_text(task, layer):
    span = task.get(layer) or {}
    return f'{span.get("start") or "unknown"} → {span.get("finish") or "unknown"}'


def detail(task, data):
    parts = [task['id']+' — '+task['label'], 'Owner: '+task['owner'], 'Kind: '+task['kind'],
             'Parent: '+str(task.get('parent') or 'not specified')]
    for layer in LAYERS:
        parts.append((data['comparison_label'] if layer == 'comparison' else layer.title())+': '+span_text(task, layer))
    p = task.get('progress')
    parts += ['Progress: '+(f'{p["percent"]}% {p["meaning"]}; source {p["source"]}' if p else 'unknown'), 'Source: '+task['source']]
    fact = task_fact(data, task)
    parts.append('Working duration: '+workday_text(fact['duration']))
    parts.append('Schedule analysis: '+('critical' if fact['critical'] else ('total float '+str(fact['float'])+' working days' if fact['float'] is not None else 'not supplied')))
    if task.get('note'): parts.append(str(task['note']))
    return ' | '.join(parts)


def svg_text(x, y, value, size=12, color='#24364e', weight='400'):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{color}" font-weight="{weight}">{esc(value)}</text>'


def working_days(start, finish, calendar):
    """Count supplied working dates in a half-open interval; never move dates."""
    if not start or not finish:
        return None
    a, b = parse_date(start), parse_date(finish)
    holidays = set(calendar.get('holidays', []))
    return sum((a+timedelta(days=n)).weekday() in calendar['working_weekdays'] and
               (a+timedelta(days=n)).isoformat() not in holidays for n in range((b-a).days))


def task_fact(data, task):
    supplied = ((data.get('analysis') or {}).get('forecast') or {}).get('tasks', {}).get(task['id'], {})
    span = task.get('forecast') or {}
    duration = supplied.get('duration_working_days')
    if duration is None:
        duration = working_days(span.get('start'), span.get('finish'), data['calendar'])
    critical = task['id'] in ((data.get('analysis') or {}).get('forecast') or {}).get('critical_task_ids', [])
    return {'duration': duration, 'float': supplied.get('total_float_working_days'), 'critical': critical}


def presentation(data):
    if data.get('presentation'):
        return data['presentation']
    dates = [span.get('finish') for task in data['tasks'] for span in [task.get('forecast') or {}] if span.get('finish')]
    finish = max(dates) if dates else 'unknown'
    return {
        'eyebrow': 'SCHEDULE / READ-ONLY SNAPSHOT',
        'headline': data['title'],
        'lede': data['scope'],
        'default_task_id': data['tasks'][0]['id'] if data['tasks'] else '',
        'metrics': [{'label': 'Forecast finish', 'value': finish, 'note': 'Supplied finish boundary'}],
        'insight_heading': 'Review the supplied network.',
        'insight_points': ['The renderer preserves supplied dates and dependencies without rescheduling them.'],
        'decision': 'Validate the schedule assumptions and source authority before commitment.'
    }


def short_date(value):
    return parse_date(value).strftime('%d %b').lstrip('0') if value else 'unknown'


def workday_text(value):
    if value is None:
        return 'unknown'
    display = f'{value:g}' if isinstance(value, (int, float)) else str(value)
    return display+' working day'+('' if value == 1 else 's')


def render_svg(data):
    dates = [parse_date(span[key]) for task in data['tasks'] for layer in LAYERS
             for span in [task.get(layer) or {}] for key in ('start', 'finish') if span.get(key)]
    first = min(dates) if dates else date(2000, 1, 1)
    last = max(dates) if dates else first
    days = max(1, (last-first).days)
    width, left, right = 1440, 350, 1408
    header, axis_height, row_height = 236, 62, 84
    row_top = header+axis_height
    row_count = max(1, len(data['tasks']))
    chart_bottom = row_top+row_count*row_height
    p = presentation(data)
    notes = [((data.get('analysis') or {}).get('method') or 'No schedule analysis supplied.')]
    notes.extend(data.get('notes', []))
    notes.extend(diagnostics(data))
    note_lines = [line for note in notes for line in textwrap.wrap(note, 170)]
    height = chart_bottom+56+len(note_lines)*18
    x = lambda value: left+(parse_date(value)-first).days/days*(right-left)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
             f'<title id="title">{esc(p["headline"])}</title>',
             '<desc id="desc">Read-only Gantt snapshot with a task grid, date axis, supplied schedule layers, milestones, dependencies, analysis notes and source caveats.</desc>',
             '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="none" stroke="#657b76"/></marker></defs>',
             '<rect width="100%" height="100%" fill="#f4f5f0"/>',
             '<g font-family="Arial,sans-serif" fill="#182c36">']
    parts.append(svg_text(24, 30, p['eyebrow'], 11, '#007969', '700'))
    parts.append(svg_text(1416, 30, f'{data["version"]} · {data["as_of"]}', 11, '#576a74', '400').replace('text x="1416.0"', 'text x="1416.0" text-anchor="end"'))
    parts.append(svg_text(24, 74, p['headline'], 30, '#182c36', '700'))
    lede_lines = textwrap.wrap(p['lede'], 140)[:2]
    for i, line in enumerate(lede_lines):
        parts.append(svg_text(24, 104+i*19, line, 13, '#576a74'))
    metrics = p['metrics'][:3]
    metric_y, metric_h = 145, 72
    metric_w = (width-48)/max(1, len(metrics))
    for i, metric in enumerate(metrics):
        mx = 24+i*metric_w
        tone = '#b44330' if metric.get('tone') == 'risk' else '#182c36'
        parts.append(f'<rect x="{mx:.1f}" y="{metric_y}" width="{metric_w-1:.1f}" height="{metric_h}" fill="#ffffff" stroke="#dce3df"/>')
        parts.append(svg_text(mx+16, metric_y+20, metric['label'].upper(), 10, '#576a74', '700'))
        parts.append(svg_text(mx+16, metric_y+46, metric['value'], 22, tone, '700'))
        parts.append(svg_text(mx+160, metric_y+45, textwrap.shorten(metric['note'], 52, placeholder='…'), 10, '#576a74'))
    parts.append(f'<rect x="24" y="{header}" width="{width-48}" height="{chart_bottom-header}" rx="10" fill="#ffffff" stroke="#dce3df"/>')
    parts.append(f'<rect x="24" y="{header}" width="326" height="{chart_bottom-header}" rx="10" fill="#fbfcf9"/>')
    parts.append(svg_text(43, header+25, 'TASK / WORKING DURATION', 10, '#576a74', '700'))
    if dates:
        cell = (right-left)/days
        if days <= 120:
            holidays = set(data['calendar'].get('holidays', []))
            for offset in range(days):
                day = first+timedelta(days=offset)
                if day.weekday() not in data['calendar']['working_weekdays'] or day.isoformat() in holidays:
                    parts.append(f'<rect x="{left+offset*cell:.1f}" y="{header}" width="{cell:.1f}" height="{chart_bottom-header}" fill="#f0f3ef"/>')
        step = max(1, (days+13)//14)
        for offset in sorted(set(range(0, days+1, step)) | {days}):
            day = first+timedelta(days=offset)
            xpos = left+offset*cell
            parts.append(f'<path d="M{xpos:.1f},{header} V{chart_bottom}" stroke="#e1e7e2"/>')
            if offset < days or offset == 0:
                parts.append(svg_text(xpos+7, header+22, day.strftime('%a').upper(), 9, '#6a7b74', '700'))
                parts.append(svg_text(xpos+7, header+43, day.strftime('%d %b').lstrip('0'), 12, '#182c36'))
    else:
        parts.append(svg_text(left+18, header+36, 'No dated intervals — no date axis inferred', 12, '#845408'))
    centers = {task['id']: row_top+i*row_height+row_height/2 for i, task in enumerate(data['tasks'])}
    tasks = {task['id']: task for task in data['tasks']}
    for link in data['links']:
        if link['from'] not in tasks or link['to'] not in tasks or link['from'] not in centers or link['to'] not in centers:
            continue
        source_span, target_span = tasks[link['from']].get('forecast') or {}, tasks[link['to']].get('forecast') or {}
        origin = source_span.get('finish' if link['type'][0] == 'F' else 'start')
        target = target_span.get('finish' if link['type'][1] == 'F' else 'start')
        if not origin or not target:
            continue
        sx, tx = x(origin), x(target)
        sy, ty = centers[link['from']]+7, centers[link['to']]+7
        elbow = min(right-5, max(sx, tx)+12)
        parts.append(f'<path class="dependency" d="M{sx:.1f},{sy:.1f} H{elbow:.1f} V{ty:.1f} H{tx:.1f}" fill="none" stroke="#657b76" stroke-width="1.2" opacity=".7" marker-end="url(#arrow)"><title>{esc(link["id"]+" · "+link["type"])}</title></path>')
    if not data['tasks']:
        parts.append(svg_text(43, row_top+47, 'No rows in this snapshot.', 13, '#576a74'))
    for i, task in enumerate(data['tasks']):
        y = row_top+i*row_height
        center = centers[task['id']]
        fact = task_fact(data, task)
        parts.append(f'<g data-task="{esc(task["id"])}" data-critical="{str(fact["critical"]).lower()}">')
        parts.append(f'<path d="M24,{y+row_height} H1416" stroke="#e1e7e2"/>')
        parts.append(svg_text(43, y+29, task['id']+' / '+textwrap.shorten(task['label'], 38, placeholder='…'), 13, '#182c36', '700'))
        duration = 'duration unknown' if fact['duration'] is None else workday_text(fact['duration'])
        status = 'critical' if fact['critical'] else (f'{fact["float"]} days total float' if fact['float'] is not None else 'criticality not supplied')
        parts.append(svg_text(43, y+53, duration+' · '+status, 10, '#576a74'))
        parts.append(svg_text(43, y+69, 'Owner: '+textwrap.shorten(task['owner'], 43, placeholder='…'), 9, '#72817b'))
        for layer, dy, thickness in [('comparison', -11, 7), ('forecast', 8, 14), ('actual', 27, 8)]:
            span = task.get(layer) or {}
            if not span.get('start') or not span.get('finish'):
                continue
            a, b = x(span['start']), x(span['finish'])
            classes = layer+(' critical' if layer == 'forecast' and fact['critical'] else '')
            if task['kind'] == 'milestone':
                parts.append(f'<path class="{classes}" d="M{a:.1f},{center+dy-7:.1f} l7,7 -7,7 -7,-7 Z" fill="{COLORS[layer]}"/>')
            else:
                parts.append(f'<rect class="{classes}" x="{a:.1f}" y="{center+dy-thickness/2:.1f}" width="{max(2,b-a):.1f}" height="{thickness}" rx="3" fill="{COLORS[layer]}"/>')
        forecast = task.get('forecast') or {}
        if forecast.get('start') and forecast.get('finish'):
            label_x = min(max(x(forecast['start']), left+4), right-115)
            label = short_date(forecast['start'])+' → '+short_date(forecast['finish'])
            parts.append(svg_text(label_x, y+76, label, 9, '#3e5951'))
        else:
            parts.append(svg_text(left+12, y+47, 'Forecast incomplete — retained in source table', 11, '#845408'))
        parts.append('</g>')
    note_y = chart_bottom+28
    parts.append(svg_text(24, note_y, 'READING NOTES / SOURCE BOUNDARIES', 10, '#007969', '700'))
    note_y += 23
    for line in note_lines:
        parts.append(svg_text(24, note_y, line, 10, '#576a74'))
        note_y += 18
    parts.append('</g></svg>')
    return '\n'.join(parts)


def render_csv(data):
    out=io.StringIO(newline='');writer=csv.writer(out)
    writer.writerow(['id','label','kind','parent','owner','layer','start','finish','source'])
    for task in data['tasks']:
        for layer in LAYERS:
            span=task.get(layer) or {}
            values=[task['id'],task['label'],task['kind'],task.get('parent') or '',task['owner'],data['comparison_label'] if layer=='comparison' else layer,span.get('start') or '',span.get('finish') or '',task['source']]
            writer.writerow(["'"+v if v.startswith(('=','+','-','@','\t','\r')) else v for v in values])
    return out.getvalue()


def render_html(data, svg, csv_text):
    tasks = data['tasks']; ds = diagnostics(data); p = presentation(data)
    owners = sorted({task['owner'] for task in tasks})
    options = ''.join(f'<option>{esc(owner)}</option>' for owner in owners)
    dates = [parse_date(span[key]) for task in tasks for layer in LAYERS
             for span in [task.get(layer) or {}] for key in ('start', 'finish') if span.get(key)]
    first = min(dates) if dates else date(2000, 1, 1)
    last = max(dates) if dates else first
    total_days = max(1, (last-first).days)
    def pct(value): return max(0, min(100, (parse_date(value)-first).days/total_days*100))
    def mini_bar(task, layer, class_name):
        span = task.get(layer) or {}
        if not span.get('start') or not span.get('finish'): return ''
        start, finish = pct(span['start']), pct(span['finish'])
        if task['kind'] == 'milestone':
            return f'<i class="mini-milestone {class_name}" style="left:{start:.2f}%"></i>'
        return f'<i class="mini-bar {class_name}" style="left:{start:.2f}%;width:{max(1,finish-start):.2f}%"></i>'
    labels = ''
    cards = ''
    rows = ''
    for task in tasks:
        fact = task_fact(data, task)
        duration = 'duration unknown' if fact['duration'] is None else workday_text(fact['duration'])
        status = 'critical' if fact['critical'] else (f'{fact["float"]} days total float' if fact['float'] is not None else 'criticality not supplied')
        attrs = f'data-row="{esc(task["id"])}" data-owner="{esc(task["owner"])}" data-search="{esc(detail(task,data).lower())}"'
        button = f'<button data-detail="{esc(detail(task,data))}" data-task-id="{esc(task["id"])}"><strong>{esc(task["id"]+" / "+task["label"])}</strong><small>{esc(duration+" · "+status)}</small></button>'
        labels += f'<div class="task-label" {attrs}>{button}</div>'
        cards += (f'<article {attrs}><div class="card-head">{button}<span class="pill">{esc(status)}</span></div>'
                  f'<p>Forecast {esc(span_text(task,"forecast"))}</p><div class="mini">{mini_bar(task,"comparison","comparison")}{mini_bar(task,"forecast","forecast")}</div>'
                  f'<div class="mini-axis"><span>{esc(short_date(first.isoformat()))}</span><span>{esc(short_date(last.isoformat()))}</span></div>'
                  f'<p>{esc(duration)} · Owner: {esc(task["owner"])}</p></article>')
        rows += (f'<tr {attrs}><th scope="row">{button}</th><td>{esc(task["owner"])}</td>'+
                 ''.join(f'<td>{esc(span_text(task,layer))}</td>' for layer in LAYERS)+
                 f'<td>{esc(task["source"])}</td></tr>')
    def uri(body, mime): return 'data:'+mime+';base64,'+base64.b64encode(body.encode()).decode()
    exports = ' '.join(f'<a class="download" download="gantt.{ext}" href="{uri(body,mime)}">{label}</a>' for ext, body, mime, label in [
        ('svg', svg, 'image/svg+xml', 'Download full SVG'),
        ('json', json.dumps(data, ensure_ascii=False, indent=2)+'\n', 'application/json', 'Editable schedule JSON'),
        ('csv', csv_text, 'text/csv', 'All date layers CSV')])
    findings = ''.join('<li>'+esc(item)+'</li>' for item in ds) or '<li>No supported structural or timing violations found. Resource feasibility and authority are not computed.</li>'
    links = ''.join('<li>'+esc(f'{link["id"]}: {link["from"]} → {link["to"]}, {link["type"]}, {link["lag"]:+g} {link["lag_unit"]}; inferred: {link["inferred"]}; source: {link["source"]}')+'</li>' for link in data['links']) or '<li>No links supplied; this does not prove independence.</li>'
    notes = ''.join('<li>'+esc(note)+'</li>' for note in data.get('notes', []))
    metrics = ''.join(f'<div class="metric {"risk" if metric.get("tone")=="risk" else ""}"><span>{esc(metric["label"])}</span><strong>{esc(metric["value"])}</strong><small>{esc(metric["note"])}</small></div>' for metric in p['metrics'])
    insight_points = ''.join('<li>'+esc(point)+'</li>' for point in p['insight_points'])
    default = next((task for task in tasks if task['id'] == p['default_task_id']), tasks[0] if tasks else None)
    initial_detail = detail(default, data) if default else 'No task is available in this snapshot.'
    chart_range = short_date(first.isoformat())+' – '+short_date(last.isoformat()) if dates else 'No dated range'
    compact_height = 62+max(1, len(tasks))*84
    chart_svg = re.sub(
        r'width="1440" height="\d+" viewBox="0 0 1440 \d+"',
        f'width="1058" height="{compact_height}" viewBox="350 236 1058 {compact_height}"',
        svg,
        count=1,
    )
    html_data = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
    return '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+esc(data['title'])+'''</title><style>
:root{--ink:#182c36;--muted:#576a74;--paper:#f4f5f0;--line:#dce3df;--teal:#007969;--red:#b44330;--gray:#a6b1be;font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;color:var(--ink);background:var(--paper)}*{box-sizing:border-box}body{margin:0}main{max-width:1480px;margin:auto;padding:32px}h1{font-size:clamp(28px,3vw,42px);font-weight:650;letter-spacing:-1.4px;line-height:1.14;margin:12px 0}h2{font-size:20px;margin:0}p{margin:8px 0}.eyebrow{font-size:11px;letter-spacing:2px;font-weight:750;color:var(--teal)}.topline{display:flex;justify-content:space-between;gap:16px}.stamp{font-size:12px;color:var(--muted);text-align:right}.lede{color:var(--muted);max-width:820px}.summary{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:12px;overflow:hidden;margin:24px 0}.metric{padding:18px 24px;background:#fff}.metric span,.metric small{display:block;color:var(--muted);font-size:12px}.metric strong{display:block;font-size:29px;font-weight:650;letter-spacing:-1px}.metric.risk strong{color:var(--red)}.panel{border:1px solid var(--line);border-radius:14px;background:#fff;overflow:hidden}.panel-head{padding:20px 24px 10px;display:flex;align-items:center;justify-content:space-between;gap:16px}.legend{display:flex;gap:18px;flex-wrap:wrap;font-size:12px;color:var(--muted)}.legend i{display:inline-block;width:18px;height:7px;vertical-align:middle;margin-right:7px;border-radius:2px}.toolbar{padding:10px 24px 16px;display:flex;gap:10px;align-items:end;flex-wrap:wrap}.toolbar label{display:grid;gap:3px;font-size:11px;color:var(--muted)}.toolbar .search{margin-right:auto}.toolbar input[type=search]{width:220px}button,input,select,summary,.download{font:inherit}button,select,input,.download{min-height:44px;border:1px solid #becdc6;border-radius:7px;background:#fff;padding:9px 12px;color:var(--ink)}button{cursor:pointer}button:hover,.download:hover{background:#eef5f0}button:focus-visible,input:focus-visible,select:focus-visible,a:focus-visible,summary:focus-visible{outline:3px solid var(--teal);outline-offset:3px}.chart-grid{display:grid;grid-template-columns:270px minmax(0,1fr);border-top:1px solid var(--line)}.labels{z-index:2;border-right:1px solid var(--line);background:#fff}.grid-head{height:64px;display:flex;align-items:center;padding:0 20px;font-size:10px;letter-spacing:1px;color:var(--muted)}.task-label{height:84px;border-top:1px solid var(--line)}.task-label button{width:100%;height:100%;border:0;border-radius:0;text-align:left;padding:12px 20px}.task-label button strong,.task-label button small{display:block}.task-label button small{font-size:11px;color:var(--muted);margin-top:4px}.task-label.selected button{background:#eaf4ef;box-shadow:inset 4px 0 var(--teal)}.scroll{overflow:auto;overscroll-behavior-x:contain}.chart{border:0;max-height:none}.chart svg{display:block;width:100%;min-width:820px;height:auto}.chart .comparison{transition:opacity .15s}.chart.no-comparison .comparison{display:none}.chart.no-dependencies .dependency{display:none}.chart.show-critical [data-task="true"]{}.chart.show-critical [data-critical="false"] .forecast{opacity:.28}.chart.show-critical .forecast.critical{fill:var(--red)!important}.chart .is-dim{opacity:.18}.chart .is-selected{filter:drop-shadow(0 0 3px rgba(0,121,105,.65))}.chart-foot{padding:12px 24px;display:flex;justify-content:space-between;gap:12px;color:var(--muted);font-size:12px;background:#fafbf8;border-top:1px solid var(--line)}.below{display:grid;grid-template-columns:1.15fr 1fr;gap:20px;margin-top:20px}.detail,.insight{padding:22px 24px;border:1px solid var(--line);border-radius:12px;background:#fff}.detail{border-top:4px solid var(--teal)}.insight{background:#eaf2ed}.detail h2,.insight h2{font-size:17px;margin-top:4px}.detail p{overflow-wrap:anywhere}.insight li{margin:8px 0}.insight ol{padding-left:20px}.pill{font-size:10px;padding:4px 7px;background:#eef3ef;color:#315247;border-radius:12px;white-space:nowrap}.exports{display:flex;gap:10px;flex-wrap:wrap;margin:20px 0}.download{text-decoration:none;font-size:13px}.notes{font-size:12px;color:var(--muted);max-width:1100px}details{margin-top:18px}summary{cursor:pointer;min-height:44px;padding:10px 0;font-weight:650}.table-wrap{overflow:auto;border:1px solid var(--line);background:#fff}table{border-collapse:collapse;width:100%;min-width:1080px;font-size:12px}th,td{text-align:left;padding:10px;border-bottom:1px solid var(--line);vertical-align:top}thead th{position:sticky;top:0;background:#eaf0ec;z-index:2}tbody th{position:sticky;left:0;background:#fff;z-index:1;min-width:250px}tbody th button{border:0;width:100%;text-align:left;padding:0}tbody th button strong,tbody th button small{display:block}tbody th button small{color:var(--muted);font-size:10px}.mobile{display:none}.mobile article{padding:16px;border-top:1px solid var(--line)}.mobile article.selected{background:#edf5ef}.card-head{display:flex;justify-content:space-between;gap:10px}.card-head button{border:0;padding:0;min-height:44px;text-align:left;flex:1}.card-head button strong,.card-head button small{display:block}.card-head button small{color:var(--muted);font-size:11px}.mobile article p{font-size:11px;color:var(--muted)}.mini{position:relative;height:30px;margin:9px 0;background:linear-gradient(to right,#fff 42%,#eef1ed 42%,#eef1ed 58%,#fff 58%);border:1px solid var(--line)}.mini-bar{position:absolute;height:6px;top:5px;background:var(--gray);border-radius:2px}.mini-bar.forecast{height:9px;top:16px;background:var(--teal)}.mini-milestone{position:absolute;width:9px;height:9px;transform:rotate(45deg);top:4px;background:var(--gray)}.mini-milestone.forecast{top:16px;background:var(--teal)}.mini-axis{display:flex;justify-content:space-between;font-size:10px;color:var(--muted)}[hidden]{display:none!important}
@media(max-width:700px) and (orientation:portrait){main{padding:18px 14px}.stamp{max-width:145px}.summary{margin:18px 0}.metric{padding:12px 10px}.metric strong{font-size:22px}.metric span,.metric small{font-size:10px}.panel-head{padding:15px;display:block}.legend{margin-top:9px;gap:10px;font-size:10px}.toolbar{padding:6px 15px 12px}.toolbar label{width:100%}.toolbar input[type=search]{width:100%}.toolbar .desktop-control{display:none}.chart-grid{display:none}.mobile{display:block}.below{grid-template-columns:1fr}.chart-foot{padding:12px 15px}.detail,.insight{padding:18px}.lede{font-size:13px}.topline{align-items:start}.desktop-table{display:none}}
@media(max-height:500px) and (orientation:landscape){main{padding:18px}.summary{margin:12px 0}.metric{padding:10px 18px}.chart-grid{grid-template-columns:220px minmax(0,1fr)}}
@media print{body{background:#fff}main{padding:0}.toolbar,.exports{display:none}.scroll{overflow:visible}.chart svg{min-width:0}.chart-grid{grid-template-columns:240px minmax(0,1fr)}.panel,.below{break-inside:avoid}.mobile{display:none}thead th,tbody th{position:static}}
</style></head><body><main><div class="topline"><span class="eyebrow">'''+esc(p['eyebrow'])+'''</span><span class="stamp">'''+esc(data['version'])+''' · '''+esc(data['as_of'])+'''<br>Read-only schedule snapshot</span></div><h1>'''+esc(p['headline'])+'''</h1><p class="lede">'''+esc(p['lede'])+'''</p><section class="summary" aria-label="Schedule summary">'''+metrics+'''</section><section class="panel" aria-label="Schedule explorer"><div class="panel-head"><h2>'''+esc(data['title'])+'''</h2><div class="legend"><span><i style="background:#a6b1be"></i>'''+esc(data['comparison_label'])+'''</span><span><i style="background:#007969"></i>Forecast</span><span>◆ Milestone</span></div></div><div class="toolbar"><label class="search">Find task, ID, owner, or source<input id="search" type="search" placeholder="Search the schedule"></label><label>Owner<select id="owner"><option value="">All owners</option>'''+options+'''</select></label><label class="desktop-control">Scale<select id="zoom"><option value="100">Fit</option><option value="150">150%</option><option value="200">200%</option></select></label><label class="desktop-control">Comparison<select id="comparison"><option value="show">Shown</option><option value="hide">Hidden</option></select></label><label class="desktop-control">Dependencies<select id="dependencies"><option value="show">Shown</option><option value="hide">Hidden</option></select></label><label class="desktop-control">Critical path<select id="critical"><option value="standard">Standard</option><option value="highlight">Highlight</option></select></label><button id="reset">Reset view</button></div><div class="chart-grid"><div class="labels"><div class="grid-head">TASK / WORKING DURATION</div>'''+labels+'''</div><div class="timeline scroll" tabindex="0" aria-label="Schedule timeline; scroll horizontally when zoomed"><div class="chart">'''+chart_svg+'''</div></div></div><div class="mobile">'''+cards+'''</div><div class="chart-foot"><span id="scope" aria-live="polite"></span><span>'''+esc(chart_range)+'''</span></div></section><div class="below"><section class="detail" aria-live="polite"><span class="eyebrow">SELECTED TASK</span><h2>Task evidence</h2><p id="detail-text">'''+esc(initial_detail)+'''</p></section><section class="insight"><span class="eyebrow">WHAT THE NETWORK TELLS US</span><h2>'''+esc(p['insight_heading'])+'''</h2><ol>'''+insight_points+'''</ol><p>'''+esc(p['decision'])+'''</p></section></div><div class="exports">'''+exports+'''</div><p class="notes"><strong>Reading this chart.</strong> Dates use [start, finish): the finish boundary is excluded. '''+esc(data['calendar']['label'])+'''. Gray comparison marks do not establish baseline approval. Diamonds mark events, not acceptance evidence. Unknown dates, owners, and progress remain explicit.</p><details><summary>Exact dates and source table</summary><div class="table-wrap desktop-table"><table><caption>Complete source task data; filters never alter downloads</caption><thead><tr><th>Task</th><th>Owner</th><th>'''+esc(data['comparison_label'])+'''</th><th>Forecast</th><th>Actual</th><th>Source</th></tr></thead><tbody>'''+rows+'''</tbody></table></div></details><details><summary>Analysis method, diagnostics, dependencies, and caveats</summary><p class="notes"><strong>Analysis method:</strong> '''+esc(((data.get('analysis') or {}).get('method') or 'No schedule analysis supplied.'))+'''</p><h3>Diagnostics</h3><ul>'''+findings+'''</ul><h3>Dependency register</h3><ul>'''+links+'''</ul><h3>Source caveats</h3><ul>'''+notes+'''</ul><p class="notes">Source: '''+esc(data['source'])+''' · Scope: '''+esc(data['scope'])+'''</p></details><noscript>JavaScript is needed only for controls. The source table, timeline, and complete downloads remain available.</noscript></main><script>
const data='''+html_data+''';const search=document.getElementById('search'),owner=document.getElementById('owner'),zoom=document.getElementById('zoom'),comparison=document.getElementById('comparison'),dependencies=document.getElementById('dependencies'),critical=document.getElementById('critical'),chart=document.querySelector('.chart');let selected='''+json.dumps(p['default_task_id'])+''';
function matches(task){const q=search.value.toLocaleLowerCase();return (!q||task.dataset.search.includes(q))&&(!owner.value||task.dataset.owner===owner.value)}
function choose(button){selected=button.dataset.taskId;document.getElementById('detail-text').textContent=button.dataset.detail;document.querySelectorAll('[data-task-id]').forEach(item=>item.closest('[data-row]')?.classList.toggle('selected',item.dataset.taskId===selected));document.querySelectorAll('svg [data-task]').forEach(group=>group.classList.toggle('is-selected',group.dataset.task===selected))}
function update(){const visibleIds=new Set();document.querySelectorAll('[data-row]').forEach(item=>{const yes=matches(item);item.hidden=!yes;if(yes)visibleIds.add(item.dataset.row)});document.querySelectorAll('svg [data-task]').forEach(group=>group.classList.toggle('is-dim',!visibleIds.has(group.dataset.task)));document.getElementById('scope').textContent=visibleIds.size+' / '''+str(len(tasks))+''' source rows shown · full network retained in exports'}
function display(){chart.querySelector('svg').style.width=zoom.value+'%';chart.classList.toggle('no-comparison',comparison.value==='hide');chart.classList.toggle('no-dependencies',dependencies.value==='hide');chart.classList.toggle('show-critical',critical.value==='highlight')}
[search,owner].forEach(control=>control.addEventListener('input',update));[zoom,comparison,dependencies,critical].forEach(control=>control.addEventListener('input',display));document.querySelectorAll('[data-detail]').forEach(button=>button.addEventListener('click',()=>choose(button)));document.querySelectorAll('.task-label [data-detail]').forEach(button=>button.addEventListener('keydown',event=>{if(!['ArrowUp','ArrowDown'].includes(event.key))return;event.preventDefault();const list=[...document.querySelectorAll('.task-label:not([hidden]) [data-detail]')],index=list.indexOf(button),next=list[Math.max(0,Math.min(list.length-1,index+(event.key==='ArrowDown'?1:-1)))];next?.focus()}));document.getElementById('reset').addEventListener('click',()=>{search.value='';owner.value='';zoom.value='100';comparison.value='show';dependencies.value='show';critical.value='standard';update();display();search.focus()});update();display();const initial=[...document.querySelectorAll('[data-task-id]')].find(button=>button.dataset.taskId===selected);if(initial)choose(initial);
</script></body></html>'''


def demo():
    return {'title':'Fictional schedule demonstration', 'as_of':'2026-10-05', 'version':'draft-1', 'source':'Built-in fictional teaching example', 'scope':'One task and one unscheduled checkpoint; no approved commitment', 'comparison_label':'Original planning scenario', 'date_convention':'[start, finish)', 'calendar':{'label':'Monday–Friday, no holidays assumed', 'working_weekdays':[0,1,2,3,4], 'holidays':[]}, 'tasks':[{'id':'T-1','label':'Prepare evidence','kind':'task','owner':'Unknown','source':'Fictional input','forecast':{'start':'2026-10-05','finish':'2026-10-07'}, 'comparison':{'start':'2026-10-05','finish':'2026-10-06'}},{'id':'G-1','label':'Acceptance decision','kind':'milestone','owner':'Unknown','source':'Fictional input','forecast':None}], 'links':[{'id':'L-1','from':'T-1','to':'G-1','type':'FS','lag':0,'lag_unit':'calendar_days','source':'Fictional input','inferred':False}], 'notes':['Rendering this event does not approve the decision.']}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('input',nargs='?',type=Path);parser.add_argument('--output',type=Path,help='Writes .html/.svg/.json/.csv using this filename stem');parser.add_argument('--demo',action='store_true');args=parser.parse_args()
    try:
        if args.demo == bool(args.input): raise ValueError('Choose input JSON or --demo')
        data=validate(demo() if args.demo else json.loads(args.input.read_text(encoding='utf-8')))
        svg=render_svg(data);csv_text=render_csv(data)
        if args.output:
            args.output.parent.mkdir(parents=True,exist_ok=True)
            outputs={'.svg':svg,'.html':render_html(data,svg,csv_text),'.json':json.dumps(data,ensure_ascii=False,indent=2)+'\n','.csv':csv_text}
            for suffix,body in outputs.items(): Path(str(args.output)+suffix).write_text(body,encoding='utf-8',newline='')
            print(json.dumps({'files':[str(args.output)+suffix for suffix in outputs], 'diagnostics':diagnostics(data)},ensure_ascii=False))
        else: print(svg)
        return 0
    except (OSError,ValueError,TypeError,KeyError) as exc:
        print('Input error: '+str(exc),file=sys.stderr);return 2


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    raise SystemExit(main())
