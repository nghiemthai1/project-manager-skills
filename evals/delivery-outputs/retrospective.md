# Cedar retrospective — failed rehearsal

Draft based on evidence available 2026-10-22; rehearsal date and complete timeline unknown. Learning question: how can the team detect and act on attachment migration failures earlier without removing required acceptance work? Proposed participants: Dev, Kit, Inez, Pax and Sol; support-agent perspective is missing. No workshop attendance, consensus or assignment acceptance is claimed. Gather independent observations and logs before discussing explanations.

Prior improvement: “more testing” was proposed in the previous retrospective; no owner, review point or result was recorded. Its implementation and effect are unknown, not demonstrated failure or success. Recover any execution evidence; retain the old action and link the bounded replacement experiment below.

| Observation and evidence | Interpretation / uncertainty | Alternative to investigate |
|---|---|---|
| Attachment links failed in rehearsal | A relationship-preservation defect exists; technical mechanism and responsible changes unknown | Identifier transformation, mapping mismatch, environment/access behavior or test/data differences; inspect logs and examples |
| Manager says Kit was careless | An allegation, not a proven cause or motive | Unclear contract/acceptance criteria, missing review or tooling constraints may matter; seek Kit's perspective |
| Restore has not been demonstrated | Recovery evidence is missing | Timing, ownership and prerequisites may explain the gap; absence does not prove restore failure |
| Mapping expected October 29 vs need October 27 | Handoff plan and integration need conflict | Clarify usable partial delivery, estimate basis and when need was communicated |
| Dev has 28 available vs 32 demanded hours next week | Four-hour known overload constrains improvement work | Confirm other obligations, skilled cover and daily timing rather than assuming unlimited testing capacity |

Themes: observable relationship behavior and an accountable learning loop. Alternatives considered: simply increasing test volume lacks a targeted mechanism/measure; universal full-data testing has unknown cost; a bounded linkage regression experiment directly addresses observed behavior and can reveal whether the proposed test detects this known failure. Root-cause investigation remains necessary alongside the experiment.

| Experiment | Hypothesis | Owner / acceptance | Measure | Review point | Result |
|---|---|---|---|---|---|
| EXP-ATT-01: add an explicit attachment-linkage check to one next rehearsal cycle | A check that verifies correct parent ticket, target existence and authorized opening will detect the reproduced defect before business acceptance | Dev proposed technical owner; Inez proposed acceptance reviewer; Kit supplies defect evidence; assignments unconfirmed | On the same representative dataset/version, record eligible relationships, checked coverage, broken/wrong-parent/inaccessible counts, detection of the known failing case, runtime and false-positive review | At the next rehearsal evidence review, before readiness decision; calendar date to confirm | Not run; effectiveness unknown |

Plan: Dev/Inez agree representative coverage, retain the known failing fixture and capture build/config/data identity. Confirm time/effort and allocation in near-term planning; do not add unestimated work atop the four-hour overload. Run the check before and after remediation when feasible, preserving results and any other changes so improvement is not automatically attributed to testing. Testing detects a defect; it does not itself repair linkage.

Proposed success for this bounded experiment: the check flags the known broken case, produces reviewable relationship evidence, and distinguishes the repaired case without unexplained false passes. Passing a small sample does not demonstrate all production data is correct. At review, adopt for wider validated use if useful, adjust if coverage/noise/runtime is unsuitable, or stop this method if it misses the known defect and test an alternative. No outcome is declared today.

Sol should put EXP-ATT-01 into the control action record with accepted owner, estimate and review date, and start the next retrospective with its measured results. Preserve conflicting perspectives and request technical records before drawing causal conclusions; no individual blame or unsupported “carelessness” finding is made.
