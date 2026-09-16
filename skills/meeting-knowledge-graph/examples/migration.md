# Meeting Knowledge Graph: migration example

Fictional training scenario. Values and thresholds are examples, not defaults for real projects.

## Source: Northstar rehearsal, 6 November

| Turn | Source text |
|---|---|
| T001 | Chen: "Some attachment links are missing. We have reproduced the loss." |
| T002 | Beck: "I will investigate the mapping, but I cannot promise a fix by Monday." |
| T003 | Rosa: "I am not accepting operations handover without a demonstrated restore." |
| T004 | Jules: "We might phase the migration. Noel has not approved that." |

## Worked extraction

M-I002 is an actual issue supported by T001, linked to the earlier M-R01 risk. Beck owns an investigation action from T002. Its deadline is unspecified; Monday is explicitly not a commitment. Rosa's T003 is an acceptance condition, not evidence that restore has passed. Phasing remains a proposal at T004.

The series delta creates M-I002, updates the risk relationship, adds Beck's action, and preserves the unresolved phasing decision. Keep the previous rehearsal record intact.

## Later meeting

On 9 November, Noel approves M-CR02, a 28 November cutover, and B2 USD 300,000 with authorized funding. The decision concept is updated with new evidence; the 6 November proposal is retained as history. On 25 November a failed restore demonstration becomes evidence for a hold, not a reason to delete Noel's earlier planning decision.

## Repair

**Flawed:** "Beck will fix the issue by Monday and the phased rollout is approved."

**Corrected:** "Beck committed to investigate, with no deadline. Phasing was proposed on 6 November and approved separately on 9 November."
