# RACI as a usable visual matrix

A colored Markdown table is only one presentation. A useful artifact lets someone find a deliverable, identify bounded responsibilities, inspect uncertainty and trace confirmation without mistaking visual neatness for agreement.

## Model before layout

Retain matrix ID/version, as-of, scope, source and overall confirmation state. Give each row and role stable IDs separate from display labels. A role can map to a named person, deputy, body or unresolved identity; retain the supplied mapping and its evidence.

Each cell needs three independent dimensions:

1. **Relationship:** R, A, C, I, justified A/R, explicit no assignment, or unresolved.
2. **Work boundary:** for example “R: supply evidence” rather than responsibility for the acceptance decision itself.
3. **Confirmation:** proposed, confirmed, disputed or unknown, with source/date when supplied.

An empty source cell is ambiguous until the source convention is known. Use “—” only for explicit no assignment and “?” for unresolved. Do not turn an unresolved A into the PM to make the grid pass an audit. Missing confirmation does not delete a useful proposal.

Store full IDs and evidence in editable JSON/CSV. CSV should have a long-form companion when a single cell cannot carry code, boundary and confirmation safely. A visual abbreviation such as R* must have its full meaning in the legend and accessible detail, not only a tooltip.

## Desktop layout

Keep deliverables on rows and roles on columns, with frozen row labels and column headers for larger matrices. Group by actual phase or workstream; do not merge independent acceptance decisions to save space. Show version, scope, proposed/confirmed state, legend and unresolved count above the matrix.

Use one restrained color per relationship plus printed letters. Distinguish confirmation with border/pattern/text, not by reusing the R/A color scale. A proposed A can be colored as A while retaining its proposed label. A/R must remain legible as two duties.

Provide row and role summaries. Flag missing/competing A, missing R, unconfirmed material assignments and unusually concentrated review demands. **Counts are responsibility patterns, not effort or utilization.** Do not compute an overload percentage from R/A totals.

Keep annotations adjacent to the affected row or in a numbered audit register. Long duties should wrap or expand; do not shrink the whole grid. Exported graphics require the same caveats and legend as the interactive view.

## Interaction and small screens

For a self-contained read-only HTML view, provide search by row/role/ID, a role-focused view, an unresolved/disputed filter and a reset. Show visible versus total rows and columns. Filtering to one role must not make a row look as if no A exists elsewhere: show “other assignments hidden” and offer the full row.

Cell selection should open persistent text containing deliverable, role, code, work boundary, confirmation and source. Use native buttons/links or a properly implemented accessible grid. Keyboard focus must be visible and must survive reset/filter changes sensibly. Hover can preview; it cannot be the only way to read an assignment.

On portrait screens, show deliverable cards with readable role/code/state lines or a focused role list. Offer full-matrix horizontal inspection when useful. Landscape can show more columns, but never require rotation to read the caveat or find an unknown assignment.

## Editing and collaboration

Default to a proposed read-only artifact. If editing is requested, separate local draft edits from confirmed agreements. Validate codes and bounded-row rules, retain before/after history, and show conflicts instead of last-write-wins assumptions. Changing a cell is not evidence that the named person accepted the duty. Sending invitations or updating a tracker follows the user's actual authorization.

## Export and review

Deliver editable source, a readable SVG/PDF/PNG when requested, an accessible table and optionally standalone HTML. Label export scope, filters and role subset. Paginate large matrices with repeated role headers/row IDs rather than squeezing text. Keep the full audit register and source/confirmation record with the graphic.

Review long labels, missing and duplicate role IDs, disputed cells, A/R, multiple A, zero R, unknown versus explicitly blank, role filtering, keyboard cell details and narrow layout. Compare every rendered letter and qualification with source data. Check that a screenshot cannot be mistaken for confirmed assignments when the source is a draft.
