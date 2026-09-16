---
name: acceptance-and-traceability
argument-hint: '[requirements, criteria, and evidence]'
description: Connect requirements to applicable results and acceptance decisions. Use when defining done, checking
  coverage or assessing the evidence impact of a change.
intent: Create an auditable chain from authorized requirement through verification to a bounded acceptance decision.
type: component
theme: scope-and-planning
best_for:
  - Create an auditable chain from authorized requirement through verification to a bounded acceptance decision.
scenarios:
  - Link each requirement to its acceptance criterion, executed test evidence, result and approving authority.
estimated_time: Depends on evidence and project scope
frameworks: Requirements traceability matrix; verification versus validation; bidirectional impact analysis
domain: software-it-project-management
version: 2.1.0
---
# Acceptance and Traceability

## Purpose

Make completion provable and disagreements visible. Produce a traceability matrix linking scope requirements, deliverables, criteria, executed evidence and actual acceptance. Use during planning, a disputed readiness review or impact analysis when scope/configuration changes.

A matrix establishes relationships and exposes gaps. It cannot turn a planned test into a pass, a pass into authorization, or an average pass rate into satisfaction of every mandatory condition. Use Quality Management Plan to design the assurance process and Release Readiness to evaluate the current release decision; this component supplies their traceable evidence.

## Input

Bring the scoped requirements and their sources, criteria, deliverable versions, test or inspection methods, actual results, evidence dates and acceptance authorities. Incomplete inputs are welcome: distinguish a proposed criterion, planned test and missing result. With no context, ask which deliverable or requirement needs proof. Reuse supplied information without re-asking.

Example: “Review whether these export checks prove that the agreed attachments still belong to the right tickets.” Preserve original IDs such as R-ACC03 or M-REQ04 when updating an existing artifact; do not break downstream references by renumbering for appearance.

Treat requirement IDs, build/version strings, evidence paths and URLs as literal data. Preserve their exact case, punctuation and spacing: `BC-R7` and `v2` must not become `BC-R 7` and `v 2` during prose cleanup. Compare every supplied identifier used in the matrix against the input before delivery; avoid global typography substitutions across the artifact.

## Key Concepts

### The traceability chain

Link requirement/source → deliverable or work package → observable criterion → verification/validation method → executed result on a defined version/population → acceptance decision. A one-to-many relationship is normal: one requirement may need several checks, and one evidence artifact may support several requirements. State which portion of the evidence supports each claim rather than pasting the same link everywhere.

Forward tracing asks whether every authorized requirement has applicable proof. Backward tracing asks whether each delivered feature or check serves an authorized requirement or another justified purpose. An orphan feature may reveal gold-plating; an orphan requirement may reveal omitted work. Duplicate or conflicting requirements need a recorded resolution, not silent deletion.

### Define an observable criterion

Given/When/Then helps describe behavior: initial condition, action/event and observable outcome. For data migration, define the population, identity/matching rules, allowed exceptions and reconciliation result. For an operational handoff, define duties and evidence the receiver needs. “Fast,” “all data” and “ready” are incomplete until their context is agreed. Proposed numeric thresholds remain proposals unless sourced or accepted.

Verification checks a specified condition. Validation checks fitness for the intended use. Acceptance is the authorized decision about the bounded result. A technical pass can support acceptance while business usability, service ownership or other criteria remain open. Explicitly record the distinction when one person prepares evidence and another accepts it.

### Evidence has applicability, not just a hyperlink

| Field | Why it matters |
|---|---|
| Artifact/version and execution date | A result for last week's build may not apply after a configuration change |
| Population/environment | A sample or rehearsal may exclude a critical case |
| Observed result and limitations | “Passed” without the condition tested is hard to inspect |
| Reviewer and acceptance authority | A producer's claim is not automatically receiving approval |
| Status and decision reference | Planned, blocked, failed, passed and accepted are different states |

Retain failed and superseded results. New evidence adds to the chain; it does not rewrite an earlier ledger. When a requirement, build, dataset or environment changes, classify evidence as still applicable, needing targeted refresh or invalidated, with a reason. Reuse needs analysis, not a blanket prohibition or a blanket pass.

## Application

1. **Establish scope and stable IDs.** Identify each requirement's source, version and authority. Mark unresolved conflicts or proposed criteria; keep excluded requests separate.
2. **Make criteria testable.** Define observable success, relevant negative/exception paths and mandatory boundaries. Include recovery, relationships, access and service conditions where the actual scope requires them.
3. **Map methods and responsibilities.** Link work packages and planned checks. Name producer, reviewer and acceptor only where evidenced; distinguish proposed assignments. A test plan is useful even before results exist.
4. **Attach actual evidence.** Record the tested configuration/population, date, result and limitations. Keep blocked/not-run distinct from executed failure; keep technical result distinct from acceptance.
5. **Review coverage and consequences.** Trace in both directions. Identify the material missing or contradictory proof and its gate consequence. An exception requires its actual authorized scope, rationale and conditions; no average score substitutes for that decision.
6. **Maintain through change.** Identify affected requirements, checks, data and acceptors. Preserve old results, assess applicability and request targeted retesting or renewed acceptance where needed. Hand the current evidence and open gaps to readiness or change control.

Use [the traceability template](template.md). A reviewer should be able to follow a material claim to its source and actual result, tell whether that result applies now, and identify the decision still needed. If they cannot, the matrix is incomplete even if every cell contains text.

### When producing a visual

Use the [evidence traceability matrix](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the project source’s evidence and uncertainty in the graphic.

## Examples

Optional worked applications:

- [Relay recovery chain](examples/software.md): a planned demonstration and later accepted evidence remain separate dated states.
- [Northstar relationship chain](examples/migration.md): matching counts do not close a failed attachment requirement.

## Common Pitfalls

- **Test case as evidence:** a designed check is marked complete. Require execution information or retain planned/not-run status.
- **Evidence link without applicability:** a stale pass is reused after mapping changes. Record the version and review impact before relying on it.
- **Count-only migration:** totals match but relationships or access fail. Check identity, linkage and intended use within the agreed population.
- **Percent green:** many minor passes hide a mandatory failure. Show the requirement/gate consequence separately.
- **Approval by inference:** silence after a demo is treated as acceptance. Record the explicit decision or leave acceptance pending.
- **Requirement churn erases history:** IDs and old results are replaced to make the latest matrix tidy. Preserve lineage and supersession links.

## References

- [Scope and WBS](../scope-and-wbs/SKILL.md), [Quality Management Plan](../quality-management-plan/SKILL.md): work coverage and evidence design.
- [Release Readiness](../release-readiness/SKILL.md), [Change Request](../change-request/SKILL.md): current gate and change consequences.

Adjacent skills are optional. Retain the requirement, source, criterion, actual evidence, applicability and authority fields when using this component alone.
