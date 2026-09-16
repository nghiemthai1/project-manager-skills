---
name: project-recovery-advisor
description: "Develop feasible recovery options for a troubled software or IT project, with causal evidence, tradeoffs, authority, and measurable checkpoints."
metadata:
  type: interactive
  domain: software-it-project-management
  version: "1.0.0"
---
# Project Recovery Advisor

## Purpose

Help a project choose a credible response when the current plan is no longer feasible. Use after a health diagnostic or a material failure. Recovery may mean rescoping, resequencing, delaying, pausing, or stopping; it does not always mean preserving the original promise.

## Input

Bring the baseline, current forecast, observed blockers, acceptance constraints, available resources, and decision authority.

Example: "The migration rehearsal failed and forecast costs exceed funding. Compare recovery options."

If the cause or remaining work is uncertain, define a bounded investigation before promising a recovered date.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Cause before acceleration

A dependency bottleneck, unstable scope, insufficient capacity, and failed acceptance need different responses. Adding people will not automatically shorten work constrained by approvals or learning. Treat causal claims as hypotheses until supported.

### Feasible option set

Consider resequencing, reducing optional scope, changing release phases, adding confirmed capacity, moving dates, or pausing. Compare each with the unchanged plan. Explain consequences for users, cost, operations, and residual risk. Quality or safety conditions are not bargaining chips unless the authorized governance explicitly permits and approves an exception.

### Recovery contract

A chosen option needs an owner, approved boundaries, evidence checkpoints, and a trigger to reconsider. A new target without those elements is another unsupported promise.

### Why this works

Separating diagnosis, choice, and verification prevents urgency from turning an attractive option into a false commitment. A stop condition prevents repeated optimistic replanning from consuming funds without learning.

## Application

1. Establish the threatened objective and authority boundary. Ask the missing questions that distinguish cause, non-negotiable criteria, and available options.
2. Stabilize immediate exposure where authorized, such as holding a release lacking required evidence. Do not implement external changes merely by drafting the plan.
3. Identify causal hypotheses and the minimum evidence needed to test them.
4. Develop feasible alternatives with scope, schedule, capacity, funding, and acceptance implications. Clearly label unconfirmed assumptions.
5. Recommend an option with conditions and explain why alternatives fit less well. If none is feasible, recommend pause or termination consideration rather than an invented recovery.
6. Record the approving authority, decision, revised baseline when authorized, and evidence checkpoints.
7. Monitor outcomes against the recovery hypothesis. Define what would require revisiting the option and preserve the original baseline history.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Overtime as default:** extra hours are assumed available and effective. Confirm capacity and sustainability before modeling them.
- **Replan without cause:** the same failure recurs under a new date. Test the mechanism the response is meant to change.
- **Quality removed:** mandatory evidence is dropped to claim recovery. Preserve acceptance conditions or seek the actual authorized exception.
- **Unfunded rescue:** a revised plan relies on money not approved. Show the authorization gap.
- **No exit condition:** recovery continues indefinitely. Define evidence checkpoints and reconsideration triggers.

## References

- [Project Health Diagnostic](../project-health-diagnostic/SKILL.md)
- [Change Request](../change-request/SKILL.md)
- [Release Readiness](../release-readiness/SKILL.md)
- [Resource Capacity Plan](../resource-capacity-plan/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
