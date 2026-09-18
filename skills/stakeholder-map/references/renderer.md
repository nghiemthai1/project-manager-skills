# Stakeholder-map renderer contract

Use `scripts/render_stakeholder_map.py` for a portable stakeholder-analysis workspace. Python 3.11+ standard library writes self-contained HTML, static SVG, normalized JSON and spreadsheet-safe CSV. The renderer code carries the repository's MIT code license; the adapted skill content retains its CC BY-NC-SA 4.0 license and attribution terms in the package root.

Each stakeholder keeps qualitative power, interest and impact categories, confidence, evidence, power domain, representation, authority, engagement ownership and a migration action. Unknown categories remain outside the relevant grid. Categories are hypotheses, not measured coordinates, and the renderer never ranks people within a quadrant.

Power x Interest derives engagement strategy; Impact x Power identifies Q1 high-impact/low-power voices. The comparison view surfaces Q1 stakeholders outside manage-closely, incomplete placement, unconfirmed representation and domain-specific authority. Participation can increase evidence contribution without silently granting formal approval power.

The browser-local editor validates dates and confirmed-representation evidence, then recalculates both grids and findings. History, undo and source restore retain source integrity. Source SVG/JSON/CSV remain immutable; full and visible draft exports are separate.

Test filters, all five views, grid and row keyboard selection, invalid representation confirmation, persistence, undo, downloads, SVG bounds, and desktop/portrait/landscape layouts.
