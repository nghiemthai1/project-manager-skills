---
name: delivery-control-cycle
description: "Run a recurring project control review that reconciles evidence, updates forecasts and RAID, records decisions, and produces actionable status."
metadata:
  type: workflow
  domain: software-it-project-management
  version: "1.0.0"
---
# Delivery Control Cycle

## Purpose

Keep project state coherent as reality changes. Use for a weekly control cycle or a material exception. The workflow coordinates artifacts and decisions; it does not create a new source of truth detached from the team's actual work.

## Input

Bring current and prior status, approved baselines, accepted work, costs, capacity, dependencies, RAID, change requests, and meeting evidence.

Example: "Run the 16 October control review and identify which decisions are needed next."

If a data source is missing or stale, report that limitation and proceed with the evidence available rather than treating it as current.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Compare, explain, decide, follow through

Control compares current evidence with an authorized plan, explains meaningful changes, selects a response, and checks that the response happened. Reporting alone stops before the decision; updating a tracker alone does not prove a result.

### As-of consistency

Costs, progress, and forecasts from different dates may tell different stories without either being false. Align the cut-off where possible and label unmatched dates. Preserve the previous period's record so a later view does not rewrite history.

### Why this works

A recurring cycle catches contradictions across artifacts before they reach decision-makers. Event-triggered exceptions prevent serious issues from waiting for a routine meeting. The same facts support both team coordination and executive reporting at different levels of detail.

## Application

1. Establish the review date, evidence cut-off, current baseline, and outstanding prior actions.
2. Collect actual delivery and acceptance evidence. Distinguish completed work from activity, forecast dates from approvals, and reported status from verified results.
3. Reconcile contradictions and stale inputs. Update linked risks, issues, assumptions, dependencies, and decisions without deleting history.
4. Reassess schedule, resource, cost, and acceptance forecasts using consistent scope and units. Label unresolved feasibility.
5. Identify exceptions outside delegated tolerances and prepare change or escalation decisions. Preserve the baseline until an actual approval changes it.
6. Produce the audience-appropriate status and coordination actions. Sending or updating live systems requires the user's authority; local drafts do not imply external completion.
7. Record decisions and confirmed actions, then check their outcomes at the next review. Invoke an earlier exception review when a release gate or material exposure changes.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Meeting replaces control:** the team reads slides without decisions or follow-up. End with the choices and evidence needed next.
- **Rolling rewrite:** last week's report is edited to match today's truth. Keep dated versions and explain the delta.
- **Stale input blend:** a recent budget and month-old acceptance report are presented as one current picture. Label dates and confidence.
- **Action closed by update:** an owner says "working on it" and the issue closes. Require the relevant completion evidence.
- **Cadence over consequence:** urgent failure waits for Friday. Use event-triggered review.

## References

- [Status Report](../status-report/SKILL.md)
- [Raid Log](../raid-log/SKILL.md)
- [Project Budget](../project-budget/SKILL.md)
- [Project Health Diagnostic](../project-health-diagnostic/SKILL.md)
- [Change Request](../change-request/SKILL.md)
- [Meeting Knowledge Graph](../meeting-knowledge-graph/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
