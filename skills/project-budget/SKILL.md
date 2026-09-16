---
name: project-budget
description: "Build and review project cost baselines, actuals, forecasts, reserves, and earned value indicators. Use for budget planning, variance analysis, or funding decisions."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Project Budget

## Purpose

Help the project manager distinguish what the project may spend, what it has spent, and what it is now expected to cost. Use for a budget baseline, control-period update, or funding escalation. A calculated forecast is not authorization.

## Input

Bring currency, reporting date, scoped cost categories, approved budget and approval record, actuals, commitments, remaining estimate, and reserve treatment. Earned value additionally requires planned value and objective earning rules.

Example: "Explain the 16 October Relay variance and the funding decision it implies."

If planned/earned value is not maintained reliably, use actual-plus-estimate-to-complete forecasting. Do not manufacture EVM from subjective percent complete.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Baseline and funding

Budget at completion (BAC) is the performance baseline used in EVM. Contingency for identified risks may be included according to the project's budgeting convention. Management reserve is commonly held outside the performance baseline; explicitly state local treatment. A funding envelope and spending authority must be recorded separately from forecast arithmetic.

### Earned value

PV is budgeted work planned by the status date; EV is budgeted value of work actually earned under defined rules; AC is actual cost. CV=EV-AC and SV=EV-PV are value variances. CPI=EV/AC and SPI=EV/PV are ratios. SV is not a count of days. Use the [helper contract](references/helper.md) for forecast assumptions and zero denominators.

### Why this works

Comparing earned progress with cost exposes an overrun earlier than cash spent alone. A current remaining-work estimate incorporates scope changes and known problems that a historical ratio may miss. Comparing multiple forecast assumptions supports a decision rather than pretending one formula predicts the future.

Actuals, open commitments, and remaining estimates must be reconciled so the same cost is not counted twice. Define the accounting cut-off before comparing values.

## Application

1. Establish scope, currency, as-of date, baseline version, and authorization. Reconcile cost data to the same period and population.
2. Separate baseline, reserve, actuals, commitments, and estimate to complete. Document how committed but unspent costs enter the remaining forecast.
3. Choose actual-plus-remaining forecast unless objective earned-value records support EVM. Where supported, use [earned_value.py](scripts/earned_value.py).
4. Explain variances and compare forecast scenarios. Treat a ratio forecast as a diagnostic, not an automatic replacement for the management forecast.
5. Identify gaps against the baseline and total authorized funding, with explicit reserve release authority.
6. Present options with scope/schedule/quality consequences. Request a funding or scope decision from the right authority; preserve the earlier baseline.
7. Record accepted changes prospectively and show the bridge from the previous budget. Keep prior reports unchanged.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Burn equals progress:** spending 50% is reported as 50% complete. Use accepted earning rules or a separate deliverable view.
- **Reserve invisibility:** reserve is silently absorbed into BAC. State its location, authority, and release record.
- **Formula as prophecy:** EAC is presented as a guaranteed final cost. State the persistence assumption and compare a bottom-up remaining estimate.
- **Budget after the fact:** an overrun is erased by overwriting BAC. Preserve the baseline and link the authorized change.
- **Duplicate commitments:** a purchase order is included in actuals and added again in remaining costs. Reconcile incurred and unincurred amounts.

## References

- [DOE earned value and forecast guidance](https://www.energy.gov/documents/integrated-project-management-using-earned-value-management-system)
- [Status Report](../status-report/SKILL.md)
- [Change Request](../change-request/SKILL.md)
- [Project Health Diagnostic](../project-health-diagnostic/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
