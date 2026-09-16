---
name: integrated-project-planning
description: Reconcile scope, acceptance, schedule, capacity, costs and controls into one plan. Use when preparing
  a baseline or revising a plan whose parts no longer agree.
metadata:
  type: workflow
  domain: software-it-project-management
  version: 2.1.0
  intent: Coordinate planning artifacts and resolve cross-discipline contradictions before presenting a bounded
    baseline decision.
  frameworks: Integrated baseline planning; progressive elaboration; consistency review
  best_for: '["Coordinate planning artifacts and resolve cross-discipline contradictions before presenting a bounded
    baseline decision."]'
  scenarios: '["Bring scope, estimates, dependencies, people, costs, risks and acceptance together into one coherent
    delivery plan."]'
  estimated_time: Depends on evidence and project scope
---
# Integrated Project Planning

## Purpose

Create a plan whose parts agree and whose unresolved assumptions are visible to the people deciding. Produce an integrated plan, feasible options, an evidence-based baseline request and a control handoff. Use after initiation or when a material change invalidates the delivery model.

An integrated plan is not a stack of separately optimistic documents. Scope determines work; acceptance determines completion; dependencies and estimates shape sequence; capacity determines whether the work can actually overlap; costs and risks shape affordability and response choices. Changing one can invalidate the others.

## Input

Bring the mandate, current plan versions, scope and acceptance, estimates, dependencies, resource calendars, financial evidence, risk responses and actual governance. Enter at the earliest unresolved phase and reuse applicable artifacts. With partial input, produce a useful draft and the decisions needed to complete it; with no input, ask what project outcome or baseline decision needs planning.

Example: “Turn these kickoff outputs into a baseline proposal, but the same specialist is on two workstreams and service handover is missing.” Use inline facts without repeating an interview. Never import the numerical toy network or staffing data from a neighboring example into the user's plan.

## Key Concepts

### Integration is a set of consistency tests

| Interface between artifacts | Contradiction to find |
|---|---|
| Charter → WBS → acceptance | A required outcome is missing, duplicated or has no observable completion rule |
| Estimate → capacity → schedule | Effort becomes duration without availability, or one specialist appears on parallel work |
| Dependency → schedule → gate | A provider delivers after the usable input is needed, or a review has no time/resources |
| Scope/sequence → cost/funding | Transition, vendor correction or duplicated operation is absent from the estimate |
| Risk response → work/cost/owner | A response is promised but unresourced, unfunded or unassigned |
| Governance → baseline/change | A prepared proposal is presented as approved, or one authority's decision is extended beyond its remit |

Use stable IDs and common versions to make these checks practical. A traceability link connects artifacts; it does not prove their underlying assumptions are consistent. Review the actual values and boundaries.

### Plan progressively without hiding later obligations

Near-term work needs enough detail to execute; uncertain later work can be a planning package with an estimate basis, uncertainty and a decomposition trigger. Keep its cost, dependencies, acceptance and transition consequences visible. A blank late-phase schedule is not evidence that the phase takes no time.

Distinguish target, current forecast, proposed baseline, approved baseline and actual result. Baseline approval records exactly what was authorized and under what conditions. A sponsor's cost/date decision does not waive an independent security or operational acceptance requirement.

### Sequence operational readiness and handover correctly

Before go/no-go, establish the required immediate operating coverage, recovery capability, monitoring and acceptance evidence for safe execution. Full service transfer may occur after cutover and stabilization when the receiver can accept the actual service and residuals. Do not require all post-cutover evidence before cutover, but do not leave execution unsupported. Define the two boundaries and receiving decisions separately.

## Application

### Phase 1: Establish mandate and decision boundaries

Input: charter, current authorization and unresolved choices. Confirm included outcomes, exclusions, sponsor/PM remit and independent acceptance roles. Output: planning boundary, version map and decision-rights record. Exit: enough authority/scope is known to plan, with material conflicts exposed as options; missing information does not prevent a clearly labeled draft. Use Project Charter and Project Governance if available.

### Phase 2: Define work and completion

Input: planning boundary and receiving needs. Build the WBS and acceptance chain, including integration, assurance, project control, transition and closure work. Output: bounded packages, criteria, proposed/confirmed owners and open scope decisions. Exit: consequential work is represented and completion can be evaluated, or a named investigation/decision explains the gap. Handoff to Scope and WBS and Acceptance and Traceability is optional; their fields can live in the plan.

### Phase 3: Model feasible delivery and funding

Input: packages, estimates, provider/receiver dependencies and calendars. Build the dependency model, reconcile individual resources and review/transition timing, then price the same scope and sequence. Include risk-response effort and costs once. Output: current forecast scenarios, capacity constraints, cost/ETC and funding bridge. Exit: a feasible option is evidenced or the unresolved constraints and tradeoffs are explicit. Revisit phase 2 if scope options change.

### Phase 4: Challenge the integrated proposal

Input: all current artifacts. Run the consistency tests above and inspect a failed gate, delayed input or absent specialist scenario. Output: contradiction log, corrected proposal and decision brief with options, assumptions and conditions. Branch: proceed to decision when the relevant basis is adequate; rework the model when a contradiction changes feasibility; seek a bounded investigation when evidence cannot support commitment. Do not conceal unknowns to make every field green.

### Phase 5: Record the actual decision and hand off control

Input: proposal, relevant authority decisions and conditions. Record exactly which scope/date/funding versions were approved; retain rejected options, open assumptions and separate acceptance gates. Output: baseline/forecast map, control cadence, owners and first evidence checkpoints. Exit: Delivery Control Cycle can compare current evidence against the correct authorized boundaries, or the plan remains a proposal pending a real decision. Later changes re-enter the affected phase without erasing earlier baselines.

Use [the integrated-plan template](template.md). A decision-ready plan should let a reviewer trace a milestone to work, people, cost, acceptance and authority. It need not pretend all uncertainties are resolved; it must show which uncertainties matter to the decision and what happens if they break the plan.

### When producing a visual

Use the [linked baseline review pack](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay integrated proposal](examples/software.md): pre-approval planning with missing capacity/interface evidence and later independent scope/date decisions.
- [Northstar revised plan](examples/migration.md): phased scope, funding, rehearsal, immediate coverage and later service transfer form one chain.

## Common Pitfalls

- **Document bundle as plan:** scope, dates and costs use different versions. Reconcile their actual boundaries before requesting approval.
- **Date-driven omission:** testing or transition vanishes to fit the target. Restore the required work and surface the tradeoff.
- **Risk response without resources:** the register promises mitigation while the plan contains no work, owner or cost. Integrate the response or mark it uncommitted.
- **Approval of unknowns as certainty:** missing inputs disappear from the sponsor summary. State conditions, confidence limits and the next evidence decision.
- **Full handover before its evidence exists:** post-cutover acceptance is placed before execution. Separate immediate operating readiness from later accepted transfer.
- **One approval covers all:** budget authorization is called security or service acceptance. Preserve each authority's bounded decision.

## References

- [GAO Schedule Assessment Guide](https://www.gao.gov/products/gao-16-89g): integrated schedule logic and quality.
- [Scope and WBS](../scope-and-wbs/SKILL.md), [Acceptance and Traceability](../acceptance-and-traceability/SKILL.md): work and proof.
- [Milestone Schedule](../milestone-schedule/SKILL.md), [Resource Capacity Plan](../resource-capacity-plan/SKILL.md), [Project Budget](../project-budget/SKILL.md): feasible delivery and funding.
- [Delivery Control Cycle](../delivery-control-cycle/SKILL.md): hand off approved comparisons and current uncertainty.

Related skills are optional components, not installation dependencies. Preserve their required artifact relationships when planning with this package alone.
