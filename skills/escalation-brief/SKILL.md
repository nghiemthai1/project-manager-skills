---
name: escalation-brief
argument-hint: '[exception, options, and required decision]'
description: Present evidence, options and a precise decision request. Use when a project consequence exceeds delegated
  authority or a time-critical exception needs intervention.
intent: Draft a decision-ready escalation that explains the authority boundary, credible options, timing basis and
  consequence of no decision without assigning blame.
type: component
theme: delivery-and-decisions
best_for:
  - Draft a decision-ready escalation that explains the authority boundary, credible options, timing basis and consequence
    of no decision without assigning blame.
scenarios:
  - Prepare a decision brief for the sponsor because the forecast exceeds my authority; compare options and give
    a deadline.
estimated_time: Depends on evidence and project scope
frameworks: SBAR; options and recommendation; last responsible decision point
domain: software-it-project-management
version: 2.1.0
license: MIT
---
# Escalation Brief

## Purpose

Bring a consequential choice to someone able to make it. The output is a concise brief with evidence, options, recommendation and a specific ask. Use when the team cannot resolve an issue within its authority, a dependency threatens an agreed tolerance, or a required gate needs a decision.

Escalation is not an announcement that something is bad or a way to transfer blame. Routine coordination within authority can stay with the team. A status report may point to this brief; the brief should let the decider act without reconstructing the entire project.

## Input

Use the observed issue or threatened objective, current baseline, dated evidence, attempted responses and their results, actual authority limits, available options and decision window. Separate a forecast consequence from an already observed impact. If authority or timing is unknown, make identifying it part of the immediate ask.

Example: “Escalate the migration funding exposure and unusable supplier input. Do not present a revised budget or date as already approved.”

Draft with missing impact estimates if useful, but label it a preliminary brief or evidence request. Do not manufacture a costed option, deadline or failed remediation history. Preparing a brief does not send it.

## Key Concepts

### SBAR supplies an order, not an authority model

Adapt Situation, Background, Assessment and Recommendation to a project decision. Situation states the current choice; Background gives the relevant baseline and context; Assessment explains evidence and consequences; Recommendation names the preferred response and request. The framework originated in clinical communication; this is an original project-use application, not a claim of clinical or project certification.

Keep these sections short enough that the requested decision remains visible. The detailed test record, cost model or incident history belongs in an evidence link unless the reader needs it to compare options.

### Escalate to the right decision boundary

A sponsor may authorize funding or baseline change while security, business acceptance and service transfer have different authorities. Splitting the ask is often better than asking the most senior person to “approve everything.” Use actual delegation or identify its absence. No universal monetary, percentage or day threshold should be invented.

### The last responsible decision point has a basis

A useful decision must leave time to implement the selected response before its opportunity closes. Work backward from the irreversible action or required usable result, accounting for implementation, validation and coordination lead time. Record date/time zone and assumptions where known. If lead time or availability is unknown, label the deadline proposed and request the missing evidence; “urgent” is not a calculation.

No response is not consent. State what continuing under current authority would mean, including inability to proceed through a required gate. A team may recommend hold without claiming the formal authority already issued one.

### Compare options on the same boundary

Include the current course/no-decision consequence, the requested response and a credible alternative where one exists. Compare scope, time, cost/funding, acceptance, capacity and residual risk. Distinguish feasible options from ideas requiring investigation. A security waiver is not an available option merely because it would save time.

## Application

1. **Name the decision and actual decider.** State what exceeds the team's remit and why. If multiple authorities are involved, split the choices and their dependencies. Do not confuse the person maintaining the issue with the person authorized to accept its consequence.
2. **Reconcile the evidence.** Establish as-of, baseline/source, actual condition, current forecast and confidence. Preserve disputed facts and missing data. Link prior response attempts only if evidenced; a proposed fix is not an attempted failed fix.
3. **Explain consequence and timing.** Identify the objective at risk and what happens without a decision. Derive the useful decision window from remaining work and constraints, or label it unknown/proposed. A local supplier date gap is not automatically an identical final-project delay.
4. **Develop comparable options.** State assumptions, resources, costs, evidence gates and who would implement each. Include doing nothing as a consequence, not necessarily a valid recommendation. If missing evidence prevents comparison, request a bounded investigation with a clear return decision instead of presenting speculation as ready for approval.
5. **Recommend and ask precisely.** Explain why one option best protects the objective under known constraints. State approval scope, conditions, evidence needed and what would change the recommendation. Separate an investigation request, plan change and actual execution permission.
6. **Review and follow through.** Use the [brief template](template.md). Someone reading only the first paragraph should know the choice and urgency basis. Deliver only when authorized; record actual decision, conditions and communication state separately. Update related plans prospectively and verify the response worked. An escalation is not closed because it was sent.

Quality check: the brief uses facts rather than motives, presents a bounded ask to real authority, shows comparable options and explains the no-decision consequence. Unknowns are explicit without burying the recommendation. If the right action is local coordination, say so and avoid an unnecessary approval loop.

### When producing a visual

Use the [decision options comparison](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the project source’s evidence and uncertainty in the graphic.

## Examples

Optional worked applications:

- [Relay funding and recovery escalation](examples/software.md): the proposed review date and cost forecast remain unapproved.
- [Northstar funding and phasing decision](examples/migration.md): the reserve bridge and incomplete option evidence are visible.

## Common Pitfalls

- **Urgency without a choice:** “critical, please help” gives no action. Name the decision, authority and consequence before detail.
- **Escalation as accusation:** claims about a supplier's motives distract from the constraint. Use dated commitments, observations and impact instead.
- **False binary:** only more money or failure is offered. Examine credible sequencing, scope, timing and capacity responses; label unproven ideas.
- **Invented cutoff:** a convenient meeting date becomes a contractual deadline. State the real timing basis or mark a proposed review.
- **Approval expands:** funding consent becomes release permission. Preserve independent acceptance gates and decision scopes.
- **Sent means solved:** the issue closes when the email leaves. Track response, implementation and evidence that the consequence was resolved.

## References

- [AHRQ SBAR communication tool](https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/sbar.html) provides the communication structure; project authority and option analysis are application guidance here.
- [Status Report](../status-report/SKILL.md), [Project Budget](../project-budget/SKILL.md), [Project Recovery Advisor](../project-recovery-advisor/SKILL.md) and [Decision Log](../decision-log/SKILL.md) are optional input and follow-through artifacts.
