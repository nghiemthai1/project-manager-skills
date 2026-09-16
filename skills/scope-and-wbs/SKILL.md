---
name: scope-and-wbs
description: "Define project scope and a deliverable-oriented work breakdown with exclusions, ownership, and completion evidence. Use before estimating or controlling scope."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Scope and Work Breakdown

## Purpose

Translate a mandate into manageable deliverables without hiding the work required for acceptance and transition. Use for initial planning or impact analysis. A WBS organizes scope; it does not prescribe the execution sequence.

## Input

Bring the charter, deliverables, exclusions, acceptance conditions, interfaces, and known constraints.

Example: "Break the SSO pilot into work packages, including the work needed to operate it."

If boundaries are disputed, capture competing interpretations for decision rather than choosing one silently.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Deliverable-oriented decomposition

A work breakdown structure groups all agreed project work into progressively smaller deliverables or work packages. The 100% rule is a completeness test: children together cover their parent's scope without overlapping it. It is not a claim that all requirements are known at kickoff.

A work-package description states its outcome, boundary, owner, and completion evidence. Stop decomposing when the package can be estimated, assigned, and assessed credibly. Excessively small tasks make the hierarchy expensive to maintain; packages too broad hide uncertainty.

Include management, integration, testing, migration, training, rollout reversal, and closure work when required. Product features alone rarely represent the whole project.

### Why this works

Scope boundaries reduce double counting and expose omitted work before costs and dates acquire false precision. A separate dependency model then sequences these packages. Agile work can use evolving lower-level detail while preserving explicit release boundaries.

## Application

1. Confirm the mandate and scope version. List included outcomes and explicit exclusions.
2. Decompose by deliverable or workstream, then into accountable work packages. Keep the hierarchy understandable to its owners.
3. Write a brief dictionary entry for each package: outcome, boundary, acceptance, owner, assumptions, and interfaces.
4. Check parent coverage and overlap. Include enabling and transition work, not only build activity.
5. Flag unresolved scope decisions before estimating affected packages. Do not hide unknown work in a miscellaneous bucket.
6. Hand packages to estimation, capacity, and schedule planning. Maintain scope versions and route material changes through the agreed change process.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Task list mistaken for scope:** a sequence of meetings omits the required outcome. Anchor packages in deliverables and their acceptance.
- **Missing transition work:** training and support disappear from estimates. Review the operational handover explicitly.
- **Double-counted integration:** every team estimates the full shared integration effort. Define ownership and boundaries at interfaces.
- **Decomposition as certainty:** a detailed hierarchy hides unknown data quality. Preserve uncertainty and investigation work.

## References

- [Project Charter](../project-charter/SKILL.md)
- [Acceptance And Traceability](../acceptance-and-traceability/SKILL.md)
- [Estimation Advisor](../estimation-advisor/SKILL.md)
- [Change Request](../change-request/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
