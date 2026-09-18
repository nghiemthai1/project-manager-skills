# Scope and WBS renderer contract

Use `scripts/render_scope_wbs.py` for a portable scope-control workspace. Python 3.11+ standard library writes self-contained HTML, static SVG, normalized JSON and spreadsheet-safe CSV.

Each package keeps a stable ID, parent, kind, scope state, maturity, observable output, boundary, completion evidence, acceptor, owner state, estimate basis, confidence, source references, requirement links and interfaces. Multiple top-level deliverables are allowed; every non-top-level parent must exist and cycles are rejected.

Requirement coverage is explicit rather than inferred from labels. Active requirements need one primary package boundary; support links can contribute without duplicating ownership. Coverage gaps, multiple primaries, partial packages, unconfirmed owners, untraced packages and proposed changes stay visible. The 100% rule tests the declared boundary and never claims uncertainty vanished.

The browser-local editor validates parent changes and traceability, updates the coverage links, and recalculates all audits. History, undo and source restore retain source integrity. Source SVG/JSON/CSV remain immutable; full and visible draft exports are separate.

Test filters, all five views, hierarchy selection, keyboard row/card/node selection, cycle and unknown-requirement errors, persistence, undo, downloads, SVG bounds, and desktop/portrait/landscape layouts.
