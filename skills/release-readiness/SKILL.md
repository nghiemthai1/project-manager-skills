---
name: release-readiness
description: "Assess release or cutover readiness against explicit acceptance, recovery, operational, and authorization evidence. Use for a go/no-go review."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Release Readiness

## Purpose

Provide a defensible readiness recommendation before exposing users or operations to a release. Use for pilot launch, production cutover, or a major migration wave. Readiness assessment and actual go authorization are separate records.

## Input

Bring release scope/version, gate criteria, test and reconciliation results, rollback/restore evidence, service coverage, open defects, and decision authorities.

Example: "Review the 25 November migration cutover evidence and recommend go or hold."

Missing evidence stays missing. A deadline or a previously approved plan is not evidence that a criterion passed.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Gates are conditions, not percentages

A gate defines the evidence required for a decision. A mandatory failed condition cannot be canceled by many minor passes. Separate blockers from explicitly waivable exceptions and from lower-priority follow-up work according to the project's actual rules.

### Recoverability and ownership

A rollback or restore plan describes an intended response. A relevant demonstration provides evidence it works under stated conditions. Record the decision window, irreversible steps, recovery limits, monitoring, and who owns the service during the release. Full post-release handover may occur later, but immediate operational coverage must be explicit.

### Why this works

An evidence matrix connects each readiness claim to a responsible authority. It prevents the release date, a vendor receipt, or code completion from substituting for business and operational acceptance.

## Application

Before drafting, separate supplied case facts from illustrative examples and neighboring cases. Do not import a lesson, test result, proposed intervention, or approval from another case. Label any new recommendation as proposed. A technical lead is not automatically the confirmed receiving acceptance authority; mark that assignment unconfirmed unless supplied. Describe a hold as recommended until an authorized hold decision is evidenced, and call an approved cutover date a baseline.

1. Confirm the release boundary, version, target window, and actual go/no-go authority.
2. List agreed acceptance and operational gates with owners and required evidence. Mark any proposed criteria unconfirmed.
3. Inspect current results and their applicability to this version and environment. Separate passed, failed, not run, unknown, and approved exception states.
4. Review dependencies, unresolved defects, rollback/restore, monitoring, support coverage, and communication readiness.
5. Recommend go, conditional go only where permitted, or hold. Explain each blocking gap and the evidence or authorized exception needed to change the recommendation.
6. Record the authority's actual decision and conditions separately. Do not infer a waiver from schedule pressure or broad sponsorship.
7. Define recheck triggers for changed scope, environment, data, or evidence; a prior pass may no longer apply after a material change.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Checklist arithmetic:** 95% of items pass, so a failed restore is ignored. Evaluate the consequence and mandatory gates.
- **Plan equals proof:** a rollback document is treated as a successful rehearsal. Inspect demonstration evidence and applicability.
- **Sponsor as universal waiver:** budget authority is assumed to override security or business acceptance. Verify the actual governance.
- **Version mismatch:** tests from a previous build justify a changed release. Review applicability and rerun affected evidence.
- **Go as completion:** authorization is treated as successful deployment. Monitor actual execution and retain the handover/closure steps.

## References

- [Acceptance And Traceability](../acceptance-and-traceability/SKILL.md)
- [Release And Handover](../release-and-handover/SKILL.md)
- [Decision Log](../decision-log/SKILL.md)
- [Project Recovery Advisor](../project-recovery-advisor/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
