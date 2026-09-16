"""Check Dean-style metadata/section gates in this repo's portable metadata layout.

These checks are structural; they do not grade framework choice or execution.
"""
import argparse
from pathlib import Path
import re
import sys
import yaml
from validate import ROOT, REQUIRED, TYPES, frontmatter, without_fences, local_link_errors


def check(path):
    errors=[]
    try:
        data,body=frontmatter(path.read_text(encoding='utf-8'))
        name=data.get('name')
        if not isinstance(name,str) or len(name)>64 or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name):
            errors.append('name must be kebab-case, at most 64 characters')
        if name!=path.parent.name:
            errors.append('name must match package directory')
        description=data.get('description')
        if not isinstance(description,str) or not 1<=len(description)<=200:
            errors.append('description must contain 1–200 characters')
        elif not re.search(r'\bUse (?:when|for|before|during|after|to)\b',description,re.I):
            errors.append('description needs a concrete usage trigger')
        metadata=data.get('metadata')
        if not isinstance(metadata,dict):
            errors.append('metadata must be a mapping')
        else:
            if metadata.get('type') not in TYPES:
                errors.append('unsupported skill type')
            if any(not isinstance(value,str) for value in metadata.values()):
                errors.append('metadata values must be strings for portability')
            if not isinstance(metadata.get('intent'),str) or not metadata.get('intent','').strip():
                errors.append('metadata.intent must explain the fuller job')
        headings=re.findall(r'^## (.+)$',without_fences(body),re.M)
        if [heading for heading in headings if heading in REQUIRED]!=list(REQUIRED):
            errors.append('required sections must appear once and in order')
        if re.search(r'\b(?:TODO|FIXME|TBD_AUTHOR)\b',body):
            errors.append('unfinished author scaffold')
        for relative in ('template.md','examples/software.md','examples/migration.md','agents/openai.yaml'):
            if not (path.parent/relative).is_file():
                errors.append(f'missing {relative}')
        if data.get('license')=='CC-BY-NC-SA-4.0':
            for relative in ('SOURCE.md','LICENSE.md'):
                if not (path.parent/relative).is_file():
                    errors.append(f'adaptation missing {relative}')
        if path.is_relative_to(ROOT):
            errors.extend(local_link_errors(path,ROOT))
    except (ValueError,TypeError,OSError,yaml.YAMLError) as exc:
        errors.append(str(exc))
    return errors


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paths',nargs='*',type=Path,help='SKILL.md paths; omit for the whole library')
    args=parser.parse_args()
    paths=[p.resolve() for p in args.paths] if args.paths else sorted((ROOT/'skills').glob('*/SKILL.md'))
    count=0
    for path in paths:
        errors=check(path)
        for error in errors:
            print(f'{path.parent.name}: {error}',file=sys.stderr)
        count+=bool(errors)
    print(f'Metadata gates: {len(paths)-count}/{len(paths)} packages pass. This is not a behavioral evaluation.')
    return 1 if count else 0


if __name__=='__main__':
    raise SystemExit(main())
