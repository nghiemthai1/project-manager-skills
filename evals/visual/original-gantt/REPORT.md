# Independent Gantt forward test

All fixtures are fictional. Canonical skills and helpers were not edited. Browser/keyboard/viewport QA is delegated to the parent task; this report covers actual helper execution, source fidelity, SVG geometry and validator behavior.

## Main result

Generated `schedule.html`, `schedule.svg` (1420 × 784), `schedule.json`, `schedule.csv` and `schedule-source.json` in this directory. Main diagnostics correctly identify T-01 partial actual, M-02 missing forecast, DEP-X FS-zero forecast conflict and DEP-Z external endpoint. No dates were repaired.

Command:

```powershell
.venv/Scripts/python.exe .work/gantt-forward-test/forward_test.py
```

The test invokes this CLI for each named fixture:

```powershell
.venv/Scripts/python.exe skills/gantt-chart/scripts/render_gantt.py .work/gantt-forward-test/schedule-source.json --output .work/gantt-forward-test/schedule
```

Full observations and paths are in `test-results.json`.

## Mapping and assumptions

| Supplied fact | Normalized field | Treatment |
|---|---|---|
| Schedule dated 2028-02-28 | as_of | Exact ISO date |
| Monday–Friday and Feb 29 holiday | calendar | Weekdays 0–4, holiday 2028-02-29; no rescheduling |
| T-01 / S-1 and dates | task ID/source, forecast, comparison | Exact source values; comparison approval unknown |
| Actual began Feb 28, no finish | T-01 actual | Start 2028-02-28, finish null; mapping to work T-01 explicitly labeled assumption |
| M-02 / S-2 without dates | milestone with null layers | Retained without invented bar or diamond |
| R-03 review Mar 1–2 | forecast | Exact dates; source ID not supplied, source points to fictional request |
| Unknown owners/progress/acceptance | explicit unknown owners, null progress, caveat | No zero-progress or accepted/completed claim |
| DEP-X FS zero, DEP-Z external SS +2 working days | links | Exact IDs/types/lag retained; zero lag unit not supplied is labeled unknown |
| Endpoint convention not supplied | [start, finish) | Explicit renderer/display assumption; written dates unchanged |

## Verified behavior

- JSON exact round-trip for primary, cycle, empty, partial and long fixtures.
- Forecast and comparison SVG geometry matches their exact source endpoints; the Feb 29 holiday occupies the correct daily band.
- Partial actual start produces no completed interval; M-02 produces no dated milestone.
- Typed links and external endpoints survive JSON and readable dependency registers.
- Cycle fixture emits a cycle diagnostic; zero-length task emits its own warning without changing kind.
- Empty fixture says no dated intervals and draws no fabricated project date axis.
- Partial intervals and empty date objects are preserved with missing-data diagnostics.
- CSV has nine task/layer records and correct CRLF; embedded SVG/JSON/CSV downloads match files, ignoring the optional final newline.
- Long source label text survives JSON, and SVG parses with markup escaped.

## Reproduced defects

1. **Long owner text overlaps later tasks in SVG.** `long-source.json` includes both a long task label and long owner string. Task labels expand row height, but owner wrapping does not. In `long.svg`, T-01 owner text continues through baseline y=861 while M-02's first label begins at y=575. This corrupts task/owner association and affects the embedded HTML graphic and SVG download. Compute row height using all wrapped task and owner lines. The label-only expansion itself works in this fixture.
2. **Invalid calendar object crashes outside the validation error path.** `invalid-calendar-type-source.json` uses `calendar: null`. The renderer exits 1 with an uncaught AttributeError at `calendar.get('label')`; the CLI normally promises input errors as exit 2 with a concise diagnostic. Validate that calendar is a dict before accessing it. No artifacts were written for this malformed fixture.

## Limits

This is not a browser render review or screen-reader certification. The overlap defect is established from generated text coordinates; parent browser QA can inspect `long.html`. The renderer is a date-only snapshot reader, and this test does not claim working-day lag computation, resource feasibility or approval validation.
