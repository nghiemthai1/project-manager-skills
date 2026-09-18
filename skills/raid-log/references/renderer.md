# RAID log renderer contract

Use `scripts/render_raid_log.py` for a portable RAID control workspace. Python 3.11+ standard library writes self-contained HTML, static SVG, normalized JSON and spreadsheet-safe CSV.

Each record keeps one type, stable ID, evidence, owner state, action, closure test, transition rule and explicit links. Type details remain distinct: risks retain cause-event-effect and response fields; assumptions retain premise, boundary, validation and expiry; issues retain observed condition, consequence, resolution and escalation; dependencies retain provider, receiver, usable condition, needed/committed/forecast/actual dates and receiver acceptance.

The transition graph links records without renaming them. An optional ordinal risk score is available only when an agreed scale and actual ratings are supplied. Current issues, mandatory conditions, invalid assumptions, materialized risks, late dependencies and unconfirmed ownership can require attention without a fabricated score.

The browser-local editor validates type-specific states, dates, links, ratings and acceptance authority, then recalculates attention, unknown and overdue flags. History, undo and source restore retain source integrity. Source SVG/JSON/CSV remain immutable; full and visible draft exports are separate.

Test filters, all five views, graph selection, keyboard row/card/node selection, invalid type-specific cases, persistence, undo, downloads, SVG bounds, and desktop/portrait/landscape layouts.
