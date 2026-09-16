---
name: delivery-approach-advisor
description: "Choose predictive, agile, or hybrid delivery based on uncertainty, feedback, dependencies, and governance. Use when starting or changing a project approach."
metadata:
  type: interactive
  domain: software-it-project-management
  version: "1.0.0"
---
# Delivery Approach Advisor

## Purpose

Recommend a delivery approach that fits the work and the organization's decision constraints. Use at initiation or when current practices obstruct learning or control. The result is a tailored operating approach, not a declaration that one methodology is always superior.

## Input

Bring the desired outcome, uncertainty, delivery constraints, feedback access, external dependencies, and approval requirements.

Example: "We have a fixed migration window but uncertain data quality. Should this project be agile or predictive?"

Do not ask the requester to pick a methodology before understanding the problem.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Three independent questions

How uncertain is the work? How quickly can useful feedback arrive? Which commitments must be controlled? These dimensions often point to different practices within one project.

Predictive planning fits sufficiently understood work with stable interfaces and expensive coordination. Its value is explicit sequencing and control; its weakness is false certainty when discovery is incomplete. Agile delivery fits work where usable increments and frequent feedback reduce uncertainty. Iterations without accessible feedback offer little learning. Hybrid delivery deliberately uses adaptive learning within controlled boundaries, such as rehearsals inside an approved migration window.

A fixed deadline does not make requirements known. A regulated gate does not prohibit incremental testing. A two-week meeting cadence does not establish Scrum.

### Why this works

Choosing practices from the actual uncertainty avoids methodology labels as substitutes for decisions. Explicit boundaries also show which changes a team may make and which require sponsor approval.

## Application

1. Read supplied context, then ask the largest missing discriminator: uncertainty, feedback availability, or constraints. Ask one material question at a time, normally no more than three to five.
2. Compare predictive, agile, and hybrid options against those conditions. Include the cost of delayed feedback and the cost of uncontrolled change.
3. Recommend an approach and identify where each practice applies: discovery/rehearsal, delivery increments, governance, and release approval.
4. Define the feedback cadence, planning horizon, baseline boundaries, decision rights, and measurable exit conditions.
5. Identify an early trial and evidence that would trigger a change in approach. Keep the recommendation adaptable without making every commitment provisional forever.
6. Produce the recommendation and hand it to project kickoff and integrated planning.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Agile by calendar:** standups and sprints are added without usable increments or feedback. Define what each iteration learns or delivers.
- **Fixed date means fixed knowledge:** uncertainty is hidden to satisfy a deadline. Preserve the constraint while investigating the unknowns and presenting tradeoffs.
- **Hybrid as ambiguity:** nobody knows which scope changes need approval. State decision boundaries explicitly.
- **Methodology as identity:** a team defends a label despite poor outcomes. Agree on evidence for changing practices before the trial.

## References

- [Scrum framework and accountabilities](https://scrumguides.org/scrum-guide.html)
- [Project Kickoff](../project-kickoff/SKILL.md)
- [Integrated Project Planning](../integrated-project-planning/SKILL.md)
- [Sprint Planning](../sprint-planning/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
