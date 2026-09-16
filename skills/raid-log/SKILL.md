---
name: raid-log
description: Maintain distinct risks, assumptions, issues and dependencies with evidence and closure rules. Use
  when setting up controls or updating them after new project evidence.
metadata:
  type: component
  domain: software-it-project-management
  version: 2.1.0
  intent: Maintain a dated RAID register whose classification, response, ownership and lifecycle follow the evidence
    rather than optimistic status labels.
  frameworks: RAID; cause-event-effect; issue lifecycle; assumption validation
  best_for: '["Maintain a dated RAID register whose classification, response, ownership and lifecycle follow the
    evidence rather than optimistic status labels."]'
  scenarios: '["Update our linked risks, assumptions, issues and dependencies with owners, triggers and next actions."]'
  estimated_time: Depends on evidence and project scope
---
# RAID Log

## Purpose

Keep four different management questions visible: what might happen, what the plan assumes, what is already wrong, and what usable input is needed from elsewhere. The deliverable is a register with evidence, responses, review points and linked history. A long list without decisions or follow-up is not project control.

Use it when establishing controls or incorporating new facts from delivery, meetings and tests. Use a risk workshop to discover and assess uncertain events; use a dependency map when handoff timing needs deeper analysis. This skill maintains their current state without erasing how it changed.

## Input

Bring the as-of date, affected objectives/baseline, existing IDs, new evidence, ownership and authority records, assessment scales and previous actions. Preserve the source wording where interpretation is uncertain. Ask the smallest classification-changing question: “Has this happened, or is it still possible?”

Example: “The attachment-link problem we listed as a risk has now appeared in rehearsal. Update the log without losing the earlier warning.”

Missing probability, owners, dates or acceptance cannot be filled from examples. A register may contain explicit unknowns and an action to resolve them. Do not set every due date to the next meeting merely because it appears in the source.

## Key Concepts

### Type determines the next action

| Type | Useful statement | Management question | Evidence for closure or transition |
|---|---|---|---|
| Risk | Because of a cause, an uncertain event may affect an objective | What response changes likelihood/consequence or prepares us? | Exposure no longer relevant, realized event linked to issue, or authorized disposition with monitoring as needed |
| Assumption | The plan relies on an unverified premise within a stated boundary | How and by when will we validate it? | Evidence validates/invalidates that premise for the stated conditions; revisit if conditions change |
| Issue | An observed current condition causes a consequence | What resolves or disposes of the problem? | Applicable resolution/retest or explicit authorized acceptance/transfer of a bounded residual obligation |
| Dependency | A provider must supply a usable result to a receiver | What is needed, promised, forecast and accepted? | Receiver acceptance of specified result, not merely upload or a provider's “done” |

One fact may generate linked records. A late supplier file can be a dependency variance and a current blocker issue; possible downstream incompatibility remains a separate risk. Avoid duplicate unconnected entries that assign the same repair twice.

### Assessment is not fabricated measurement

Cause–event–effect phrasing explains exposure. “Vendor risk” does not. Record affected scope, date, cost, quality or service objective, timing/proximity and evidence confidence. If using probability/impact categories, define their meanings and escalation rules first. Multiplication of ordinal scores is a sorting convention; it is not expected loss, probability or a universal comparison across projects.

Quantitative expected monetary value needs defensible probabilities and monetary outcomes. It does not describe the worst case or automatically authorize a reserve. Do not sum overlapping scenarios as independent exposures without analyzing their relationship. A low-ranked threat to a mandatory gate may still require action.

### Owner, action performer and authority are different

The risk owner monitors and coordinates its response. An action performer implements a test or fix. The person authorized to accept residual exposure may be someone else. The PM maintaining the log is not automatically all three. Accepted risk is a decision about exposure; it is not proof the exposure disappeared or permission to ignore a mandatory criterion.

### State changes preserve history

Keep stable IDs and dated updates. When a risk materializes, create or link the observed issue and record which event/population occurred. Preserve any remaining uncertainty about other populations separately. An invalid assumption may force a forecast revision, change request or issue; it is not fixed merely by deleting the assumption.

## Application

1. **Reconcile the evidence cutoff.** Identify what was known at the stated date. Preserve IDs and previous states; distinguish current observations, future forecasts and source claims. Later success cannot be inserted into an earlier review.
2. **Classify and write the item.** Use the type table. State the specific condition, objective and consequence. If two entries describe one underlying event, link them and define their separate purpose. Preserve disagreements as evidence gaps rather than voting a fact into existence.
3. **Assess decision relevance.** Identify exposure timing, severity, confidence and current controls. Apply only agreed scales. Where likelihood is unknown, state it; prioritize based on a justified gate consequence or investigation need without inventing a number.
4. **Choose action and decision route.** Risks need response, trigger, contingency and residual exposure. Assumptions need validation method and expiry/revisit point. Issues need resolution criteria and escalation. Dependencies need provider/receiver, usable condition and separate needed/committed/forecast/actual dates. Identify actual owners or mark proposed/unassigned.
5. **Review effectiveness and changes.** Check whether actions happened and whether they changed the condition. “Mitigation complete” and “risk reduced” require different evidence. Promote time-critical items and unresolved ownership; hand material authority gaps to an escalation brief. Do not silently change a baseline to make the register look healthy.
6. **Close with the right evidence.** Record date, evidence, actual accepting authority where required and any transferred residual work. A planned retest is not a passed retest. Keep superseded, reopened and materialized histories. Produce the [current register and update ledger](template.md) with the next review trigger.

Quality check: a reader can explain why each item is classified, what changes next, who can decide and what would justify closure. A proposed owner/action remains visibly proposed. No dependency is closed by a supplier's assurance alone.

### When producing a visual

Use the [exception board with optional risk grid](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay's four distinct records](examples/software.md): an unavailable environment is an issue while interface compatibility remains uncertain.
- [Northstar risk-to-issue transition](examples/migration.md): preserve M-R01 when M-I002 records actual lost links.

## Common Pitfalls

- **Everything is future risk:** an existing outage gets only a probability score. Create an issue with a resolution criterion and retain genuinely uncertain consequences separately.
- **Assumption without expiry:** an old premise silently supports every new plan. Define its validation event and revisit boundary; reassess downstream commitments when false.
- **Owner by spreadsheet convenience:** every row names the PM. Distinguish coordination, technical work and residual-risk authority; surface unaccepted assignments.
- **Score substitutes for judgment:** a low product score hides a mandatory gate threat. Review the consequence and authority before rank.
- **Closed by action completion:** a file was patched, so the issue is closed. Require current applicable verification and the required acceptance or authorized disposition.
- **History disappears:** a risk is renamed to match today's outcome. Keep the earlier statement and link the new issue, decision and residual exposure.

## References

- [Orange Book risk principles](https://www.gov.uk/government/publications/orange-book) supplies broader risk-governance context; local scales and decision rights still need definition.
- [Risk Workshop](../risk-workshop/SKILL.md), [Dependency Map](../dependency-map/SKILL.md) and [Escalation Brief](../escalation-brief/SKILL.md) provide optional deeper analysis.
- [Meeting Knowledge Graph](../meeting-knowledge-graph/SKILL.md) preserves source history; this register is a current control view, not a replacement for earlier ledgers.
