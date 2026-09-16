---
name: quality-management-plan
argument-hint: '[quality objectives, controls, and evidence]'
description: Define quality criteria, prevention, verification and defect control. Use when project quality expectations
  need an executable plan before delivery or release.
intent: Plan how the project will prevent defects, verify outputs and obtain acceptance using risk-proportionate
  evidence.
type: component
theme: controls-and-assurance
best_for:
  - Plan how the project will prevent defects, verify outputs and obtain acceptance using risk-proportionate evidence.
scenarios:
  - 'Use quality-management-plan: Plan how the project will prevent defects, verify outputs and obtain acceptance
    using risk-proportionate evidence.'
estimated_time: Depends on evidence and project scope
frameworks: Quality planning/assurance/control; verification versus validation; risk-based testing; PDCA
domain: software-it-project-management
version: 2.1.0
---
# Quality Management Plan

## Purpose

Turn “make it high quality” into a plan for observable criteria, preventive practices, verification, defect handling and acceptance. Produce a quality matrix with named evidence and decision boundaries. Use before execution or when escaped defects reveal that existing checks do not test what matters.

This plan defines how quality will be managed. Acceptance and Traceability tracks requirement-to-result evidence; Release Readiness evaluates the current gate. A plan naming a test is not proof that the test ran or passed.

## Input

Bring deliverables, user/operational needs, applicable standards or contract criteria, risk analysis, interfaces, test environments/data, current defects and acceptance authorities. Use existing context directly. With partial input, draft the plan and identify criteria needing agreement. With no input, ask which deliverable's quality is in question.

Example: “Plan quality for a ticket migration where counts can reconcile while attachment links are wrong.” Do not invent certification, universal defect thresholds or permission to use production data. Specify evidence requirements within the actual project context.

## Key Concepts

### Prevention, process assurance and output control

Prevention reduces defects before they are made: clear interface contracts, reviewed mappings, representative test data or rehearsed procedures. Assurance examines whether the agreed quality process is appropriate and followed. Control examines actual outputs against criteria. Acceptance is the authorized judgment about a defined result. Useful plans combine these rather than replacing all quality work with a final test phase.

Verification asks whether specified criteria were met; validation asks whether the result serves the intended use. A migration can verify equal record counts while failing validation because users cannot follow attachment links. Include the consequential user or operator journey as well as technical checks.

### Match evidence to consequence

Risk-based testing concentrates depth on failures with important consequences and uncertain behavior. It does not silently waive mandatory criteria. Specify the population, sample method if any, environment/configuration and result evidence. A clean convenience sample establishes only what was checked; extrapolation needs a justified sampling basis. Risk scores help focus discussion but are not automatically probabilities or expected financial loss.

Define severity by consequence and priority by the order of response; a low-frequency recovery failure can be severe. Use the organization's existing scheme or mark a proposed scheme for agreement. Never assert “zero defects” from a finite test set; say which checks passed and what remains untested.

### Metrics need denominators and decisions

A pass rate needs the number of applicable checks, executed checks, blocked checks and failures. Excluding blocked tests can make the percentage look better while confidence falls. A mandatory failed gate is not averaged away by many low-consequence passes. Defect age, recurrence and escaped defects can prompt process improvement, but no universal red/amber threshold is supplied here.

PDCA connects a proposed improvement to a small trial, inspection and a decision to adopt, adjust or abandon. Do not declare an improvement effective merely because an action was completed.

## Application

1. **Define quality from the receiving need.** For each material deliverable state the criterion, source, population and acceptance authority. Separate mandatory criteria from preferences and unresolved proposals. Include service operation and recovery, not just functionality.
2. **Choose prevention and assurance.** Match plausible failure causes to preventive reviews, process checks and required independence. Give these activities owners and timing; do not assign self-approval where the actual assurance rule requires separation.
3. **Plan verification and validation.** Define method, environment/version, data, entry conditions, evidence location and reviewer. Include negative, boundary, integration and recovery cases where relevant. Explain what a sample can and cannot establish.
4. **Define defect and exception handling.** Record observed behavior, expected criterion, reproducible evidence, consequence, owner, correction and retest scope. An exception request goes to the actual authority; a PM's schedule pressure does not approve residual risk.
5. **Set the reporting and improvement loop.** Track applicable/executed/blocked/failed checks and material open defects. Use recurring failures to test a process improvement; keep the cause as a hypothesis until evidence supports it.
6. **Review and maintain the plan.** Walk through a failed high-consequence test and a changed scope/version. Ensure evidence is invalidated or refreshed when applicability changes. Pass actual results to readiness and preserve earlier failures rather than overwriting them with the latest pass.

Use [the quality-plan template](template.md). The plan is usable when a delivery owner knows what to do, a reviewer knows what evidence to inspect and an acceptor can explain the consequence of a failure. A list of tools or a target pass percentage alone is not enough.

### When producing a visual

Use the [assurance and evidence coverage matrix](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay recovery evidence](examples/software.md): define prevention and testing while retaining the failed 28 October security gate.
- [Northstar migration correctness](examples/migration.md): counts, relationships, permissions and restore require different checks.

## Common Pitfalls

- **Test count becomes confidence:** 99 minor passes outweigh one failed recovery check. Report applicability and critical failures separately; preserve mandatory gates.
- **Counts equal correctness:** record totals match while relationships or permissions fail. Verify identities, relationships and intended use as well as totals.
- **Blocked tests disappear:** the denominator shrinks and pass rate improves. Show not-run and blocked work explicitly.
- **Fix without retest scope:** one sample succeeds while affected interfaces remain unverified. Define regression impact and retain the version of each result.
- **Training called assurance:** a team attended a session but the process still fails. Inspect actual application and outcomes; use PDCA to test improvement.

## References

- [Acceptance and Traceability](../acceptance-and-traceability/SKILL.md): requirement/result links.
- [Risk Workshop](../risk-workshop/SKILL.md), [Release Readiness](../release-readiness/SKILL.md): risk selection and current gate decisions.
- [ASQ quality planning](https://asq.org/quality-resources/quality-plans), [QA and QC](https://asq.org/quality-resources/quality-assurance-vs-control), [PDCA](https://asq.org/quality-resources/pdca-cycle): method references.

These links do not claim certification. The plan remains usable without adjacent skills by retaining criteria, evidence, applicability and authority fields.
