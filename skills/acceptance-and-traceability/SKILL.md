---
name: acceptance-and-traceability
description: "Connect scoped requirements to deliverables, test evidence, and acceptance authority. Use to define done, review coverage, or assess change impact."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Acceptance and Traceability

## Purpose

Make completion provable. Use when requirements need testable acceptance, when a release has disputed readiness, or when a change affects multiple deliverables. A traceability matrix shows coverage and gaps; it does not make a failed requirement acceptable.

## Input

Bring the scope, requirements, business and operational conditions, tests, results, and acceptance authorities.

Example: "Review whether our migration evidence proves the agreed attachment requirements."

If criteria are missing, propose them for confirmation. Do not report proposed criteria or planned tests as accepted evidence.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Traceability chain

Link a stable requirement ID to its rationale, deliverable, verification method, actual result, and acceptance decision. Bidirectional review asks both whether each requirement has evidence and whether each delivered feature has an authorized purpose.

### Verification and acceptance

Verification checks whether a stated condition is met. Acceptance is the authorized judgment about the deliverable. A passing test may be necessary without being sufficient: operations ownership, usability, or a contractual decision may still be outstanding.

Given/When/Then is useful for observable behavior. Quantitative migration reconciliation needs a defined population, matching rules, exception treatment, and result evidence. Vague phrases such as "fast" or "all data" must be made testable in context.

### Why this works

The chain makes omissions and change consequences visible. Separate result and approval fields prevent a test execution from being mistaken for permission to release. Do not reduce high-severity failures to a reassuring overall percentage.

## Application

1. Identify scoped requirements and the source establishing each one. Resolve duplicate or conflicting requirements without erasing history.
2. Define observable acceptance criteria, including negative paths, recovery, access, and service readiness where relevant.
3. Name the verification method and acceptance authority. Label proposed criteria pending agreement.
4. Link deliverables, tests, execution results, evidence dates, and actual decisions. Keep planned/not-run/failed/passed distinct from accepted.
5. Review coverage in both directions and identify any release-blocking gap. A waiver requires the actual authorized decision, scope, and rationale.
6. When requirements change, reassess affected deliverables and evidence. Do not reuse stale test results without evaluating applicability.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Test case as evidence:** a planned test is marked complete. Record execution result and artifact location.
- **Count-only migration:** matching record counts hide corrupted relationships. Validate identity, linkage, representative content, and exception rules.
- **Percent green:** many minor passes obscure a critical failure. Preserve gate-level consequences.
- **Approval by inference:** silence after a demo becomes acceptance. Require an evidenced decision or leave acceptance pending.

## References

- [Scope And Wbs](../scope-and-wbs/SKILL.md)
- [Release Readiness](../release-readiness/SKILL.md)
- [Change Request](../change-request/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
