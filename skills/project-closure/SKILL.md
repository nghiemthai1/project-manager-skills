---
name: project-closure
description: "Close a project with explicit acceptance, financial reconciliation, transferred obligations, archived evidence, and post-project benefit ownership."
metadata:
  type: workflow
  domain: software-it-project-management
  version: "1.0.0"
---
# Project Closure

## Purpose

Finish the project's temporary responsibilities without losing ongoing obligations. Use after delivery and service handover, or for an authorized early termination. Deployment, exhausted budget, or an empty task board alone does not establish closure.

## Input

Bring the charter and baselines, acceptance and handover records, actual/remaining costs, open issues, contracts or obligations, learning, and benefit measures.

Example: "Prepare Northstar's closure decision after operations handover."

If acceptance or ownership is incomplete, produce a closure-readiness assessment and list the unresolved conditions rather than claiming the project is closed.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Administrative closure and continuing value

The project can close while benefits are still being measured, provided ownership and review are transferred explicitly. Conversely, a successful technical launch does not close outstanding financial or service obligations.

### Residual work

An open item may be completed, transferred with acceptance, accepted as a residual risk by the right authority, or retained as a closure blocker. Writing a name next to it is not evidence that the recipient accepted responsibility.

### Closure baseline history

Compare the final outcome with original and approved revised baselines. Explain changes rather than presenting the final plan as if it were the original commitment. Separate final actual costs from unresolved invoices or forecast accruals.

### Why this works

A closure decision creates an accountable boundary between the temporary project and ongoing operations. Preserved history supports honest learning, while named benefit ownership prevents value review from disappearing when the team disbands.

## Application

Before drafting, separate supplied case facts from illustrative examples and neighboring cases. Do not import a lesson, test result, proposed intervention, or approval from another case. Label any new recommendation as proposed. A technical lead is not automatically the confirmed receiving acceptance authority; mark that assignment unconfirmed unless supplied. Describe a hold as recommended until an authorized hold decision is evidenced, and call an approved cutover date a baseline.

1. Confirm the closure route: normal completion or authorized termination. Identify the authority and criteria.
2. Reconcile scope acceptance, release outcomes, and explicit service handover. List any unmet conditions.
3. Reconcile actual costs, remaining commitments, and financial ownership. Do not infer final financial close from a forecast or budget approval.
4. Disposition every material open issue, risk, action, and obligation with evidence of completion, accepted transfer, or authorized residual exposure.
5. Record lessons and compare outcomes with original and revised baselines. Preserve decisions and exceptions.
6. Assign and confirm post-project benefit measures, owner, and review date. Planned benefits are not reported as realized benefits.
7. Archive a navigable evidence set and request or record the actual closure decision. Release resources only within that authority and confirmed transfer.
8. Produce a closure report stating what ended and which responsibilities continue elsewhere.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Launch equals closure:** acceptance, support, and finances remain unresolved. Review closure conditions separately.
- **Transfer by naming:** an issue is assigned to operations without agreement. Obtain acceptance or keep it open.
- **Final cost from EAC:** a forecast is presented as actual spend. Reconcile accounts and label remaining estimates.
- **Benefits declared early:** expected adoption or savings become facts. Transfer measurement and report only observed results.
- **History sanitized:** only the final date and budget are shown. Preserve the original baseline and authorized changes.

## References

- [Release And Handover](../release-and-handover/SKILL.md)
- [Lessons Learned](../lessons-learned/SKILL.md)
- [Project Budget](../project-budget/SKILL.md)
- [Decision Log](../decision-log/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
