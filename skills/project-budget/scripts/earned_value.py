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

"""Cumulative earned value indicators in one currency and at one status date."""

def compute(data):
    obj(data, ('currency', 'as_of', 'pv', 'ev', 'ac', 'bac'))
    currency = label(data['currency'], 'currency')
    as_of = label(data['as_of'], 'as_of')
    from datetime import date
    try:
        parsed_date = date.fromisoformat(as_of)
    except ValueError:
        raise ValueError('as_of must be an ISO calendar date YYYY-MM-DD') from None
    if parsed_date.isoformat() != as_of:
        raise ValueError('as_of must be YYYY-MM-DD')
    pv, ev, ac, bac = [number(data[k], k) for k in ('pv','ev','ac','bac')]
    if bac <= 0:
        raise ValueError('bac must be greater than zero')
    if pv > bac or ev > bac:
        raise ValueError('pv and ev must not exceed the current approved bac; check baseline and earning rules')
    cpi = ev/ac if ac else None
    spi = ev/pv if pv else None
    if ev > 0 and ((ac > 0 and cpi == 0) or (pv > 0 and spi == 0)):
        raise ValueError('ratio underflow; rescale monetary inputs to a consistent unit')
    factor = cpi*spi if cpi and spi else None
    if factor is not None and (not math.isfinite(factor) or factor == 0):
        raise ValueError('composite ratio exceeds supported numeric range; rescale inputs')
    cpi_eac = bac/cpi if cpi else None
    composite_eac = ac+(bac-ev)/factor if factor else None
    atypical_eac = ac+(bac-ev)
    return {'method': 'Cumulative earned value', 'currency': currency, 'as_of': as_of,
            'pv': pv, 'ev': ev, 'ac': ac, 'bac': bac, 'cv': ev-ac, 'sv': ev-pv,
            'cpi': cpi, 'spi': spi, 'eac_cpi': cpi_eac, 'eac_cpi_spi': composite_eac,
            'eac_remaining_at_budget': atypical_eac,
            'vac_cpi': bac-cpi_eac if cpi_eac is not None else None,
            'assumptions': ['All values are cumulative at the same date, currency, scope, and approved baseline.',
                            'eac_cpi assumes observed cost efficiency continues; eac_cpi_spi also applies schedule efficiency to remaining cost.',
                            'eac_remaining_at_budget assumes past cost variance will not recur in remaining work.',
                            'None of these forecasts authorizes spending or is automatically the management forecast.',
                            'SV is in currency, not days; SPI approaches 1 at completed scope even if completion was late.',
                            'A zero denominator makes the corresponding ratio or forecast unavailable.']}

DEMO = {'currency': 'USD', 'as_of': '2026-10-16', 'pv': 50000, 'ev': 40000, 'ac': 48000, 'bac': 100000}


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
