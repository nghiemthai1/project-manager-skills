---
name: project-health-diagnostic
description: "Diagnose project health from scope, schedule, cost, quality, capacity, and evidence confidence. Use when status is disputed, incomplete, or inconsistent."
metadata:
  type: interactive
  domain: software-it-project-management
  version: "1.0.0"
---
# Project Health Diagnostic

## Purpose

Find the delivery condition that most needs attention and explain the evidence behind it. Use when reports contradict one another or a project appears healthy despite unresolved concerns. A diagnostic is a decision aid, not a certified audit or a universal scoring model.

## Input

Bring the as-of date, baseline, current reports, forecast, acceptance evidence, risks/issues, and decisions.

Example: "Our dashboard is green but release acceptance is incomplete. Diagnose the real condition."

With sparse evidence, produce a confidence-aware diagnostic and a short list of information that would change the conclusion.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Health and confidence

Health describes the assessed condition relative to objectives and tolerances. Confidence describes how well the evidence supports that assessment. Unknown is not green, and a confidently reported forecast can still be bad news.

Review scope, schedule, cost, quality/acceptance, resources, and material risks separately. The overall narrative should reflect the consequential constraint, not an average that cancels a failed gate with cheap spending.

### Tolerance-based review

Use actual agreed thresholds or explicitly provisional criteria. RAG is a communication shorthand; it should summarize an explained decision about intervention. A cost ratio alone does not establish schedule readiness. A stable backlog does not prove the right scope is accepted.

### Why this works

Triangulating baseline, actual evidence, and current forecast exposes inconsistencies a single dashboard hides. Separating missing evidence from poor performance also identifies whether the next step is investigation or intervention.

## Application

1. Establish the decision and as-of date. Ask only missing context that changes the diagnosis, normally at most three to five questions.
2. Confirm the baseline and tolerance authority. Separate proposed revisions from approved ones.
3. Review each dimension with evidence, variance, trend, confidence, and consequence. Reconcile contradictory sources rather than choosing the more favorable one.
4. Identify the binding delivery constraint and any independent gate failure. Do not average these away.
5. Distinguish symptoms from causal hypotheses. Ask what evidence would confirm or disprove the suspected cause.
6. Recommend the next intervention or evidence request, responsible role, and review trigger. Keep recovery options separate from claimed recovery success.
7. Produce a concise diagnostic with knowns, unknowns, and the decision needed. Route material recovery work to a dedicated recovery plan.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Composite green:** healthy spending masks a failed acceptance condition. Surface the gate independently.
- **Confidence as health:** detailed reporting is mistaken for good performance. Assess the condition and evidence quality separately.
- **Missing means fine:** blank risk fields become zero risk. Show the unknown and the decision it prevents.
- **Symptoms as causes:** lateness is attributed to low effort without evidence. Test capacity, scope, dependencies, and acceptance hypotheses.
- **Universal thresholds:** an arbitrary CPI band becomes policy. Use agreed tolerances or label the interpretation provisional.

## References

- [Earned value interpretation](https://www.energy.gov/documents/integrated-project-management-using-earned-value-management-system)
- [Status Report](../status-report/SKILL.md)
- [Project Recovery Advisor](../project-recovery-advisor/SKILL.md)
- [Project Budget](../project-budget/SKILL.md)
- [Release Readiness](../release-readiness/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
