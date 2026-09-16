# Northstar lesson: test the property that matters

Fictional training scenario. M-I002 on 6 November records lost attachment links, related to earlier M-R01. Counts can match even when a file points to the wrong ticket. That observation supports the limit of count reconciliation for this relationship requirement.

The transferable principle is to combine completeness checks with checks of the properties required for usable acceptance. Counts remain useful for population questions; they do not prove identity, relationships, permissions or recoverability. The lesson is not “counts are useless,” nor does it prescribe one universal sample size or error tolerance.

A proposed practice adds expected relationship rules, applicable mapping/version, justified coverage and explicit exception disposition to the migration acceptance template. It fits migrations where parent/child associations carry business meaning. Other transformations may need different invariants; sampling only easy records or repeating known seeded cases cannot establish all-population correctness.

| Evidence state | What can be claimed |
|---|---|
| Observed lost links despite count-oriented assurance | The supplied checks did not establish the required relationship property |
| Proposed relationship-check suite and exception review | A rationale for improving evidence; no measured effect yet |
| Later successful rehearsal/acceptance | A bounded outcome in the scenario; not proof that this proposed template change caused it |
| Broader adoption | Not supplied; cannot call it an organizational standard or field-tested method |

Adoption proposal: have the responsible migration/acceptance owners add the fields and review their usefulness on the next relevant migration. Saira's acceptance perspective is needed; Chen may contribute technical checks, but actual assignments/capacity remain to confirm. Measure detection and disposition of meaningful errors, false positives, coverage and review burden—not merely number of tests run.

Retain contrary results. If the revised check misses a different linkage mechanism, refine its applicability instead of editing history to say it always worked. A later restore failure concerns another property and should have its own evidence/lesson record.

**Repair:** “Matching counts are useless; this template guarantees correctness” overreacts in both directions. The corrected lesson explains what counts establish, which other properties need proof and what remains untested about the adoption proposal.
