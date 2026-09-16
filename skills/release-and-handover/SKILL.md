---
name: release-and-handover
description: "Coordinate an authorized release through execution, monitoring, recovery decisions, and explicit service handover. Use for software launches and IT cutovers."
metadata:
  type: workflow
  domain: software-it-project-management
  version: "1.0.0"
---
# Release and Handover

## Purpose

Carry an authorized release through controlled execution and transfer of responsibility. Use after readiness assessment, entering earlier if gate evidence is still incomplete. A successful deployment command is not the same as a stable service or accepted handover.

## Input

Bring the release scope/version, readiness record, go authority, execution plan, rollback/restore limits, monitoring, communications, and receiving service owner.

Example: "Prepare the Northstar cutover and handover workflow from the accepted rehearsal evidence."

If go authorization or mandatory evidence is missing, draft the runbook and identify the hold; do not execute a live change.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Three separate transitions

Readiness establishes whether evidence supports release. Go authorization permits a defined execution under stated conditions. Handover transfers specific responsibilities after the receiving owner accepts them. These may happen on different dates.

### Reversible and irreversible steps

A release sequence needs checkpoints before hard-to-reverse actions, a recovery decision owner, and time limits based on the actual environment. Do not invent a rollback guarantee when data changes or external effects cannot be reversed.

### Service ownership

Identify who watches the service during rollout, who handles incidents, what support material is available, and when responsibility changes. Hypercare is a defined support arrangement with exit criteria, not an indefinite period of extra attention.

### Why this works

Explicit transition conditions prevent work from falling between delivery and operations. Monitoring evidence supports a decision to continue, pause, recover, or hand over without relying on optimistic completion language.

## Application

Before drafting, separate supplied case facts from illustrative examples and neighboring cases. Do not import a lesson, test result, proposed intervention, or approval from another case. Label any new recommendation as proposed. A technical lead is not automatically the confirmed receiving acceptance authority; mark that assignment unconfirmed unless supplied. Describe a hold as recommended until an authorized hold decision is evidenced, and call an approved cutover date a baseline.

1. Confirm the release boundary, current readiness evidence, and actual authority. Resolve or hold missing mandatory gates before live execution.
2. Prepare the execution sequence with owners, prerequisites, checkpoints, verification, and recovery decision points. Mark proposed assignments until confirmed.
3. Establish immediate operational coverage, incident escalation, approved communications, and the receiving service owner's handover criteria.
4. Execute only the actions authorized by the user and relevant governance. Record actual outcomes and deviations; do not claim execution from a prepared checklist.
5. Monitor agreed signals, compare them with thresholds, and invoke the authorized recovery path when conditions require it.
6. Transfer runbooks, access, known issues, support routes, and outstanding obligations. Obtain explicit receiving-owner acceptance.
7. End enhanced support only when its exit evidence is met and accepted. Hand the delivery record, residual obligations, and benefit ownership to project closure.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Go means done:** permission is reported as a successful release. Record execution and verification separately.
- **Rollback fantasy:** irreversible data changes are ignored. Identify real recovery limits and decision timing.
- **Handover by email:** documents are sent but ownership is not accepted. Obtain the receiving owner's decision.
- **Owner gap:** project staff stop support before operations takes over. Define interim coverage explicitly.
- **Endless hypercare:** support has no exit criteria. Agree evidence, authority, and residual issue ownership.

## References

- [Release Readiness](../release-readiness/SKILL.md)
- [Communication Plan](../communication-plan/SKILL.md)
- [Decision Log](../decision-log/SKILL.md)
- [Project Closure](../project-closure/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
