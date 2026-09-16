# Delivery Approach Advisor: migration example

Fictional training scenario. Values and thresholds are examples, not defaults for real projects.

## Dialogue at initiation

**Jules:** "The vendor contract and cutover window are fixed, but we do not trust attachment data."

**Advisor:** "Can you rehearse on representative data before the cutover decision?"

**Jules:** "Yes, with controlled test environments."

## Recommendation

Use a hybrid approach. Plan procurement, environment access, training, and cutover dependencies predictively. Run short data-migration rehearsals to learn about linkage and recovery. Feed each rehearsal's evidence into the forecast and risk record. Keep cutover authorization gated by reconciliation, restore, and service acceptance.

Revisit the approach if representative data is unavailable or feedback cannot arrive before the decision window. A rehearsal with irrelevant samples is not a learning cycle.

## Repair

**Flawed:** "Because the date is fixed, estimate all migration work upfront and prohibit iteration."

**Corrected:** "The date constrains choices; it does not remove data uncertainty. Use rehearsals to expose the tradeoffs before the sponsor must decide."
