---
name: milestone-schedule
description: Build and analyze dependency logic, float and milestone forecasts. Use when testing schedule feasibility
  or the effect of a duration or dependency change.
metadata:
  type: component
  domain: software-it-project-management
  version: 2.1.0
  intent: Produce an explainable schedule model and milestone decision without confusing unconstrained offsets with
    feasible committed dates.
  frameworks: Critical Path Method; total float; rolling-wave scheduling
  best_for: '["Produce an explainable schedule model and milestone decision without confusing unconstrained offsets
    with feasible committed dates."]'
  scenarios: '["Calculate which dependency paths govern finish and how much total float each activity has in this
    task network."]'
  estimated_time: Depends on evidence and project scope
---
# Milestone Schedule

## Purpose

Explain when the modeled work can finish, which dependencies govern that result and what a change actually affects. Produce a task network, calculated offsets where valid, milestone evidence requirements and a feasible calendar forecast only when the necessary resources/calendars are known. Use for baseline preparation, remaining-work planning or a claimed delay.

A target date is a comparison, not an input that makes the work fit. A Gantt chart communicates dated work; this skill establishes and challenges the logic behind it. Keep scope, forecast and approved comparison versions visible.

## Input

Bring deliverables, duration estimates and units, predecessor relationships, calendars, resource limits, external commitments, review lead times and milestone criteria. Use supplied context directly. With missing durations or links, create a provisional logic/missing-input table; with no input, ask which finish decision is being tested. Do not label an unsupported chain critical.

Example: “The vendor handoff is two days late. Show what evidence we need before changing the pilot forecast.” The local helper accepts a limited model, so do not silently discard unsupported date constraints or relationship types to make an input run.

## Key Concepts

### Calculate the network, then test whether it can be worked

For finish-to-start relationships with zero lag, a task starts after all predecessors finish. In a forward pass, `ES = max(predecessor EF)` and `EF = ES + duration`, with an origin of zero for tasks without predecessors. The modeled finish is the largest terminal EF. In a backward pass, terminal LF is that common finish; other `LF = min(successor LS)` and `LS = LF − duration`. Total float is `LS − ES`, equivalently `LF − EF`.

A longest path governs the modeled finish; tied paths can all be critical. Total float describes movement allowed within this complete model, not free spare time owned independently by each team. Moving one activity can consume float available to others on the same path. Free float concerns delay before an immediate successor's earliest start; it is a different measure and is not returned by this helper.

The [standalone schedule helper](scripts/schedule.py) models an acyclic, finish-to-start, zero-lag network in one duration unit with a common origin/finish. It does not model working calendars, fixed-date constraints, resource leveling or other relationship types. Its result is an unconstrained offset model. Read [the input/output contract](references/helper.md) before using it; use an appropriate external scheduling method for unsupported logic rather than mislabeling the simplified result.

### Effort, calendars and scarce people change feasibility

Durations need a stated workweek, holidays, shifts and availability before becoming dates. Weekend cutover can use a different calendar from weekday engineering. A successor's earliest working start can differ from the calendar boundary at which a predecessor's productive work ends; state the convention and check any rendered chart.

Parallel branches that require one person full time are not feasible just because CPM overlaps them. Resolve the resource conflict through sequencing, actual additional capacity or a changed scope/duration assumption. Record an added resource-ordering link as a planning choice rather than pretending it was the original technical dependency. Recalculate and retain both models where comparison helps.

### A milestone is an event with evidence

Use zero duration for the acceptance or decision event. Model preparation, execution, review effort and reviewer waiting as real activities where they consume time. Define the event's observable criterion and actual authority. “Testing complete” is too vague when failed, blocked or not-run checks may remain. A scheduled event does not record actual acceptance.

Rolling-wave planning gives near-term activities enough detail to execute while later packages retain uncertainty and revisit points. Hidden later work should not vanish from the finish forecast simply because it lacks detailed tasks.

## Application

1. **Define the modeled boundary.** State scope/version, origin, duration unit, status date, current completion evidence and the target/approved finish used for comparison. Separate completed actuals from remaining forecast work.
2. **Build and challenge logic.** Assign stable IDs and all required predecessors, including external inputs and reviews. Resolve cycles and missing links as planning questions; do not delete an inconvenient dependency without evidence.
3. **Calculate the supported network.** Use consistent duration estimates. Apply forward/backward passes or the helper, inspect critical/tied/near-critical work and retain assumptions. A number from an incomplete network is not the full project's forecast.
4. **Reconcile calendars and capacity.** Check scarce-resource overlap, workweeks, holidays, windows, reviewer availability and external constraints. Show any changed sequence or added resources as an explicit scenario until confirmed.
5. **Test changes and alternatives.** Recompute after a changed duration, dependency or resource choice. Compare finish, criticality and remaining uncertainty. Compression of one tied branch alone may not improve finish; faster work may require additional cost or risk decisions.
6. **Deliver the schedule decision.** State the feasible forecast if supported, its variance to the unchanged baseline/target, milestone criteria and unresolved decisions. Baseline approval is a separate event; retain prior approved versions when it changes.

Use [the schedule template](template.md). Quality review checks complete logic, useful estimates, consistent units, feasible resource/calendar assumptions, gate evidence and the distinction between calculated model and authorized commitment.

### When producing a visual

Use the [logic network plus milestone view](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Software network](examples/software.md): forward/backward passes, one-day float and a changed critical duration, with runnable input.
- [Migration network](examples/migration.md): tied branches and a shared-specialist alternative, with runnable input.

## Common Pitfalls

- **Dates before logic:** every task receives a convenient date. Build dependencies and estimates first, then expose the gap to target.
- **Resource-free realism:** one specialist appears on two full-time branches. Sequence work or confirm genuine additional capacity before committing.
- **Calendar smuggling:** seven working-day offsets become seven calendar days. Apply the actual calendars and boundary convention separately.
- **One critical path assumed:** only one of two tied branches is accelerated. Inspect all controlling branches and recompute.
- **Review work hidden in a milestone:** a zero-duration gate conceals days of preparation or waiting. Schedule the work leading to the event.
- **Forecast overwrites baseline:** reporting erases variance. Preserve the approval reference and comparison history.

## References

- [GAO Schedule Assessment Guide](https://www.gao.gov/products/gao-16-89g): schedule quality and critical-path reasoning.
- [Dependency Map](../dependency-map/SKILL.md), [Resource Capacity Plan](../resource-capacity-plan/SKILL.md): handoffs and feasible assignments.
- [Gantt Chart](../gantt-chart/SKILL.md), [Change Request](../change-request/SKILL.md): visualize and authorize changes separately.

Related packages are optional. The model, assumptions, source task table and decision remain portable.
