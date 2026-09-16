---
name: benefits-realization
argument-hint: '[benefit hypotheses and measured outcomes]'
description: Define and verify benefits after project delivery. Use when outputs need to be connected to owned,
  measurable business outcomes and review decisions.
intent: Carry benefit hypotheses from a business case into measured outcomes and accountable post-project decisions.
type: workflow
theme: transition-and-outcomes
best_for:
  - Carry benefit hypotheses from a business case into measured outcomes and accountable post-project decisions.
scenarios:
  - 'Use benefits-realization: Carry benefit hypotheses from a business case into measured outcomes and accountable
    post-project decisions.'
estimated_time: Depends on evidence and project scope
frameworks: Benefits map; leading/lagging measures; ownership and review plan
domain: software-it-project-management
version: 2.1.0
---
# Benefits Realization

## Purpose

Establish whether the delivered change produces the intended business value, for whom and at what ongoing cost. Produce a benefits map, measurement profiles, an accepted ownership handoff and a review decision. Use during business-case/planning work and after delivery; benefits may take longer to emerge than the project takes to close.

Delivery, acceptance, adoption and benefits answer different questions. A system can be accepted and used without reducing handling time or improving reliability. The workflow should reveal that result, not reinterpret every completed deliverable as a realized benefit.

## Input

Bring the business-case claims, delivered capability, affected population, current performance baseline, intended measures/targets, operational costs, data access, business owners and review dates. Use supplied context without re-asking. Missing baselines permit a measurement plan, not an invented before-and-after result. With no input, ask which outcome the project was intended to improve.

Example: “The migration is handed over. Help Saira prepare the January benefit review without claiming that go-live proves faster service.” An owner or review date is factual only when supported by the project record; otherwise label it proposed.

## Key Concepts

### Trace the causal claim

Use a chain: delivered output → usable capability → changed behavior/process → outcome → benefit against a stated objective. For example, a new searchable guide is an output; operators finding the right procedure is behavior; less rework is an outcome; released support capacity may be a benefit. Each arrow is a hypothesis that needs evidence. A benefit map makes dependencies visible but does not prove causation.

Name disbenefits and operating costs as well as gains. Faster handling may coincide with more reopened tickets; reduced project cost may shift effort into operations. Avoid counting the same time saving as both a full cash saving and full capacity gain, or claiming it twice across overlapping projects.

### Define a measurement profile before announcing success

A profile states the beneficiary/cohort, exact measure, numerator/denominator where relevant, source, baseline period, target basis, observation window, owner and review decision. Leading measures such as successful task adoption can explain later outcomes; lagging measures such as rework or cost establish what changed. Neither type alone proves the other.

Keep definitions and populations comparable. If volume, case complexity, staffing or instrumentation changes, explain the effect and whether the comparison remains usable. A before/after difference may be consistent with the project hypothesis while also having alternative explanations. Use an appropriate comparison group or other evaluation method when the consequence warrants it; do not imply a controlled experiment when none occurred.

### Ownership survives the project

A benefit owner needs influence over the operating process, access to the measure and a route to act when results disappoint. Assigning a name in a closure report is not accepted ownership. Project management can coordinate the handoff; the enduring business/service owner is usually better placed to inspect results and change operations. Follow actual governance rather than assuming a title grants all authority.

## Application

### Phase 1: Define the benefit hypothesis

Input: business case, objective and affected population. Output: causal map, material benefits/disbenefits and assumptions. Separate deliverables from outcomes and monetized from unmonetized value. Exit when each material claim has a meaningful beneficiary and measure, or an explicit measurement-design question.

### Phase 2: Establish baseline and plan

Input: candidate profiles and available data. Check definitions, comparability, data quality and permissions. Output: baseline evidence or a labeled gap, target rationale, collection plan and proposed owner/review date. Exit when the review can be performed credibly; if historical data are missing, start a prospective baseline or an explicitly limited alternative rather than reconstructing invented history.

### Phase 3: Confirm enablement and handoff

Input: actual delivered scope, acceptance, adoption conditions and ongoing costs. Update the hypothesis for authorized scope changes without erasing the original case. Output: accepted business ownership, measurement access, outstanding actions and review cadence. Exit when receiving owners accept their responsibilities; technical handover alone does not complete this phase.

### Phase 4: Measure and interpret

Input: dated observations and comparable baseline. Calculate the stated measure, expose missing populations and check disbenefits. Output: observed outcome, uncertainty and possible alternative explanations. Distinguish realized, partly realized, not realized and not yet measurable; do not turn “not measured” into zero or success.

### Phase 5: Decide and sustain

Input: review evidence and residual hypothesis. Output: keep, adjust, investigate, stop or scale recommendation, decided by the actual authority with action ownership. Retain prior profiles and reports. Close benefit tracking only when the agreed review/ownership conditions are satisfied; a project closure date does not automatically end outcome accountability.

Use [the benefits template](template.md). A good review can answer what changed, compared with what, whether the comparison is credible, what costs or harms accompany it and who will act next. Adjacent skills are optional; keep those fields even without the rest of the library.

### When producing a visual

Use the [benefit chain and measured outcome comparison](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the project source’s evidence and uncertainty in the graphic.

## Examples

Optional worked applications:

- [Relay support-capacity hypothesis](examples/software.md): a dated handoff plus a separate illustrative review that distinguishes time capacity from cash.
- [Northstar service outcomes](examples/migration.md): a weak baseline limits the claim even when migration is accepted.

## Common Pitfalls

- **Go-live equals benefit:** completion is substituted for the intended business outcome. Measure the receiving process after adoption and state what is still unknown.
- **Baseline invented after the fact:** estimates of the old process are presented as observations. Label reconstruction, test sensitivity and avoid unsupported exact gains.
- **Metric definition moves:** a new cohort or excluded difficult cases make performance appear better. Retain definitions and disclose comparability changes.
- **Savings without a mechanism:** time reduction is multiplied by salary and called cash. State released capacity separately; cash release needs an actual spending change.
- **Owner by name only:** closure assigns someone without accepted responsibility or data access. Complete the handoff and identify the ongoing decision route.
- **Unfavorable results disappear:** reviews stop when benefits fall short. Record the outcome and decide whether to adjust, investigate or stop.

## References

- [Project Business Case](../project-business-case/SKILL.md): original investment hypothesis and options.
- [Organizational Change](../organizational-change/SKILL.md): adoption conditions and reinforcement.
- [Project Closure](../project-closure/SKILL.md): accepted residual obligations and benefit handoff.
- [GovS 002 Project Delivery](https://www.gov.uk/government/publications/project-delivery-functional-standard): reference for connecting delivery, outcomes and ongoing ownership; not a compliance claim.
