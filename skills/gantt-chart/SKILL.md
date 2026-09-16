---
name: gantt-chart
argument-hint: '[schedule data or timeline request]'
description: Design and deliver Gantt artifacts with source mapping, readable interaction and exports. Use when
  schedules need timelines, baseline comparisons or visual review.
intent: Choose and produce an evidence-preserving schedule visualization with explicit data mapping, calendar semantics,
  interaction, accessibility and inspected exports.
type: component
theme: scope-and-planning
best_for:
  - Turn evidenced schedule data into a readable timeline without inventing dates or completion.
scenarios:
  - 'Use gantt-chart: Turn evidenced schedule data into a readable timeline without inventing dates or completion.'
estimated_time: Depends on evidence and project scope
frameworks: Gantt timeline; working calendars; finish-to-start dependencies; baseline comparison
domain: software-it-project-management
version: 2.1.0
license: MIT
---
# Gantt Chart

## Purpose

Make the schedule visible: when work is expected, which handoffs determine starts, where gates fall, and how a forecast differs from an approved baseline. Produce a chart plus the underlying task table and assumptions. Use for a sponsor discussion, team planning, release coordination or a change-impact comparison.

A Gantt chart displays a schedule; drawing bars does not make the schedule feasible. Use Milestone Schedule to establish network logic and critical-path calculations, then use this skill to communicate the result. For unordered ideas or dates without duration evidence, create an explicitly provisional milestone view or missing-input table first.

## Input

Bring task IDs and labels, start/finish dates or durations, predecessor IDs, calendar/holiday rules, owner or role, baseline version, forecast date and any actual-progress evidence. A task export or rough table is enough to begin; unresolved values remain unresolved.

Example: “Show this release plan as a Gantt chart. Keep the approved baseline visible and highlight how the vendor delay changes the forecast.”

Use inline context without re-asking. With no data, ask which schedule to visualize and offer a fillable task table. If a demonstration is requested, use clearly labeled fictional values. Do not silently create a project start date, holiday calendar, actual completion or approval.

## Key Concepts

### Chart, network and calendar answer different questions

The chart shows time position and overlap. The dependency network explains what must precede what. The calendar translates duration units into dates. Resource planning establishes whether apparently parallel work can actually overlap. None can safely be inferred solely from the appearance of the other.

For a finish-to-start link, a successor starts no earlier than all required predecessors finish, subject to calendar and constraints. Where lead/lag or another relationship applies, use a scheduling tool that models it and document the relationship; do not replace it with a convenient arbitrary date.

### Three date layers

| Layer | Meaning | Update rule |
|---|---|---|
| Baseline | Authorized comparison point, linked to its approval/version | Change only when the relevant baseline change is approved; preserve prior versions |
| Forecast | Current expected start/finish based on remaining work and constraints | Refresh at an explicit as-of date; show why it changed |
| Actual | Observed start/finish supported by execution evidence | Record the event; do not infer from elapsed time or a plan |

When approval is absent, call the row a target or planning scenario. “Baseline” is not a styling choice. Draw baseline and forecast on separate labeled rows or layers. A completed work bar can still finish later than baseline; visual completion does not mean on time.

### Dates and boundaries

State working days, workweek, holidays and date-boundary convention. With a half-open date convention, a bar covers the half-open interval from its start through the time before its finish boundary. A Monday-start, two-working-day activity ends at Wednesday's start boundary. A milestone is a zero-duration event at a stated boundary, not an extra day of work.

Do not apply a weekday calendar to an explicitly scheduled weekend cutover. Use separate sections or a tool with the correct calendar for each activity. Hours, shifts, time zones, part-time assignments and intra-day handoffs need explicit treatment when they affect the decision.

### Status and criticality need evidence

Use completed or active status only with actual evidence. Missing percent-complete data is unknown, not zero. Percentage of time elapsed is not percentage of work earned. Critical coloring must come from the modeled schedule and its assumptions; an important executive task is not necessarily mathematically critical. Show more than one critical path when the network has ties.

## Application

1. **Validate the source table.** Retain stable task IDs, distinguish date layers, and check missing dates, inverted intervals, duplicate IDs and unknown predecessors. Ask for information that changes the chart; do not fill gaps with realistic-looking dates.
2. **Reconcile logic and calendars.** Check dependency cycles, successor timing, holidays, imposed dates and scarce-resource overlaps. Recompute the network after a material change. Label unresolved resource/calendar assumptions on the chart.
3. **Select the right view.** Use a detailed team timeline for executable work or a milestone/workstream summary for executives. Keep the full task table as the source. A simpler view can omit low-level rows without changing dates or hiding a failed gate.
4. **Generate the appropriate artifact.** For a reusable inspection view, prefer self-contained semantic HTML with SVG, persistent details and meaningful controls. For a small embedded diagram, Mermaid remains useful. Deliver editable source data and a rendered SVG/table; add other formats for the audience. Follow the design/export references below, preserve comparison labels and state as-of and visible scope.
5. **Check the rendered chart.** Inspect label clipping, date ticks, weekend handling, zero-duration milestones, predecessor joins, color meaning and baseline alignment. Compare every displayed start/finish against the source table. A diagram that parses can still tell the wrong schedule story.
6. **Explain the decision.** State changed work, finish variance in the right units, assumptions and the decision required. An updated forecast is not permission to defer a commitment. Save the source/version so a later chart can be compared without rewriting history.

Use [the task and chart template](template.md).

### Visual artifact workflow

Before rendering, read [source mapping and model](references/source-and-model.md); for vendor files or screenshots also read [import routing](references/import-routing.md). Identify planned schedule, actual history, roadmap, resource calendar or visual reconstruction before mapping dates. Keep missing tasks and relationships visible as diagnostics.

Use [design and interaction](references/design-and-interaction.md) to choose a task-grid timeline, executive milestone view, dependency graph or another clearer surface. Define read-only versus editing mode, selection, search/filter/reset, hierarchy, comparison layers and export scope before implementing controls. Preserve exact values outside hover and provide a readable portrait view as well as landscape/desktop inspection.

Use [rendering, export and QA](references/render-export-qa.md) to choose a renderer against actual rows/links and to inspect generated files. A default report needs no hosted app or live integration. Large editable schedules need a scheduling engine and measured interaction behavior, not merely more SVG bars. Deliver only the export formats actually generated and verified.

The final package includes the source mapping, normalized editable data, diagnostics, accessible table, graphical output and a short visual review record. If rendering is unavailable, provide source plus an explicitly unrendered draft; do not claim visual QA or a completed graphic.

### Mermaid conventions used here

Give tasks stable IDs. Use explicit ISO start dates or `after` references to predecessor IDs. Declare the working-calendar exclusions. Use zero-duration milestone entries. Mermaid can render the diagram, but this library does not treat it as a resource-leveling or approval engine. Check the [current syntax documentation](https://mermaid.js.org/syntax/gantt.html) for features supported by the renderer you use.

### Included offline renderer

Use [the renderer contract](references/renderer.md) when producing a standalone artifact from normalized JSON. The included [Python helper](scripts/render_gantt.py) writes self-contained HTML, a full SVG, source JSON and CSV with Python 3.11+ and no external packages. Map the supplied project data to the input contract, then inspect the actual outputs. Its supported scope is deliberately smaller than a full editing or scheduling application.

## Examples

Optional worked applications:

- [Software timeline](examples/software.md): four tasks, separate original and forecast rows, a two-working-day finish change, and the date arithmetic behind it.
- [Migration timeline](examples/migration.md): two tied branches, an acceptance checkpoint and the difference between unconstrained and resource-feasible work.

These are instructional subcases with additional fictional calendar assumptions. They do not replace Relay's or Northstar's approved project dates.

## Common Pitfalls

- **Decorative dates:** bars are stretched to fit the desired finish without changing estimates. The diagram conceals an infeasible plan. Retain the real forecast and show the gap to target.
- **Weekend cutover disappears:** global weekday exclusions move an approved Saturday event. Model its actual calendar or show it separately; check the rendered date.
- **One day added at every milestone:** acceptance events are drawn as tasks by habit. Use zero duration for the event; model the review preparation and reviewer effort separately.
- **Critical means important:** a manually red bar is presented as CPM output. Name the actual prioritization meaning or calculate criticality from the full network.
- **Baseline overwritten:** a new forecast replaces the old bar and the project appears on time. Keep comparison rows and the original approval reference.
- **Parallel bars imply spare people:** B and C share one specialist but overlap. Resolve the assignment or label the chart an unconstrained scenario; a warning without a decision is not a feasible baseline.
- **Pretty chart without source:** dates cannot be traced or reproduced. Deliver the task table, calendar assumptions, version and editable chart source together.

## References

- [Milestone Schedule](../milestone-schedule/SKILL.md): calculate and interpret schedule logic.
- [Resource Capacity Plan](../resource-capacity-plan/SKILL.md): test assignments and resource constraints.
- [Change Request](../change-request/SKILL.md): authorize changes to approved commitments.
- [Mermaid Gantt documentation](https://mermaid.js.org/syntax/gantt.html): renderer syntax and calendar behavior.

Other skills are optional handoffs. Keep the source table and assumptions usable when a rendering tool is unavailable.
