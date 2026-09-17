# Offline Gantt renderer

Run from this skill folder, or use absolute paths from another directory:

```sh
python scripts/render_gantt.py project-data.json --output output/project
python scripts/render_gantt.py --demo --output output/demo
```

Open the resulting `.html` in a browser. The same stem produces `.svg`, `.json` and `.csv`. No server, package installation or network access is needed. `--demo` without an output prints SVG. Exit code 2 means invalid input; validation completes before files are written. Use a new output stem to retain earlier snapshots.

## Input contract

Required snapshot strings: `title`, `version`, `as_of`, `source`, `scope`, `comparison_label`. State unknown metadata in words. Set `date_convention` to `[start, finish)`. `calendar` contains a descriptive `label`, `working_weekdays` (Monday=0 through Sunday=6), and an optional list of ISO `holidays`. This calendar controls shading; it does not move task dates.

`tasks` is a list with unique string `id`, `label`, `owner`, `source`, and `kind` (`task`, `milestone`, `summary`). Optional `parent` preserves the source hierarchy ID without calculating rollups. `comparison`, `forecast` and `actual` are null or objects with date-only ISO `start` and `finish`, either of which can be null. Partial intervals remain in the table and diagnostics without a fabricated bar. A milestone's known start and finish must agree. Comparison labels identify a scenario, target or named approved baseline; the helper does not establish approval.

Optional `progress` has `percent` (0–100), `meaning` and `source`. It appears in details, not as an ambiguous filled bar. Extra fields remain in JSON. Use `notes` for source caveats that must be visible in the static output.

Optional `presentation` provides the evidence-led reading path: `eyebrow`, `headline`, `lede`, `default_task_id`, one or more `metrics` (`label`, `value`, `note`, and optional `tone: "risk"`), `insight_heading`, `insight_points`, and `decision`. Optional `analysis` records a `method` plus supplied forecast task facts, critical IDs/paths and duration. The renderer displays this material but does not calculate or certify it. Only include criticality, float or scenario claims that were computed or supplied by an appropriate schedule model and whose assumptions are stated in `analysis.method`.

`links` is a list of unique `id`, `from`, `to`, `type` (FS/SS/FF/SF), numeric `lag`, `lag_unit`, `source`, and explicit Boolean `inferred`. Missing endpoints remain in the register. Zero-lag timing and nonzero `calendar_days` timing can be checked directly. Other nonzero lags are retained with a scheduling-engine diagnostic. No dates are repaired. Dependency/hierarchy cycles are reported without dropping source rows.

## Actual behavior and limits

- HTML provides source search, owner filtering, keyboard-selectable persistent details, chart scaling, comparison/dependency visibility, critical-path emphasis and reset. Search/filter results hide task controls and dim unmatched SVG rows while keeping the network visible for context. There is no dragging, writeback, computed critical path or hierarchy collapse.
- Desktop and landscape use a fixed task grid beside a horizontally scrollable timeline. Portrait replaces that wide surface with task cards, mini-bars, exact dates and the same committed selection. The complete source table, analysis method, diagnostics, dependency register and caveats are available through disclosures. Exact values do not depend on hover.
- The standalone SVG is a full editorial report with headline, metrics, task grid, bars, milestones, dependencies and source boundaries. The HTML crops that same SVG to its timeline region so it can sit beside the fixed grid without duplicating the report header.
- Downloads contain the full original snapshot, irrespective of filters. JSON is the authoritative editable model; CSV exports three task date layers and does not encode the dependency graph, presentation or calendar. Formula-leading CSV text receives an apostrophe. The SVG uses direct dates and supplied analysis labels; HTML/JSON retain full task evidence.
- Supported data is date-only with one display calendar. Intraday schedules, calendar-driven lag arithmetic, time-zone conversion, resource leveling and vendor file parsing need separate tooling. Import guidance describes mapping decisions, not implemented adapters.
- This renderer is intended for small review artifacts. Inspect larger snapshots before relying on them. It creates all rows and links; it does not virtualize them. A successful five-task example proves nothing about ten thousand tasks.

Review actual output at the intended sizes using [accessibility, export and testing](gantt-accessibility-export-and-testing.md) and [mobile-first responsive visualization](mobile-first-responsive-visualization.md). If only source generation was tested, say so. Do not label browser print output a delivered PDF until that file has been generated and inspected.
