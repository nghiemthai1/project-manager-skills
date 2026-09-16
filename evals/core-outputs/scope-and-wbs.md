# Cedar scope and WBS — draft v0.1, 22 October 2026
Based on C-B1 / C-01 (1 October). The mandate is approved; this decomposition and proposed criteria/assignments need owner review. Cutover remains 14 November and the performance budget USD 200,000; separate reserve USD 20,000.

**Export and import are activities within migration, not a complete scope model.** UI customization is not established as a deliverable by the supplied mandate; retain only configuration demonstrably necessary for accepted support workflows. Analytics redesign is excluded. The historical-analytics favor requires impact analysis and an authorized change if it adds analytics work; historical archive access already in scope must not be confused with analytics.

Proposed accountable package owners are labeled below. Acceptance roles use Inez for business and Pax for operations; detailed authority/criteria remain to be confirmed.

| WBS ID | Parent | Deliverable / outcome | Package owner | Completion evidence, proposed | Boundary / interfaces / assumptions |
|---|---|---|---|---|---|
| 1 | — | Accepted support migration | Sol coordinates | Inez/Pax acceptance and authorized cutover/closure | Root covers approved scope plus necessary enabling work; final release authority to confirm |
| 1.1 | 1 | Controlled project and transition plan | Sol, proposed | Scope, decision/change records, integrated plan, closure record | Coordinates all packages; does not duplicate technical testing |
| 1.2 | 1 | Usable migrated data | Dev, proposed | Child packages reconciled and business accepted | Active tickets and attachments only; archive access separate |
| 1.2.1 | 1.2 | Active ticket population migrated | Dev, proposed | Identity/content/status reconciliation and reviewed exceptions | Contains export/import activities; needs agreed mapping/population; vendor mapping interface |
| 1.2.2 | 1.2 | Valid attachment content and ticket links | Dev, proposed | Content/link integrity evidence and regression results | Owns attachment linkage remediation; no duplication of ticket field migration; behavior currently uncertain |
| 1.3 | 1 | Authorized usable access | Owner unassigned | Positive/negative permission tests and reviewer acceptance | Accounts/roles needed for workflows; security authority and role rules to confirm |
| 1.4 | 1 | Demonstrated recovery capability | Owner unassigned; Pax operational acceptance | Executed restore against agreed recovery criteria and usable procedure | Owns recovery validation, not all migration tests; restore currently undemonstrated |
| 1.5 | 1 | Trained support users | Owner unassigned; Inez business acceptance | Training completion and workflow demonstrations | Training content depends on usable workflows; population and competence criteria unknown |
| 1.6 | 1 | Accessible retained archive | Owner unassigned; Inez business acceptance | Authorized retrieval and access-control evidence | Provides archive access, not analytics redesign; retention/access rules need confirmation |
| 1.7 | 1 | Release and service transition evidence | Sol, proposed | Child package results accepted and handover recorded | Integrates results; does not re-estimate all component test work |
| 1.7.1 | 1.7 | Integrated rehearsal and readiness assessment | Dev, proposed | End-to-end workflow evidence and dispositioned defects | Owns cross-package validation; component tests stay with originating packages |
| 1.7.2 | 1.7 | Controlled cutover and operational handover | Execution owner unassigned; Pax operational acceptance | Authorized cutover, validated service, support ownership, closure/open-item disposition | Cutover and reversal runbook use 1.4 recovery capability; reversal criteria and final decision authority to confirm |

## Coverage and overlap review
The six explicit scope elements all have homes: tickets 1.2.1, attachments 1.2.2, access 1.3, restore 1.4, training 1.5, archive access 1.6. Governance, integration testing, cutover, reversal preparation, and handover appear explicitly. Children of 1.2 separate ticket migration from attachments; children of 1.7 separate integrated evidence from execution/transition. Lower detail remains open until packages can be credibly estimated and assigned.

Do not double count export/import as separate deliverables in addition to 1.2.1, count component tests again under 1.7.1, or charge restore construction twice under reversal. Vendor mapping is an input to 1.2 and the dependency plan, not unexplained miscellaneous scope.

## Decisions before estimating affected packages
Clarify whether “historical analytics” means existing archive retrieval or new analytics capability. The former belongs within 1.6 if consistent with approved requirements; the latter needs a documented change assessment for Nia's authorized decision and is not approved as a favor. Confirm the necessary UI configuration, acceptance criteria, data populations, recovery objectives, security reviewer, and unassigned package owners.

Provide these packages to estimation, capacity, and dependency/schedule planning. The WBS does not establish sequence or critical path. Current planning must account for broken links, the vendor gap, and Dev's four-hour overload. This draft is the first decomposition supplied; no earlier WBS baseline or approved scope change is evidenced.
