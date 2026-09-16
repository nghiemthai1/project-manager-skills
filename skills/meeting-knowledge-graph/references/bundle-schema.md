# OKF meeting bundle

Target OKF v0.2: Markdown concepts with YAML frontmatter, standard Markdown links, optional indexes, and optional logs.

```text
index.md
log.md
meetings/
decisions/
actions/
questions/
risks/
entities/
topics/
```

Create only directories the meeting needs. `index.md` and `log.md` are reserved and normally have no frontmatter. The root index may declare:

```yaml
---
okf_version: "0.2"
---
```

Every other Markdown file requires nonempty `type`. Prefer `title`, `description`, `tags`, `generated`, and `sources` when known. Producer-defined meeting fields are allowed.

```yaml
---
type: Decision
title: Use Postgres for event processing
description: Postgres remains current until the traffic threshold is crossed.
tags: [meeting, architecture]
status: stable
decision_status: current
generated: { by: meeting-knowledge-graph/codex, at: 2026-09-02T15:00:00-04:00 }
sources:
  - id: meeting-2026-09-02
    resource: /meetings/2026-09-02-architecture.md
    title: Architecture meeting — 2026-09-02
---
```

Use OKF `status` only for document lifecycle: `draft`, `stable`, or `deprecated`. Store domain state separately, such as `decision_status`, `action_status`, or `question_status`.

## Evidence and history

Put traceable evidence in the body:

```markdown
## Current

Use Postgres until approximately 10k events/second.[^meeting-2026-09-02]

## Evidence

- `T031–T036` — decision and threshold; speaker attribution: high.

## History

- Proposed in [Sep 2 meeting](/meetings/2026-09-02-architecture.md).

[^meeting-2026-09-02]: [Architecture meeting](/meetings/2026-09-02-architecture.md)
```

Links assert relationships; explain the relationship in surrounding prose. Prefer bundle-relative links beginning with `/`. Keep broken intentional links if they represent not-yet-written knowledge.

Indexes list children with short descriptions. Logs use newest-first `YYYY-MM-DD` sections and link every changed concept. Preserve unknown frontmatter keys when updating files.
