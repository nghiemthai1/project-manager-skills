import base64
import copy
import csv
import importlib.util
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[1]
HELPER=ROOT/'skills/gantt-chart/scripts/render_gantt.py'
spec=importlib.util.spec_from_file_location('gantt',HELPER)
gantt=importlib.util.module_from_spec(spec);spec.loader.exec_module(gantt)
def span(a,b):return {'start':a,'finish':b}
data={'title':'Fictional handoff schedule','as_of':'2028-02-28','source':'Fictional user request','scope':'T-01, M-02 and R-03; external EXT-9 is outside snapshot','version':'draft-1','comparison_label':'Supplied comparison; approval unknown','date_convention':'[start, finish)',
 'calendar':{'label':'Monday-Friday; 2028-02-29 holiday','working_weekdays':[0,1,2,3,4],'holidays':['2028-02-29']},
 'tasks':[
  {'id':'T-01','label':'Work','kind':'task','owner':'unknown','source':'S-1','forecast':span('2028-02-28','2028-03-02'),'comparison':span('2028-02-28','2028-03-01'),'actual':span('2028-02-28',None),'progress':None},
  {'id':'M-02','label':'Checkpoint','kind':'milestone','owner':'unknown','source':'S-2','forecast':None,'comparison':None,'actual':None,'progress':None},
  {'id':'R-03','label':'Review','kind':'task','owner':'unknown','source':'Fictional user request; source ID not supplied','forecast':span('2028-03-01','2028-03-02'),'comparison':None,'actual':None,'progress':None}],
 'links':[
  {'id':'DEP-X','from':'T-01','to':'R-03','type':'FS','lag':0,'lag_unit':'unknown; zero lag supplied','source':'Fictional user request','inferred':False},
  {'id':'DEP-Z','from':'EXT-9','to':'M-02','type':'SS','lag':2,'lag_unit':'working_days','source':'Fictional user request','inferred':False}],
 'notes':['Fictional data. No acceptance evidence or percent-progress evidence supplied.',
  'As-of date and all written dates retained without repair. Comparison approval is unknown.',
  'Mapping assumption: the stated actual start belongs to T-01, the work item; no actual finish was supplied.',
  'Display assumption: [start, finish) follows this renderer contract; source did not specify endpoint inclusion. Dates are unchanged.',
  'Working days and holiday are supplied by the requester; owners and relationship lag calendars beyond this snapshot are unknown.']}

def render(name,fixture):
 p=OUT/(name+'-source.json');p.write_text(json.dumps(fixture,ensure_ascii=False,indent=2),encoding='utf-8')
 proc=subprocess.run([sys.executable,str(HELPER),str(p),'--output',str(OUT/name)],capture_output=True,text=True,encoding='utf-8')
 return proc

proc=render('schedule',data);assert proc.returncode==0,proc.stderr
summary=json.loads(proc.stdout)
assert json.loads((OUT/'schedule.json').read_text(encoding='utf-8'))==data
assert any(x.startswith('DEP-X: forecast violates') for x in summary['diagnostics'])
assert any(x.startswith('DEP-Z: endpoint outside') for x in summary['diagnostics'])
assert any(x.startswith('T-01: partial actual') for x in summary['diagnostics'])
assert any(x.startswith('M-02: forecast incomplete') for x in summary['diagnostics'])
svg=ET.parse(OUT/'schedule.svg').getroot();ns={'s':'http://www.w3.org/2000/svg'}
groups={x.attrib['data-task']:x for x in svg.findall('.//s:g[@data-task]',ns)}
assert not groups['M-02'].findall('.//s:rect',ns)
assert not groups['M-02'].findall('.//s:path[@class]',ns)
forecast=groups['T-01'].find('.//s:rect[@class="forecast"]',ns)
comparison=groups['T-01'].find('.//s:rect[@class="comparison"]',ns)
assert float(forecast.attrib['x'])==410 and float(forecast.attrib['width'])==970
assert float(comparison.attrib['width'])==646.7
assert not groups['T-01'].findall('.//*[@class="actual"]',ns)
holiday=[r for r in svg.findall('.//s:rect',ns) if r.attrib.get('fill')=='#e8edf4']
assert len(holiday)==1 and float(holiday[0].attrib['x'])==733.3
rows=list(csv.DictReader(io.StringIO((OUT/'schedule.csv').read_text(encoding='utf-8'))))
assert len(rows)==9
assert rows[2]['start']=='2028-02-28' and rows[2]['finish']==''
assert b'\r\r\n' not in (OUT/'schedule.csv').read_bytes()
html=(OUT/'schedule.html').read_text(encoding='utf-8')
assert 'SS, +2 working_days' in html and 'Progress: unknown' in html
for ext,b64 in re.findall(r'download="gantt\.(\w+)" href="data:[^;]+;base64,([^"]+)"',html):
 assert base64.b64decode(b64).rstrip()==(OUT/('schedule.'+ext)).read_bytes().rstrip()

fixtures={}
cycle=copy.deepcopy(data)
cycle['links'].append({'id':'DEP-CYCLE','from':'R-03','to':'T-01','type':'FS','lag':0,'lag_unit':'calendar_days','source':'Fictional adverse fixture','inferred':False})
fixtures['cycle']=cycle
empty=copy.deepcopy(data);empty['tasks']=[];empty['links']=[];fixtures['empty']=empty
partial=copy.deepcopy(data);partial['tasks'][0]['forecast']=span(None,'2028-03-02');partial['tasks'][0]['comparison']={};partial['tasks'][2]['forecast']=span('2028-03-01',None);fixtures['partial']=partial
long=copy.deepcopy(data);long['tasks'][0]['label']='Long task label '+('preserve exact wording < > & " '+'' )*20;long['tasks'][0]['owner']='Long source owner '+('Functional responsibility group '*25);fixtures['long']=long
fixture_results={}
for name,fixture in fixtures.items():
 r=render(name,fixture);assert r.returncode==0,(name,r.stderr)
 fixture_results[name]=json.loads(r.stdout)
 assert json.loads((OUT/(name+'.json')).read_text(encoding='utf-8'))==fixture
 ET.parse(OUT/(name+'.svg'))
assert any(x.startswith('Dependency cycle:') for x in fixture_results['cycle']['diagnostics'])
emptytext=' '.join(ET.parse(OUT/'empty.svg').getroot().itertext());assert 'No dated intervals' in emptytext and '2000-01-01' not in emptytext

# Probe malformed calendar type and accepted zero/partial task intervals.
bad=copy.deepcopy(data);bad['calendar']=None
r=render('invalid-calendar-type',bad)
calendar_type={'exit_code':r.returncode,'stderr':r.stderr}
zero=copy.deepcopy(data);zero['tasks'][0]['forecast']=span('2028-02-28','2028-02-28')
r=render('zero-task',zero);assert r.returncode==0
assert any('zero-length forecast task' in x for x in json.loads(r.stdout)['diagnostics'])

# The owner's multiple wrapped lines must fit before the next task.
longsvg=ET.parse(OUT/'long.svg').getroot();gg=longsvg.findall('.//s:g[@data-task]',ns)
first_owner_lines=[float(t.attrib['y']) for t in gg[0].findall('s:text',ns) if float(t.attrib.get('x',0))==25 and t.attrib.get('font-size')=='11']
second_label_y=min(float(t.attrib['y']) for t in gg[1].findall('s:text',ns) if float(t.attrib.get('x',0))==25)
owner_overlap={'last_owner_baseline':max(first_owner_lines),'next_task_first_label_baseline':second_label_y,'overlaps':max(first_owner_lines)>=second_label_y}
assert owner_overlap['overlaps']

results={'main':summary,'svg_dimensions':{k:svg.attrib[k] for k in ['width','height']},'fixtures':fixture_results,'invalid_calendar_type':calendar_type,'long_owner_overlap':owner_overlap,'tested':['Source JSON exact round-trip for primary and all valid adverse fixtures','Typed links and external endpoint retained','FS-zero contradiction diagnosed without repair','Unscheduled milestone no invented diamond','Partial actual no completed bar','Leap-day holiday shaded at correct date','Forecast and comparison pixel endpoints preserve source dates','Empty source no fake date axis','Cycles diagnosed','SVG XML valid; injected markup escaped','CSV 9 task/layer records, correct line endings','All embedded exports equal external files'],'not_tested':['Browser controls, keyboard, viewport layout; parent handles browser QA']}
(OUT/'test-results.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(results,ensure_ascii=False,indent=2))
