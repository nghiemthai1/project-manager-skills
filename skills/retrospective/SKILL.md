---
name: retrospective
description: "Facilitate and document an evidence-based delivery retrospective with a small set of owned improvement experiments. Use after an iteration, milestone, or project event."
metadata:
  type: component
  domain: software-it-project-management
  version: "1.0.0"
---
# Retrospective

## Purpose

Help a team learn from how work happened and choose a practical improvement. Use after a Sprint, rehearsal, milestone, or incident-related delivery cycle. A retrospective is not a performance ranking or a substitute for a formal incident investigation.

## Input

Bring the goal, period, observable outcomes, timeline, participant perspectives, and previous improvement actions.

Example: "Run a retro on the failed migration rehearsal and select one improvement to test."

If perspectives conflict, preserve the disagreement and seek evidence instead of forcing consensus.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Observation, interpretation, experiment

An observation is what happened. An interpretation explains why. An experiment tests whether a change improves the situation. Keeping these separate prevents a plausible story from becoming an established root cause.

Start/Stop/Continue is useful for quickly organizing suggestions. A timeline helps when sequence matters. Five Whys can explore a causal hypothesis, but does not prove one root cause or justify blaming the last person in the chain. Use the method that fits the question.

### Closed learning loop

An improvement needs an owner, a bounded change, a success measure, and a review point. In a Plan-Do-Check-Act pattern, the review determines whether to adopt, adjust, or stop the experiment.

### Why this works

Small observable experiments are easier to execute and evaluate than broad promises such as "communicate better." Reviewing earlier actions prevents retrospectives from repeatedly producing the same untested list.

## Application

1. Agree the period, learning question, and discussion boundaries. Review prior improvement actions and their evidence.
2. Gather observations independently before interpreting them. Use a timeline or another appropriate structure.
3. Separate facts from hypotheses and identify missing perspectives. Discuss system conditions, decisions, and constraints without inventing motives.
4. Select a small number of consequential themes. Evaluate alternatives rather than treating the first suggestion as the answer.
5. Define one to three feasible experiments with owner, expected effect, measurement, and review point. Label proposed assignments until accepted.
6. Produce the retrospective artifact and carry improvements into actual planning.
7. At the review, compare observed results with the hypothesis and adopt, adjust, or stop. Preserve failed experiments as learning rather than deleting them.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Blameless means consequence-free:** decisions and constraints are never examined. Discuss evidence and accountable actions without personal accusations.
- **Five Whys certainty:** a conversational chain is declared a proven root cause. Validate the hypothesis against alternative explanations.
- **Action avalanche:** fifteen improvements compete with delivery. Select a small feasible set.
- **No measurement:** "better communication" cannot be checked. Define the changed behavior and observable result.
- **Repeated amnesia:** last retro's actions vanish. Start with their outcomes.

## References

- [Scrum Guide: retrospective purpose](https://scrumguides.org/scrum-guide.html)
- [Lessons Learned](../lessons-learned/SKILL.md)
- [Sprint Planning](../sprint-planning/SKILL.md)
- [Delivery Control Cycle](../delivery-control-cycle/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
