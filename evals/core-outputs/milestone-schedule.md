# Cedar milestone schedule analysis

As of 2026-10-22. Approved baseline C-B1 / C-01 (2026-10-01): cutover 2026-11-14. The manager's 2026-11-21 suggestion is unapproved. This instructional network is not yet a mapped Cedar delivery schedule.

The schedule helper was run on controls-schedule-input.json. Units are working-day offsets from zero, with finish-to-start, zero-lag links, a common origin/finish and no resource leveling or calendars.

| Activity | Duration | Predecessor | Early start/finish | Late start/finish | Total float | Resource |
|---|---:|---|---|---|---:|---|
| A | 2 | None | 0 / 2 | 0 / 2 | 0 | Unknown |
| B | 4 | A | 2 / 6 | 2 / 6 | 0 | Dev full-time |
| C | 4 | A | 2 / 6 | 2 / 6 | 0 | Dev full-time |
| D | 1 | B, C | 6 / 7 | 6 / 7 | 0 | Unknown |
| E | 0 | D | 7 / 7 | 7 / 7 | 0 | Milestone; acceptance unspecified |

Both A-B-D-E and A-C-D-E are critical paths. All activities have zero float in this model; there is no distinct near-critical branch. The calculated finish is offset 7. It proves the dependency-only minimum under the supplied durations; it does not prove a seven-day calendar commitment.

B and C overlap completely and require the same full-time person. With Dev as the sole eligible resource, sequencing B then C (or C then B) yields A 0-2, B 2-6, C 6-10, D 10-11, E 11: 11 working-day offsets, conditional on continuous full-time availability and the stated durations. Resource sequencing is a proposed constraint, not an original technical dependency. Additional skilled capacity could restore parallel work only after availability and costs are confirmed. Dev's actual next-week availability is 28 hours with 32 hours of known demand, so even this leveled illustration is not a commitment.

| Cedar gate | Required evidence | Target / baseline | Forecast | Approval role |
|---|---|---|---|---|
| Vendor mapping accepted | Usable mapping tested against agreed integration needs | Need 2026-10-27; individual baseline unknown | Vendor expectation 2026-10-29, not accepted commitment | Receiver Dev and provider Kit; acceptance criteria to agree |
| Attachment rehearsal passes | Broken links corrected and linkage retested successfully | Unknown | Unknown; current failure | Business owner Inez, technical evidence Dev |
| Restore demonstrated | Executed restore result meeting Pax's agreed criteria | Before operational handover | Unknown; not demonstrated | Pax |
| Cutover readiness | Scope evidence, acceptance, operational readiness and authorized go/no-go | C-B1 2026-11-14 | Unknown; 2026-11-21 is only a suggestion | Confirm governance with Nia; Inez/Pax acceptance |

Sol should obtain task-to-deliverable mapping, estimate basis, start anchor, daily calendars/holidays/leave, other resource needs, actual remaining effort, vendor handoff commitment and review/acceptance lead times. Reconcile the two-calendar-day vendor expectation gap and Dev's overload before date approval. Keep C-B1 intact and submit any justified revised date through Nia with impacts and evidence. No new baseline approval is recorded.
