---
name: sprint-planning
description: "Prepare an evidence-based Sprint plan with a goal, team forecast, capacity, dependencies, and Definition of Done. Use with a Scrum team, not as a manager-imposed commitment."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Sprint Planning

## Purpose

Help a Scrum team form a coherent Sprint Goal and realistic forecast. Use when preparing or facilitating Sprint Planning. The project manager coordinates project constraints and external decisions; the skill does not replace the Product Owner, Scrum Master, or Developers' accountabilities.

## Input

Bring the Product Goal, ordered backlog, current increment, Definition of Done, recent completion evidence, availability, and dependencies.

Example: "Help us plan SSO integration work with an uncertain platform handoff and a support rotation."

If history is missing, use explicit uncertainty rather than borrowing another team's velocity.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Goal, forecast, and plan

The Sprint Goal expresses the coherent objective. Selected backlog items are a forecast of work to achieve it; the Developers create and adapt their plan. The Product Owner brings ordering and value context, while the Scrum Team collaborates on the goal. A manager assigning every task upfront is not the same process.

### Capacity and Definition of Done

Past completion informs the forecast only when comparable to current availability and work. Leave, support, and external dependencies affect feasibility. Definition of Done describes required quality; removing it to fit more scope produces hidden unfinished work.

### Why this works

A goal supports useful tradeoffs when details change. Keeping quality fixed while adjusting feasible scope protects transparency. Velocity is a local planning observation, not an individual productivity target or a cross-team comparison.

## Application

1. Establish the desired Sprint outcome and relevant project constraints with the Product Owner and team.
2. Inspect recent completed work, current availability, support demand, and unresolved dependencies. Use the capacity helper only when hour-based inputs are appropriate.
3. Collaboratively select a coherent set of work that supports the goal. Let Developers assess feasibility and plan delivery.
4. Clarify acceptance, dependencies, and the Definition of Done. Record uncertain handoffs and alternative work without pretending both are committed.
5. Surface project-level funding, release, or cross-team decisions separately; a Sprint forecast does not authorize them.
6. Produce the goal, forecast, key plan, risks, and coordination actions. During delivery, support adaptation with the Product Owner without endangering the goal or quietly reducing quality.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Velocity target:** the team is pressured to increase points rather than deliver usable work. Inspect outcomes and constraints.
- **Manager commitment:** a project date is converted into a promised backlog without team feasibility. Preserve Developer planning authority.
- **Quality traded for count:** testing is moved outside Done to fit more work. Reduce or renegotiate scope instead.
- **Dependency wish:** external work is assumed available despite an unconfirmed handoff. Record the dependency and contingency.
- **Points equal hours:** local sizing is treated as a universal unit. Keep relative estimates and time availability distinct.

## References

- [Scrum Guide: Sprint Planning and accountabilities](https://scrumguides.org/scrum-guide.html)
- [Resource Capacity Plan](../resource-capacity-plan/SKILL.md)
- [Dependency Map](../dependency-map/SKILL.md)
- [Delivery Control Cycle](../delivery-control-cycle/SKILL.md)
- [Retrospective](../retrospective/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
