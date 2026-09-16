---
name: prioritization-advisor
argument-hint: '[options, constraints, and decision criteria]'
description: Choose a scope prioritization method that fits evidence and constraints. Use when optional project
  work competes for limited time, funding or capacity.
intent: Recommend and apply a defensible prioritization method while preserving mandatory acceptance and decision
  rights.
type: interactive
theme: scope-and-planning
best_for:
  - Recommend and apply a defensible prioritization method while preserving mandatory acceptance and decision rights.
scenarios:
  - 'Use prioritization-advisor: Recommend and apply a defensible prioritization method while preserving mandatory
    acceptance and decision rights.'
estimated_time: Depends on evidence and project scope
frameworks: MoSCoW; RICE; weighted scoring; Cost of Delay; value/effort; Kano
domain: software-it-project-management
version: 2.1.0
license: CC-BY-NC-SA-4.0
---
# Prioritization Advisor

## Purpose
Guide project managers in choosing the right prioritization framework by asking adaptive questions about delivery context, team context, decision-making needs, and stakeholder dynamics. Use this to avoid "framework whiplash" (switching frameworks constantly) or applying the wrong framework (e.g., using RICE for strategic bets or ICE for data-driven decisions). Outputs a recommended framework with implementation guidance tailored to your context.

This is not a scoring calculator—it's a decision guide that matches prioritization frameworks to your specific situation.

## Input

**Works best with:** What you're trying to prioritize and why now (scope tradeoff, backlog ordering, dependency sequencing).
**Also useful:** Delivery context, decision authority, mandatory commitments, team size, data availability, and frameworks you've tried that failed.

Anything supplied with the invocation itself — text after the skill name, a pasted context dump — counts as answers already given. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** The advisor opens by asking about your delivery context and the decision you need the framework to make.

**Example invocation:** `Help me pick a framework: SSO pilot, a fixed target date, mandatory recovery evidence, optional operator improvements and limited capacity.`

## Key Concepts

### The Prioritization Framework Landscape
Common frameworks and when to use them:

**Scoring frameworks:**
- **RICE** (Reach, Impact, Confidence, Effort) — Data-informed, requires comparable estimates and their evidence
- **ICE** (Impact, Confidence, Ease) — Lightweight, gut-check scoring
- **Value vs. Effort** (2x2 matrix) — Quick wins vs. strategic bets
- **Weighted Scoring** — Custom criteria with stakeholder input

**Strategic frameworks:**
- **Kano Model** — Classify features by customer delight (basic, performance, delight)
- **Opportunity Scoring** — Rate importance vs. satisfaction gap
- **Buy-a-Feature** — Customer budget allocation exercise
- **MoSCoW** (Must, Should, Could, Won't) — Forcing function for hard choices

**Contextual frameworks:**
- **Cost of Delay** — Urgency-based (time-sensitive features)
- **Impact Mapping** — Goal-driven (tie features to outcomes)
- **Story Mapping** — User journey-based (narrative flow)

### Why This Works
- **Context-aware:** Matches framework to delivery context, team maturity, data availability
- **Anti-dogmatic:** No single "best" framework—it depends on your situation
- **Actionable:** Provides implementation steps, not just framework names

### Anti-Patterns (What This Is NOT)
- **Not a universal ranking:** Frameworks aren't "better" or "worse"—they fit different contexts
- **Not a replacement for strategy:** Frameworks execute strategy; they don't create it
- **Not set-it-and-forget-it:** Reassess frameworks as the project context changes

### When to Use This
- Choosing a prioritization framework for the first time
- Switching frameworks (current one isn't working)
- Aligning stakeholders on prioritization process
- Onboarding new PMs to team practices

### When NOT to Use This
- When you already have a working framework (don't fix what isn't broken)
- For a simple one-off choice where a brief options comparison is sufficient
- As a substitute for strategic vision (frameworks can't tell you what to build)

---

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the default interaction protocol for this skill.

It defines:
- session heads-up + entry mode (Guided, Context dump, Best guess)
- one-question turns with plain-language prompts
- progress labels (for example, Context Qx/8 and Scoring Qx/5)
- interruption handling and pause/resume behavior
- numbered recommendations at decision points
- quick-select numbered response options for regular questions (include `Other (specify)` when useful)

This file defines the domain-specific assessment content. If there is a conflict, follow this file's domain logic.

## Application

This interactive skill asks **up to 4 adaptive questions**, offering **3-4 enumerated options** at each step. Offer guided, context-dump or best-guess entry; a supplied context dump goes straight to the missing decision. Ask one question at a time and stop when the recommendation is adequately supported. Best guess labels uncertain ratings and does not invent authority.

---

### Question 1: Delivery Context

**Agent asks:** "What decision must this prioritization support?"

1. **Explore uncertain work** — Choose what to investigate before committing; evidence is weak.
2. **Protect a delivery boundary** — Decide which optional scope fits a date or budget while retaining mandatory acceptance.
3. **Order comparable improvements** — Choose among discretionary items with measurable reach, benefit and effort.
4. **Coordinate multiple workstreams** — Resolve dependencies and shared-capacity conflicts across a project or program.

**Or describe the decision in your own words.** Distinguish a target from an approved commitment. Identify who owns backlog order and who may change project baselines; these may be different people.

---

### Question 2: Team Context

**Agent asks:**
"What's your team and stakeholder environment like?"

**Offer 4 enumerated options:**

1. **Small team, limited resources** — "One small delivery team, limited specialist availability" (Need simple, fast framework)
2. **Cross-functional team, aligned** — "Business, operations, engineering aligned; clear goals; good collaboration" (Can use data-driven frameworks)
3. **Multiple stakeholders, misaligned** — "Execs, sales, customers all have opinions; need transparent process" (Need consensus-building framework)
4. **Large org, complex dependencies** — "Multiple teams, shared milestones, cross-team dependencies" (Need coordination framework)

**Or describe your team/stakeholder context.**

**User response:** [Selection or custom]

---

### Question 3: Decision-Making Needs

**Agent asks:**
"What's the primary challenge you're trying to solve with prioritization?"

**Offer 4 enumerated options:**

1. **Too many ideas, unclear which to pursue** — "Backlog is 100+ items; need to narrow to top 10" (Need filtering framework)
2. **Stakeholders disagree on priorities** — "Sales wants features, execs want strategic bets, engineering wants tech debt" (Need alignment framework)
3. **Lack of data-driven decisions** — "Prioritizing by gut feel; want metrics-based process" (Need scoring framework)
4. **Hard tradeoffs between strategic bets vs. quick wins** — "Balancing long-term vision vs. short-term customer needs" (Need value/effort framework)

**Or describe your specific challenge.**

**User response:** [Selection or custom]

---

### Question 4: Data Availability

**Agent asks:**
"How much data do you have to inform prioritization?"

**Offer 3 enumerated options:**

1. **Minimal data** — "New delivery context, no comparable performance data" (Gut-based frameworks)
2. **Some data** — "Basic analytics, customer feedback, but no rigorous data collection" (Lightweight scoring frameworks)
3. **Rich data** — "Usage metrics, A/B tests, customer surveys, clear success metrics" (Data-driven frameworks)

**Or describe your data situation.**

**User response:** [Selection or custom]

---

### Choose the branch from evidence

Mandatory acceptance, contractual scope and approved constraints are eligibility checks before optional scoring. A high score does not waive security or grant authority to remove committed scope. An infeasible must-have set calls for a decision about the target, resources or scope, not relabeling required work as optional.

| Decision/evidence | First choice | Why / boundary |
|---|---|---|
| Fixed delivery boundary, clear acceptance | MoSCoW | Establish viable minimum and explicit deferrals; distinguish this-timebox priorities from permanent value |
| Comparable optional improvements with usable measurements | RICE | Common reach period and effort units make comparisons interpretable |
| Several materially different decision criteria | Weighted scoring | Agree criteria, anchors and weights before seeing scores; test whether modest weight changes reverse the order |
| Time-dependent economic loss with credible estimates | Cost of Delay, optionally divided by duration | State value units and time profile; resolve prerequisites and constrained resources separately |
| Weak evidence, early exploration | Value/effort ranges or a small investigation | Expose uncertainty instead of multiplying guesses into apparent precision |

For MoSCoW, ask what happens if an item is absent: no viable/acceptable outcome supports Must; a workable but costly alternative may support Should; optional improvement supports Could; Won't this time explicitly records deferral. Do not label every request Must. Kano examines customer satisfaction patterns; it does not establish technical dependencies or mandatory acceptance.

### Output: Recommend Prioritization Framework

After collecting responses, the agent recommends a framework:

```markdown
# Prioritization Framework Recommendation

**Based on your context:**
- **Delivery Context:** [From Q1]
- **Team Context:** [From Q2]
- **Decision-Making Need:** [From Q3]
- **Data Availability:** [From Q4]

---

## Recommended Framework: [Framework Name]

**Why this framework fits:**
- [Rationale 1 based on Q1-Q4]
- [Rationale 2]
- [Rationale 3]

**When to use it:**
- [Context where this framework excels]

**When NOT to use it:**
- [Limitations or contexts where it fails]

---

## How to Implement

### Step 1: [First implementation step]
- [Detailed guidance]
- [Example: "Define scoring criteria: Reach, Impact, Confidence, Effort"]

### Step 2: [Second step]
- [Detailed guidance]
- [Define anchors appropriate to the chosen method; do not apply a universal 1–10 scale]

### Step 3: [Third step]
- [Detailed guidance]
- [Example: "Calculate RICE score: (Reach × Impact × Confidence) / Effort"]

### Step 4: [Fourth step]
- [Detailed guidance]
- [Example: "Rank by score; review top 10 with stakeholders"]

---

## Example Scoring Template

[Provide a concrete example of how to use the framework]

**Example (if RICE):**

| Feature | Reach (users/month) | Impact (1-3) | Confidence (%) | Effort (person-months) | RICE Score |
|---------|---------------------|--------------|----------------|------------------------|------------|
| Feature A | 10,000 | 3 (massive) | 80% | 2 | 12,000 |
| Feature B | 5,000 | 2 (high) | 70% | 1 | 7,000 |
| Feature C | 2,000 | 1 (medium) | 50% | 0.5 | 2,000 |

**Priority:** Feature A > Feature B > Feature C

---

## Alternative Framework (Second Choice)

**If the recommended framework doesn't fit, consider:** [Alternative framework name]

**Why this might work:**
- [Rationale]

**Tradeoffs:**
- [What you gain vs. what you lose]

---

## Common Pitfalls with This Framework

1. **[Pitfall 1]** — [Description and how to avoid]
2. **[Pitfall 2]** — [Description and how to avoid]
3. **[Pitfall 3]** — [Description and how to avoid]

---

## Reassess When

- Constraints, evidence or decision scope change
- Team grows or reorganizes
- Stakeholder dynamics shift
- Current framework feels broken (e.g., too slow, ignoring important factors)

---

**Next options:** 1. Apply the method to supplied candidates. 2. Resolve missing evidence. 3. Prepare a decision brief. Use the requested option directly when already clear.
```

---

### When producing a visual

Use the [tradeoff plot or ranked options table](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the project source’s evidence and uncertainty in the graphic.

## Examples

Optional worked applications:

- [Relay software example](examples/software.md): protect acceptance before prioritizing optional scope; a worked MoSCoW decision and a RICE sensitivity subcase.
- [Northstar migration example](examples/migration.md): scope change versus mandatory recovery, with a conditional comparison of discretionary support options.

The RICE formula is `(Reach × Impact × Confidence) / Effort`. Confidence is a fraction in arithmetic (80% = 0.8), not a calibrated probability of success. Use one reach period and one effort unit across candidates. The linked worked examples state their impact assumptions; Intercom's original scale includes 3, 2, 1, 0.5 and 0.25. A score does not encode dependencies, approval or a feasible delivery date.

## Common Pitfalls

### Pitfall 1: Using the Wrong Framework for Your Stage
**Symptom:** A small uncertain project scores ten weakly evidenced criteria to three decimal places

**Consequence:** The ranking looks precise while the main uncertainty remains unresolved.

**Fix:** Match the method to the decision and evidence. Use ranges or investigation when data cannot support a ranking; do not choose a method solely from project age.

---

### Pitfall 2: Framework Whiplash
**Symptom:** Switching frameworks every quarter

**Consequence:** Team confusion, lost time, no consistency.

**Fix:** Keep a stable method across comparable decisions. Reassess when constraints or evidence change; record why the method changed so earlier scores are not compared as equivalent.

---

### Pitfall 3: Treating Scores as Gospel
**Symptom:** "Feature A scored 8,000, Feature B scored 7,999, so A wins"

**Consequence:** Ignores strategic context, judgment, and vision.

**Fix:** Use frameworks as input, not automation. Document exceptions and obtain decisions from the actual authority; a project manager cannot override acceptance or backlog accountabilities through scoring.

---

### Pitfall 4: Solo PM Scoring
**Symptom:** PM scores features alone, presents to team

**Consequence:** Lack of buy-in, engineering/design don't trust scores.

**Fix:** Collaborative scoring sessions. Business, operations and engineering contribute evidence; the actual decision owner decides.

---

### Pitfall 5: No Framework at All
**Symptom:** "We prioritize by who shouts loudest"

**Consequence:** HiPPO (Highest Paid Person's Opinion) wins, not data or strategy.

**Fix:** Start with the decision, evidence and authority. Choose the smallest method that exposes the tradeoff; an ill-fitting score can legitimize the loudest voice.

---

## References

- [Workshop Facilitation](../workshop-facilitation/SKILL.md): guided, context-dump and best-guess modes; skip answered questions.
- [Scope and WBS](../scope-and-wbs/SKILL.md): scope boundaries before ranking.
- [Change Request](../change-request/SKILL.md): authorized changes to a committed baseline.
- [Sprint Planning](../sprint-planning/SKILL.md): preserve Scrum accountabilities during forecasting.
- [Agile Business Consortium MoSCoW](https://www.agilebusiness.org/resource/what-is-moscow-prioritization/): timebox scope categories and their use.
- [Intercom RICE explanation](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/): source formula and scale conventions.
- [Source and changes](SOURCE.md), [license](LICENSE.md).

Related skills are optional. If unavailable, include the boundary, options, authority and evidence directly in the recommendation.
