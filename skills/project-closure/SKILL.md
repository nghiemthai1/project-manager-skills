---
name: project-closure
argument-hint: '[closure evidence and remaining obligations]'
description: Reconcile delivery, finances and continuing obligations. Use when preparing normal project closure
  or authorized termination with explicit acceptance and ownership.
intent: Prepare and record a defensible project closure or termination with accepted deliverables, reconciled costs,
  owned residual obligations and a continuing benefit-review plan.
type: workflow
theme: transition-and-outcomes
best_for:
  - Prepare and record a defensible project closure or termination with accepted deliverables, reconciled costs,
    owned residual obligations and a continuing benefit-review plan.
scenarios:
  - Determine whether we can close the project given acceptance, financial obligations, residual work and the benefits
    handoff.
estimated_time: Depends on evidence and project scope
frameworks: Closure assurance; financial reconciliation; residual transfer; benefits handoff
domain: software-it-project-management
version: 2.1.0
license: MIT
---
# Project Closure

## Purpose

End the temporary project's responsibilities without losing work, money, evidence or ongoing duties. Produce a closure-readiness assessment and report with the actual authority decision. Deployment, spent budget or an empty task board is insufficient evidence of closure.

Use after delivery/service transfer or when considering early termination. A project may close while benefits are still measured if responsibility and review are explicitly transferred. Conversely, delivered functionality does not erase open invoices, unaccepted service duties or contractual obligations.

## Input

Use charter/scope, original and revised baselines, acceptance/release/handover records, final actuals, accruals/commitments, residual items, contract obligations, lessons and benefit ownership. Include closure authority and criteria. Preserve exact IDs and source boundaries; do not borrow another case's financial reconciliation or clean residual register.

Example: “Prepare closure after operations handover, showing what remains with continuing owners.”

A recorded closure approval is a fact even when its supporting packet is missing. Report that actual decision and the evidence gaps separately; do not erase the decision or invent underlying proof. If closure has not occurred, provide a readiness recommendation rather than label the project closed.

## Key Concepts

### Closure route changes the evidence

Normal completion reconciles what was accepted against authorized scope. Termination explains why work stops, what was delivered or abandoned, which commitments remain, and how data/assets/service exposure will be handled. An early stop is not automatically failure, and sunk spending alone is not a reason to continue.

No generic cancel instruction terminates supplier contracts, removes access or deletes project data. Those actions follow actual authority, obligations and retention rules. Unknown requirements remain gaps for the proper owner; do not fabricate policy.

### Residual obligations need accepted disposition

Each material item must be completed with evidence, transferred with receiving-owner acceptance, accepted as bounded residual exposure by actual authority, or left as a closure blocker under the project's rules. A proposed owner in a spreadsheet is not an accepted transfer. Record work, resources, timing, source and escalation after the project team leaves.

### Final cost is a reconciled view

Separate incurred actuals, accrued/unpaid amounts, remaining unincurred commitments, estimated closeout work, released funds and unknowns. Avoid counting an invoice both in actuals and again as an additional obligation. A final budget or EAC is not actual spend. A project can have approved closure while financial processing continues with explicit accepted ownership; do not call accounts settled without evidence.

### History explains the result

Compare actual delivery against original and approved revised scope/date/cost, showing the decisions that changed them. “On time to the final baseline” and “on time to the original commitment” are different statements. Benefits promised at initiation may remain unobserved at closure; a future review is a continuing responsibility, not realized value.

## Application

### Phase 1 — Establish route and decision boundary

**Inputs:** mandate, current state and closure/termination request. Identify actual authority, applicable criteria and whether a closure decision already exists. For termination, identify consequences of stopping as well as continuing.

**Outputs:** route-specific checklist and evidence inventory, with missing policies/records explicit.

**Exit:** the reviewer can distinguish proposed closure, actual approval and actions the approval permits. A technical lead is not automatically service or closure authority.

### Phase 2 — Reconcile scope and responsibility

**Inputs:** authorized scope/history, actual results and receiving acceptance. Map each deliverable to accepted, partially accepted, not delivered or unknown, with exact decision scope. Review full service handover and any interim responsibilities.

**Outputs:** outcome/baseline bridge and residual-disposition register. For termination, include unfinished work, data/assets, service safeguards and supplier/customer commitments as applicable.

**Exit:** material responsibilities have evidenced disposition or remain named blockers. A sent document, planned handover or silent recipient does not close the transfer.

### Phase 3 — Reconcile financial and commercial closeout

**Inputs:** actual cost ledger, accrual/commitment detail and remaining obligations. Verify cutoff, scope/currency, duplicates and unknowns with the actual finance/commercial owners. Distinguish approved release of funds from an assumed budget balance.

**Outputs:** financial bridge, outstanding obligation owners and evidence needed for settlement. No final actual is inferred from BAC or EAC.

**Exit:** finance is demonstrably reconciled or remaining processing is explicitly accepted under the actual closure rules. Missing invoices cannot be treated as zero obligations.

### Phase 4 — Transfer learning, benefits and evidence

**Inputs:** results, decision history, contextual lessons, ongoing benefit measures and actual retention/access rules. Identify who accepts each continuing review and what evidence they will use.

**Outputs:** benefit-review agreement, usable evidence index and bounded lessons/adoption proposals. Preserve original records and unknown metadata. Archive means maintain authorized access/retention, not automatically delete working files.

**Exit:** the receiving owners can find and use what they accepted. An untested recommendation is not field-proven learning, and a forecast benefit is not an observed result.

### Phase 5 — Decide and verify the boundary

**Inputs:** the [closure packet](template.md) and unresolved conditions. Recommend approve, conditional closure only where actual rules permit, or defer/hold with exact gaps. Record the authority's actual choice, effective scope and continuing obligations.

**Outputs:** closure/termination report, accepted residual register and permitted resource-release actions. Execute external changes only under user authorization and actual decision scope.

**Exit:** what ended and what continues are explicit. If the project is already approved closed but supporting evidence is missing, preserve that fact and identify assurance gaps/continuing work; do not retroactively manufacture a complete packet.

### When producing a visual

Use the [closure evidence and residual transfer matrix](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the project source’s evidence and uncertainty in the graphic.

## Examples

Optional worked applications:

- [Relay closure record](examples/software.md): B2 is not final actual cost, and the benefit review remains later.
- [Northstar closure record](examples/migration.md): phased baseline history, accepted service transfer and missing underlying evidence coexist honestly.

## Common Pitfalls

- **Launch equals closure:** service, finance and residual work vanish. Inspect each closure boundary separately.
- **Transfer by naming:** operations gets a task without acceptance or resources. Obtain a bounded receiving decision or keep the item unresolved.
- **EAC becomes final spend:** a forecast fills an absent ledger. Reconcile incurred/remaining obligations and label unknowns.
- **Benefits declared early:** targets become achievements when the team disbands. Transfer measurement and report only observed outcomes.
- **History sanitized:** the final plan is presented as the original promise. Retain the original-to-revised-to-actual bridge.
- **Approval erased by missing paperwork:** a real closure decision is denied because attachments are absent. Report the decision and the assurance gap separately.
- **Termination deletes obligations:** stopping work is treated as automatic contract/access/data disposal authority. Identify and follow actual obligations and decision scope.

## References

- [Release and Handover](../release-and-handover/SKILL.md), [Project Budget](../project-budget/SKILL.md) and [Decision Log](../decision-log/SKILL.md) supply optional outcome/authority records.
- [Lessons Learned](../lessons-learned/SKILL.md) and [Benefits Realization](../benefits-realization/SKILL.md) preserve learning and ongoing outcome measurement. Use the described handoff fields if these packages are unavailable.
