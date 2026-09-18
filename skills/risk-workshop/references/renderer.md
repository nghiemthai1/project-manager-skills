# Risk workshop renderer contract

Use `scripts/render_risk_workshop.py` for a portable risk-control workspace. Python 3.11+ standard library writes self-contained HTML, static SVG, normalized JSON and spreadsheet-safe CSV.

Each record preserves cause, uncertain event, objective effect, evidence confidence, existing control, response mechanism, proposed or confirmed owner, trigger, contingency, residual assessment and authority. An optional probability-impact grid is available only when an agreed ordinal scale and actual ratings are supplied; otherwise risks remain in an explicit unknown lane.

The renderer uses a declared ordinal threshold only for screening. Mandatory conditions remain priority without invented likelihood. Scores are not probability, money or expected loss, and a transferred obligation does not remove residual business exposure.

The browser-local editor validates the scale and acceptance rules and recalculates priority. History, undo and source restore retain source integrity. Source SVG/JSON/CSV remain immutable; full and visible draft exports are separate.

Test filters, all four views, keyboard selection, invalid acceptance/rating cases, persistence, undo, downloads, SVG bounds, and desktop/portrait/landscape layouts.
