---
name: lessons-learned
description: Capture reusable learning with evidence, context and limits. Use when a milestone, experiment or project
  outcome should inform another team or future delivery.
metadata:
  type: component
  domain: software-it-project-management
  version: 2.0.0
  intent: Turn observed project outcomes and bounded improvement results into contextual lessons, separate practice
    maturity from aspiration and define a verifiable adoption action.
  frameworks: After-action review; contextual lessons; knowledge transfer
  best_for: '["Turn observed project outcomes and bounded improvement results into contextual lessons, separate
    practice maturity from aspiration and define a verifiable adoption action."]'
  scenarios: '["Turn this completed project experience into a transferable lesson with context, evidence, limits
    and an adoption route."]'
  estimated_time: Depends on evidence and project scope
---
# Lessons Learned

## Purpose

Help another project apply learning without repeating the mistake or misapplying the remedy. Produce a lesson card with context, evidence, mechanism or hypothesis, applicability limits and an adoption proposal. A slogan or success story does not explain what a future team should do differently.

Use at milestones, after an experiment or at closure. The retrospective develops local improvement hypotheses; this skill makes the evidenced learning transferable. An observed failure can teach a valid limit even when the proposed remedy is untested. Keep those two knowledge states separate.

## Input

Use the objective, expected/actual outcome, dated decisions, constraints, evidence, retrospective experiments and observed results. Include failures, counterexamples and later changed conditions. Preserve exact source IDs, versions and links so the lesson remains auditable.

Example: “Capture what the migration taught us about count reconciliation, relationship correctness and the limits of the proposed new tests.”

Missing results do not prevent a draft; label the recommendation proposed. Do not claim an action was adopted, tested widely or field-proven without evidence. Reuse supplied context instead of demanding a formal postmortem before helping.

## Key Concepts

### After-action review supplies the evidence chain

Ask what was expected, what happened, why the difference might have occurred, and what should be repeated or changed. The first two need observable evidence; the causal explanation may remain a hypothesis. Preserve constraints and information available at the time so hindsight does not turn an uncertain decision into negligence.

### Transfer requires conditions and counterconditions

A useful lesson states: in this context, this mechanism or limit matters; consider this practice when these conditions hold; do not assume it works when these other conditions differ. For example, count checks can support population completeness while failing to prove relationship correctness. The transferable principle is to test the required property, not to abandon counts everywhere.

State counterconditions: different failure mechanisms, scale, governance, data, resources or timing may require another approach. If the remedy adds cost, review burden or risk, include it rather than presenting learning as a free improvement.

### Maturity is more than a publication label

| Practice state | Evidence required | Claim to avoid |
|---|---|---|
| Proposed from observed evidence | Defined rationale and contextual observation | “Proven solution” |
| Tested in a bounded case | Actual implementation/result and comparison limits | Universal causation or reliability |
| Adopted in a stated setting | Actual owner/process change and use evidence | Adoption everywhere or guaranteed benefit |
| Revised/superseded | New evidence and reason for changed guidance | Erasing prior result/history |

Document lifecycle (draft/stable/deprecated) and practice state are different. A polished published lesson may still recommend an untested practice. Multiple simultaneous improvements and favorable outcomes do not identify which change caused the benefit.

### Adoption needs a changed behavior and review

Name the relevant template, control, decision or training behavior to change, the actual or proposed owner, the receiving context and the check for usefulness. Publishing a card is distribution, not adoption. A completed template edit shows implementation, not effect.

## Application

1. **Select a consequential bounded finding.** State the learning question and event/objective. Recover relevant evidence, chronology and original information limits. Avoid combining unrelated mechanisms into a broad “communicate/test better” lesson.
2. **Separate the chain.** Record observation, interpretation, intervention, actual result and remaining uncertainty. If a practice was never tried, leave its result absent. Include contrary evidence and failed experiments; do not retain only victories.
3. **Write the principle and limits.** Explain what a future practitioner can infer, where it applies, where it may fail and what to inspect before adopting it. Distinguish a logic-based insufficiency finding from an empirical claim that a remedy improves outcomes.
4. **Assign practice maturity.** Use the evidence table, not enthusiasm. A single synthetic example cannot justify “battle-tested.” Preserve original and later versions if the lesson changes.
5. **Define adoption and evaluation.** Use the [lesson template](template.md) to specify the proposed change, recipient, owner, effort/tradeoff, review measure and guardrail. Confirm ownership before reporting it accepted. Select outcome measures that do not reward concealing failures or weakening criteria.
6. **Make it findable and revisit.** Link to the source decisions/results and the relevant process/template. Record actual distribution, use and outcomes when they happen. At review, refine, retain or supersede with evidence; a failed transfer may identify a missing contextual condition rather than invalidate every part of the lesson.

Quality check: the reader can identify both the useful rule and the limit on its evidence. Recommendations are actionable and bounded; claims of adoption/effect have actual records. A lesson may end with “test this next” when that is the honest state.

## Examples

- [Relay acceptance-evidence lesson](examples/software.md): an observed gate failure informs a proposed planning practice, not a proven meeting cadence.
- [Northstar reconciliation lesson](examples/migration.md): count equality has a valid but limited role; relationship checks need their own coverage and adoption evidence.

## Common Pitfalls

- **Slogan lesson:** “test earlier” leaves the method and timing unexplained. Name the failure property, evidence lead time and decision it serves.
- **Victory bias:** only successful responses are recorded. Preserve failures and conditions that made a practice ineffective.
- **Universal cure:** one project's workaround becomes policy everywhere. State applicability, counterconditions and costs.
- **Causality inflation:** improvement after a change proves that change caused it. Record confounders and comparison limits.
- **Publication means adoption:** a repository entry is called organizational change. Verify actual use and effect separately.
- **Maturity by adjective:** “proven” replaces validation. Use the observed practice state and evidence boundary.

## References

- [Retrospective](../retrospective/SKILL.md) supplies local experiments; [Acceptance and Traceability](../acceptance-and-traceability/SKILL.md) supports evidence applicability.
- [Project Closure](../project-closure/SKILL.md) and [Organizational Change](../organizational-change/SKILL.md) receive learning and adoption actions. These are optional handoffs, not hidden dependencies.
