# Milestone schedule renderer contract

Use `scripts/render_milestone.py` for a portable logic and milestone workspace. Python 3.11+ standard library writes self-contained HTML, static SVG, normalized JSON and spreadsheet-safe CSV.

The source records stable task IDs, kind, duration, predecessor IDs, owner/resource, state, exit evidence, authority and source, plus explicit feasibility scenarios. The renderer supports only an acyclic finish-to-start, zero-lag network in one duration unit. It calculates ES/EF, LS/LF, total float, tied zero-float records and modeled finish. It does not apply calendars, fixed dates, other relationship types, lags or resource leveling.

The browser-local editor validates durations, zero-duration milestones, predecessor IDs, self-links, evidence and cycles, then recalculates the network. Source scenarios and comparison claims require revalidation after edits. History, undo and confirmed source restore retain source integrity. Source SVG/JSON/CSV remain immutable; full and visible draft exports are separate.

Test filters, all four views, keyboard selection, invalid milestone/cycle cases, persistence, undo, downloads, SVG bounds, and desktop/portrait/landscape layouts.
