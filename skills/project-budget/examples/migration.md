# Northstar: low spending with adverse earned performance

Fictional control artifact as of 23 October 2026. M-D001 approved B1: BAC 240k USD plus separate management reserve 24k. Cumulative PV=80k, EV=60k, AC=75k. The data are aligned to the same baseline/date; detailed earning records and supplier obligations still need inspection for an operational decision.

| Measure / scenario | Result | Meaning |
|---|---:|---|
| CV = 60−75 | −15k USD | Cost exceeds budgeted value earned |
| SV = 60−80 | −20k USD | Value behind plan; no calendar delay implied |
| CPI / SPI | 0.8 / 0.75 | Cost and value-progress ratios |
| EAC if CPI persists | 240/0.8 = 300k | Historical cost-efficiency scenario |
| EAC remaining at budget | 75+(240−60) = 255k | Remaining scope assumes budgeted performance |
| EAC with CPI×SPI | 75+180/(0.8×0.75) = 375k | Stronger combined-efficiency scenario, not selected by default |

Run [the source input](../assets/migration-evm.json):

```sh
python scripts/earned_value.py --input assets/migration-evm.json --format markdown
```

AC/BAC = 31.25% measures cost incurred relative to budget, not completion or health. Only 60k of budgeted work has been earned for 75k spent. The scenario range is a reason to inspect remaining data remediation, vendor obligations, rehearsal and transition effort rather than pick whichever value fits the funding available.

## Funding bridge and later decision

At EAC 300k, the gap to BAC is 60k and to the 264k total envelope is 36k. Access to reserve remains separately controlled. Jules should prepare the current ETC, cost-category reconciliation and feasible scope/date alternatives for Noel. On 23 October there is no authorization to treat 300k as the baseline.

M-CR02 on 9 November later authorizes phased scope, 28 November cutover and B2 300k with funding resolved: original 240k + 24k reserve + 36k additional authority. Preserve the earlier report and actual approval conditions. The later restore failure still affects readiness; budget authorization does not waive it.

## Decision and repair

A bottom-up forecast may differ from every ratio scenario if remaining work has different economics. Explain that evidence and reconcile unspent commitments once; do not call a statistical ratio the only correct answer.

**Repair:** “Only 31.25% spent, so budget is healthy” becomes “current efficiency implies a material possible overrun; reconcile the remaining estimate and obtain funding/scope decisions while preserving B1 history.”
