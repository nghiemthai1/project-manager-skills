---
name: risk-workshop
description: "Facilitate a focused project risk review using objectives, a premortem, evidence-based assessment, and owned responses. Use before a major plan or gate."
metadata:
  type: interactive
  domain: software-it-project-management
  version: "1.0.0"
---
# Risk Workshop

## Purpose

Identify risks that change project decisions and convert them into responses. Use before commitment, at a major change, or when a risk register has become stale. A workshop should improve choices rather than maximize the number of entries.

## Input

Bring objectives, scope, constraints, the current plan, known incidents, and participant perspectives.

Example: "Run a risk workshop before we accept the migration cutover plan."

For guided use, establish the decision, most uncertain area, and available evidence with a few focused questions. Do not demand a complete risk register before helping create one.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Premortem and objective-based review

A premortem asks participants to imagine a future failure and explain plausible causes. It helps surface concerns that optimism or hierarchy suppresses. Its stories are hypotheses, not facts or measured probabilities. Pair it with a structured review of schedule, cost, scope, quality, operations, people, vendor, and change risks relevant to the project.

### Assess before scoring

Use cause-event-consequence statements. Distinguish likelihood, impact, proximity, detectability, and evidence quality rather than hiding them in one unsupported score. Define qualitative scales before ranking. A low-probability catastrophic event may merit action even if a simple product score is modest.

### Response choices

Avoid by changing the plan; mitigate by reducing likelihood or consequence; transfer or share a contractual exposure without pretending accountability disappears; accept within authority with a contingency and trigger.

### Why this works

Independent first-pass thinking broadens the concerns raised. An owned response with a trigger turns discussion into control, while a stated uncertainty prevents invented precision.

## Application

1. Establish the decision being protected and the review boundary. Ask only missing material context, normally three to five questions at most.
2. Invite independent risk ideas before group discussion. Use a premortem prompt and objective-based categories to expose overlooked areas.
3. Consolidate duplicates while preserving distinct causes and consequences. Move present problems into issues.
4. Agree assessment criteria and assess evidence, likelihood, impact, timing, and confidence. Keep unknown values unknown.
5. Select responses for the most consequential risks. Record owner, action, early-warning trigger, contingency, and residual exposure.
6. Identify who must accept residual risks outside team authority. Draft the decision request instead of approving it yourself.
7. Produce the prioritized risk record and follow-up review. Explain why lower-priority items receive less attention and what would promote them.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Premortem becomes prediction:** a plausible story is assigned a fabricated probability. Record it as a hypothesis and seek evidence.
- **Ranking without scale:** participants score the same impact differently. Define objectives and category meanings first.
- **Mitigation without trigger:** an action has no signal for escalation. State when it starts and what indicates it is failing.
- **Transferred means gone:** a vendor contract is assumed to remove business consequences. Record the residual operational exposure.
- **Workshop ends at the list:** no one changes a plan. Assign follow-up and decision authority.

## References

- [Risk management principles](https://www.gov.uk/government/publications/orange-book)
- [Raid Log](../raid-log/SKILL.md)
- [Release Readiness](../release-readiness/SKILL.md)
- [Project Recovery Advisor](../project-recovery-advisor/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
