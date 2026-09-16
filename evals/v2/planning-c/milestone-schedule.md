# Fictional Quartz milestone schedule assessment

Prepared 2026-09-16; project status date and approved baseline not supplied. Model boundary is only A, B, C and D. Unit: working-day offsets from origin 0, finish-to-start links with zero lag. No calendar, start date, actual progress or milestone acceptance authority is supplied. Requested finish offset 6 is a target, not an evidenced approval.

The manager's claim that shortening B from 3 to 2 makes finish 5 is unsupported. The original dependency-only model finishes at 6 on two tied paths. Changing B alone leaves C controlling finish at 6. Both parallel models also conflict with Jo's single-person availability; a serial resource-feasible model finishes at 9 originally or 8 with the proposed reduction, conditional on that reduction being achievable and continuous Jo availability.

| Task | Original duration | Technical predecessors | Resource | Original ES/EF | Original LS/LF | Original float | Changed duration | Changed ES/EF | Changed LS/LF | Changed float |
|---|---:|---|---|---|---|---:|---:|---|---|---:|
| A | 1 | None | Not supplied | 0/1 | 0/1 | 0 | 1 | 0/1 | 0/1 | 0 |
| B | 3 | A | Jo full time | 1/4 | 1/4 | 0 | 2 | 1/3 | 2/4 | 1 |
| C | 3 | A | Jo full time | 1/4 | 1/4 | 0 | 3 | 1/4 | 1/4 | 0 |
| D | 2 | B,C | Not supplied | 4/6 | 4/6 | 0 | 2 | 4/6 | 4/6 | 0 |

Original critical paths: A-B-D and A-C-D, both 6. After the duration proposal, A-C-D remains 6 while A-B-D totals 5; B has one working day total float in this unconstrained model. That float is not extra Jo capacity. No free float or fixed-target negative-float calculation is claimed. The helper supports only common-finish unconstrained offsets; it does not level resources or model date constraints.

## Resource reconciliation

There is no additional capacity. Choose B before C as an explicit resource-ordering scenario, adding B as a predecessor of C for this scenario while retaining original technical links. It is not a newly discovered technical dependency. Reverse ordering would give the same modeled finish because both require Jo full time after A.

| Resource-feasible scenario | A | B | C | D | Finish | Variance to target 6 |
|---|---|---|---|---|---:|---:|
| Original durations, B then C | 0–1 | 1–4 | 4–7 | 7–9 | 9 | +3 working-day offsets |
| Proposed B=2, B then C | 0–1 | 1–3 | 3–6 | 6–8 | 8 | +2 working-day offsets |

The augmented resource-ordering chain governs each of these finishes; each task has zero total float against its respective augmented-model finish. Reducing B saves one day in the serial model, from 9 to 8, not from 6 to 5. These are feasible relative to the supplied Jo constraint, not a validated full-project staffing/calendar commitment. Availability for A/D, other Jo obligations and the basis for B's faster duration are unknown.

| Milestone | Target | Current forecast basis | Exit evidence / authority | Open decision |
|---|---:|---|---|---|
| Finish of modeled D | 6 | Original feasible sequence 9; change scenario 8 | D's deliverable and acceptance criterion unspecified; authority unknown | Confirm actual scope/evidence, proposed sequence and credible duration before any commitment |

A zero-duration finish event would not add work; any required inspection/reviewer waiting must be added as explicit activities if absent from D's duration. No such extra duration is invented here.

Next steps: Jo and the relevant delivery authority should validate whether B can be reduced without dropping required work/quality or assuming unavailable help. Identify owners and availability for A/D, task outputs and required gate evidence. If offset 6 remains required, assess additional evidence-backed changes to durations/scope/sequence under actual authority; the current facts do not support it. No extra capacity is assumed and no baseline is changed. A real date requires a start anchor, working calendar, holidays/shifts, resource calendars and external/review constraints. Do not convert offset gaps into calendar dates.

Executed local schedule helper for the original and changed technical networks using schedule-original.json and schedule-change.json. Resource-ordering calculations above are explicit manual forward/backward calculations, separate from the helper's unconstrained outputs. No accepted shortening, actual completion or external schedule change is recorded.

