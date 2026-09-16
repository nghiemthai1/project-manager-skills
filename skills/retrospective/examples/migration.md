# Northstar retrospective after the 6 November rehearsal

Fictional training scenario. M-I002 records reproduced missing attachment links, related to M-R01. The fact that record counts match does not establish correct relationships. The precise root cause, test-population coverage and actual retrospective attendance are not supplied.

Use a timeline plus a focused causal inquiry: what checks were selected, what relationship rules were understood, and when applicable mapping evidence became available? “Testing was bad” is too broad to identify a change. Five Whys may help explore a hypothesis, but no link in that chain is proof without source evidence.

| Observation | Candidate explanation | Check before concluding |
|---|---|---|
| Links were lost in rehearsal | Earlier checks may have emphasized counts and missed relationship identity | Inspect actual criteria, test selection and results; do not presume nobody tested links |
| Supplier mapping matters | Identifier rules may differ across populations or versions | Compare failing cases and mapping/configuration; correlation is not root cause |
| Business acceptance is incomplete | Evidence may not cover the agreed use/population | Saira reviews scope/criteria and exception treatment |

Proposed experiment: add a bounded relationship-check suite and explicit exception review to the next authorized rehearsal. Include known failures and justified representative/negative cases; any seeded-failure exercise uses a suitable nonproduction test environment, not live records. Chen is proposed implementer subject to capacity/acceptance; Saira reviews whether the evidence addresses business criteria.

Hypothesis: explicit expected parent/attachment relationships expose errors that count checks cannot. Measure detection of known or safely seeded broken relationships, false positives and interpretable exceptions; retain counts for their separate completeness question. No universal sample size or allowed error rate is assigned. Guardrail: do not select only easy cases or call the entire migration correct because the experiment detects its own seeded examples.

Review after actual execution: record configuration/population, implementation, observed results, limits and the adopt/adjust/stop decision. None of those results is supplied now, so the practice remains proposed. Correction of the actual M-I002 defect remains required delivery work; it is not optional because the team is experimenting with its detection method.

The later 25 November restore failure needs a separate mechanism/evidence review. Do not merge relationship integrity and recoverability into a single vague lesson.

**Repair:** “Add more tests, close lesson” is replaced with a specific failure-detection hypothesis and a pending evidence review.
