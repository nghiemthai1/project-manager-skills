# Capacity renderer contract

Use `scripts/render_capacity.py` when a capacity decision benefits from a portable review workspace rather than a prose table alone. It uses Python 3.11+ standard library and writes a self-contained HTML file, a static SVG snapshot, normalized JSON and spreadsheet-safe CSV.

```sh
python scripts/render_capacity.py capacity-source.json --output capacity-plan
python scripts/render_capacity.py --demo --output capacity-demo
```

## Source model

The top-level source records `title`, `version`, `as_of`, `source`, `scope`, `state`, `period`, `unit`, `people`, `constraints`, `options`, `presentation`, `analysis` and optional `notes`. The only supported unit is `hours`; convert other measures explicitly before rendering.

Each person needs a stable ID, display name, role, nonempty skill list, gross/leave/overhead hours, availability confirmation state and evidence, a timing note, source, and an explicit allocation list. Each allocation keeps a stable ID, work, required skill, window, hours, confirmation state, source and note. Use `hours: null` with `status: "unknown"` for known-but-unquantified demand. Never enter missing work as zero.

Constraints record the person, work, skill, window, conflict, consequence, status and source. Options record the proposed hours/timing change, skill or onboarding basis, effects, authority/status and recalculated result. These are evidence records; the renderer does not invent or approve either.

## Calculations and limits

For each person:

- availability = gross − leave − overhead;
- known demand = sum of allocations with numeric hours;
- remaining = availability − known demand;
- overload = max(0, known demand − availability);
- known load = known demand / availability when availability is positive;
- unknown allocations are counted and excluded from numeric demand.

Team totals summarize the supplied scope. They never cancel a person's overload or establish that skills are interchangeable. The renderer does not level resources, resolve intraday conflicts, calculate productive onboarding capacity or write to a planning system.

## Interactive editing

The HTML editor changes people and allocations only in browser local storage. It validates required evidence, nonnegative finite hours, leave plus overhead, allocation-state/hour consistency and unique IDs. It recalculates the chart, register and supported totals after a save. Timing/skill constraints and option outcomes stay as source evidence and receive a visible revalidation warning when the draft changes.

History retains up to 200 before/after person changes. Undo is sequential; restore source snapshot requires confirmation. Source SVG/JSON/CSV downloads remain byte-equivalent to the generated files. Draft JSON/CSV and visible-draft CSV are separate exports. Local edits do not confirm availability, authorize reassignment or write to a live system.

## Review gates

Validate the source and regenerate all formats. Compare generated artifacts with the source, inspect overloaded and spare people, and verify unknown allocations remain visible. In a real browser, test search, filters, overload-only mode, all four views, keyboard row selection, editing validation, persistence, undo, restore and downloads at desktop, portrait and landscape sizes. Print/PDF should state the period, source boundary and current draft context.
