---
name: communication-plan
argument-hint: '[audiences and communication needs]'
description: Plan project communications around decisions, evidence and feedback. Use when updates are missed, audiences
  need different detail or meetings fail to resolve work.
intent: Create an audience-specific communication agreement with consistent evidence, explicit response expectations
  and event-driven exception paths.
type: component
theme: stakeholders-and-collaboration
best_for:
  - Create an audience-specific communication agreement with consistent evidence, explicit response expectations
    and event-driven exception paths.
scenarios:
  - Build an audience/message/channel/cadence plan with feedback routes for the rollout.
estimated_time: Depends on evidence and project scope
frameworks: Communication matrix; push/pull/interactive communication
domain: software-it-project-management
version: 2.1.0
license: MIT
---
# Communication Plan

## Purpose

Help each audience understand or decide something in time to act. Produce a communication matrix, message patterns and a feedback check. This is useful at initiation and when “we already sent that” repeatedly fails to resolve work. It does not send messages or schedule meetings on its own.

Use a status report for one dated update, an escalation brief for one decision beyond authority, or an engagement advisor when the relationship and approach themselves need diagnosis. This plan coordinates those communications across the project.

## Input

Use affected audiences, decisions and work they own, current channels, response lead times, stakeholder preferences, evidence sources, time zones, accessibility needs and known misunderstandings. Identify which arrangements are already agreed. If a channel, cadence or contact is unknown, propose it without implying confirmation.

Example: “Sponsors want fewer meetings, but supplier changes keep reaching the test team too late. Build a plan around the real decision windows.”

Ask first for the missed decision or handoff and its consequence. A distribution list alone does not explain information needs. Avoid demanding a large survey before creating a useful draft.

## Key Concepts

### Purpose precedes channel

Informing, requesting a decision, coordinating a handoff and preparing people to operate a service need different content. Choose an asynchronous summary when evidence is stable and the response is straightforward. Use a focused discussion when interpretation is contested, tradeoffs interact or questions will change the decision. A meeting is not inherently a stronger approval record.

Match frequency to the rate of change and the latest useful response time. Routine cadence handles predictable updates. Event triggers handle a failed gate, a threatened handoff or a decision that will expire before the next report. Do not apply a universal weekly cadence or response deadline.

### Closed-loop communication has a specific closure

Delivery means a message reached a channel. Acknowledgment means it was received or understood to the extent stated. Acceptance means the actual authority agreed to the specified result. These are different records. Specify the required response: corrected forecast, acknowledged usable handoff, answered question, acceptance decision or demonstrated operator understanding.

### Tailor detail without changing facts

The sponsor may need options and funding exposure while engineers need versioned failure evidence. Both views must use the same as-of date, baseline and source. Maintain one authoritative record for each kind of fact, not necessarily one tool for every purpose. Link decisions to the decision log and technical results to the actual test record.

### Lead time includes preparation and response

Work backward from the point a decision becomes ineffective: allow evidence preparation, reviewer time and implementation lead time. If those durations are unknown, the proposed deadline remains provisional. Urgent formatting cannot create decision-maker availability. A missed response should trigger a defined route, not implied consent.

## Application

1. **Map audiences to action.** Identify who decides, contributes, operates or is affected. State one purpose per communication. Split a broad “all stakeholders” row when recipients need different actions or evidence. Confirm actual authority independently of seniority or mailing-list membership.
2. **Define the evidence contract.** Name the record/version, status date, comparison baseline and level of detail. Specify what the sender validates before use and how contradictions are resolved. If two trackers disagree, show the discrepancy and assign reconciliation instead of choosing the more convenient date.
3. **Choose channel and timing.** Use existing accessible channels that fit the purpose and sensitivity. Record routine cadence plus event trigger, response expectation and timing basis. Preserve preferences already supplied, including asynchronous communication; propose a discussion only when its decision value is clear.
4. **Close the loop.** Name the communication owner, actual recipient/authority, expected response and record location. Mark proposed assignments. Set an exception route for no response, disputed evidence or a changed decision; an escalation draft still needs authorization to send.
5. **Draft the pattern.** A decision message should contain situation/as-of, evidence, options, recommended action, specific decision and needed-by basis. A handoff message adds usable conditions and receiver validation. An operational notice states audience action, effective version/window and support route. Do not broadcast sensitive technical or personal details where a restricted evidence link suffices.
6. **Test and improve.** Walk a real missed handoff or failed gate through the [plan template](template.md). Can someone identify the recipient, useful response and fallback? At an agreed review, inspect response timeliness, reopened misunderstandings and decision quality. Attendance/open rates alone do not prove effectiveness. Combine or remove low-value communications through the actual team agreement.

Quality check: every row has a purpose, source, owner, recipient, trigger and closure; unknowns are explicit. Material exceptions have a faster path than routine cadence. The same date cannot be a target in one message and an approved baseline in another without evidence of a decision.

### When producing a visual

Use the [audience-channel cadence matrix](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the project source’s evidence and uncertainty in the graphic.

## Examples

Optional worked applications:

- [Relay communication agreement](examples/software.md): sponsor decisions, security evidence and operator readiness have distinct responses.
- [Northstar failed-gate communication](examples/migration.md): a restore failure changes the immediate communication path while later user notices remain conditional.

## Common Pitfalls

- **Distribution replaces design:** everyone gets the same deck, nobody sees their action. Split audiences by decision or operational need and keep facts consistent.
- **Read receipt becomes approval:** a delivered message is recorded as sign-off. Require the actual bounded acceptance and keep it separate from acknowledgment.
- **Urgency waits for cadence:** a failed gate sits until the weekly update. Add an event trigger tied to its decision window.
- **Parallel truths:** slides and tracker show different dates. Reconcile sources and label baseline, forecast and actual explicitly before reuse.
- **Message volume as success:** more meetings conceal unresolved questions. Review whether the required response occurred and remove duplication.
- **Unreachable fallback:** the plan says “escalate” but names no authority or alternative route. Confirm the role and availability; show the gap while unresolved.

## References

- [Stakeholder Map](../stakeholder-map/SKILL.md) and [Stakeholder Engagement Advisor](../stakeholder-engagement-advisor/SKILL.md) help identify audiences and relationship needs.
- [Status Report](../status-report/SKILL.md), [Escalation Brief](../escalation-brief/SKILL.md) and [Decision Log](../decision-log/SKILL.md) provide the dated communications and response record.
- [Organizational Change](../organizational-change/SKILL.md) checks whether operational communication leads to actual ability and adoption.

These are optional handoffs; the audience/evidence/response matrix works independently.
