# Offline renderer contract

`scripts/render_dependency_map.py` is a deterministic reader for small dependency snapshots. It uses Python 3.11+ standard library only and makes no network request.

## Command

```sh
python scripts/render_dependency_map.py INPUT.json --output OUTPUT_STEM
python scripts/render_dependency_map.py --demo --output OUTPUT_STEM
```

It writes:

- `.html`: self-contained interactive graph, DSM, detail panel, local draft editor and register;
- `.svg`: complete static provider-to-receiver snapshot;
- `.json`: normalized source-equivalent data;
- `.csv`: complete spreadsheet-safe dependency register.

The HTML toolbar can export the current full draft as JSON/CSV and a filtered visible-slice draft CSV. Permanent source SVG/JSON/CSV downloads remain complete and immutable.

## Validation behavior

The helper rejects duplicate IDs, missing node endpoints, self-dependencies, invalid states, malformed dates and a committed date without commitment evidence. The browser editor enforces the same rules before saving a local change. Required text cannot be silently absent; use explicit `unknown` wording. It retains nullable dates, original IDs, states, evidence and notes.

The only calculated schedule value is calendar-day local margin when both needed-by and forecast dates exist. The helper does not infer commitments, acceptance, probability, severity, CPM float, a critical path or project delay. An optional critical-path block must be explicitly supplied with a named method and source dependency IDs.

## Layout behavior

The renderer assigns stable left-to-right layers from provider to receiver. Nodes involved in unresolved cycles share a later layer so the cycle stays visible without manufactured precedence. Filtering recomputes the visible graph. The matrix counts visible provider/receiver pairs.

The static SVG and permanent source downloads always contain the complete supplied snapshot. Search, status, party, gaps-only and link-focus controls affect the review surface and visible-slice draft CSV only. Saved draft edits recalculate the graph, matrix, register and display metrics. Cycles remain visible and receive a coordination warning; the editor does not silently delete or reorder an interface.

## Local draft editing

Select **Edit draft**, then select a graph edge or register row. The form can change provider and receiver, status and acceptance, handoff wording, usable criteria, dates, commitment evidence, both owners, evidence/source and notes. Stable IDs and the node inventory remain source controlled.

Draft changes persist in browser local storage for the artifact title, version and as-of date. Every save records a before/after entry; **Undo** reverses the latest save, and **Restore source** clears the full local draft after confirmation. Reloading the file restores valid draft data and history. Invalid or stale stored data is ignored.

Draft JSON records the source version/as-of values, export time, changed dependency count, history and a warning that source analysis must be revalidated after topology or date edits. Draft CSV exports the current rows. These browser-only changes do not write back to the input JSON or permanent files and do not provide shared review, approval or audit retention.

## Safe use and limits

All generated HTML is self-contained. User text is escaped for markup, the embedded JSON is protected from script termination, and CSV formula prefixes are neutralized. Still treat output files as project records and review them before distribution.

The helper is intended for small review artifacts with a browser-local working draft. It does not edit source systems, optimize graph crossings, schedule activities, model resources, preserve governed revision history or provide a multi-user workflow. Use a governed source system or suitable graph/schedule engine when those capabilities are required.

## Verification checklist

1. Compare dependency IDs, provider/receiver direction and dates with the source.
2. Confirm negative margins and unknown dates render literally.
3. Test search, status/party filters, gaps-only, link focus, zoom, graph/DSM switching, keyboard selection, Escape reset, local save validation, reload persistence, undo, source restore, draft exports, visible CSV and print.
4. Inspect desktop, phone portrait and phone landscape sizes.
5. Parse the SVG and JSON and compare generated files byte-for-byte with a fresh renderer run.
