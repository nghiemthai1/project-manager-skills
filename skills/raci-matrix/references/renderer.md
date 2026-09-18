# Offline RACI renderer

Run from this skill folder, or use absolute paths:

```sh
python scripts/render_raci.py project-data.json --output output/project
python scripts/render_raci.py --demo --output output/demo
```

The helper requires Python 3.11+ and no packages. It writes self-contained `.html`, `.svg`, `.json` and `.csv` files. Open HTML locally in a browser. No network or live assignment occurs. `--demo` alone prints SVG; validation failures exit 2 before writing artifacts. Use a new stem when preserving earlier versions.

## Input

Required strings are `title`, `version`, `as_of`, `source`, `scope`, `state`. Unknown metadata is explicit text. `roles` contains unique string `id` and `label`, with optional `function`, `authority` and `source`. `row_groups` contains display `id`, `index` and `name`. `rows` contains unique string `id`, `label`, `group`, optional row `source`, and `cells`, keyed by every role ID. Do not omit an unresolved cell.

Each cell has `code` (`R`, `A`, `C`, `I`, `A/R`, `?` or `—`), `state` (`proposed`, `confirmed`, `disputed`, `unknown`), `note` (narrow duty) and `source` (evidence reference). `?` is unresolved; `—` explicitly means no assignment. A confirmed cell requires a reference, though the helper cannot verify its truth.

`presentation` supplies `eyebrow`, `headline`, `lede`, `default_row_id`, metric cards, readout points and a decision prompt. `analysis.method` declares the audit boundary. `consulted_review_threshold` and `accountability_concentration_threshold` are positive integers used only to raise transparent review signals. They never change a code or establish workload. Put important caveats in the optional `notes` list.

## Reading and audit

Horizontal row checks flag missing or multiple A assignments, missing R, unknowns, disputes, unconfirmed assignments and consultation counts above the declared threshold. A/R counts toward both A and R. Vertical role profiles count R/A/C/I/?/— plus confirmation states and apply the declared accountability concentration threshold. They include proposed assignments and do not calculate effort or prove overload. The helper reports findings without changing letters or confirming authority.

Desktop/landscape provide a grid with sticky role/deliverable headers. Portrait uses deliverable cards. Matrix, row-audit and role-profile tabs share search, workstream, role, confirmation, findings and authority filters. Role focus hides other columns with a visible warning. Reset restores all rows/roles. Every cell is a native keyboard button with persistent duty/evidence details and arrow-key movement.

**Edit draft** opens a browser-local editor for the selected cell. It can change relationship, confirmation state, bounded duty and evidence. The renderer rejects unsupported values and refuses a confirmed assignment without evidence. If a confirmed relationship letter changes, the editor resets confirmation to proposed until current evidence is supplied. Saved edits immediately recalculate metrics, row audits, role profiles and filter metadata. The browser keeps a before/after history in local storage, supports one-step-at-a-time undo, and can restore the complete embedded source snapshot. Reloading the same artifact in the same browser retains the draft. This local state is not a multi-user agreement, live assignment or external-system write.

Source SVG, JSON and CSV downloads always reproduce the complete immutable snapshot embedded by the renderer. Draft JSON and Draft CSV contain the current locally edited matrix; draft JSON also records base version/as-of, export time, changed-cell count and edit history. Visible draft CSV contains only the current rows and focused role. Filters never alter the source downloads.

The SVG includes the product header, metric cards, grouped matrix, redundant confirmation styling, legend, scope and analysis boundary. HTML and editable files contain every evidence reference. Source JSON is exact input data; source and draft CSV are one row per cell and prefix formula-leading values with an apostrophe for spreadsheet safety. PDF/PNG require a separate actual export and inspection. There is no capacity model, notification action, conflict-resolving collaboration service or live assignment workflow.

The examples are small matrices. Inspect any larger matrix and consider multiple bounded matrices before shrinking text or hiding roles. Follow [the artifact review](artifact-review.md), including checks against actual input and rendered output.
