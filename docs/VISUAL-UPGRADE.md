# Visual artifact upgrade

Status: completed and published as [v2.1.0](https://github.com/nghiemthai1/project-manager-skills/releases/tag/v2.1.0) after owner approval. Both downloaded ZIPs and all six extracted helpers were verified. Reference: the owner-installed gantt-chart-visualization skill and its six references, plus its mobile visualization foundation. The [reference inventory](../catalog/visual-reference.json) records inspected file hashes; the installed copy is not modified or required at runtime.

The current `gantt-chart` package now carries the six reference guides unchanged, vendors the mobile foundation for standalone use, and adapts the reference entrypoint to this library's required teaching structure, evidence semantics, examples and offline renderer. It covers source-system ingestion, normalized contracts, responsive interaction, scale-aware rendering, accessibility, export and test gates directly inside the distributable package.

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
- [x] Publish privately and verify the downloaded artifact payload.

## Boundaries

A review artifact can be a standalone HTML file; it does not require a web app, server, tracker integration or live writeback. Gantt, RACI and Dependency Map now support explicitly local draft editors with validation, immutable source data, before/after history, undo, source restore and separate draft exports. Gantt recalculates the visible task schedule and supported timing diagnostics without shifting successors or recomputing source CPM analysis; RACI recalculates its audit views; Dependency Map recalculates its graph, DSM, register and local metrics while retaining cycles for coordination review. None makes a multi-user or live-system claim. A renderer does not become a scheduling engine by drawing linked bars. A colored or edited RACI cell does not confirm an assignment.

Use the reference's design principles with original project-specific explanations. Preserve existing Dean licenses when changing those packages. Do not copy installation policy from the global skill: this library retains normal automatic discovery. The global skill's unavailable sibling files must not become hidden dependencies of a distributed package.

## Delivered scope

- Ten original standalone renderers: Gantt, RACI, Dependency Map, Resource Capacity Plan, Project Budget, Milestone Schedule, Release Readiness, Risk Workshop, RAID Log and Scope and WBS. Each fictional software/migration case includes offline HTML, SVG, exact source JSON and spreadsheet-safe CSV. Gantt includes its full source-ingestion, data-contract, interaction, performance, accessibility and mobile design references plus browser-local task editing with date/milestone/progress/hierarchy validation, conflict diagnostics, recalculation, history and source/draft export separation. RACI adds matrix, row-audit and role-profile views with declared thresholds, evidence detail, separate assignment/confirmation semantics and browser-local draft editing with validation/history/undo. Dependency Map adds a directed graph, DSM, evidence register, local-margin controls, an explicit CPM boundary and browser-local agreement editing with cycle warnings, validation, history, undo and source/draft export separation. Resource Capacity Plan adds per-person stacked demand, availability markers, unknown-demand states, a capacity register, timing/skill checks, conditional options and browser-local person/allocation editing with arithmetic recalculation and source/draft export separation. Project Budget adds forecast comparison, cost-register reconciliation, EVM math, explicit unknown obligations, funding options and browser-local financial editing with recalculation and source/draft export separation. Milestone Schedule adds a recalculated logic network, timing register, milestone evidence, feasibility scenarios and browser-local task editing with cycle validation. Release Readiness adds an independent gate matrix, recommendation-to-authority decision path, recovery/coverage review, cutoff-safe chronology and browser-local gate editing with blocker recalculation. Risk Workshop adds optional declared-scale mapping, an explicit unknown lane, cause-to-contingency response chains, cutoff-safe chronology and browser-local risk editing with priority recalculation. RAID Log adds four type-specific exception lanes, a linked transition graph, timing/receiver-acceptance review and browser-local item editing with attention, unknown and overdue recalculation. Scope and WBS adds a part-of hierarchy, package dictionary, explicit requirement coverage, boundary/change review and browser-local package editing with cycle and overlap checks.
- All 42 packages have a recorded [visual route](VISUAL-COVERAGE.md). Thirty-three additional packages have job-specific visual contracts. Seven remain conversation/text-first by default; charts are not manufactured where they add no decision value.
- Two additional rendered software companions cover benefits and stakeholder mapping. Their source tables, assumptions and editable JSON accompany the SVGs. Dependency Map, Resource Capacity Plan, Project Budget, Release Readiness, Risk Workshop and Scope and WBS have moved from this static-companion set to dedicated software/migration renderers.
- Codex ZIP packaging now includes HTML. The existing `.agents/skills` plus `AGENTS.md` release layout and both download aliases are preserved.

## Evidence and limits

[Visual evaluation record](../evals/visual/README.md) distinguishes independent fictional executions, corrected outputs, browser checks and structural checks. Local validation includes generated-artifact equality, isolated renderer execution, browser interaction and package payload comparison. This does not certify screen-reader behavior or field adoption.

The included Gantt renderer is a date-only schedule viewer with a browser-local task draft. It preserves typed relationships and calendars but does not implement vendor adapters, resource leveling, intraday scheduling, link editing, live writes or critical-path calculation. It displays explicitly supplied and method-labeled criticality/float analysis, and flags that analysis for revalidation after local changes. Its product view groups phases in one sticky schedule grid, filters the visible review slice, redraws dependency links, highlights a selected chain, validates edited task fields/dates, reports timing conflicts without shifting successors, and exposes current scope in the UI and print context. Permanent SVG/JSON/CSV downloads preserve the complete source snapshot; draft JSON/CSV and the explicitly labeled visible-draft CSV remain separate. The Dependency Map renderer calculates only comparable calendar-day local margins, preserves unknowns and acceptance states, and does not infer commitments, critical paths or project delay; its local editor never writes to source files and marks retained analysis for revalidation. The RACI helper audits rows and role patterns without approving roles, inferring authority or treating assignment counts as workload. The Capacity renderer recalculates supported hourly arithmetic and exposes unknown allocations, but does not infer skill interchangeability, level resources, resolve intraday conflicts or approve staffing changes; its evidence checks and option outcomes are visibly marked for revalidation after local edits.

The Project Budget renderer recalculates supported EVM and cost-bridge arithmetic but does not select a forecast, convert monetary schedule variance into time, release reserve or authorize spending.

Two hundred-row synthetic generation probes establish only that these examples generated successfully on the local machine. They are not a large-project performance guarantee. Browser checks use local Chrome; mobile-sized layouts are not tests on physical phones.

Hosted compatibility passed on Ubuntu/Windows with Python 3.11/3.14 for commit `25c5ab0e39653986f2ddd0496412db0c22cc9e06`: [CI run](https://github.com/nghiemthai1/project-manager-skills/actions/runs/35141626680). The [local release candidate](../evals/visual/release-candidate.json) has matching payloads and six successfully executed extracted helpers. That candidate report is historical; the published v2.1.0 release includes the final downloaded-payload verification report.
