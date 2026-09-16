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


class VisualTests(unittest.TestCase):
    def test_generated_examples_match_source(self):
        for slug, module in [('gantt-chart', gantt), ('raci-matrix', raci)]:
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
        data=raci.demo();del data['rows'][0]['cells']['OPS']
        with self.assertRaises(ValueError):raci.validate(data)

    def test_untrusted_text_is_escaped_and_csv_guarded(self):
        for module in (gantt,raci):
            data=module.demo();data['title']='</script><script>alert(1)</script>'
            item=data['tasks'][0] if module is gantt else data['rows'][0]
            item['label']='=WEBSERVICE("example")'
            svg=module.render_svg(data);csv=module.render_csv(data);html=module.render_html(data,svg,csv)
            self.assertNotIn(data['title'],html)
            self.assertIn("'=WEBSERVICE",csv)
            self.assertNotRegex(html,r'<(?:script|link)\b[^>]*(?:src|href)="https?://')

    def test_isolated_cli_outputs_and_windows_csv_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            for module in (gantt,raci):
                script=Path(temp)/Path(module.__file__).name
                script.write_bytes(Path(module.__file__).read_bytes())
                stem=Path(temp)/script.stem
                run=subprocess.run([sys.executable,'-I',str(script),'--demo','--output',str(stem)],cwd=temp,capture_output=True,text=True)
                self.assertEqual(run.returncode,0,run.stderr)
                for suffix in ('.svg','.html','.json','.csv'):self.assertTrue(Path(str(stem)+suffix).is_file())
                self.assertNotIn(b'\r\r\n',Path(str(stem)+'.csv').read_bytes())
                self.assertEqual(json.loads(Path(str(stem)+'.json').read_text(encoding='utf-8')),module.demo())


if __name__ == '__main__': unittest.main()
