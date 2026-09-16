---
name: project-charter
description: "Draft a project charter with outcomes, scope boundaries, authority, constraints, and success measures. Use to authorize or clarify a software or IT project."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Project Charter

## Purpose

Establish what the project exists to achieve and the authority under which it will operate. Use before detailed planning or when inherited work lacks a shared mandate. A draft charter is not an approval, and a charter is not a full implementation plan.

## Input

Bring the problem, intended outcome, sponsor, affected users, constraints, proposed scope, funding basis, and decision rights.

Example: "Draft the Northstar migration charter from this business case and sponsor mandate."

If the sponsor or authorization is missing, write a proposed charter and an explicit decision request.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Outcomes, outputs, and boundaries

An output is a deliverable, such as a migrated service desk. An outcome is the change it enables, such as support staff processing the agreed workflows on the new system. Specify measurable completion and an owner for post-project benefit review; do not promise benefits without a measurement basis.

Scope exclusions prevent plausible adjacent requests from quietly entering the plan. Constraints state actual limits, while assumptions state unverified conditions. A target is not a commitment until the relevant authority approves it.

### Authority

Name who sponsors the project, who coordinates it, who accepts deliverables, and who decides changes outside delegated tolerances. RACI may clarify work responsibilities later, but it cannot create authority absent from the organization.

### Why this works

A short mandate provides a stable reference for later tradeoffs. It makes disagreements visible before detailed schedules give them the appearance of agreement.

## Application

1. State the problem and desired operational outcome in terms stakeholders can assess.
2. Define the deliverables, exclusions, and acceptance authority. Separate immediate project completion from benefits realized later.
3. Record target dates, funding basis, constraints, assumptions, and major uncertainties without inventing precision.
4. Identify sponsor, project manager, key owners, and escalation/change authority. Mark nominations as proposed until accepted.
5. State success measures and where their evidence will come from.
6. Present the charter as proposed or approved according to actual evidence. Record the approving person, date, and decision reference only when supplied.
7. Use the charter to guide kickoff and scope decomposition; escalate contradictions rather than quietly resolving them in the document.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Solution as purpose:** "install platform X" hides the problem being solved. Add the operational outcome and success evidence.
- **Everything included:** a broad transformation promise has no exclusions. Name adjacent work outside the mandate.
- **Signature fiction:** a polished template includes an approval never given. Keep the status proposed and show the pending decision.
- **Benefit ownership gap:** success is defined only after the team dissolves. Assign a post-project review owner without claiming the benefit already occurred.

## References

- [Scope And Wbs](../scope-and-wbs/SKILL.md)
- [Project Kickoff](../project-kickoff/SKILL.md)
- [Decision Log](../decision-log/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
