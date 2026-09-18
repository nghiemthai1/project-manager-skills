"""Behavior and source-fidelity checks for portable visual renderers."""
import copy
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


def load(slug, filename):
    path = ROOT/'skills'/slug/'scripts'/filename
    spec = importlib.util.spec_from_file_location(filename[:-3], path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


gantt = load('gantt-chart', 'render_gantt.py')
raci = load('raci-matrix', 'render_raci.py')
dependency = load('dependency-map', 'render_dependency_map.py')
capacity = load('resource-capacity-plan', 'render_capacity.py')
budget = load('project-budget', 'render_budget.py')
milestone = load('milestone-schedule', 'render_milestone.py')
readiness = load('release-readiness', 'render_readiness.py')


class VisualTests(unittest.TestCase):
    def test_generated_examples_match_source(self):
        for slug, module in [('gantt-chart', gantt), ('raci-matrix', raci), ('dependency-map', dependency),
                             ('resource-capacity-plan', capacity), ('project-budget', budget),
                             ('milestone-schedule', milestone), ('release-readiness', readiness)]:
            for scene in ('software', 'migration'):
                stem = ROOT/'skills'/slug/'examples'/'assets'/scene
                data = module.validate(json.loads(Path(str(stem)+'-source.json').read_text(encoding='utf-8')))
                self.assertEqual(json.loads(Path(str(stem)+'.json').read_text(encoding='utf-8')), data)
                svg = module.render_svg(data)
                csv = module.render_csv(data)
                for ext, body in [('svg',svg), ('html',module.render_html(data,svg,csv)), ('csv',csv)]:
                    # Git may translate text endings. Compare normalized payloads.
                    actual = Path(str(stem)+'.'+ext).read_bytes().replace(b'\r\n',b'\n')
                    self.assertEqual(actual, body.encode().replace(b'\r\n',b'\n'))
                ET.fromstring(svg)

    def test_gantt_unknown_dates_and_literals_preserved(self):
        data=gantt.demo();data['tasks'][0]['id']='BC-R7';data['links'][0]['from']='BC-R7'
        data['tasks'][0]['actual']={'start':'2028-02-29','finish':None}
        original=copy.deepcopy(data)
        gantt.validate(data); ds=gantt.diagnostics(data);svg=gantt.render_svg(data)
        self.assertEqual(original,data)
        self.assertTrue(any('partial actual' in x for x in ds))
        self.assertIn('BC-R7',svg)
        self.assertIn('unknown',gantt.span_text(data['tasks'][1],'forecast'))

    def test_gantt_declared_analysis_and_presentation_are_validated(self):
        data=gantt.demo();data['presentation']={'eyebrow':'Demo','headline':'Evidence first','lede':'One dated task.',
            'default_task_id':'T-1','metrics':[{'label':'Finish','value':'7 Oct','note':'Supplied boundary'}],
            'insight_heading':'Review the source.','insight_points':['No dates were recalculated.'],'decision':'Validate before commitment.',
            'phases':[{'id':'prepare','index':'01','name':'Preparation'}]}
        data['tasks'][0].update(phase='prepare',tone='design')
        data['analysis']={'method':'Supplied teaching result; no scheduling performed.',
            'forecast':{'critical_task_ids':['T-1'],'tasks':{'T-1':{'duration_working_days':2,'total_float_working_days':0}}}}
        self.assertIs(gantt.validate(data),data)
        self.assertIn('Evidence first',gantt.render_svg(data))
        broken=copy.deepcopy(data);broken['analysis']['forecast']['critical_task_ids']=['MISSING']
        with self.assertRaises(ValueError):gantt.validate(broken)
        broken=copy.deepcopy(data);broken['tasks'][0]['phase']='missing'
        with self.assertRaises(ValueError):gantt.validate(broken)
        broken=copy.deepcopy(data);broken['tasks'][0]['tone']='rainbow'
        with self.assertRaises(ValueError):gantt.validate(broken)

    def test_typed_link_timing_does_not_reschedule(self):
        data=gantt.demo();data['tasks'][1]['forecast']={'start':'2026-10-06','finish':'2026-10-06'}
        snapshot=copy.deepcopy(data)
        self.assertTrue(any('violates' in d for d in gantt.diagnostics(data)))
        data['links'][0]['type']='SS'
        self.assertFalse(any('violates' in d for d in gantt.diagnostics(data)))
        self.assertEqual(snapshot['tasks'],data['tasks'])
        data['links'][0].update(lag=2,lag_unit='working_days')
        self.assertTrue(any('scheduling engine' in d for d in gantt.diagnostics(data)))

    def test_missing_endpoints_cycles_and_empty(self):
        data=gantt.demo();data['links'][0]['from']='EXT-9'
        self.assertTrue(any('outside snapshot' in d for d in gantt.diagnostics(data)))
        data['links'][0].update({'from':'T-1','to':'T-1'})
        self.assertTrue(any('cycle' in d for d in gantt.diagnostics(data)))
        data['tasks']=[];data['links']=[]
        self.assertIn('No dated intervals',gantt.render_svg(gantt.validate(data)))

    def test_invalid_calendar_dates_and_progress(self):
        for value in (None, [], 'Monday', {'label':'x','working_weekdays':[True]}):
            data=gantt.demo();data['calendar']=value
            with self.assertRaises(ValueError):gantt.validate(data)
        for value in ('2027-02-29','2026-10-05T00:00:00Z','10/05/2026'):
            with self.assertRaises(ValueError):gantt.parse_date(value)
        data=gantt.demo();data['tasks'][0]['progress']={'percent':30}
        with self.assertRaises(ValueError):gantt.validate(data)

    def test_long_owner_stays_in_own_svg_row(self):
        data=gantt.demo();data['tasks'][0]['owner']='Long owner division '*70
        svg=ET.fromstring(gantt.render_svg(data));ns={'s':'http://www.w3.org/2000/svg'}
        groups=svg.findall('.//s:g[@data-task]',ns)
        first_text=[float(t.attrib['y']) for t in groups[0].findall('s:text',ns)]
        second_text=[float(t.attrib['y']) for t in groups[1].findall('s:text',ns)]
        self.assertLess(max(first_text),min(second_text))

    def test_gantt_product_view_and_local_editor_are_present(self):
        data=gantt.demo();html=gantt.render_html(data,gantt.render_svg(data),gantt.render_csv(data))
        for token in ('id="editToggle"','id="taskEditor"','id="undoEdit"',
                      'id="discardDraft"','id="draftJson"','id="draftCsv"',
                      'id="draftTaskTable"','id="draftDiagnostics"',
                      'id="editForecastStart"','id="editForecastFinish"',
                      'Milestone dates must coincide',
                      'This parent change would create a hierarchy cycle.',
                      'function draftSnapshot()','changed_tasks',
                      'Source exports and downstream dates remain unchanged.'):
            self.assertIn(token,html)
        self.assertEqual(html.count('download="gantt.'),3)

    def test_raci_audit_separates_confirmation_and_letter(self):
        data=raci.demo();row=data['rows'][0]
        self.assertTrue(any('Unresolved cells' in f['findings'] for f in raci.audit(data)))
        row['cells']['PM'].update(code='A/R',state='confirmed',source='M-4')
        row['cells']['OPS'].update(code='I',state='confirmed',source='M-4')
        self.assertEqual(raci.audit(data),[])
        row['cells']['OPS']['code']='A'
        self.assertTrue(any('2 A' in flag for f in raci.audit(data) for flag in f['findings']))

    def test_raci_confirmed_needs_source_and_cells_are_explicit(self):
        data=raci.demo();data['rows'][0]['cells']['PM']['state']='confirmed'
        with self.assertRaises(ValueError):raci.validate(data)

    def test_raci_vertical_audit_and_declared_thresholds(self):
        data=raci.demo()
        profile={item['id']:item for item in raci.role_audit(data)}
        self.assertEqual(profile['PM']['counts']['R'],1)
        self.assertEqual(profile['PM']['exact_counts']['R'],1)
        self.assertEqual(profile['OPS']['counts']['?'],1)
        self.assertIn('unresolved assignment',profile['OPS']['signals'][0])
        data['analysis']['accountability_concentration_threshold']=True
        with self.assertRaises(ValueError):raci.validate(data)
        data=raci.demo();data['rows'][0]['group']='missing'
        with self.assertRaises(ValueError):raci.validate(data)

    def test_raci_product_views_and_export_scope_are_present(self):
        data=raci.demo();html=raci.render_html(data)
        for token in ('id="matrixTab"','id="auditTab"','id="rolesTab"','id="authority"',
                      'id="visibleCsv"','id="editToggle"','id="cellEditor"','id="undoEdit"',
                      'id="discardDraft"','id="draftJson"','id="draftCsv"',
                      'Confirmed assignments require an evidence or source reference.',
                      'Role profiles','other columns are hidden'):
            self.assertIn(token,html)
        self.assertEqual(html.count('download="raci-matrix.'),3)

    def test_dependency_margin_direction_and_acceptance(self):
        data=dependency.demo();original=copy.deepcopy(data)
        dep=data['dependencies'][1]
        self.assertEqual(dependency.local_margin(dep),-2)
        self.assertEqual(dependency.category(dep),'gap')
        self.assertIn(',-2,',dependency.render_csv(data))
        dep['acceptance_state']='accepted';dep['status']='accepted'
        self.assertEqual(dependency.category(dep),'closed')
        self.assertEqual(original['dependencies'][1]['forecast'],'2026-10-22')

    def test_dependency_rejects_missing_endpoints_and_unsupported_cpm(self):
        data=dependency.demo();data['dependencies'][0]['provider']='MISSING'
        with self.assertRaises(ValueError):dependency.validate(data)
        data=dependency.demo();data['analysis']['critical_path']={'dependency_ids':['MISSING'],'method':'Imported CPM'}
        with self.assertRaises(ValueError):dependency.validate(data)
        data=dependency.demo();data['dependencies'][0]['committed']='2026-10-18'
        with self.assertRaises(ValueError):dependency.validate(data)
        data=raci.demo();del data['rows'][0]['cells']['OPS']
        with self.assertRaises(ValueError):raci.validate(data)

    def test_dependency_product_views_and_local_editor_are_present(self):
        data=dependency.demo();html=dependency.render_html(data)
        for token in ('id="graphTab"','id="matrixTab"','id="dependencyEditor"',
                      'id="editToggle"','id="undoEdit"','id="discardDraft"',
                      'id="draftJson"','id="draftCsv"','id="editProvider"',
                      'id="editReceiver"','id="editForecast"',
                      'Provider and receiver must be different nodes.',
                      'A committed date requires commitment evidence.',
                      'function draftSnapshot()','changed_dependencies',
                      'directed cycle retained for review'):
            self.assertIn(token,html)
        self.assertEqual(html.count('download="dependency-network.'),3)

    def test_capacity_preserves_individual_overload_and_unknown_demand(self):
        data=capacity.demo();original=copy.deepcopy(data)
        totals=capacity.summary(data)
        self.assertEqual(totals['available_hours'],88)
        self.assertEqual(totals['known_demand_hours'],84)
        self.assertEqual(totals['person_overload_hours'],8)
        self.assertEqual(capacity.person_result(data['people'][0])['overload_hours'],8)
        data['people'][1]['allocations'].append({'id':'A-4','work':'Unbounded support','skill':'security assurance',
            'window':'19–30 Oct','hours':None,'status':'unknown','source':'Demand exists; hours not bounded','note':''})
        self.assertEqual(capacity.person_result(data['people'][1])['unknown_allocations'],1)
        self.assertEqual(capacity.person_result(data['people'][1])['known_demand_hours'],20)
        self.assertEqual(original['people'][0]['allocations'][0]['hours'],48)

    def test_capacity_validation_and_local_editor_are_present(self):
        data=capacity.demo();data['people'][0]['leave_hours']=81
        with self.assertRaises(ValueError): capacity.validate(data)
        data=capacity.demo();data['people'][0]['allocations'][0].update(status='unknown',hours=4)
        with self.assertRaises(ValueError): capacity.validate(data)
        data=capacity.demo();html=capacity.render_html(data)
        for token in ('id="chartTab"','id="tableTab"','id="constraintsTab"','id="optionsTab"',
                      'id="personEditor"','id="editToggle"','id="allocationEditor"',
                      'id="addAllocation"','id="undoEdit"','id="discardDraft"',
                      'id="draftJson"','id="draftCsv"','id="visibleCsv"',
                      'Unknown allocations must leave hours blank.',
                      'function draftSnapshot()','changed_people',
                      'Arithmetic recalculated; source exports remain unchanged.'):
            self.assertIn(token,html)
        self.assertEqual(html.count('download="capacity-plan.'),3)

    def test_budget_calculations_keep_forecast_and_authority_distinct(self):
        data=budget.demo();calc=budget.calculations(data)
        self.assertAlmostEqual(calc['cpi'],5/6)
        self.assertEqual(calc['forecasts']['cost_efficiency'],120)
        self.assertEqual(calc['ledger_difference'],0)
        data['categories'][0]['other_etc']=None
        self.assertIsNone(budget.calculations(data)['forecasts']['bottom_up'])
        self.assertEqual(budget.calculations(data)['unknown_remaining_fields'],1)

    def test_budget_validation_and_local_editor_are_present(self):
        data=budget.demo();data['baseline']['total_envelope']=99
        with self.assertRaises(ValueError):budget.validate(data)
        data=budget.demo();data['categories'][0].update(status='unknown',committed_unspent=0,other_etc=1)
        with self.assertRaises(ValueError):budget.validate(data)
        html=budget.render_html(budget.demo())
        for token in ('id="forecastTab"','id="ledgerTab"','id="performanceTab"','id="fundingTab"',
                      'id="budgetEditor"','id="editToggle"','id="categoryEditor"',
                      'id="undoEdit"','id="discardDraft"','id="draftJson"','id="draftCsv"',
                      'id="visibleCsv"','Total funding envelope cannot be below BAC.',
                      'function draftSnapshot()','Local financial draft saved. Arithmetic recalculated'):
            self.assertIn(token,html)
        self.assertEqual(html.count('download="project-budget.'),3)

    def test_milestone_network_and_editor(self):
        data=milestone.demo();net=milestone.compute_network(data)
        self.assertEqual(net['finish'],7)
        self.assertEqual(net['tasks']['C']['float'],1)
        data['tasks'][1]['predecessors']=['E']
        with self.assertRaises(ValueError):milestone.validate(data)
        html=milestone.render_html(milestone.demo())
        for token in ('id="networkTab"','id="timingTab"','id="milestonesTab"','id="scenariosTab"',
                      'id="taskEditor"','id="editPredecessors"','id="undoEdit"','id="discardDraft"',
                      'id="draftJson"','id="draftCsv"','id="visibleCsv"',
                      'The edited network contains a directed cycle.','function draftSnapshot()','changed_tasks'):
            self.assertIn(token,html)
        self.assertEqual(html.count('download="milestone-schedule.'),3)

    def test_release_readiness_keeps_gates_and_authority_independent(self):
        data=readiness.demo();summary=readiness.readiness(data)
        self.assertEqual(summary['recommendation'],'hold')
        self.assertEqual(summary['blockers'],['G-REC'])
        data['gates'][0]['status']='accepted_exception'
        data['gates'][0]['evidence_ref']='EX-1';data['gates'][0]['observed_on']='2026-10-28';data['gates'][0]['exception_authority']='Sponsor'
        with self.assertRaises(ValueError):readiness.validate(data)
        html=readiness.render_html(readiness.demo())
        for token in ('id="gatesTab"','id="decisionTab"','id="coverageTab"','id="chronologyTab"',
                      'id="gateEditor"','id="editClassification"','id="undoEdit"','id="discardDraft"',
                      'id="draftJson"','id="draftCsv"','id="visibleCsv"',
                      'Accepted exception requires exceptionable classification.','function draftSnapshot()','changed_gates'):
            self.assertIn(token,html)
        self.assertEqual(html.count('download="release-readiness.'),3)

    def test_untrusted_text_is_escaped_and_csv_guarded(self):
        for module in (gantt,raci,dependency,capacity,budget,milestone,readiness):
            data=module.demo();data['title']='</script><script>alert(1)</script>'
            if module is gantt: item=data['tasks'][0];item['label']='=WEBSERVICE("example")'
            elif module is raci: item=data['rows'][0];item['label']='=WEBSERVICE("example")'
            elif module is dependency: data['dependencies'][0]['handoff']='=WEBSERVICE("example")'
            elif module is capacity: data['people'][0]['name']='=WEBSERVICE("example")'
            elif module is budget: data['categories'][0]['label']='=WEBSERVICE("example")'
            elif module is milestone: data['tasks'][0]['label']='=WEBSERVICE("example")'
            else: data['gates'][0]['label']='=WEBSERVICE("example")'
            svg=module.render_svg(data);csv=module.render_csv(data);html=module.render_html(data,svg,csv)
            self.assertNotIn(data['title'],html)
            self.assertIn("'=WEBSERVICE",csv)
            self.assertNotRegex(html,r'<(?:script|link)\b[^>]*(?:src|href)="https?://')

    def test_isolated_cli_outputs_and_windows_csv_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            for module in (gantt,raci,dependency,capacity,budget,milestone,readiness):
                script=Path(temp)/Path(module.__file__).name
                script.write_bytes(Path(module.__file__).read_bytes())
                stem=Path(temp)/script.stem
                run=subprocess.run([sys.executable,'-I',str(script),'--demo','--output',str(stem)],cwd=temp,capture_output=True,text=True)
                self.assertEqual(run.returncode,0,run.stderr)
                for suffix in ('.svg','.html','.json','.csv'):self.assertTrue(Path(str(stem)+suffix).is_file())
                self.assertNotIn(b'\r\r\n',Path(str(stem)+'.csv').read_bytes())
                self.assertEqual(json.loads(Path(str(stem)+'.json').read_text(encoding='utf-8')),module.demo())


if __name__ == '__main__': unittest.main()
