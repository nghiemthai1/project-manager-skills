# Offline Gantt renderer

Run from this skill folder, or use absolute paths from another directory:

```sh
python scripts/render_gantt.py project-data.json --output output/project
python scripts/render_gantt.py --demo --output output/demo
```

Open the resulting `.html` in a browser. The same stem produces `.svg`, `.json` and `.csv`. No server, package installation or network access is needed. `--demo` without an output prints SVG. Exit code 2 means invalid input; validation completes before files are written. Use a new output stem to retain earlier snapshots.

## Input contract

Required snapshot strings: `title`, `version`, `as_of`, `source`, `scope`, `comparison_label`. State unknown metadata in words. Set `date_convention` to `[start, finish)`. `calendar` contains a descriptive `label`, `working_weekdays` (Monday=0 through Sunday=6), and an optional list of ISO `holidays`. This calendar controls shading; it does not move task dates.

`tasks` is a list with unique string `id`, `label`, `owner`, `source`, and `kind` (`task`, `milestone`, `summary`). Optional `phase` references a declared presentation phase, and optional `tone` chooses `product`, `design`, `platform`, or `quality` for non-critical forecast bars. Optional `parent` preserves the source hierarchy ID without calculating rollups. `comparison`, `forecast` and `actual` are null or objects with date-only ISO `start` and `finish`, either of which can be null. Partial intervals remain in the table and diagnostics without a fabricated bar. A milestone's known start and finish must agree. Comparison labels identify a scenario, target or named approved baseline; the helper does not establish approval.

Optional `progress` has `percent` (0–100), `meaning` and `source`. It appears in details, not as an ambiguous filled bar. Extra fields remain in JSON. Use `notes` for source caveats that must be visible in the static output.

Optional `presentation` provides the evidence-led reading path: `eyebrow`, `headline`, `lede`, `default_task_id`, one or more `metrics` (`label`, `value`, `note`, and optional `tone: "risk"`), `insight_heading`, `insight_points`, and `decision`. Its optional `phases` list uses unique `{id, index, name}` records; task phase references are validated before output. Optional `analysis` records a `method` plus supplied forecast task facts, critical IDs/paths and duration. The renderer displays this material but does not calculate or certify it. Only include criticality, float or scenario claims that were computed or supplied by an appropriate schedule model and whose assumptions are stated in `analysis.method`.

`links` is a list of unique `id`, `from`, `to`, `type` (FS/SS/FF/SF), numeric `lag`, `lag_unit`, `source`, and explicit Boolean `inferred`. Missing endpoints remain in the register. Zero-lag timing and nonzero `calendar_days` timing can be checked directly. Other nonzero lags are retained with a scheduling-engine diagnostic. No dates are repaired. Dependency/hierarchy cycles are reported without dropping source rows.

## Actual behavior and limits

- HTML builds a grouped product Gantt from the normalized data. It provides search, phase and owner filters; critical-only review; comparison and dependency toggles; zoom; keyboard row navigation; selected predecessor/successor highlighting; persistent details; a current-draft table; browser-local task editing; source/full-draft/visible-draft exports; reset; and a print/PDF layout with active-filter context. There is no dragging, source writeback, computed critical path or hierarchy collapse.
- Desktop, landscape, and portrait use one horizontally scrollable schedule surface with a sticky date header and frozen task pane. Phase rows remain visible in the same grid, empty filters show an explicit recovery state, and selected task facts never depend on hover. The complete source table, analysis method, diagnostics, dependency register and caveats are available through disclosures.
- The standalone SVG remains a complete editorial report with headline, metrics, task grid, bars, milestones, dependencies and source boundaries. The HTML renders its interactive grid independently so filters, zoom and dependency redraw remain synchronized.
- The three source download links contain the complete original snapshot irrespective of filters or local edits. **Draft JSON** includes current tasks, source basis, local history, diagnostics and an explicit analysis-revalidation warning. **Draft CSV** exports every current task/date layer, while **Visible draft CSV** reflects current filters. JSON is the authoritative full model; CSV does not encode the dependency graph, presentation or calendar. Formula-leading CSV text receives an apostrophe. The SVG uses direct source dates and supplied analysis labels.
- Supported data is date-only with one display calendar. Local saves validate canonical dates, non-inverted intervals, coincident milestone boundaries, phase/kind/tone values, progress evidence, required text and hierarchy-cycle prevention. Partial intervals remain explicit diagnostics. Existing typed links are checked against the edited forecast; violations are shown without moving downstream dates. Intraday schedules, calendar-driven lag arithmetic, time-zone conversion, resource leveling and vendor file parsing need separate tooling. Import guidance describes mapping decisions, not implemented adapters.
- This renderer is intended for small review artifacts. Inspect larger snapshots before relying on them. It creates all rows and links; it does not virtualize them. A successful five-task example proves nothing about ten thousand tasks.

## Local draft behavior

Select **Edit draft** and choose a chart row or current-draft table row. Task IDs and dependency topology stay source controlled. The form can change phase, kind, tone, label, owner, parent, comparison/forecast/actual boundaries, evidenced progress, source and note.

Changes persist in browser local storage for the artifact title, version and as-of date. Each save records before/after task state. **Undo** reverses the latest save, and **Restore source** clears all local task changes after confirmation. Invalid or stale stored data is ignored.

The chart axis, bars, milestones, owner filters, current-draft table, working-duration facts, supported diagnostics and finish metrics recalculate after a save. Supplied critical-path, float, scenario and presentation analysis remains visibly source-derived and is marked for revalidation. Local edits do not authorize a baseline, alter links, shift successors, write files, synchronize a source system or provide a governed audit log.

Review actual output at the intended sizes using [accessibility, export and testing](gantt-accessibility-export-and-testing.md) and [mobile-first responsive visualization](mobile-first-responsive-visualization.md). Exercise invalid dates, milestone mismatch, hierarchy-cycle prevention, dependency conflicts, range/metric recalculation, reload persistence, sequential undo, source restore and source/draft export separation. If only source generation was tested, say so. Do not label browser print output a delivered PDF until that file has been generated and inspected.
