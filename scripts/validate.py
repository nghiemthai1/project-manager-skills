"""Validate package structure, metadata, catalog drift, and repository-local links."""
import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ('Purpose','Input','Key Concepts','Application','Examples','Common Pitfalls','References')
TYPES = {'component','interactive','workflow'}
# Reviewed target inventory is independent of which folders happen to exist.
# Adding an empty folder cannot make an omitted planned package disappear.
LIBRARY_PATH = 'catalog/library.json'


def library_rows(root):
    rows = json.loads((root/LIBRARY_PATH).read_text(encoding='utf-8'))
    if not isinstance(rows, list) or not rows:
        raise ValueError('library manifest must be a nonempty list')
    names = [row['name'] for row in rows]
    if len(set(names)) != len(names):
        raise ValueError('duplicate names in library manifest')
    for row in rows:
        for key in ('name', 'category', 'focus', 'frameworks', 'type'):
            if not isinstance(row[key], str) or not row[key].strip():
                raise ValueError(f'library row requires nonempty {key}')
        if row['type'] not in TYPES:
            raise ValueError(f"invalid library type: {row['name']}")
    return rows


def framework_tables(entries, library, prefix=''):
    by_name = {entry['name']: entry for entry in entries}
    categories = list(dict.fromkeys(row['category'] for row in library))
    lines = []
    for category in categories:
        rows = [row for row in library if row['category'] == category]
        lines.extend([f'### {category} ({len(rows)})', '', '| Skill | Focus | Framework |', '|---|---|---|'])
        for row in rows:
            entry = by_name.get(row['name'])
            if entry is None:
                continue
            lines.append(f"| [{entry['title']}]({prefix}{entry['path']}) | {row['focus']} | {row['frameworks']} |")
        lines.append('')
    return '\n'.join(lines).rstrip()


TABLE_START = '<!-- skill-framework-catalog:start -->'
TABLE_END = '<!-- skill-framework-catalog:end -->'



def frontmatter(text):
    parts=text.split('---',2)
    if len(parts)!=3 or parts[0].strip():
        raise ValueError('missing opening YAML frontmatter')
    result=yaml.safe_load(parts[1])
    if not isinstance(result,dict): raise ValueError('frontmatter must be a mapping')
    return result,parts[2]


def without_fences(text):
    result=[]
    fence=None
    for line in text.splitlines():
        mark=re.match(r'^\s*(`{3,}|~{3,})',line)
        if mark:
            token=mark.group(1)
            if fence is None: fence=token[0]
            elif token[0]==fence: fence=None
            continue
        if fence is None: result.append(line)
    return '\n'.join(result)


def bundle_root(path,root):
    for parent in (path.parent,*path.parents):
        if not parent.is_relative_to(root): break
        index=parent/'index.md'
        if index.exists():
            try:
                data,_=frontmatter(index.read_text(encoding='utf-8'))
                if data.get('okf_version')=='0.2': return parent
            except (ValueError,yaml.YAMLError): pass
    return root


def local_link_errors(path,root):
    text=without_fences(path.read_text(encoding='utf-8'))
    errors=[]
    for target in re.findall(r'!?\[[^\]\n]+\]\(([^)]+)\)',text):
        target=target.strip().split(' "',1)[0].strip('<>')
        parsed=urlsplit(target)
        if parsed.scheme or target.startswith('//'): continue
        filename=unquote(parsed.path)
        if not filename: continue
        resolved=((bundle_root(path,root)/filename.lstrip('/')) if filename.startswith('/') else path.parent/filename).resolve()
        if not resolved.is_relative_to(root):
            errors.append(f'{path.relative_to(root)}: link escapes package: {target}')
        elif not resolved.exists():
            errors.append(f'{path.relative_to(root)}: missing link target: {target}')
    return errors


def validate(root=ROOT):
    root=root.resolve()
    errors=[]
    entries=[]
    try:
        library = library_rows(root)
    except (ValueError, KeyError, TypeError, OSError) as exc:
        return [f'library manifest: {exc}'], []
    expected = {row['name'] for row in library}
    intended = {row['name']: row for row in library}
    found={p.parent.name for p in (root/'skills').glob('*/SKILL.md')}
    if found!=expected:
        errors.append(f'skill set mismatch: missing={sorted(expected-found)}, unexpected={sorted(found-expected)}')
    for path in sorted((root/'skills').glob('*/SKILL.md')):
        slug=path.parent.name
        try:
            data,body=frontmatter(path.read_text(encoding='utf-8'))
            if data.get('name')!=slug or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug) or len(slug)>64:
                errors.append(f'{slug}: invalid or mismatched name')
            description=data.get('description')
            if not isinstance(description,str) or not 1<=len(description)<=200:
                errors.append(f'{slug}: invalid description')
            meta=data.get('metadata',{})
            if not isinstance(meta,dict) or meta.get('type') not in TYPES or any(not isinstance(v,str) for v in meta.values()):
                errors.append(f'{slug}: metadata must be string-valued with a supported type')
            headings = re.findall(r'^## (.+)$', without_fences(body), re.MULTILINE)
            required_headings = [heading for heading in headings if heading in REQUIRED]
            if required_headings != list(REQUIRED):
                errors.append(f'{slug}: required sections must occur once in the prescribed order')
            if slug in intended and meta.get('type') != intended[slug]['type']:
                errors.append(f'{slug}: type differs from reviewed library manifest')
            if re.search(r'\b(?:TODO|FIXME|TBD_AUTHOR)\b',body): errors.append(f'{slug}: unfinished author scaffold')
            for relative in ('template.md','examples/software.md','examples/migration.md','agents/openai.yaml'):
                if not (path.parent/relative).is_file(): errors.append(f'{slug}: missing {relative}')
            ui=yaml.safe_load((path.parent/'agents/openai.yaml').read_text(encoding='utf-8'))['interface']
            if not 25<=len(ui['short_description'])<=64: errors.append(f'{slug}: UI short description length')
            if '$'+slug not in ui['default_prompt']: errors.append(f'{slug}: UI prompt missing explicit invocation')
            entries.append({'name':slug,'title':ui['display_name'],'type':meta.get('type'),'description':description,'path':f'skills/{slug}/SKILL.md','category':intended.get(slug,{}).get('category'),'focus':intended.get(slug,{}).get('focus'),'frameworks':intended.get(slug,{}).get('frameworks')})
        except (ValueError,yaml.YAMLError,KeyError,TypeError,OSError) as exc:
            errors.append(f'{slug}: {exc}')
    catalog=root/'catalog/skills.json'
    if catalog.exists():
        try:
            if json.loads(catalog.read_text(encoding='utf-8'))!=entries: errors.append('catalog/skills.json differs from skill metadata; rebuild catalog')
        except (ValueError,OSError) as exc: errors.append(f'catalog: {exc}')
    else: errors.append('catalog/skills.json missing')
    readme = (root/'README.md').read_text(encoding='utf-8')
    table_block = TABLE_START+'\n'+framework_tables(entries, library)+'\n'+TABLE_END
    if table_block not in readme:
        errors.append('README framework catalog differs from manifest; rebuild catalog')
    for path in root.rglob('*.md'):
        rel=path.relative_to(root)
        if any(part.startswith('.') for part in rel.parts) or rel.parts[0]=='meeting-knowledge-graph' or path.name.startswith('TLDR_AI_'):
            continue
        errors.extend(local_link_errors(path,root))
    return errors,entries


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build-catalog',action='store_true',help='write metadata catalog and task-oriented Markdown index')
    args=parser.parse_args()
    errors,entries=validate()
    if args.build_catalog:
        target=ROOT/'catalog'; target.mkdir(exist_ok=True)
        (target/'skills.json').write_text(json.dumps(entries,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
        library = library_rows(ROOT)
        tables = framework_tables(entries, library, '../')
        (target/'README.md').write_text('# Skill catalog\n\n'+f'{len(entries)} packages. Frameworks explain the methods used; they do not establish certification or field reliability. Read each skill for fit, limits, examples and failure analysis.\n\n'+tables+'\n',encoding='utf-8')
        readme_path = ROOT/'README.md'
        readme = readme_path.read_text(encoding='utf-8')
        block = TABLE_START+'\n'+framework_tables(entries, library)+'\n'+TABLE_END
        if TABLE_START in readme and TABLE_END in readme:
            start = readme.index(TABLE_START)
            end = readme.index(TABLE_END, start)+len(TABLE_END)
            readme = readme[:start]+block+readme[end:]
        else:
            readme = readme.replace('## Calculation helpers', '## Skills and frameworks\n\n'+block+'\n\n## Calculation helpers')
        readme_path.write_text(readme,encoding='utf-8')
        errors,_=validate()
    if errors:
        for error in errors: print(error,file=sys.stderr)
        return 1
    print(f'Validated {len(entries)} skill packages, metadata catalog, and repository-local links.')
    print('Structural validation does not establish teaching quality or real-world reliability.')
    return 0

if __name__=='__main__': raise SystemExit(main())
