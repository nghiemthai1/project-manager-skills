---
name: raid-log
description: "Maintain risks, assumptions, issues, and dependencies with distinct states, evidence, owners, and review actions. Use for ongoing project control."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# RAID Log

## Purpose

Keep uncertain threats, unverified premises, current problems, and required handoffs distinct enough to manage. Use for project setup, control reviews, or changes discovered in meetings. A RAID log is useful only when entries lead to decisions or follow-up.

## Input

Bring project context, existing IDs, new evidence, owners, dates, and agreed risk criteria.

Example: "Update our log: the potential attachment-link problem occurred in rehearsal."

If an item is ambiguous, preserve its wording and clarify whether it is a possibility, premise, present condition, or dependency. Do not assign arbitrary probability or ownership.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Four different management questions

A risk is an uncertain event or condition affecting objectives. An assumption is an unverified premise used in the plan. An issue is a present problem requiring resolution. A dependency is a required deliverable or decision across a boundary. They can be related without being interchangeable.

State a risk as cause, possible event, and consequence. State an assumption with a validation method and consequence if false. Issues need resolution evidence, and dependencies need provider/receiver acceptance.

### Scoring and response

Qualitative probability/impact scales prioritize attention only when their meanings are defined. Multiplying ordinal scores is a ranking convention, not expected monetary loss. Numerical expected value requires justified probabilities and monetary consequences and still does not represent worst-case exposure.

### Why this works

Classification changes the next action. Once an event occurs, create a linked issue and update the risk's state; do not delete the original uncertainty and its response history.

## Application

1. Preserve existing IDs and history. Classify new entries by what is known at the as-of date.
2. Write a specific event, premise, problem, or handoff and link its evidence and affected objective.
3. Record owner, review date, and next action only when known. Flag unassigned items for an ownership decision.
4. For risks, assess probability/impact using the agreed scale and state confidence; choose a response and trigger. For assumptions, record validation and expiry/revisit point.
5. For issues, record resolution and escalation needs. For dependencies, record both parties and acceptance timing.
6. Link changes across categories: an invalid assumption may create a risk or issue; a missed dependency may become an issue.
7. Review the highest-consequence entries first. Close only with evidence that matches the item type, retaining reopened and superseded history.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Everything is a risk:** an outage already happening receives only a future mitigation. Classify it as an issue and assign resolution work.
- **Owner means resolver:** the PM owns the log and is therefore assigned every technical repair. Separate coordination from action ownership.
- **Scoring as measurement:** probability-impact scores are presented as dollar exposure. Keep ordinal ranking and quantitative analysis separate.
- **Closed by optimism:** "should be fine" closes an issue. Require actual resolution or an authorized disposition.
- **History loss:** a materialized risk is overwritten. Link it to the new issue so the prior warning and response remain inspectable.

## References

- [Risk governance principles](https://www.gov.uk/government/publications/orange-book)
- [Risk Workshop](../risk-workshop/SKILL.md)
- [Dependency Map](../dependency-map/SKILL.md)
- [Meeting Knowledge Graph](../meeting-knowledge-graph/SKILL.md)
- [Escalation Brief](../escalation-brief/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
