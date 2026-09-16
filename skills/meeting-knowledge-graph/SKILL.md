---
name: meeting-knowledge-graph
description: "Convert transcripts, notes, or available recording transcriptions into evidence-linked OKF project memory. Use for durable meeting records and recurring-series updates, not a brief summary."
metadata:
  type: workflow
  domain: software-it-project-management
  version: "1.0.0"
---
# Meeting Knowledge Graph

## Purpose

Turn meeting evidence into durable project memory without erasing the discussion that produced it. Use when decisions, assumptions, objections, actions, and changing facts must remain traceable across meetings. For a brief summary with no durable record, use a simple summary instead.

This workflow retains the existing OKF v0.2 bundle format. It enriches the teaching and review guidance without migrating historical records.

## Input

Bring a transcript, meeting notes, or a recording with an available transcription capability. Useful additions are the meeting date, participant list, speaker-keyword reference, and existing OKF bundle. Do not invent a transcript if audio cannot be processed; request accessible text and explain that limitation.

Example: "Add this steering meeting to our existing bundle. Keep objections, tentative dates, and the decision that replaced last week's plan."

For an existing bundle, read its index, recent change log, and only the relevant concepts before updating. A participant list alone does not identify an unlabeled speaker.

Use context already supplied. If inputs are incomplete, distinguish useful draft work from decisions that require missing evidence. Mark unknowns explicitly; never fill them with example data.

## Key Concepts

### Evidence before synthesis

Create an immutable chronological ledger with turn IDs such as T001. The ledger is the source for claims; a summary is a derived view. A missing timestamp remains missing. If the source is condensed notes, preserve the note order and say the record is not verbatim speech.

### Proposal, decision, action

A proposal is an option under discussion. A decision needs evidence of the choice and the authority or agreement that made it operative. An action needs an actual commitment, not merely "someone should." Record absent owners or deadlines as unassigned or unspecified.

### Confidence has dimensions

Speaker attribution confidence and claim status are different. A clearly identified speaker can make an uncertain estimate. An anonymous turn can unambiguously record an objection. Preserve both distinctions rather than attaching one confidence label to everything.

### Current state and history

A concept page expresses current knowledge with evidence and history. Earlier meeting records remain unchanged when a later meeting supersedes a decision. Document status (draft/stable/deprecated) is separate from domain state such as an action being open or a decision being superseded.

### Why this works

Linked concepts make the latest state usable, while immutable meeting records preserve how it changed. That combination prevents a polished summary from becoming stronger evidence than the source and makes disagreements visible instead of resolving them through wording.

## Application

1. Preserve the ordered source ledger, including numbers, caveats, examples, rejected options, and source type. Never regroup it by inferred speaker.
2. Resolve speaker identities only where the evidence supports them. Keep unresolved identities and contradictory labels explicit.
3. Perform four independent attention passes: detail, decisions, actions, and graph relationships. Use [the extraction guide](references/agent-prompts.md). If authorized subagents are available, give them the same ledger independently; otherwise do the passes sequentially. Parallelism is optional and does not change the evidence standard.
4. Reconcile every proposed claim against the ledger. Do not settle conflicts by majority vote. Preserve alternatives, disagreements, thresholds, and revisit conditions.
5. Write meeting and concept files using [the bundle schema](references/bundle-schema.md) and [the output template](references/output-template.md). Preserve unknown frontmatter fields and stable slugs when updating existing concepts.
6. For a recurring meeting, classify each change as new, unchanged, updated, resolved, reopened, superseded, or contradicted. Update affected concepts and the newest-first change log; never rewrite earlier meeting records to match current knowledge.
7. Derive a brief summary, decisions, actions, open questions, risks, and uncertainties from the reconciled record. Evidence links belong in the durable bundle even when the brief is short.
8. Check that each current claim has evidence, every changed concept has history, and no proposal became an approval during compression.

Use the [artifact template](template.md). Keep the deliverable concise; retain the reasoning needed to explain its consequential choices.



## Examples

- [Software release](examples/software.md): application, reasoning, and a corrected failure.
- [IT migration](examples/migration.md): application, reasoning, and a corrected failure.

## Common Pitfalls

- **Summary replaces evidence:** detailed objections vanish after a concise recap. Preserve the ledger and derive the recap last; sample-check omitted caveats.
- **Speaker by plausibility:** a technical statement is assigned to the engineer because it sounds like their role. Keep it anonymous unless supported by actual attribution evidence.
- **Consensus by silence:** "no objections recorded" becomes unanimous approval. Record the literal source condition and leave approval status unconfirmed.
- **History rewritten:** a superseded date disappears from the previous meeting. Preserve old records, mark the concept's current state, and link the new decision.
- **Everything in one confidence score:** a certain attribution makes a speculative claim appear established. Track attribution separately from proposal/forecast/decision state.

## References

- [Decision Log](../decision-log/SKILL.md)
- [Raid Log](../raid-log/SKILL.md)
- [Status Report](../status-report/SKILL.md)

Related skills are optional handoffs. If unavailable, use the artifact requirements described here; do not stop solely because another skill is not installed.
