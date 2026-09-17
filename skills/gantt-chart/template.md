# Gantt source, product and review template

- Project / audience / version / as-of date:
- Purpose: planning scenario, baseline proposal, forecast review, or actual history:
- Source classification: schedule engine, task tracker, roadmap, resource calendar, static export, or visual reconstruction:
- Source snapshot / export date / visible filter scope / permissions:
- Baseline approval and source (or explicitly none):
- Calendar: workweek, holidays, time zone, task-specific exceptions:
- Finish convention: inclusive last work date or exclusive finish boundary:
- Artifact mode: static explanation, read-only explorer, or editable planner:

## Source mapping

| Source field / path | Normalized field | Conversion / date policy | Trusted, inferred, missing or unsupported | Evidence / consequence |
|---|---|---|---|---|
| | | | | |

| ID | Deliverable / task | Owner | Predecessors / relationship / lag | Duration / unit / basis | Baseline start | Baseline finish | Forecast start | Forecast finish | Actual start/finish and evidence | Status / unknowns |
|---|---|---|---|---|---|---|---|---|---|---|

## Chart

Replace the fictional demonstration below with supplied data; do not use these dates as project facts.

```mermaid
gantt
    title Fictional layout demonstration - replace with project evidence
    dateFormat YYYY-MM-DD
    axisFormat %d %b
    todayMarker off
    section Planning scenario - no approval implied
    Example work :example, 2026-10-05, 2d
    Example gate :milestone, gate, after example, 0d
```

## Reading and interaction contract

- Dominant question the default view answers:
- Large-screen grid / timeline / persistent detail behavior:
- Search, filter, grouping, sort, zoom, selection, hierarchy and reset:
- Dependency, comparison, critical-path, non-working-time and label toggles:
- Portrait summary or focused slice; landscape behavior when needed:
- Touch and keyboard paths; hover replacement; focus-return behavior:
- Editing validation, permissions, preview, undo and sync/conflict behavior, or explicitly read-only:

## Dependencies, resource conflicts and missing data

| Task / constraint | Evidence | Effect still to validate | Owner / action | Decision date or unknown |
|---|---|---|---|---|

## Variance and decision

State what moved, compared with which baseline, in working or calendar days, and whether change approval exists.

## Render review

Compare displayed starts/finishes to the source; inspect long labels, weekend events, milestone positions, legend, status claims and baseline/forecast distinction. Keep editable source with any exported visual.

## Visual delivery record

- Decision/audience and reason for this visual rather than a simpler alternative:
- Source file/system, field mapping, snapshot/filter coverage and missing data:
- Artifact mode: static, read-only inspection, or explicitly requested editing:
- Desktop, portrait and landscape reading path; essential values outside hover:
- Controls actually implemented and checked; selection/filter/reset behavior:
- Editable source and generated export paths; full versus current-view scope:
- Render dimensions/tool, source-to-mark checks, defects repaired and remaining limits:
- Performance evidence: tested task/link count, visible rows, date span and interaction result:
- Accessibility checks: semantic table/summary, focus path, non-color cues, reduced motion and screen-reader scope:
- Offline/live state: last updated, stale/partial behavior, reconnect or explicitly static/offline:
