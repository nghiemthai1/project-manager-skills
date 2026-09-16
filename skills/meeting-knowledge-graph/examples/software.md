# Relay steering meeting: evidence before the brief

Fictional training source, 19 October 2026. The following five turns are the complete source supplied for this example. Timestamps are absent; explicit speaker labels identify speakers, except T004. A participant roster would not justify assigning that anonymous turn.

| Turn | Speaker / attribution | Source text |
|---|---|---|
| T001 | Mina / explicit label | “B1 is 100,000 dollars. The forecast is 120,000; the current authorization totals 110,000 including reserve.” |
| T002 | Omar / explicit label | “We could defer operator dashboard polish. That would not remove the recovery-access requirement.” |
| T003 | Ada / explicit label | “Approve CR-001, the deferral, and B2 at 120,000. I authorize the extra 10,000 beyond the original envelope.” |
| T004 | Unknown / unresolved | “Is 30 October still feasible?” |
| T005 | Omar / explicit label | “I cannot confirm that until we rerun integration.” |

The detail pass preserves 100,000/120,000/110,000 and the extra 10,000 distinction. The decision pass records the proposed deferral at T002 and actual scope/funding choice at T003; it does not extend approval into security or a new release date. The action pass cannot infer that Omar committed to run integration or promised a date from T005. The graph pass links CR-001 to scope/budget and to unchanged recovery acceptance.

Reconciled brief: “Ada approved CR-001's specified deferral and B2 funding. Pilot feasibility remains unresolved pending integration evidence. An anonymous question asks about 30 October.” No unanimous agreement or date commitment is evidenced.

Example current concept `/decisions/cr-001.md` uses the existing slug. The custom `retention` field below is fictional existing metadata and must survive an update:

```markdown
---
type: Decision
title: CR-001 scope and funding change
status: stable
decision_status: current
retention: {class: project, review_after: null}
sources:
  - id: relay-steering-2026-10-19
    resource: /meetings/2026-10-19-steering.md
---
## Current
Ada approved the optional-polish deferral and B2 at USD 120,000,
including an extra USD 10,000 beyond the original envelope.
The recovery requirement remains. No changed date is approved here.
## Evidence
T002–T003 in [the meeting](/meetings/2026-10-19-steering.md)
support the scope boundary and actual funding decision.
## History
- 19 October: proposed deferral at T002, approved at T003.
```

Keep schedule feasibility as an open question/current uncertainty linked to T004–T005. Speaker confidence for Omar is high while the claim is explicitly unconfirmed; these are different dimensions. Index the changed concepts and link them in the 19 October log section.

A later 29 October source supplies D-004, deferring the pilot to 3 November. Add that meeting/decision, update the schedule concept and newest-first log, and retain this 19 October ledger exactly. Do not replace T004's question with the later answer or alter `retention.review_after: null` to an invented date.

**Repair:** “Everyone agreed to launch 30 October with 120k” loses authority boundaries and uncertainty. The ledger-linked record preserves what was actually chosen and what was not.
