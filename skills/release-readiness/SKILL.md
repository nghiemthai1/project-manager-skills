---
name: release-readiness
description: Assess a defined release against current gate evidence. Use before a pilot, launch or migration cutover
  to recommend go or hold without inventing authorization.
metadata:
  type: component
  domain: software-it-project-management
  version: 2.1.0
  intent: Produce a version-specific readiness matrix and recommendation that separates required gates, permitted
    exceptions, immediate service coverage and actual go authority.
  frameworks: Readiness gates; exception authority; operational acceptance
  best_for: '["Produce a version-specific readiness matrix and recommendation that separates required gates, permitted
    exceptions, immediate service coverage and actual go authority."]'
  scenarios: '["Evaluate the current release evidence and recommend go or hold; restore failed even though most
    checks passed."]'
  estimated_time: Depends on evidence and project scope
---
# Release Readiness

## Purpose

Make a defensible readiness recommendation before a release exposes users or operations to change. Produce an evidence matrix and bounded decision request for the exact version, scope, environment and window. Readiness assessment, actual go authorization and successful execution are separate states.

Use for a pilot, software launch or migration wave. A previously approved plan establishes a comparison and authority boundary; it does not prove today's configuration is ready. When live incidents already exist, follow the applicable incident process as well as the project decision route.

## Input

Use release scope/version/population, window and baseline, actual gate rules, test/reconciliation results, defect dispositions, recovery evidence, dependencies, monitoring, support coverage and authorities. Preserve IDs and evidence locations literally. Separate supplied case facts from illustrative examples or neighboring cases; never borrow their tests, approvals or proposed interventions.

Example: “Review the 25 November cutover evidence and identify what prevents a go recommendation.”

If criteria or authority are missing, draft the matrix with those gaps. Do not invent a zero-defect threshold, permitted waiver, recovery time or approver. A technical lead is not automatically the receiving business or service acceptor. Use existing context before asking the few questions that change the recommendation.

## Key Concepts

### A gate is a condition, not a checklist percentage

Classify requirements under actual governance: mandatory conditions, exceptions that specified authorities may permit, and follow-up items that do not block the decision. If classification is unknown, say so. Many minor passes do not compensate for one required restore failure. A composite percentage obscures which condition governs exposure.

### Applicability is part of the result

Record configuration/version, environment, data population, method, execution date, observed result and limitations. A pass for a previous mapping or small unrepresentative sample does not automatically support the current release. Review change impact and refresh affected evidence; do not discard all historical evidence indiscriminately or reuse it without justification.

Verification result and acceptance decision are distinct. A passed test may support a domain acceptance; that acceptance may still leave other domains and go authority unresolved. The matrix should show both, not one ambiguous “approved” column.

### Recovery and operational coverage have real boundaries

A rollback/restore document states a plan. An applicable demonstration supports a capability within tested conditions. Identify irreversible data/external effects, the last useful recovery decision point, recovery limitations, monitoring signals and who can act. Do not assume a snapshot reverses every external transaction.

Immediate operating coverage, escalation and recovery ownership must be established before exposure. Full service handover may occur after actual rollout and stabilization evidence. Requiring a completed post-launch report before launch is impossible; removing pre-launch coverage because handover is later is equally unsound.

### Conditional go is not deferred proof by default

Use conditional go only if actual governance permits the specified condition and authority. Identify whether the condition must be satisfied before execution or may remain as an explicitly accepted residual obligation. A mandatory failed gate without a permitted authorized exception remains a blocker; “we will fix it after go” does not change that.

## Application

1. **Fix the decision boundary.** Identify exact release/version/population/environment/window and actual go/no-go authority. Distinguish approved baseline from desired or forecast date. Record what this decision covers and what remains outside it.
2. **Build the gate inventory.** Map agreed scope and acceptance to required evidence, actual acceptor, classification and exception authority if any. Mark proposed criteria and unconfirmed roles. Include relevant security, business, recovery, operational, dependency and communication conditions without assuming every project needs an identical checklist.
3. **Inspect evidence, not status labels.** Record passed, failed, not run, unknown and accepted exception distinctly. Attach applicable source/result and the actual acceptance state. Reconcile conflicting evidence and preserve previous-version results as history. A vendor upload is not receiving acceptance.
4. **Challenge recovery and exposure.** Review actual demonstrations, point-of-no-return constraints, monitoring, intervention triggers, operator access and immediate coverage. Confirm capacity for correction/retest and decision timing. Unknowns that prevent safe execution remain visible; a runbook cannot fill them by assertion.
5. **Recommend a bounded outcome.** Recommend go only when applicable evidence and required acceptances support the defined scope. Recommend hold when a required condition is failed/absent or critical authority is unresolved. Use permitted conditional go only with exact conditions, owner, timing and consequence. Do not claim the actual authority issued a hold merely because you recommend it.
6. **Record the actual decision and recheck rule.** Use the [matrix template](template.md). Record decider, date, scope/version/window, conditions and decision ID when evidenced. If configuration, population, environment, evidence or window changes, assess applicability again. An earlier go does not grant indefinite permission for materially different exposure.

Quality check: the headline agrees with every independent mandatory gate; claims have applicable evidence; the actual authority can see what is passed, missing, rejected or exceptionally accepted. The record states what would change a hold recommendation and never equates go with completed deployment.

### When producing a visual

Use the [independent gate evidence matrix](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay missing recovery evidence](examples/software.md): B2 funding and the existing date do not satisfy security acceptance.
- [Northstar failed restore](examples/migration.md): the phased baseline preserves the gate and separates later go from service transfer.

## Common Pitfalls

- **Checklist arithmetic:** a high pass count hides a required failure. Assess condition and consequence rather than averaging.
- **Plan equals proof:** a recovery document is called a successful demonstration. Inspect actual execution and its limits.
- **Sponsor as universal waiver:** funding authority is used to bypass independent acceptance. Verify actual exception/go rights and scope.
- **Stale pass reused:** previous-version evidence supports a changed release without analysis. Map change impact and refresh affected checks.
- **Coverage after exposure:** operators are assigned only at handover. Confirm immediate coverage before go, then validate full transfer later.
- **Go means done:** permission is reported as successful delivery. Link subsequent execution and monitoring evidence separately.

## References

- [Acceptance and Traceability](../acceptance-and-traceability/SKILL.md), [Quality Management Plan](../quality-management-plan/SKILL.md) and [Project Governance](../project-governance/SKILL.md) supply optional criteria/evidence/authority inputs.
- [Release and Handover](../release-and-handover/SKILL.md), [Decision Log](../decision-log/SKILL.md) and [Project Recovery Advisor](../project-recovery-advisor/SKILL.md) support the next action. The matrix remains usable without adjacent packages.
