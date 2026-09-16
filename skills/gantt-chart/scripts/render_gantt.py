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
import sys
import textwrap

LAYERS = ('comparison', 'forecast', 'actual')
COLORS = {'comparison': '#7d8ca4', 'forecast': '#176c91', 'actual': '#286645'}


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
    if task.get('note'): parts.append(str(task['note']))
    return ' | '.join(parts)


def svg_text(x, y, value, size=12, color='#24364e', weight='400'):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{color}" font-weight="{weight}">{esc(value)}</text>'


def render_svg(data):
    dates = [parse_date(span[k]) for task in data['tasks'] for layer in LAYERS
             for span in [task.get(layer) or {}] for k in ('start', 'finish') if span.get(k)]
    first = min(dates) if dates else date(2000, 1, 1)
    last = max(dates) if dates else first
    days = max(1, (last-first).days)
    width, left, right = 1420, 410, 1380
    x = lambda day: left+(parse_date(day)-first).days/days*(right-left)
    lines = []
    for text in [data['title'], f'{data["version"]} · As of {data["as_of"]}', data['scope'],
                 'Source: '+data['source'], 'Calendar: '+data['calendar']['label']+' · [start, finish); finish is excluded',
                 'Gray: '+data['comparison_label']+' · Blue: forecast · Green: actual · Diamond: event, not acceptance']:
        lines.extend(textwrap.wrap(text, 150))
    top = 32+len(lines)*21+58
    row_heights = [max(105, 32+len(textwrap.wrap(t['id']+' · '+t['label'], 43))*17
                       +len(textwrap.wrap('Owner: '+t['owner'],43))*14) for t in data['tasks']]
    bottom = top+sum(row_heights)
    notes = list(data.get('notes', []))+diagnostics(data)
    notes += [f'{link["id"]}: {link["from"]} → {link["to"]} {link["type"]} {link["lag"]:+g} {link["lag_unit"]}; '+('inferred; ' if link['inferred'] else '')+'source '+link['source'] for link in data['links']]
    notes += ['No rows in this snapshot.'] if not data['tasks'] else []
    note_lines = [line for note in notes for line in textwrap.wrap(note, 170)]
    height = bottom+55+len(note_lines)*18
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
             f'<title id="title">{esc(data["title"])}</title><desc id="desc">Read-only schedule snapshot. Every source task is retained. Exact dates, ownership and sources are in the companion HTML and JSON.</desc>',
             '<defs><marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6" fill="none" stroke="#5d4a78"/></marker></defs>',
             f'<rect width="{width}" height="{height}" fill="#f7f9fc"/><g font-family="Arial,sans-serif">']
    y = 29
    for i, line in enumerate(lines): parts.append(svg_text(24,y,line,16 if i == 0 else 12,weight='700' if i == 0 else '400')); y += 21
    parts.append(svg_text(24,top-18,'TASK / SOURCE ID / OWNER',12,weight='700'))
    if dates:
        # Bounded tick work. Daily grids are useful only at short ranges.
        step = max(1, (days+15)//16)
        if days <= 120:
            for offset in range(days):
                day = first+timedelta(days=offset)
                if day.weekday() not in data['calendar']['working_weekdays'] or day.isoformat() in data['calendar'].get('holidays', []):
                    parts.append(f'<rect x="{x(day.isoformat()):.1f}" y="{top-8}" width="{(right-left)/days:.1f}" height="{bottom-top+8}" fill="#e8edf4"/>')
        for offset in sorted(set(range(0,days+1,step)) | {days}):
            day = first+timedelta(days=offset); xpos=x(day.isoformat())
            parts.append(f'<path d="M{xpos:.1f},{top-8} V{bottom}" stroke="#cdd7e4"/>')
            # Two endpoint labels near each other are avoided by the step rule below.
            if offset != days or days % step == 0 or days % step >= step/2:
                parts.append(svg_text(xpos-19,top-19,day.strftime('%d %b'),11))
        if days > 120: parts.append(svg_text(left,top-38,'Long range: non-working-day shading omitted; source calendar retained',11))
    else: parts.append(svg_text(left,top-18,'No dated intervals — no date axis inferred',12))
    centers = {}; y = top
    for task, rh in zip(data['tasks'], row_heights):
        centers[task['id']] = y+56
        parts.append(f'<g data-task="{esc(task["id"])}"><path d="M20,{y+rh} H1400" stroke="#d6deea"/>')
        for i,line in enumerate(textwrap.wrap(task['id']+' · '+task['label'],43)):
            parts.append(svg_text(25,y+19+i*17,line,12,weight='600'))
        owner_y=y+23+len(textwrap.wrap(task['id']+' · '+task['label'],43))*17
        for i,line in enumerate(textwrap.wrap('Owner: '+task['owner'],43)):
            parts.append(svg_text(25,owner_y+i*14,line,11))
        for n,layer in enumerate(LAYERS):
            span=task.get(layer) or {}; sy=y+16+n*27
            if not span.get('start') or not span.get('finish'): continue
            a,b=x(span['start']),x(span['finish']);color=COLORS[layer]
            if task['kind']=='milestone':
                parts.append(f'<path class="{layer}" d="M{a:.1f},{sy-5} l6,6 -6,6 -6,-6 Z" fill="{color}"/>')
            else:
                parts.append(f'<rect class="{layer}" x="{a:.1f}" y="{sy-3}" width="{max(1,b-a):.1f}" height="9" rx="2" fill="{color}"/>')
            label=span['start'][5:]+' → '+span['finish'][5:]
            label_x=max(left,min(a,right-110))
            parts.append(svg_text(label_x,sy+18,label,10,color))
        if not (task.get('forecast') or {}).get('start') or not (task.get('forecast') or {}).get('finish'):
            parts.append(svg_text(left,y+48,'Forecast incomplete — retained in source table',12,'#845408'))
        parts.append('</g>'); y+=rh
    tasks={t['id']:t for t in data['tasks']}
    for link in data['links']:
        if link['from'] not in tasks or link['to'] not in tasks: continue
        a=tasks[link['from']].get('forecast') or {}; b=tasks[link['to']].get('forecast') or {}
        origin=a.get('finish' if link['type'][0]=='F' else 'start');target=b.get('finish' if link['type'][1]=='F' else 'start')
        if not origin or not target: continue
        sx,tx=x(origin),x(target); sy=centers[link['from']]-13;ty=centers[link['to']]-13
        elbow=min(right+12,max(sx,tx)+10)
        parts.append(f'<path class="dependency" d="M{sx:.1f},{sy} H{elbow:.1f} V{ty} H{tx:.1f}" fill="none" stroke="#5d4a78" stroke-width="1.2" stroke-dasharray="3 2" marker-end="url(#arrow)"><title>{esc(link["id"]+" "+link["type"])}</title></path>')
    y=bottom+30
    for line in note_lines: parts.append(svg_text(24,y,line,11)); y+=18
    parts.append('</g></svg>');return '\n'.join(parts)


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
    tasks=data['tasks'];ds=diagnostics(data)
    owners=sorted({t['owner'] for t in tasks})
    options=''.join(f'<option>{esc(owner)}</option>' for owner in owners)
    rows=''.join(f'<tr data-row="{esc(t["id"])}" data-owner="{esc(t["owner"])}" data-search="{esc(detail(t,data).lower())}"><th scope="row"><button data-detail="{esc(detail(t,data))}">{esc(t["id"])} · {esc(t["label"])}</button></th><td>{esc(t["owner"])}</td>'+''.join(f'<td>{esc(span_text(t,layer))}</td>' for layer in LAYERS)+f'<td>{esc(t["source"])}</td></tr>' for t in tasks)
    cards=''.join(f'<article data-row="{esc(t["id"])}" data-owner="{esc(t["owner"])}" data-search="{esc(detail(t,data).lower())}"><h3>{esc(t["id"])} · {esc(t["label"])}</h3><p>Owner: {esc(t["owner"])}</p><dl>'+''.join(f'<dt>{esc(data["comparison_label"] if layer=="comparison" else layer.title())}</dt><dd>{esc(span_text(t,layer))}</dd>' for layer in LAYERS)+f'</dl><button data-detail="{esc(detail(t,data))}">Inspect source and details</button></article>' for t in tasks)
    def uri(body,mime):return 'data:'+mime+';base64,'+base64.b64encode(body.encode()).decode()
    exports=' '.join(f'<a download="gantt.{ext}" href="{uri(body,mime)}">{label}</a>' for ext,body,mime,label in [('svg',svg,'image/svg+xml','Full SVG'),('json',json.dumps(data,ensure_ascii=False,indent=2),'application/json','Source JSON'),('csv',csv_text,'text/csv','All date layers CSV')])
    findings=''.join('<li>'+esc(x)+'</li>' for x in ds) or '<li>No supported structural or timing violations found. Resource feasibility and authority are not computed.</li>'
    links=''.join('<li>'+esc(f'{link["id"]}: {link["from"]} → {link["to"]}, {link["type"]}, {link["lag"]:+g} {link["lag_unit"]}; inferred: {link["inferred"]}; source: {link["source"]}')+'</li>' for link in data['links']) or '<li>No links supplied; this does not prove independence.</li>'
    notes=''.join('<li>'+esc(n)+'</li>' for n in data.get('notes', []))
    return '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+esc(data['title'])+'''</title><style>
:root{font:15px/1.45 Arial,sans-serif;color:#24364e;background:#f4f7fb}*{box-sizing:border-box}body{margin:0}main{max-width:1500px;margin:auto;padding:24px}h1{margin:0;color:#142e45}.meta,#scope{background:white;padding:12px;border-left:4px solid #627b9c}.toolbar{display:flex;flex-wrap:wrap;gap:12px;align-items:end;margin:18px 0}.toolbar label{display:grid;gap:4px}input,select,button{font:inherit;min-height:44px;padding:8px;border:1px solid #9eacc1;border-radius:5px;background:white}button{cursor:pointer;text-align:left}button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #126abb;outline-offset:3px}a{display:inline-block;color:#174e85;padding:10px}.scroll{overflow:auto;border:1px solid #c8d2e0;background:white;max-height:72vh}.chart svg{display:block;width:100%;min-width:1100px;height:auto}.table{margin-top:16px}table{border-collapse:separate;border-spacing:0;width:100%;min-width:1100px}th,td{padding:10px;border-bottom:1px solid #d8e0ec;text-align:left;vertical-align:top}thead th{position:sticky;top:0;background:#eaf0f7;z-index:2}tbody th{position:sticky;left:0;background:white;min-width:270px;z-index:1}tbody th button{width:100%;border:0}thead th:first-child{left:0;z-index:3}td{overflow-wrap:anywhere;min-width:140px}.mobile{display:none}article,#detail{padding:16px;background:white;border:1px solid #bfcddf;border-radius:6px;margin:16px 0}#detail{border:2px solid #617fa0;overflow-wrap:anywhere}article h3{margin:0}dt{font-weight:bold}dd{margin:0 0 10px}input,select{max-width:100%}[hidden]{display:none!important}.no-comparison .comparison{display:none}@media(max-width:600px){main{padding:16px}h1{font-size:25px}.desktop{display:none}.mobile{display:block}.toolbar label{width:100%}.chart-controls{display:none!important}}@media print{.toolbar,.exports{display:none}.scroll{max-height:none;overflow:visible}.chart svg{min-width:0}.mobile{display:none}.desktop{display:block}thead{display:table-header-group}thead th,tbody th{position:static}tr{break-inside:avoid}}
</style><main><h1>'''+esc(data['title'])+'''</h1><p class="meta">'''+esc(f'{data["version"]} · As of {data["as_of"]} · {data["scope"]}')+'''<br>Source: '''+esc(data['source'])+'''<br>Calendar: '''+esc(data['calendar']['label'])+''' · [start, finish); finish boundary excluded.</p><p>Gray: '''+esc(data['comparison_label'])+''' · Blue: forecast · Green: actual. Diamonds mark events, not acceptance. Unknown dates and progress stay unknown.</p><div class="toolbar"><label>Find task / ID / source<input id="search" type="search"></label><label>Owner<select id="owner"><option value="">All owners</option>'''+options+'''</select></label><label class="chart-controls">Chart scale<select id="zoom"><option value="100">Fit</option><option value="150">150%</option><option value="200">200%</option></select></label><label class="chart-controls">Comparison bars<select id="comparison"><option value="show">Shown</option><option value="hide">Hidden</option></select></label><button id="reset">Reset view</button></div><p id="scope" aria-live="polite"></p><div class="desktop"><div class="chart scroll" tabindex="0" aria-label="Complete schedule timeline; scroll horizontally for dates">'''+svg+'''</div><p>Filters apply to the source table below. The timeline always retains all rows and links for context. Chart scale and comparison visibility affect inspection only.</p><div class="table scroll"><table><caption>Exact source dates; select a task for persistent details</caption><thead><tr><th scope="col">Task</th><th scope="col">Owner</th><th scope="col">'''+esc(data['comparison_label'])+'''</th><th scope="col">Forecast</th><th scope="col">Actual</th><th scope="col">Source</th></tr></thead><tbody>'''+rows+'''</tbody></table></div></div><div class="mobile">'''+cards+'''</div><section id="detail" aria-live="polite"><h2>Task detail</h2><p id="detail-text">Select a task for evidence, progress meaning and full date layers.</p></section><section><h2>Diagnostics</h2><ul>'''+findings+'''</ul><h2>Dependency register</h2><ul>'''+links+'''</ul><h2>Reading notes</h2><ul>'''+notes+'''</ul></section><section class="exports"><h2>Complete artifact exports</h2><p>Downloads always contain all rows, date layers and the original comparison. JSON also preserves links, calendars and any extra source fields. CSV contains task date layers only and prefixes formula-leading text with an apostrophe.</p>'''+exports+'''</section><noscript>JavaScript is needed only for controls. Source tables and complete exports remain available.</noscript></main><script>
const search=document.getElementById('search'),owner=document.getElementById('owner'),zoom=document.getElementById('zoom'),comparison=document.getElementById('comparison');
function update(){let count=0;document.querySelectorAll('[data-row]').forEach(el=>{const yes=el.dataset.search.includes(search.value.toLocaleLowerCase())&&(!owner.value||el.dataset.owner===owner.value);el.hidden=!yes;if(yes&&el.tagName==='TR')count++;});document.getElementById('scope').textContent=count+' / '''+str(len(tasks))+''' source rows shown. Timeline retains all rows and links. Downloads always contain the full snapshot.';document.getElementById('detail-text').textContent='Select a visible task. Previous selection cleared after view change.';}
[search,owner].forEach(el=>el.addEventListener('input',update));zoom.addEventListener('input',()=>document.querySelector('.chart svg').style.width=zoom.value+'%');comparison.addEventListener('input',()=>document.querySelector('.chart').classList.toggle('no-comparison',comparison.value==='hide'));document.getElementById('reset').addEventListener('click',()=>{search.value='';owner.value='';zoom.value='100';comparison.value='show';document.querySelector('.chart svg').style.width='100%';document.querySelector('.chart').classList.remove('no-comparison');update();search.focus();});document.querySelectorAll('[data-detail]').forEach(el=>el.addEventListener('click',()=>document.getElementById('detail-text').textContent=el.dataset.detail));update();
</script></html>'''


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
