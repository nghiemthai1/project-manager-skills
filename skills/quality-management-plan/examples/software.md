# Relay: quality plan for the recovery path

Fictional plan and status snapshot as of 28 October 2026. B2 funding/scope changes did not waive security acceptance. Lena has rejected readiness because recovery access has not been demonstrated. Rows below describe a proposed quality approach; they do not assert that all listed checks were executed.

| Criterion / need | Preventive practice | Planned evidence and applicability | Authority / actual status |
|---|---|---|---|
| SAML login works for the pilot tenant | Review identity-provider contract and tenant configuration | Executed permitted/denied sign-in cases on the intended build/configuration | Relevant test result not supplied in this snapshot |
| Agreed audit events are usable | Review schema and receiver expectations together | Evidence of expected events and failure behavior reaching the receiver | Interface delivery timing alone is not verification |
| Recovery access can be performed | Review recovery procedure with engineering/security and operators | Demonstration on applicable configuration, with results and limitations retained | Lena rejected readiness on 28 October; required evidence absent |
| Operators can follow guidance and reverse rollout | Walk through procedure before the gate | Observed operator execution and reversal evidence | Theo's service acceptance remains separate and not yet recorded |

## Defect and gate handling

Record the missing recovery demonstration as a readiness blocker with its evidence gap. Omar owns technical remediation in the scenario; exact execution/review times require agreement. A plan to demonstrate recovery tomorrow is still a plan. After execution, retain the original failure/gap and add the new result with its build/configuration and Lena's actual acceptance decision. Do not backfill the later 2 November acceptance into 28 October.

Additional fictional reporting example: of 12 applicable checks, 8 passed, 1 failed and 3 are blocked/not run. The executed pass fraction is 8/9, while completion is 9/12. Neither ratio establishes readiness; the identity and consequence of the failed and blocked checks matter. These counts are a teaching subcase, not Relay test results.

## Improvement hypothesis

Hypothesis: rehearsing the recovery evidence package earlier with the intended reviewer will expose missing inputs before the release gate. Proposed trial: review the next package before scheduling its formal demonstration, then compare the specific omissions found and gate rework. Trial owner/date are not yet assigned. Completing the review meeting alone would not establish improvement.

**Repair:** “Most tests passed, so quality is green” averages away a required recovery gate. State the failed/absent evidence and its decision consequence directly.
