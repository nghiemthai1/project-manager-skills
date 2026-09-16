"""Audit trigger metadata and display curated positive/sibling-negative cases.

This tool does not call a model or claim automatic-routing accuracy. Execute the
cases independently and retain observed selections to test routing behavior.
"""
import argparse
import json
from pathlib import Path
import re
import sys
import yaml
from validate import ROOT, frontmatter, library_rows


def check(data,cases,names):
    errors=[]
    name=data.get('name')
    description=data.get('description','')
    if not isinstance(description,str) or not 1<=len(description)<=200:
        errors.append('invalid trigger description length')
    elif not re.search(r'\bUse (?:when|for|before|during|after|to)\b',description,re.I):
        errors.append('description lacks usage trigger')
    case=cases.get(name)
    if not isinstance(case,dict):
        return errors+['missing curated trigger cases']
    for key in ('positive','negative'):
        if not isinstance(case.get(key),str) or not case.get(key,'').strip():
            errors.append(f'missing {key} user request')
    if case.get('positive')==case.get('negative'):
        errors.append('positive and negative cases must differ')
    if case.get('negative_skill') not in names or case.get('negative_skill')==name:
        errors.append('negative case needs a different reviewed sibling skill')
    return errors


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paths',nargs='*',type=Path,help='SKILL.md paths; omit for all')
    parser.add_argument('--show-cases',action='store_true')
    args=parser.parse_args()
    cases=json.loads((ROOT/'evals/trigger-cases.json').read_text(encoding='utf-8'))
    names={row['name'] for row in library_rows(ROOT)}
    paths=args.paths or sorted((ROOT/'skills').glob('*/SKILL.md'))
    failures=0
    if set(cases)!=names:
        print('trigger case inventory differs from reviewed library',file=sys.stderr)
        failures+=1
    for path in paths:
        try:
            data,_=frontmatter(path.read_text(encoding='utf-8'))
            errors=check(data,cases,names)
            failures+=bool(errors)
            for error in errors:
                print(f'{path.parent.name}: {error}',file=sys.stderr)
            if args.show_cases:
                print(json.dumps({'name':data.get('name'),'description':data.get('description'),'cases':cases.get(data.get('name'))},ensure_ascii=False))
        except (ValueError,OSError,TypeError,yaml.YAMLError) as exc:
            print(f'{path}: {exc}',file=sys.stderr)
            failures+=1
    print(f'Trigger readiness: {len(paths)} descriptions inspected; {failures} failing checks. Model routing has not been executed by this tool.')
    return 1 if failures else 0


if __name__=='__main__':
    raise SystemExit(main())
