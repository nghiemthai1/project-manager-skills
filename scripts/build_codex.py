"""Build a Codex archive, repeatable within the same compression runtime."""
import argparse
from pathlib import Path
import shutil
from zipfile import ZipFile, ZipInfo, ZIP_DEFLATED

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {'.md', '.yaml', '.yml', '.json', '.py', '.mmd', '.svg', '.csv', '.html'}
BINARY_SUFFIXES = {'.png'}
ALLOWED = TEXT_SUFFIXES | BINARY_SUFFIXES


def payload_bytes(source):
    data = source.read_bytes()
    return data.replace(b'\r\n', b'\n') if source.suffix in TEXT_SUFFIXES else data


def build(root=ROOT, output=None):
    root = Path(root).resolve()
    output = Path(output) if output else root/'dist/codex'
    entries = {'AGENTS.md': (root/'packaging/codex/AGENTS.md').read_bytes()}
    packages = sorted((root/'skills').glob('*/SKILL.md'))
    if not packages:
        raise ValueError('No skill packages found')
    for entrypoint in packages:
        for source in sorted(entrypoint.parent.rglob('*')):
            relative = source.relative_to(root/'skills')
            if any(part.startswith('.') or part == '__pycache__' for part in relative.parts):
                continue
            if source.is_symlink():
                raise ValueError(f'Symlinks are not packaged: {relative}')
            if source.is_file() and source.suffix in ALLOWED:
                # Normalize text line endings so Windows and Linux payloads match.
                entries['.agents/skills/'+relative.as_posix()] = payload_bytes(source)
    entries['AGENTS.md'] = entries['AGENTS.md'].replace(b'\r\n', b'\n')
    output.mkdir(parents=True, exist_ok=True)
    archive = output/'codex-project-manager-skills.zip'
    with ZipFile(archive, 'w', compression=ZIP_DEFLATED) as bundle:
        for name, content in sorted(entries.items()):
            info = ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            bundle.writestr(info, content)
    alias = output/'pm-skills-codex.zip'
    shutil.copyfile(archive, alias)
    return alias


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, help='output directory (default: dist/codex)')
    args = parser.parse_args()
    print(build(output=args.output))
