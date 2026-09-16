# Vega interface estimate — planning basis, not a date commitment

**Use three-point PERT as a provisional effort estimate. It yields 6 person-days, not a 95% finish date.** With 3 person-days of availability per week, that central effort corresponds to two capacity-equivalent weeks before unknown environment waiting and calendar/sequence effects. It does not establish completion exactly two weeks after start.

Decision requested: a 95% date commitment. Start date, working calendar, actual completion criteria, contributor identity, estimate date and approved commitment authority were not supplied. The three inputs share a stated boundary, but its detailed inclusion/exclusion rules and scenario explanations still need validation.

| Scenario | Supplied effort | Conditions / limitations |
|---|---|---|
| Optimistic | 2 person-days | Favorable conditions unspecified; not a guaranteed minimum |
| Most likely | 5 person-days | Typical conditions unspecified; not a committed duration |
| Pessimistic | 14 person-days | Adverse conditions unspecified; not a maximum or 95% bound |
| Capacity | 3 available person-days/week | Supplied availability; weekly distribution and sustained allocation over the task remain to confirm |
| External environment | Wait unknown | Elapsed-time dependency; do not silently include a made-up delay or treat it as zero |

## Valid calculation
PERT convention: **(2 + 4×5 + 14)/6 = 6 person-days**.

Triangular convention: **(2+5+14)/3 = 7 person-days**. This is a useful alternative that gives the adverse case more relative weight. PERT is selected because a most-likely scenario is supplied and the convention weights it explicitly, not because its mean happens to match the manager's desired window.

Spread heuristic: **(14−2)/6 = 2 person-days**. No validated distribution exists; this is not evidence of normality. Neither “6 ± 2×2” nor any automatic percentile calculation establishes a 95% interval or date. The **2–14 person-day scenario range** is a planning description, not a statistical confidence interval.

At a uniform effective rate of 3 person-days/week, capacity equivalents are:
- Optimistic: 2/3 ≈ **0.67 weeks**.
- Most likely: 5/3 ≈ **1.67 weeks**.
- PERT mean: 6/3 = **2 weeks**.
- Pessimistic: 14/3 ≈ **4.67 weeks**.
- Triangular mean: 7/3 ≈ **2.33 weeks**.

These are workload-to-capacity ratios, not a calendar forecast or probability distribution. Two weeks would offer six person-days if that availability is realized, leaving no margin relative to the PERT central effort for extra effort. Environment waiting may extend elapsed time; its effect depends on when access is needed and whether other work can proceed. It cannot be added correctly without dependency timing.

## Method limits and next investigation
Three-point estimation is suitable for this bounded effort discussion. Comparable completed-task history or decomposed work could improve the basis, but neither was supplied. If the environment changes feasibility or the task boundary, conduct a bounded investigation before refining a delivery forecast: establish when a usable environment can be provided, its access/acceptance prerequisites, and which work is blocked. Proposed investigation owner is the interface engineer with the environment provider; names, accepted assignment and effort cap require agreement.

## Planning handoff
Pass the effort scenarios and assumptions to the actual schedule/capacity owner, currently unnamed. Confirm:
1. scope and completion rule, including testing, review and environment setup; avoid double counting;
2. start date, working calendar, distribution of the three available person-days and continued allocation;
3. environment availability, task sequence and parallelizable work;
4. scenario conditions and relevant actual data for any later probability model.

Keep **“exactly two weeks after start” as the manager's requested target**, separately from the estimate. Even a supplied start date would not fix the missing waiting/probability evidence. Record any commitment only after feasible planning and the actual authority's decision.

Re-estimate on environment clarification, changed scope/capacity, actual effort or new comparable evidence. No validated 95% date, team acceptance of the estimate, or approved delivery commitment is established.
