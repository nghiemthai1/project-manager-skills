---
name: status-report
description: Report project evidence, forecast variance and decisions needed. Use for an executive update, recurring
  control report or material exception.
metadata:
  type: component
  domain: software-it-project-management
  version: 2.0.0
  intent: Produce a dated audience-specific status report that preserves baseline, forecast, actual and acceptance
    states and makes the next intervention clear.
  frameworks: RAG by tolerance; management by exception; baseline/forecast/actual
  best_for: '["Produce a dated audience-specific status report that preserves baseline, forecast, actual and acceptance
    states and makes the next intervention clear."]'
  scenarios: '["Write a one-screen sponsor update from these current facts, showing delivery confidence, changes
    and decision asks."]'
  estimated_time: Depends on evidence and project scope
---
# Status Report

## Purpose

Help the reader decide whether and how to intervene. State what changed, what it means for delivery, and the decision needed. A status report is a selective control view, not a copy of the task tracker or permission to change the plan.

Use for executive updates, regular delivery reviews and material exceptions. Use a health diagnostic when conflicting signals need investigation before a credible conclusion exists. If the immediate job is one choice beyond delegated authority, use an escalation brief and link it from the report.

## Input

Use reporting date/cutoff, audience, previous report, applicable approval/baseline records, current forecast method, observed actuals, acceptance evidence, current issues and decisions. Identify sources that disagree. Mark missing or stale information explicitly rather than assuming no news is good news.

Example: “Write Ada a one-screen 16 October update from the cost data, interface forecast and current acceptance gaps. No change has been approved.”

The report can be partial if data is incomplete. State which conclusion cannot yet be supported and what evidence will resolve it. Do not copy fictional example people, ratings or thresholds into a real update.

Preserve supplied baseline, decision, requirement and version identifiers exactly, including case, punctuation and spacing. For example, `VB1` must not become `VB 1` in a polished report. Compare referenced identifiers with the input before delivery; never apply a global prose-spacing rule across them.

## Key Concepts

### Use four distinct states

The **target** is desired performance. The **baseline** is the authorized comparison point. The **forecast** is today's expectation under stated assumptions. **Actuals** are observed results. Acceptance is a separate decision about a defined result; completed effort or a passed test is not automatically accepted scope.

A revised forecast belongs in the report before a change is approved. A revised baseline requires its actual decision reference and effective date. Preserve original-to-current baseline history and forecast movement so rebaselining cannot erase earlier performance.

### RAG summarizes a decision rule

Red/amber/green should mean something under the project's tolerances and escalation rules. A common local interpretation is red requiring intervention, amber carrying a material threat with a credible response, and green supported within agreed boundaries. These are not universal thresholds. If rules are absent, label the assessment provisional and explain its evidence; use unknown when data cannot support a rating.

Assess scope, schedule, cost, quality/acceptance and operations separately where they differ. A required release gate failure cannot be averaged away by green cost and scope rows. Conversely, one uncertain input does not prove a specific final-date slip without the schedule model.

### Report outcome and consequence

“Six workshops held” describes activity. “Acceptance population agreed by the actual owner, record X” describes a decision result. If acceptance has not occurred, say work is prepared, tested, awaiting review or blocked as supported. Do not turn a percentage of tasks closed into percentage of business value or readiness.

Cost indicators also need interpretation: CPI describes earned value per cost, SPI compares earned to planned value, and monetary schedule variance is not days late. A forecast cost is not a funding authorization. Keep reserve and approval boundaries visible where they affect the decision.

## Application

1. **Fix audience and cutoff.** Identify what the recipient can decide and the period covered. Reconcile source conflicts or report them explicitly. A later approval cannot be used to improve an earlier report. Record stale-source dates when they differ from the reporting date.
2. **Build the comparison underneath the headline.** For each material dimension, show baseline/authority, current forecast or observation, variance, confidence and consequence. Calculate date differences on the declared calendar and like date definitions; do not subtract supplier delivery from receiver acceptance and call the result project float.
3. **Select a defensible health statement.** Lead with the highest-consequence current evidence and its needed action. State provisional/unknown status where appropriate. A reader seeing only the first paragraph should not infer readiness when required evidence is failed or absent.
4. **Report progress and changes.** Name a few completed/accepted outcomes with evidence, material forecast movement and changed issues. Keep planned work separate. Explain why an item matters instead of listing every activity. Retain issue/risk distinctions and stable IDs.
5. **Make the asks executable.** State decision, actual authority, evidence/option needed, useful decision time and consequence of delay. If authority or time is unknown, identify that gap. Limit executive asks to the few consequential choices; link deeper analysis.
6. **Check consistency and fit.** Test the headline against each row, then against current decisions. Tailor detail, not facts. Use the [template](template.md), but do not fill sections that add no decision value. For a requested one-screen executive update, aim for 150–250 words and at most three material asks; put detailed arithmetic and diagnostic evidence in an appendix.
7. **Preserve the dated record.** Record author/source references and compare with the previous report. Correct errors transparently. Drafting is not sending, and acknowledgment of a report is not approval of its recommendations. Update linked decision/change records only when actual decisions occur.

Quality check: every confident claim has a source or calculation; every forecast has an assumption/as-of; every baseline has authority; every material blocker survives into the headline or clear decision section. “No decision needed” is acceptable when supported, not a default used to avoid difficult asks.

## Examples

- [Relay executive update and evidence appendix](examples/software.md): a 120k forecast remains distinct from B1 and funding permission.
- [Northstar intervention report](examples/migration.md): a reserve does not eliminate the total-envelope gap or prove a new cutover date.

## Common Pitfalls

- **Green headline, red gate:** a failed acceptance condition is hidden below healthy metrics. Rewrite the headline around the consequential blocker and decision.
- **Baseline laundering:** the newest forecast replaces the approved date. Restore separate columns and the actual change reference.
- **Activity theatre:** meeting and task counts imply accepted delivery. Name observable results and acceptance state, or label the work in progress.
- **False precision:** an interface delay becomes an identical whole-project delay. Show the local gap and missing network/capacity analysis.
- **Ask without authority:** “leadership help” reaches no accountable decider. State the choice, role and window; keep unknowns explicit.
- **Overgrown executive brief:** every control detail crowds out intervention. Keep the short report, link an evidence appendix and preserve the same facts.

## References

- [DOE earned-value overview](https://www.energy.gov/documents/integrated-project-management-using-earned-value-management-system) and [Project Budget](../project-budget/SKILL.md) support indicator interpretation.
- [Project Health Diagnostic](../project-health-diagnostic/SKILL.md), [Escalation Brief](../escalation-brief/SKILL.md) and [Decision Log](../decision-log/SKILL.md) are optional handoffs for diagnosis, action and authority.
