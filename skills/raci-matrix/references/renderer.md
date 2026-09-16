# Offline RACI renderer

Run from this skill folder, or use absolute paths:

```sh
python scripts/render_raci.py assets/software-source.json --output output/software
python scripts/render_raci.py --demo --output output/demo
```

The helper requires Python 3.11+ and no packages. It writes self-contained `.html`, `.svg`, `.json` and `.csv` files. Open HTML locally in a browser. No network or live assignment occurs. `--demo` alone prints SVG; validation failures exit 2 before writing artifacts. Use a new stem when preserving earlier versions.

## Input

The [software source](../assets/software-source.json) is a complete fictional model. Required strings are `title`, `version`, `as_of`, `source`, `scope`, `state`. Unknown metadata is explicit text. `roles` contains unique string `id` and `label`. `rows` contains unique string `id`, `label`, and `cells`, keyed by every role ID. Do not omit an unresolved cell.

Each cell has `code` (`R`, `A`, `C`, `I`, `A/R`, `?` or `—`), `state` (`proposed`, `confirmed`, `disputed`, `unknown`), `note` (narrow duty) and `source` (evidence reference). `?` is unresolved; `—` explicitly means no assignment. A confirmed cell requires a reference, though the helper cannot verify its truth. The source JSON preserves additional fields. Put important caveats in the optional `notes` list so they appear in the SVG as well.

## Reading and audit

Row checks flag missing or multiple A assignments, missing R, unknowns, disputes and unconfirmed assignments. A/R counts toward both A and R. Role totals summarize all rows, irrespective of filters, and include proposed assignments. They do not calculate effort or prove overload. The helper reports findings without changing letters or confirming authority.

Desktop/landscape provide a grid with sticky role/deliverable headers. Portrait uses deliverable cards. Search covers row data and role labels; role focus hides other columns with a visible warning. The findings filter selects rows needing review. Reset restores all rows/roles. Every cell is a native keyboard button with persistent duty/evidence details. Full SVG, JSON and CSV downloads remain independent of filters.

The SVG shows letter and confirmation state in each cell and appends narrower duty notes. HTML and editable files contain every evidence reference. JSON is exact source data; CSV is one row per cell and prefixes formula-leading values with an apostrophe for spreadsheet safety. PDF/PNG require a separate actual export and inspection. There is no cell editor or live assignment workflow.

The examples are small matrices. Inspect any larger matrix and consider multiple bounded matrices before shrinking text or hiding roles. Follow [the artifact review](artifact-review.md), including checks against actual input and rendered output.
