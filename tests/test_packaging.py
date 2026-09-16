"""Verify the extracted Codex payload, not just the ZIP filename."""
import importlib.util
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
                self.assertEqual(sum(n.endswith('/SKILL.md') for n in names),30)
                self.assertTrue(all(n=='AGENTS.md' or n.startswith('.agents/skills/') for n in names))
                self.assertFalse(any('__pycache__' in n or n.endswith('.pyc') for n in names))
                for path in (ROOT/'skills').rglob('*'):
                    if path.is_file() and path.suffix in module.ALLOWED:
                        name='.agents/skills/'+path.relative_to(ROOT/'skills').as_posix()
                        self.assertEqual(bundle.read(name),path.read_bytes().replace(b'\r\n',b'\n'))
                self.assertEqual(bundle.read('AGENTS.md'),(ROOT/'packaging/codex/AGENTS.md').read_bytes().replace(b'\r\n',b'\n'))
                bundle.extractall(target/'project')
            for helper in (target/'project/.agents/skills').glob('*/scripts/*.py'):
                result=subprocess.run([sys.executable,'-I',str(helper),'--demo'],cwd=target/'project',capture_output=True,text=True)
                self.assertEqual(result.returncode,0,result.stderr)
            first=archive.read_bytes()
            self.assertEqual(first,(target/'dist/codex-project-manager-skills.zip').read_bytes())
            self.assertEqual(first,module.build(output=target/'second').read_bytes())

if __name__=='__main__': unittest.main()
