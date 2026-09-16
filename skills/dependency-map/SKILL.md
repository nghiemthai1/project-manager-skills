---
name: dependency-map
description: "Map cross-team deliverables, provider and receiver commitments, delivery gaps, and escalation actions. Use for blocked or tightly coupled workstreams."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Dependency Map

## Purpose

Make the handoffs between teams explicit enough to coordinate. Use when one team's delivery depends on another team, vendor, or approval body. A dependency map is not a substitute for an integrated schedule, and it does not establish critical-path float from date comparisons alone.

## Input

Bring the workstreams, exchanged deliverables, providers, receivers, acceptance criteria, needed-by dates, expected-delivery dates, and confirmation evidence.

Example: "Platform expects the audit interface on 22 October, but integration needs it on 20 October. Build the dependency record and next actions."

If only one side has supplied a date, mark the other side unconfirmed. A desired delivery date is not a provider commitment.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### The handoff contract

A useful dependency states what crosses the boundary, who provides and accepts it, what usable means, and the timing needed on each side. "Waiting on Platform" conceals too much to manage.

### Local margin versus schedule float

Local delivery margin is needed-by minus expected-delivery using a declared calendar. A negative margin identifies a gap to resolve. Total float requires the integrated activity network and its scheduling assumptions. A dependency can have positive local margin while lying on a resource bottleneck or critical chain; the date gap alone cannot decide that.

### Why this works

Provider and receiver dates expose disagreement early. Acceptance criteria prevent a nominally delivered interface from being unusable. Review triggers keep the record connected to changed reality rather than a static diagram.

Use a simple table for a few handoffs. Add a Mermaid graph when it clarifies multiple teams or parallel chains. Graph arrows show direction of delivery; they do not prove causality beyond the recorded dependency.

## Application

1. Define the coordination boundary. Capture deliverables crossing it, not every internal task.
2. Assign a stable ID and record provider, receiver, deliverable, acceptance, expected date, needed-by date, and evidence date. Unknown ownership stays unknown.
3. Reconcile the two dates with both sides. Label forecasts, targets, and commitments accurately.
4. Calculate local margin only with known dates and a stated calendar. Identify negative or uncertain margins without calling them float.
5. For each material gap, propose resequencing, a smaller acceptable handoff, additional capacity with evidence, or escalation. Record who can decide and what must be confirmed.
6. Mark done only when the receiver accepts the handoff. Preserve rejected deliveries and changed dates in history.
7. Review at the project's coordination cadence and on material date/scope changes. Use integrated schedule analysis when making a final-date claim.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Ownerless arrow:** "vendor to engineering" has no named accountable contacts. Follow-up stalls. Record provider and receiver responsibility or escalate the missing assignment.
- **Delivered but unusable:** sending a file is treated as acceptance. Downstream work still cannot start. Define and record receiver validation.
- **Float by subtraction:** a two-day delivery gap is called a two-day critical-path delay. The final-date claim is unsupported. Show local margin and request network analysis.
- **Stale agreement:** last month's promise survives a scope change. Reconfirm on change and retain the old value in history.
- **Diagram overload:** internal subtasks obscure cross-team decisions. Keep detailed tasks in their own plan and map only relevant handoffs.

## References

- [Critical-path scheduling requirements](https://www.gao.gov/products/gao-16-89g)
- [Milestone Schedule](../milestone-schedule/SKILL.md)
- [Raid Log](../raid-log/SKILL.md)
- [Escalation Brief](../escalation-brief/SKILL.md)
- [Release Readiness](../release-readiness/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
