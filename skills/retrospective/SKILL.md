---
name: retrospective
argument-hint: '[observations, outcomes, and improvement goals]'
description: Turn delivery observations into a few testable improvements. Use after an iteration, rehearsal or milestone
  when the team needs evidence-based learning and follow-through.
intent: Create a retrospective record that separates observations, causal hypotheses and bounded improvement experiments,
  with ownership, measures and an actual review loop.
type: component
theme: transition-and-outcomes
best_for:
  - Create a retrospective record that separates observations, causal hypotheses and bounded improvement experiments,
    with ownership, measures and an actual review loop.
scenarios:
  - Facilitate a team review of observed work and choose a small improvement experiment with an owner and measure.
estimated_time: Depends on evidence and project scope
frameworks: PDCA; 5 Whys with evidence; experiment design
domain: software-it-project-management
version: 2.1.0
---
# Retrospective

## Purpose

Help a team understand how work happened and choose a practical improvement. Produce an evidence record and one to three feasible experiments. Use after a Sprint, rehearsal, milestone or meaningful delivery event; the number of suggestions is not the measure of success.

This is not an individual performance ranking, a substitute for a formal incident investigation, or proof of one root cause. A lessons-learned artifact later makes bounded findings reusable by other projects. First establish whether the proposed change actually helps this team.

## Input

Use the period/goal, expected and actual outcomes, event timeline, participant perspectives, relevant data and previous improvement actions. Include what went well and near misses, not only visible failures. Preserve exact IDs and dated evidence. Conflicting recollections remain conflicting until evidence resolves them.

Example: “Review the failed rehearsal and select one improvement that would detect the relationship problem earlier.”

With no raw material, ask for the event and learning question. With supplied notes, begin from them. Mark missing perspectives, ownership or measurements; do not invent attendance, motives, admissions or team consensus. Preparing an agenda does not schedule or send invitations.

## Key Concepts

### Observation, interpretation and experiment

An observation states what happened with its evidence. An interpretation proposes why. An experiment tests a change meant to affect that mechanism. “Review happened late” is different from “reviewers did not care,” and neither by itself proves that more meetings will improve readiness.

Retain alternative explanations and counterevidence. A later good result may reflect a simpler release, extra capacity or chance. Attribution should match the evidence, especially with small samples or multiple changes at once.

### Choose a method for the question

| Method | Useful when | Limit to preserve |
|---|---|---|
| Timeline | Sequence, handoffs or changing information matter | A chronology alone does not prove causation |
| Start/Stop/Continue | The team needs a quick way to organize candidate behavior changes | Suggestions still need evidence, feasibility and a test |
| Five Whys | A specific observed problem has a plausible mechanism to investigate | Do not force exactly five levels, one root cause or blame; verify each link |
| PDCA | The team can try a bounded change and review its effect | “Do” without “Check/Act” is implementation, not demonstrated learning |

In Plan–Do–Check–Act, define the hypothesis and measurement, try the change within authority, inspect actual results, then adopt, adjust or stop. Failure is useful evidence about limits and should remain in history.

### A useful experiment can be inspected

Specify the changed behavior, population/work boundary, proposed owner, resource/time limit, expected mechanism, baseline/comparison, measure, guardrail and review point. A guardrail prevents an apparent improvement from hiding harm—for example, fewer late gate gaps must not come from suppressing reports or weakening criteria.

Distinguish process execution from outcome: a review meeting held is implementation evidence; earlier discovery of material gaps is an outcome to inspect. Neither automatically proves the practice caused improvement.

## Application

1. **Set the learning boundary.** State event/period, intended outcome and the question to answer. Review earlier experiments and their actual outcomes before creating new actions. Establish respectful discussion and appropriate evidence handling; examine decisions and constraints without assigning motives.
2. **Gather observations before debate.** Invite independent input, then build a dated timeline or other fitting structure. Keep facts, recollections and hypotheses visibly distinct. Include missing/contradictory evidence and absent perspectives; a loud majority does not settle source truth.
3. **Explore mechanisms.** Select a few consequential observations. Ask what system condition, handoff, decision or assumption could produce them, what contrary evidence exists and what check would discriminate among explanations. Use Five Whys only when each step remains testable.
4. **Choose feasible experiments.** Compare candidate changes by relevance, expected learning, effort, authority and risk. Select one to three that fit actual capacity. Mark owners and dates proposed until accepted. Mandatory remediation may already be required work; do not reclassify it as optional experimentation.
5. **Write the experiment contract.** Use the [template](template.md). Define what will change, why it may work, what evidence to collect and what would justify adoption, adjustment or stopping. If no baseline exists, plan initial measurement instead of inventing a percentage improvement target.
6. **Put the change into work.** Hand accepted experiments to the actual backlog/control plan with resources and review. Drafting a retrospective does not assign live tasks or alter a required gate. Preserve dissent and reasons for not selecting other suggestions.
7. **Close the learning loop.** At review, record whether the change was implemented, observed result, comparison limits and unintended effects. Choose adopt, adjust, stop or gather more evidence. If no results are supplied, leave the experiment proposed/in progress; never fabricate a successful review to complete the story.

Quality check: a future reviewer can distinguish what happened, what is only suspected, what changed and what evidence supports the next action. A concise record can contain open questions; forced consensus or a long action list weakens it.

### When producing a visual

Use the [evidence timeline or cause map](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay acceptance-planning experiment](examples/software.md): test earlier evidence visibility rather than blame security.
- [Northstar relationship-check experiment](examples/migration.md): define the defect a test must detect and preserve separate restore concerns.

## Common Pitfalls

- **Blameless means unexamined:** decisions and constraints are never discussed. Review accountable actions with evidence while avoiding personal accusation.
- **Why-chain certainty:** an appealing narrative becomes proven cause. Check each causal link and alternatives.
- **Action avalanche:** fifteen ideas compete with delivery and none finish. Select a small feasible set with accepted capacity.
- **Metric rewards concealment:** fewer reported problems is called improvement. Add coverage/transparency guardrails and inspect missed conditions.
- **Meeting held means success:** execution of the new process becomes its outcome. Measure the intended effect separately.
- **Repeated amnesia:** prior experiments disappear. Start each review with their actual results and unresolved decisions.

## References

- [ASQ PDCA](https://asq.org/quality-resources/pdca-cycle) provides the improvement-cycle context.
- [Workshop Facilitation](../workshop-facilitation/SKILL.md) supports a difficult conversation; [Lessons Learned](../lessons-learned/SKILL.md) captures bounded reusable findings.
- [Sprint Planning](../sprint-planning/SKILL.md) and [Delivery Control Cycle](../delivery-control-cycle/SKILL.md) receive accepted improvement work. These are optional handoffs.
