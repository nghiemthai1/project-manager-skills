# Relay charter — draft before authorization

Fictional training artifact. Version R-CH-0.1, 29 September 2026. Mina prepares this proposal for sponsor Ada. No integrated baseline is approved yet; the later D-001 decision must not be backdated into this charter.

## Need and outcome

Provide enterprise single sign-on for one pilot tenant while retaining auditability, secure recovery and operable support. The supplied scenario identifies the desired capability, but does not quantify the existing support burden, failure rate or business return. Those benefits remain hypotheses until Priya and the business stakeholders define evidence.

| Included deliverable | Boundary | Explicit exclusion / interface |
|---|---|---|
| SAML login | One agreed pilot tenant and authorized workflows | SCIM provisioning excluded; identity-provider interface to validate |
| Audit events | Required event behavior and receiving integration | Event contract and receiver acceptance to agree |
| Recovery access | Demonstrable secure recovery path | Security criterion and environment applicability owned by Lena |
| Operator guidance and reversible rollout | Usable procedures, coverage and tested recovery limits | Ongoing service boundary agreed with Theo |
| Optional operator dashboard polish | Within proposed scope; can be assessed for deferral | Any deferral is a scope decision, not an implicit waiver |

## Proposed success and evidence

| Type | Proposed criterion | Evidence / owner | Timing |
|---|---|---|---|
| Delivery | Authorized pilot workflows succeed and inappropriate access is rejected | Applicable functional evidence; business acceptance role to confirm with Priya | Before pilot decision |
| Security acceptance | Agreed secure recovery demonstrated | Executed recovery evidence / Lena | Before readiness approval |
| Service acceptance | Theo accepts defined support, guidance and ongoing responsibilities | Handover packet and explicit acceptance / Theo | At transfer, after verified execution |
| Performance | Pilot target 30 October; proposed performance budget USD 100,000 | Integrated plan and sponsor decision still required | At baseline review and subsequent control points |
| Benefit | Improved pilot access/support experience | Baseline, measure and target not supplied; propose Priya as benefit owner | Later operational review; date not yet authorized |

Numbers are proposal inputs, not approved funds. Proposed separate management reserve is USD 10,000, controlled by Ada if authorized. It is not part of performance BAC and is not automatically available to spend. Detailed effort, calendar, staffing and cost feasibility still require integrated planning.

## Material assumptions and open decisions

The audit interface will be available in a usable form; its contract, date and receiving acceptance must be confirmed. Engineering and security capacity are not established by naming Omar and Lena. The pilot tenant and administrator representation need agreement. A reversible rollout requires applicable evidence, not only a written rollback plan.

Mina coordinates the plan and decisions. Ada is the proposed baseline/funding authority. Lena and Theo retain distinct acceptance responsibilities; Ada's sponsorship does not replace them. PM spending tolerances, final pilot go authority and business acceptance delegation remain to be confirmed.

## Decision requested and handoff

Ask Ada to decide the bounded scope, funding structure and integrated baseline once feasibility and acceptance conditions are explicit. Until then this remains a proposal. Hand the open interfaces, criteria and authority gaps to kickoff and planning. The scenario subsequently records D-001 on 2 October; that is a later decision record, not evidence of approval on 29 September.

**Repair:** “Approved: enterprise identity for all tenants by 30 October” invents both expanded scope and authorization. Keep one-tenant SAML, exclude SCIM, distinguish target from baseline and state the actual decision needed.
