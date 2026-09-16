---
name: delivery-control-cycle
argument-hint: '[control-period evidence and decisions]'
description: Reconcile project evidence and turn exceptions into decisions. Use for a recurring control review or
  material change in delivery, funding or readiness.
intent: Run a repeatable evidence-to-decision cycle that aligns current forecasts and controls without rewriting
  prior baselines, then verifies actual response outcomes.
type: workflow
theme: delivery-and-decisions
best_for:
  - Run a repeatable evidence-to-decision cycle that aligns current forecasts and controls without rewriting prior
    baselines, then verifies actual response outcomes.
scenarios:
  - Run the weekly evidence-to-decision control process across status, dependencies, risks, changes and escalation
    follow-through.
estimated_time: Depends on evidence and project scope
frameworks: Plan-monitor-control; exception escalation; integrated change control
domain: software-it-project-management
version: 2.1.0
---
# Delivery Control Cycle

## Purpose

Keep the project's current state coherent as reality changes. Produce a dated control packet: reconciled evidence, updated forecasts and RAID, decision requests, actual decisions and follow-up evidence. A meeting, dashboard refresh or tracker update alone is not a completed control cycle.

Use for recurring reviews and event-triggered exceptions. Fit cadence to actual decision lead time and volatility; weekly is an option, not a universal rule. A failed release gate or material exposure may need action before the next scheduled review. This workflow coordinates existing records rather than creating a competing truth source.

## Input

Use review date/cutoff, previous packet, authorized baselines, observed delivery/acceptance, costs, remaining estimates, capacity, dependencies, RAID, changes and decisions. Include prior action evidence and source dates/versions. Missing data remains an explicit limitation; a stale green report does not become current because it is pasted into a new deck.

Example: “Run the 16 October review from these evidence records and identify the decisions needed.”

Preserve source identifiers, versions and paths exactly. Use supplied context before asking. Local draft updates are distinct from changes to live systems, external notifications or spending decisions; follow actual user authorization and project delegation.

## Key Concepts

### Compare, explain, decide and verify

Compare current evidence with an authorized plan; explain material deviation and uncertainty; select a response within actual authority; verify whether it changed the result. Reporting without follow-through leaves the problem untouched. A response action marked complete does not prove the issue resolved.

### Cutoff and configuration are part of the fact

Costs, progress and tests may refer to different dates, scope or versions. Align them when possible; otherwise disclose each boundary and which combined conclusions are unavailable. A previous version's pass needs applicability review after change. Do not roll an old acceptance forward automatically.

### Current views and historical records coexist

Update a current forecast when expectations change, even before a baseline decision. Update the authorized baseline only after an actual bounded approval. Retain earlier reports and immutable meeting ledgers. A current-state summary can link a later decision without rewriting what was known at the earlier cutoff.

### Exceptions use authority, not colors alone

Use actual tolerances and gate rules. A local correction within delegation can proceed without a fictional sponsor approval step. A scope/funding/date change beyond authority needs its actual decision route. Unknown rules are a gap to resolve, not permission to select convenient thresholds.

## Application

### Phase 1 — Establish the review basis

**Inputs:** previous packet, baseline/decision history and evidence list. Fix the review purpose, cutoff, current comparison and prior open decisions/actions. Distinguish date target, forecast and baseline.

**Outputs:** source inventory with date/version/owner, current authority state and carry-forward items. Mark stale/missing sources.

**Exit:** the reviewer knows what period and configuration each conclusion can describe. Continue with a partial packet if useful; do not invent missing data to align cutoffs.

### Phase 2 — Reconcile facts and controls

**Inputs:** actual delivery, test/acceptance, costs, resource and handoff evidence. Resolve contradictions against primary records or retain them as explicit findings. Classify current issues, future risks, assumptions and dependencies separately. Check prior actions for execution and effectiveness.

**Outputs:** evidence-linked current RAID and acceptance states, contradiction log and dated deltas. Preserve IDs and previous entries; a materialized risk links to its issue.

**Exit:** material claims are supported or visibly unresolved. The packet cannot say “accepted” solely because a task owner wrote “done.”

### Phase 3 — Reforecast and diagnose

**Inputs:** reconciled scope, actuals and remaining work. Inspect schedule sequence/calendars/resources, cost/commitments/funding and acceptance evidence. Use suitable helpers only when their input assumptions fit. Do not infer date slip from monetary schedule variance or turn reserve into automatic spend permission.

**Outputs:** current forecast with method/assumptions, dimensional consequence and confidence, and alternatives needing analysis. A failed gate remains independent of favorable aggregate progress.

**Exit:** the next decision is clear even if final cost/date remains uncertain. Route causal ambiguity to a focused diagnostic; immediate established consequences need not wait for perfect unrelated data.

### Phase 4 — Decide and update within authority

**Inputs:** exceptions, options and actual delegation. Use change requests or escalation briefs for choices beyond the team; handle authorized local corrections proportionately. Record recommendation, actual approval, conditions and implementation separately.

**Outputs:** decision/action register and prospective changes to affected current plans. Historical reports retain their cutoff/baseline. No silence or meeting attendance becomes approval.

**Exit:** each material exception has an actual decision or an explicit owner/authority/evidence gap. A pending choice stays pending; do not force every row green to close the review.

### Phase 5 — Communicate and verify the response

**Inputs:** current evidence and actual decision state. Produce the requested audience-specific status using consistent facts. Prepare messages or update live records only within authorization. Set the next routine review and earlier event triggers based on the response's useful decision window.

**Outputs:** the [control packet](template.md), recipient/action handoffs and verification checkpoints. An action closes with its relevant result or authorized disposition, not “working on it.”

**Exit:** the next cycle can test whether the response happened and worked. If it did not, reopen or reconsider with new evidence; retain the earlier promise and explanation instead of rolling it forward invisibly.

### When producing a visual

Use the [control review artifact pack](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay review and follow-through](examples/software.md): original funding exposure remains in the earlier report after a later change.
- [Northstar linked control cycles](examples/migration.md): plan approval, failed restore, go, handover and closure stay separate dated events.

## Common Pitfalls

- **Slides replace control:** status is read aloud but no decision or verification follows. End with bounded choices and next evidence.
- **Stale blend:** current costs and old-version tests are presented as one current state. Show cutoffs/configurations and review applicability.
- **Rolling rewrite:** last period's report is edited to match today's truth. Append a current view and preserve the old record.
- **Action closes the issue:** “patch sent” ends a failed acceptance record. Require applicable test/acceptance or explicit authorized disposition.
- **Cadence beats consequence:** a failed gate waits for Friday. Use the exception trigger before the useful decision window closes.
- **Every correction escalated:** routine work inside delegation becomes bureaucracy. Identify the actual boundary and act proportionately.

## References

- [RAID Log](../raid-log/SKILL.md), [Project Budget](../project-budget/SKILL.md), [Acceptance and Traceability](../acceptance-and-traceability/SKILL.md) supply reconciled controls.
- [Project Health Diagnostic](../project-health-diagnostic/SKILL.md), [Change Request](../change-request/SKILL.md), [Decision Log](../decision-log/SKILL.md) and [Status Report](../status-report/SKILL.md) support decisions and communication.
- [Meeting Knowledge Graph](../meeting-knowledge-graph/SKILL.md) retains evidence/history. All handoffs are optional packages; the fields and gates above remain usable alone.
