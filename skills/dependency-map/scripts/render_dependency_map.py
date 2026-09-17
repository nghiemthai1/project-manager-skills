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

"""Render evidence-led dependency networks to offline HTML, SVG, JSON and CSV.

Python 3.11+ standard library. Arrows run provider -> receiver. The helper
calculates a local calendar-day margin only; it is not a scheduling engine and
does not infer CPM float, project delay, commitments or acceptance.
"""
import argparse
import csv
from datetime import date
import html
import io
import json
from pathlib import Path
import sys
import textwrap

STATUSES = ('unconfirmed', 'not_started', 'in_progress', 'at_risk', 'blocked', 'delivered', 'verified', 'accepted')
ACCEPTANCE = ('unknown', 'not_delivered', 'delivered_unverified', 'verification_failed', 'verified_unaccepted', 'accepted')
KINDS = ('team', 'vendor', 'service', 'authority', 'unknown')
PALETTE = {
    'gap': '#d80b61', 'blocked': '#b42318', 'at_risk': '#b54708', 'unconfirmed': '#667085',
    'watch': '#08766c', 'closed': '#286645'
}


def esc(value):
    return html.escape(str(value), quote=True)


def parse_date(value):
    if value is None:
        return None
    if not isinstance(value, str) or len(value) != 10:
        raise ValueError('Dates must be ISO YYYY-MM-DD or null')
    parsed = date.fromisoformat(value)
    if parsed.isoformat() != value:
        raise ValueError('Noncanonical ISO date')
    return parsed


def validate(data):
    if not isinstance(data, dict):
        raise ValueError('Expected a dependency snapshot object')
    for key in ('title', 'as_of', 'version', 'source', 'scope'):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f'{key}: nonempty text required; explicitly state unknown')
    parse_date(data['as_of'])
    calendar = data.get('calendar')
    if not isinstance(calendar, dict) or calendar.get('unit') != 'calendar_days' or not isinstance(calendar.get('label'), str):
        raise ValueError('calendar must state label and calendar_days unit')
    if not isinstance(data.get('nodes'), list) or not isinstance(data.get('dependencies'), list):
        raise ValueError('nodes and dependencies must be lists')
    node_ids = set()
    for node in data['nodes']:
        if not isinstance(node, dict): raise ValueError('Node must be an object')
        for key in ('id', 'label', 'owner', 'source'):
            if not isinstance(node.get(key), str) or not node[key].strip(): raise ValueError('Node '+key+' required')
        if node['id'] in node_ids: raise ValueError('Duplicate node ID: '+node['id'])
        node_ids.add(node['id'])
        if node.get('kind') not in KINDS: raise ValueError('Unsupported node kind')
    dep_ids = set()
    for dep in data['dependencies']:
        if not isinstance(dep, dict): raise ValueError('Dependency must be an object')
        for key in ('id', 'provider', 'receiver', 'handoff', 'usable_criteria', 'owner', 'receiver_owner', 'source'):
            if not isinstance(dep.get(key), str) or not dep[key].strip(): raise ValueError('Dependency '+key+' required')
        if dep['id'] in dep_ids: raise ValueError('Duplicate dependency ID: '+dep['id'])
        dep_ids.add(dep['id'])
        if dep['provider'] not in node_ids or dep['receiver'] not in node_ids:
            raise ValueError(dep['id']+': provider and receiver must reference nodes')
        if dep['provider'] == dep['receiver']: raise ValueError(dep['id']+': provider and receiver must differ')
        if dep.get('status') not in STATUSES: raise ValueError(dep['id']+': unsupported status')
        if dep.get('acceptance_state') not in ACCEPTANCE: raise ValueError(dep['id']+': unsupported acceptance state')
        for key in ('needed_by', 'requested', 'committed', 'forecast'):
            parse_date(dep.get(key))
        commitment_source = dep.get('commitment_source')
        if dep.get('committed') and (not isinstance(commitment_source, str) or not commitment_source.strip()):
            raise ValueError(dep['id']+': committed date requires commitment_source')
        if not dep.get('committed') and commitment_source not in (None, ''):
            raise ValueError(dep['id']+': commitment_source requires committed date')
        if not isinstance(dep.get('note', ''), str): raise ValueError(dep['id']+': note must be text')
    presentation = data.get('presentation')
    if not isinstance(presentation, dict): raise ValueError('presentation is required')
    for key in ('eyebrow', 'headline', 'lede', 'insight_heading', 'decision'):
        if not isinstance(presentation.get(key), str) or not presentation[key].strip(): raise ValueError('presentation '+key+' required')
    if presentation.get('default_dependency_id') not in dep_ids: raise ValueError('default_dependency_id must reference a dependency')
    metrics = presentation.get('metrics')
    if not isinstance(metrics, list) or not metrics: raise ValueError('presentation metrics required')
    for metric in metrics:
        if not isinstance(metric, dict) or any(not isinstance(metric.get(k), str) or not metric[k].strip() for k in ('label','value','note')):
            raise ValueError('Each metric needs label, value and note')
    points = presentation.get('insight_points')
    if not isinstance(points, list) or any(not isinstance(p, str) or not p.strip() for p in points):
        raise ValueError('insight_points must be text entries')
    analysis = data.get('analysis')
    if not isinstance(analysis, dict) or not isinstance(analysis.get('method'), str) or not analysis['method'].strip():
        raise ValueError('analysis must explain its method')
    focus = analysis.get('coordination_focus_ids', [])
    if not isinstance(focus, list) or any(dep_id not in dep_ids for dep_id in focus):
        raise ValueError('coordination_focus_ids must reference dependencies')
    if 'critical_path' in analysis and analysis['critical_path'] is not None:
        cpm = analysis['critical_path']
        if not isinstance(cpm, dict) or not isinstance(cpm.get('method'), str) or not isinstance(cpm.get('dependency_ids'), list):
            raise ValueError('critical_path needs an explicit method and dependency_ids')
        if any(dep_id not in dep_ids for dep_id in cpm['dependency_ids']): raise ValueError('critical_path references unknown dependency')
    if not isinstance(data.get('notes', []), list) or any(not isinstance(n, str) for n in data.get('notes', [])):
        raise ValueError('notes must be text entries')
    return data


def local_margin(dep):
    needed, forecast = parse_date(dep.get('needed_by')), parse_date(dep.get('forecast'))
    return (needed - forecast).days if needed and forecast else None


def category(dep):
    margin = local_margin(dep)
    if dep['acceptance_state'] == 'accepted' or dep['status'] == 'accepted': return 'closed'
    if dep['status'] == 'blocked' or dep['acceptance_state'] == 'verification_failed': return 'blocked'
    if margin is not None and margin < 0: return 'gap'
    if dep['status'] == 'at_risk': return 'at_risk'
    if dep['status'] == 'unconfirmed' or not dep.get('needed_by') or not dep.get('forecast'): return 'unconfirmed'
    return 'watch'


def margin_text(dep):
    value = local_margin(dep)
    if value is None: return 'not calculable'
    return ('+' if value > 0 else '') + str(value) + ' calendar days'


def layout(data):
    """Stable left-to-right layering. Cycles share a layer; arrows remain visible."""
    ids = [n['id'] for n in data['nodes']]
    outgoing = {i: [] for i in ids}
    incoming = {i: 0 for i in ids}
    for dep in data['dependencies']:
        outgoing[dep['provider']].append(dep['receiver'])
        incoming[dep['receiver']] += 1
    rank = {i: 0 for i in ids}
    queue = [i for i in ids if incoming[i] == 0]
    seen = set()
    while queue:
        current = queue.pop(0); seen.add(current)
        for target in outgoing[current]:
            rank[target] = max(rank[target], rank[current] + 1)
            incoming[target] -= 1
            if incoming[target] == 0: queue.append(target)
    # Cyclic components use the next stable column rather than inventing precedence.
    for node_id in ids:
        if node_id not in seen: rank[node_id] = max(rank.values(), default=0) + 1
    cols = {}
    for node in data['nodes']: cols.setdefault(rank[node['id']], []).append(node['id'])
    positions = {}
    for col, members in sorted(cols.items()):
        for row, node_id in enumerate(members): positions[node_id] = (70 + col * 430, 130 + row * 150)
    width = max(1040, 120 + (max(cols, default=0)+1)*430)
    height = max(560, 230 + max((len(v) for v in cols.values()), default=1)*150)
    return positions, width, height


def wrap(value, width=27):
    return textwrap.wrap(str(value), width=width, break_long_words=False, break_on_hyphens=False) or ['']


def render_svg(data):
    validate(data); pos, graph_w, graph_h = layout(data)
    width, graph_top = max(1280, graph_w + 80), 286
    height = graph_top + graph_h + 190
    nodes = {n['id']: n for n in data['nodes']}
    focus = set(data['analysis'].get('coordination_focus_ids', []))
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
           f'<title id="title">{esc(data["title"])}</title><desc id="desc">Provider-to-receiver dependency network as of {esc(data["as_of"])}. Local margins are not CPM float.</desc>',
           '<defs><filter id="shadow" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="5" stdDeviation="7" flood-color="#0b1f40" flood-opacity=".12"/></filter>',
           '<marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs>',
           '<rect width="100%" height="100%" fill="#f5f7fb"/><rect x="0" y="0" width="12" height="100%" fill="#173b2d"/>',
           f'<text x="38" y="46" font-family="Arial" font-size="13" font-weight="700" letter-spacing="2" fill="#d80b61">{esc(data["presentation"]["eyebrow"].upper())}</text>',
           f'<text x="38" y="100" font-family="Arial" font-size="42" font-weight="800" fill="#0c234b">{esc(data["presentation"]["headline"])}</text>',
           f'<text x="38" y="135" font-family="Arial" font-size="16" fill="#536581">{esc(data["presentation"]["lede"])}</text>']
    metric_x = 38
    for metric in data['presentation']['metrics']:
        out += [f'<g><rect x="{metric_x}" y="168" width="225" height="88" rx="14" fill="#fff" stroke="#ccd6e5"/>',
                f'<text x="{metric_x+16}" y="194" font-family="Arial" font-size="11" font-weight="700" fill="#667085">{esc(metric["label"].upper())}</text>',
                f'<text x="{metric_x+16}" y="222" font-family="Arial" font-size="22" font-weight="800" fill="#0c234b">{esc(metric["value"])}</text>',
                f'<text x="{metric_x+16}" y="242" font-family="Arial" font-size="11" fill="#667085">{esc(metric["note"][:38])}</text></g>']
        metric_x += 239
    out.append(f'<g transform="translate(25 {graph_top})"><rect width="{graph_w}" height="{graph_h}" rx="18" fill="#fff" stroke="#ccd6e5"/>')
    pair_totals = {}
    pair_seen = {}
    for dep in data['dependencies']:
        pair = (dep['provider'], dep['receiver'])
        pair_totals[pair] = pair_totals.get(pair, 0) + 1
    for dep in data['dependencies']:
        x1,y1=pos[dep['provider']];x2,y2=pos[dep['receiver']]
        pair = (dep['provider'], dep['receiver'])
        index = pair_seen.get(pair, 0); pair_seen[pair] = index + 1
        edge_offset = (index - (pair_totals[pair] - 1) / 2) * 34
        x1+=230;y1+=46+edge_offset;y2+=46+edge_offset
        color=PALETTE[category(dep)]; mid=(x1+x2)/2
        out.append(f'<g data-dependency="{esc(dep["id"])}"><path d="M{x1} {y1} C{mid} {y1},{mid} {y2},{x2} {y2}" fill="none" stroke="{color}" stroke-width="{4 if dep["id"] in focus else 2.5}" marker-end="url(#arrow)"/>')
        label=dep['id']+' · '+margin_text(dep)
        lx=mid-76;ly=(y1+y2)/2-17
        out.append(f'<rect x="{lx}" y="{ly}" width="152" height="27" rx="13" fill="#fff" stroke="{color}"/><text x="{mid}" y="{ly+18}" text-anchor="middle" font-family="Arial" font-size="10" font-weight="700" fill="{color}">{esc(label[:25])}</text></g>')
    for node in data['nodes']:
        x,y=pos[node['id']]
        out += [f'<g data-node="{esc(node["id"])}" transform="translate({x} {y})" filter="url(#shadow)"><rect width="230" height="92" rx="14" fill="#fff" stroke="#b8c6d9"/>',
                f'<rect width="7" height="92" rx="3" fill="#0c234b"/><text x="20" y="25" font-family="Arial" font-size="10" font-weight="700" fill="#d80b61">{esc(node["kind"].upper())}</text>',
                f'<text x="20" y="51" font-family="Arial" font-size="16" font-weight="800" fill="#0c234b">{esc(node["label"][:25])}</text>',
                f'<text x="20" y="74" font-family="Arial" font-size="11" fill="#667085">Owner: {esc(node["owner"][:25])}</text></g>']
    out.append('</g>')
    legend_y=graph_top+graph_h+38
    out.append(f'<text x="38" y="{legend_y}" font-family="Arial" font-size="12" font-weight="700" fill="#0c234b">PROVIDER → RECEIVER</text>')
    x=225
    for name in ('gap','blocked','at_risk','unconfirmed','watch','closed'):
        out.append(f'<circle cx="{x}" cy="{legend_y-4}" r="5" fill="{PALETTE[name]}"/><text x="{x+10}" y="{legend_y}" font-family="Arial" font-size="11" fill="#536581">{esc(name.replace("_"," "))}</text>');x+=112
    out.append(f'<text x="38" y="{legend_y+35}" font-family="Arial" font-size="11" fill="#667085">As of {esc(data["as_of"])} · {esc(data["calendar"]["label"])} · Source: {esc(data["source"][:130])}</text>')
    out.append(f'<text x="38" y="{legend_y+58}" font-family="Arial" font-size="11" fill="#667085">{esc(data["analysis"]["method"][:170])}</text></svg>')
    return ''.join(out)


def csv_safe(value):
    text = '' if value is None else str(value)
    if isinstance(value, str) and text[:1] in ('=', '+', '-', '@', '\t', '\r'): text = "'"+text
    return text


def render_csv(data):
    validate(data); stream=io.StringIO(newline=''); writer=csv.writer(stream,lineterminator='\n')
    writer.writerow(['dependency_id','provider','receiver','handoff','usable_criteria','needed_by','requested','committed','forecast','local_margin_calendar_days','status','acceptance_state','owner','receiver_owner','source','note'])
    nodes={n['id']:n['label'] for n in data['nodes']}
    for dep in data['dependencies']:
        writer.writerow([csv_safe(v) for v in (dep['id'],nodes[dep['provider']],nodes[dep['receiver']],dep['handoff'],dep['usable_criteria'],dep.get('needed_by'),dep.get('requested'),dep.get('committed'),dep.get('forecast'),local_margin(dep),dep['status'],dep['acceptance_state'],dep['owner'],dep['receiver_owner'],dep['source'],dep.get('note',''))])
    return stream.getvalue()


def _safe_json(data):
    return json.dumps(data, ensure_ascii=False, separators=(',', ':')).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')


def render_html(data, svg=None, csv_text=None):
    validate(data); svg=svg or render_svg(data); csv_text=csv_text or render_csv(data)
    payload=_safe_json(data); svg_json=_safe_json(svg); csv_json=_safe_json(csv_text)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(data['title'])}</title>
<style>
.button{{display:inline-flex!important;align-items:center;text-decoration:none}}
:root{{--navy:#0c234b;--ink:#13294b;--muted:#60708b;--line:#ccd6e5;--paper:#f5f7fb;--pink:#d80b61;--green:#08766c;--red:#b42318;--amber:#b54708}}*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font:15px/1.42 Inter,Segoe UI,Arial,sans-serif;border-left:10px solid #173b2d}}button,input,select{{font:inherit}}button:focus-visible,input:focus-visible,select:focus-visible,[tabindex]:focus-visible{{outline:3px solid #ff8fbd;outline-offset:2px}}.page{{padding:28px 20px 50px;max-width:1800px;margin:auto}}header{{display:flex;gap:32px;justify-content:space-between;align-items:end;margin-bottom:22px}}.eyebrow{{font-size:12px;letter-spacing:2px;color:var(--pink);font-weight:800}}h1{{font-size:46px;line-height:1.05;margin:14px 0 0}}.lede{{max-width:760px;text-align:right;color:var(--muted);font-size:18px}}.metrics{{display:grid;grid-template-columns:repeat(4,minmax(180px,1fr));gap:12px;margin-bottom:18px}}.metric,.toolbar,.workspace,.insight,.register{{background:#fff;border:1px solid var(--line);border-radius:18px}}.metric{{padding:14px 16px}}.metric b{{display:block;font-size:24px;margin:4px 0}}.metric span,.metric small{{display:block;color:var(--muted)}}.metric span{{font-size:11px;font-weight:800;letter-spacing:.08em}}.toolbar{{padding:14px 16px;display:flex;gap:12px;align-items:end;flex-wrap:wrap;position:sticky;top:8px;z-index:8;box-shadow:0 8px 28px #0c234b12}}label{{font-size:11px;font-weight:800;color:#536581;letter-spacing:.04em}}label input,label select{{display:block;margin-top:5px;min-width:190px}}input,select,.button{{height:46px;border:1px solid #b9c8dc;border-radius:12px;background:#fff;padding:0 13px;color:var(--navy)}}.button{{font-weight:750;cursor:pointer}}.button.active,.button.primary{{border-color:var(--pink);color:#a40048;background:#fff5fa}}.button.dark{{background:var(--navy);color:#fff}}.spacer{{flex:1}}.tabs{{display:flex;gap:8px}}.workspace{{margin-top:16px;overflow:hidden}}.view-head{{display:flex;justify-content:space-between;gap:20px;padding:16px 18px;border-bottom:1px solid var(--line)}}.view-head b{{font-size:18px}}.view-head span{{color:var(--muted)}}.graph-shell{{overflow:auto;min-height:520px;background:linear-gradient(#fff,#fbfcfe)}}#graph{{display:block;min-width:980px;transform-origin:0 0}}.node rect{{fill:#fff;stroke:#b8c6d9;stroke-width:1.5}}.node .rail{{fill:var(--navy);stroke:none}}.node text{{pointer-events:none}}.node.dim,.edge.dim{{opacity:.13}}.node.selected rect{{stroke:var(--pink);stroke-width:4}}.edge path{{fill:none;stroke-width:3}}.edge.focus path{{stroke-width:5}}.edge .hit{{stroke:transparent;stroke-width:18;cursor:pointer}}.edge text{{font-size:11px;font-weight:750;cursor:pointer}}.detail{{display:grid;grid-template-columns:1fr 1fr;gap:18px;padding:20px;border-top:1px solid var(--line);background:#fbfcfe}}.detail h2{{margin:0 0 8px;font-size:23px}}.tag{{display:inline-block;padding:5px 9px;border-radius:99px;background:#eef2f7;font-size:12px;font-weight:800;margin-right:6px}}.facts{{display:grid;grid-template-columns:repeat(2,1fr);gap:10px}}.fact{{background:#fff;border:1px solid var(--line);border-radius:12px;padding:10px}}.fact small{{display:block;color:var(--muted)}}.matrix-wrap{{display:none;overflow:auto;padding:18px}}table{{border-collapse:collapse;width:100%}}th,td{{border:1px solid var(--line);padding:10px;text-align:left;vertical-align:top}}th{{background:#edf2f8;color:var(--navy)}}.matrix td{{text-align:center;min-width:100px}}.matrix .count{{display:inline-grid;place-items:center;width:34px;height:34px;border-radius:50%;background:#ffe5f0;color:#a40048;font-weight:800}}.insight{{margin-top:16px;padding:20px;display:grid;grid-template-columns:1fr 1fr;gap:28px}}.insight h2{{margin:0}}.insight li{{margin:7px 0}}.decision{{border-left:5px solid var(--pink);padding:12px 14px;background:#fff5fa}}.register{{margin-top:16px;padding:18px;overflow:auto}}.register h2{{margin-top:0}}.empty{{display:none;padding:60px;text-align:center;color:var(--muted)}}
@media(max-width:800px){{.page{{padding:18px 10px}}header{{display:block}}h1{{font-size:34px}}.lede{{text-align:left;margin-top:14px}}.metrics{{grid-template-columns:1fr 1fr}}.toolbar{{position:static}}label,label input,label select{{width:100%;min-width:0}}.spacer{{display:none}}.detail,.insight{{grid-template-columns:1fr}}.register table thead{{display:none}}.register table,.register tbody,.register tr,.register td{{display:block;width:100%}}.register tr{{border:1px solid var(--line);margin-bottom:12px;border-radius:12px;overflow:hidden}}.register td{{border:0;border-bottom:1px solid #edf2f8}}.register td:before{{content:attr(data-label);display:block;font-size:10px;font-weight:800;color:var(--muted)}}}}
@media print{{body{{border:0;background:#fff}}.page{{padding:0}}.toolbar{{position:static;box-shadow:none}}.toolbar label,.toolbar button:not(.active),.tabs{{display:none}}.workspace,.metric,.insight,.register{{break-inside:avoid}}#graph{{transform:none!important}}}}
</style></head><body><main class="page"><header><div><div class="eyebrow">{esc(data['presentation']['eyebrow'].upper())}</div><h1>{esc(data['presentation']['headline'])}</h1></div><div class="lede">{esc(data['presentation']['lede'])}</div></header>
<section class="metrics">{''.join(f'<div class="metric"><span>{esc(m["label"])}</span><b>{esc(m["value"])}</b><small>{esc(m["note"])}</small></div>' for m in data['presentation']['metrics'])}</section>
<section class="toolbar" aria-label="Dependency controls"><label>FIND HANDOFF<input id="search" type="search" placeholder="ID, handoff, owner"></label><label>STATUS<select id="status"><option value="">All statuses</option>{''.join(f'<option value="{s}">{esc(s.replace("_"," ").title())}</option>' for s in STATUSES)}</select></label><label>PARTY<select id="party"><option value="">All parties</option>{''.join(f'<option value="{esc(n["id"])}">{esc(n["label"])}</option>' for n in data['nodes'])}</select></label><button class="button" id="gaps">Gaps only</button><button class="button" id="links">Hide other links</button><button class="button" id="reset">Reset</button><button class="button" id="minus" aria-label="Zoom out">−</button><button class="button" id="plus" aria-label="Zoom in">+</button><span class="spacer"></span><a class="button" id="fullSvg" download="dependency-network.svg">SVG</a><a class="button" id="fullJson" download="dependency-network.json">JSON</a><a class="button" id="fullCsv" download="dependency-network.csv">Full CSV</a><button class="button" id="export">Visible CSV</button><button class="button dark" id="print">Print / PDF</button></section>
<section class="workspace"><div class="view-head"><div><b id="count"></b><br><span>Arrow direction is provider → receiver. Select a handoff or node to inspect its evidence chain.</span></div><div class="tabs"><button class="button active" id="graphTab">Graph</button><button class="button" id="matrixTab">DSM matrix</button></div></div><div class="graph-shell" id="graphShell"><svg id="graph" role="img" aria-label="Interactive provider-to-receiver dependency graph"></svg><div class="empty" id="empty">No dependencies match the current filters.</div></div><div class="matrix-wrap" id="matrix"></div><div class="detail" id="detail" aria-live="polite"></div></section>
<section class="insight"><div><div class="eyebrow">READOUT</div><h2>{esc(data['presentation']['insight_heading'])}</h2><ul>{''.join(f'<li>{esc(p)}</li>' for p in data['presentation']['insight_points'])}</ul></div><div><div class="decision">{esc(data['presentation']['decision'])}</div><p><b>Method boundary.</b> {esc(data['analysis']['method'])}</p><p><b>As of/source.</b> {esc(data['as_of'])} · {esc(data['source'])}</p></div></section>
<section class="register"><h2>Accessible dependency register</h2><table id="register"><thead><tr><th>ID</th><th>Provider → receiver</th><th>Handoff / usable criteria</th><th>Dates / margin</th><th>State</th><th>Evidence</th></tr></thead><tbody></tbody></table></section></main>
<script>const DATA={payload},FULL_SVG={svg_json},FULL_CSV={csv_json};const $=s=>document.querySelector(s),NS='http://www.w3.org/2000/svg';const nodeMap=Object.fromEntries(DATA.nodes.map(n=>[n.id,n]));let selected=DATA.presentation.default_dependency_id,onlyGaps=false,hideOthers=false,zoom=1,view='graph';
const e=s=>String(s??'').replace(/[&<>"']/g,c=>({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c]));const margin=d=>d.needed_by&&d.forecast?Math.round((Date.parse(d.needed_by)-Date.parse(d.forecast))/86400000):null;const cat=d=>d.acceptance_state==='accepted'||d.status==='accepted'?'closed':d.status==='blocked'||d.acceptance_state==='verification_failed'?'blocked':margin(d)!==null&&margin(d)<0?'gap':d.status==='at_risk'?'at_risk':d.status==='unconfirmed'||!d.needed_by||!d.forecast?'unconfirmed':'watch';const colors={{gap:'#d80b61',blocked:'#b42318',at_risk:'#b54708',unconfirmed:'#667085',watch:'#08766c',closed:'#286645'}};const marginText=d=>margin(d)===null?'not calculable':`${{margin(d)>0?'+':''}}${{margin(d)}} calendar days`;
function visible(){{let q=$('#search').value.trim().toLowerCase(),s=$('#status').value,p=$('#party').value;return DATA.dependencies.filter(d=>(!q||[d.id,d.handoff,d.usable_criteria,d.owner,d.receiver_owner,nodeMap[d.provider].label,nodeMap[d.receiver].label].join(' ').toLowerCase().includes(q))&&(!s||d.status===s)&&(!p||d.provider===p||d.receiver===p)&&(!onlyGaps||cat(d)==='gap'||cat(d)==='blocked'));}}
function ranks(deps,nodes){{let incoming=Object.fromEntries(nodes.map(n=>[n.id,0])),out=Object.fromEntries(nodes.map(n=>[n.id,[]]));deps.forEach(d=>{{out[d.provider].push(d.receiver);incoming[d.receiver]++}});let r=Object.fromEntries(nodes.map(n=>[n.id,0])),q=nodes.filter(n=>incoming[n.id]===0).map(n=>n.id),seen=new Set;while(q.length){{let a=q.shift();seen.add(a);out[a].forEach(b=>{{r[b]=Math.max(r[b],r[a]+1);if(--incoming[b]===0)q.push(b)}})}}let mx=Math.max(0,...Object.values(r));nodes.forEach(n=>{{if(!seen.has(n.id))r[n.id]=mx+1}});return r}}
function renderGraph(deps){{let svg=$('#graph'),used=new Set(deps.flatMap(d=>[d.provider,d.receiver])),nodes=DATA.nodes.filter(n=>used.has(n.id));svg.innerHTML='<defs><filter id="s" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="5" stdDeviation="6" flood-color="#0b1f40" flood-opacity=".12"/></filter><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="context-stroke"/></marker></defs>';if(!deps.length){{svg.style.display='none';$('#empty').style.display='block';return}}svg.style.display='block';$('#empty').style.display='none';let rr=ranks(deps,nodes),cols={{}};nodes.forEach(n=>(cols[rr[n.id]]??=[]).push(n));let pos={{}};Object.entries(cols).forEach(([c,arr])=>arr.forEach((n,i)=>pos[n.id]=[60+Number(c)*430,90+i*145]));let w=Math.max(980,120+(Math.max(...Object.keys(cols).map(Number))+1)*430),h=Math.max(500,180+Math.max(...Object.values(cols).map(a=>a.length))*145);svg.setAttribute('viewBox',`0 0 ${{w}} ${{h}}`);svg.setAttribute('width',w*zoom);svg.setAttribute('height',h*zoom);let active=deps.find(d=>d.id===selected),related=new Set(active?[active.provider,active.receiver]:[]),pairTotals={{}},pairSeen={{}};deps.forEach(d=>{{let p=d.provider+'|'+d.receiver;pairTotals[p]=(pairTotals[p]||0)+1;pairSeen[p]=0}});deps.forEach(d=>{{let p=d.provider+'|'+d.receiver,edgeOffset=(pairSeen[p]++-(pairTotals[p]-1)/2)*34,[x1,y1]=pos[d.provider],[x2,y2]=pos[d.receiver];x1+=240;y1+=45+edgeOffset;y2+=45+edgeOffset;let mid=(x1+x2)/2,g=document.createElementNS(NS,'g');g.setAttribute('class','edge '+((hideOthers&&active&&d.id!==selected&&!related.has(d.provider)&&!related.has(d.receiver))?'dim ':'')+(d.id===selected?'focus':''));g.setAttribute('tabindex','0');g.setAttribute('role','button');g.setAttribute('aria-label',`${{d.id}}: ${{nodeMap[d.provider].label}} to ${{nodeMap[d.receiver].label}}`);g.innerHTML=`<path d="M${{x1}} ${{y1}} C${{mid}} ${{y1}},${{mid}} ${{y2}},${{x2}} ${{y2}}" stroke="${{colors[cat(d)]}}" marker-end="url(#a)"/><path class="hit" d="M${{x1}} ${{y1}} C${{mid}} ${{y1}},${{mid}} ${{y2}},${{x2}} ${{y2}}"/><rect x="${{mid-67}}" y="${{(y1+y2)/2-17}}" width="134" height="27" rx="13" fill="#fff" stroke="${{colors[cat(d)]}}"/><text x="${{mid}}" y="${{(y1+y2)/2+1}}" text-anchor="middle" fill="${{colors[cat(d)]}}">${{e(d.id)}} · ${{e(marginText(d))}}</text>`;g.onclick=()=>{{selected=d.id;render()}};g.onkeydown=x=>{{if(x.key==='Enter'||x.key===' '){{x.preventDefault();g.dispatchEvent(new MouseEvent('click',{{bubbles:true}}))}}}};svg.appendChild(g)}});nodes.forEach(n=>{{let [x,y]=pos[n.id],g=document.createElementNS(NS,'g'),incident=deps.some(d=>d.id===selected&&(d.provider===n.id||d.receiver===n.id));g.setAttribute('class','node '+(incident?'selected ':'')+(hideOthers&&active&&!related.has(n.id)?'dim':''));g.setAttribute('transform',`translate(${{x}} ${{y}})`);g.setAttribute('tabindex','0');g.setAttribute('role','button');g.setAttribute('aria-label',n.label);g.innerHTML=`<rect width="240" height="90" rx="14" filter="url(#s)"/><rect class="rail" width="7" height="90" rx="3"/><text x="20" y="24" font-size="10" font-weight="800" fill="#d80b61">${{e(n.kind.toUpperCase())}}</text><text x="20" y="49" font-size="16" font-weight="800" fill="#0c234b">${{e(n.label.slice(0,27))}}</text><text x="20" y="72" font-size="11" fill="#667085">Owner: ${{e(n.owner.slice(0,28))}}</text>`;g.onclick=()=>{{let first=deps.find(d=>d.provider===n.id||d.receiver===n.id);if(first){{selected=first.id;render()}}}};g.onkeydown=x=>{{if(x.key==='Enter'||x.key===' '){{x.preventDefault();g.dispatchEvent(new MouseEvent('click',{{bubbles:true}}))}}}};svg.appendChild(g)}})}}
function renderDetail(deps){{let d=deps.find(x=>x.id===selected)||deps[0];if(!d){{$('#detail').innerHTML='<p>Select broader filters to inspect a handoff.</p>';return}}selected=d.id;$('#detail').innerHTML=`<div><span class="tag">${{e(d.id)}}</span><span class="tag">${{e(cat(d).replace('_',' '))}}</span><h2>${{e(d.handoff)}}</h2><p><b>${{e(nodeMap[d.provider].label)}} → ${{e(nodeMap[d.receiver].label)}}</b></p><p>${{e(d.usable_criteria)}}</p><p><b>Evidence:</b> ${{e(d.source)}}</p></div><div class="facts"><div class="fact"><small>Needed by</small><b>${{e(d.needed_by||'unknown')}}</b></div><div class="fact"><small>Forecast</small><b>${{e(d.forecast||'unknown')}}</b></div><div class="fact"><small>Local margin</small><b>${{e(marginText(d))}}</b></div><div class="fact"><small>Acceptance</small><b>${{e(d.acceptance_state.replaceAll('_',' '))}}</b></div><div class="fact"><small>Provider owner</small><b>${{e(d.owner)}}</b></div><div class="fact"><small>Receiver owner</small><b>${{e(d.receiver_owner)}}</b></div><div class="fact"><small>Committed date</small><b>${{e(d.committed||'not evidenced')}}</b></div><div class="fact"><small>Status</small><b>${{e(d.status.replaceAll('_',' '))}}</b></div></div>`}}
function renderMatrix(deps){{let ids=DATA.nodes.map(n=>n.id),counts={{}};deps.forEach(d=>counts[d.provider+'|'+d.receiver]=(counts[d.provider+'|'+d.receiver]||0)+1);$('#matrix').innerHTML=`<table class="matrix"><caption>Counts summarize visible handoffs; they do not measure effort or criticality.</caption><thead><tr><th>Provider ↓ / Receiver →</th>${{ids.map(i=>`<th>${{e(nodeMap[i].label)}}</th>`).join('')}}</tr></thead><tbody>${{ids.map(a=>`<tr><th>${{e(nodeMap[a].label)}}</th>${{ids.map(b=>`<td>${{counts[a+'|'+b]?`<span class="count">${{counts[a+'|'+b]}}</span>`:'·'}}</td>`).join('')}}</tr>`).join('')}}</tbody></table>`}}
function renderRegister(deps){{$('#register tbody').innerHTML=deps.map(d=>`<tr><td data-label="ID"><b>${{e(d.id)}}</b></td><td data-label="Provider → receiver">${{e(nodeMap[d.provider].label)}} → ${{e(nodeMap[d.receiver].label)}}</td><td data-label="Handoff / usable criteria"><b>${{e(d.handoff)}}</b><br>${{e(d.usable_criteria)}}</td><td data-label="Dates / margin">Need ${{e(d.needed_by||'unknown')}}<br>Forecast ${{e(d.forecast||'unknown')}}<br><b>${{e(marginText(d))}}</b></td><td data-label="State">${{e(d.status.replaceAll('_',' '))}}<br>${{e(d.acceptance_state.replaceAll('_',' '))}}</td><td data-label="Evidence">${{e(d.source)}}</td></tr>`).join('')}}
function render(){{let deps=visible();$('#count').textContent=`${{deps.length}} of ${{DATA.dependencies.length}} handoffs visible`;renderGraph(deps);renderDetail(deps);renderMatrix(deps);renderRegister(deps);$('#graphShell').style.display=view==='graph'?'block':'none';$('#matrix').style.display=view==='matrix'?'block':'none';$('#graphTab').classList.toggle('active',view==='graph');$('#matrixTab').classList.toggle('active',view==='matrix');}}
function resetControls(){{$('#search').value='';$('#status').value='';$('#party').value='';onlyGaps=false;hideOthers=false;zoom=1;selected=DATA.presentation.default_dependency_id;$('#gaps').classList.remove('active');$('#links').classList.remove('active');$('#links').textContent='Hide other links';render()}}function downloadLink(id,body,type){{$('#'+id).href=URL.createObjectURL(new Blob([body],{{type}}))}}downloadLink('fullSvg',FULL_SVG,'image/svg+xml');downloadLink('fullJson',JSON.stringify(DATA,null,2)+'\\n','application/json');downloadLink('fullCsv',FULL_CSV,'text/csv');$('#reset').onclick=resetControls;
['search','status','party'].forEach(id=>$('#'+id).addEventListener(id==='search'?'input':'change',render));$('#gaps').onclick=()=>{{onlyGaps=!onlyGaps;$('#gaps').classList.toggle('active',onlyGaps);render()}};$('#links').onclick=()=>{{hideOthers=!hideOthers;$('#links').classList.toggle('active',hideOthers);$('#links').textContent=hideOthers?'Show all links':'Hide other links';render()}};$('#minus').onclick=()=>{{zoom=Math.max(.65,zoom-.1);render()}};$('#plus').onclick=()=>{{zoom=Math.min(1.6,zoom+.1);render()}};$('#graphTab').onclick=()=>{{view='graph';render()}};$('#matrixTab').onclick=()=>{{view='matrix';render()}};$('#print').onclick=()=>window.print();$('#export').onclick=()=>{{let deps=visible(),rows=['dependency_id,provider,receiver,handoff,needed_by,forecast,local_margin_calendar_days,status,acceptance_state'];let q=v=>{{let s=String(v??'').replaceAll('"','""');if(typeof v==='string'&&/^[=+\\-@\\t\\r]/.test(s))s="'"+s;return `"${{s}}"`}};deps.forEach(d=>rows.push([d.id,nodeMap[d.provider].label,nodeMap[d.receiver].label,d.handoff,d.needed_by,d.forecast,margin(d),d.status,d.acceptance_state].map(q).join(',')));let a=document.createElement('a');a.href=URL.createObjectURL(new Blob([rows.join('\\n')+'\\n'],{{type:'text/csv'}}));a.download='dependency-map-visible.csv';a.click();URL.revokeObjectURL(a.href)}};document.addEventListener('keydown',x=>{{if(x.key==='Escape'){{$('#search').value='';$('#status').value='';$('#party').value='';onlyGaps=false;hideOthers=false;render()}}}});render();</script></body></html>'''


def demo():
    return validate({'title':'Dependency network demo','as_of':'2026-10-16','version':'1.0','source':'Fictional instructional demo','scope':'Three provider-to-receiver handoffs',
      'calendar':{'label':'Calendar days; no timezone conversion','unit':'calendar_days'},
      'nodes':[{'id':'VENDOR','label':'Vendor','kind':'vendor','owner':'Beck','source':'Demo'}, {'id':'PLATFORM','label':'Platform','kind':'team','owner':'Owner unconfirmed','source':'Demo'}, {'id':'INTEGRATION','label':'Integration','kind':'team','owner':'Omar','source':'Demo'}, {'id':'SECURITY','label':'Security','kind':'authority','owner':'Lena','source':'Demo'}],
      'dependencies':[{'id':'DEP-01','provider':'VENDOR','receiver':'PLATFORM','handoff':'Versioned export map','usable_criteria':'Version, exceptions and sample are documented.','needed_by':'2026-10-19','requested':'2026-10-18','committed':None,'commitment_source':None,'forecast':'2026-10-20','status':'at_risk','acceptance_state':'not_delivered','owner':'Beck','receiver_owner':'Owner unconfirmed','source':'Demo source','note':'Forecast is not a commitment.'},{'id':'DEP-02','provider':'PLATFORM','receiver':'INTEGRATION','handoff':'Reachable audit interface','usable_criteria':'Schema and representative events validate.','needed_by':'2026-10-20','requested':None,'committed':None,'commitment_source':None,'forecast':'2026-10-22','status':'in_progress','acceptance_state':'not_delivered','owner':'Owner unconfirmed','receiver_owner':'Omar','source':'Demo source','note':''},{'id':'DEP-03','provider':'INTEGRATION','receiver':'SECURITY','handoff':'Recovery evidence','usable_criteria':'Recovery flow is demonstrated and recorded.','needed_by':None,'requested':None,'committed':None,'commitment_source':None,'forecast':None,'status':'unconfirmed','acceptance_state':'unknown','owner':'Omar','receiver_owner':'Lena','source':'Demo source; dates unknown','note':''}],
      'presentation':{'eyebrow':'Dependency control','headline':'Interfaces before arrows','lede':'See who provides what, when the receiver needs it, and which evidence makes it usable.','default_dependency_id':'DEP-02','metrics':[{'label':'Handoffs','value':'3','note':'Supplied records'},{'label':'Negative gaps','value':'2','note':'Local calendar margin'},{'label':'Unconfirmed','value':'1','note':'Unknown dates retained'},{'label':'CPM claims','value':'0','note':'No integrated network'}],'insight_heading':'Reconcile the boundary first','insight_points':['Forecast and commitment remain distinct.','Delivery does not establish receiver acceptance.'],'decision':'Resolve DEP-02 timing and acceptance evidence before relying on the handoff.'},
      'analysis':{'method':'Rule-based coordination view from supplied dependency fields; local margins are not CPM float.','coordination_focus_ids':['DEP-02'],'critical_path':None},'notes':['Fictional instructional data.']})


def main(argv=None):
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('input',nargs='?');parser.add_argument('--demo',action='store_true');parser.add_argument('--output',help='Output stem without extension; omit to print SVG');args=parser.parse_args(argv)
    if args.demo == bool(args.input): parser.error('Provide exactly one input JSON or --demo')
    data=demo() if args.demo else validate(json.loads(Path(args.input).read_text(encoding='utf-8')))
    svg=render_svg(data);csv_text=render_csv(data)
    if not args.output:
        print(svg)
        return 0
    stem=Path(args.output);stem.parent.mkdir(parents=True,exist_ok=True)
    Path(str(stem)+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    Path(str(stem)+'.svg').write_text(svg,encoding='utf-8')
    Path(str(stem)+'.html').write_text(render_html(data,svg,csv_text),encoding='utf-8')
    Path(str(stem)+'.csv').write_text(csv_text,encoding='utf-8',newline='')
    print('Wrote '+', '.join(str(stem)+s for s in ('.html','.svg','.json','.csv')))
    return 0


if __name__ == '__main__': sys.exit(main())
