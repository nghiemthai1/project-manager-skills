---
name: estimation-advisor
description: "Select and explain an estimation approach for software or IT work, with ranges, assumptions, and validation steps. Use before committing dates or effort."
metadata:
  type: interactive
  domain: software-it-project-management
  version: "1.0.0"
---
# Estimation Advisor

## Purpose

Choose an estimation method proportionate to the uncertainty and consequence of the decision. Help the requester understand the estimate's basis and limits. Use for early sizing, delivery planning, or reassessment after new evidence. Do not manufacture confidence by adding decimal places.

## Input

Bring the work description, definition of complete, decision being supported, comparable outcomes, and relevant constraints.

Example: "Estimate the integration work. We have one completed comparable change, but the provider interface is not stable."

With no data, guide method selection and produce an assumption log. A worked demonstration is allowed only when clearly labeled fictional; it is not the user's estimate.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Choose by uncertainty

| Approach | Fits | Does not establish |
|---|---|---|
| Analogous estimate | A genuinely comparable completed task exists | Accuracy when scope, team, or environment differ materially |
| Bottom-up estimate | Work and acceptance are decomposed enough to size | Certainty about hidden integration or coordination work |
| Three-point estimate | A bounded task has identifiable favorable, typical, and adverse conditions | A validated deadline probability |
| Empirical throughput forecast | Comparable completed items and stable flow observations exist | Transferable team productivity or a guarantee |
| Timeboxed investigation | A dominant unknown prevents defensible sizing | The final delivery duration before investigation |

### Three-point reasoning

Optimistic, most-likely, and pessimistic values describe the same task in the same unit. The triangular mean is (O+M+P)/3. The PERT convention weights the most-likely case: (O+4M+P)/6. The spread (P-O)/6 is a heuristic, not evidence of a normal distribution. Do not turn it into an automatic 95% interval.

Effort consumes person-time. Duration depends on sequencing, capacity, waiting, and calendars. Story points are team-local relative measures, not exchangeable hours.

### Why this works

Selecting the method before calculating avoids using an attractive number to conceal missing knowledge. Explaining the adverse case identifies what to investigate or mitigate. Re-estimation becomes a response to changed evidence rather than negotiation over a preferred date.

## Application

1. Ask what decision the estimate supports: exploratory comparison, a planning forecast, or a commitment request. Reuse answers already supplied.
2. Ask only the missing discriminator: comparable history, scope clarity, or the dominant unknown. Offer appropriate methods and explain their tradeoffs.
3. Recommend one method and state what evidence would change that recommendation. If the unknown dominates, recommend an investigation with an exit question.
4. Elicit values and units with the people closest to the work. Separate assumptions, exclusions, waiting time, and external dependencies.
5. Calculate transparently. For three-point work, optionally use the [standalone helper](scripts/estimate.py) and its [input contract](references/helper.md).
6. Present the range, central estimate if justified, confidence limitations, and validation/revisit trigger. Keep the estimate separate from an approved commitment.
7. Hand duration planning to the schedule and capacity process. Do not add uncertain task estimates as if correlation and parallelism do not exist.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Reverse-engineered estimate:** the desired date becomes the most-likely input. The calculation merely restates pressure. Elicit scenarios independently, then compare the forecast with the target.
- **Precision theater:** 5.000 days sounds more certain than the inputs. Show useful precision and describe the uncertainty drivers.
- **Points-to-hours exchange rate:** another team's velocity is used to price this team's work. Rebuild the estimate with relevant observations or explicit effort assumptions.
- **Unbounded pessimistic case:** an outage lasting forever becomes the P input. Define the scenario boundary and log catastrophic tail risks separately rather than pretending the three points cover every possibility.

## References

- [Schedule estimation and uncertainty](https://www.gao.gov/products/gao-16-89g)
- [Scope And Wbs](../scope-and-wbs/SKILL.md)
- [Resource Capacity Plan](../resource-capacity-plan/SKILL.md)
- [Milestone Schedule](../milestone-schedule/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
