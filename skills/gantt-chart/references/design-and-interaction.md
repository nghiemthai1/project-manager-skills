# Gantt reading and interaction design

Choose the decision before choosing the renderer. The default view should answer one question: what changed, what governs finish, what happens next, or where assignments conflict.

## Choose the surface

| Decision | Best starting view | Limitation |
|---|---|---|
| Compare spans and dated handoffs | Task grid plus Gantt timeline | Needs trustworthy dates/calendars |
| Explain a few executive commitments | Milestone/phase timeline | Hides work detail; retain source table |
| Trace blockers with unreliable dates | Dependency graph and edge register | Cannot imply a finish forecast |
| Assign owners or inspect exact fields | Table or RACI | Does not establish date feasibility |
| Explain workload by time | Capacity/resource timeline | Needs effort and availability, not just task counts |
| Compare uncertain dates | Interval/scenario view | Label assumptions; no invented confidence level |
| Discuss workflow states | Kanban or flow view | Created/closed history is not a future schedule |

## Default desktop composition

Pair a stable task grid with a calendar axis. Keep names/IDs, owners, dates and warnings readable without hover. Freeze the identifying column when horizontal scrolling is needed; keep row heights and grid/bar alignment stable. Group by the actual phase/WBS and make rollup meaning explicit.

Use filled bars for the current chosen layer, thin outlined bars for an evidenced comparison, diamonds for milestones and text/badges for unknowns or constraints. A planning scenario must not acquire an “approved baseline” label through styling. Non-working shading supplies context, not effort. Show the as-of marker when it helps; label an as-of marker separately from real today. Do not draw an automatic today line on an old snapshot as if its data were current.

Colors encode one defined meaning at a time. Pair criticality, failed gates and late finishes with words, line styles or shapes. Use direct labels outside short bars. Keep full source labels in the table/details when the graphic abbreviates them.

## Read-only interaction contract

- **Search/filter:** match literal ID, label or owner; show active filters and visible/total counts. Reset restores the unfiltered scope. Hidden predecessors remain disclosed.
- **Scale/range:** provide explicit day/week/month or fit controls appropriate to the data; preserve selection. Do not capture browser wheel scrolling unexpectedly.
- **Selection:** click or keyboard opens persistent details, exact date layers, evidence and predecessor/successor list. Hover is optional preview only.
- **Hierarchy:** collapse children without changing dates or implying completed work. Explain whether the parent is a computed rollup or manually supplied row.
- **Dependencies:** use restrained lines, selected chains or a relationship detail view. Avoid a wall of overlapping arrows. Preserve relationship type and lag in readable form.
- **Comparison:** baseline/scenario visibility can be toggled without mutating either layer. The export caption states the chosen layers.
- **Export:** offer a complete source-data export and clearly scoped current-view/full-view graphics. A filter must not silently become the complete project.

Only implement controls that work. If an artifact is static, say so and supply its data/table; do not draw fake search, zoom or export buttons. A standalone HTML file can provide inspection without a server or live integration.

## Portrait and landscape

At a phone-width viewport, lead with the decision summary and key dates, then a focused timeline or task cards with exact dates. Put secondary controls in a collapsible area. Do not scale a wide SVG until its text is unreadable. Offer horizontal inspection as an explicit option while preserving a useful narrow default.

For landscape, preserve the identifying column and a wider time window. Controls must remain reachable with touch and keyboard. Closing filters/details should return focus to the selected task or relevant control. A search keyboard must not permanently cover the only reset/close action.

## Editing is a separate mode

Do not add drag handles to a read-only report. When the user requests an editable planner, define whether an edit is local, a scenario or a source-system change. Date fields must provide an alternative to dragging. Validate calendars, typed links, locks and downstream impacts before commit; show a preview, undo/discard and source-version conflict handling. Parent rollups should not masquerade as directly editable tasks. No source write should occur on every pointer movement.

This library's artifact examples need no live writeback. Use a scheduling component/service when actual editing semantics exceed a small report renderer; visual polish cannot replace a schedule engine.
