# Release readiness renderer contract

Use `scripts/render_readiness.py` for a portable readiness control room. Python 3.11+ standard library writes self-contained HTML, static SVG, normalized JSON and spreadsheet-safe CSV.

The source fixes the exact release ID/version, environment, population, window, baseline, go authority and actual decision state. Each gate records classification, applicability, result, evidence and date, acceptor state, exception authority, required action, owner, due date and source. Dated events preserve later chronology without backfilling the cutoff snapshot.

The derived recommendation treats every applicable mandatory or exceptionable gate independently. A pass needs accepted or explicitly not-required acceptance; an accepted exception applies only to an exceptionable gate with named authority and evidence. The renderer never turns the result into a percentage or formal authorization.

The browser-local editor validates the gate contract and recalculates blockers. History, undo and source restore retain source integrity. Source SVG/JSON/CSV remain immutable; full and visible draft exports are separate.

Test filters, all four views, keyboard row selection, invalid exception/pass cases, persistence, undo, downloads, SVG bounds, and desktop/portrait/landscape layouts.
