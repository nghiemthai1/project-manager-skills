---
name: resource-capacity-plan
description: "Compare project demand with realistic availability and skills, expose overloads, and develop staffing or scope options for a defined planning period."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Resource Capacity Plan

## Purpose

Make resource constraints visible before they become missed commitments. Use for sprint preparation, shared-specialist allocation, or cross-project planning. This plan proposes allocations; it does not grant authority over another manager's staff.

## Input

Bring a common planning period, named people or explicit roles, gross available hours, leave, operational duties, other assignments, and the demand basis.

Example: "Check whether Omar can support the pilot while retaining his support rotation."

Missing cross-project allocations make available capacity uncertain. Do not treat the absence of those records as zero demand.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Capacity is not headcount

Gross hours minus leave and non-project overhead gives modeled availability. Compare it with all demand in the same period. Do not subtract the same meeting or support duty twice: either it is a deduction or an allocation with a clear basis.

### Skills and timing

Unused hours on a security specialist do not automatically replace integration engineering hours. A period total can also hide a one-day peak or a dependency bottleneck. Review skill fit and intra-period timing after the arithmetic.

### Why this works

A named overload creates a concrete choice: reduce or defer demand, change sequence, add genuinely available skilled capacity, or accept a consequence through the right authority. An optimistic utilization target creates no capacity.

Use hours when reliable effort estimates exist. For a stable agile team, empirical throughput may provide a better forecast than detailed individual allocation. Never convert story points using a universal hours ratio.

## Application

1. Establish period boundaries and whether data covers all assignments. Label missing allocations as unknown rather than entering invented zeros.
2. Separate gross hours, leave, overhead, and project demand. Record source dates and assumptions.
3. Use [capacity.py](scripts/capacity.py) for hour-based comparison after reading [the input contract](references/helper.md).
4. Examine each person's overload and required skill. Do not let aggregate spare hours cancel a specialist shortage.
5. Check sequencing and intra-period peaks. Compare realistic options with their lead times and learning costs.
6. Record proposed allocation changes, approving resource managers, and unresolved decisions. Recalculate only after changes are confirmed or clearly label a what-if scenario.
7. Review when availability, scope, or external commitments change. Feed confirmed capacity to the schedule.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **100% before interruption:** all gross hours are committed while leave and support are ignored. Include evidenced deductions or label them unknown.
- **Double haircut:** support is deducted from availability and counted again as demand. Reconcile each category once.
- **Fungible people:** spare security hours are used to cancel an engineering overload. Check the actual skill and timing requirement.
- **Nominal staffing:** a new hire is treated as productive immediately. Include confirmed start, access, onboarding, and supervision demands.
- **False certainty from empty records:** missing assignments are entered as zero. State the data gap and withhold an unconditional feasibility claim.

## References

- [Capacity in Sprint forecasting](https://scrumguides.org/scrum-guide.html)
- [Sprint Planning](../sprint-planning/SKILL.md)
- [Milestone Schedule](../milestone-schedule/SKILL.md)
- [Project Recovery Advisor](../project-recovery-advisor/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
