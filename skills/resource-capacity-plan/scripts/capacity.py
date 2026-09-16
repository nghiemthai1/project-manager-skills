"""Capacity and allocated demand by person in hours for one stated period."""

def compute(data):
    obj(data, ('period', 'people'))
    period = label(data['period'], 'period')
    if not isinstance(data['people'], list) or not data['people']:
        raise ValueError('people must be a nonempty list')
    rows, ids = [], set()
    for person in data['people']:
        obj(person, ('id', 'gross_hours', 'leave_hours', 'overhead_hours', 'allocations'))
        who = label(person['id'], 'person id')
        if who in ids:
            raise ValueError(f'duplicate person id: {who}')
        ids.add(who)
        gross, leave, overhead = [number(person[k], k) for k in ('gross_hours', 'leave_hours', 'overhead_hours')]
        available = gross - leave - overhead
        if available < 0:
            raise ValueError(f'{who}: leave plus overhead exceeds gross hours')
        if not isinstance(person['allocations'], list):
            raise ValueError(f'{who}: allocations must be a list; [] explicitly means none')
        projects, demand = set(), 0.0
        for allocation in person['allocations']:
            obj(allocation, ('project', 'hours'))
            project = label(allocation['project'], 'project')
            if project in projects:
                raise ValueError(f'{who}: duplicate project allocation: {project}')
            projects.add(project)
            demand += number(allocation['hours'], 'allocated hours')
        rows.append({'id': who, 'available_hours': available, 'demand_hours': demand,
                     'remaining_hours': available-demand, 'overload_hours': max(0.0,demand-available),
                     'load_percent': 100*(demand/available) if available else None})
    return {'method': 'Capacity against allocated demand', 'period': period, 'unit': 'hours', 'people': rows,
            'total_available_hours': sum(r['available_hours'] for r in rows),
            'total_demand_hours': sum(r['demand_hours'] for r in rows),
            'sum_person_overload_hours': sum(r['overload_hours'] for r in rows),
            'assumptions': ['All allocations cover the same period; missing projects understate demand.',
                            'Leave and overhead are disjoint deductions; no automatic utilization haircut is applied.',
                            'Spare hours on another person do not establish interchangeable skills or resolve an overload.']}

DEMO = {'period': '2026-10-19 through 2026-10-30', 'people': [
    {'id': 'Omar', 'gross_hours': 80, 'leave_hours': 8, 'overhead_hours': 16,
     'allocations': [{'project': 'Relay', 'hours': 48}, {'project': 'support', 'hours': 16}]},
    {'id': 'Lena', 'gross_hours': 40, 'leave_hours': 0, 'overhead_hours': 8,
     'allocations': [{'project': 'Relay', 'hours': 20}]}]}


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
