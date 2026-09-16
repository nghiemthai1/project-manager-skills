# Relay: R-ACC03 from requirement to acceptance

Fictional artifact with two snapshots. R-ACC03 requires a tenant administrator to regain authorized access when the external identity provider is unavailable while preserving auditability and access controls. This existing instructional requirement elaborates the approved recovery boundary. Lena is security acceptance authority; Theo reviews operator guidance. Exact test identifiers and evidence file paths have not been supplied.

## Snapshot 1 — 28 October 2026

| Chain element | Current entry | Evidence state |
|---|---|---|
| Requirement/source | R-ACC03; recovery within approved pilot scope | Scope supported; detailed test design still needs its applicable record |
| Deliverable | Recovery access implementation and demonstration | Implementation completion not independently established here |
| Criterion | Authorized administrator can recover access with required controls/auditability | Observable behavior; detailed configuration and checks to record |
| Planned verification | Applicable recovery demonstration and review of control/audit results | Planned; no completed demonstration supplied |
| Execution evidence | Absent as of this snapshot | Not a passed test; do not invent a file path or run ID |
| Security decision | Lena rejects readiness because evidence is missing | Requirement not accepted for the release gate |
| Operator guidance | Theo's usability review is separate | Review result not supplied; documentation alone proves no behavior |

Other SAML tests passing cannot close R-ACC03. “Recovery documented” would support only the existence of guidance, not execution or acceptance. The action is to obtain applicable demonstration evidence and the actual review decision; exact timing and capacity require confirmation.

## Snapshot 2 — 2 November 2026

The scenario records successful security evidence accepted on 2 November. Add that dated acceptance to the chain and retain the 28 October gap/rejection. The underlying run identifier, build/configuration and artifact location are not in this short scenario; a real operational matrix must retrieve them before claiming a fully inspectable evidence pack. The teaching example reports the supplied acceptance fact without fabricating those details.

This later decision does not authorize every release condition or establish Theo's eventual service transfer. It also does not make the earlier matrix wrong: that matrix accurately represented the evidence available then.

## Change-impact check and repair

If a recovery configuration changes after the demonstration, review which R-ACC03 checks remain applicable. Preserve prior results and request targeted refresh where the changed behavior affects them. Do not automatically retain all passes or discard unrelated evidence without analysis.

**Repair:** “Recovery documented, therefore accepted” becomes “guidance exists; demonstration absent on 28 October; later security acceptance recorded on 2 November, with operational evidence references still needed for full auditability.”
