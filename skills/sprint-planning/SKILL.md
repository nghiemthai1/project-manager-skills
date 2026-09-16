---
name: sprint-planning
argument-hint: '[Sprint Goal, backlog, and capacity context]'
description: Prepare a coherent Sprint Goal and feasible team forecast. Use when supporting Scrum Sprint Planning
  with capacity, dependencies and required quality made explicit.
intent: Help a Scrum team prepare a Sprint Goal, selected-work forecast and delivery plan while preserving team
  accountabilities, quality and separate project authority.
type: component
theme: delivery-and-decisions
best_for:
  - Help a Scrum team prepare a Sprint Goal, selected-work forecast and delivery plan while preserving team accountabilities,
    quality and separate project authority.
scenarios:
  - Help the Scrum team form a coherent Sprint Goal and feasible selected-work forecast from backlog and availability.
estimated_time: Depends on evidence and project scope
frameworks: Scrum Sprint Planning; Sprint Goal; Definition of Done; capacity
domain: software-it-project-management
version: 2.1.0
---
# Sprint Planning

## Purpose

Help a Scrum team prepare a coherent goal and a feasible forecast. The output is a planning packet for the team, with selected work, completion evidence, dependencies and coordination actions. The project manager contributes project constraints and external decisions without replacing the team's planning accountabilities.

First confirm the team actually uses Scrum. A two-week migration checklist is not automatically a Sprint. If it does not, use a delivery/rehearsal-cycle plan and retain the practical capacity and acceptance checks without inventing Scrum roles or claiming Scrum compliance.

## Input

Use Product Goal/value context, ordered backlog, current Increment, Definition of Done, item acceptance criteria, recent actual completion, availability, support demand and external constraints. Supplied context answers the relevant questions; do not repeat it. Missing history means a less confident forecast, not permission to borrow another team's velocity.

Example: “Prepare the next SSO Sprint with an uncertain platform handoff and a support rotation. Show what the team still needs to decide.”

Preserve exact backlog and dependency IDs. Distinguish a preparation draft from an actual team-selected Sprint Backlog. Do not label proposed goals, assignments or item selections committed merely because they appear in a template.

## Key Concepts

### Why, what and how

In Scrum, planning connects a Sprint Goal, the work Developers select with Product Owner discussion, and their delivery plan. Developers own that plan and adapt it; the Product Owner provides value and ordering context. The Scrum Master supports the framework and team effectiveness. The PM's coordinating role grants no substitute authority over these accountabilities.

The goal expresses a useful objective; selected items are a forecast. Quality does not decrease to fit a target. Scope can be clarified and renegotiated with the Product Owner without endangering the goal. A Sprint ending is not a project release authorization.

### Capacity tests the work, not a points quota

Inspect actual availability, support, leave, review/test bottlenecks, access and external waits. If hour-based information is useful, subtract disjoint deductions and count support once. An aggregate spare total can hide the only qualified person's overload. Capacity does not prove all selected work can be sequenced or completed.

Relative estimates are local planning information; there is no universal conversion from points to hours. Compare recent completed work only when team, work boundary and conditions are sufficiently similar. Do not turn a mean velocity into a guaranteed minimum, target individual output or extrapolate a percentage increase because the project is late.

### Done, acceptance and release answer different questions

The Definition of Done provides the quality boundary for the Increment. Item criteria describe the intended behavior. Project domain acceptance and release authorization may add separate decisions. Record how they relate rather than weakening Done or assuming one substitutes for all others.

When a dependent input is unconfirmed, identify useful work that genuinely remains feasible and what it proves. A mock may support a bounded test but not final integration acceptance. Do not call both the primary and fallback paths fully selected if capacity only supports one.

## Application

1. **Confirm applicability and preparation state.** Identify the actual team/accountabilities, planning period and supplied constraints. If this is preparation, label the output proposed and leave selection to Developers. If Scrum is not in use, explain the alternate cycle-plan framing and proceed with that useful artifact.
2. **Frame one coherent outcome.** Connect a candidate goal to useful change in capability or validated learning that supports delivery. “Complete all tickets” is not a reason for the Sprint. Ask what a user/reviewer could inspect at the end and why it matters. The team finalizes the actual goal through its process.
3. **Inspect feasibility.** Compare relevant completion history with current availability and known demand. Identify skill/access bottlenecks, dependencies and prerequisite evidence. Carry incomplete prior work as remaining work to inspect and reorder, not an automatic extra commitment. Avoid an invented utilization haircut or point-to-hour ratio.
4. **Prepare a candidate selection.** For each item, show goal contribution, applicable criteria/Done, dependencies, estimate basis and uncertainty. Distinguish feasible candidates, conditional work and deferred/unselected work. Ask Developers to choose and plan a coherent feasible set; do not allocate every task from the PM role.
5. **Make uncertainty actionable.** Define which input/decision is needed, by whom, the usable condition and a useful review point. Identify a bounded alternate slice if the dependency fails; keep the forecast conditional until evidence supports it. Mandatory project scope excluded from this Sprint remains project work unless separately changed.
6. **Check the plan and handoffs.** Use the [planning template](template.md). Can the team describe the goal, evidence of Done, first feasible work and response to the main uncertainty? Route funding, date, supplier and release decisions to their actual authorities. Record actual team selections separately from recommendations.
7. **Adapt with evidence.** During delivery, use observed work and changed inputs to inspect progress toward the goal. Revise the delivery plan and discuss scope with the Product Owner as appropriate; do not silently lower quality. If the goal becomes obsolete, the Product Owner holds Sprint-cancellation authority. Record the actual decision rather than treating the PM's preference as cancellation.

Quality check: the artifact supports a useful outcome, makes conditional work visible and does not convert project pressure into team guarantees. An empty history field is an uncertainty; a failed requirement remains work, even if many small tasks are complete.

### When producing a visual

Use the [sprint forecast board](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay planning packet](examples/software.md): one person's overload and an unconfirmed audit handoff constrain the candidate forecast.
- [Northstar applicability and rehearsal plan](examples/migration.md): hybrid delivery is not relabeled Scrum; an optional Scrum application preserves the same evidence boundary.

## Common Pitfalls

- **Velocity target:** a demanded points increase substitutes for feasibility. Compare actual available capability and useful completed outcomes.
- **Manager commitment:** a project date becomes a guaranteed item list without team selection. Keep the preparation draft and team forecast distinct.
- **Testing next Sprint:** removing quality work makes the count fit. Reduce selected scope or revisit the goal; preserve Done.
- **Fallback doubles capacity:** both blocked work and alternate work are counted as fully deliverable. Model the branch and its trigger explicitly.
- **Unselected means descoped:** required project work disappears because it did not fit this Sprint. Keep it in the project boundary and route any scope change separately.
- **Demo means release:** a visible increment is treated as security/service/go approval. Retain the actual required decisions.

## References

- [Scrum Guide](https://scrumguides.org/scrum-guide.html) defines Scrum accountabilities and planning. The capacity tables and project handoffs here are contextual practices, not extra Scrum rules.
- [Resource Capacity Plan](../resource-capacity-plan/SKILL.md), [Dependency Map](../dependency-map/SKILL.md) and [Delivery Approach Advisor](../delivery-approach-advisor/SKILL.md) are optional preparation aids.
- [Delivery Control Cycle](../delivery-control-cycle/SKILL.md) and [Retrospective](../retrospective/SKILL.md) receive project coordination and improvement evidence.
