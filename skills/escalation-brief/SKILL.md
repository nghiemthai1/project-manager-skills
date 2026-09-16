---
name: escalation-brief
description: "Draft a focused project escalation with evidence, impact, options, recommendation, and a decision owner. Use when a blocker exceeds delegated authority."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Escalation Brief

## Purpose

Bring an unresolved consequence to someone able to decide. Use when authority, resources, tolerance, or a time-critical gate exceeds the team's remit. An escalation should make a choice easier, not transfer blame or merely announce bad news.

## Input

Bring the issue, evidence, affected objective, attempted responses, authority limit, options, and decision window.

Example: "Escalate Northstar's forecast funding gap and cutover options to Noel."

If the decision owner or needed-by date is unknown, identify that gap explicitly. Drafting does not authorize sending.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Escalation threshold

Escalate when the consequence or decision lies outside delegated authority, when an unresolved dependency threatens an agreed tolerance, or when a gate requires a higher-level choice. Do not invent a universal monetary or day threshold; use the project's actual rules.

### Decision-oriented structure

State situation, evidence, consequence, options, recommendation, and specific ask. Explain what happens if no decision is made. Distinguish the last responsible decision point from an arbitrary urgent deadline.

### Why this works

An authority holder can compare feasible options without reconstructing the whole project. Including attempted responses shows what remains unresolved without turning the brief into a defense of the team.

## Application

1. Confirm what exceeds the team's authority and which objective is affected.
2. Reconcile the evidence and baseline. Separate observed impact from forecast consequence.
3. Describe previous responses and why they did not resolve the decision. Avoid attributing motives or blame.
4. Present feasible options, including the consequence of no action. State tradeoffs in scope, time, cost, quality, and risk where material.
5. Recommend an option with a rationale and any conditions. Do not offer an unauthorized waiver as if it were available.
6. Address the ask to the actual decision authority, with the evidenced decision window or an explicitly proposed deadline.
7. Deliver a draft brief and record the resulting decision only when it occurs. Update related artifacts after authorization.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Urgency without decision:** "this is critical" leaves the recipient unsure what to do. State the choice and consequence.
- **Escalation as accusation:** blame displaces useful evidence. Explain the constraint and options.
- **False binary:** only "approve more money" or "fail" is offered. Evaluate scope, sequence, timing, and capacity alternatives where feasible.
- **Deadline invention:** a convenient date is presented as a contractual cutoff. Label the basis and uncertainty.
- **Silent send:** a drafted brief is treated as delivered. Keep external action and approval explicit.

## References

- [Status Report](../status-report/SKILL.md)
- [Project Budget](../project-budget/SKILL.md)
- [Project Recovery Advisor](../project-recovery-advisor/SKILL.md)
- [Decision Log](../decision-log/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
