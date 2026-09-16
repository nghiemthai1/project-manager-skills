"""Verify the extracted Codex payload, not just the ZIP filename."""
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile
import yaml

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
                for slug in expected:
                    license_name=f'.agents/skills/{slug}/LICENSE.md'
                    self.assertEqual(bundle.read(license_name),(ROOT/'skills'/slug/'LICENSE.md').read_bytes().replace(b'\r\n',b'\n'))
                for helper in (ROOT/'skills').glob('*/scripts/*.py'):
                    code_license=helper.parent/'LICENSE.md'
                    self.assertEqual(code_license.read_text(encoding='utf-8'),(ROOT/'LICENSE.md').read_text(encoding='utf-8'))
                    self.assertIn(b'MIT License',bundle.read('.agents/skills/'+helper.relative_to(ROOT/'skills').as_posix()))
                for asset in ('software.mmd','software.svg','migration.mmd','migration.svg'):
                    self.assertIn('.agents/skills/gantt-chart/examples/assets/'+asset,names)
                for slug in ('gantt-chart', 'raci-matrix'):
                    for scene in ('software', 'migration'):
                        for extension in ('.html', '.svg', '.json', '.csv'):
                            self.assertIn(f'.agents/skills/{slug}/examples/assets/{scene}{extension}', names)
                for slug in json.loads((ROOT/'catalog/upstream-sources.json').read_text(encoding='utf-8')):
                    self.assertIn(f'.agents/skills/{slug}/SOURCE.md',names)
                    self.assertIn(f'.agents/skills/{slug}/LICENSE.md',names)
                self.assertTrue(all(n=='AGENTS.md' or n.startswith('.agents/skills/') for n in names))
                self.assertFalse(any('__pycache__' in n or n.endswith('.pyc') for n in names))
                for path in (ROOT/'skills').rglob('*'):
                    if path.is_file() and path.suffix in module.ALLOWED:
                        name='.agents/skills/'+path.relative_to(ROOT/'skills').as_posix()
                        expected_bytes=path.read_bytes()
                        if path.suffix in {'.md','.yaml','.yml','.json','.py','.mmd','.svg','.csv','.html'}:
                            expected_bytes=expected_bytes.replace(b'\r\n',b'\n')
                        if path.name == 'SKILL.md':
                            source_parts = expected_bytes.decode('utf-8').split('---',2)
                            install_parts = bundle.read(name).decode('utf-8').split('---',2)
                            source_header = yaml.safe_load(source_parts[1])
                            install_header = yaml.safe_load(install_parts[1])
                            self.assertNotIn('metadata',source_header)
                            self.assertTrue(set(install_header) <= {'name','description','license','compatibility','allowed-tools','metadata'})
                            expanded = {key:value for key,value in install_header.items() if key != 'metadata'}
                            for key,value in install_header.get('metadata',{}).items():
                                self.assertIsInstance(value,str)
                                expanded[key] = json.loads(value) if key in ('best_for','scenarios') else value
                            self.assertEqual(expanded,source_header)
                            self.assertEqual(install_parts[2],source_parts[2])
                        else:
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
            (package/'SKILL.md').write_bytes(b'---\r\nname: example\r\ndescription: Example skill\r\n---\r\n# Example\r\n')
            image_bytes=b'\x89PNG\r\n\x1a\n\x00\r\n\xff'
            (package/'example.png').write_bytes(image_bytes)
            (package/'example.mmd').write_bytes(b'gantt\r\n')
            with ZipFile(module.build(root=root,output=Path(temporary)/'dist')) as bundle:
                self.assertEqual(bundle.read('.agents/skills/example/example.png'),image_bytes)
                self.assertEqual(bundle.read('.agents/skills/example/example.mmd'),b'gantt\n')

if __name__=='__main__': unittest.main()
