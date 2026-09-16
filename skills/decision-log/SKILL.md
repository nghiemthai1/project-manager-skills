---
name: decision-log
argument-hint: '[decision, authority, rationale, and conditions]'
description: Record the exact choice, authority, rationale and conditions. Use when project decisions need traceable
  history across meetings, changes or conflicting recollections.
intent: Create durable decision records that distinguish proposals from authority and preserve bounded approvals,
  implementation state and later supersession.
type: component
theme: delivery-and-decisions
best_for:
  - Create durable decision records that distinguish proposals from authority and preserve bounded approvals, implementation
    state and later supersession.
scenarios:
  - Record what was actually decided, by whom, why, under which conditions, and what earlier decision it supersedes.
estimated_time: Depends on evidence and project scope
frameworks: DACI; decision records; option analysis
domain: software-it-project-management
version: 2.1.0
---
# Decision Log

## Purpose

Preserve what was decided, by whom, on what evidence, and within which limits. The output is a decision register plus enough detail for a future reader to understand the consequential choice. It prevents a suggestion from becoming a mandate and a narrow approval from expanding into unrelated permission.

Use for baseline, funding, scope, delivery approach and acceptance-related choices. A log records decisions; an escalation brief develops a choice, and a change request coordinates its impacts and implementation. A technical architecture record may supply deeper technical rationale while this log records project consequences and authority.

## Input

Use the question, dated source notes, options, actual participants/decider, delegated authority, stated rationale, conditions and affected artifacts. Include previous decision IDs and any later contrary evidence. Ask for missing authority or wording only when it changes classification; otherwise draft a record with the gap explicit.

Example: “Record CR-001 without making its funding approval look like launch permission.”

Decision IDs, baseline IDs, versions and evidence paths are literal data. Copy them exactly, including case, punctuation and spacing; `V-D1` must not become `V-D 1` during formatting. Check each supplied reference against its source before delivery and avoid global prose substitutions across the record.

Do not manufacture a debate, consensus or rejected option from what seems sensible after the fact. Analysis can propose alternatives; the historical record must say which alternatives were actually documented and which are later reconstruction.

## Key Concepts

### DACI organizes a decision, not its legitimacy

The Driver coordinates the work; the Approver makes the bounded choice; Contributors provide relevant expertise; Informed recipients need the outcome. Use DACI where coordination is unclear. A person's appearance in a role table does not establish their actual delegation. Separate decisions when funding, security, business acceptance and release require different authorities instead of naming one universal approver.

### Choice state and implementation state are separate

| Decision state | Meaning | What it does not establish |
|---|---|---|
| Proposed | A choice is requested or recommended | Approval or permission to execute |
| Approved, with stated conditions | Actual authorized choice for defined scope | Conditions fulfilled, implementation complete, or other authorities' acceptance |
| Rejected | Actual authority declined the specified option | Every alternative permanently forbidden |
| Deferred | Decision intentionally postponed with reason/revisit basis | Approval by absence of response |
| Superseded in specified respects | A later decision replaces part or all of this choice | The earlier decision never existed |

Track implementation as not started/in progress/verified or unknown with its own evidence. If conditions delay effectiveness, state that explicitly; if approval is effective now with later obligations, record those obligations. Do not guess which interpretation applies.

### Rationale needs contemporaneous boundaries

Record the evidence available at decision time, tradeoff, rejected option if documented, assumptions and revisit trigger. A later failure may justify reconsideration but does not prove earlier participants knew it. Preserve uncertainty and dissent rather than smoothing history into unanimity.

Partial supersession matters: a new funding baseline can replace the cost provision while leaving the original release criteria and date unchanged. Identify each affected field. A changed forecast alone never supersedes an authorized baseline.

## Application

1. **Extract the actual question and source.** Keep IDs, date and exact decision scope. Separate quotations/observations from interpretation. Where source attribution is uncertain, record that uncertainty; speaker confidence and approval authority are different questions.
2. **Classify the act.** Is the source a suggestion, recommendation, actual decision, conditional decision or implementation update? Confirm actual authority through the supplied mandate/delegation. A meeting participant saying “sounds good” may not establish approval of every implication.
3. **Capture choice and rationale.** State options and tradeoffs actually evidenced. Mark undocumented alternatives or rationale as unknown; if adding present-day analysis, label it separately. Record conditions, exclusions, risks accepted and assumptions requiring review.
4. **Map consequences precisely.** List affected scope/date/cost/acceptance/resource artifacts and fields. Explain what remains in force. Name implementation owners only where accepted. Separate approval date, effective date and expected implementation date when they differ.
5. **Link history.** Retain the earlier record and append the new one. State which provisions supersede which IDs, and which coexist. Correct transcription errors transparently without rewriting earlier meeting ledgers to match later decisions.
6. **Check action and review.** Use the [template](template.md) to record implementation evidence and open conditions. A missed assumption or review trigger opens a reconsideration; it does not automatically authorize reversal. Communicate the actual decision only within existing authorization and record recipient acknowledgment separately.

Quality check: a reader can answer who had authority, what changed, when it took effect, what did not change, what evidence supported it and what remains unimplemented. If any answer is missing, preserve the gap instead of turning an incomplete record into a confident approval.

### When producing a visual

Use the [decision chronology or option map](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the project source’s evidence and uncertainty in the graphic.

## Examples

Optional worked applications:

- [Relay's separate scope/funding/date decisions](examples/software.md): CR-001 does not contain D-004 or security acceptance.
- [Northstar's partial supersession](examples/migration.md): M-CR02 replaces specified baseline provisions while recovery and reconciliation remain required.

## Common Pitfalls

- **Minutes become mandate:** a participant's proposal becomes “approved.” Restore proposed status and identify the actual decision evidence needed.
- **Funding means go:** cost authorization is treated as release clearance. Separate the decision boundaries and required acceptances.
- **Rationale invented later:** a plausible story replaces missing source reasoning. Mark it retrospective analysis, not the recorded deliberation.
- **Supersession erases everything:** changing budget deletes date and acceptance history. Name the exact fields replaced and preserve remaining provisions.
- **Approval means completion:** an authorized change is marked implemented. Require execution/verification evidence and track open conditions separately.
- **Latest truth rewrites old ledgers:** earlier minutes are edited to match a later choice. Append a dated decision and current-state view, preserving original evidence.

## References

- [Atlassian DACI](https://www.atlassian.com/team-playbook/plays/daci) describes decision coordination roles.
- [Project Governance](../project-governance/SKILL.md), [Change Request](../change-request/SKILL.md) and [Meeting Knowledge Graph](../meeting-knowledge-graph/SKILL.md) are optional authority, implementation and evidence handoffs.
