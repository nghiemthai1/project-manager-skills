---
name: project-business-case
description: Compare project options, costs, benefits and uncertainty. Use when an investment or material continuation
  decision needs a defensible business case.
metadata:
  type: component
  domain: software-it-project-management
  version: 2.1.0
  intent: Recommend an investment option with explicit alternatives, assumptions, benefit ownership and a decision
    boundary.
  frameworks: Options appraisal; cost-benefit analysis; sensitivity analysis
  best_for: '["Recommend an investment option with explicit alternatives, assumptions, benefit ownership and a decision
    boundary."]'
  scenarios: '["Use project-business-case: Recommend an investment option with explicit alternatives, assumptions,
    benefit ownership and a decision boundary."]'
  estimated_time: Depends on evidence and project scope
---
# Project Business Case

## Purpose

Help an authorized sponsor decide whether to invest, defer, stop or investigate. Produce a recommendation that explains the problem, realistic alternatives, whole-life consequences and the assumptions that could reverse the choice. Use before a charter or when a project's business justification materially changes.

A business case is a decision argument, not a sales pitch for an already preferred solution. A project can deliver its specification and still have a weak business case. Conversely, mandatory work may be justified without a positive monetized return; compare feasible ways to meet the obligation rather than inventing savings.

## Input

Bring the problem and affected people, current performance, decision deadline, options, cost estimates, benefit hypotheses, constraints, dependencies and funding authority. Rough notes are sufficient for a partial case. Use supplied context without re-asking; if nothing is supplied, ask what investment decision is being considered and provide an empty options structure.

Example: “Compare a one-tenant SSO pilot with a full rollout and deferral. We know delivery estimates but have no verified support-cost baseline.” Missing amounts remain unknown. Do not treat a requested budget as a cost estimate or a vendor quote as a complete whole-life cost.

## Key Concepts

### Compare against a credible counterfactual

The counterfactual describes what happens without this investment: continued service, minimum maintenance, rising support costs, or inability to meet a known obligation. It is not always zero cost or zero risk. Include a do-minimum option where doing nothing is infeasible. Compare options over a common population, period and price basis; otherwise their apparent advantages may come from different boundaries.

### Separate affordability from value

An option may have attractive expected benefits but exceed available funding or scarce delivery capacity. Identify implementation, migration, training, recurring operation, transition overlap and exit costs. Record contingency basis and management reserve separately. Do not count the same reserve in both an estimate and an extra allowance.

Benefits may be cash-releasing savings, capacity released for other work, revenue effects, reduced exposure or unmonetized service improvements. Time saved is not automatically cash saved: identify whether spending can actually fall. Benefits shared by two initiatives need an attribution rule so a portfolio does not claim both in full.

### Use the arithmetic only when its inputs fit

| Method | Useful question | Required caution |
|---|---|---|
| Undiscounted net benefit | Over this stated short horizon, do incremental benefits exceed incremental costs? | State timing is ignored; do not call it NPV |
| Payback | When does cumulative net cash flow become nonnegative? | Timing and recurring cost matter; payback ignores value after that point |
| NPV | What is the value of dated future net cash flows on an agreed discount basis? | Use an evidenced rate and horizon; show `sum(net cash flow_t / (1+r)^t)` and initial outlay consistently |
| Sensitivity / scenarios | Which assumptions would change the decision? | Vary consequential assumptions, including correlated changes; a base case is not a probability forecast |

Do not import a universal discount rate, uplift, ROI target or assumed realization percentage. If data are inadequate, produce a conditional case and propose the smallest investigation that can change the decision.

## Application

1. **Frame the decision.** State the problem, evidence, objective, decision owner and latest useful decision point. Separate the observed problem from the proposed solution. Identify mandatory outcomes before comparing discretionary benefits.
2. **Build viable options.** Include counterfactual/do-minimum and at least one meaningfully different option where available. Eliminate an option only with a stated reason such as inability to satisfy acceptance, unaffordable cash needs or unavailable capacity.
3. **Model consequences consistently.** Use the same horizon and cost/benefit categories for every option. Separate sourced estimates, assumptions and unknowns. Assign proposed benefit owners and data sources without inventing their acceptance.
4. **Challenge the preferred option.** Test adoption, cost escalation, delivery delay and continuing operating costs. Calculate a break-even assumption when meaningful. Explain nonfinancial effects alongside the model rather than burying them in an arbitrary score.
5. **Recommend a bounded action.** Choose invest, defer, stop, do minimum or investigate. State conditions, staged funding or pilot limits where useful. Preserve disagreement and the strongest alternative; sunk costs alone do not justify continuing.
6. **Record the actual decision and handoff.** A recommendation remains proposed until the actual authority decides. Pass the authorized boundary to the charter and planning work; pass benefit definitions and review needs to the eventual business owner. Revisit when a material assumption changes.

Use [the business-case template](template.md). Before calling the case decision-ready, check that the recommendation can be traced to comparable options, every decisive number has a basis, affordability is addressed and the downside could be explained to a skeptical sponsor. Unknown mandatory evidence makes the decision conditional rather than magically complete.

### When producing a visual

Use the [option comparison with ranges](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay pilot investment](examples/software.md): a conditional short-horizon comparison with explicitly synthetic benefit assumptions.
- [Northstar continuation](examples/migration.md): a material forecast change calls for renewed justification, not retrospective approval.

## Common Pitfalls

- **Only the preferred option is plausible:** alternatives are deliberately weak, so comparison adds no scrutiny. Include a credible smaller or staged option and the real counterfactual.
- **Capacity savings called cash:** staff time improves but expenditure does not fall. Separate released capacity from cash savings and identify the mechanism for monetization.
- **Sunk-cost defense:** “We have spent too much to stop” ignores remaining value. Compare future incremental consequences, while reporting prior spend transparently.
- **Precision without a baseline:** an exact ROI rests on unmeasured demand or adoption. Label assumptions, show ranges and collect the decisive baseline.
- **Positive NPV treated as permission:** the calculation hides cash limits or required acceptance. Check affordability, authority and constraints before recommending commitment.

## References

- [Project Charter](../project-charter/SKILL.md): translate an authorized option into a mandate.
- [Project Budget](../project-budget/SKILL.md): cost baseline, actuals and forecasts.
- [Benefits Realization](../benefits-realization/SKILL.md): test the outcome after delivery.
- [HM Treasury Green Book](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government): appraisal reference; its jurisdiction-specific rules and rates are not defaults for this library.

Adjacent skills are optional handoffs. The case should stand alone with its decision, basis, alternatives and conditions.
