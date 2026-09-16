"""Regression guards for recorded fixtures; these do not execute an AI model."""
import importlib.util
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import yaml

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / 'evals/outputs/meeting-bundle'

class EvidenceTests(unittest.TestCase):
    def test_meeting_source_turns_preserved_in_order(self):
        source=(ROOT/'evals/requests.md').read_text(encoding='utf-8')
        for day in ('03','06'):
            date='2026-11-'+day
            section=source.split('Meeting '+date+':',1)[1].split('Meeting ',1)[0]
            quotes=re.findall(r'T00[1-4] [^\n]+?: "([^"\n]+)"',section)
            self.assertEqual(len(quotes),4)
            record=(BUNDLE/'meetings'/f'{date}-connector.md').read_text(encoding='utf-8')
            positions=[record.index('"'+quote+'"') for quote in quotes]
            self.assertEqual(positions,sorted(positions))
            for turn in ('T001','T002','T003','T004'):
                self.assertIn('| '+turn+' |',record)

    def test_okf_metadata_and_evidence_links(self):
        def metadata(path):
            return yaml.safe_load(path.read_text(encoding='utf-8').split('---',2)[1])
        self.assertEqual(metadata(BUNDLE/'index.md')['okf_version'],'0.2')
        for path in BUNDLE.rglob('*.md'):
            if path.name in ('index.md','log.md'): continue
            data=metadata(path)
            self.assertIn(data['status'],('draft','stable','deprecated'))
            for key in ('type','title','description','tags','sources'):
                self.assertIn(key,data)
            for source in data['sources']:
                resource=source['resource']
                if resource.startswith('/'):
                    self.assertTrue((BUNDLE/resource.lstrip('/')).is_file())
        action=metadata(BUNDLE/'actions/vendor-residency.md')
        self.assertIsNone(action['due_date'])
        self.assertEqual(action['action_status'],'open')
        topic=metadata(BUNDLE/'topics/hosted-connector.md')
        self.assertEqual(topic['option_status'],'evaluating_not_approved')

    def test_helpers_work_as_isolated_copies(self):
        paths=[p for p in (ROOT/'skills').glob('*/scripts/*.py') if not p.name.startswith('render_')]
        self.assertEqual(len(paths),4)
        with tempfile.TemporaryDirectory() as temp:
            for path in paths:
                dest=Path(temp)/path.name
                shutil.copy2(path,dest)
                process=subprocess.run([sys.executable,'-I',str(dest),'--demo','--format','json'],cwd=temp,capture_output=True,text=True)
                self.assertEqual(process.returncode,0,process.stderr)
                self.assertIsInstance(json.loads(process.stdout),dict)

if __name__=='__main__': unittest.main()
