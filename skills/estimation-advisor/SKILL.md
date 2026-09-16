---
name: estimation-advisor
argument-hint: '[work scope and estimation evidence]'
description: Choose and explain an estimation method with units, assumptions and uncertainty. Use when sizing work
  or testing a forecast before committing effort or dates.
intent: Select an evidence-appropriate estimate and explain what it can support without turning scenarios into promised
  dates or probabilities.
type: interactive
theme: scope-and-planning
best_for:
  - Select an evidence-appropriate estimate and explain what it can support without turning scenarios into promised
    dates or probabilities.
scenarios:
  - Help estimate this uncertain integration task. We have optimistic, likely and pessimistic durations but no probability
    model.
estimated_time: Depends on evidence and project scope
frameworks: Analogous/parametric/bottom-up estimation; three-point PERT; empirical forecasting
domain: software-it-project-management
version: 2.1.0
---
# Estimation Advisor

## Purpose

Help the requester make an estimation decision proportionate to the evidence and consequence. Produce a method recommendation, calculation where justified, assumptions, uncertainty drivers and a next validation step. Use for exploratory sizing, planning or reassessment after scope or delivery evidence changes.

An estimate describes work under stated assumptions. A forecast adds current sequence, resources and calendar. A commitment is an authorized decision informed by both. The same number should not silently move through all three meanings.

## Input

Bring the work boundary and completion rule, decision being supported, units, comparable actual outcomes, constraints and dominant unknowns. Use supplied information without asking again. With no data, help choose the method and produce an assumption/evidence plan; invent numbers only for a clearly requested fictional demonstration.

Example: “We have O=2, M=4 and P=12 person-days for integration. Can we promise a date with 95% confidence?” Offer guided, context-dump or best-guess entry. Guided mode asks one material question at a time, up to four; best guess labels assumptions and does not convert absent data into a precise estimate.

## Key Concepts

### Match the method to available evidence

| Method | Fits when | Check before using / limit |
|---|---|---|
| Analogous | A completed comparable item has actual effort/duration | Explain differences in scope, team, environment and completion; one analogy is not a calibrated distribution |
| Parametric | A defensible rate/relationship links a size driver to effort | Validate unit, range and fixed setup work; extrapolation outside observed conditions can fail |
| Bottom-up | Packages and acceptance are defined enough for contributors to estimate | Include integration, review, transition and coordination once; detail does not eliminate unknowns |
| Three-point | A bounded task has explainable favorable, typical and adverse scenarios | All values describe the same task/unit; scenarios are not automatic statistical confidence bounds |
| Empirical flow forecast | Comparable completed items and relevant flow observations exist | Check demand, item size, work-in-progress and process changes; history is conditional evidence |
| Bounded investigation | A dominant uncertainty prevents defensible sizing | Define the question, proposed timebox and exit evidence; it is not the full delivery estimate |

Relative sizes can support a team's discussion, but story points are not universal hours or a cross-team productivity scale. Do not force a points-to-days conversion when relevant history is absent. Select the method before negotiating a preferred number.

### Three-point reasoning and arithmetic

For ordered values O ≤ M ≤ P in one unit, the triangular mean is `(O+M+P)/3`; the PERT convention is `(O+4M+P)/6`. `(P-O)/6` is a spread heuristic under the convention, not evidence of normality. Neither the inputs nor that formula establishes a 95% interval, a deadline probability or a calibrated expected finish. The methods weight the same scenarios differently; choose and explain the convention rather than selecting whichever yields the preferred date.

Describe the scenario conditions. An unbounded disaster does not belong as an infinite P value; bound the modeled task/scenario and retain extreme risks separately. Correlated unknowns can affect several packages together, so adding means and treating spreads as independent may understate project uncertainty.

### Effort, elapsed time and flow

Effort consumes person-time. Duration includes sequencing, available capacity, queues, waiting and calendars. Ten person-days do not guarantee five elapsed days with two people; work may not be divisible and coordination can increase. For flow-based forecasting, state the cohort and historical window and distinguish a rough rate calculation from a distribution-based forecast. A small or noncomparable dataset should reduce confidence, not encourage precise percentile claims.

## Application

### Question 1: Which decision and unit?

Offer exploratory comparison, planning forecast or commitment request. Clarify effort, elapsed duration, cost or relative size. If a date is requested, identify the schedule/capacity inputs needed rather than pretending an effort estimate is already a calendar promise.

### Question 2: What evidence is available?

Offer comparable actual work, measurable size/rate, decomposed packages, bounded scenario knowledge or little defensible evidence. Use that answer to select the method family. Reuse any supplied O/M/P or historical data, but check its boundary and unit.

### Question 3: What could materially change the estimate?

Ask about the largest unknown: unstable interface, data quality, unfamiliar technology, acceptance, environment access or external waiting. If this dominates all other inputs, prefer investigation over scoring guesses. If it is bounded, make it a scenario/assumption with a revisit trigger.

### Question 4: Are the estimate conditions feasible?

Confirm only the missing factor that affects use: contributor capability, unavailable time, dependency, parallelism or acceptance work. Record who supplied the estimate and what remains unconfirmed; do not assume a team has accepted an agent-generated number.

### Deliver the recommendation

1. Name the preferred method and why the evidence supports it.
2. Show a credible alternative or an investigation if the decisive uncertainty remains.
3. Calculate transparently where inputs permit. For three-point work use the optional [standalone helper](scripts/estimate.py) after reading [its contract](references/helper.md); it returns scenario means/spread, not probabilities.
4. State the useful estimate, scenario range where appropriate, exclusions, confidence limits and evidence that would trigger re-estimation. Do not call O–P a confidence interval.
5. Hand the effort/duration basis to capacity and schedule planning, with owner/acceptance status and unresolved dependencies. Preserve the user's target separately.

Use [the estimation template](template.md). A good estimate is explainable by its scope, evidence and conditions, not by the number of decimal places. Do not demand all four questions when the input already supports a bounded answer.

### When producing a visual

Use the [estimate ranges or empirical forecast](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the project source’s evidence and uncertainty in the graphic.

## Examples

Optional worked applications:

- [Relay three-point estimate](examples/software.md): asymmetric scenarios, different means and no invented confidence date.
- [Northstar method choice](examples/migration.md): distinguish a bounded rehearsal estimate from unknown data-correction work.

## Common Pitfalls

- **Reverse-engineered estimate:** the target becomes M and the formula repeats it. Elicit conditions independently and compare the resulting estimate with the target.
- **Precision theater:** decimals imply confidence absent from the evidence. Round appropriately and explain dominant uncertainty.
- **Points-to-hours exchange rate:** another team's velocity becomes this team's duration. Use relevant actual observations or change the method.
- **Independent-risk fiction:** shared vendor/environment uncertainty is treated as independent in every package. Model the shared condition and test the aggregate consequence.
- **Investigation without an exit question:** a spike becomes unbounded work. State what evidence it must produce and what decision follows.

## References

- [GAO Schedule Assessment Guide](https://www.gao.gov/products/gao-16-89g): estimate basis, schedule logic and uncertainty.
- [Scope and WBS](../scope-and-wbs/SKILL.md), [Resource Capacity Plan](../resource-capacity-plan/SKILL.md), [Milestone Schedule](../milestone-schedule/SKILL.md): turn the bounded estimate into a feasible plan.

Adjacent skills are optional. The estimate remains useful with its unit, basis, assumptions and handoff requirements explicitly stated.
