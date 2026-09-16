"""Finish-to-start, zero-lag CPM in duration units; not a calendar or resource scheduler."""

def compute(data):
    obj(data, ('unit', 'tasks'))
    unit = label(data['unit'], 'unit')
    if not isinstance(data['tasks'], list) or not data['tasks']:
        raise ValueError('tasks must be a nonempty list')
    nodes = {}
    for task in data['tasks']:
        obj(task, ('id', 'duration', 'predecessors'))
        ident = label(task['id'], 'task id')
        if ident in nodes:
            raise ValueError(f'duplicate task id: {ident}')
        duration = number(task['duration'], 'duration')
        if not isinstance(task['predecessors'], list):
            raise ValueError('predecessors must be a list')
        predecessors = [label(p, 'predecessor') for p in task['predecessors']]
        if len(set(predecessors)) != len(predecessors):
            raise ValueError(f'{ident}: duplicate predecessor')
        nodes[ident] = {'duration': duration, 'predecessors': predecessors, 'successors': []}
    for ident, node in nodes.items():
        for predecessor in node['predecessors']:
            if predecessor not in nodes:
                raise ValueError(f'{ident}: missing predecessor {predecessor}')
            nodes[predecessor]['successors'].append(ident)
    import heapq
    degree = {k: len(v['predecessors']) for k,v in nodes.items()}
    ready = [k for k,v in degree.items() if v == 0]
    heapq.heapify(ready)
    order = []
    while ready:
        ident = heapq.heappop(ready)
        order.append(ident)
        node = nodes[ident]
        node['es'] = max((nodes[p]['ef'] for p in node['predecessors']), default=0.0)
        node['ef'] = node['es'] + node['duration']
        for successor in node['successors']:
            degree[successor] -= 1
            if degree[successor] == 0:
                heapq.heappush(ready, successor)
    if len(order) != len(nodes):
        raise ValueError('dependency cycle detected; resolve it before CPM analysis')
    duration = max(n['ef'] for n in nodes.values())
    rows = []
    for ident in reversed(order):
        node = nodes[ident]
        node['lf'] = min((nodes[s]['ls'] for s in node['successors']), default=duration)
        node['ls'] = node['lf'] - node['duration']
        node['float'] = max(0.0, node['ls']-node['es'])
        node['critical'] = math.isclose(node['float'], 0.0, abs_tol=1e-9)
    for ident in order:
        n = nodes[ident]
        rows.append({'id': ident, 'duration': n['duration'], 'early_start': n['es'], 'early_finish': n['ef'],
                     'late_start': n['ls'], 'late_finish': n['lf'], 'total_float': n['float'], 'critical': n['critical']})
    edges = [{'from': a, 'to': b} for a in order for b in sorted(nodes[a]['successors'])
             if nodes[a]['critical'] and nodes[b]['critical'] and math.isclose(nodes[a]['ef'],nodes[b]['es'],abs_tol=1e-9,rel_tol=0)]
    return {'method': 'Unconstrained finish-to-start CPM', 'unit': unit, 'project_duration': duration,
            'tasks': rows, 'critical_activities': [r['id'] for r in rows if r['critical']], 'critical_edges': edges,
            'assumptions': ['One common project origin and finish; all terminal tasks must finish.',
                            'Finish-to-start links, zero lag, no date constraints, calendars, or resource leveling.',
                            'Zero-duration milestones are permitted. Multiple critical paths may exist.',
                            'A delivery-date gap is not total float. Output offsets are not calendar dates.']}

DEMO = {'unit': 'working_days', 'tasks': [
    {'id': 'A', 'duration': 2, 'predecessors': []},
    {'id': 'B', 'duration': 4, 'predecessors': ['A']},
    {'id': 'C', 'duration': 3, 'predecessors': ['A']},
    {'id': 'D', 'duration': 1, 'predecessors': ['B','C']}]}


import argparse
import json
import math
import sys
from pathlib import Path


def obj(value, required, optional=()):
    if not isinstance(value, dict):
        raise ValueError("expected a JSON object")
    missing = set(required) - value.keys()
    unknown = value.keys() - set(required) - set(optional)
    if missing or unknown:
        raise ValueError(f"missing fields: {sorted(missing)}; unknown fields: {sorted(unknown)}")
    return value


def number(value, name):
    if type(value) not in (int, float):
        raise ValueError(f"{name} must be a finite nonnegative number, not text or boolean")
    try:
        result = float(value)
    except OverflowError:
        raise ValueError(f"{name} exceeds supported numeric range") from None
    if not math.isfinite(result) or result < 0:
        raise ValueError(f"{name} must be a finite nonnegative number")
    return result


def label(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")
    return value.strip()


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON field: {key}")
        result[key] = value
    return result


def finite_result(value):
    if isinstance(value, float) and not math.isfinite(value):
        raise ValueError("calculation exceeded finite numeric range; reduce input magnitudes")
    if isinstance(value, dict):
        for item in value.values():
            finite_result(item)
    if isinstance(value, list):
        for item in value:
            finite_result(item)


def markdown(result):
    def cell(value):
        text = "Unavailable" if value is None else json.dumps(value, ensure_ascii=False) if isinstance(value, (dict, list)) else str(value)
        return text.replace("|", "\\|").replace("\n", " ")
    lines = ["# " + result['method'], ""]
    for key, value in result.items():
        if key == 'method':
            continue
        if isinstance(value, list) and value and isinstance(value[0], dict):
            columns = list(value[0])
            lines += ["## " + key.replace('_', ' ').title(), "", "| " + " | ".join(columns) + " |", "| " + " | ".join(['---']*len(columns)) + " |"]
            lines += ["| " + " | ".join(cell(row.get(c)) for c in columns) + " |" for row in value]
            lines += [""]
        else:
            lines += [f"- **{key.replace('_', ' ')}:** {cell(value)}"]
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--input', help='JSON file path, or - for stdin')
    source.add_argument('--demo', action='store_true', help='calculate the fictional worked input')
    parser.add_argument('--format', choices=('json', 'markdown'), default='markdown')
    args = parser.parse_args()
    try:
        raw = DEMO if args.demo else json.loads(sys.stdin.read() if args.input == '-' else Path(args.input).read_text(encoding='utf-8-sig'), object_pairs_hook=unique_object)
        result = compute(raw)
        finite_result(result)
        print(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) if args.format == 'json' else markdown(result))
    except (ValueError, OSError, OverflowError, RecursionError) as error:
        parser.exit(2, f"error: {error}\n")


if __name__ == '__main__':
    main()
