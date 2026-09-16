# Relay: scope with a recovery dictionary

Fictional artifact as of 16 October 2026. B1 was approved by Ada under D-001 on 2 October. The decomposition and detailed assignments below are a working interpretation for confirmation; they do not add a new approval. SCIM is excluded; optional operator dashboard polish is still within B1 at this date.

| WBS ID | Deliverable / included work | Completion and boundary | Proposed delivery role |
|---|---|---|---|
| 1.0 | Accepted pilot service access | One pilot tenant; SAML, audit, recovery and reversible rollout | Mina coordinates overall scope |
| 1.1 | SAML access capability | Defined pilot behavior and applicable test evidence | Omar |
| 1.2 | Audit-event integration | Agreed events usable by the receiving interface; shared integration counted here once | Omar with platform input |
| 1.3 | Recovery access and evidence | R-ACC03 demonstration and Lena's security acceptance | Omar prepares; Lena accepts |
| 1.4 | Service transition package | Guidance, reversal procedure, agreed support coverage and eventual Theo acceptance | Mina coordinates; contributors to confirm |
| 1.5 | Optional operator dashboard polish | Improvement inside B1, separately identifiable for tradeoff | Omar/Priya to confirm boundary |
| 1.6 | Project control and closure evidence | Baseline/change records, coordinated reviews and accepted residual handoff | Mina |

## Dictionary: 1.3 Recovery access and evidence

Output: demonstrated authorized recovery when the external identity provider is unavailable, preserving auditability and access controls. This elaborates the existing fictional R-ACC03 requirement. Included work is recovery implementation, applicable demonstration preparation, execution evidence and correction/retest if needed. SCIM provisioning is excluded; general operator guidance belongs to 1.4, with this package supplying recovery-specific input rather than duplicating the whole guide.

Omar is the proposed delivery role consistent with his engineering role; detailed effort allocation is not confirmed by the WBS. Lena's security acceptance is distinct from Theo's review of operator usability. Required inputs include applicable configuration and environment; availability and precise acceptance test details need confirmation. No estimate is supplied, so the dictionary hands its defined scope and uncertainty to estimation rather than adding invented days.

## Coverage and change review

The hierarchy includes acceptance and transition work that a “frontend/backend” list would omit. The shared audit integration is counted in 1.2, while each team's internal implementation remains bounded. An open review must confirm affected administrator representation and the exact receiver for the platform interface.

Deferring 1.5 may be a useful proposal, but on 16 October it is not yet an authorized deletion. CR-001 on 19 October later approves that deferral. Preserve the dated B1 view and link the later change rather than pretending the polish was always excluded.

**Repair:** “WBS = SAML frontend, backend and meetings” cannot show who proves recovery or accepts service. The revised hierarchy exposes those deliverables and their distinct completion evidence.
