# Cedar cutover readiness review

Review date: 2026-10-22. Release boundary: hosted-service migration of active tickets, attachments, access, restore, training and archive access. Build/version and environment identifiers are unknown. Approved cutover baseline is 2026-11-14, C-B1 / C-01; November 21 is unapproved. Nia is sponsor, Inez business acceptance owner and Pax operations owner; actual go/no-go and exception authorities must be confirmed rather than inferred from budget authority. Detailed criterion thresholds are proposed pending agreement.

| Gate | Required evidence | Actual evidence | Acceptance owner | State / consequence |
|---|---|---|---|---|
| Release identity | Immutable build/config/data/environment scope matching tests | Not supplied | Technical owner to confirm | Unknown; applicability cannot be established |
| Engineering completion | Completed scope plus relevant verification | Engineering reports code complete; supporting evidence absent | Dev technical coordination | Reported only; no business/operational acceptance inferred |
| Attachment integrity | Successful correct-ticket linkage and accessible attachments after migration | Rehearsal failed; specific version/date not supplied beyond status context | Inez with Dev evidence | Failed; blocking functional scope defect; no exception |
| Active-ticket completeness/usability | Reconciliation and business workflow results | Not supplied | Inez | Unknown; require evidence |
| Access and archive | Approved access tests and archive retrieval results | Not supplied | Inez/Pax roles to agree | Unknown |
| Recovery | Executed relevant restore/rollback evidence within agreed objectives | No result; execution status unknown | Pax | Missing; blocking recoverability evidence |
| Immediate service coverage | Accepted named rota, incident path and authority throughout cutover | Operations has not accepted coverage | Pax | Not accepted; blocking owner gap |
| Training and communication | User/support readiness, approved messages and escalation routes | Not supplied | Inez/Pax | Unknown |
| Vendor handoff | Usable mapping accepted by Dev | Expected October 29; need October 27 | Dev receiver / Kit provider contact | Pending; threatens integration/testing time |
| Authorization | Explicit decision for defined version/window and conditions | No go decision supplied | Actual authority to confirm | Not authorized |

Recommendation: HOLD. A reported 95% checklist completion cannot offset failed attachment behavior, absent recovery evidence or unaccepted coverage. It is not launch permission. No exception has been authorized; conditional go is unsupported without rules permitting specific exceptions and the appropriate acceptance/waiver authority.

Recovery and monitoring preparation: identify irreversible data changes and external effects, last safe recovery decision point, recovery duration and tested limits. All are currently unknown; do not promise rollback. Propose watching ticket/attachment usability, access errors, reconciliation failures and service health, with Pax/Dev agreeing thresholds and an incident/recovery decision owner. Immediate cutover coverage is separate from later full handover and must be accepted before launch.

Change recommendation only after repaired linkage passes on the intended release, Pax accepts applicable executed recovery evidence and coverage, remaining scope gates are evidenced, dependencies and capacity are feasible, and authorized exceptions (if permitted) are recorded. Record actual decision separately: pending; no authority, timestamp or go reference exists. Recheck on build/config/data changes, new defects, changed window/resources or invalidated recovery evidence. C-B1 remains unchanged while Sol prepares evidence and date/funding options.
