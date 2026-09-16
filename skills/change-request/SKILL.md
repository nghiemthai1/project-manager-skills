---
name: change-request
description: "Assess and record a proposed change to project scope, schedule, cost, or acceptance with impact, options, authority, and baseline history."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Change Request

## Purpose

Make the consequence of a proposed change visible before it becomes an implicit commitment. Use when a request crosses agreed baseline or delegated decision boundaries. Routine backlog refinement inside those boundaries need not become a formal change board exercise.

## Input

Bring the current baseline, proposed change and reason, affected deliverables, timing, cost, risks, acceptance, and decision authority.

Example: "Assess deferring dashboard polish to protect the SSO pilot while preserving security criteria."

If impact data is incomplete, produce a preliminary assessment with the missing evidence and conditions for decision.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Change control protects informed choice

A change request connects a proposed deviation to its effects across scope, schedule, capacity, cost, quality, risk, and operations. A small feature may have a large integration or approval consequence. Conversely, a low-impact internal adjustment may sit within delegated authority.

### Baseline and forecast

A forecast updates expectations. A baseline change updates the authorized comparison point. Recording a late forecast does not itself require pretending the baseline changed; approving a change does not erase prior performance.

### Why this works

Visible alternatives make change a deliberate tradeoff. Exact approval boundaries prevent "yes to the idea" from becoming unlimited permission to spend, delay, or relax acceptance.

## Application

1. Identify the request, rationale, requester, and current baseline. Determine whether it crosses an agreed control boundary.
2. Trace affected deliverables, dependencies, acceptance, resources, cost, and service obligations. Record estimates as estimates with a basis.
3. Compare doing nothing, the requested change, and a feasible alternative where one exists. Include the cost of delay in deciding.
4. State the recommended option and evidence still needed. Identify the actual authority and decision window.
5. Keep status proposed until an authorized decision is evidenced. Record approval, rejection, deferral, or conditions accurately.
6. After approval, update only the affected baselines, notify relevant owners when authorized, and preserve the earlier versions and decision link.
7. Verify that implementation matches the approved scope and conditions. Close the request based on evidence, not merely approval.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Small favor exemption:** a request bypasses impact assessment because it sounds easy. Check interfaces, acceptance, and operating consequences.
- **Forecast becomes approval:** a more realistic date is silently adopted. Separate expected finish from authorized baseline.
- **Condition loss:** a conditional approval is recorded as unconditional. Carry the conditions into implementation and verification.
- **Bureaucracy for every task:** harmless refinement is forced through a board. Apply the agreed authority boundaries proportionately.
- **History deletion:** previous performance disappears after rebaseline. Retain the bridge from old to new.

## References

- [Decision Log](../decision-log/SKILL.md)
- [Acceptance And Traceability](../acceptance-and-traceability/SKILL.md)
- [Integrated Project Planning](../integrated-project-planning/SKILL.md)
- [Project Budget](../project-budget/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
