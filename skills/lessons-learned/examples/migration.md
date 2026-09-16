# Lessons Learned: migration example

Fictional training scenario. Values and thresholds are examples, not defaults for real projects.

## Lesson: reconciliation must test relationships as well as population

Northstar's attachment files could be present while their ticket links were wrong. The observed failure supports including identity and relationship checks in the agreed reconciliation method. File-count equality alone did not answer the business acceptance question.

The practice applies where relationships carry business meaning. It does not mean every migration needs the same sample size or zero tolerance for every low-severity discrepancy; those decisions need context and authority.

An adoption action is to update the migration acceptance template with relationship rules and exception disposition. Saira's acceptance perspective is required. Record actual ownership and later effectiveness evidence instead of assuming a template edit guarantees success.

## Repair

**Flawed:** "Counts are useless."

**Corrected:** "Counts provide population evidence but must be combined with the checks required to establish correctness for the agreed use."
