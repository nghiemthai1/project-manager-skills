---
name: communication-plan
description: "Design a project communication plan around stakeholder decisions, information needs, cadence, channels, and feedback. Use when updates are missed or meetings lack purpose."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Communication Plan

## Purpose

Give each audience the information needed to act at the right time. Use at initiation or when repeated updates are not resolving coordination problems. This skill creates a plan and drafts; it does not send communications or schedule meetings without authorization.

## Input

Bring stakeholders, decision rights, project cadence, existing channels, information sensitivity, and recurring misunderstandings.

Example: "Plan communications for Relay's delivery team, sponsor, security, and service owner."

If preferred channels or availability are unknown, propose them and mark them unconfirmed.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Purpose before channel

A communication exists to inform, obtain a decision, coordinate work, validate understanding, or support a transition. Choosing a weekly meeting before its purpose often produces passive reporting and unresolved decisions.

Match cadence to the decision's lead time and the rate of change. Routine updates can be asynchronous; ambiguous or contested decisions may need a focused discussion. Material exceptions need event-triggered escalation rather than waiting for the next scheduled report.

### Closed-loop communication

Sending is not the same as understanding, and understanding is not approval. Specify the response or evidence that closes the loop: acknowledged handoff, recorded decision, answered question, or validated readiness.

### Why this works

A purpose, owner, and response expectation reduce duplicate updates and make missing engagement visible. Different audiences receive different detail, while the underlying project facts remain consistent.

## Application

1. Map each audience to its decisions, affected work, and information needs. Confirm who has authority rather than inferring from distribution lists.
2. Choose channel, format, cadence, and event triggers. Use existing channels where they work; avoid parallel sources of truth.
3. Assign a communication owner and a response expectation. Mark proposed arrangements until accepted.
4. Define what evidence and version every update should use, including as-of date and baseline.
5. Plan sensitive content handling and stakeholder accessibility in context. Do not place confidential detail in a broad channel by default.
6. Include an exception path for urgent risks, missed responses, and changed decisions.
7. Review whether communications produce decisions or understanding. Remove or combine low-value meetings through the appropriate team agreement.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Same deck for everyone:** operational detail hides sponsor decisions while operators lack usable instructions. Tailor detail, not facts.
- **Cadence without trigger:** a failed gate waits a week for reporting. Define immediate exception communication.
- **Sent means approved:** a distribution list is treated as sign-off. State the required response and authority.
- **Multiple truths:** chat, slides, and tracker carry different dates. Link each update to a dated source and baseline.

## References

- [Stakeholder Map](../stakeholder-map/SKILL.md)
- [Status Report](../status-report/SKILL.md)
- [Escalation Brief](../escalation-brief/SKILL.md)
- [Release And Handover](../release-and-handover/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
