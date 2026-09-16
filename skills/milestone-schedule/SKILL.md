---
name: milestone-schedule
description: "Build a dependency-based project schedule with milestone acceptance, critical-path reasoning, and explicit baseline and forecast dates."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Milestone Schedule

## Purpose

Produce a credible sequence of work and decision milestones. Use when forecasting delivery, examining a date change, or preparing a schedule baseline. A list of desired dates is an input, not a validated schedule.

## Input

Bring deliverables, durations with units, predecessor relationships, team calendars, capacity constraints, externally fixed dates, and milestone acceptance criteria.

Example: "Build the integration sequence and show whether a two-day delay changes our pilot forecast."

If task durations or links are unknown, map the missing information and provide a provisional sequence. Do not label an unsupported chain the critical path.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Critical Path Method

CPM computes the longest dependency-constrained route to completion. A forward pass establishes earliest starts and finishes. A backward pass establishes latest starts and finishes consistent with the modeled finish. Total float measures permitted movement within that model. Multiple critical paths are possible.

The local helper supports only finish-to-start links with zero lag, one duration unit, and a common origin and finish. It does not model calendars, fixed dates, resource leveling, or other relationship types. A calendar schedule must reconcile those constraints separately before dates are promised.

### Milestones and acceptance

A milestone is a zero-duration event with observable exit evidence, such as security acceptance. "Testing complete" without a completion rule is not a useful gate. Include integration, reviews, vendor handoffs, and operational readiness rather than only development tasks.

### Why this works

Dependencies explain why a date changes. Explicit duration and calendar assumptions show what the forecast relies on. Keeping a forecast separate from an approved baseline reveals variance instead of erasing it.

## Application

1. Start from accepted deliverables and required gates. Decompose enough to identify sequencing, ownership, and duration evidence.
2. Record predecessor logic, including external deliverables and reviews. Resolve cycles as planning contradictions, not by arbitrarily deleting a link.
3. Estimate durations and state calendars, waiting, and capacity assumptions. Distinguish effort from duration.
4. Compute the dependency network where applicable using [schedule.py](scripts/schedule.py); read [its contract](references/helper.md) before interpreting offsets as dates.
5. Check resource feasibility, imposed dates, holidays, and approval availability outside the simple helper. Document changes made to resolve conflicts.
6. Identify critical and near-critical work under the chosen model. Compare current forecast dates with targets and any approved baseline.
7. Present the schedule, milestone evidence, uncertainties, and decisions required. Record baseline approval separately; update forecasts without overwriting baseline history.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Dates before logic:** target dates are assigned without predecessors or duration. The plan cannot explain slippage. Build the network and compare the result with the target.
- **Resource-free realism:** independent tasks share the only specialist but are scheduled in parallel. CPM alone misses the conflict. Reconcile the capacity constraint before making a commitment.
- **Calendar smuggling:** seven working-day offsets are treated as seven calendar days. State units and apply the actual calendar separately.
- **Single critical path assumption:** one tied branch is ignored. Check all zero-float activities and critical edges.
- **Rebaseline as reporting:** the forecast replaces the original promise. Retain the approval history and variance.

## References

- [GAO Schedule Assessment Guide](https://www.gao.gov/products/gao-16-89g)
- [Dependency Map](../dependency-map/SKILL.md)
- [Resource Capacity Plan](../resource-capacity-plan/SKILL.md)
- [Estimation Advisor](../estimation-advisor/SKILL.md)
- [Change Request](../change-request/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
