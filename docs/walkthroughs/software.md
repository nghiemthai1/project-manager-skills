# Relay: from mandate to accepted handover

This is a complete fictional training walkthrough. It follows the [shared scenario](../SCENARIOS.md) and adds explicitly identified financial and transfer evidence at closure. Figures are examples, not recommended budgets or tolerances.

## 1. Establish the mandate

Use [Project Charter](../../skills/project-charter/SKILL.md), [Delivery Approach Advisor](../../skills/delivery-approach-advisor/SKILL.md), and [Project Kickoff](../../skills/project-kickoff/SKILL.md).

The proposed outcome is one enterprise tenant using SAML access with auditability and recovery. Included work is SAML login, audit events, recovery access, operator guidance, and a reversible rollout. SCIM is excluded. Mina coordinates the project; Ada sponsors it; Priya orders product work; Lena accepts security evidence; Theo accepts service handover.

Before 2 October, 30 October is a target. D-001 on 2 October approves B1: the stated scope, 30 October pilot, and USD 100,000 performance budget. USD 10,000 management reserve is separately sponsor-controlled. A kickoff attendee list alone would not establish that approval.

## 2. Connect the plan

Use [Scope and Work Breakdown](../../skills/scope-and-wbs/SKILL.md), [Acceptance and Traceability](../../skills/acceptance-and-traceability/SKILL.md), and [Integrated Project Planning](../../skills/integrated-project-planning/SKILL.md).

| Work package | Required completion evidence | Authority or receiver |
|---|---|---|
| SAML pilot access | Relevant functional and tenant validation | Product/business acceptance as agreed |
| Audit interface | Accepted contract tests and event evidence | Receiving integration owner |
| Recovery access | Demonstrated secure recovery | Lena |
| Service transition | Usable runbook, coverage, and ownership acceptance | Theo |
| Reversible rollout | Applicable recovery evidence and decision limits | Release authority and technical owners |

The plan must include these acceptance activities, not just coding. Dates for unknown handoffs remain unconfirmed. Resource constraints must be reconciled with the schedule before a promise is made.

## 3. Test estimates and capacity

An instructional integration task has O=2, M=4, P=12 person-days. [Estimation Advisor](../../skills/estimation-advisor/SKILL.md) produces a PERT central estimate of five person-days and a triangular mean of six. Neither is a five-day delivery guarantee.

For the 19–30 October capacity subcase, Omar has 56 available hours and 64 hours of demand, an eight-hour overload. Lena has 32 available and twenty demanded. Team totals show four spare hours, but the specialist overload remains. [Resource Capacity Plan](../../skills/resource-capacity-plan/SKILL.md) identifies the decision needed rather than transferring Lena's capacity by arithmetic.

The helper's four-task CPM demo gives a seven-working-day unconstrained duration, with C having one day of float. This toy network teaches the method; it is not Relay's calendar baseline. The actual interface's two-calendar-day gap must be assessed in the remaining integrated network.

## 4. Run the 16 October control review

Use [Delivery Control Cycle](../../skills/delivery-control-cycle/SKILL.md), [Dependency Map](../../skills/dependency-map/SKILL.md), [RAID Log](../../skills/raid-log/SKILL.md), and [Project Budget](../../skills/project-budget/SKILL.md).

| Record | Evidence | Consequence |
|---|---|---|
| DEP-001 | Interface expected 22 October; needed 20 October | -2 calendar-day local margin; final-date effect not yet established |
| R-001 | Possible interface incompatibility | Validate compatibility; probability not invented |
| I-001 | Test environment currently unavailable | Resolve actual blocker and assess verification impact |
| Budget | PV 50,000; EV 40,000; AC 48,000; BAC 100,000 | CPI 0.8333, SPI 0.8, CV -8,000, SV -10,000 USD |

If cost efficiency persists, EAC is USD 120,000. The forecast is USD 20,000 above BAC and USD 10,000 above the entire original envelope. It does not authorize funding. A cost-only continuation and a remaining-at-budget assumption produce different forecasts; the team must inspect remaining work rather than select whichever looks best.

## 5. Make and preserve changes

Use [Change Request](../../skills/change-request/SKILL.md), [Decision Log](../../skills/decision-log/SKILL.md), and [Escalation Brief](../../skills/escalation-brief/SKILL.md).

CR-001 proposes deferring optional operator dashboard polish and addressing the forecast funding gap. Ada approves on 19 October: the scope deferral, B2 performance budget USD 120,000, and the extra USD 10,000 beyond the original total envelope. The funding bridge includes the original USD 100,000, release/reallocation of the original USD 10,000 reserve, and USD 10,000 additional authorization. No unchanged reserve is silently counted a second time.

Security acceptance remains unchanged. The 16 October report stays against B1. A later status uses B2 with the decision link. A meeting record preserves what Ada approved, what Omar merely proposed, and what remained unknown about the pilot forecast.

## 6. Hold when readiness fails

Use [Release Readiness](../../skills/release-readiness/SKILL.md) and [Project Recovery Advisor](../../skills/project-recovery-advisor/SKILL.md).

On 28 October, recovery access has not been demonstrated and Lena rejects readiness. The recommendation is hold. Earlier scope and budget approval does not waive the evidence condition. D-004 on 29 October defers the pilot to 3 November. Security evidence is accepted on 2 November.

| Date | State | Evidence meaning |
|---|---|---|
| 28 October | Hold recommended | Required recovery evidence absent |
| 29 October | Date revised | D-004 changes the pilot date, not the test result |
| 2 November | Security evidence accepted | Relevant criterion now supported |
| 3 November | Pilot begins | Actual execution, distinct from approval |
| 6 November | Service handover accepted | Theo accepts defined ongoing responsibility |

## 7. Learn and close

Use [Release and Handover](../../skills/release-and-handover/SKILL.md), [Retrospective](../../skills/retrospective/SKILL.md), [Lessons Learned](../../skills/lessons-learned/SKILL.md), and [Project Closure](../../skills/project-closure/SKILL.md).

The retrospective distinguishes the observed missing evidence from hypotheses about why it was planned too late. A proposed improvement is to establish acceptance evidence lead times earlier. It is not called proven merely because a meeting is added.

For this complete walkthrough, add these fictional closure exhibits to the shared source set:

- F-001, finance reconciliation dated 9 November: final actual cost USD 119,000; no remaining project accruals or purchase commitments. This is additional evidence, not inferred from B2.
- H-001, 6 November: Theo accepts the service runbook, support coverage, access, and known-issue register. The register has no release-blocking items; any ordinary service backlog is accepted into Theo's ownership.
- C-001, 10 November: Ada approves closure after reviewing acceptance, H-001, and F-001. Final actual cost is USD 19,000 above original B1 and USD 1,000 below B2.
- BR-001: Priya accepts ownership of the 4 December benefit review. The measure is successful pilot access and support experience against the agreed business criteria; no benefit result is claimed yet.

The shorter closure skill example intentionally lacks F-001 and must report final cost unknown. This fuller walkthrough demonstrates how additional evidence resolves that gap without changing prior facts.

## What to check when reusing the workflow

Can every date be identified as target, baseline, forecast, or actual? Does each approval name its scope? Are operational and security conditions preserved through recovery? Does closure rely on actual evidence rather than the last approved plan? If any answer is unclear, return to the relevant record before polishing the summary.
