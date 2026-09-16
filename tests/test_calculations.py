"""Independent numeric examples, invariants, and CLI boundary tests."""
import copy
import importlib.util
import itertools
import json
import math
from pathlib import Path
import random
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
PATHS = {
    'estimate': ROOT/'skills/estimation-advisor/scripts/estimate.py',
    'capacity': ROOT/'skills/resource-capacity-plan/scripts/capacity.py',
    'schedule': ROOT/'skills/milestone-schedule/scripts/schedule.py',
    'evm': ROOT/'skills/project-budget/scripts/earned_value.py',
}

def load(name):
    spec = importlib.util.spec_from_file_location(name, PATHS[name])
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

MODULES = {name: load(name) for name in PATHS}

class EstimateTests(unittest.TestCase):
    def test_asymmetric_case(self):
        got = MODULES['estimate'].compute({'unit':'person_days','optimistic':2,'most_likely':4,'pessimistic':12})
        self.assertAlmostEqual(got['triangular_mean'], 6)
        self.assertAlmostEqual(got['pert_mean'], 5)
        self.assertAlmostEqual(got['pert_standard_deviation_heuristic'], 5/3)

    def test_equal_and_zero_estimates(self):
        for value in (0, 3.5):
            got=MODULES['estimate'].compute({'unit':'hours','optimistic':value,'most_likely':value,'pessimistic':value})
            self.assertAlmostEqual(got['pert_mean'],value)
            self.assertEqual(got['pert_standard_deviation_heuristic'],0)

    def test_ordering_is_required(self):
        for o,m,p in ((5,2,8),(1,9,7)):
            with self.assertRaises(ValueError):
                MODULES['estimate'].compute({'unit':'hours','optimistic':o,'most_likely':m,'pessimistic':p})

    def test_means_within_bounds(self):
        rng=random.Random(13)
        for _ in range(100):
            o,m,p=sorted(rng.uniform(0,1000) for _ in range(3))
            got=MODULES['estimate'].compute({'unit':'hours','optimistic':o,'most_likely':m,'pessimistic':p})
            self.assertLessEqual(o,got['pert_mean'])
            self.assertLessEqual(got['pert_mean'],p)
            self.assertLessEqual(o,got['triangular_mean'])
            self.assertLessEqual(got['triangular_mean'],p)

class CapacityTests(unittest.TestCase):
    def test_overload_not_hidden_by_other_person(self):
        got=MODULES['capacity'].compute(copy.deepcopy(MODULES['capacity'].DEMO))
        self.assertEqual(got['total_available_hours'],88)
        self.assertEqual(got['total_demand_hours'],84)
        self.assertEqual(got['sum_person_overload_hours'],8)
        self.assertEqual(got['people'][0]['remaining_hours'],-8)
        self.assertAlmostEqual(got['people'][0]['load_percent'],100*64/56)

    def test_zero_capacity(self):
        for demand in (0,2):
            got=MODULES['capacity'].compute({'period':'week 1','people':[{'id':'a','gross_hours':0,'leave_hours':0,'overhead_hours':0,'allocations':[{'project':'x','hours':demand}]}]})
            self.assertIsNone(got['people'][0]['load_percent'])
            self.assertEqual(got['sum_person_overload_hours'],demand)

    def test_deductions_cannot_exceed_gross(self):
        data=copy.deepcopy(MODULES['capacity'].DEMO)
        data['people'][0]['leave_hours']=80
        with self.assertRaises(ValueError): MODULES['capacity'].compute(data)

    def test_duplicate_people_and_allocations(self):
        data=copy.deepcopy(MODULES['capacity'].DEMO)
        data['people'].append(copy.deepcopy(data['people'][0]))
        with self.assertRaises(ValueError): MODULES['capacity'].compute(data)
        data=copy.deepcopy(MODULES['capacity'].DEMO)
        data['people'][0]['allocations'].append({'project':'Relay','hours':1})
        with self.assertRaises(ValueError): MODULES['capacity'].compute(data)

    def test_explicit_empty_allocations(self):
        data=copy.deepcopy(MODULES['capacity'].DEMO)
        data['people'][0]['allocations']=[]
        self.assertEqual(MODULES['capacity'].compute(data)['people'][0]['demand_hours'],0)

class ScheduleTests(unittest.TestCase):
    def test_branch_and_merge(self):
        got=MODULES['schedule'].compute(MODULES['schedule'].DEMO)
        self.assertEqual(got['project_duration'],7)
        rows={r['id']:r for r in got['tasks']}
        self.assertEqual(rows['C']['total_float'],1)
        self.assertEqual(rows['C']['late_start'],3)
        self.assertEqual(got['critical_activities'],['A','B','D'])
        self.assertEqual(got['critical_edges'],[{'from':'A','to':'B'},{'from':'B','to':'D'}])

    def test_tied_paths_and_milestone(self):
        data=copy.deepcopy(MODULES['schedule'].DEMO)
        data['tasks'][2]['duration']=4
        data['tasks'].append({'id':'END','duration':0,'predecessors':['D']})
        got=MODULES['schedule'].compute(data)
        self.assertEqual(len(got['critical_activities']),5)
        self.assertEqual(got['project_duration'],7)

    def test_disconnected_work_shares_finish(self):
        got=MODULES['schedule'].compute({'unit':'hours','tasks':[{'id':'a','duration':3,'predecessors':[]},{'id':'b','duration':8,'predecessors':[]}]})
        rows={r['id']:r for r in got['tasks']}
        self.assertEqual(rows['a']['total_float'],5)
        self.assertEqual(got['critical_activities'],['b'])

    def test_cycle_and_missing_dependency(self):
        for tasks in ([{'id':'a','duration':1,'predecessors':['a']}],
                      [{'id':'a','duration':1,'predecessors':['b']},{'id':'b','duration':1,'predecessors':['a']}],
                      [{'id':'a','duration':1,'predecessors':['missing']}]):
            with self.assertRaises(ValueError): MODULES['schedule'].compute({'unit':'days','tasks':tasks})

    def test_reordered_input_does_not_change_output(self):
        data=copy.deepcopy(MODULES['schedule'].DEMO)
        expected=MODULES['schedule'].compute(data)
        data['tasks'].reverse()
        self.assertEqual(expected,MODULES['schedule'].compute(data))

    def test_small_dags_against_enumerated_paths(self):
        # Independent oracle enumerates every source-to-sink path, not a forward/backward pass.
        rng=random.Random(42)
        for _ in range(80):
            count=6
            tasks=[{'id':str(i),'duration':rng.randint(0,8),'predecessors':[str(j) for j in range(i) if rng.random()<0.35]} for i in range(count)]
            successors={t['id']:[u['id'] for u in tasks if t['id'] in u['predecessors']] for t in tasks}
            durations={t['id']:t['duration'] for t in tasks}
            paths=[]
            def walk(path):
                children=successors[path[-1]]
                if not children: paths.append(path)
                for child in children: walk(path+[child])
            for t in tasks:
                if not t['predecessors']: walk([t['id']])
            totals=[(p,sum(durations[x] for x in p)) for p in paths]
            longest=max(v for _,v in totals)
            got=MODULES['schedule'].compute({'unit':'days','tasks':tasks})
            self.assertEqual(got['project_duration'],longest)
            for row in got['tasks']:
                longest_through=max(v for p,v in totals if row['id'] in p)
                self.assertEqual(row['total_float'],longest-longest_through)

class EarnedValueTests(unittest.TestCase):
    def test_relay_case(self):
        got=MODULES['evm'].compute(MODULES['evm'].DEMO)
        for key,value in {'cv':-8000,'sv':-10000,'cpi':5/6,'spi':0.8,'eac_cpi':120000,'eac_cpi_spi':138000,'eac_remaining_at_budget':108000,'vac_cpi':-20000}.items():
            self.assertAlmostEqual(got[key],value)

    def test_migration_case(self):
        got=MODULES['evm'].compute({'currency':'USD','as_of':'2026-10-23','pv':80000,'ev':60000,'ac':75000,'bac':240000})
        self.assertAlmostEqual(got['eac_cpi'],300000)
        self.assertEqual(got['cv'],-15000)
        self.assertEqual(got['sv'],-20000)

    def test_zero_denominators(self):
        data={'currency':'USD','as_of':'2026-01-01','pv':0,'ev':0,'ac':0,'bac':100}
        got=MODULES['evm'].compute(data)
        for field in ('cpi','spi','eac_cpi','eac_cpi_spi','vac_cpi'): self.assertIsNone(got[field])
        self.assertEqual(got['eac_remaining_at_budget'],100)
        data.update(ev=10)
        self.assertIsNone(MODULES['evm'].compute(data)['cpi'])

    def test_completed_late_project_spi_does_not_indicate_timeliness(self):
        got=MODULES['evm'].compute({'currency':'USD','as_of':'2026-12-31','pv':100,'ev':100,'ac':150,'bac':100})
        self.assertEqual(got['spi'],1)
        self.assertEqual(got['eac_cpi'],150)

    def test_iso_week_date_is_not_calendar_date_contract(self):
        data=copy.deepcopy(MODULES['evm'].DEMO)
        data['as_of']='2026-W01-1'
        with self.assertRaises(ValueError):
            MODULES['evm'].compute(data)

    def test_numeric_underflow_is_an_error(self):
        for pv,ev,ac,bac in ((1e300,1e-300,1e300,1e300),(1,1e-200,1,1)):
            with self.assertRaises(ValueError):
                MODULES['evm'].compute({'currency':'USD','as_of':'2026-10-16','pv':pv,'ev':ev,'ac':ac,'bac':bac})

    def test_invalid_baseline_or_date(self):
        for patch in ({'bac':0},{'ev':100001},{'pv':100001},{'as_of':'2026-02-30'},{'as_of':'20261016'}):
            data=dict(MODULES['evm'].DEMO,**patch)
            with self.assertRaises(ValueError): MODULES['evm'].compute(data)

class BoundaryTests(unittest.TestCase):
    def test_number_rejects_false_text_negative_nan_infinity(self):
        for module in MODULES.values():
            for bad in (True,False,'1',-1,None,float('nan'),float('inf'),10**10000):
                with self.subTest(module=module.__name__,value=type(bad).__name__):
                    with self.assertRaises(ValueError): module.number(bad,'test')

    def test_missing_and_unknown_fields(self):
        for module in MODULES.values():
            with self.assertRaises(ValueError): module.compute({})
            with self.assertRaises(ValueError): module.compute(dict(module.DEMO,unexpected=1))
            with self.assertRaises(ValueError): module.compute([])

    def test_demos_run_from_unrelated_working_directory(self):
        import tempfile
        with tempfile.TemporaryDirectory() as temp:
            for path in PATHS.values():
                for fmt in ('json','markdown'):
                    run=subprocess.run([sys.executable,str(path),'--demo','--format',fmt],cwd=temp,capture_output=True,text=True)
                    self.assertEqual(run.returncode,0,run.stderr)
                    if fmt=='json': self.assertIn('method',json.loads(run.stdout))
                    else: self.assertTrue(run.stdout.startswith('# '))

    def test_cli_stdin_and_errors(self):
        for name,path in PATHS.items():
            run=subprocess.run([sys.executable,str(path),'--input','-','--format','json'],input=json.dumps(MODULES[name].DEMO),capture_output=True,text=True)
            self.assertEqual(run.returncode,0,run.stderr)
            for bad in ('{','{"unit":"a","unit":"b"}','[]','null'):
                run=subprocess.run([sys.executable,str(path),'--input','-'],input=bad,capture_output=True,text=True)
                self.assertEqual(run.returncode,2,run.stderr)
                self.assertNotIn('Traceback',run.stderr)

    def test_finite_output_guard(self):
        for module in MODULES.values():
            with self.assertRaises(ValueError): module.finite_result({'nested':[float('inf')]})

if __name__=='__main__':
    unittest.main()
