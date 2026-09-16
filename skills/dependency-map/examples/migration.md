# Dependency Map: migration example

Fictional training scenario. Values and thresholds are examples, not defaults for real projects.

## Record at 23 October

M-DEP01 is the vendor export mapping. Beck is provider contact and Chen is receiver. Expected delivery is 4 November, against a 2 November need: -2 calendar days of local margin. Acceptance includes sample records with correct attachment identifiers and documented transformations.

## Worked coordination decision

Jules requests a mapping review before treating delivery as complete. An early sample would allow Chen to test linkage while the vendor completes the final mapping. This is a proposal, not a promise on Beck's behalf. If the sample fails, the receiving work remains blocked even if the mapping file arrived on time.

At the 6 November rehearsal, actual lost attachment links become M-I002. Keep M-DEP01's delivery history and link the issue instead of retroactively pretending the dependency was never delivered. Acceptance status must explain which condition failed.

## Repair

**Flawed:** "Mapping file uploaded; dependency closed."

**Corrected:** "File received, acceptance failed on attachment linkage. M-I002 owns remediation; receiving migration work cannot proceed to the acceptance gate."
