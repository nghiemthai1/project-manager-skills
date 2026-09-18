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

"""Render evidence-led project budgets to offline HTML, SVG, JSON and CSV.

The standard-library renderer keeps performance, ledger, forecast and funding
views distinct. It calculates supported EVM scenarios but never selects a
forecast, releases reserve or authorizes spending.
"""
import argparse
import base64
import csv
from datetime import date
import html
import io
import json
import math
from pathlib import Path
import sys
import textwrap

STATES=('confirmed','proposed','unknown')
OPTION_STATES=('open','proposed','approved','rejected')
FORECAST_IDS=('bottom_up','remaining_at_budget','cost_efficiency','combined_efficiency')

def esc(value): return html.escape(str(value),quote=True)
def _text(item,key,context,required=True):
    value=item.get(key)
    if not isinstance(value,str) or (required and not value.strip()):
        raise ValueError(f'{context} {key}: {"nonempty " if required else ""}text required')
def _number(value,context,nullable=False,positive=False):
    if nullable and value is None:return
    if type(value) not in (int,float) or not math.isfinite(float(value)) or value<0 or (positive and value<=0):
        raise ValueError(f'{context}: finite {"positive" if positive else "nonnegative"} number required')

def validate(data):
    if not isinstance(data,dict):raise ValueError('Expected a project-budget snapshot object')
    for key in ('title','version','as_of','source','scope','state','currency','scale'):_text(data,key,'snapshot')
    try:
        parsed=date.fromisoformat(data['as_of'])
        if parsed.isoformat()!=data['as_of']:raise ValueError
    except ValueError:raise ValueError('as_of must be an ISO date YYYY-MM-DD') from None
    baseline=data.get('baseline')
    if not isinstance(baseline,dict):raise ValueError('baseline is required')
    for key in ('id','approval','reserve_control','source'):_text(baseline,key,'baseline')
    for key in ('bac','management_reserve','total_envelope'):_number(baseline.get(key),f'baseline {key}',positive=key=='bac')
    if baseline['total_envelope']<baseline['bac']:raise ValueError('total_envelope cannot be below BAC')
    perf=data.get('performance')
    if not isinstance(perf,dict):raise ValueError('performance is required')
    for key in ('earning_rule','source'):_text(perf,key,'performance')
    for key in ('pv','ev','ac'):_number(perf.get(key),f'performance {key}')
    if perf['pv']>baseline['bac'] or perf['ev']>baseline['bac']:raise ValueError('PV and EV cannot exceed BAC in this renderer')
    categories=data.get('categories')
    if not isinstance(categories,list) or not categories:raise ValueError('categories must be a nonempty list')
    ids=set()
    for item in categories:
        if not isinstance(item,dict):raise ValueError('Each category must be an object')
        for key in ('id','label','status','source','note'):_text(item,key,'category',required=key!='note')
        if item['id'] in ids:raise ValueError(f'duplicate category id: {item["id"]}')
        ids.add(item['id'])
        if item['status'] not in STATES:raise ValueError(f'{item["id"]}: invalid status')
        _number(item.get('actual'),f'{item["id"]} actual')
        for key in ('committed_unspent','other_etc'):_number(item.get(key),f'{item["id"]} {key}',nullable=True)
        if item['status']=='unknown' and item['committed_unspent'] is not None and item['other_etc'] is not None:
            raise ValueError(f'{item["id"]}: unknown category must retain at least one null remaining amount')
    selected=data.get('recommended_forecast_id')
    if selected is not None and selected not in FORECAST_IDS:raise ValueError('recommended_forecast_id is invalid')
    options=data.get('funding_options',[])
    if not isinstance(options,list):raise ValueError('funding_options must be a list')
    option_ids=set()
    for item in options:
        if not isinstance(item,dict):raise ValueError('Each funding option must be an object')
        for key in ('id','label','amount','basis','effect','authority','status','source'):_text(item,key,'funding option')
        if item['id'] in option_ids:raise ValueError(f'duplicate funding option id: {item["id"]}')
        option_ids.add(item['id'])
        if item['status'] not in OPTION_STATES:raise ValueError(f'{item["id"]}: invalid option status')
    presentation=data.get('presentation')
    if not isinstance(presentation,dict):raise ValueError('presentation is required')
    for key in ('eyebrow','headline','lede','insight_heading','decision'):_text(presentation,key,'presentation')
    points=presentation.get('insight_points')
    if not isinstance(points,list) or not points or any(not isinstance(x,str) or not x.strip() for x in points):raise ValueError('insight_points must be nonempty text')
    analysis=data.get('analysis')
    if not isinstance(analysis,dict):raise ValueError('analysis is required')
    for key in ('method','accounting_boundary','authorization_boundary'):_text(analysis,key,'analysis')
    notes=data.get('notes',[])
    if not isinstance(notes,list) or any(not isinstance(x,str) for x in notes):raise ValueError('notes must be text entries')
    return data

def calculations(data):
    b,p=data['baseline'],data['performance'];pv,ev,ac,bac=p['pv'],p['ev'],p['ac'],b['bac']
    cpi=ev/ac if ac else None;spi=ev/pv if pv else None
    known_remaining=sum((x['committed_unspent'] or 0)+(x['other_etc'] or 0) for x in data['categories'])
    unknown=sum(x['committed_unspent'] is None for x in data['categories'])+sum(x['other_etc'] is None for x in data['categories'])
    actual_categories=sum(x['actual'] for x in data['categories'])
    forecasts={
      'bottom_up':None if unknown else ac+known_remaining,
      'remaining_at_budget':ac+bac-ev,
      'cost_efficiency':bac/cpi if cpi else None,
      'combined_efficiency':ac+(bac-ev)/(cpi*spi) if cpi and spi else None}
    return {'cv':ev-ac,'sv':ev-pv,'cpi':cpi,'spi':spi,'known_remaining':known_remaining,
      'unknown_remaining_fields':unknown,'category_actual':actual_categories,'ledger_difference':ac-actual_categories,
      'forecasts':forecasts}

def spreadsheet_text(value):
    text='' if value is None else str(value)
    return "'"+text if isinstance(value,str) and text.startswith(('=','+','-','@','\t','\r')) else text

def render_csv(data):
    validate(data);calc=calculations(data);stream=io.StringIO(newline='');w=csv.writer(stream,lineterminator='\n')
    w.writerow(['category_id','category','actual','committed_unspent','other_etc','known_category_total','status','source','note','currency','scale','as_of','baseline_id','bac','management_reserve','total_envelope','pv','ev','ac','ledger_difference'])
    for item in data['categories']:
        known=item['actual']+(item['committed_unspent'] or 0)+(item['other_etc'] or 0)
        values=[item['id'],item['label'],item['actual'],item['committed_unspent'],item['other_etc'],known,item['status'],item['source'],item['note'],data['currency'],data['scale'],data['as_of'],data['baseline']['id'],data['baseline']['bac'],data['baseline']['management_reserve'],data['baseline']['total_envelope'],data['performance']['pv'],data['performance']['ev'],data['performance']['ac'],calc['ledger_difference']]
        w.writerow([spreadsheet_text(x) for x in values])
    return stream.getvalue()

def _svg_text(x,y,value,size=13,fill='#13294b',weight='400',anchor=None):
    a=f' text-anchor="{anchor}"' if anchor else ''
    return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" fill="{fill}" font-weight="{weight}"{a}>{esc(value)}</text>'

def render_svg(data):
    validate(data);calc=calculations(data);b,p=data['baseline'],data['performance'];width=1440
    names={'actual':'Actual cost','bac':'Performance baseline','envelope':'Funding envelope','bottom_up':'Bottom-up EAC','remaining_at_budget':'Remaining-at-budget EAC','cost_efficiency':'Cost-efficiency EAC','combined_efficiency':'Combined-efficiency EAC'}
    rows=[('actual',p['ac']),('bac',b['bac']),('envelope',b['total_envelope'])]+[(k,calc['forecasts'][k]) for k in FORECAST_IDS]
    maximum=max([x for _,x in rows if x is not None]+[1]);bar_x,bar_w=390,850;height=420+len(rows)*62
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
      f'<title id="title">{esc(data["title"])}</title>',f'<desc id="desc">Project budget comparison as of {esc(data["as_of"])}. Bars compare overlapping financial views and are not additive.</desc>',
      '<rect width="100%" height="100%" fill="#f5f7fb"/><rect width="12" height="100%" fill="#173b2d"/>',
      _svg_text(38,42,data['presentation']['eyebrow'].upper(),12,'#d80b61','800'),_svg_text(38,96,data['presentation']['headline'],40,'#0c234b','800'),_svg_text(38,130,data['presentation']['lede'],15,'#536581')]
    metrics=[('BAC',b['bac'],b['id']),('Actual',p['ac'],'at cutoff'),('CPI',calc['cpi'],'cost efficiency'),('SPI',calc['spi'],'value progress'),('Ledger difference',calc['ledger_difference'],'AC less category actual')]
    for i,(label,value,note) in enumerate(metrics):
        x=38+i*270;display='Unavailable' if value is None else (f'{value:.3f}' if label in ('CPI','SPI') else f'{value:g}')
        out += [f'<rect x="{x}" y="166" width="252" height="90" rx="14" fill="#fff" stroke="#ccd6e5"/>',_svg_text(x+15,190,label.upper(),10,'#667085','800'),_svg_text(x+15,222,display,23,'#0c234b','800'),_svg_text(x+15,242,note,10,'#667085')]
    y=300;palette={'actual':'#176b87','bac':'#0c234b','envelope':'#08766c','bottom_up':'#c26716','remaining_at_budget':'#6f42a6','cost_efficiency':'#d80b61','combined_efficiency':'#b42318'}
    for key,value in rows:
        out += [_svg_text(38,y+23,names[key],13,'#13294b','700')]
        if value is None:out += [_svg_text(bar_x,y+23,'Unavailable: remaining estimate has unknown fields',12,'#a25b00','700')]
        else:
            w=value/maximum*bar_w
            out += [f'<rect x="{bar_x}" y="{y}" width="{max(2,w)}" height="34" rx="7" fill="{palette[key]}"/>',_svg_text(min(bar_x+w+12,width-42),y+23,f'{value:g} {data["scale"]} {data["currency"]}',12,'#13294b','700','end' if bar_x+w+12>=width-42 else None)]
        y+=62
    decision_y=y+24
    out += [_svg_text(38,decision_y,'DECISION',10,'#d80b61','800')]
    for i,line in enumerate(textwrap.wrap(data['presentation']['decision'],150,break_long_words=False)[:3]):out.append(_svg_text(38,decision_y+24+i*18,line,12,'#13294b','600'))
    out += [_svg_text(38,decision_y+82,f'As of {data["as_of"]} · {data["state"]} · amounts in {data["scale"]} {data["currency"]}',10,'#667085'),'</svg>']
    return ''.join(out)

def _safe_json(value):return json.dumps(value,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c').replace('>','\\u003e').replace('&','\\u0026')
def _data_uri(text,media_type):return f'data:{media_type};base64,'+base64.b64encode(text.encode()).decode()

def render_html(data,svg=None,csv_text=None):
    validate(data);svg=svg or render_svg(data);csv_text=csv_text or render_csv(data)
    page=r'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>__TITLE__</title><style>
:root{--navy:#0c234b;--ink:#13294b;--muted:#60708a;--line:#cfdae9;--bg:#f3f6fa;--pink:#d80b61;--green:#08766c;--red:#b42318;--shadow:0 12px 30px rgba(12,35,75,.09)}*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 Arial,sans-serif;border-left:10px solid #173b2d}button,input,select,textarea{font:inherit;color:inherit}button,.button{border:1px solid #b9c8dc;border-radius:12px;background:#fff;padding:11px 14px;font-weight:700;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center;justify-content:center}.primary{background:var(--navy);color:#fff}.accent{border-color:var(--pink);color:#a60049;background:#fff5f9}.active{box-shadow:0 0 0 3px #ffb8d6;border-color:var(--pink)}button:focus-visible,.button:focus-visible,input:focus-visible,select:focus-visible,textarea:focus-visible,[tabindex]:focus-visible{outline:3px solid #79a8e8;outline-offset:2px}.hero{padding:28px 32px 20px;display:grid;grid-template-columns:minmax(0,1fr) minmax(300px,640px);gap:28px;align-items:end}.eyebrow{text-transform:uppercase;color:var(--pink);font-weight:800;letter-spacing:2px;font-size:12px}.hero h1{font-size:clamp(32px,4vw,52px);line-height:1.02;margin:16px 0 0}.hero .lede{color:var(--muted);font-size:17px;text-align:right;margin:0}.metrics{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;padding:0 30px 18px}.metric{background:#fff;border:1px solid var(--line);border-radius:14px;padding:13px 15px;box-shadow:var(--shadow)}.metric small{display:block;color:var(--muted);font-weight:800;text-transform:uppercase}.metric b{display:block;font-size:23px;margin-top:5px}.metric span{color:var(--muted);font-size:11px}.controls{margin:0 20px 16px;padding:16px 18px;background:#fff;border:1px solid var(--line);border-radius:18px;display:grid;grid-template-columns:minmax(210px,1.3fr) minmax(170px,.7fr) auto auto;gap:12px;align-items:end;box-shadow:var(--shadow)}label{font-weight:800;font-size:12px;color:#536581;text-transform:uppercase}input,select,textarea{display:block;width:100%;margin-top:5px;border:1px solid #b9c8dc;border-radius:10px;padding:10px 11px;background:#fff;min-height:42px}textarea{min-height:72px;resize:vertical}.control-actions{display:flex;gap:8px;flex-wrap:wrap}.scope{grid-column:1/-1;color:var(--muted);font-size:12px}.tabs{display:flex;gap:7px;margin:0 30px 13px;flex-wrap:wrap}.tab{border-radius:999px;padding:8px 13px}.view{margin:0 20px 18px;background:#fff;border:1px solid var(--line);border-radius:18px;box-shadow:var(--shadow);overflow:hidden}.view-head{padding:18px 20px;border-bottom:1px solid var(--line)}.view-head h2{margin:0 0 3px;font-size:20px}.view-head p{margin:0;color:var(--muted)}.chart{padding:15px 20px 24px}.bar-row{display:grid;grid-template-columns:280px minmax(360px,1fr) 190px;gap:15px;align-items:center;padding:10px 0}.bar-label b{display:block}.bar-label small{color:var(--muted)}.bar-track{height:36px;background:#e8edf4;border-radius:8px;overflow:hidden}.bar{height:100%;border-radius:8px}.amount{text-align:right;font-weight:800}.amount small{display:block;color:var(--muted);font-weight:400}.gap{color:var(--red)}.okay{color:var(--green)}.scroll{overflow:auto}.data-table{width:100%;border-collapse:collapse;min-width:1080px}.data-table th,.data-table td{padding:11px 12px;border-bottom:1px solid #dce4ef;text-align:left;vertical-align:top}.data-table th{background:#edf2f8;color:#536581;font-size:11px;text-transform:uppercase}.data-table tbody tr:hover,.data-table tbody tr.edited{background:#fff4f9}.cards{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;padding:18px}.card{border:1px solid var(--line);border-radius:14px;padding:15px}.card h3{margin:4px 0 8px}.card p{margin:5px 0;color:var(--muted)}.card small{color:var(--pink);font-weight:800}.detail{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(360px,.9fr);gap:18px;margin:0 20px 18px}.panel{background:#fff;border:1px solid var(--line);border-radius:18px;padding:18px 20px;box-shadow:var(--shadow)}.panel h2{margin:0 0 8px}.facts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px}.fact{border:1px solid #d8e1ed;border-radius:11px;padding:10px}.fact small{display:block;text-transform:uppercase;color:var(--muted);font-size:9px;font-weight:800}.fact b{display:block;margin-top:4px}.editor{border-top:5px solid var(--pink)}.editor[hidden]{display:none}.form-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}.wide{grid-column:1/-1}.cat-edit{border:1px solid #d4deeb;border-radius:12px;padding:10px;margin:10px 0}.cat-edit .form-grid{grid-template-columns:1fr repeat(3,.65fr)}.editor-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px}.error{min-height:20px;color:var(--red);font-weight:700}.notice{margin:0 20px 18px;padding:14px 18px;border:1px solid #efc17c;background:#fff7e6;border-radius:14px;color:#69420b}.history{max-height:180px;overflow:auto;padding-left:19px;color:var(--muted)}.empty{padding:40px;text-align:center;color:var(--muted)}footer{padding:8px 30px 30px;color:var(--muted);font-size:11px}
@media(max-width:900px){body{border-left-width:6px}.hero{grid-template-columns:1fr;padding:22px 18px 16px}.hero .lede{text-align:left}.metrics{grid-template-columns:repeat(2,1fr);padding:0 16px 15px}.controls{margin:0 10px 14px;grid-template-columns:1fr 1fr}.tabs{margin:0 16px 12px}.view,.detail{margin-left:10px;margin-right:10px}.chart{overflow-x:auto}.bar-row{grid-template-columns:210px 400px 150px}.detail{grid-template-columns:1fr}.cards{grid-template-columns:1fr}.form-grid{grid-template-columns:repeat(2,1fr)}.cat-edit .form-grid{grid-template-columns:1fr 1fr}}@media(max-width:520px){.metrics{grid-template-columns:1fr 1fr}.controls{grid-template-columns:1fr}.bar-row{grid-template-columns:165px 340px 120px}.form-grid,.cat-edit .form-grid{grid-template-columns:1fr}.wide{grid-column:1}.hero h1{font-size:34px}}@media print{body{border:0;background:#fff}.controls,.tabs,.editor,#historyPanel{display:none!important}.view,.panel{box-shadow:none;margin:8px 0}.hero{padding:12px 0}.metrics{padding:0}.notice{margin:8px 0}}</style></head><body>
<header class="hero"><div><div class="eyebrow">__EYEBROW__</div><h1>__HEADLINE__</h1></div><p class="lede">__LEDE__</p></header>
<section class="metrics"><div class="metric"><small>BAC</small><b id="mBac"></b><span id="mBaseline"></span></div><div class="metric"><small>Actual cost</small><b id="mAc"></b><span>at accounting cut-off</span></div><div class="metric"><small>CPI / SPI</small><b id="mRatios"></b><span>cost / value-progress ratios</span></div><div class="metric"><small>Selected EAC</small><b id="mEac"></b><span id="mMethod"></span></div><div class="metric"><small>Funding gap</small><b id="mGap"></b><span>to total envelope</span></div></section>
<section class="controls"><label>Find category or option<input id="search" type="search" placeholder="Search cost, evidence or authority"></label><label>Scenario<select id="scenario"><option value="">All forecast scenarios</option><option value="gap">Above funding envelope</option><option value="within">Within funding envelope</option><option value="unavailable">Unavailable</option></select></label><button id="editToggle" class="accent">Edit local draft</button><div class="control-actions"><button id="reset">Reset view</button><button id="print" class="primary">Print / PDF</button></div><div class="scope" id="scope"></div></section>
<nav class="tabs"><button id="forecastTab" class="tab active">Forecast comparison</button><button id="ledgerTab" class="tab">Cost register</button><button id="performanceTab" class="tab">Performance math</button><button id="fundingTab" class="tab">Funding decisions</button></nav>
<section class="view" id="forecastView"><div class="view-head"><h2>Overlapping cost and funding views</h2><p>Bars share a zero-based scale. They compare amounts and must not be stacked as additive spend.</p></div><div class="chart" id="chart"></div></section>
<section class="view" id="ledgerView" hidden><div class="view-head"><h2>Cost category register</h2><p>Actual, committed-but-unspent and other ETC remain separate so obligations are counted once.</p></div><div class="scroll"><table class="data-table" id="ledger"><thead><tr><th>Category</th><th>Actual</th><th>Committed unspent</th><th>Other ETC</th><th>Known total</th><th>Status</th><th>Evidence</th></tr></thead><tbody></tbody></table></div></section>
<section class="view" id="performanceView" hidden><div class="view-head"><h2>Performance and scenario math</h2><p>SV is value in __CURRENCY__, not calendar delay. A ratio is unavailable when its denominator is zero.</p></div><div class="cards" id="performanceCards"></div></section>
<section class="view" id="fundingView" hidden><div class="view-head"><h2>Funding and scope options</h2><p>Forecast, reserve and spending authority remain separate controls.</p></div><div class="cards" id="fundingCards"></div></section>
<div class="notice" id="draftNotice" hidden><b>Local draft:</b> financial arithmetic is recalculated here. Source decision options and the selected management forecast must be revalidated after edits.</div>
<section class="detail"><article class="panel"><h2>Control boundary</h2><div class="facts" id="facts"></div><p><b>Accounting boundary:</b> __ACCOUNTING__</p><p><b>Authorization boundary:</b> __AUTH__</p><p><b>Decision:</b> __DECISION__</p></article>
<form class="panel editor" id="budgetEditor" hidden><h2>Edit financial draft</h2><p>Changes stay in this browser. Baseline and category IDs remain stable.</p><div class="form-grid"><label>BAC<input id="editBac" type="number" min="0" step="0.01"></label><label>Management reserve<input id="editReserve" type="number" min="0" step="0.01"></label><label>Total envelope<input id="editEnvelope" type="number" min="0" step="0.01"></label><label>PV<input id="editPv" type="number" min="0" step="0.01"></label><label>EV<input id="editEv" type="number" min="0" step="0.01"></label><label>AC<input id="editAc" type="number" min="0" step="0.01"></label><label>Selected forecast<select id="editRecommended"><option value="">None / conditional</option><option value="bottom_up">Bottom-up</option><option value="remaining_at_budget">Remaining at budget</option><option value="cost_efficiency">Cost efficiency</option><option value="combined_efficiency">Combined efficiency</option></select></label><label class="wide">Earning rule<textarea id="editEarning"></textarea></label><label class="wide">Performance evidence<textarea id="editPerformanceSource"></textarea></label></div><h3>Cost categories</h3><div id="categoryEditor"></div><p class="error" id="editError"></p><div class="editor-actions"><button class="primary" type="submit" id="saveBudget">Save local draft</button><button type="button" id="closeEditor">Close</button></div></form></section>
<section class="detail"><article class="panel"><h2>Evidence basis</h2><p><b>Method:</b> __METHOD__</p><p><b>Baseline approval:</b> __APPROVAL__</p><p><b>Reserve control:</b> __RESERVE_CONTROL__</p></article><article class="panel" id="historyPanel"><h2>Local history</h2><div class="editor-actions"><button id="undoEdit">Undo last edit</button><button id="discardDraft">Restore source snapshot</button></div><ol class="history" id="history"></ol></article></section>
<footer><div class="control-actions"><a class="button" id="fullSvg" download="project-budget.svg">Source SVG</a><a class="button" id="fullJson" download="project-budget.json">Source JSON</a><a class="button" id="fullCsv" download="project-budget.csv">Source CSV</a><button id="draftJson">Draft JSON</button><button id="draftCsv">Draft CSV</button><button id="visibleCsv">Visible draft CSV</button></div><p>Source exports preserve the embedded snapshot. Draft exports do not approve spending, release reserve or write to a financial system.</p></footer>
<script>
const SOURCE_DATA=__DATA__,SOURCE_CSV=__CSV__,SOURCE_SVG=__SVG__,KEY='project-budget:'+SOURCE_DATA.title+':'+SOURCE_DATA.version;const clone=x=>JSON.parse(JSON.stringify(x));let DATA=clone(SOURCE_DATA),HISTORY=[],view='forecast',editMode=false,editMessage='';const $=q=>document.querySelector(q),e=x=>String(x??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b),fmt=x=>x===null||x===undefined?'Unavailable':Number(x).toLocaleString(undefined,{maximumFractionDigits:2}),money=x=>fmt(x)+' '+DATA.scale+' '+DATA.currency;
function calc(){let b=DATA.baseline,p=DATA.performance,cpi=p.ac?p.ev/p.ac:null,spi=p.pv?p.ev/p.pv:null,known=DATA.categories.reduce((s,x)=>s+(x.committed_unspent??0)+(x.other_etc??0),0),unknown=DATA.categories.reduce((s,x)=>s+(x.committed_unspent===null)+(x.other_etc===null),0),catActual=DATA.categories.reduce((s,x)=>s+x.actual,0),forecasts={bottom_up:unknown?null:p.ac+known,remaining_at_budget:p.ac+b.bac-p.ev,cost_efficiency:cpi?b.bac/cpi:null,combined_efficiency:cpi&&spi?p.ac+(b.bac-p.ev)/(cpi*spi):null};return{cv:p.ev-p.ac,sv:p.ev-p.pv,cpi,spi,known,unknown,catActual,ledgerDifference:p.ac-catActual,forecasts}}
const names={actual:'Actual cost',bac:'Performance baseline BAC',envelope:'Total funding envelope',bottom_up:'Bottom-up EAC',remaining_at_budget:'Remaining-at-budget EAC',cost_efficiency:'Cost-efficiency EAC',combined_efficiency:'Combined-efficiency EAC'},colors={actual:'#176b87',bac:'#0c234b',envelope:'#08766c',bottom_up:'#c26716',remaining_at_budget:'#6f42a6',cost_efficiency:'#d80b61',combined_efficiency:'#b42318'};
function changed(){return !same({baseline:DATA.baseline,performance:DATA.performance,categories:DATA.categories,recommended_forecast_id:DATA.recommended_forecast_id},{baseline:SOURCE_DATA.baseline,performance:SOURCE_DATA.performance,categories:SOURCE_DATA.categories,recommended_forecast_id:SOURCE_DATA.recommended_forecast_id})}
function rows(){let c=calc(),all=[{id:'actual',value:DATA.performance.ac,note:'incurred at cut-off'},{id:'bac',value:DATA.baseline.bac,note:DATA.baseline.id},{id:'envelope',value:DATA.baseline.total_envelope,note:'authorization boundary'},...Object.entries(c.forecasts).map(([id,value])=>({id,value,note:id==='bottom_up'?(c.unknown?c.unknown+' unknown remaining fields':'actual + current ETC'):'formula scenario'}))],filter=$('#scenario').value;return all.filter(x=>!filter||(filter==='unavailable'?x.value===null:filter==='gap'?x.value!==null&&x.value>DATA.baseline.total_envelope:x.value!==null&&x.value<=DATA.baseline.total_envelope))}
function renderMetrics(){let c=calc(),id=DATA.recommended_forecast_id,eac=id?c.forecasts[id]:null,gap=eac===null?null:eac-DATA.baseline.total_envelope;$('#mBac').textContent=money(DATA.baseline.bac);$('#mBaseline').textContent=DATA.baseline.id;$('#mAc').textContent=money(DATA.performance.ac);$('#mRatios').textContent=(c.cpi===null?'—':fmt(c.cpi))+' / '+(c.spi===null?'—':fmt(c.spi));$('#mEac').textContent=eac===null?'Conditional':money(eac);$('#mMethod').textContent=id?names[id]:'No scenario selected';$('#mGap').textContent=gap===null?'Unavailable':(gap>0?'+':'')+money(gap);$('#mGap').className=gap>0?'gap':'okay'}
function renderChart(){let items=rows(),max=Math.max(1,...items.filter(x=>x.value!==null).map(x=>x.value));$('#chart').innerHTML=items.length?items.map(x=>{let gap=x.value===null?null:x.value-DATA.baseline.total_envelope;return`<div class="bar-row"><div class="bar-label"><b>${e(names[x.id])}</b><small>${e(x.note)}</small></div><div class="bar-track">${x.value===null?'':`<div class="bar" style="width:${x.value/max*100}%;background:${colors[x.id]}"></div>`}</div><div class="amount ${gap>0?'gap':x.id.includes('efficiency')||x.id==='bottom_up'?'':'okay'}">${x.value===null?'Unavailable':money(x.value)}${x.id.includes('efficiency')||x.id==='bottom_up'||x.id==='remaining_at_budget'?`<small>${gap===null?'unknown gap':(gap>0?'+':'')+money(gap)+' vs envelope'}</small>`:''}</div></div>`}).join(''):'<div class="empty">No scenarios match the current filter.</div>'}
function visibleCategories(){let q=$('#search').value.trim().toLowerCase();return DATA.categories.filter(x=>!q||[x.label,x.source,x.note,x.status].join(' ').toLowerCase().includes(q))}
function renderLedger(){let items=visibleCategories();$('#ledger tbody').innerHTML=items.map(x=>`<tr tabindex="0" class="${changed()?'edited':''}"><td><b>${e(x.label)}</b><br><small>${e(x.id)}</small></td><td>${money(x.actual)}</td><td>${x.committed_unspent===null?'Unknown':money(x.committed_unspent)}</td><td>${x.other_etc===null?'Unknown':money(x.other_etc)}</td><td><b>${money(x.actual+(x.committed_unspent??0)+(x.other_etc??0))}</b></td><td>${e(x.status)}</td><td>${e(x.source)}<br><small>${e(x.note)}</small></td></tr>`).join('')}
function renderPerformance(){let c=calc(),cards=[['CV',c.cv,'EV − AC; monetary variance'],['SV',c.sv,'EV − PV; not calendar days'],['CPI',c.cpi,'EV / AC'],['SPI',c.spi,'EV / PV'],['Actual reconciliation',c.ledgerDifference,'AC less category actual'],['Unknown remaining fields',c.unknown,'excluded from bottom-up EAC']];$('#performanceCards').innerHTML=cards.map(x=>`<article class="card"><small>${e(x[0])}</small><h3>${x[1]===null?'Unavailable':fmt(x[1])}</h3><p>${e(x[2])}</p></article>`).join('')}
function renderFunding(){let q=$('#search').value.trim().toLowerCase(),items=DATA.funding_options.filter(x=>!q||Object.values(x).join(' ').toLowerCase().includes(q));$('#fundingCards').innerHTML=items.length?items.map(x=>`<article class="card"><small>${e(x.id)} · ${e(x.status)}</small><h3>${e(x.label)}</h3><p><b>Amount:</b> ${e(x.amount)}</p><p><b>Basis:</b> ${e(x.basis)}</p><p><b>Effect:</b> ${e(x.effect)}</p><p><b>Authority:</b> ${e(x.authority)}</p><p><b>Source:</b> ${e(x.source)}</p></article>`).join(''):'<div class="empty">No funding options match the current search.</div>'}
function renderFacts(){let c=calc();$('#facts').innerHTML=`<div class="fact"><small>PV</small><b>${money(DATA.performance.pv)}</b></div><div class="fact"><small>EV</small><b>${money(DATA.performance.ev)}</b></div><div class="fact"><small>AC</small><b>${money(DATA.performance.ac)}</b></div><div class="fact"><small>Reserve</small><b>${money(DATA.baseline.management_reserve)}</b></div><div class="fact"><small>Envelope</small><b>${money(DATA.baseline.total_envelope)}</b></div><div class="fact"><small>Known ETC</small><b>${money(c.known)}</b></div>`}
function categoryEditor(x){return`<div class="cat-edit" data-id="${e(x.id)}"><div class="form-grid"><label>Category<input class="c-label" value="${e(x.label)}"></label><label>Actual<input class="c-actual" type="number" min="0" step=".01" value="${x.actual}"></label><label>Committed unspent<input class="c-committed" type="number" min="0" step=".01" value="${x.committed_unspent??''}"></label><label>Other ETC<input class="c-etc" type="number" min="0" step=".01" value="${x.other_etc??''}"></label><label>Status<select class="c-status">${['confirmed','proposed','unknown'].map(s=>`<option ${s===x.status?'selected':''}>${s}</option>`).join('')}</select></label><label class="wide">Evidence<input class="c-source" value="${e(x.source)}"></label><label class="wide">Note<textarea class="c-note">${e(x.note)}</textarea></label></div></div>`}
function populateEditor(){let b=DATA.baseline,p=DATA.performance;$('#editBac').value=b.bac;$('#editReserve').value=b.management_reserve;$('#editEnvelope').value=b.total_envelope;$('#editPv').value=p.pv;$('#editEv').value=p.ev;$('#editAc').value=p.ac;$('#editRecommended').value=DATA.recommended_forecast_id||'';$('#editEarning').value=p.earning_rule;$('#editPerformanceSource').value=p.source;$('#categoryEditor').innerHTML=DATA.categories.map(categoryEditor).join('')}
function edited(){let next=clone(DATA);next.baseline.bac=Number($('#editBac').value);next.baseline.management_reserve=Number($('#editReserve').value);next.baseline.total_envelope=Number($('#editEnvelope').value);next.performance.pv=Number($('#editPv').value);next.performance.ev=Number($('#editEv').value);next.performance.ac=Number($('#editAc').value);next.performance.earning_rule=$('#editEarning').value.trim();next.performance.source=$('#editPerformanceSource').value.trim();next.recommended_forecast_id=$('#editRecommended').value||null;next.categories=[...document.querySelectorAll('.cat-edit')].map((row,i)=>{let old=DATA.categories[i],nullable=sel=>{let v=row.querySelector(sel).value.trim();return v===''?null:Number(v)};return{id:old.id,label:row.querySelector('.c-label').value.trim(),actual:Number(row.querySelector('.c-actual').value),committed_unspent:nullable('.c-committed'),other_etc:nullable('.c-etc'),status:row.querySelector('.c-status').value,source:row.querySelector('.c-source').value.trim(),note:row.querySelector('.c-note').value.trim()}});return next}
function validateDraft(d){let nums=[d.baseline.bac,d.baseline.management_reserve,d.baseline.total_envelope,d.performance.pv,d.performance.ev,d.performance.ac];if(nums.some(x=>!Number.isFinite(x)||x<0)||d.baseline.bac<=0)return'Financial amounts must be finite and nonnegative; BAC must be positive.';if(d.baseline.total_envelope<d.baseline.bac)return'Total funding envelope cannot be below BAC.';if(d.performance.pv>d.baseline.bac||d.performance.ev>d.baseline.bac)return'PV and EV cannot exceed BAC.';if(!d.performance.earning_rule||!d.performance.source)return'Earning rule and performance evidence are required.';for(let x of d.categories){if(!x.label||!x.source)return'Every category needs a label and evidence source.';if(!Number.isFinite(x.actual)||x.actual<0||[x.committed_unspent,x.other_etc].some(v=>v!==null&&(!Number.isFinite(v)||v<0)))return'Category amounts must be nonnegative or blank where unknown.';if(x.status==='unknown'&&x.committed_unspent!==null&&x.other_etc!==null)return'Unknown categories must keep at least one remaining amount blank.'}return''}
function renderHistory(){$('#history').innerHTML=HISTORY.length?HISTORY.slice().reverse().map(x=>`<li>${e(x.at)} · financial draft</li>`).join(''):'<li>No local edits in this browser.</li>';$('#undoEdit').disabled=!HISTORY.length;$('#discardDraft').disabled=!changed()&&!HISTORY.length}
function setView(){for(let name of ['forecast','ledger','performance','funding']){$('#'+name+'View').hidden=view!==name;$('#'+name+'Tab').classList.toggle('active',view===name)}}
function render(){renderMetrics();renderChart();renderLedger();renderPerformance();renderFunding();renderFacts();renderHistory();setView();let c=calc();$('#scope').textContent=`${rows().length} comparison rows · ${visibleCategories().length} / ${DATA.categories.length} cost categories visible · ${c.unknown} unknown remaining fields · ${changed()?'local draft active':'source snapshot'}`;$('#draftNotice').hidden=!changed();$('#budgetEditor').hidden=!editMode;if(editMode&&!$('#budgetEditor').matches(':focus-within'))populateEditor();$('#editError').textContent=editMessage}
function draftSnapshot(){let out=clone(DATA);out.local_draft={base_version:SOURCE_DATA.version,changed:changed(),history_entries:HISTORY.length,exported_at:new Date().toISOString(),notice:'Browser-local proposal; no spending or reserve authority is implied.'};return out}
function csvText(items=DATA.categories){let q=x=>{x=x??'';x=String(x);if(/^[=+\-@\t\r]/.test(x))x="'"+x;return/[",\n]/.test(x)?'"'+x.replaceAll('"','""')+'"':x},c=calc(),head=['category_id','category','actual','committed_unspent','other_etc','known_category_total','status','source','note','currency','scale','as_of','baseline_id','bac','management_reserve','total_envelope','pv','ev','ac','ledger_difference'];return[head,...items.map(x=>[x.id,x.label,x.actual,x.committed_unspent,x.other_etc,x.actual+(x.committed_unspent??0)+(x.other_etc??0),x.status,x.source,x.note,DATA.currency,DATA.scale,DATA.as_of,DATA.baseline.id,DATA.baseline.bac,DATA.baseline.management_reserve,DATA.baseline.total_envelope,DATA.performance.pv,DATA.performance.ev,DATA.performance.ac,c.ledgerDifference])].map(row=>row.map(q).join(',')).join('\n')+'\n'}
function download(name,body,type){let a=document.createElement('a');a.href=URL.createObjectURL(new Blob([body],{type}));a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(a.href),500)}
function persist(){localStorage.setItem(KEY,JSON.stringify({baseline:DATA.baseline,performance:DATA.performance,categories:DATA.categories,recommended_forecast_id:DATA.recommended_forecast_id,history:HISTORY}))}
function loadDraft(){try{let x=JSON.parse(localStorage.getItem(KEY));if(x&&x.baseline&&x.performance&&Array.isArray(x.categories)&&x.categories.length===SOURCE_DATA.categories.length){Object.assign(DATA,{baseline:x.baseline,performance:x.performance,categories:x.categories,recommended_forecast_id:x.recommended_forecast_id});HISTORY=Array.isArray(x.history)?x.history.slice(-200):[]}}catch(error){localStorage.removeItem(KEY)}}
$('#budgetEditor').onsubmit=event=>{event.preventDefault();let before={baseline:clone(DATA.baseline),performance:clone(DATA.performance),categories:clone(DATA.categories),recommended_forecast_id:DATA.recommended_forecast_id},next=edited(),error=validateDraft(next);if(error){editMessage=error;$('#editError').textContent=error;return}let after={baseline:next.baseline,performance:next.performance,categories:next.categories,recommended_forecast_id:next.recommended_forecast_id};if(same(before,after)){editMessage='No changes to save.';$('#editError').textContent=editMessage;return}Object.assign(DATA,after);HISTORY.push({before,after:clone(after),at:new Date().toISOString()});HISTORY=HISTORY.slice(-200);editMessage='Local financial draft saved. Arithmetic recalculated; source exports remain unchanged.';persist();render()};
$('#editToggle').onclick=()=>{editMode=!editMode;editMessage=editMode?'Editing is local to this browser.':'';render();if(editMode)$('#editBac').focus()};$('#closeEditor').onclick=()=>{editMode=false;editMessage='';render()};$('#undoEdit').onclick=()=>{let x=HISTORY.pop();if(!x)return;Object.assign(DATA,clone(x.before));editMessage='Undid the last local financial edit.';persist();render()};$('#discardDraft').onclick=()=>{if(!confirm('Restore the embedded budget snapshot and clear local history?'))return;DATA=clone(SOURCE_DATA);HISTORY=[];localStorage.removeItem(KEY);editMessage='Source snapshot restored.';render()};
for(let name of ['forecast','ledger','performance','funding'])$('#'+name+'Tab').onclick=()=>{view=name;setView()};for(let id of ['search','scenario'])$('#'+id).addEventListener(id==='search'?'input':'change',render);$('#reset').onclick=()=>{$('#search').value='';$('#scenario').value='';view='forecast';render()};$('#print').onclick=()=>window.print();$('#fullSvg').href=SOURCE_SVG;$('#fullJson').href='data:application/json;base64,'+btoa(unescape(encodeURIComponent(JSON.stringify(SOURCE_DATA,null,2)+'\n')));$('#fullCsv').href='data:text/csv;base64,'+btoa(unescape(encodeURIComponent(SOURCE_CSV)));$('#draftJson').onclick=()=>download('project-budget-local-draft.json',JSON.stringify(draftSnapshot(),null,2)+'\n','application/json');$('#draftCsv').onclick=()=>download('project-budget-local-draft.csv',csvText(),'text/csv');$('#visibleCsv').onclick=()=>download('project-budget-visible-draft.csv',csvText(visibleCategories()),'text/csv');document.addEventListener('keydown',event=>{if(event.key==='Escape'){if(editMode){editMode=false;editMessage='';render()}else $('#reset').click()}});loadDraft();render();
</script></body></html>'''
    replacements={'__TITLE__':esc(data['title']),'__EYEBROW__':esc(data['presentation']['eyebrow']),'__HEADLINE__':esc(data['presentation']['headline']),'__LEDE__':esc(data['presentation']['lede']),'__CURRENCY__':esc(data['currency']),'__ACCOUNTING__':esc(data['analysis']['accounting_boundary']),'__AUTH__':esc(data['analysis']['authorization_boundary']),'__DECISION__':esc(data['presentation']['decision']),'__METHOD__':esc(data['analysis']['method']),'__APPROVAL__':esc(data['baseline']['approval']),'__RESERVE_CONTROL__':esc(data['baseline']['reserve_control']),'__DATA__':_safe_json(data),'__CSV__':_safe_json(csv_text),'__SVG__':_safe_json(_data_uri(svg,'image/svg+xml'))}
    for token,value in replacements.items():page=page.replace(token,value)
    return page

def demo():
    return validate({'title':'Project budget demo','version':'1.0','as_of':'2026-10-16','source':'Fictional instructional evidence','scope':'Relay B1 cost control snapshot','state':'conditional forecast','currency':'USD','scale':'k',
      'baseline':{'id':'B1','approval':'D-001 approved 2 October 2026','bac':100,'management_reserve':10,'total_envelope':110,'reserve_control':'Sponsor-controlled outside the performance baseline','source':'Decision D-001'},
      'performance':{'pv':50,'ev':40,'ac':48,'earning_rule':'Discrete deliverables and evidenced weighted milestones','source':'Fictional performance report through 16 October'},
      'categories':[{'id':'LABOR','label':'Internal delivery labor','actual':28,'committed_unspent':0,'other_etc':32,'status':'proposed','source':'Ledger L-16 and remaining estimate E-9','note':'ETC excludes support after handover.'},
                    {'id':'VENDOR','label':'Vendor services','actual':8,'committed_unspent':12,'other_etc':0,'status':'confirmed','source':'PO-20 reconciliation','note':'The 8 incurred is not repeated in the 12 unspent.'},
                    {'id':'PLATFORM','label':'Platform and tooling','actual':12,'committed_unspent':4,'other_etc':4,'status':'proposed','source':'Ledger L-16 and estimate E-9','note':''}],
      'recommended_forecast_id':'cost_efficiency',
      'funding_options':[{'id':'F-1','label':'Release original management reserve','amount':'10 k USD','basis':'Separately controlled reserve outside B1','effect':'Raises accessible funding only with the recorded release; does not erase cost variance.','authority':'Sponsor','status':'proposed','source':'D-001 control terms'},
                         {'id':'F-2','label':'Authorize additional funding','amount':'10 k USD beyond original envelope','basis':'Needed if the 120 k USD scenario is selected after ETC review','effect':'Would close the remaining gap to the scenario.','authority':'Sponsor / funding authority','status':'open','source':'Fictional 16 October decision request'}],
      'presentation':{'eyebrow':'Cost control','headline':'Forecast is evidence, not permission','lede':'Compare performance, remaining-work assumptions and the authorized envelope before choosing a funding or scope action.','insight_heading':'A 120k forecast exceeds both controls','insight_points':['20k above BAC.','10k above the original total envelope.'],'decision':'Reconcile the current ETC and obligations, then obtain an explicit reserve and additional-funding or scope decision.'},
      'analysis':{'method':'Cumulative EVM scenarios plus actual-and-remaining cost reconciliation at one status date.','accounting_boundary':'Actuals, unspent commitments and other ETC are separated; category actuals reconcile to AC.','authorization_boundary':'Forecasts do not release reserve or authorize spending.'},
      'notes':['Fictional instructional data; amounts are thousands of USD.']})

def main(argv=None):
    if hasattr(sys.stdout,'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8');sys.stderr.reconfigure(encoding='utf-8')
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('input',nargs='?');parser.add_argument('--demo',action='store_true');parser.add_argument('--output',help='Output stem without extension; omit to print SVG');args=parser.parse_args(argv)
    if args.demo==bool(args.input):parser.error('Provide exactly one input JSON or --demo')
    data=demo() if args.demo else validate(json.loads(Path(args.input).read_text(encoding='utf-8')))
    svg,csv_text=render_svg(data),render_csv(data)
    if not args.output:print(svg);return 0
    stem=Path(args.output);stem.parent.mkdir(parents=True,exist_ok=True)
    Path(str(stem)+'.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    Path(str(stem)+'.svg').write_text(svg,encoding='utf-8')
    Path(str(stem)+'.html').write_text(render_html(data,svg,csv_text),encoding='utf-8')
    Path(str(stem)+'.csv').write_text(csv_text,encoding='utf-8',newline='')
    print('Wrote '+', '.join(str(stem)+x for x in ('.html','.svg','.json','.csv')));return 0

if __name__=='__main__':sys.exit(main())
