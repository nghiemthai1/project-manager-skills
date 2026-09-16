---
name: project-intake-advisor
argument-hint: '[request or initiative idea]'
description: Triage an incoming request into a project, change, operational task or investigation. Use when a vague
  ask or escalation needs a response before commitment.
intent: Separate the literal request from its intended outcome and route it without inventing commitments.
type: interactive
theme: initiation-and-governance
best_for:
  - Separate the literal request from its intended outcome and route it without inventing commitments.
scenarios:
  - 'Use project-intake-advisor: Separate the literal request from its intended outcome and route it without inventing
    commitments.'
estimated_time: Depends on evidence and project scope
frameworks: Request triage; outcome-evidence-action; decision rights
domain: software-it-project-management
version: 2.0.0
license: CC-BY-NC-SA-4.0
---
# Project Intake Advisor

## Purpose

Decode an incoming message — a Slack ping, email, mandate, escalation, or FYI — into a structured breakdown before you respond. This skill acts as a chief-of-staff-grade analyst sitting in a project manager's chair: it separates the **literal ask** from the **job-to-be-done** underneath it, distinguishes observed sender authority from assumptions about power and stake, and opens the conversation toward a reply or next artifact.

Use it when a request lands and you need to decide whether it belongs in a new project, an existing change process, operational work, or an investigation. The output is a request breakdown, route, next decision and optional draft reply. Use it when your first instinct is to answer the words on the screen. The skill slows that reflex down: it finds the outcome, for whom, and why now — not how to build. It is not a programmer breaking down a spec. When a request sounds like a feature or a build order, the skill hunts for the outcome and the job-to-be-done beneath it.

## Input

**Works best with:** The incoming message itself — pasted text, a screenshot, an image, an attached file, or a PDF. The skill extracts the full message from whatever form it takes before analyzing.

**Also useful:**
- Who sent it and their apparent role relative to your work (upstream, peer, downstream)
- The situation or thread the message arrived in
- What you want next — analysis only, or a drafted reply too

Anything supplied with the invocation itself — text after the skill name, the pasted message, surrounding notes — counts as answers already given. Treat anything written *around* the message as sender or situation context. Use it and skip whatever it covers; don't re-ask.

**Arriving empty-handed? That works too.** Drop in the message and nothing else. If sender or situation is unknown and it changes the read, the advisor asks at most 3 targeted questions in total, one at a time, then proceeds with clearly labeled assumptions. If part of the message is unreadable or cut off, the advisor says so and works with what is there.

**Example invocation:** `My VP DM'd me: "Any chance the dashboard redesign lands next sprint? Board's asking." Analyze this before I reply.`

## Key Concepts

### The Ask vs. the Job-to-Be-Done

The literal ask is what the words request. The job-to-be-done is the outcome the sender is actually chasing. "Can we get the dashboard redesign into next sprint?" is the ask; "I need something concrete to show the board that we're responsive" may be the job. **Responding to the ask when the job is different is how PMs build the wrong thing fast.** Every breakdown separates these two explicitly.

### The Sender Read: Power, Stake, Subtext

Before you respond, you read the room. Who sent it, what is their role relative to your work, and are they upstream (they set your priorities), a peer (they need your cooperation), or downstream (they depend on your output)? Power and stake can change the response even when the words are identical. A senior request merits checking authority and consequence; seniority alone does not turn a question into an approved baseline change.

### Success Criteria vs. Must-Haves (the distinction PMs blur)

These are not the same thing, and conflating them is a classic PM error:
- **Success criteria** = how the sender will *judge* whether the result worked (the pass/fail bar, the metric, the definition of done)
- **Must-haves** = what has to go *into the deliverable* (the hard requirements)

A deliverable can hit every must-have and still fail the success criteria. Keeping them separate is a core teaching of this skill.

### Infer, Do Not Invent

The skill reasons from evidence in the message and marks every guess as an inference. It never presents a guess as a stated fact. Everything inferred lands in an explicit **Assumptions to Validate** list at the end — so the human knows exactly what the analysis rests on.

### Scale Depth to the Message

The breakdown has twelve sections, but a one-line ping does not need all twelve. The skill collapses or skips empty sections and marks them "none stated" where the template calls for it. Over-filling a trivial message with twelve dense sections is a failure mode, not thoroughness.

### The Sticky-Note Rule

Prefer short, scannable bullets. Preserve exact names, dates, units and authority qualifications when brevity would lose meaning. Direct quotes remain verbatim; do not transliterate names or alter source evidence to meet a style rule.

### Facilitation Source of Truth

Use [`workshop-facilitation`](../workshop-facilitation/SKILL.md) as the default interaction protocol for this skill.

It defines:
- session heads-up + entry mode (Guided, Context dump, Best guess)
- one-question turns with plain-language prompts
- crediting inline invocation context so answered questions are skipped
- interruption handling and pause/resume behavior

For this skill specifically: the pasted message *is* the context dump. Ask clarifying questions only when sender or situation is genuinely unknown **and** it changes the read — at most 3, one at a time.

## Application

### Step 1 — Extract the message

Pull the full message from whatever form it arrives in (screenshot, image, file, PDF, or text) before analyzing. If any part is unreadable or cut off, say so and work with what you have.

### Step 2 — Fill only the gaps that change the read

If sender identity or situation is unknown and it would change the analysis, ask at most 3 targeted questions, one at a time:
1. "Who sent this and what is their role relative to your work?"
2. "What is the situation or thread this arrived in?"
3. "Do you want analysis only, or a drafted reply too?"

Then proceed with clearly labeled assumptions. **Do not ask questions the message already answers.**

### Step 3 — Render the breakdown

Render in Markdown using the structure below. Scale depth to the message: collapse or skip any empty section; mark it "none stated" where the template calls for it. Apply the Sticky-Note Rule without dropping consequential qualifications or altering source text. Use [`template.md`](template.md) for the copy/paste fill-in structure a PM can work through by hand.

```markdown
## Incoming Request Breakdown

### 1. Classify
- Message type and channel, one line
- Types: meeting prep, feedback, feature request, mandate, escalation, FYI, ask for help, other

### 2. Sender Read
- Who sent it, apparent role
- Relationship: upstream, peer, or downstream
- Power and stake where they matter

### 3. Literal Ask
- What they explicitly want, plain terms

### 4. Underlying Problem Space
- The job they are trying to get done
- The outcome behind the request
- Separate the ask from the need

### 5. Sentiment and Subtext
- Tone, urgency, frustration, enthusiasm, politics
- Quote the tell if there is one

### 6. Must-Haves vs Nice-to-Haves
- Hard requirements for the deliverable
- Soft preferences, clearly separated

### 7. Hard Negatives
- What they explicitly do not want
- "None stated" if none

### 8. Success Criteria
- Pass/fail bar, metric, or definition of done
- How they will judge the result worked
- Capture only what is stated; mark implied ones as inference
- "None stated" if none

### 9. Hard Constraints
- Drop-dead dates, budget, non-negotiables
- "None stated" if none

### 10. Gaps and Ambiguities
- What is unclear or missing before committing

### 11. Risks
- Scope, expectation, political, timeline landmines

### 12. Recommended Next Steps
- 2 to 4 concrete moves, ordered

### Assumptions to Validate
- [Anything inferred rather than stated]
- [Sender read or intent guessed]
- [Success criteria or constraints implied]
```

### Step 4 — Route the work and open the conversation

| Route | Evidence needed | Output / boundary |
|---|---|---|
| New project candidate | Distinct outcome, sponsor/owner, cross-team or temporary delivery need | Intake brief and business-case questions; not an approved charter |
| Change to active project | Relevant scope/date/cost baseline and requested deviation | Change-impact brief for the actual authority; no silent addition |
| Operational work | Existing service responsibility and normal work channel | Proposed service handoff; do not invent an SLA or assign a live queue |
| Investigation | Outcome, feasibility or evidence too unclear to commit | Bounded question, proposed owner/timebox and decision it will inform |

Use the least heavy route that handles the consequence. Urgent incidents should follow the organization's actual incident process when known; a project intake analysis must not delay an authorized response. A mixed message may contain more than one route; keep them separate.


After rendering, ask only a remaining question that changes the recommendation, staying within the three-question total. If the user already requested a reply or artifact, provide it. Otherwise offer four next options:

1. **Draft a reply to the sender** (Recommended)
2. **Build a meeting agenda for this ask**
3. **Draft the intake or change-impact brief**
4. **Draft a counter-proposal that protects the outcome**

Ask the user to reply with `1`, `2`, `3`, `4`, a combination like `1 and 3`, or a custom path.

## Examples

Optional worked applications:

- [Relay request triage](examples/software.md): a requested addition to an active baseline, with a draft reply that does not promise delivery.
- [Northstar request triage](examples/migration.md): separate a migration incident from an excluded reporting enhancement and route each appropriately.

### One-line FYI: depth collapses

Message: "Legal signed off on the new terms." Capture the sender's report and ask for the approval record only if needed for the decision. A report of sign-off is not the record itself. Do not infer security, service or go-live acceptance. Acknowledge or draft the relevant checklist update when requested; no twelve-section wall is necessary.

## Common Pitfalls

### Pitfall 1: Breaking It Down Like a Spec
**Symptom:** Treating a feature-shaped request as a build order and jumping to implementation tasks.

**Consequence:** You optimize the wrong thing efficiently. You solve the ask and miss the job, then wonder why the sender is still unhappy after you delivered exactly what they said.

**Fix:** Always run Section 4 (Underlying Problem Space). Name the outcome and the job-to-be-done before touching "how."

### Pitfall 2: Blurring Success Criteria and Must-Haves
**Symptom:** Listing "the dashboard must have export" under the same heading as "they'll judge this by whether the board is reassured."

**Consequence:** You build a deliverable that ticks every requirement and still fails the real bar. The two answer different questions — *what goes in* vs. *how they judge it*.

**Fix:** Keep Sections 6 and 8 strictly separate. Ask yourself: is this a thing in the box, or the ruler they measure the box with?

### Pitfall 3: Inventing Instead of Inferring
**Symptom:** Presenting a guess about the sender's motive as if the message stated it.

**Consequence:** The human acts on fabricated certainty, walks into the room wrong, and loses trust when the assumption cracks.

**Fix:** Mark every guess as an inference and surface it in Assumptions to Validate. If you didn't read it in the message, it's an assumption — label it.

### Pitfall 4: Over-Filling a One-Liner
**Symptom:** Rendering all twelve sections for a two-sentence FYI.

**Consequence:** Analysis theater. The reader can't find the signal, and the breakdown looks rigorous while adding nothing.

**Fix:** Scale depth to the message. Collapse empty sections; mark "none stated." A one-line ping earns a one-paragraph read.

## References

- [Workshop Facilitation](../workshop-facilitation/SKILL.md): entry modes, one-question turns and interruptions.
- [Stakeholder Map](../stakeholder-map/SKILL.md): extend the sender read with evidenced power and impact.
- [Project Business Case](../project-business-case/SKILL.md): compare investment options after intake.
- [Change Request](../change-request/SKILL.md): analyze and authorize proposed baseline changes.
- [Escalation Brief](../escalation-brief/SKILL.md): prepare a time-bound authority decision.
- [Source and changes](SOURCE.md), [license](LICENSE.md): adaptation of Dean Peters's Incoming Request Breakdown.

If an adjacent skill is unavailable, produce the bounded brief and its required evidence here. Drafting does not imply sending a reply, approving a project or changing a live queue.
