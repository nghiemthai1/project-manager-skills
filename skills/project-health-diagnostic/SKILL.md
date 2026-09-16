---
name: project-health-diagnostic
description: Diagnose delivery health and evidence confidence. Use when project status is disputed, incomplete or
  contradicted by cost, schedule or acceptance evidence.
metadata:
  type: interactive
  domain: software-it-project-management
  version: 2.1.0
  intent: Find the consequential delivery constraints through a dimensional evidence review, distinguish symptoms
    from causal hypotheses and recommend the next decision or investigation.
  frameworks: Dimensional health assessment; leading/lagging indicators; causal hypotheses
  best_for: '["Find the consequential delivery constraints through a dimensional evidence review, distinguish symptoms
    from causal hypotheses and recommend the next decision or investigation."]'
  scenarios: '["Reports are green but milestones, defects and staffing tell different stories. Diagnose current
    delivery health and missing evidence."]'
  estimated_time: Depends on evidence and project scope
---
# Project Health Diagnostic

## Purpose

Explain the condition that most needs attention and the evidence supporting that conclusion. Produce a dimensional diagnostic and a short recommendation. Use when a dashboard conflicts with delivery evidence, reports disagree, or decision-makers cannot tell whether the plan remains credible.

This is not a universal health score, certified audit or business-growth diagnostic. It evaluates software/IT project delivery against its actual objectives and authority. A status report communicates the result; a recovery advisor develops the response when the current plan is infeasible.

## Input

Bring the decision and as-of date, approved scope/date/cost, current forecasts, actual results, acceptance records, capacity, dependencies and previous reports. Rough or contradictory inputs are useful: they identify what needs investigation. Preserve supplied IDs and versions literally; a polished summary must not alter its source references.

Example: “Our report is green, but the required restore failed and the cost forecast exceeds funding. What is the real condition?”

Choose **guided** mode for one question at a time, **context dump** to synthesize the evidence already supplied, or **best guess** for a provisional diagnostic with explicit assumptions. Do not invent data or authority in any mode. Ask only for information that changes the decision; sparse evidence can support a bounded conclusion.

## Key Concepts

### Condition and confidence are separate axes

Health describes the assessed delivery condition relative to objectives. Confidence describes the strength and applicability of the supporting evidence. A clearly evidenced failed gate is poor condition with high confidence. A cheerful month-old report for a different release version is weak evidence, regardless of its color.

Unknown is neither healthy nor proof of failure. It may prevent a decision, warrant investigation or require a conservative readiness recommendation under an actual gate rule. Explain which conclusion is supported instead of assigning an arbitrary middle score.

### Dimensions cannot always compensate for one another

Review scope, schedule, cost/funding, quality/acceptance, resources, dependencies and operational readiness. Use a dimension only when material to the decision. A required gate failure remains independently consequential even if spending is below budget. A composite average can hide that fact.

Use agreed tolerances. If absent, provide a direct narrative or label provisional criteria. No standard CPI band, days-late threshold or five-color scheme is imposed by this skill. Separate an approved baseline breach from a threatened future breach and a missing forecast.

### Triangulation tests claims

Compare baseline authority, observed results and forecast basis. Check dates, versions, populations, units and sources before combining numbers. Leading indicators such as missing usable inputs may expose future trouble; lagging results such as accepted work or actual cost show what has occurred. Neither alone establishes the whole picture.

An evidence-rich forecast may still be unfavorable. A low spend percentage may reflect missing delivery rather than good cost control. A passing sample with unknown selection cannot establish population-wide acceptance.

### Symptoms do not establish causes

“Late” is an outcome, not proof of low effort. Candidate mechanisms include unavailable inputs, resource conflicts, rework, unclear scope, weak evidence or slow decisions. Write each as a hypothesis with supporting/contrary observations and the smallest discriminating check. Several independent constraints may exist; do not force one root cause because a framework asks for it.

## Application

### Ask up to four adaptive questions

Skip answered questions and ask one at a time in guided mode. Offer the options and accept other context.

1. **Which decision must this diagnosis support?** Choose continuing the plan, committing a date/funding, approving release, or resolving conflicting reports. If no decision is clear, first state the objective and the consequence of being wrong.
2. **What is actually authorized and current?** Identify baseline/decision IDs, as-of and tolerance rules. If only a target or proposal exists, diagnose against that state without inventing a baseline. If records conflict, preserve both and identify the authority/source needed to resolve them.
3. **What directly observed evidence most challenges the headline?** Branch to failed/absent acceptance, schedule/dependency, cost/funding, capacity or scope evidence. Ask about applicability and cutoff, not more dashboard labels. If the result is already supplied, inspect it rather than repeating the question.
4. **What would change the next action?** Identify missing forecast, causal evidence, authority or feasible response. If a mandatory failure already supports intervention, do not wait for perfect data in unrelated dimensions before saying so.

### Build the diagnostic

Use the [template](template.md) to show for each material dimension: authorized comparison, observation/forecast, date/version, variance or gap, evidence confidence and decision consequence. Check the overall narrative against the most consequential independent condition. Record unknowns and contradictions as findings, not silent zeroes.

For each suspected cause, describe the mechanism, supporting and contrary evidence, check and responsible role. Distinguish “confirmed blocker” from “hypothesized reason.” Keep diagnosis separate from the approval or execution of a recovery plan.

### Select a numbered recommendation

1. **Continue with targeted monitoring:** evidence supports the current course within actual limits. Name the signal that would change the conclusion; avoid an unconditional green forecast.
2. **Resolve a specific evidence gap:** the missing information could change the decision and no established condition already demands stronger intervention. Define the question, evidence owner and useful review point.
3. **Intervene through a recovery/change decision:** a supported constraint threatens or breaches objectives beyond current authority. State the affected boundary, immediate coordination and required option analysis.
4. **Recommend hold or pause at the decision boundary:** a required condition is failed/absent or no viable funded/authorized path is evidenced. Distinguish the recommendation from an actual hold decision and preserve any unaffected work that remains authorized.

Explain why the selected branch fits, which alternatives are premature and what new evidence could change it. Give the actual decision authority or the gap in identifying that authority. Finish with a concise diagnosis plus evidence table; a formal numeric overall score is unnecessary.

### When producing a visual

Use the [dimension-by-dimension health view](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay on 28 October](examples/software.md): funding changes do not resolve a failed recovery gate.
- [Northstar on 23 October](examples/migration.md): a funding exposure is known while final-date impact remains uncertain.

## Common Pitfalls

- **Composite green:** healthy dimensions cancel a required failure. Keep the gate independent and lead with its consequence.
- **Confidence mistaken for health:** detailed cost records make an unfavorable forecast look safe. State condition and evidence confidence separately.
- **Missing means fine:** blank acceptance fields become green. Identify the evidence gap and decision it prevents.
- **Symptoms become blame:** late work is attributed to effort without investigation. Compare plausible mechanisms with discriminating evidence.
- **One ratio becomes everything:** CPI or spend percentage is used as completion or schedule confidence. Interpret each measure within its boundary.
- **Diagnosis claims authority:** the report says release is formally canceled without a decision. Recommend the needed action and record actual authority separately.

## References

- [Project Budget](../project-budget/SKILL.md), [Milestone Schedule](../milestone-schedule/SKILL.md) and [Acceptance and Traceability](../acceptance-and-traceability/SKILL.md) support dimension-specific evidence.
- [Status Report](../status-report/SKILL.md), [Project Recovery Advisor](../project-recovery-advisor/SKILL.md) and [Release Readiness](../release-readiness/SKILL.md) are optional next artifacts. The diagnostic works independently using the fields above.
