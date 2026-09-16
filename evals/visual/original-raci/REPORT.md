# Independent RACI forward test

Fictional request: H-7 PM R confirmed by M-3, OPS authority unknown; H-8 PM A/R and OPS I confirmed by M-4; H-9 two proposed A and no R. No live writes, network access, publishing or canonical skill changes.

## Result

The renderer generated offline HTML and SVG plus editable JSON and long-form CSV. JSON round-trips every input value. CSV retains all six cell records, IDs, duties, sources and confirmation states. H-7 remains `?` for OPS. H-8 has no audit findings. H-9 is flagged for two A assignments, no R and incomplete confirmation. Source minutes are preserved as requester-cited evidence, not independently verified records. Dates and named role holders remain unknown.

Actual command:

```powershell
.venv/Scripts/python.exe .work/visual-forward-test/forward_test.py
```

The test invokes:

```powershell
.venv/Scripts/python.exe skills/raci-matrix/scripts/render_raci.py .work/visual-forward-test/handoffs-source.json --output .work/visual-forward-test/handoffs
```

Outputs: `handoffs.html`, `handoffs.svg` (780 × 777), `handoffs.json`, `handoffs.csv`, `handoffs-source.json`, `test-results.json` in this folder. The HTML includes a Rows with findings filter, role selector, search, reset and persistent assignment detail. Embedded JSON/SVG downloads match corresponding generated files after newline normalization. A CSV mismatch uncovered the Windows newline defect below. All relative links in the invoked skill and references resolve.

## Adverse cases

Duplicate role ID, missing explicit cell, invalid code, confirmed assignment without evidence and invalid confirmation state each exit 2 before writing artifacts. HTML/XML injection is escaped. A formula-leading role label receives an apostrophe in CSV. An adverse fixture preserves explicit no assignment, unknown and disputed simultaneously. See `adverse.html`, `adverse.svg` and the script.

## Gaps found by reading the generated output and executable code

1. The skill and visual contract do not mention the included `scripts/render_raci.py`, its CLI, schema, example source or output behavior. I had to enumerate package files and inspect the helper and sample JSON to discover the workflow. A direct linked renderer quickstart would make the requested visual reliably reproducible from skill instructions.
2. The visual contract requires row and role summaries, visible versus total columns, and unresolved count above the matrix. The current HTML has only visible row totals and a generic role-hidden warning; there are no role totals/concentration summaries or unresolved count above the matrix. The SVG has a row-findings total below the matrix. This does not prevent this small request but is a capability/contract mismatch.
3. Search promises role search in the visual contract. The HTML search corpus serializes each row, whose cell keys contain role IDs but not the separate role display labels. Searching a role label distinct from its ID cannot match on that label unless it coincidentally occurs in the row. The present test uses PM/OPS for both, so it does not expose that mismatch in the primary artifact.
4. The standalone SVG contains duties, states and a generic pointer to companion source files, but lacks per-cell evidence references and detailed audit findings. Those are preserved in companion HTML/JSON/CSV, so deliver the package together. No claim of standalone SVG evidence completeness is justified.
5. On Windows, the written CSV has `CR CR LF` line endings because `csv.writer` creates CRLF and `Path.write_text` performs newline translation again. The embedded CSV download has correct CRLF. Python DictReader tolerates the file's blank physical rows, so initial semantic checks passed; byte-level export comparison exposed the defect. Write CSV with `newline=''` (or disable translation for all outputs) and test written bytes.

## Inspection limits

This test parses generated SVG XML and checks data/content and JavaScript wiring, but does not execute browser controls, verify keyboard focus or inspect rendered desktop/portrait/landscape layouts. SVG dimensions come from the actual output. Browser/assistive-technology behavior is not claimed tested.
