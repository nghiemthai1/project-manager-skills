"""Offline RACI renderer: inspectable HTML, SVG, JSON and spreadsheet-safe CSV.

Python 3.11+ standard library. No scheduling, approval, network or live writes.
"""
import argparse
import base64
import csv
import html
import io
import json
from pathlib import Path
import sys
import textwrap

COLORS = {'R': ('#dbeafe', '#173d73'), 'A': ('#e3defa', '#423075'),
          'C': ('#d6eee9', '#155d54'), 'I': ('#edf0f4', '#38475a'),
          'A/R': ('#e3defa', '#423075'), '?': ('#fff0d0', '#744c0e'),
          '—': ('#ffffff', '#5b6677')}
STATES = {'proposed', 'confirmed', 'disputed', 'unknown'}

def esc(value):
    return html.escape(str(value), quote=True)

def validate(data):
    if not isinstance(data, dict):
        raise ValueError('Expected an object')
    for key in ('title', 'version', 'as_of', 'source', 'scope', 'state'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'{key}: nonempty text required; state unknown explicitly')
    roles = data.get('roles'); rows = data.get('rows')
    if not isinstance(roles, list) or not isinstance(rows, list):
        raise ValueError('roles and rows must be lists')
    for label, items in [('role', roles), ('row', rows)]:
        ids = []
        for item in items:
            if not isinstance(item, dict) or not isinstance(item.get('id'), str) or not item['id'].strip():
                raise ValueError(f'{label}: literal string ID required')
            if not isinstance(item.get('label'), str) or not item['label'].strip():
                raise ValueError(f'{label} {item["id"]}: label required')
            ids.append(item['id'])
        if len(ids) != len(set(ids)):
            raise ValueError(f'Duplicate {label} ID')
    role_ids = {x['id'] for x in roles}
    for row in rows:
        if not isinstance(row.get('cells'), dict) or set(row['cells']) != role_ids:
            raise ValueError(f'{row["id"]}: every role needs an explicit cell, including unknowns')
        for rid, cell in row['cells'].items():
            if not isinstance(cell, dict) or cell.get('code') not in COLORS:
                raise ValueError(f'{row["id"]}/{rid}: invalid code')
            if cell.get('state') not in STATES:
                raise ValueError(f'{row["id"]}/{rid}: invalid confirmation state')
            for key in ('note', 'source'):
                if not isinstance(cell.get(key), str):
                    raise ValueError(f'{row["id"]}/{rid}: {key} must be text')
            if cell['state'] == 'confirmed' and not cell['source'].strip():
                raise ValueError(f'{row["id"]}/{rid}: confirmed requires an evidence reference')
    if not isinstance(data.get('notes', []), list) or any(not isinstance(n, str) for n in data.get('notes', [])):
        raise ValueError('notes must be text entries')
    return data

def audit(data):
    findings = []
    for row in data['rows']:
        cells = list(row['cells'].values())
        ac = sum(c['code'] in ('A', 'A/R') for c in cells)
        rc = sum(c['code'] in ('R', 'A/R') for c in cells)
        flags = []
        if ac != 1: flags.append(f'{ac} A assignments; confirm bounded ownership')
        if not rc: flags.append('No R assignment')
        if any(c['code'] == '?' for c in cells): flags.append('Unresolved cells')
        if any(c['state'] == 'disputed' for c in cells): flags.append('Disputed assignment')
        if any(c['code'] != '—' and c['state'] != 'confirmed' for c in cells): flags.append('Assignments not fully confirmed')
        if flags: findings.append({'id': row['id'], 'findings': flags})
    return findings

def svg_text(x, y, value, size=13, fill='#26354a', weight='400'):
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" font-weight="{weight}">{esc(value)}</text>'

def render_svg(data):
    roles = data['roles']; rows = data['rows']; findings = audit(data)
    left = 310; cw = 145; width = max(780, left + cw * len(roles) + 30)
    # Wrap content before assigning geometry; no silent truncation.
    head_lines = textwrap.wrap(f'{data["state"]} · {data["version"]} · As of {data["as_of"]}', max(30, (width - 60)//7))
    scope_lines = textwrap.wrap(data['scope'], max(30, (width-60)//7))
    source_lines = textwrap.wrap('Source: '+data['source'], max(30, (width-60)//7))
    title_lines = textwrap.wrap(data['title'], max(20, (width-60)//13))
    top = 35 + len(title_lines)*28 + (len(head_lines)+len(scope_lines)+len(source_lines))*19 + 45
    header_h = max([60]+[24 + len(textwrap.wrap(r['label'], 18))*17 for r in roles])
    heights = [max(74, 28 + len(textwrap.wrap(row['id'],35))*14 + len(textwrap.wrap(row['label'],35))*17) for row in rows]
    cell_notes = [f'{row["id"]} / {role["label"]}: {row["cells"][role["id"]]["note"]}' for row in rows for role in roles if row['cells'][role['id']]['note']]
    notes = ['R performs · A owns result · C consulted · I informed · A/R both · ? unresolved · — no assignment',
             'Dashed border = proposed/unknown; solid border = confirmed; red outline = disputed.',
             f'{len(rows)} rows · {len(roles)} roles · {len(findings)} rows with review findings. Counts are not utilization.'] + data.get('notes', []) + cell_notes
    note_lines = [line for n in notes for line in textwrap.wrap(n, max(30,(width-60)//7))]
    height = top + header_h + sum(heights) + 45 + len(note_lines)*19
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
             f'<title id="title">{esc(data["title"])}</title><desc id="desc">{esc(data["state"])} responsibility matrix. Full assignments, notes and sources are available in the accompanying HTML, JSON and CSV.</desc>',
             f'<rect width="{width}" height="{height}" fill="#f7f9fc"/>', '<g font-family="Arial, sans-serif">']
    y = 35
    for line in title_lines: parts.append(svg_text(26,y,line,23,'#13283f','700'));y+=28
    for line in head_lines + scope_lines + source_lines: parts.append(svg_text(26,y,line,13));y+=19
    parts.append(svg_text(26,top+30,'DELIVERABLE / DECISION',12,'#42516a','700'))
    for i, role in enumerate(roles):
        for j,line in enumerate(textwrap.wrap(role['label'],18)):
            parts.append(svg_text(left+i*cw+12,top+25+j*17,line,13,'#13283f','700'))
    y = top+header_h
    for row,rh in zip(rows,heights):
        parts.append(f'<rect x="20" y="{y}" width="{width-40}" height="{rh}" fill="#fff" stroke="#dde3ec"/>')
        id_lines = textwrap.wrap(row['id'],35)
        for j,line in enumerate(id_lines):
            parts.append(svg_text(32,y+19+j*14,line,11,'#5b6677'))
        for j,line in enumerate(textwrap.wrap(row['label'],35)):
            parts.append(svg_text(32,y+25+len(id_lines)*14+j*17,line,13,'#26354a','600'))
        for i,role in enumerate(roles):
            c=row['cells'][role['id']]; bg,fg=COLORS[c['code']];x=left+i*cw+8
            dash='' if c['state']=='confirmed' else ' stroke-dasharray="4 3"'
            stroke='#a12032' if c['state']=='disputed' else '#a3adbd'
            parts.append(f'<rect x="{x}" y="{y+10}" width="{cw-16}" height="{rh-20}" rx="8" fill="{bg}" stroke="{stroke}"{dash}/>')
            parts.append(svg_text(x+12,y+34,c['code'],20,fg,'700'))
            parts.append(svg_text(x+12,y+52,c['state'],10,fg))
        y+=rh
    y+=30
    for line in note_lines:parts.append(svg_text(26,y,line,12));y+=19
    parts += ['</g></svg>'];return '\n'.join(parts)

def detail(row, role, cell):
    return f'{row["id"]} — {row["label"]} | {role["label"]}: {cell["code"]}; {cell["state"]}. Duty: {cell["note"] or "not further specified"}. Source: {cell["source"] or "unknown"}.'

def spreadsheet_text(value):
    # JSON retains exact strings. Prefix only spreadsheet formula-leading values.
    return "'"+value if value.startswith(('=','+','-','@','\t','\r')) else value

def render_csv(data):
    target=io.StringIO(newline='');writer=csv.writer(target)
    writer.writerow(['row_id','deliverable','role_id','role','code','confirmation','work_boundary','source'])
    for row in data['rows']:
        for role in data['roles']:
            c=row['cells'][role['id']]
            writer.writerow([spreadsheet_text(v) for v in [row['id'],row['label'],role['id'],role['label'],c['code'],c['state'],c['note'],c['source']]])
    return target.getvalue()

def render_html(data, svg, csv_text):
    roles=data['roles'];rows=data['rows'];findings=audit(data);flag_ids={f['id'] for f in findings}
    def uri(text, mime):return 'data:'+mime+';base64,'+base64.b64encode(text.encode()).decode()
    buttons=lambda row: ''.join(f'<td data-role="{esc(role["id"])}"><button data-state="{esc(row["cells"][role["id"]]["state"])}" class="cell code-{esc(row["cells"][role["id"]]["code"].replace("/",""))}" data-detail="{esc(detail(row,role,row["cells"][role["id"]]))}"><b>{esc(row["cells"][role["id"]]["code"])}</b><small>{esc(row["cells"][role["id"]]["state"])}</small><span class="sr">{esc(role["label"])}</span></button></td>' for role in roles)
    table_rows=''.join(f'<tr data-row="{esc(row["id"])}" data-findings="{str(row["id"] in flag_ids).lower()}" data-search="{esc((json.dumps(row,ensure_ascii=False)+' '+ ' '.join(r['label'] for r in roles)).lower())}"><th scope="row">{esc(row["id"])}<br>{esc(row["label"])}</th>{buttons(row)}</tr>' for row in rows)
    cards=''.join(f'<article data-row="{esc(row["id"])}" data-findings="{str(row["id"] in flag_ids).lower()}" data-search="{esc((json.dumps(row,ensure_ascii=False)+' '+ ' '.join(r['label'] for r in roles)).lower())}"><h3>{esc(row["label"])}</h3><p>{esc(row["id"])}</p>'+''.join(f'<button class="card-cell" data-role="{esc(role["id"])}" data-detail="{esc(detail(row,role,row["cells"][role["id"]]))}">{esc(role["label"])} <b>{esc(row["cells"][role["id"]]["code"])}</b> · {esc(row["cells"][role["id"]]["state"])}</button>' for role in roles)+'</article>' for row in rows)
    opts=''.join(f'<option value="{esc(x["id"])}">{esc(x["label"])}</option>' for x in roles)
    heads=''.join(f'<th scope="col" data-role="{esc(x["id"])}">{esc(x["label"])}</th>' for x in roles)
    audit_html=''.join(f'<li><b>{esc(f["id"])}</b>: {esc("; ".join(f["findings"]))}</li>' for f in findings) or '<li>No structural findings; this does not confirm assignments.</li>'
    exports=' '.join(f'<a download="raci.{ext}" href="{uri(body,mime)}">{label}</a>' for ext,body,mime,label in [('svg',svg,'image/svg+xml','Full SVG'),('json',json.dumps(data,ensure_ascii=False,indent=2),'application/json','Source JSON'),('csv',csv_text,'text/csv','All cells CSV')])
    unresolved=sum(c['code']=='?' or c['state']=='unknown' for row in rows for c in row['cells'].values())
    summaries='<ul>'+''.join('<li>'+esc(role['label'])+': '+', '.join(f'{code}: {sum(row["cells"][role["id"]]["code"] in ((code, "A/R") if code in ("A", "R") else (code,)) for row in rows)}' for code in ('A','R','C','I','?'))+'</li>' for role in roles)+'</ul>'
    unresolved=sum(c['code']=='?' or c['state']=='unknown' for row in rows for c in row['cells'].values())
    summaries='<ul>'+''.join('<li>'+esc(role['label'])+': '+', '.join(f'{code}: {sum(row["cells"][role["id"]]["code"] in ((code, "A/R") if code in ("A", "R") else (code,)) for row in rows)}' for code in ('A','R','C','I','?'))+'</li>' for role in roles)+'</ul>'
    notes=''.join(f'<li>{esc(n)}</li>' for n in data.get('notes',[]))
    return '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'''+esc(data['title'])+'''</title><style>
:root{font-family:Arial,sans-serif;color:#26354a;background:#f4f7fb;line-height:1.45}*{box-sizing:border-box}body{margin:0;overflow-wrap:anywhere}main{max-width:1500px;margin:auto;padding:24px}h1{color:#13283f;margin:0 0 8px}.meta,.notice{border-left:4px solid #526a8b;padding:10px 14px;background:#fff}.notice{border-color:#b87c18}button,input,select{font:inherit;min-height:44px}button,a,input,select{outline-offset:3px}button:focus-visible,a:focus-visible,input:focus-visible,select:focus-visible{outline:3px solid #056dca}.toolbar{display:flex;flex-wrap:wrap;gap:12px;align-items:end;padding:14px 0}.toolbar label{display:grid;gap:4px}input,select,button{border:1px solid #a3adbd;border-radius:6px;background:white;padding:8px}a{display:inline-block;padding:9px 12px;color:#17467f}.scroll{overflow:auto;max-height:68vh;border:1px solid #cbd4e1;background:white}table{border-collapse:separate;border-spacing:0;min-width:900px;width:100%}th,td{padding:9px;border-bottom:1px solid #dce3ed;text-align:left}thead th{position:sticky;top:0;background:#e9eef6;z-index:2;min-width:135px}tbody th{position:sticky;left:0;background:#fff;min-width:270px;max-width:340px;z-index:1}thead th:first-child{left:0;z-index:3}.cell{min-width:110px;width:100%;text-align:left;border-style:dashed}.cell b{display:block;font-size:20px}.cell small{display:block}.cell[data-state="confirmed"]{border-style:solid}.cell[data-state="disputed"]{border:2px solid #a12032}.cell[data-state="unknown"]{background:#fff0d0;color:#744c0e}.code-R{background:#dbeafe;color:#173d73}.code-A,.code-AR{background:#e3defa;color:#423075}.code-C{background:#d6eee9;color:#155d54}.code-I{background:#edf0f4;color:#38475a}#detail{background:#fff;border:2px solid #657c9d;padding:16px;margin:16px 0;overflow-wrap:anywhere}.mobile{display:none}article{background:white;padding:16px;margin:12px 0;border:1px solid #ccd6e5;border-radius:8px}article h3{margin:0}.card-cell{display:block;width:100%;text-align:left;margin:6px 0}.sr{position:absolute;left:0;top:0;left:0;top:0;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}[hidden]{display:none!important}@media(max-width:600px){main{padding:16px}.desktop{display:none}.mobile{display:block}.toolbar{gap:8px}.toolbar label{max-width:100%}input,select{width:100%}h1{font-size:25px}.toolbar label:first-child{width:100%}}@media print{.toolbar,.exports,button#reset{display:none}.scroll{overflow:visible;max-height:none}thead th,tbody th{position:static}.cell{border:1px solid #777}main{padding:0}.mobile{display:none}.desktop{display:block}thead{display:table-header-group}tr{break-inside:avoid}}
</style><main><h1>'''+esc(data['title'])+'''</h1><p class="meta">'''+esc(f'{data["state"]} · {data["version"]} · As of {data["as_of"]}')+'''<br>'''+esc(data['scope'])+'''<br>Source: '''+esc(data['source'])+'''</p><p><b>R</b> performs · <b>A</b> owns result · <b>C</b> consulted · <b>I</b> informed · <b>A/R</b> both · <b>?</b> unresolved · <b>—</b> no assignment. Select a cell for its full duty and source.</p><p>'''+str(unresolved)+''' unresolved cells · '''+str(len(findings))+''' rows with findings. Letters count proposed and confirmed assignments alike.</p><p>'''+str(unresolved)+''' unresolved cells · '''+str(len(findings))+''' rows with findings. Letters count proposed and confirmed assignments alike.</p><div class="toolbar"><label>Find deliverable / ID / evidence<input id="search" type="search"></label><label>Role view<select id="role"><option value="">All roles</option>'''+opts+'''</select></label><label><span>Review filter</span><select id="issues"><option value="all">All rows</option><option value="findings">Rows with findings</option></select></label><button id="reset">Reset view</button></div><p id="scope" class="notice" aria-live="polite"></p><div class="desktop scroll"><table><caption class="sr">Responsibility assignments and confirmation states</caption><thead><tr><th scope="col">Deliverable / decision</th>'''+heads+'''</tr></thead><tbody>'''+table_rows+'''</tbody></table></div><div class="mobile">'''+cards+'''</div><section id="detail" aria-live="polite"><b>Assignment detail</b><p id="detail-text">Select a cell. A colored letter is not confirmation of agreement.</p></section><section><h2>Role counts · full matrix</h2>'''+summaries+'''<h2>Role counts · full matrix</h2>'''+summaries+'''<h2>Audit findings</h2><ul>'''+audit_html+'''</ul><p>Counts reveal responsibility patterns, not utilization or staffing feasibility.</p><ul>'''+notes+'''</ul></section><section class="exports"><h2>Complete artifact exports</h2><p>Downloads include the full matrix, regardless of inspection filters. CSV prefixes formula-leading text with an apostrophe for spreadsheet safety; JSON preserves every literal value.</p>'''+exports+'''</section><noscript><p>Interactive filtering and details require JavaScript. Full source JSON and CSV contain every duty and evidence reference; the complete table remains readable.</p></noscript></main><script>
const search=document.getElementById('search'),role=document.getElementById('role'),issues=document.getElementById('issues');
function update(){const q=search.value.toLocaleLowerCase();let count=0;document.querySelectorAll('[data-row]').forEach(el=>{const yes=el.dataset.search.includes(q)&&(issues.value==='all'||el.dataset.findings==='true');el.hidden=!yes;if(yes&&el.tagName==='TR')count++;});document.querySelectorAll('[data-role]').forEach(el=>el.hidden=!!role.value&&el.dataset.role!==role.value);document.getElementById('scope').textContent=count+' / '''+str(len(rows))+''' rows shown. '+(role.value?'Role-focused view: assignments in other columns are hidden; return to All roles before auditing ownership.':'All roles shown.')+' Filters affect inspection only; downloads contain the complete matrix.';document.getElementById('detail-text').textContent='Select a visible cell. Previous selection cleared after view change.';}
[search,role,issues].forEach(el=>el.addEventListener('input',update));document.getElementById('reset').addEventListener('click',()=>{search.value='';role.value='';issues.value='all';update();search.focus();});document.querySelectorAll('[data-detail]').forEach(el=>el.addEventListener('click',()=>{document.getElementById('detail-text').textContent=el.dataset.detail;}));update();
</script></html>'''

def demo():
    return {'title':'Fictional RACI demonstration','version':'draft-1','as_of':'unknown','source':'Fictional built-in example','scope':'One bounded handoff; assignments are proposals','state':'Proposed', 'roles':[{'id':'PM','label':'Project manager'},{'id':'OPS','label':'Service owner'}], 'rows':[{'id':'H-1','label':'Service transfer decision','cells':{'PM':{'code':'R','state':'proposed','note':'Prepare the handover record','source':''},'OPS':{'code':'?','state':'unknown','note':'Actual acceptance authority unresolved','source':''}}}], 'notes':['This demonstration records no actual transfer or accepted assignment.']}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('input',nargs='?',type=Path);parser.add_argument('--output',type=Path,help='Output filename stem; writes .svg/.html/.json/.csv');parser.add_argument('--demo',action='store_true');args=parser.parse_args()
    try:
        if args.demo and args.input:raise ValueError('Choose an input file or --demo')
        if not args.demo and not args.input:raise ValueError('Provide input JSON or --demo')
        data=validate(demo() if args.demo else json.loads(args.input.read_text(encoding='utf-8')))
        svg=render_svg(data);csv_text=render_csv(data)
        if args.output:
            stem=args.output;stem.parent.mkdir(parents=True,exist_ok=True)
            files={'.svg':svg,'.html':render_html(data,svg,csv_text),'.json':json.dumps(data,indent=2,ensure_ascii=False)+'\n','.csv':csv_text}
            for suffix,content in files.items():Path(str(stem)+suffix).write_text(content,encoding='utf-8',newline='')
            print(json.dumps({'files':[str(stem)+x for x in files],'rows':len(data['rows']),'roles':len(data['roles']),'findings':audit(data)},ensure_ascii=False))
        else:print(svg)
        return 0
    except (OSError,ValueError,TypeError,KeyError) as exc:
        print(f'Input error: {exc}',file=sys.stderr);return 2
if __name__=='__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')
    raise SystemExit(main())
