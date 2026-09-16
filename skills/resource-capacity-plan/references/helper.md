# Capacity helper

```sh
python scripts/capacity.py --demo --format json
python scripts/capacity.py --input capacity.json --format markdown
```

Required JSON:

```json
{"period":"2026-10-19 through 2026-10-30","people":[{"id":"Omar","gross_hours":80,"leave_hours":8,"overhead_hours":16,"allocations":[{"project":"Relay","hours":48},{"project":"support","hours":16}]}]}
```

All hour values are finite and nonnegative. People and project allocation IDs must be unique within their respective scope. People cannot be empty; an explicitly empty allocations list means no allocated demand. Missing assignments must be resolved before using the tool; it cannot detect work omitted from input. Leave plus overhead cannot exceed gross hours.

Availability = gross - leave - overhead. Demand is the sum of allocations. Remaining = available - demand. Person overload = max(0, demand - available). Load percent = demand / available * 100, or null when availability is zero. Output preserves person-level overload even if team-level totals have spare hours. It does not infer skill interchangeability, optimal utilization, or daily timing.


Use `--input -` for stdin. Unknown fields and duplicate JSON keys are errors. Valid results exit 0; invalid input, unsupported values, numeric overflow, or read failures exit 2 with an explanation on stderr. Output goes to stdout, and input files are never changed. The helper uses Python 3.11+ standard library only and works from any current directory when invoked by its path.
