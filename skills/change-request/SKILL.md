---
name: change-request
argument-hint: '[proposed change and current baseline]'
description: Assess a proposed change and preserve exact approval boundaries. Use when scope, date, cost or acceptance
  changes cross agreed project control limits.
intent: Develop a proportionate change assessment with integrated impacts, feasible alternatives, bounded authority
  and verified prospective baseline updates.
type: component
theme: delivery-and-decisions
best_for:
  - Develop a proportionate change assessment with integrated impacts, feasible alternatives, bounded authority
    and verified prospective baseline updates.
scenarios:
  - Assess a specific proposed change to the approved scope and date, compare impacts and prepare the authorization
    record.
estimated_time: Depends on evidence and project scope
frameworks: Integrated change control; impact analysis; configuration history
domain: software-it-project-management
version: 2.1.0
license: MIT
---
# Change Request

## Purpose

Make a proposed change an informed choice before it becomes an implicit commitment. Produce a request, integrated impact assessment, decision record and implementation verification plan. Use when a request crosses the actual baseline or delegated control boundary.

Routine refinement within agreed authority does not need an invented change board. Record the relevant local decision and update plans proportionately. A forecast update also does not automatically change the baseline: report reality promptly while keeping authorization distinct.

## Input

Use current baseline/version/decision, requester and reason, exact change, affected scope/requirements, timing, estimates, capacity, dependencies, acceptance and operating obligations. Include actual delegation/tolerance rules and previous related requests. If the boundary is unclear, identify it rather than imposing a universal threshold.

Example: “Assess deferring included dashboard polish while preserving the required pilot capabilities and recovery evidence.”

Incomplete impacts can produce a preliminary assessment with evidence gaps and a bounded investigation recommendation. Do not present an uncosted idea as an implementation-ready approval. Drafting does not contact stakeholders, alter contracts or commit resources.

## Key Concepts

### Integrated change control follows consequences

A small feature can change testing, data, security or service obligations. A removed item can leave orphan dependencies or make a deliverable unusable. Trace effects across scope/WBS, acceptance, schedule, resources, cost/funding, risks, supplier commitments and transition. Use depth proportional to the actual consequence, not the requester's description of it as “just a small favor.”

Separate approval of an idea, authorization to investigate, conditional plan approval and permission to implement. They have different boundaries and evidence needs. An urgent request does not create emergency delegation; use the actual emergency procedure if one is supplied.

### Before, proposed after, authorized after

Show three states. Before is the current authorized provision. Proposed after is the requested scenario and forecast impact. Authorized after exists only when an actual decision identifies it. Preserve earlier performance and reports against the baseline applicable at their cutoff.

Approval can be partial: cost and scope may change while date and acceptance remain. Conditions may delay effectiveness or impose implementation obligations; record which, rather than interpreting “approved subject to” as unconditional permission.

### Impact ranges need a consistent boundary

Compare alternatives with the same scope, horizon, currency and cost inclusions. Include rework, retesting, transition and ongoing consequences where relevant. Savings from deferral are not automatically cash savings; fixed commitments and transferred future work may remain. A new EAC is a forecast, while available funding and reserve release are separate questions.

Dependencies and resource bottlenecks can prevent a shorter task from improving the finish. Show the schedule mechanism rather than summing optimistic savings. A required criterion cannot be dropped merely because a preference score is low.

## Application

1. **Triage the boundary.** Identify the actual change and authority it crosses. If within delegation, record that basis and use proportionate control. If unknown, draft impacts and obtain the specific delegation evidence. Do not make every backlog edit a sponsor decision.
2. **Define before/after precisely.** Preserve requirement/work-package IDs and versions. State included, removed, deferred and unchanged scope; distinguish a changed acceptance criterion from a new implementation method. If the phase population is unknown, do not invent it to complete the form.
3. **Trace integrated impacts.** Build the [impact matrix](template.md) with evidence, estimate basis, uncertainty, owner and affected artifact. Test for omitted verification/support work and duplicated cost. Identify which previous evidence remains applicable after configuration changes and what must be refreshed.
4. **Compare options and timing.** Include current course/no change, requested change and a feasible alternative when available. Explain benefits, disadvantages, residual risk and opportunity lost if the decision is delayed. Derive the useful decision point from lead times or mark it proposed. Recommend investigation when a critical unknown prevents responsible choice.
5. **Record the exact decision.** Keep proposed, approved, rejected and deferred states distinct. Capture actual authority, date/effectiveness, conditions, scope and funding source. Split independent acceptance/release authorities. No response, a discussion or a supplier estimate is approval.
6. **Implement prospectively and verify.** After actual authorization, update only affected baselines and linked plans, retaining old versions and decision references. Communicate within authorization. Verify implementation against the approved boundary and conditions, including applicable acceptance evidence. Close when verification or an explicit authorized disposition supports it, not merely when the approver says yes.

Quality check: a reviewer can compare before/proposed/approved states, explain impacts and unknowns, identify real authority and see how compliance with the decision will be verified. If the report's only benefit is “now green,” investigate whether it hides variance rather than changes delivery.

### When producing a visual

Use the [before/after impact comparison](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the project source’s evidence and uncertainty in the graphic.

## Examples

Optional worked applications:

- [Relay CR-001 and separate date change](examples/software.md): deferring polish does not remove recovery evidence or authorize a new date.
- [Northstar phased change](examples/migration.md): scope population remains explicit and later failed restore still controls readiness.

## Common Pitfalls

- **Small-favor exemption:** sounding easy substitutes for impact tracing. Check interfaces, acceptance, capacity and service effects before choosing the control path.
- **Forecast becomes permission:** a revised estimate/date is copied into baseline. Keep it proposed until actual authority decides.
- **Conditions disappear:** approval wording is shortened to “yes.” Carry conditions into affected artifacts and verification.
- **Scope removal creates fake savings:** deferred work and fixed supplier costs vanish from the model. Show what is avoided, shifted, still committed or unknown.
- **Approval closes the request:** nobody checks that the implemented result matches the choice. Verify exact scope and applicable evidence before closure.
- **History is cleaned up:** old reports are rewritten to the new date. Keep their cutoffs and add the prospective baseline bridge.

## References

- [Decision Log](../decision-log/SKILL.md) preserves authority; [Acceptance and Traceability](../acceptance-and-traceability/SKILL.md) checks affected evidence.
- [Integrated Project Planning](../integrated-project-planning/SKILL.md), [Project Budget](../project-budget/SKILL.md) and [Dependency Map](../dependency-map/SKILL.md) provide optional impact analysis. When unavailable, use the matrix and checks described here.
