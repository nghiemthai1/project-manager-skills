---
name: gantt-chart
argument-hint: '[schedule data, source export, timeline request, or Gantt design problem]'
description: Design, critique, map and deliver Gantt charts from schedules, trackers, roadmaps or exports. Use for task spans, milestones, dependencies, baselines, critical paths or resource timelines.
intent: Choose and produce an evidence-preserving schedule visualization with explicit source mapping, calendar semantics, responsive interaction, accessibility, scale limits and inspected exports.
type: component
theme: scope-and-planning
best_for:
  - Turn evidenced schedule data into a readable, responsive timeline without inventing dates, progress or authority.
  - Design or critique a Gantt product surface, source adapter, interaction model or export workflow.
scenarios:
  - Turn a dated task table into an interactive baseline-versus-forecast Gantt with dependencies and accessible exports.
  - Map a Project, Primavera, Jira, GitHub Projects, Smartsheet, monday.com, Asana, ClickUp or Azure DevOps export into a trustworthy timeline.
estimated_time: Depends on evidence, source complexity and artifact scope
frameworks: Gantt timeline; source normalization and provenance; working calendars; dependency and baseline comparison; responsive interaction
domain: software-it-project-management
version: 2.3.0
license: MIT
---
# Gantt Chart

## Purpose

Design, critique, map and deliver Gantt charts when the schedule itself is the evidence. A useful Gantt combines a stable task grid, calendar axis, bars, milestones, dependencies, comparison layers and an explicit reading path. It may be a small offline report, an exploratory view or an editable scheduling product; those modes have different data, interaction and validation requirements.

First decide whether Gantt is the right surface. Use it when time spans, sequence, dependency, resource or baseline reasoning drives the decision. Use Kanban for flow state and WIP, a table for exact lookup, a milestone timeline for a few executive dates, a dependency graph when dates are unreliable, a calendar for booking without project logic, or an uncertainty view when ranges and scenarios matter more than one date.

A Gantt displays a schedule; drawing bars does not make that schedule feasible. Critical path needs a complete network and calendar assumptions. Resource feasibility needs assignments, capacity and timing. An attractive forecast is not an approved baseline, and a milestone diamond is not acceptance evidence.

## Input

Bring the scheduling question and intended audience, then the best available source: a true schedule engine, task tracker, roadmap snapshot, resource calendar, static table/export or visual artifact. Include task IDs and hierarchy, start/finish or duration, dependency types and lag, calendar/holiday rules, owner or resource, status/progress meaning, baseline version, forecast as-of date, actual evidence, constraints and source links where available.

For external data, identify the system, export format and date, visible filters, timezone/locale, permission scope and whether the extract is complete. Discover native and custom fields before mapping them. Preserve source IDs, field names and ambiguous values rather than silently turning a custom “Target end” field into schedule truth.

Use supplied context without re-asking. Partial data supports a partial artifact with diagnostics. Missing dates remain unscheduled; missing percent complete remains unknown. If no schedule data is supplied, ask which schedule or source should be visualized and offer the [source and review template](template.md). If a demonstration is requested, use clearly labeled fictional values.

## Key Concepts

### Classify the question and source before drawing

Identify whether the user needs a planned schedule, actual lifecycle history, roadmap, resource plan, capacity view, baseline-variance review, critical-path review or stakeholder snapshot. Then classify the source. A Project/P6 export can contain schedule semantics; a Jira or spreadsheet view may be a filtered task snapshot; a PDF or screenshot is visual evidence rather than reliable structured data.

Do not infer a planned span from issue-created and issue-closed dates unless the user asks for actual lifecycle analysis. Do not treat an exported row number as stable identity or assume a filtered export includes hidden predecessors and children. Read [API and export ingestion](references/gantt-api-and-export-format-ingestion.md) before mapping vendor data or static exports.

### Normalize schedule meaning and provenance

Separate source adaptation from rendering. Normalize tasks, hierarchy/WBS, date layers, resources, calendars, dependencies, constraints, progress, source IDs and diagnostics. Keep field-level provenance and mark every inference. A renderer should not need to know Jira field IDs or Project XML paths; a source adapter should not decide visual layout.

Use [the normalized data contract](references/gantt-data-contracts-and-integrations.md) for reusable components, adapters, APIs, fixtures or synchronization. For the included offline helper, follow its narrower [renderer contract](references/renderer.md). It preserves supplied dates and relationships but does not schedule, level resources or compute critical path.

### Chart, network, calendar and resources answer different questions

The chart shows time position and overlap. The network explains what must precede what. The calendar translates duration units into dates. Resource analysis tests whether apparently parallel work can overlap. Reconcile all four before claiming feasibility.

Store date-only values as dates, not UTC instants. State the finish convention. Under `[start, finish)`, a Monday-start two-working-day task finishes at Wednesday’s boundary. A milestone is a zero-duration event at a stated boundary; preparation, review and acceptance effort remain separate work.

Keep baseline, forecast and actual distinct:

| Layer | Meaning | Update rule |
|---|---|---|
| Baseline | Authorized comparison point with an approval/version | Change only through actual baseline authority; preserve prior versions |
| Forecast | Current expectation from remaining work and constraints | Refresh at an explicit as-of date and explain movement |
| Actual | Observed execution event with applicable evidence | Record the event; do not infer it from elapsed time or a plan |

When approval is absent, label the layer target or planning scenario. Use completed/active status and progress only when the source defines and supports them. Critical styling must come from the modeled network and assumptions, not from business importance or manual color.

### A Gantt is a responsive product surface

The default large-screen view normally uses a frozen task grid and horizontally scrollable timeline with stable row alignment. Show the scale, today or as-of marker when meaningful, non-working time, bars, milestones, direct labels and restrained dependency lines. Choose one dominant reading question: what is planned, what moved, what blocks, who is overloaded, or what differs from baseline.

Mobile portrait needs a usable summary or focused slice rather than a miniature desktop chart. Prefer task/phase cards with compact bars, exact dates and persistent selection. Add landscape support when horizontal dependency inspection or editing matters. Keep the visualization visible while search, filters or settings are used; provide touch and keyboard paths and replace hover with tap, focus, selection or always-visible facts. Read [mobile-first responsive visualization](references/mobile-first-responsive-visualization.md) for the full contract.

### Match the renderer to scale and editability

| Need | Suitable approach |
|---|---|
| Small review artifact with optional browser-local task edits | Semantic HTML task grid plus SVG, immutable source exports and validated local draft history |
| Lightweight reporting | Highcharts Gantt, Frappe Gantt, Plotly timelines, Observable Plot or comparable read-only tooling |
| Resource booking | FullCalendar resource timeline or another scheduler where resources and slots dominate |
| Enterprise editable schedule | Bryntum, DHTMLX, Kendo UI, Syncfusion or a comparable scheduling component with calendars, validation, undo and import/export |
| Large dense product surface | Virtualized HTML grid with Canvas/SVG layers; Canvas for dense bars/links when DOM cost dominates |

Avoid raw WebGL unless density, continuous pan/zoom or GPU picking makes Canvas and DOM impractical. Read [performance and rendering](references/gantt-performance-and-rendering.md) before promising behavior for hundreds or thousands of rows.

## Application

1. **Classify the decision and mode.** State the question, audience and whether the result is a static explanation, read-only explorer or editable planner. Confirm that Gantt is primary; name the better surface when it is not.
2. **Inspect and map the source.** Inventory fields, IDs, filters, calendars, hierarchy, relationship semantics, date types and authority. Build a source-field → normalized-field → conversion → evidence/uncertainty map. Keep missing and ambiguous fields visible.
3. **Validate and normalize.** Check duplicate IDs, invalid or partial intervals, unknown predecessors, hierarchy/dependency cycles, milestone meaning, timezone/date boundaries and source coverage. Retain unscheduled tasks and unsupported typed links as diagnostics rather than dropping them. Reconcile date layers without rewriting history.
4. **Test schedule claims.** Check successor timing against dependency type, lag and calendar. Recompute the network after material change when a suitable engine exists. Check scarce-resource overlaps using actual demand and availability. State which claims remain unavailable.
5. **Choose the reading path.** Use a detailed task-grid timeline for executable work, a workstream/milestone summary for executives, a resource timeline for allocation or another surface when clearer. Keep the complete normalized data even when the visible view is a summary. Read [design and use cases](references/gantt-chart-design-and-use-cases.md).
6. **Define interaction before implementation.** Specify search, filtering, grouping, sorting, zoom/pan, hierarchy, task selection, dependency highlighting, comparison/critical-path toggles, reset, export and deep links. For editing, also define drag/resize validation, cycle prevention, downstream-change preview, permissions, undo, stale versions and sync failure. Read [interaction patterns](references/gantt-interaction-patterns.md).
7. **Design large-screen and mobile states.** Preserve the same claim, source context and caveats while reducing density through prioritization and disclosure. Keep exact values outside hover, controls keyboard reachable and touch targets usable. Define what remains visible while the mobile keyboard or settings panel is open.
8. **Generate the artifact and exports.** For a rich small schedule, prefer self-contained semantic HTML plus SVG, a persistent details view and editable normalized JSON. Use the [included renderer](references/renderer.md) when its date-only, browser-local draft contract fits. It validates task fields and date layers, previews conflicts, persists undoable local history and separates source from draft exports without scheduling successors or writing back. Mermaid is suitable for a compact embedded diagram, not a scheduling engine. Define whether each export is source, current full draft, selected range or visible slice.
9. **Inspect behavior and output.** Compare every visible start, finish, milestone, label and relationship with normalized data. Test desktop, portrait and landscape; search/reset; keyboard selection; comparison/dependency toggles; empty, partial and error states; date-only timezone edges; long labels; static exports and active filter disclosure. Read [accessibility, export and testing](references/gantt-accessibility-export-and-testing.md).
10. **Explain the decision.** State what changed, compared with which layer, in the correct units; identify driving work, uncertainty, resource/calendar assumptions and the decision required. Record generated files, tested viewports and known limits. Preparing or changing a chart does not authorize a baseline, source write or external notification.

### Deliverable contract

Deliver the source mapping, normalized editable data, diagnostics, accessible task table, graphical view and short visual-review record together. Include:

- whether Gantt is the primary recommendation and why;
- source classification, snapshot/filter coverage, trusted/mapped/inferred/missing fields and date policy;
- canonical task, dependency, calendar, resource and comparison-layer model;
- implemented interactions, renderer/stack choice and measured scale assumptions;
- desktop, portrait and relevant landscape behavior, including keyboard/touch alternatives;
- export scope and actual generated formats; and
- unsupported scheduling, governed multi-user editing, synchronization or performance claims.

## Examples

Optional worked applications:

- [Software timeline](examples/software.md): original and forecast layers, a two-working-day finish change, an explicit critical path, a phase-grouped interactive review surface and the arithmetic behind it.
- [Migration timeline](examples/migration.md): two tied branches, an acceptance checkpoint and the difference between unconstrained and resource-feasible work.

These fictional subcases add calendar assumptions for teaching. Their HTML artifacts support validated browser-local task editing, conflict diagnostics, history, undo, source restore and separate source/draft exports. They do not replace Relay’s or Northstar’s approved project dates.

## Common Pitfalls

- **Decorative dates:** bars are stretched to meet the desired finish. Retain the evidence-based forecast and show the gap to target.
- **Tracker history becomes a plan:** created/closed timestamps are mapped as scheduled dates. Classify them as lifecycle history or obtain planned fields.
- **Baseline overwritten:** a current forecast replaces the authorized comparison. Preserve both layers and the baseline decision reference.
- **Critical means important:** manually red work is presented as CPM output. Calculate from the complete model or label the color’s actual meaning.
- **Filtered source looks complete:** hidden predecessors, children or custom fields disappear. Show source coverage and missing-context diagnostics.
- **Weekend or timezone shift:** date-only milestones move during timestamp conversion. Preserve date-only values and the display calendar.
- **Parallel bars imply capacity:** the same specialist is booked twice. Test demand, skill and timing or label the view unconstrained.
- **Hover-only truth:** dates, blockers and warnings disappear for keyboard, touch and static exports. Keep essential facts in text and persistent details.
- **Desktop squeezed onto mobile:** labels and touch targets become unusable. Provide a focused mobile state with the same claim and caveats.
- **Editing without a schedule contract:** drag handles appear before permissions, calendars, validation, undo or sync behavior exist. Keep the view read-only until those rules are defined.
- **Demo proves scale:** five tasks are used to promise 10,000-row performance. Measure realistic rows, links, instances and interactions first.
- **Pretty chart without source:** the schedule cannot be reproduced or challenged. Deliver normalized data, mapping, diagnostics and exports with the visual.

## References

- [Gantt chart design and use cases](references/gantt-chart-design-and-use-cases.md): fit, reading tasks, encoding and alternatives.
- [Gantt interaction patterns](references/gantt-interaction-patterns.md): navigation, inspection, editing and conflict behavior.
- [API and export ingestion](references/gantt-api-and-export-format-ingestion.md): Project, Primavera, Jira, GitHub Projects, Smartsheet, monday.com, Asana, ClickUp, Azure DevOps and common file formats.
- [Data contracts and integrations](references/gantt-data-contracts-and-integrations.md): normalized schema, adapters, scheduling engines, view state and sync boundaries.
- [Performance and rendering](references/gantt-performance-and-rendering.md): SVG/Canvas/hybrid choices, virtualization, culling and scale limits.
- [Accessibility, export and testing](references/gantt-accessibility-export-and-testing.md): keyboard, screen-reader fallbacks, fixtures and release gates.
- [Mobile-first responsive visualization](references/mobile-first-responsive-visualization.md): portrait/landscape layouts, touch, keyboard, offline and constrained-device behavior.
- [Offline renderer](references/renderer.md): package-local JSON contract and verified HTML/SVG/JSON/CSV output.
- [Milestone Schedule](../milestone-schedule/SKILL.md), [Resource Capacity Plan](../resource-capacity-plan/SKILL.md) and [Change Request](../change-request/SKILL.md): optional network, resource and authority handoffs.

Adjacent skills are optional. When unavailable, preserve the schedule model, evidence boundaries and decision explanation described here.
