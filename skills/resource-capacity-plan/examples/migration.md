# Northstar: a rehearsal week with conditional coverage

Fictional instructional capacity subcase; no calendar week or actual assignment approval is asserted. Chen has 40 gross hours, 8 leave and 4 overhead. Availability is 28. Migration rehearsal requires 24 and existing-system support 8, totaling 32. Overload is 4; modeled load is about 114.3%.

| Category | Hours | Treatment |
|---|---:|---|
| Gross | 40 | One common planning period |
| Leave | 8 | Deduct once |
| Meetings/administration | 4 | Overhead; excludes support |
| Rehearsal demand | 24 | Proposed effort need |
| Existing-system support | 8 | Allocation, not another deduction |
| Vendor help | Unknown | Not entered as available replacement capacity |

Run [the example input](assets/migration-capacity.json):

```sh
python scripts/capacity.py --input examples/assets/migration-capacity.json --format markdown
```

## What-if and authority

A proposed transfer of four support hours would reduce Chen's demand from 32 to 28 and eliminate the modeled weekly overload. It is feasible only if a competent recipient accepts coverage at the needed times through the actual resource/support authority. Jules may coordinate the request; the case does not name an approver or prove that Beck's team is available or authorized to cover the work.

If no transfer is possible, examine whether rehearsal work can be resequenced or a required window changed. That may affect the integrated forecast. Do not assume overtime or delete restore/reconciliation effort to balance the table.

## Timing challenge

The separate instructional schedule has mapping validation and restore-environment preparation in parallel. If both require Chen full time, even a balanced weekly total does not make that overlap workable. Check the daily sequence and preserve the difference between the original technical dependencies and any resource-order choice. Vendor mapping readiness, environment access and acceptance-review availability may further constrain productive hours.

Record the current case as resource-constrained and the support-transfer case as proposed. Recalculate after actual availability or scope changes; retain the earlier data rather than making the old plan appear feasible retrospectively.

**Repair:** “Use the vendor for the remaining four hours” invents skill, capacity and permission. Obtain those facts or change demand/sequence through the appropriate decision.
