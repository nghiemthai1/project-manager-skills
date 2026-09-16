---
name: risk-workshop
description: Facilitate a focused risk review and choose owned responses. Use before a commitment, after a material
  change or when uncertainty is hidden by a stale register.
metadata:
  type: interactive
  domain: software-it-project-management
  version: 2.1.0
  intent: Guide a bounded risk conversation from independent hypotheses through evidence-based assessment to response
    options, triggers and residual-risk decisions.
  frameworks: Premortem; probability-impact matrix; response planning; residual risk
  best_for: '["Guide a bounded risk conversation from independent hypotheses through evidence-based assessment to
    response options, triggers and residual-risk decisions."]'
  scenarios: '["Facilitate a premortem to identify plausible failure causes, assess uncertainty and choose responses."]'
  estimated_time: Depends on evidence and project scope
---
# Risk Workshop

## Purpose

Discover uncertainty that could change a project decision, then choose what to do about it. Produce a prioritized risk record and response recommendation. Success is a better decision or changed plan, not the largest possible risk list.

Use before commitment, at a material change or when a register no longer explains current exposure. If the event has already happened, start issue resolution and use the workshop for remaining uncertainty. A workshop cannot authorize a failed gate to pass or establish probabilities through group confidence alone.

## Input

Use the objective/decision, scope and baseline, current plan, known incidents, evidence, constraints and relevant perspectives. Existing context answers questions; do not repeat it. Missing details can remain explicit in a provisional assessment.

Choose **guided mode** to ask one material question at a time, **context-dump mode** to synthesize supplied notes and ask only gaps, or **best-guess mode** to draft hypotheses and provisional responses with assumptions visible. Best guess never means invented events, ratings, attendance, commitments or approvals.

Example: “Before we commit to migration cutover, test our confidence in attachment relationships and recoverability.”

## Key Concepts

### Premortem broadens discovery, not proof

Invite people to imagine a defined future failure and independently write plausible causes before discussion. Then ask what present evidence supports or contradicts each story. Independent input can surface concerns that a senior person's opening view suppresses. Pair it with an objective-based scan across scope, schedule, cost, quality, operations, people, suppliers and adoption; use only relevant categories.

Stories are hypotheses. “It failed in our imagined future” is not an observation or a probability estimate. Keep actual incidents separate. For sensitive disagreement, offer a route that does not require public agreement with the most senior participant.

### Assess meaning before assigning a score

Write cause, uncertain event and objective consequence. Examine likelihood, impact, proximity, detectability and evidence confidence separately. If the project has a probability/impact matrix, use its defined scales and escalation rules. If not, draft categories for agreement or use qualitative consequence/evidence descriptions without numerical multiplication.

A matrix is a screening tool. Ordinal score products do not measure expected loss, and averaging them can hide a low-likelihood consequence outside tolerance. Quantitative analysis needs relevant data, distributions and dependencies; do not simulate confidence from workshop votes.

### Responses have mechanisms and residual exposure

Avoid changes the plan to remove the exposure; mitigate reduces likelihood or consequence; transfer/share allocates defined contractual or financial responsibility; accept records an authorized decision with appropriate monitoring/contingency. Operational accountability and business disruption do not disappear because a supplier has an obligation.

Distinguish the preventive response from the contingency triggered if warning or failure occurs. “Monitor closely” may be a detection action but does not itself reduce impact. Assess residual exposure after a response is actually implemented and its effectiveness checked, not after it is merely assigned.

## Application

### Establish the conversation in up to four adaptive questions

Ask one at a time in guided mode; skip answered questions. Offer choices and accept freeform context.

1. **What decision and failure boundary are we protecting?** Options: baseline commitment, release/cutover gate, supplier handoff, major change, other. If the boundary is unclear, first produce the decision/objective statement. Do not workshop “all project risk forever.”
2. **Where is uncertainty or current evidence weakest?** Options: technical/data, timing/capacity, supplier/coordination, acceptance/operations, adoption, mixed. Branch into a relevant premortem and request direct evidence. If an event is already observed, record a linked issue and examine residual uncertainty.
3. **How will consequence and timing be assessed?** Use actual scales/tolerances if supplied. Otherwise ask which objective cannot tolerate failure and when a response stops being useful. Unknown likelihood remains unknown; a mandatory gate does not need a made-up score to deserve attention.
4. **What responses and authority are available?** Establish who can implement a change, what capacity/evidence it needs and who can accept residual exposure. If no owner or authority is known, recommend identifying that role before treating a response as committed.

### Discover and challenge

Use independent first-pass ideas, then consolidate duplicates while preserving materially different causes, populations or consequences. Ask for a contrary example and existing controls. Scan omitted objectives and stakeholders; a vendor-only group may miss operator consequences. Limit attention to decision-relevant uncertainties and explicitly park the rest with a review trigger.

### Select a numbered recommendation

Choose the best-supported branch and explain alternatives:

1. **Implement a preventive response:** when a feasible intervention can reduce a material exposure before the decision. State mechanism, effort/capacity, owner, evidence of effectiveness and residual uncertainty.
2. **Investigate before commitment:** when missing evidence could change feasibility or response choice. Define the question, bounded investigation, proposed resource/time cap and decision it will enable. Do not invent the cap as an approved allocation.
3. **Change the plan or hold the commitment:** when required evidence is absent, a gate has failed or exposure exceeds actual tolerance. Present scope/sequence/date options; only the actual authority can approve a change.
4. **Accept and monitor within authority:** when exposure and tradeoffs are understood and the authorized owner accepts them. Record warning signal, contingency, review point and decision reference. A mandatory criterion cannot be waived by choosing this label.

Multiple risks may need different branches. Do not force one score or response across the whole project. If an opportunity is in scope, make its positive objective effect explicit and evaluate action and downside on the same evidence basis.

### Produce the response record and handoff

Use the [workshop template](template.md) to capture question/answer context, risk statements, evidence/confidence, priority rationale, response, performer/owner, trigger, contingency, residual authority and next review. Keep proposed assignments and acceptance decisions separate. Hand current problems to issue resolution and material changes to change control. Revisit when evidence, proximity, scope or control effectiveness changes.

### When producing a visual

Use the [risk exposure and control map](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay recovery workshop](examples/software.md): an acceptance-critical threat is prioritized without an invented likelihood.
- [Northstar migration review](examples/migration.md): attachment integrity and recoverability require separate controls; supplier transfer is not disappearance of exposure.

## Common Pitfalls

- **Fiction becomes evidence:** premortem stories are written as incidents. Label hypotheses and seek observable support before revising factual status.
- **Precision by voting:** participants assign percentages with no basis. Use agreed qualitative meanings or an evidence-gathering action; record confidence.
- **Mitigation by document:** a runbook exists, so recoverability is called controlled. Test the actual behavior and operator ability against criteria.
- **Transfer means gone:** contract responsibility replaces the project's contingency. Retain residual business exposure and actual cutover authority.
- **Assigned means accepted:** a workshop volunteers an absent engineer. Record a proposal and confirm capacity/ownership before relying on it.
- **List without a decision:** many risks are scored but no plan changes. End with a recommendation, action/evidence, trigger and authority for each priority exposure.

## References

- [Orange Book](https://www.gov.uk/government/publications/orange-book) for broader risk-governance principles.
- [Workshop Facilitation](../workshop-facilitation/SKILL.md) supports the conversation; [RAID Log](../raid-log/SKILL.md) maintains resulting states.
- [Release Readiness](../release-readiness/SKILL.md) and [Project Recovery Advisor](../project-recovery-advisor/SKILL.md) receive evidence or plan-change recommendations.

Optional related skills are not runtime dependencies. The response record can be used on its own.
