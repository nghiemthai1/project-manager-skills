# Project Manager Skills for Codex

This project includes project management skills in `.agents/skills/`. Use them to help plan, coordinate, review, recover, and close software and IT projects.

## Use the library

Match the user's task to the relevant skill description, then read that skill's `SKILL.md`. Read linked templates and references only as needed for the task. Examples are optional illustrations; open them when requested or when they clarify an unfamiliar method, rather than rereading them during routine use. Start with the user's decision and explain why the chosen framework fits and where it stops being useful. Do not run the entire lifecycle for a bounded request.

Examples of starting points:

- `project-intake-advisor` and `project-business-case` for request triage and investment options.
- `project-charter` for mandate, scope, success and authority.
- `raci-matrix` for bounded responsibility assignments.
- `gantt-chart` for dated timelines with source tables and editable chart assets.
- `integrated-project-planning` for a coherent delivery plan.
- `status-report` for an evidence-based update.
- `project-health-diagnostic` and `project-recovery-advisor` for troubled delivery.
- `release-readiness` for an evidence-based go/no-go recommendation.
- `meeting-knowledge-graph` for durable, linked meeting memory.

Use supplied context before asking questions. Ask only for missing information that changes the decision, and mark unknowns explicitly. Templates are starting points; tailor the output to the requested audience and length.

## Evidence and authority

Separate targets, approved baselines, forecasts and actual results. Keep proposals distinct from decisions, acceptance distinct from technical completion, and role suggestions distinct from confirmed authority. Never invent evidence, deadlines, funding, commitments or approvals. Fictional example values are not facts about this project.

Preserve original baselines and meeting ledgers when later decisions change current state. For OKF v0.2 bundles, retain stable slugs, unknown metadata, source links and history.

Preserve supplied IDs, version strings, slugs, paths and URLs exactly, including case, punctuation and spacing. Treat them as literal data during prose formatting; do not apply global spacing substitutions to artifacts. Compare identifiers against the input before delivering a record.

Drafting a plan does not authorize external messages, changes to live systems, spending or releases. Follow the user's actual authorization and the project's existing rules.

## Optional calculations

Four skills include offline Python 3.11+ standard-library helpers: estimation-advisor, resource-capacity-plan, milestone-schedule and project-budget. Read the owning skill's helper contract before running its script. Calculations do not establish missing evidence or grant approval.

This library has synthetic scenario and automated test evidence. Do not claim production field use or universal reliability.

## Source notices

Closely adapted skills include SOURCE.md and LICENSE.md. Preserve those files when copying packages; their stated licenses also cover their accompanying adaptations and examples. Other original packages retain the repository's stated rights status.
