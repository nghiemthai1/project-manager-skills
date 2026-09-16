# Migration rehearsal: two controlling branches

Fictional instructional subcase, not Northstar's approved cutover or actual rehearsal history. Unit: working-day offsets. Technical links are finish-to-start with zero lag; the initial calculation assumes B and C can operate in parallel with separate capacity.

| Task | Duration | Predecessors | ES | EF | LS | LF | Total float |
|---|---:|---|---:|---:|---:|---:|---:|
| A Extract sample | 2 | None | 0 | 2 | 0 | 2 | 0 |
| B Validate mapping | 3 | A | 2 | 5 | 2 | 5 | 0 |
| C Prepare restore environment | 3 | A | 2 | 5 | 2 | 5 | 0 |
| D Reconcile and restore | 2 | B, C | 5 | 7 | 5 | 7 | 0 |
| E Accept rehearsal | 0 | D | 7 | 7 | 7 | 7 | 0 |

Both A-B-D-E and A-C-D-E total seven working days. Accelerating B by one day leaves C finishing at offset 5, so D and E do not move. The zero-duration E represents the acceptance event only; any preparation, review effort or waiting would need activities and constraints of its own.

Run the [source input](../assets/migration-network.json):

```sh
python scripts/schedule.py --input assets/migration-network.json --format markdown
```

## Resource-feasible alternative

If Chen must work full time on both B and C, their overlap is impossible. One explicit scenario adds B-before-C as a resource-order choice while preserving the original technical need for A. The sequence becomes A 0–2, B 2–5, C 5–8, D 8–10, E at 10. Ten offsets is the resource-feasible duration under this simplified availability assumption. Do not call the extra order an original technical requirement. C-before-B has the same total here; a real choice should consider readiness and downstream value.

Jules must still confirm Chen's actual availability, vendor mapping, environment readiness and Saira's review timing, then apply the real calendar. Northstar's approved Saturday cutover cannot be placed by assuming every activity uses a weekday-only calendar.

The later M-CR02 approval changes the real baseline to 28 November; this toy calculation neither creates that decision nor rewrites the earlier 21 November comparison.

**Repair:** “Accelerate mapping and finish earlier” ignores the tied restore branch and shared specialist. Inspect both controlling paths and the resource model before choosing a compression action.
