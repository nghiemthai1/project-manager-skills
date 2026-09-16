# Visual artifact upgrade

Status: implemented and validated on the review branch; main promotion and private release await owner approval after automatic approval review rejected those final actions. Reference: the owner-installed gantt-chart-visualization skill and its six references, plus its mobile visualization foundation. The [reference inventory](../catalog/visual-reference.json) records inspected file hashes; the installed copy is not modified or required at runtime.

The requested outcome is comparable visual-design depth in this repository, especially Gantt and RACI, with the same standard applied whenever another skill produces a graphical artifact. Preserve the repository's project-management methods and evidence semantics. No hosted application is required.

## Capability comparison and acceptance

| Global reference capability | Project-library outcome | Verification |
|---|---|---|
| Chart fit and alternatives | Choose timeline, graph, matrix, table or uncertainty view from the decision | Guide/reference and challenge execution |
| Inspect and map source fields | Preserve IDs, source date/filter scope, planned/actual meaning, unknown fields | Explicit source mapping and hostile/missing-input fixtures |
| Normalize before rendering | Dated task layers and typed links; RACI cells retain code, work boundary and confirmation separately | Model contracts and renderer validation |
| Calendar/date semantics | Date-only values unchanged; inclusive/exclusive boundary explicit; holidays/task calendars retained | Leap-day/weekend/timezone and baseline fixtures |
| Reading and interaction | Useful default, search/filter/selection, visible scope/reset, stable rows and non-hover details | Real browser checks and screenshots |
| Mobile/accessibility | Desktop plus portrait/landscape evidence, readable labels, keyboard selection, non-color state | 390px/844px/desktop inspection and interaction |
| Static/data exports | Self-contained interactive HTML, SVG snapshot, editable JSON/CSV; clear current/full scope | Actual exported files checked against source |
| Scale and renderer choice | Small-artifact renderer with measured limits; route large/editable scheduling to appropriate tooling | Stress/empty/long-label fixtures; no unsupported performance claims |
| Other visual artifacts | Graphical contracts and examples for relevant PM jobs; tables stay tables when clearer | Complete 42-skill routing audit and reviewed examples |
| Portable distribution | All required references/assets inside packages; offline standard-library helpers | Extracted Codex package tests and private release download |

## Work gates

- [x] Read the installed guide, all six references and mobile foundation; compare current Gantt/RACI.
- [x] Upgrade Gantt guide, model/import/design/interaction/export references and template.
- [x] Upgrade RACI guide, visual model/design/audit references and template.
- [x] Produce and inspect richer Gantt/RACI artifacts for both fictional examples.
- [x] Apply visual standards to all other applicable skills, with scope-specific examples and honest chart choices.
- [x] Test source integrity, numerical/date semantics, interaction, accessibility and exports with adverse inputs.
- [x] Run authoring, catalog, calculation, packaging and cross-platform gates.
- [ ] Publish privately and verify the downloaded artifact payload.

## Boundaries

A read-only artifact can be a standalone HTML file; it does not require a web app, server, tracker integration or live writeback. Editing is a separate requested mode with calendar/dependency validation, undo and conflict handling. A renderer does not become a scheduling engine by drawing linked bars. A colored RACI cell does not confirm an assignment.

Use the reference's design principles with original project-specific explanations. Preserve existing Dean licenses when changing those packages. Do not copy installation policy from the global skill: this library retains normal automatic discovery. The global skill's unavailable sibling files must not become hidden dependencies of a distributed package.

## Delivered scope

- Two original standalone renderers: Gantt and RACI. Each fictional software/migration case includes offline HTML, SVG, exact source JSON and spreadsheet-safe CSV. Both guides teach source mapping, artifact choice, interaction, responsive reading, uncertainty and export inspection.
- All 42 packages have a recorded [visual route](VISUAL-COVERAGE.md). Thirty-three additional packages have job-specific visual contracts. Seven remain conversation/text-first by default; charts are not manufactured where they add no decision value.
- Eight additional rendered software companions cover budget, benefits, capacity, WBS, dependency handoff, stakeholder mapping, risk evidence and release readiness. Their source tables, assumptions and editable JSON accompany the SVGs. Existing full migration examples remain available; this revision does not claim eight new migration graphics.
- Codex ZIP packaging now includes HTML. The existing `.agents/skills` plus `AGENTS.md` release layout and both download aliases are preserved.

## Evidence and limits

[Visual evaluation record](../evals/visual/README.md) distinguishes independent fictional executions, corrected outputs, browser checks and structural checks. Local validation passes all 42 unit tests, including isolated renderer execution and package payload comparison. This does not certify screen-reader behavior or field adoption.

The included Gantt renderer is a read-only, date-only snapshot viewer. It preserves typed relationships and calendars but does not implement vendor adapters, resource leveling, intraday scheduling, editing, live writes or computed critical paths. Search filters its source table/cards while the chart retains the complete network; the UI explicitly states that scope. The wider guide explains when a different renderer or schedule engine is needed. The RACI helper reports evidence/assignment gaps without approving roles. Both produce full exports, not current-filter-only exports.

Two hundred-row synthetic generation probes establish only that these examples generated successfully on the local machine. They are not a large-project performance guarantee. Browser checks use local Chrome; mobile-sized layouts are not tests on physical phones.

Hosted compatibility passed on Ubuntu/Windows with Python 3.11/3.14 for commit `25c5ab0e39653986f2ddd0496412db0c22cc9e06`: [CI run](https://github.com/nghiemthai1/project-manager-skills/actions/runs/35141626680). The [local release candidate](../evals/visual/release-candidate.json) has matching payloads and six successfully executed extracted helpers. It is not yet a published release.
