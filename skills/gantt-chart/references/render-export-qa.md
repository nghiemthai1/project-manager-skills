# Rendering, export and visual acceptance

## Renderer choice

For a small read-only artifact, semantic HTML plus SVG keeps labels inspectable and produces vector exports. Mermaid is useful for a compact embedded diagram, but its layout and renderer-specific syntax may limit frozen grids, detailed layers and interaction. A spreadsheet is appropriate when the audience needs to edit exact cells and already works there.

For thousands of tasks, start with a phase summary or filtered slice and preserve the complete data. A product-scale view may need row virtualization, a shared scroll model and Canvas for dense marks; editing additionally needs scheduling rules. Do not claim performance for 10,000 rows because a five-row example worked. Record tested rows, links, date span, viewport, runtime and observed behavior. Check current tool capabilities before choosing a library.

## Export package

Include title, source/snapshot, as-of, date convention/timezone, visible scope, chosen layers, legend and caveats in every shareable view. Export actual values and IDs, not only drawn geometry. Default deliverables are editable source data plus a rendered SVG and a semantic table; add a self-contained HTML inspection view when it helps the user. PNG/PDF are optional audience-specific exports. Do not claim an export exists until it has been generated and inspected.

Full schedules may require pages split by row and time range. Repeat headers and identifiers across pages. A screenshot of the viewport is not a full-project export. Remove inactive controls from print while preserving active filters and the “visible / total” distinction. Wait for fonts/layout before capture.

## Accessibility

Use meaningful document headings, native controls, labels and table headers. Keep dates/owners/warnings in text outside hover. Make task selection and details available through keyboard; retain visible focus. Use redundant labels/shapes for status and criticality and a useful textual summary. Reduced-motion preference should suppress nonessential animations; an offline report usually needs none.

Use readable text and adequately separated touch targets at the actual target viewport. Test high zoom and narrow layouts. A screenshot inspection alone does not establish screen-reader compatibility; inspect semantic structure and describe the checks actually performed.

## Adverse fixtures and review

| Fixture | What must remain true |
|---|---|
| Missing dates / empty source | No invented bars, zero-completion claims or fake project range; explicit empty/unscheduled state |
| Long names / many rows | IDs remain exact; labels stay legible; scope limits/summary/pagination explicit |
| Weekend milestone / holiday / leap date | Event remains at its evidenced boundary; excluded periods do not silently move it |
| Date-only export in another timezone | Same written date; no UTC conversion shift |
| Baseline and forecast differ | Both retained and correctly labeled; comparison remains visible in export |
| Duplicate ID / cycle / missing predecessor | Diagnostic identifies source IDs; no silent dropping or false feasible-plan claim |
| FS, SS, FF, SF and lag | Typed relationship preserved; unsupported calculation not flattened to FS |
| Same scarce resource on parallel work | Known demand conflict visible; coloring alone does not fix it |
| Filter / selected chain | Visible counts, hidden context and reset work; export scope accurate |
| Keyboard / portrait / landscape | Selection, exact facts and reset usable without hover or tiny labels |
| Special characters in IDs/labels | HTML/SVG escaped; text cannot become executable markup; CSV/JSON retains literals |

Before delivery, compare every bar endpoint, milestone and comparison against normalized source data. Inspect desktop, portrait and landscape renders, not just parser success. Record defects and repair them, then recapture affected views. State which interactions, export formats and scale were actually tested.
