# Offline renderer contract

`scripts/render_dependency_map.py` is a deterministic reader for small dependency snapshots. It uses Python 3.11+ standard library only and makes no network request.

## Command

```sh
python scripts/render_dependency_map.py INPUT.json --output OUTPUT_STEM
python scripts/render_dependency_map.py --demo --output OUTPUT_STEM
```

It writes:

- `.html`: self-contained interactive graph, DSM, detail panel and register;
- `.svg`: complete static provider-to-receiver snapshot;
- `.json`: normalized source-equivalent data;
- `.csv`: complete spreadsheet-safe dependency register.

The HTML toolbar can export a visible-slice CSV. That action is filtered; the permanent CSV remains complete.

## Validation behavior

The helper rejects duplicate IDs, missing node endpoints, self-dependencies, invalid states, malformed dates and a committed date without commitment evidence. Required text cannot be silently absent; use explicit `unknown` wording. It retains nullable dates, original IDs, states, evidence and notes.

The only calculated schedule value is calendar-day local margin when both needed-by and forecast dates exist. The helper does not infer commitments, acceptance, probability, severity, CPM float, a critical path or project delay. An optional critical-path block must be explicitly supplied with a named method and source dependency IDs.

## Layout behavior

The renderer assigns stable left-to-right layers from provider to receiver. Nodes involved in unresolved cycles share a later layer so the cycle stays visible without manufactured precedence. Filtering recomputes the visible graph. The matrix counts visible provider/receiver pairs.

The static SVG and permanent downloads always contain the complete supplied snapshot. The HTML's search, status, party, gaps-only and link-focus controls affect the review surface and visible-slice CSV only.

## Safe use and limits

All generated HTML is self-contained. User text is escaped for markup, the embedded JSON is protected from script termination, and CSV formula prefixes are neutralized. Still treat output files as project records and review them before distribution.

The helper is intended for small read-only review artifacts. It does not edit source systems, optimize graph crossings, schedule activities, model resources, preserve revision history by itself or provide a multi-user workflow. Use a governed source system or suitable graph/schedule engine when those capabilities are required.

## Verification checklist

1. Compare dependency IDs, provider/receiver direction and dates with the source.
2. Confirm negative margins and unknown dates render literally.
3. Test search, status/party filters, gaps-only, link focus, zoom, graph/DSM switching, keyboard selection, Escape reset, visible CSV and print.
4. Inspect desktop, phone portrait and phone landscape sizes.
5. Parse the SVG and JSON and compare generated files byte-for-byte with a fresh renderer run.
