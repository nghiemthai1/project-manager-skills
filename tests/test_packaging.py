"""Verify the extracted Codex payload, not just the ZIP filename."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('build_codex',ROOT/'scripts/build_codex.py')
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class PackagingTests(unittest.TestCase):
    def test_archive_layout_payload_and_extracted_helpers(self):
        with tempfile.TemporaryDirectory() as temporary:
            target=Path(temporary)
            archive=module.build(output=target/'dist')
            with ZipFile(archive) as bundle:
                names=bundle.namelist()
                self.assertIn('AGENTS.md',names)
                expected={row['name'] for row in json.loads((ROOT/'catalog/library.json').read_text(encoding='utf-8'))}
                actual={n.split('/')[2] for n in names if n.endswith('/SKILL.md')}
                self.assertEqual(actual,expected)
                for asset in ('software.mmd','software.svg','migration.mmd','migration.svg'):
                    self.assertIn('.agents/skills/gantt-chart/assets/'+asset,names)
                for slug in json.loads((ROOT/'catalog/upstream-sources.json').read_text(encoding='utf-8')):
                    self.assertIn(f'.agents/skills/{slug}/SOURCE.md',names)
                    self.assertIn(f'.agents/skills/{slug}/LICENSE.md',names)
                self.assertTrue(all(n=='AGENTS.md' or n.startswith('.agents/skills/') for n in names))
                self.assertFalse(any('__pycache__' in n or n.endswith('.pyc') for n in names))
                for path in (ROOT/'skills').rglob('*'):
                    if path.is_file() and path.suffix in module.ALLOWED:
                        name='.agents/skills/'+path.relative_to(ROOT/'skills').as_posix()
                        expected_bytes=path.read_bytes()
                        if path.suffix in {'.md','.yaml','.yml','.json','.py','.mmd','.svg','.csv'}:
                            expected_bytes=expected_bytes.replace(b'\r\n',b'\n')
                        self.assertEqual(bundle.read(name),expected_bytes)
                self.assertEqual(bundle.read('AGENTS.md'),(ROOT/'packaging/codex/AGENTS.md').read_bytes().replace(b'\r\n',b'\n'))
                bundle.extractall(target/'project')
            for helper in (target/'project/.agents/skills').glob('*/scripts/*.py'):
                result=subprocess.run([sys.executable,'-I',str(helper),'--demo'],cwd=target/'project',capture_output=True,text=True)
                self.assertEqual(result.returncode,0,result.stderr)
            first=archive.read_bytes()
            self.assertEqual(first,(target/'dist/codex-project-manager-skills.zip').read_bytes())
            self.assertEqual(first,module.build(output=target/'second').read_bytes())

    def test_binary_assets_survive_packaging(self):
        with tempfile.TemporaryDirectory() as temporary:
            root=Path(temporary)/'source'
            (root/'packaging/codex').mkdir(parents=True)
            (root/'packaging/codex/AGENTS.md').write_bytes(b'# Instructions\r\n')
            package=root/'skills/example'
            package.mkdir(parents=True)
            (package/'SKILL.md').write_bytes(b'# Example\r\n')
            image_bytes=b'\x89PNG\r\n\x1a\n\x00\r\n\xff'
            (package/'example.png').write_bytes(image_bytes)
            (package/'example.mmd').write_bytes(b'gantt\r\n')
            with ZipFile(module.build(root=root,output=Path(temporary)/'dist')) as bundle:
                self.assertEqual(bundle.read('.agents/skills/example/example.png'),image_bytes)
                self.assertEqual(bundle.read('.agents/skills/example/example.mmd'),b'gantt\n')

if __name__=='__main__': unittest.main()
