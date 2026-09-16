---
name: project-budget
argument-hint: '[baseline, cost evidence, and forecast assumptions]'
description: Build and review cost baselines, actuals, remaining forecasts and funding gaps. Use when planning a
  budget or explaining project cost performance and reserve decisions.
intent: Reconcile project cost evidence and forecast assumptions while separating performance measurement from spending
  authorization.
type: component
theme: controls-and-assurance
best_for:
  - Reconcile project cost evidence and forecast assumptions while separating performance measurement from spending
    authorization.
scenarios:
  - Analyze cumulative PV, EV and AC against BAC, forecast remaining cost and expose funding gaps.
estimated_time: Depends on evidence and project scope
frameworks: Cost baseline; contingency versus management reserve; earned value management
domain: software-it-project-management
version: 2.1.0
license: MIT
---
# Project Budget

## Purpose

Explain what the project is authorized to spend, what it has incurred and what its remaining work is expected to cost. Produce a cost/funding bridge, forecast comparison and decision request. Use for baseline preparation, period control, a funding escalation or a proposed scope change.

A forecast is not authorization. A budget increase does not prove better cost performance, and low cash spend does not prove healthy delivery. Keep financial evidence aligned to the same scope, currency, baseline and status date before calculating ratios.

## Input

Bring cost categories, estimates, actuals/accruals, open commitments, remaining-work estimate, approved budget and decision record, reserve treatment, currency and accounting cut-off. Earned value additionally needs planned value and objective earning rules. Reuse supplied context; partial data supports a qualified bridge, not invented precision. With no input, ask whether the decision concerns initial affordability, current variance or additional funding.

Example: “Explain Relay's 16 October cost position and the decision implied by a 120k forecast.” If PV/EV are not maintained credibly, use actual-plus-estimate-to-complete with completion evidence rather than manufacturing EVM from a subjective percent complete.

## Key Concepts

### Keep four financial views distinct

| View | Meaning / control |
|---|---|
| Performance baseline / BAC | Budget at completion for the defined scope used in performance measurement; identify its approval |
| Reserves | State the local convention: identified-risk contingency may be inside the baseline, while management reserve may be outside and separately controlled |
| Actuals and commitments | Incurred cost versus future obligations; reconcile invoiced/accrued/unspent amounts at one cut-off |
| Forecast and funding | Expected total cost versus the authorized envelope and access to funds; reserve existence is not automatic release authority |

Do not add an entire purchase order to actuals when part of it is already incurred. Explain whether unspent commitments are included in the remaining estimate. Whole-life operation or benefit costs may be outside the project baseline yet still belong in the business case; state the boundary instead of silently excluding them.

### Use earned value only with a defensible earning basis

PV is budgeted work planned by the status date; EV is budgeted value of work actually earned under defined rules; AC is actual cost. Examples of earning rules include discrete completed deliverables or weighted milestones with objective evidence. Time elapsed and money spent are not equivalent to earned progress.

`CV = EV − AC` and `SV = EV − PV` are monetary/value variances. `CPI = EV/AC` and `SPI = EV/PV` are ratios. Monetary SV is not calendar delay; SPI reaches one for fully earned baseline scope even if completion was late. Ratios with zero denominators are unavailable, not automatically healthy.

### Forecasts express different assumptions

| Forecast | Formula | When its assumption needs scrutiny |
|---|---|---|
| Bottom-up management forecast | `AC + current ETC` | ETC must cover all remaining scope, correction, commitments and transition once |
| Remaining at budget | `AC + BAC − EV` | Assumes past variance does not recur in remaining work |
| Cost efficiency persists | `BAC / CPI` | Historical aggregate efficiency must be relevant to remaining work |
| Cost and schedule efficiencies persist | `AC + (BAC−EV)/(CPI×SPI)` | Strong combined assumption; not an automatic default or date forecast |

The spread between scenarios is a prompt to inspect remaining work, not permission to pick the cheapest. The [offline helper](scripts/earned_value.py) calculates supported indicators and unavailable values; read [its contract](references/helper.md). It does not choose management's forecast, release reserve or convert currency. Preserve full calculation precision internally and round for the audience.

## Application

1. **Establish the cost boundary.** Record scope/baseline version, authorization, currency, cut-off and accounting basis. Identify whether reserve, taxes, supplier costs, internal effort and transition are included, excluded or unknown.
2. **Reconcile costs and obligations.** Build actual, committed-but-unspent and uncommitted-remaining views. Remove double counting without losing obligations; mark incomplete ledgers rather than assuming zero.
3. **Select the measurement method.** Use actual-plus-ETC unless reliable PV/EV support EVM. Where EVM applies, retain earning rules and result evidence. The helper accepts only one aligned cumulative dataset.
4. **Compare and explain forecasts.** Calculate the relevant scenarios and inspect current bottom-up remaining work. Explain material variance causes as evidenced findings or hypotheses; do not assert that a ratio identifies a cause.
5. **Show the funding bridge.** Compare the recommended/conditional forecast with BAC and the total authorized envelope. Separate reserve release from additional authority. Present scope/date/quality consequences of options to the actual decider.
6. **Record changes prospectively.** Link the exact authorization, new baseline and reserve treatment. Preserve earlier reports and the prior baseline. Revisit forecasts when actuals, scope, remaining estimates or obligations change.

Use [the budget template](template.md). A decision-ready artifact reconciles the dollars, explains the forecast assumption and makes the authorization gap visible. Unknown obligations or weak EV make the conclusion conditional rather than a reason to invent numbers.

### When producing a visual

Use the [baseline, actual and forecast comparison](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the project source’s evidence and uncertainty in the graphic.

## Examples

Optional worked applications:

- [Relay cost/funding bridge](examples/software.md): three forecast assumptions, reserve treatment and the later B2 decision.
- [Northstar cost pressure](examples/migration.md): low spend does not mean healthy progress; includes a bridge to revised funding.

## Common Pitfalls

- **Burn equals progress:** 50% spent becomes 50% complete. Use objective earning or a separate deliverable view.
- **Reserve invisibility:** reserve is silently included twice or treated as free spending authority. State location, control and release record.
- **Formula as prophecy:** one EAC becomes a guaranteed cost. Explain assumptions and compare current remaining-work evidence.
- **Budget after the fact:** BAC is overwritten to erase past variance. Retain dated reports and authorized change history.
- **Duplicate commitments:** incurred supplier cost is added again as future obligation. Reconcile consumed and unspent portions.
- **Dollar SV becomes days:** a financial variance is used to move a milestone. Use the actual schedule for calendar impact.

## References

- [DOE earned value guidance](https://www.energy.gov/documents/integrated-project-management-using-earned-value-management-system): measures and forecast assumptions.
- [Project Business Case](../project-business-case/SKILL.md), [Status Report](../status-report/SKILL.md), [Change Request](../change-request/SKILL.md): justification, reporting and authorized change.

Related packages are optional. Retain the cost boundary, evidence, forecast basis and approval distinction in a standalone budget artifact.
