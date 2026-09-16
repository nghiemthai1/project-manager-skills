---
name: project-recovery-advisor
description: Choose a credible response when the delivery plan fails. Use after a material project setback or diagnosis,
  with causal evidence, options and measurable checkpoints.
metadata:
  type: interactive
  domain: software-it-project-management
  version: 2.1.0
  intent: Develop and compare feasible project recovery options, preserve mandatory outcomes and authority, and
    define evidence checkpoints that test whether the chosen intervention works.
  frameworks: Root-cause hypotheses; recovery option appraisal; recovery checkpoints
  best_for: '["Develop and compare feasible project recovery options, preserve mandatory outcomes and authority,
    and define evidence checkpoints that test whether the chosen intervention works."]'
  scenarios: '["The approved plan is no longer feasible. Compare scope, sequence, resource and date recovery options
    with checkpoints."]'
  estimated_time: Depends on evidence and project scope
---
# Project Recovery Advisor

## Purpose

Help choose a credible response when the current plan no longer works. Recovery may mean resequencing, reducing optional scope, phasing, changing capacity or dates, pausing, or stopping. Preserving the original promise is not automatically the best or feasible outcome.

Produce a recovery recommendation and conditional execution agreement with checkpoints. Use a health diagnostic first when the actual condition is unclear. If production harm is occurring, follow the applicable incident authority/process; drafting a project recovery plan does not authorize live operational changes.

## Input

Bring the threatened objective, current baseline and forecast, observed failure, required acceptance, causal evidence, remaining work, resources, funding and authority. Identify irreversible commitments and current exposure. Preserve exact IDs, versions and earlier decisions.

Example: “The rehearsal failed and remaining cost exceeds funding. Compare a phased recovery with the unchanged plan.”

Use **guided mode** for one adaptive question at a time, **context dump** for supplied evidence, or **best guess** for explicitly provisional options. Missing causes or estimates may justify a bounded investigation instead of a promised recovered date. Do not invent capacity, consent, savings or approved exceptions.

## Key Concepts

### Stabilization, diagnosis and recovery are different

Stabilization limits immediate exposure within actual authority. Diagnosis tests why the plan fails. Recovery changes a mechanism and verifies the result. Sending a patch is an action; applicable verification and acceptance determine whether it repaired the consequential problem.

A response can be useful before every cause is understood, but describe its uncertainty. Do not claim a causal explanation merely because a result improved after an intervention; other conditions may have changed.

### Match the option to the constraint

| Constraint | Candidate response | Evidence needed before relying on it |
|---|---|---|
| Unusable external input | Earlier usable subset, resequence independent work, negotiate real handoff | Receiver criteria, provider commitment and validation capacity |
| Shared skilled bottleneck | Resequence, transfer suitable work, add confirmed qualified capacity | Skill/access/timing plus onboarding and coordination costs |
| Scope exceeds capacity/funding | Defer optional scope, phase delivery, revise timing or investment | Exact retained outcome, dependencies, whole-life costs and authority |
| Failed acceptance | Diagnose, correct and retest applicable behavior | Current result/version, required criteria and actual acceptor |
| Value or feasibility no longer credible | Pause, redesign or termination consideration | Remaining options, obligations, consequences and sponsor decision |

Adding people cannot accelerate every wait or learning constraint. Overlapping work can increase rework; compression can add cost or reduce useful verification time. Show the mechanism and risks instead of applying an automatic percentage reduction.

### A recovery agreement is testable

Specify authorized boundaries, owner/performer, resources, current baseline comparison, leading evidence, outcome checkpoint, review authority and a stop/reconsider trigger. “Back on track next month” is another target unless supported by feasible work and evidence.

A revised baseline preserves history. The original failure and forecast remain part of learning and accountability; a new date is not proof of successful recovery. Required acceptance remains unless an actual permitted exception is explicitly authorized; do not offer imaginary waivers.

## Application

### Ask up to four adaptive questions

Skip supplied answers. Ask one at a time in guided mode and offer choices with freeform context.

1. **What must the response protect, and what can change?** Identify mandatory outcomes, requested dates, funding limits, service consequences and decision rights. If boundaries are unclear, separate known requirements from proposals before comparing options.
2. **What is observed, and what is the suspected mechanism?** Options: input/dependency, capacity, technical quality, scope/change, authority, mixed. Link actual evidence; define a discriminating check for uncertain causes. If immediate exposure exists, identify stabilization permitted under current authority.
3. **Which resources and alternatives are actually available?** Confirm qualified capacity, supplier options, residual work, lead time and funding. Distinguish confirmed from proposed. Unknown availability cannot support a guaranteed finish.
4. **What evidence would prove improvement or make us stop?** Define acceptance/results, useful review point and reconsideration rule. If the main assumptions cannot be tested before irreversible commitment, recommend an investigation or pause decision.

### Compare a feasible option set

Use the [template](template.md) to compare the unchanged course, a mechanism-changing intervention and at least one credible alternative when available. Keep scope, horizon and cost inclusions consistent. Include correction, validation, transition and residual obligations. Record ranges and dependencies; do not add nominal time savings without recomputing the constrained sequence.

### Give a numbered recommendation

1. **Recover within current authority:** a feasible response changes the constraint without crossing delegated limits. Name the confirmed resources and verification checkpoint; do not add an unnecessary sponsor gate.
2. **Seek a bounded baseline/funding change:** the preferred response is credible but changes authorized scope, date or cost. State the exact requested change and separate acceptance/release authorities.
3. **Investigate before selecting:** a material uncertainty changes which option works. Define the smallest useful test, proposed limit/owner and return decision; do not call it a recovered plan yet.
4. **Recommend pause or termination consideration:** no credible authorized/funded option protects required outcomes or value. Show obligations and consequences of stopping as well as continuing. Only actual authority makes the decision.

Explain rejected options and what evidence would make them viable. Several workstreams may need different responses; keep the integrated consequence visible.

### Record, execute within authority and inspect

After an actual decision, record its scope, conditions and effective date, update affected plans prospectively and confirm owners/resources. Drafting alone does not execute or announce the response. At each checkpoint compare actual evidence with the recovery hypothesis, not merely task completion. If the mechanism is not improving or assumptions fail, return to the decision authority with revised options rather than rolling the promise forward indefinitely.

### When producing a visual

Use the [recovery option scenarios](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay's bottleneck-led options](examples/software.md): staffing does not automatically fix an external input or acceptance gap.
- [Northstar phased recovery](examples/migration.md): an approved plan still requires later restore and reconciliation evidence.

## Common Pitfalls

- **Overtime as an estimate:** extra hours are assumed available and productive. Confirm allocation, skills, timing and sustainability before modeling the option.
- **New date, same mechanism:** the plan slips repeatedly without learning. Name what the intervention changes and inspect that evidence.
- **Patch equals recovery:** delivery of a fix closes the response. Require applicable retest and actual acceptance for the consequential condition.
- **Unfunded rescue:** a preferred option consumes unapproved money. Show funding/reserve authority separately from forecast need.
- **Quality disappears:** acceptance is relaxed to fit a date without authority. Retain required criteria or identify an actual permitted exception decision.
- **No stop condition:** checkpoints report activity forever. Define evidence that triggers replan, pause or termination consideration.

## References

- [Project Health Diagnostic](../project-health-diagnostic/SKILL.md), [Dependency Map](../dependency-map/SKILL.md) and [Resource Capacity Plan](../resource-capacity-plan/SKILL.md) support diagnosis/feasibility.
- [Change Request](../change-request/SKILL.md), [Release Readiness](../release-readiness/SKILL.md) and [Project Closure](../project-closure/SKILL.md) support optional decision and outcome handoffs. Use the described artifacts directly if these packages are unavailable.
