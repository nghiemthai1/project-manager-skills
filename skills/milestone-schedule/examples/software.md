# Software integration: work the forward and backward passes

Fictional instructional network, not Relay's approved calendar schedule. Unit: working-day offsets from zero. Assume finish-to-start links, zero lag and distinct available resources for parallel branches. No holidays, real dates or post-integration release gates are modeled.

| Task | Duration | Predecessors | ES | EF | LS | LF | Total float |
|---|---:|---|---:|---:|---:|---:|---:|
| A Agree contract | 2 | None | 0 | 2 | 0 | 2 | 0 |
| B Implement interface | 4 | A | 2 | 6 | 2 | 6 | 0 |
| C Prepare receiver tests | 3 | A | 2 | 5 | 3 | 6 | 1 |
| D Integrate | 1 | B, C | 6 | 7 | 6 | 7 | 0 |

Forward: D cannot start at C's finish 5 because B finishes at 6. Its ES is max(6,5)=6 and EF=7. Backward: D must start at 6 to retain finish 7, so B/C each have LF=6. C's LS=6−3=3; its ES=2, giving one working day of total float. A-B-D governs finish. C's float is not a promise of spare people or a calendar holiday allowance.

Run the [source input](../assets/software-network.json) from this skill folder:

```sh
python scripts/schedule.py --input assets/software-network.json --format markdown
```

## Changed-duration case

If B increases from four to six working days, its EF becomes 8; D runs 8–9 and finish becomes offset 9. C still finishes at 5 and now has LS 5/LF 8, so total float becomes 3. The change adds two working-day offsets to this network. It does not prove a two-calendar-day delay to Relay's pilot because real calendars, staffing, acceptance and subsequent work are absent.

## Decision and evidence

Mina should obtain the actual remaining network before altering the 30 October forecast. Lena's security acceptance needs its own evidence and review availability. If B and C use the same full-time specialist, even the original seven-day model is infeasible until the resource conflict is resolved. The Gantt skill's separate dated example illustrates calendar placement; it does not promote this toy network into Relay's baseline.

**Repair:** “The vendor is two days late, so move the pilot two days” skips the remaining logic. Retain the local gap, compute the actual affected network and obtain an authorized baseline decision only if a commitment changes.
