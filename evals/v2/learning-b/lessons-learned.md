# Finch contextual lesson — counts and relationship correctness

Document lifecycle: **draft**. Lesson ID, author and evidence dates: not supplied; no identifier invented to replace source IDs **F-M2** or **L-9**.

**Observed lesson:** equal source/target counts did not prove correct parent relationships in F-M2. **Proposed practice:** assess relationship checks using L-9. Its actual use and effectiveness are unverified; publication and a later successful migration do not make it battle-tested or guarantee correctness.

Learning question: what evidence should establish correct migrated relationships, separately from volume reconciliation?

## Evidence chain
| Expectation / question | Supplied observation | Interpretation or hypothesis | Actual intervention and result | Limits |
|---|---|---|---|---|
| Correct migrated data, including parent relationships | F-M2 had equal **1,000 source and target counts**, but **4 observed wrong parent links** | Counts measure cardinality; they do not establish the correct pairing of child and parent. Specific defect cause remains unknown | No corrective result for F-M2 supplied | Population and inspection coverage unknown. Do not report a 0.4% defect rate, four affected records, or exactly four total defects without a valid denominator and scope |
| Whether L-9 improves relationship verification | Team proposed relationship-check template **L-9** but had not used it at proposal stage | A relevant relationship check could detect defects counts miss; that is a hypothesis about L-9, not established effectiveness | Template later published; no actual use evidence supplied | Its content, coverage, executor, results and review cost are unknown |
| Whether subsequent success validates L-9 | Next migration succeeded after a smaller population, new vendor patch, extra engineer and template publication | Several changed conditions could explain the outcome; actual mechanism and contribution remain unknown | Reported successful migration, with no comparison isolating effects | Success criteria and detailed results are absent; neither L-9 use nor causal effect is established |
| Whether Ops adopted the practice | Recipient has not responded | Silence is neither agreement nor use | No accepted owner/process change or execution evidence | Cannot claim Ops adoption |

## Transferable principle and boundaries
Use evidence matched to the property claimed: **retain count checks for their limited reconciliation role, and evaluate relationship identity/correctness separately where relationships matter.** Do not ban all count checks; equal totals can coexist with omissions, duplicates or incorrect associations. No single check guarantees all correctness.

This lesson applies to migrations in which links between records have business meaning. Before choosing a method, establish the relevant population, expected relationships, mapping/version, independent reference data, exception rules and acceptance authority. Those specifics are not supplied for L-9.

Different data models, external references, access behavior or content defects may require additional checks. A small sample may miss failures; a check based on the same faulty mapping may reproduce the error rather than detect it. Relationship checks do not by themselves establish recovery, service readiness or overall migration acceptance. Possible costs include preparation, execution/review effort and false-positive investigation; none is quantified here.

## Practice maturity
- **F-M2 insufficiency finding:** supported by the supplied fictional observation; count equality did not establish correct parent links in that case.
- **L-9:** proposed and published; actual use/testing unverified. It cannot be promoted to “tested in a bounded case” merely because a later migration succeeded.
- **Ops adoption:** not evidenced. No response, accepted owner or changed process/use record.
- **Effectiveness or guarantee:** not established. The simultaneous population, patch and staffing changes prevent attribution, even if later L-9 use were discovered.

Publication state is separate from document quality, practice maturity and organizational adoption.

## Proposed adoption and review
| Proposed behavior | Owner / recipient status | Evidence and guardrail | Review / decision |
|---|---|---|---|
| Review L-9 against the required relationship property and define a bounded pilot | Technical/data-quality owner unassigned; Ops is proposed recipient only | Identify scope, expected relationships, version, effort cap and actual acceptor before committing; do not assume the published template contains adequate checks | Review before selecting a pilot; date and capacity to agree |
| Run a documented check on known failure and known correct fixtures, then a justified population/sample | Qualified performer and reviewer unassigned | Confirm detection of known wrong-parent cases and handling of correct cases; record coverage, false positives/negatives where known, runtime and review effort | Label results only for the tested boundary; detecting a defect is not repairing it |
| Evaluate a subsequent representative application | Receiving team must explicitly agree to use the practice | Retain actual L-9 version/use record, defects detected, escaped defects where ascertainable, other interventions and cost | Use a comparison or controlled variation where feasible; otherwise disclose confounding and avoid a causal claim |
| Establish Ops adoption if useful | Ops response and accepted process owner pending | Record explicit acceptance, changed process and actual use; publication/receipt alone is insufficient | Adopt in that stated setting, revise if coverage/cost is unsuitable, or stop using the method if it cannot test the required property |

Do not reward a low defect count achieved by reducing coverage, hiding findings or weakening acceptance. Track both coverage and correctness evidence. A bounded success can justify further evaluation, not universal reliability.

Source references: **F-M2** migration observation, **L-9** proposal/publication, later migration outcome and unanswered Ops recipient are supplied case facts. No artifact paths, URLs, timestamps or actual source logs were provided; none are fabricated. Proposed next step is to recover those records and agree the bounded evaluation.

Revision history: this draft preserves the initial failed-relationship observation and later reported success with its confounders. No superseded prior lesson is supplied. No template change, distribution, recipient contact or adoption has been performed by this artifact.
