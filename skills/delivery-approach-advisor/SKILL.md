---
name: delivery-approach-advisor
argument-hint: '[delivery context and constraints]'
description: Choose and tailor predictive, agile or hybrid practices. Use when uncertainty, feedback, dependencies
  and governance need to fit one delivery approach.
intent: Recommend an explicit operating approach, with learning loops, controlled boundaries and evidence for reassessment.
type: interactive
theme: initiation-and-governance
best_for:
  - Recommend an explicit operating approach, with learning loops, controlled boundaries and evidence for reassessment.
scenarios:
  - Requirements will evolve, but cutover needs formal approval. Recommend suitable delivery practices and explain
    the tradeoffs.
estimated_time: Depends on evidence and project scope
frameworks: Predictive/agile/hybrid tailoring; rolling-wave planning
domain: software-it-project-management
version: 2.0.0
---
# Delivery Approach Advisor

## Purpose

Select practices that help this project learn and deliver within its real constraints. Produce a recommendation with operating rules, alternatives, an early trial and review triggers. Use at initiation or when the current approach delays feedback, creates false certainty or leaves decisions unclear.

The decision is not which methodology label the team should defend. It is which work can be planned reliably, which uncertainty needs feedback, which interfaces need coordination and which commitments require authorization. Different workstreams can need different practices, provided their handoffs and decision rights remain clear.

## Input

Bring the desired outcome, what is uncertain, feedback access, team/dependency structure, delivery constraints and approval requirements. Use inline answers directly. With partial or no input, start from the decision the user needs rather than asking them to choose a methodology first.

Example: “Our migration has a fixed cutover window, uncertain data quality and weekly access to business users. What approach fits?” Offer guided, context-dump or best-guess mode. Guided mode asks one material question at a time; context-dump mode skips answered questions; best guess produces a provisional recommendation and marks its assumptions.

## Key Concepts

### Four separate dimensions

| Dimension | What to learn | Consequence for practices |
|---|---|---|
| Requirement/technical uncertainty | Which behavior or feasibility is still unknown? | Use experiments, thin increments or rehearsals where they can resolve the unknown |
| Feedback latency | Who can inspect a usable result, and how often? | A short iteration without real feedback may create activity without learning |
| Coordination constraints | Which vendors, resources, environments or windows govern handoffs? | Use explicit dependencies, near-term sequencing and commitment checks |
| Governance boundary | Which scope, money, quality and date decisions are delegated? | Retain actual approval and acceptance gates regardless of iteration cadence |

A fixed deadline does not make requirements known. A mandatory gate does not prohibit incremental evidence collection. A team that meets every two weeks is not necessarily practicing Scrum. Describe actual practices and accountabilities before applying a framework name.

### Compare approaches by fit and cost

Predictive planning is useful when important scope and interfaces are sufficiently understood and coordination changes are costly. It makes sequence and control explicit, but loses value when detailed plans disguise unresolved discovery. Agile practices use usable increments and feedback to adapt; they need enough feedback access and capability to turn learning into changed work. Hybrid delivery intentionally combines adaptive work with controlled interfaces or milestones; it fails when “hybrid” leaves everyone unsure who may change what.

Rolling-wave planning gives near-term work executable detail and later work an honest planning horizon with review points. It does not mean every commitment is provisional forever. Preserve approved boundaries while updating the forecast and seeking decisions when evidence changes feasibility.

## Application

Ask up to four adaptive questions, using what is already supplied. Stop early when the decision is sufficiently supported. At an interruption, answer the question and retain the working assumptions rather than restarting the interview.

### Question 1: What must this approach decide?

1. Establish the delivery approach for a new project.
2. Repair a current process that is not producing useful feedback or reliable handoffs.
3. Coordinate workstreams with different uncertainty and approval needs.

Capture the intended outcome and the practical failure of the current approach, if any. A preference for “agile” is context, not proof of fit.

### Question 2: Where is the uncertainty, and can we learn early?

1. Scope and technical path are largely understood.
2. User behavior or requirements need observation of increments.
3. Technical/data feasibility needs experiments or rehearsals.
4. Evidence is too weak to tell; start with a bounded investigation.

Ask who can provide meaningful feedback only if not already known. If nobody is available, recommend a realistic feedback arrangement or a limited investigation rather than claiming that more iterations solve the problem.

### Question 3: What must stay coordinated or authorized?

1. Stable external interfaces or expensive shared windows.
2. A controlled release/acceptance gate with flexible implementation inside it.
3. Frequent scope decisions delegated to the team within an explicit boundary.
4. Authority or dependencies remain unclear.

Clarify targets versus approved commitments and the actual acceptance authorities. Missing delegation remains a governance action, not permission for unrestricted change.

### Question 4: Can the team operate the proposed practices?

Check available skills, usable increments, environment access, cross-team dependencies and decision latency. Ask only about the constraint that could reverse the recommendation. A proposed practice that requires unavailable user access or scarce reviewers needs a different cadence or enabling action.

### Recommendation and implementation

Offer numbered alternatives with a preferred one:

1. **Predictive emphasis:** establish bounded scope, dependency logic and review gates; revise forecasts when evidence changes.
2. **Adaptive emphasis:** define inspectable increments, feedback owner/cadence and scope-ordering authority; keep acceptance and funding limits explicit.
3. **Deliberate hybrid:** name the adaptive work, controlled interfaces/gates and handoff between them. Do not use the label as the explanation.
4. **Investigate first:** timebox the dominant unknown with a proposed owner, evidence question and next decision, without pretending it estimates the whole project.

Tailor the selected option into a practice table: workstream, planning horizon, feedback artifact, decision owner, controlled boundary and exit evidence. Define a small trial and observable signals for revisiting the approach, such as repeated unusable increments, unresolved interfaces or a review queue that dominates elapsed time. Use [the recommendation template](template.md). The handoff to kickoff/planning is the explicit operating agreement, not a methodology slogan.

## Examples

- [Relay tailored delivery](examples/software.md): iterative integration inside defined pilot scope and independent acceptance.
- [Northstar rehearsal-led hybrid](examples/migration.md): uncertain data quality with controlled cutover and service transfer.

## Common Pitfalls

- **Agile by calendar:** ceremonies exist but no usable result is inspected. Define the increment and feedback decision each cycle must support.
- **Fixed date means fixed knowledge:** discovery is hidden to defend the target. Investigate uncertainty and show the tradeoff to the actual authority.
- **Hybrid as ambiguity:** work can be changed by anyone at any time. State which decisions are local and which alter approved boundaries.
- **Feedback without access:** a plan relies on users or reviewers who are unavailable. Secure a credible feedback route or acknowledge the resulting limitation.
- **Methodology as identity:** the team defends the label despite poor results. Agree observable trial/review criteria before adopting the practices.

## References

- [Scrum Guide](https://scrumguides.org/scrum-guide.html): use Scrum terminology consistently with its actual accountabilities and commitments.
- [Workshop Facilitation](../workshop-facilitation/SKILL.md): optional guided/context-dump interaction support.
- [Project Kickoff](../project-kickoff/SKILL.md), [Integrated Project Planning](../integrated-project-planning/SKILL.md), [Project Governance](../project-governance/SKILL.md): turn the recommendation into coordinated work.

If adjacent skills are unavailable, deliver the practice, boundary, owner and evidence table directly.
