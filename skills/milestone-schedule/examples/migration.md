# Milestone Schedule: migration example

Fictional training scenario. Values and thresholds are examples, not defaults for real projects.

## Instructional migration network

An example rehearsal contains A: extract sample (2 working days), B: validate mapping (3 after A), C: prepare restore environment (3 after A), D: reconcile and restore (2 after B and C), and E: accept rehearsal (0 after D).

Both A-B-D-E and A-C-D-E take seven working days. B and C are both critical. Shortening B alone does not shorten the finish while C still takes three days.

## Application to Northstar

Jules records actual calendars and Chen's availability before scheduling the rehearsal. If Chen is required full-time on both B and C, the parallel model is infeasible. The schedule must sequence or resource the work explicitly, then recalculate. The vendor mapping and Saira's acceptance availability are external constraints to confirm.

The 9 November approval changes the baseline cutover to 28 November. Earlier reports retain the original 21 November baseline.

## Repair

**Flawed:** "Accelerate mapping and the whole rehearsal finishes earlier."

**Corrected:** "Mapping and restore preparation are tied critical branches in this model. Improvement must address both, and the resource plan must permit parallel execution."
