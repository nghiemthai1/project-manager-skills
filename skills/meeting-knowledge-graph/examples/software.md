# Meeting Knowledge Graph: software example

Fictional training scenario. Values and thresholds are examples, not defaults for real projects.

## Source: Relay steering meeting, 19 October

| Turn | Source text |
|---|---|
| T001 | Mina: "B1 is 100,000 dollars. The forecast is 120,000; the current authorization totals 110,000 including reserve." |
| T002 | Omar: "We could defer operator dashboard polish. That would not remove the recovery-access requirement." |
| T003 | Ada: "Approve CR-001, the deferral, and B2 at 120,000. I authorize the extra 10,000 beyond the original envelope." |
| T004 | Unknown speaker: "Is 30 October still feasible?" |
| T005 | Omar: "I cannot confirm that until we rerun integration." |

## Worked extraction

The current budget concept links B2 to T003 and preserves B1 in history. CR-001 is approved because Ada explicitly chooses and authorizes it. The schedule concept remains unconfirmed: T005 withholds a forecast, despite a clearly attributed speaker. T004 becomes an open question with anonymous attribution; it does not become an action assigned to Omar.

Concept relationship: CR-001 changes scope and budget but does not waive security acceptance. Evidence for that boundary is T002 together with the approval's stated scope. The brief says: "Scope deferral and B2 approved; pilot feasibility awaits integration evidence."

## Repair

**Flawed:** "Everyone agreed to release on 30 October with a 120,000 budget."

**Corrected:** "Ada approved B2 and the specified deferral at T003. The release forecast is unresolved at T005. The record contains no evidence of unanimous agreement."

## Later update

On 29 October, D-004 defers the pilot to 3 November. Update the schedule concept and its history. Do not edit this 19 October ledger to make the later date appear known earlier.
