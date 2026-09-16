# Estimation Advisor: migration example

Fictional training scenario. Values and thresholds are examples, not defaults for real projects.

## Guided decision

**Jules:** "How long will the attachment migration take? The last migration took three weeks."

**Advisor:** "Does the earlier migration match this record population, attachment scheme, and restore requirement?"

**Jules:** "No. The old system had no attachments."

**Advisor:** "That analogy supports some setup work but not the dominant migration risk. Run a bounded rehearsal on representative attachment cases, then estimate the remaining migration bottom-up."

## Worked recommendation

Chen's proposed investigation must answer whether identifiers preserve ticket-to-attachment relationships and how reconciliation detects missing links. Inputs include representative edge cases, an explicit sample basis, elapsed extraction time, failed-record handling, and restore evidence. No duration is invented for this investigation; Chen must propose the timebox with available capacity.

Use observed rehearsal throughput only after separating fixed setup from record-volume work. Explain whether the test environment represents production. Re-estimate when the mapping or population changes.

## Repair

**Flawed:** "Three weeks, because we migrated a system before."

**Corrected:** "The prior three-week migration is not comparable for attachment handling. Estimate shared setup from history; resolve attachment linkage through a rehearsal before forecasting total duration."
