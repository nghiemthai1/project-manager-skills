# Northstar recurring meeting: preserve the denied deadline

Fictional training source, 6 November 2026. Existing bundle contains M-R01's prior risk statement and a phased-migration proposal concept. Unknown existing frontmatter keys and stable slugs must be retained.

| Turn | Source text |
|---|---|
| T001 | Chen: “Some attachment links are missing. We have reproduced the loss.” |
| T002 | Beck: “I will investigate the mapping, but I cannot promise a fix by Monday.” |
| T003 | Rosa: “I am not accepting operations handover without a demonstrated restore.” |
| T004 | Jules: “We might phase the migration. Noel has not approved that.” |

All speaker labels are explicit in this synthetic source; no timestamps are supplied. The ledger retains the order and negations. Chen's observation supports current issue M-I002, linked to M-R01, but does not prove the mapping's exact root cause. Beck commits to investigate, not to fix by Monday. Rosa states a service-acceptance condition, not a passing restore or formal release decision. Phasing remains proposed at T004.

| Series change | Current concept action | Evidence / history |
|---|---|---|
| New observed issue | Create M-I002 with observed lost links and remaining cause/population uncertainty | T001; link prior M-R01 without deleting its earlier warning |
| New investigation action | Beck owner, deadline unspecified; domain state open | T002 including explicit denial of a promised Monday fix |
| Acceptance condition reiterated | Preserve demonstrated-restore requirement; no acceptance granted | T003 |
| Proposal remains unresolved | Phased migration not approved as of 6 November | T004; no supersession from discussion alone |

Example action concept uses `status` for document lifecycle and a separate domain field:

```markdown
---
type: Action
title: Investigate attachment mapping
status: stable
action_status: open
owner: Beck
due_date: null
custom_vendor_reference: null
sources:
  - id: northstar-rehearsal-2026-11-06
    resource: /meetings/2026-11-06-rehearsal.md
---
## Current
Beck committed to investigate mapping. No fix deadline was promised.
## Evidence
T002 in [the rehearsal](/meetings/2026-11-06-rehearsal.md).
## History
- 6 November: investigation commitment recorded; Monday explicitly not promised.
```

In a later 9 November meeting, supplied new evidence records Noel approving M-CR02, 28 November cutover and B2 USD 300,000 with funding. Update the affected decision/current plan and add dated history; the 6 November meeting still says phasing was unapproved then. A new 25 November failed restore is later evidence for hold/review, not permission to erase the earlier plan approval or mark Beck's investigation complete.

The brief and current controls derive from these concepts, while the full ledger retains the rejected deadline and acceptance condition. An unchanged action in a later meeting is not resolved through silence. Unknown custom metadata remains unknown.

**Repair:** “Beck will fix by Monday; phasing approved” removes two explicit negatives. The corrected bundle preserves the actual action, denied commitment and later separate approval.
