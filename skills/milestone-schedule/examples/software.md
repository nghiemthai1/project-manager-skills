# Milestone Schedule: software example

Fictional training scenario. Values and thresholds are examples, not defaults for real projects.

## Instructional network

This four-task exercise illustrates the method; it is not Relay's approved calendar schedule.

| Task | Duration, working days | Predecessors |
|---|---|---|
| A: agree contract | 2 | none |
| B: implement interface | 4 | A |
| C: prepare receiver tests | 3 | A |
| D: integrate | 1 | B, C |

Earliest finish is day-offset 7. A-B-D is critical. C begins at offset 2 and finishes at 5; its latest start is 3 and latest finish is 6, giving one working day of float.

If B grows from four to six working days, the unconstrained network finishes at offset 9. That does not prove Relay's pilot slips two calendar days: actual calendars, subsequent release gates, and resources are absent from this exercise.

## Decision

Mina uses this reasoning to request the actual remaining network before changing the 30 October forecast. Lena's security acceptance remains a separate gate and must have explicit exit evidence.

## Repair

**Flawed:** "The vendor is two days late, so move the pilot two days."

**Corrected:** "Recalculate the integrated network and reconcile calendars and resources. The known local delivery gap alone does not establish the pilot impact."
