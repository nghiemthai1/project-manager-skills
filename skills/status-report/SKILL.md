---
name: status-report
description: "Create evidence-based project status updates with baseline variance, forecast, risks, and explicit decisions needed. Use for weekly or executive reporting."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Status Report

## Purpose

Help a stakeholder decide whether to intervene. Report what changed, what the change means for delivery, and who needs to decide next. Use for a recurring project update or a dated exception report. A status report does not approve a revised baseline or replace a detailed schedule.

## Input

Bring the reporting date, audience, last report, approved scope/date/budget, current forecast, and evidence of accepted work. Useful additions are unresolved decisions and owners.

Example: "Write the 16 October Relay update for Ada using these costs, dependency changes, and the prior report."

If the baseline or forecast is missing, produce a partial report with an explicit confidence gap. Do not infer a green status from an absence of reported problems.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Baseline, actual, forecast

The baseline is the authorized comparison point. Actuals describe observed results. The forecast is today's expectation. Keeping all three visible prevents a moving target from hiding a missed commitment. A target date without approval is not a baseline.

### RAG with evidence

Red/amber/green summarizes an agreed tolerance, not the team's mood. Explain the assessment separately for scope, schedule, cost, and quality where they differ. Red means intervention is required under the project's rules; amber means credible recovery exists but material risk remains; green requires supporting evidence. If no thresholds have been agreed, label your rating provisional and explain the proposed interpretation. Use unknown when the evidence cannot support a rating.

### Why this works

A short narrative connected to a decision lets the reader act without reconstructing a backlog. Leading with accepted outcomes avoids confusing effort with progress. Showing forecast changes also exposes deteriorating situations before a formal breach.

An executive update emphasizes tradeoffs and decisions. A team update adds immediate dependencies and operational detail. Neither audience receives different facts.

## Application

1. Fix the as-of date and audience. Reconcile contradictions between the tracker, forecast, prior report, and approval log before selecting a rating.
2. Identify completed outcomes with acceptance evidence. Keep partial progress distinct from accepted deliverables.
3. Compare current forecasts with the applicable baseline. Show original and revised baselines when a change was approved, including the decision ID.
4. Write a short health statement with the most consequential evidence. Do not average away a release-blocking failure behind healthy cost or scope.
5. List the next few deliverables and the risks/issues affecting them, with owners and dates when evidenced.
6. End with explicit decisions or help required, decision owner, needed-by date, and consequence of delay. If those fields are unknown, name the gap.
7. Review the headline against every underlying row. Keep the detailed evidence linked and record changes since the last report.
8. For a one-screen executive request, aim for 150–250 words with at most three material asks. Use only the template sections needed for the decision; move detailed diagnostics to a separate linked appendix when useful. Do not turn an executive brief into a full control report.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Green headline, red evidence:** a blocked release is buried in a footnote. Stakeholders miss the intervention window. Rewrite the headline around the blocker and the decision it requires; check whether someone reading only the first paragraph would act correctly.
- **Baseline laundering:** the latest forecast silently replaces the authorized date. Slippage disappears. Show both columns and link the approval for any rebaseline.
- **Activity as achievement:** "held six workshops" substitutes for an accepted outcome. Report the decision, validated requirement, or other result, or label the work still in progress.
- **Ask without a recipient:** "leadership support needed" has no executable next step. Specify the decision and accountable authority, leaving unknowns explicit.

## References

- [Earned value interpretation](https://www.energy.gov/documents/integrated-project-management-using-earned-value-management-system)
- [Project Health Diagnostic](../project-health-diagnostic/SKILL.md)
- [Project Budget](../project-budget/SKILL.md)
- [Escalation Brief](../escalation-brief/SKILL.md)
- [Decision Log](../decision-log/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
