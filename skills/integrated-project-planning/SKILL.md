---
name: integrated-project-planning
description: "Build a coherent project plan connecting scope, acceptance, estimates, dependencies, capacity, budget, risk, and governance. Use before approving or revising a baseline."
metadata:
  type: workflow
  domain: software-it-project-management
  version: "1.0.0"
---
# Integrated Project Planning

## Purpose

Create a plan whose parts agree with each other. Use after initiation or when a major change invalidates the current delivery model. The output is a decision-ready integrated plan, not a collection of independently optimistic documents.

## Input

Bring the mandate, scope, acceptance criteria, known constraints, resource information, estimates, external commitments, and governance.

Example: "Turn our kickoff outputs into a baseline proposal with realistic capacity and release gates."

Enter at the earliest unresolved decision. Reuse valid existing artifacts rather than repeating kickoff or rebuilding accepted scope.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Integration is consistency

Scope determines required work. Acceptance defines what counts as complete. Estimates and dependencies shape the schedule. Capacity tests whether the sequence is feasible. Costs and risks shape the funding and contingency decisions. Changing one dimension can invalidate another.

### Baseline as decision

A baseline records the agreed comparison point for control. A draft plan or an attractive forecast does not authorize it. Keep the plan's assumptions, exclusions, and uncertainty visible at approval.

### Why this works

An integrated review reveals contradictions such as a release date before security evidence, a shared specialist assigned twice, or a budget excluding operational transition. Iterating the plan is cheaper than hiding those contradictions until delivery.

Tailor detail to the decision horizon. Near-term work needs executable detail; uncertain later work needs honest ranges and revisit points, not fabricated precision.

## Application

1. Confirm mandate and decision rights; do not assume a technical lead is the receiving acceptance authority. Label unconfirmed assignments as proposed; resolve material scope disagreements or present them as choices.
2. Establish scope packages and observable acceptance. Link the charter, WBS, and traceability records.
3. Estimate work with a justified method and documented assumptions. Map internal and external dependencies.
4. Build the schedule, including acceptance and transition gates. Establish accepted immediate operational coverage before go/no-go. Distinguish this from full service handover after verified cutover and stabilization; record the receiver's actual acceptance before closure. Reconcile resources, calendars, and constraints before promoting dates to a baseline proposal.
5. Build cost and funding views from the same scope and sequence. Identify reserve treatment and authorization gaps.
6. Review risks, response costs, stakeholder engagement, communications, and change controls. Rework earlier steps where findings alter feasibility.
7. Use only the supplied project evidence; do not import an illustrative network or facts from a neighboring case. Run a cross-artifact consistency review: common scope version, dates, units, owners, acceptance rules, and approval status.
8. Present feasible options and tradeoffs to the approving authority. Record the actual baseline decision; hand the approved comparison points and unresolved assumptions to the delivery control cycle.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Document bundle as plan:** schedule, budget, and scope disagree. Reconcile their shared assumptions and versions before approval.
- **Date-driven omission:** testing or transition is removed to hit a target without a scope decision. Surface the tradeoff instead.
- **Risk reserve by habit:** a percentage is added without explaining exposure or authority. State the basis and what the reserve covers.
- **Approval of unknowns disguised as certainty:** unresolved inputs disappear from the sponsor summary. Show the decision's conditions and remaining evidence needs.

## References

- [Integrated schedule quality](https://www.gao.gov/products/gao-16-89g)
- [Scope And Wbs](../scope-and-wbs/SKILL.md)
- [Acceptance And Traceability](../acceptance-and-traceability/SKILL.md)
- [Milestone Schedule](../milestone-schedule/SKILL.md)
- [Resource Capacity Plan](../resource-capacity-plan/SKILL.md)
- [Project Budget](../project-budget/SKILL.md)
- [Delivery Control Cycle](../delivery-control-cycle/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
