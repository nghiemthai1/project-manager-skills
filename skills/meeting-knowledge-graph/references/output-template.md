# New bundle template

## Meeting concept

Path: `/meetings/YYYY-MM-DD-slug.md`

```markdown
---
type: Meeting
title: <meeting title>
description: <one-sentence factual description>
tags: [meeting, <series slug>]
meeting_date: YYYY-MM-DD
series: <series name or null>
generated: { by: meeting-knowledge-graph/codex, at: <ISO 8601 datetime> }
sources:
  - id: source-transcript
    resource: <input path, URL, or scope descriptor>
    title: Source transcript
---

# Brief

<short summary derived from the record>

# Outcomes

- Decisions: ...
- Actions: ...
- Open questions: ...
- Risks: ...

# Chronological record

| Turn | Time | Speaker | Confidence | Statement |
|---|---|---|---|---|
| T001 | ... | ... | ... | ... |

# Knowledge links

- [Concept](/decisions/concept.md) — relationship and meeting-specific change.

# Attribution notes

<unresolved identities, candidates, and basis; omit if none>
```

For long records, use subsections or lists instead of a table when that preserves readable source detail.

## Concept bodies

Use sections appropriate to the type: `Current`, `Rationale`, `Alternatives`, `Dependencies`, `Evidence`, `History`, and `Related`. Omit empty sections.

For recurring meetings, add a delta to the meeting file:

```markdown
# Series delta

## New
- ...

## Updated
- ...

## Resolved, reopened, superseded, or contradicted
- ...
```

Update only affected concepts and indexes. Never rewrite earlier meeting records to match later knowledge.
