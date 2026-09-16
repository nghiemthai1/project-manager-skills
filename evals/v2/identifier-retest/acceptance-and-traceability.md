# Beacon current traceability and acceptance

**BC-R7 is not accepted for v2.** Two v2 attachment failures were observed on 4 October, and Fran has not accepted v2. Preserve the 1 October v1 sample pass as historical evidence; do not relabel it as v2 evidence or approval.

Source: supplied fictional case. Requirement source-document location, scope/version authority, current as-of date/year, execution environment, evidence artifact paths and test IDs are unknown.

| Requirement ID / source | Deliverable | Observable criterion / method | Executed evidence and population | Result / applicability | Acceptor / actual decision | Gap / next action |
|---|---|---|---|---|---|---|
| BC-R7 / supplied requirement: correct attachment relationships for agreed population | Attachment relationships under v1 mapping | Exact executed check not supplied | 1 October: ten-record sample passed on v1; sample selection and relationship coverage unknown | Historical reported pass limited to tested sample; neither whole-population coverage nor applicability to changed v2 is established | Fran identified as owner; v1 acceptance decision not supplied | Retain result and inspect test/data/mapping details before deciding whether any portion can be reused |
| BC-R7 / same requirement | Attachment relationships under v2 mapping | Validate correct identities and attachment-to-parent relationships across agreed population; detailed criterion below is proposed | Mapping changed to v2 on 3 October; two v2 attachment failures observed 4 October; population/denominator and evidence paths unknown | Current adverse evidence. No valid failure rate or population-wide result can be inferred | Fran has **not accepted v2**; no decision reference or exception supplied | Identify failing cases, investigate cause, correct and execute applicable retests; seek Fran's bounded decision |
| BC-R7 / supplier's claim | Counts associated with mapping/version not specified | Count comparison, scope and execution method unknown | Supplier says same counts mean good to go; supporting record/version/date absent | A reported count result does not verify correct relationships or overcome observed v2 failures | Supplier claim is not Fran's acceptance | Obtain underlying count evidence if useful; keep it separate from relationship correctness and approval |

## Proposed completion criterion
For the explicitly agreed population and mapping version, each included attachment must resolve to its correct expected parent with the required relationship preserved. Agree authoritative identifiers/matching rules, handling of missing or incorrect parents, and any allowed exceptions with Fran before recording those details as approved. No new tolerance or exception is invented.

Proposed verification: compare actual to independently established expected relationships, include the known v2 failing cases and relevant negative/exception paths, and record version/configuration, population, selection/coverage, environment, date, observed results and limitations. A planned check is not an execution result. Test performer and technical reviewer remain unassigned.

## Version and evidence-impact record
| Event | Affected requirement/evidence | Applicability decision now | Required review |
|---|---|---|---|
| v1 ten-record sample passes 1 October | BC-R7 historical sample result | Retain as a v1 pass only; selection limits preserved | Recover exact tested relationships and source evidence |
| Mapping changes to v2 on 3 October | BC-R7 and checks sensitive to mapping | Relationship evidence needs impact review and targeted refresh; no blanket reuse as v2 acceptance | Determine what changed and whether any unchanged portion remains supported |
| Two v2 failures observed 4 October | BC-R7 current verification | Failures remain current contrary evidence; not overwritten by old pass | Investigate, remediate and retest affected behavior with coverage justified |
| Fran has not accepted v2; decision date unspecified | BC-R7 acceptance | Pending/not accepted; no waiver supplied | Present applicable results and limitations for actual decision |

Forward coverage: BC-R7 lacks sufficient current applicable proof across the agreed population. The population definition and sample basis must be recovered; no excluded subpopulation is invented. Backward coverage: linkage tests directly serve BC-R7; count checks may support a separate completeness question but cannot establish relationship correctness. No other authorized requirement or delivered feature was supplied for broader audit.

Recommendation: do not report BC-R7 or v2 as accepted. Hand the failures, applicability review and missing population evidence to the responsible readiness/acceptance process. Any later acceptance must identify the tested version, scope, evidence and actual authority decision. No baseline, test history or live acceptance record was changed.
