import copy
import csv
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
HELPER = ROOT / 'skills/raci-matrix/scripts/render_raci.py'
spec = importlib.util.spec_from_file_location('raci_renderer', HELPER)
raci = importlib.util.module_from_spec(spec)
spec.loader.exec_module(raci)

def cell(code, state, note, source):
    return dict(code=code, state=state, note=note, source=source)

data = dict(title='Fictional handoff responsibility matrix', version='draft-1',
    as_of='unknown; not supplied', source='Fictional user request; minutes M-3 and M-4 as cited by requester',
    scope='H-7 handoff, H-8 archive task, H-9 purchase approval',
    state='Partially confirmed; unresolved and proposed assignments remain',
    roles=[dict(id='PM', label='PM'), dict(id='OPS', label='OPS')],
    rows=[
        dict(id='H-7',label='Handoff evidence and acceptance',cells={
            'PM':cell('R','confirmed','Prepare the evidence package; acceptance authority is separate','M-3'),
            'OPS':cell('?','unknown','Acceptance authority unresolved','Fictional user request')}),
        dict(id='H-8',label='Separate archive task',cells={
            'PM':cell('A/R','confirmed','Own and perform the archive task','M-4'),
            'OPS':cell('I','confirmed','Receive archive outcome; notification trigger not supplied','M-4')}),
        dict(id='H-9',label='Purchase approval',cells={
            'PM':cell('A','proposed','Proposed purchase approval authority; no preparation assignment','Fictional user request'),
            'OPS':cell('A','proposed','Proposed purchase approval authority; no preparation assignment','Fictional user request')})
    ], notes=['Fictional scenario. Source minutes are cited by the requester, not independently verified.',
       '? means unresolved; no explicit no-assignment cells were supplied. No R is assigned to H-9.',
       'Role-to-person mappings, confirmation dates, resolution authority and due dates were not supplied.',
       'H-7: confirm actual acceptance authority before acceptance; H-9: resolve competing A proposals and identify a preparer before purchase approval.'])
source = OUT / 'handoffs-source.json'
source.write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
run = subprocess.run([sys.executable,str(HELPER),str(source),'--output',str(OUT/'handoffs')],capture_output=True,text=True,encoding='utf-8')
assert run.returncode == 0, run.stderr
result=json.loads(run.stdout)
assert [f['id'] for f in result['findings']] == ['H-7','H-9']
assert 'No R assignment' in result['findings'][1]['findings']
assert '2 A assignments; confirm bounded ownership' in result['findings'][1]['findings']
assert json.loads((OUT/'handoffs.json').read_text(encoding='utf-8')) == data
records=list(csv.DictReader(io.StringIO((OUT/'handoffs.csv').read_text(encoding='utf-8'))))
assert len(records)==6
assert records[0]['source']=='M-3' and records[1]['code']=='?'
assert records[2]['code']=='A/R' and records[3]['source']=='M-4'
svg=ET.parse(OUT/'handoffs.svg').getroot()
svg_text=' '.join(svg.itertext())
for token in ['H-7','H-8','H-9','A/R','unknown','proposed','confirmed','Prepare the evidence package']:
    assert token in svg_text, token
html=(OUT/'handoffs.html').read_text(encoding='utf-8')
assert 'Rows with findings' in html and 'data-findings="false"' in html
assert 'data-detail=' in html and 'M-3' in html
assert 'downloads contain the complete matrix' in html
assert 'href="http' not in html and 'src="http' not in html
checks=[]
def reject(name, change):
    candidate=copy.deepcopy(data); change(candidate)
    p=OUT/(name+'.json');p.write_text(json.dumps(candidate),encoding='utf-8')
    proc=subprocess.run([sys.executable,str(HELPER),str(p),'--output',str(OUT/(name+'-output'))],capture_output=True,text=True)
    assert proc.returncode==2,(name,proc.returncode,proc.stderr)
    assert not list(OUT.glob(name+'-output.*'))
    checks.append({'case':name,'exit_code':proc.returncode,'stderr':proc.stderr.strip()})
reject('duplicate-role',lambda d:d['roles'].append(d['roles'][0]))
reject('missing-cell',lambda d:d['rows'][0]['cells'].pop('OPS'))
reject('invalid-code',lambda d:d['rows'][0]['cells']['PM'].update(code='APPROVED'))
reject('missing-evidence',lambda d:d['rows'][0]['cells']['PM'].update(source=''))
reject('invalid-state',lambda d:d['rows'][0]['cells']['PM'].update(state='accepted'))
adverse=copy.deepcopy(data)
adverse['roles'][0]['label']='=DANGEROUS() <script>alert(1)</script>'
adverse['rows'][0]['cells']['PM']['note']='Long duty <img src=x onerror=alert(1)> & evidence "quoted"'
adverse['rows'][1]['cells']['OPS']=cell('—','confirmed','Explicit no assignment in adverse fixture only','M-4')
adverse['rows'][2]['cells']['PM']['state']='disputed'
raci.validate(adverse)
csv_adverse=raci.render_csv(adverse)
assert list(csv.DictReader(io.StringIO(csv_adverse)))[0]['role'].startswith("'=DANGEROUS")
adverse_svg=raci.render_svg(adverse)
ET.fromstring(adverse_svg)
adverse_html=raci.render_html(adverse,adverse_svg,csv_adverse)
assert '<script>alert(1)</script>' not in adverse_html
assert '<img src=x onerror=' not in adverse_html
assert '—' in adverse_html and '?' in adverse_html and 'disputed' in adverse_html
(OUT/'adverse.html').write_text(adverse_html,encoding='utf-8')
(OUT/'adverse.svg').write_text(adverse_svg,encoding='utf-8')
summary={'renderer':str(HELPER),'primary_output':result,'svg_dimensions':{k:svg.attrib[k] for k in ['width','height']},'adverse_rejections':checks,'passes':['Exact JSON round-trip','Six CSV assignment records and source IDs','SVG XML and displayed codes/states/work boundary','Self-contained exports and findings controls present','Formula text prefixed in CSV','HTML/XML injection escaped','Explicit no assignment, unknown and disputed coexist in adverse fixture'],'limitations':['No browser interaction or rendered viewport inspection yet','SVG has generic reference to companion evidence but no per-cell evidence references or detailed audit register']}
(OUT/'test-results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
