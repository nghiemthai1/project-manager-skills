# Orion prioritization recommendation

**Use a mandatory-acceptance filter first, then RICE sensitivity analysis for the two optional improvements.** Restore demonstration is required before cutover by signed OR-A. A low reach score cannot remove that requirement.

The requested decision is an order for constrained delivery. Capacity, cutover date, backlog decision authority, dependencies and overall team availability are not supplied. The request gives enough evidence for a provisional order, not a delivery commitment.

## Method and calculations

Treat restore as **Must** under a simple MoSCoW classification; guide search and shortcuts are optional candidates, provisionally **Could**. The owner of backlog order must confirm the discretionary order; changing OR-A would require its actual authorized acceptance/change process, not a score.

For optional candidates use:

**RICE = reach × impact × confidence ÷ effort**

Both optional reach inputs are users/month and effort is person-days. Use impact 1 as supplied, without inventing its scale meaning. Confidence 0.8 or 0.5 is a scoring factor, not a calibrated chance of success. Scores below are comparative monthly reach-weighted values per person-day.

| Candidate | Boundary | Calculation | Interpretation |
|---|---|---|---|
| Restore recovery demonstration | Required by signed OR-A; not eligible for optional elimination | Not included in optional RICE ranking | Reach of 2 administrators lacks the optional items' monthly period and does not capture its acceptance role. Supplied effort 3 person-days still needs capacity and feasibility validation |
| Guide search | Optional | 200 × 1 × 0.8 ÷ 2 = **80** | Higher than the conservative shortcuts case |
| Shortcuts | Optional | 120 × 1 × 0.5 ÷ effort = 60/effort; **30–120** for effort 2–0.5 person-days | Range crosses guide search's score; no stable ranking across the estimate range |

At **0.75 person-days**, shortcuts scores 60/0.75 = **80**, tying guide search. Shortcuts ranks above search below 0.75 person-days, and below search above it. Choosing a midpoint without a basis would conceal this sensitivity.

## Proposed order and next decision
1. **Protect restore demonstration and its prerequisites before cutover.** Assign a qualified owner and confirm capacity, execution evidence and authorized acceptance. Priority does not prove it can finish or mean unrelated optional work cannot run in parallel.
2. **Provisionally place guide search next**, using a conservative comparison against shortcuts' two-day case. This is an explicit conservative choice, not an invariant RICE result.
3. **Place shortcuts after search pending effort clarification.** Ask the people doing the work to narrow the 0.5–2-day range and identify prerequisites; if credible effort is below 0.75 days, consider reversing the optional order.

Do not promise that either optional item fits. Confirm actual capacity after the mandatory work; if it is insufficient, defer optional work. If the mandatory set itself is infeasible, seek a decision on timing/resources through the actual authority instead of dropping restore.

A simple value/effort comparison is the fallback if reach, impact or confidence estimates cannot be justified; it is less numerically precise but exposes weak assumptions. Reassess after effort clarification, changed capacity, dependency discovery or an authorized acceptance change.

**Actual decision:** none recorded. Proposed order only; no OR-A exception, backlog approval, or capacity commitment is established.
