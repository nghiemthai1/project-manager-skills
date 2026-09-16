# MIT License
#
# Copyright (c) 2026 Thai Nghiem
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""Three-point estimates in one declared unit. No probability-of-deadline claims."""

def compute(data):
    obj(data, ('unit', 'optimistic', 'most_likely', 'pessimistic'))
    unit = label(data['unit'], 'unit')
    o, m, p = [number(data[k], k) for k in ('optimistic', 'most_likely', 'pessimistic')]
    if not o <= m <= p:
        raise ValueError('require optimistic <= most_likely <= pessimistic')
    triangular = o/3 + m/3 + p/3
    pert = o/6 + (2/3)*m + p/6
    spread = (p-o)/6
    return {'method': 'Three-point estimation', 'unit': unit, 'optimistic': o,
            'most_likely': m, 'pessimistic': p, 'triangular_mean': triangular,
            'pert_mean': pert, 'pert_standard_deviation_heuristic': spread,
            'assumptions': ['Inputs describe the same scoped task and unit.',
                            'PERT weights the most-likely case four times; these are elicited estimates.',
                            'The spread heuristic is not a validated confidence interval or a deadline probability.']}

DEMO = {'unit': 'person_days', 'optimistic': 2, 'most_likely': 4, 'pessimistic': 12}


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
