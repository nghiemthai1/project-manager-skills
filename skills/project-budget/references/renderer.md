# Project budget renderer contract

Use `scripts/render_budget.py` for a portable financial-control workspace. Python 3.11+ standard library produces self-contained HTML, static SVG, normalized JSON and spreadsheet-safe CSV.

```sh
python scripts/render_budget.py budget-source.json --output project-budget
python scripts/render_budget.py --demo --output budget-demo
```

## Source and calculations

The snapshot records identity, status date, currency/scale, approved baseline and reserve control, aligned PV/EV/AC with earning evidence, cost categories, an optional selected forecast, funding/scope options, presentation and analysis boundaries. Each category separates actual, committed-but-unspent and other ETC. Use `null` for an unknown remaining amount; do not enter zero.

The renderer calculates CV, SV, CPI, SPI, remaining-at-budget EAC, cost-efficiency EAC and combined-efficiency EAC. Bottom-up EAC equals AC plus known remaining commitments and ETC only when every remaining field is known. It also shows AC less category actuals as a reconciliation difference. Monetary SV is never converted to calendar delay.

The scale is a display contract such as `k`; all numeric amounts must already share it and one currency. The renderer does not convert currency, infer earning, choose management's forecast, release reserve or authorize spending.

## Local editing

The HTML editor changes baseline amounts, PV/EV/AC, selected scenario, earning evidence and cost-category amounts/status/evidence in browser local storage. It validates nonnegative finite values, positive BAC, envelope at least BAC, PV/EV at most BAC, evidence fields and unknown/null consistency. It recalculates supported arithmetic and funding gaps after save.

History retains up to 200 before/after financial drafts. Undo is sequential and source restore is confirmed. Source SVG/JSON/CSV remain byte-equivalent to generated files; draft JSON/CSV and visible-category CSV are separate. Editing does not change source decision options or grant authority, so the page marks those records for revalidation.

## Review gates

Regenerate all formats and compare them with source. Verify category actuals reconcile or display the difference, unknown obligations keep bottom-up EAC unavailable, forecast gaps use the total envelope, and reserve stays outside BAC under the declared convention. In a real browser, test search, scenario filters, all four views, editing validation, persistence, undo, restore, downloads and desktop/portrait/landscape layouts. Print/PDF must retain the cutoff and authority boundary.
