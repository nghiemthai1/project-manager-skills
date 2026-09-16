---
name: decision-log
description: "Record project decisions with authority, alternatives, rationale, conditions, and supersession history. Use when choices must remain traceable across meetings or changes."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Decision Log

## Purpose

Preserve what was decided, why, by whom, and under which conditions. Use for scope, schedule, funding, architecture-related project choices, or governance decisions. A decision log records authority; it does not manufacture it.

## Input

Bring source notes, options, decision participants, authority, date, rationale, and any conditions or later changes.

Example: "Record CR-001 and explain what it changed without implying security was waived."

If the source contains only a recommendation, record a proposed decision with the approval still pending.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Decision record

A useful record preserves the choice, alternatives considered, rationale, consequences, conditions, and revisit trigger. These fields explain a decision when participants are unavailable later.

DACI distinguishes the Driver coordinating a decision, Approver making it, Contributors supplying expertise, and Informed recipients. Use it when unclear decision roles delay work. It is a role-clarification convention, not proof of authority.

### State and history

Proposed, approved, rejected, deferred, and superseded are different states. Supersession does not erase the earlier decision. A changed forecast does not supersede an approved baseline unless the authorized decision says so.

### Why this works

Alternatives and rationale prevent repeated debates from losing context. Explicit conditions stop a narrow approval from expanding into permission for unrelated actions.

## Application

1. Identify the actual decision question and the evidence available at the time.
2. Separate proposals, recommendations, and decisions. Confirm the approving authority and source before marking approved.
3. Record options and rationale, including the rejected option that a later reader is likely to revisit.
4. State exact scope, conditions, consequences, and implementation owner where evidenced. Keep approval distinct from action completion.
5. Assign a stable ID and link affected scope, schedule, budget, risks, or requirements.
6. For later changes, create a new record and link supersession; retain original wording and context.
7. Capture a revisit trigger where the decision relies on a changing assumption.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Minutes become mandate:** a suggestion in notes is marked approved. Preserve proposed status until evidence supports authority.
- **Approval expands:** funding approval is treated as release permission. State the decision's scope and conditions.
- **Rationale disappears:** only the chosen option remains. Record why alternatives were rejected so later review is meaningful.
- **History overwritten:** a new date replaces the old decision. Link supersession rather than editing history into agreement.

## References

- [DACI decision roles](https://www.atlassian.com/team-playbook/plays/daci)
- [Meeting Knowledge Graph](../meeting-knowledge-graph/SKILL.md)
- [Change Request](../change-request/SKILL.md)
- [Project Charter](../project-charter/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
