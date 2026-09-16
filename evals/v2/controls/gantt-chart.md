# Fictional Atlas dated Gantt

Planning scenario v0.1, prepared 2026-09-16; a separate project status date is not supplied. Calendar: Monday-Friday, no holidays. Start 2026-10-05 at start-of-day. All dates below are local date boundaries; timezone and hours per day are not supplied and are not needed for this day-level illustration. Finish is exclusive: Monday-start two-working-day A occupies Monday/Tuesday and ends at Wednesday's start. Successors use the next available working start boundary. E is a zero-duration milestone.

**Executive explanation:** the approved comparison milestone remains October 14 at start-of-day under AT-1. Fin cannot work full time on B and C simultaneously. Sequencing B then C yields E at the start of October 19: three working days, or five calendar days, later than the approved comparison. This scenario is feasible for the stated specialist constraint; it does not establish all other staffing or acceptance requirements. No revised baseline or change approval exists. A green/on-time report and overlapping Fin bars would conceal the known conflict.

| ID | Duration | Technical predecessors | Resource condition | Proposed start | Exclusive finish | Occupied working dates | Approved comparison |
|---|---:|---|---|---|---|---|---|
| A | 2 working days | None | Owner unknown | Oct 5 | Oct 7 | Oct 5,6 | Task baseline unknown |
| B | 4 working days | A | Fin full time | Oct 7 | Oct 13 | Oct 7,8,9,12 | Task baseline unknown |
| C | 3 working days | A | Fin full time; proposed after B | Oct 13 | Oct 16 | Oct 13,14,15 | Task baseline unknown |
| D | 1 working day | B,C | Owner unknown | Oct 16 | Oct 19 | Oct 16 | Task baseline unknown |
| E | 0 | D | Event; authority/criterion unknown | Oct 19 | Oct 19 | None | Oct 14 start-of-day, AT-1 |

Dates are 2026. The CSV preserves full ISO dates, original dependencies, added resource ordering, unknown task baselines and absent actual evidence. B-before-C is a proposed resource sequence, not a claimed original technical dependency. C-before-B would also finish October 19 under these assumptions; no supplied fact favors one, so B-first is a stated scheduling choice.

The dependency-only parallel calculation would occupy B Oct7-13 and C Oct7-12, D Oct13-14, E Oct14. It explains why the approved date appears attainable in an unconstrained chart, but would require two full-time Fin assignments during the overlap. It is not the proposed feasible chart. Original dependency duration is 7 working days; the single-specialist serial sequence requires 10. No complete approved task schedule was provided, so the approved comparison is drawn only as the supplied milestone.

Editable chart source: atlas-gantt.mmd. Static preview: atlas-gantt.png. The image is a locally drawn calendar fallback from the same dated table, not a rendered Mermaid output. Neither chart uses green, active, done or percent-complete labels because no actual progress or RAG criteria were supplied. No critical coloring is used; the technical and resource-constrained models differ.

## Decisions and remaining evidence

Adopt the sequential scenario for further planning only after confirming Fin's uninterrupted availability on these dates and owners/availability for A and D. If October14 must be retained, investigate genuinely available qualified second capacity to permit overlap, or authorized reductions in work/duration supported by estimates. Neither capacity nor reduced effort is supplied; do not depict either as approved. Otherwise submit the evidenced October19 forecast and its consequences to the actual change authority. The AT-1 approver's identity and decision deadline are unknown.

The toy task labels have no supplied deliverable meanings or acceptance criteria. E's milestone criterion and actual authority need definition before a real commitment. Calendars explicitly exclude holidays for this fictional case; no outside holiday assumptions were imported. Actual start/finish and percent complete remain unknown, not inferred from dates or set to zero. No external scheduling or project update occurred.

## Review of presentation

Compare the separate AT-1 and E milestone rows at Oct14 and Oct19; working dates are listed explicitly above to make weekend treatment auditable. A/B/C/D dates match the CSV and editable Mermaid source. No mmdc executable was available on PATH, so Mermaid renderer-specific parsing, milestone positioning and browser layout remain unverified. The local static preview provides a checked fallback; it does not claim Mermaid validation. Retain both source and this limitation when exporting with a future renderer.
