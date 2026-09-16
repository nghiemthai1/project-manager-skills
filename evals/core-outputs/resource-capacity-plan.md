# Cedar next-week resource capacity plan

As of 2026-10-22; units hours. Planning period is the supplied “next week”; a Monday-Friday interpretation would be 2026-10-26 through 2026-10-30, pending confirmation. Only Dev's supplied allocations are modeled. Other people's allocations, skills and capacity remain unknown.

| Person | Gross | Leave | Overhead | Available | Migration | Support | Total demand | Remaining | Load |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Dev | 40 | 8 | 4 | 28 | 24 | 8 | 32 | -4 | 114.3% |
| Other staff | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown |

The capacity helper was run on controls-capacity-input.json. Availability = 40-8-4 = 28; overload = 32-28 = 4 hours. Support is demand and has not also been deducted from availability. Assuming no omitted Dev assignments, the deficit is four hours; omitted work could increase it. Team totals cannot be inferred from this single-person result.

Unknown assignments are not free capacity. Another person's spare hours cannot offset Dev without the right migration/support skills, confirmed manager allocation and compatible daily timing. The vendor mapping expected October 29 against an October 27 need may compress migration demand; daily scheduling still needs validation.

| Proposed option | Effect if confirmed | Cost / lead time | Decision owner |
|---|---|---|---|
| Transfer 4 support hours to qualified available cover | Dev demand 28; no modeled slack | Cover availability, skill and handoff effort unknown | Support resource manager, identity to confirm |
| Defer 4 migration hours | Dev demand 28; migration delivery impact must be scheduled | May delay tests/gates; cost impact unknown | Sol coordinates with Dev; Nia approves baseline impacts |
| Transfer 4 migration hours | Dev demand 28 before training/handoff overhead | Requires skills, access and confirmed allocation; possible extra demand/cost | Receiving resource manager, identity to confirm |

Recommendation: first seek confirmed support cover while checking the critical migration sequence; until confirmed, report overload and no feasible unconditional staffing commitment. Do not assume overtime or recruit productive capacity instantly. Sol should collect all assignments and daily timing from resource managers, Dev should validate effort and skill needs, and a resource authority should approve reallocation before next week's work is committed. Review at that decision and whenever leave, mapping timing or work estimates change. C-B1 date and budget remain unchanged; options are proposals.
