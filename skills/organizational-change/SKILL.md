---
name: organizational-change
argument-hint: '[affected groups and adoption evidence]'
description: Prepare affected people to adopt new ways of working. Use when project delivery changes roles, processes
  or services and training alone will not establish readiness.
intent: Coordinate impact assessment, readiness, adoption support and reinforcement around the people affected by
  delivery.
type: workflow
theme: transition-and-outcomes
best_for:
  - Coordinate impact assessment, readiness, adoption support and reinforcement around the people affected by delivery.
scenarios:
  - 'Use organizational-change: Coordinate impact assessment, readiness, adoption support and reinforcement around
    the people affected by delivery.'
estimated_time: Depends on evidence and project scope
frameworks: ADKAR lens; change impact assessment; readiness and reinforcement
domain: software-it-project-management
version: 2.1.0
---
# Organizational Change and Adoption

## Purpose

Help affected people use and sustain the project's delivered change. Produce an impact map, targeted adoption actions, readiness evidence and a transition to ongoing ownership. Use when technical delivery changes how people work, who decides, what support is needed or how performance is measured.

This is organizational adoption, not approval of scope/date/cost changes; use Change Request for baseline control. A communication campaign or training completion report can be part of adoption work, but neither proves people can perform the new task under real conditions.

## Input

Bring the future process, affected groups, current work practices, adoption barriers, technical rollout sequence, managers/support roles, training evidence and known readiness criteria. Use supplied context without re-asking. Partial input is enough for a draft impact map; if none is supplied, ask whose work will change and what they will need to do differently.

Example: “Our service-desk migration changes attachment handling and escalation. Staff attended training, but operations doubts they can recover a failed import.” Treat concerns as information to investigate, not proof of resistance or an attitude problem.

## Key Concepts

### Start with observable work change

An impact statement identifies the group, current task, future task, changed tools/roles, consequence and support need. Segment by meaningful work differences such as shift, access, location or responsibility. A single organization-wide message can miss a night-shift operator whose handoff differs from the day team.

Separate necessary behavior from optional preferences. Preserve accessibility, language and support needs when they affect participation. Do not collect or expose sensitive personal judgments merely to fill an adoption scorecard. Use work-relevant evidence and the least personal detail needed for the decision.

### ADKAR as a diagnostic lens

Prosci's ADKAR names Awareness, Desire, Knowledge, Ability and Reinforcement. Use those distinctions to ask why a required behavior is not happening: is the purpose unclear, the incentive or concern unresolved, instruction missing, practical ability blocked, or ongoing support absent? A low-confidence interview impression is not a psychometric diagnosis. This library supplies an original planning application, not a proprietary assessment instrument or certification.

A person may know the process but lack access or time to execute it. More training will not repair that barrier. Conversely, making access available does not establish understanding. Diagnose the specific work condition and test the proposed response.

### Readiness and adoption are different observations

Readiness concerns whether people and support arrangements can perform at transition. Adoption concerns what they actually do after the change. Reinforcement maintains the behavior through usable support, feedback, manager routines and corrected process friction. Metrics should name the cohort, denominator, period and data source; average training attendance can conceal an unprepared critical group.

## Application

### Phase 1: Map impacts and ownership

Input: delivery scope and current/future work. Output: impact table by affected group, material changes, proposed business/change owners and unknowns. Exit when the critical work changes and receiving roles are visible, or an explicit investigation is assigned as proposed. Use Stakeholder Identification to find missing groups; do not assume only named managers are affected.

### Phase 2: Diagnose barriers and design responses

Input: impact map, interviews/observations and existing evidence. Use ADKAR to distinguish the likely barrier, recording hypotheses separately from observed facts. Output: targeted responses with owners, resources and a measure of useful behavior. Exit when each material barrier has an appropriate action or a clearly owned decision; a newsletter is not the default answer to every problem.

### Phase 3: Prepare and demonstrate readiness

Input: response plan, actual environments, role access and support arrangements. Run representative practice or rehearsals, including critical exception paths. Output: readiness evidence and gaps by group. Branch to ready, ready for a bounded supported pilot, or hold/rework according to actual criteria and authority. Technical and security acceptance remain separate; a good training result cannot waive a failed release gate.

### Phase 4: Support the transition

Input: authorized rollout decision, known readiness gaps and accepted support coverage. Provide targeted assistance, feedback routes and clear escalation during the transition. Output: adoption observations, incidents/friction, updated support actions and named receiving owners. Exit when agreed support/transition conditions are met, not simply because the launch date has passed.

### Phase 5: Reinforce and hand off

Input: observed behavior, support demand and remaining gaps. Inspect whether the intended behavior persists, adjust the work system and transfer ongoing measures/actions to the business/service owner. Output: accepted reinforcement and benefit-monitoring handoff. If adoption remains weak, diagnose the barrier again instead of declaring training a success and closing the issue.

Use [the change/adoption template](template.md). Link each action to an observed or hypothesized barrier and a test of whether it helped. Where a related skill is unavailable, retain the group, impact, owner, evidence and next-decision fields directly.

### When producing a visual

Use the [group readiness and adoption matrix](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay pilot adoption](examples/software.md): distinguish a missing recovery demonstration from an operator learning need.
- [Northstar service-desk adoption](examples/migration.md): attendance, role access and demonstrated ability support different conclusions.

## Common Pitfalls

- **Resistance label replaces inquiry:** dissent is attributed to attitude while access or workload is broken. Ask what prevents the required behavior and observe the work.
- **One message for every group:** materially different tasks receive the same support. Segment by actual impact and give each group the relevant path.
- **Attendance equals ability:** a course completion rate masks failure on the real workflow. Observe representative execution and critical exceptions.
- **Change team owns benefits forever:** the project closes without a business owner for sustained behavior. Agree the handoff and ongoing decision cadence before withdrawing support.
- **Adoption overrides acceptance:** enthusiasm is used to justify technical release. Keep security, business and service gates independent and current.

## References

- [Prosci ADKAR](https://www.prosci.com/methodology/adkar): model provenance and the five individual-change outcomes.
- [Stakeholder Identification](../stakeholder-identification/SKILL.md), [Communication Plan](../communication-plan/SKILL.md): affected groups and purposeful feedback.
- [Release and Handover](../release-and-handover/SKILL.md), [Benefits Realization](../benefits-realization/SKILL.md): authorized transition and later outcome evidence.
- [Change Request](../change-request/SKILL.md): separate control of project baselines.
