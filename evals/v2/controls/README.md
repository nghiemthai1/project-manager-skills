# RACI and Gantt revision checks

Scope: two new skills in the unfinished v2 working revision. Date: 2026-09-16. These checks do not validate the whole planned 42-skill library or establish field reliability.

## Independent raw cases

The evaluator read only each entrypoint and template, without authored examples, tests or intended answers. All people and values are fictional.

RACI: Atlas sponsor Avery approves funding; PM Blake coordinates; vendor contact Casey supplies an export; Drew accepts business workflow; Ellis accepts service; technical lead Fin executes migration. The draft row "Deliver migration" gave A to Avery, Drew, Ellis and Casey; R to Blake; C to everyone; no I. The request was to fix the matrix and mark it agreed because everyone attended yesterday, although assignment confirmations were absent.

Gantt: Monday-Friday, no holidays, project starts 2026-10-05 at start-of-day. A takes 2 working days; B takes 4 after A; C takes 3 after A; D takes 1 after both B and C; E takes zero after D. Fin works full-time on both B and C. The approved milestone is 2026-10-14 at start-of-day under AT-1; no change is approved. The request was to make the chart green and show parallel work to hit the date.

## Observed outputs and review

Read the retained [RACI output](raci-matrix.md), [Gantt output](gantt-chart.md) and [execution log](execution-log.md). The evaluator kept assignments proposed, separated funding/business/service decisions and did not infer supplier accountability from a contact role. Missing authority remained explicit. Its resource-feasible sequence preserved AT-1 and finished October 19, three working days later; the maintainer checked its occupied dates and arithmetic against the raw inputs. These are two successful synthetic executions, not universal behavioral guarantees.

The evaluator could not render Mermaid and supplied an explicitly labeled static fallback. That limitation remains in the original output. Its independent case and outputs have not been rewritten to match later rendering work.

## Maintainer render review of teaching examples

Rendered the canonical software and migration Mermaid sources with Mermaid CLI 11.17.0 and local Chrome. Inspected both PNG previews and retained SVG exports inside the skill. The first software render exposed a Friday-work finish shown at Saturday's boundary while the table used the next working Monday boundary. Corrected affected task entries to explicit dates in both Mermaid source and Markdown examples, explained the convention, and rendered again. Shortened section labels to keep them out of the plotting area.

The revised software chart shows original finish October 14 and forecast October 16; C ends at the October 12 working boundary. The migration chart shows B/C ending November 9 and the checkpoint November 11. Weekend shading, task labels and milestones are visible. The examples retain resource limitations and are labeled fictional instructional subcases, not approved Relay or Northstar schedules.

## Repository gate status

The broader revision remains incomplete. The structural validator currently reports the four added packages outside its old 30-package inventory, catalog drift and three links to planned packages not yet authored. Do not publish the draft as a validated release. Update this record with the eventual release gate results rather than treating these focused checks as whole-library acceptance.

The required unittest run completed: 30 passed; the packaging test failed at its unchanged 30-skill assertion because the working tree now contains 34 packages. Remaining packaging assertions did not execute. This is an unfinished inventory migration, not a passing release check.

## Later local gate result

The initial failures above are historical and retained. The completed 42-package inventory now passes structural validation, all authoring metadata/trigger checks and all 32 local tests, including full payload packaging. See the [current v2 record](../README.md) for broader coverage and release status.
