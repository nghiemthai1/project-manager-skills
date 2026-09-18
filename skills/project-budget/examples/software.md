# Relay: cost position before the funding decision

Fictional control artifact as of 16 October 2026. D-001 approved B1 on 2 October: BAC 100,000 USD and separately controlled management reserve 10,000. Cumulative PV 50,000, EV 40,000 and AC 48,000 refer to that same baseline and date. The example assumes the supplied EV is maintained under applicable earning rules; the underlying detailed ledger is not reproduced here.

| Indicator / forecast | Calculation | Result | Interpretation |
|---|---|---:|---|
| CV | 40,000−48,000 | −8,000 USD | Earned work cost more than its budgeted value |
| SV | 40,000−50,000 | −10,000 USD | Value behind plan, not days late |
| CPI | 40,000/48,000 | 0.8333 | Current earned value per dollar of actual cost |
| SPI | 40,000/50,000 | 0.8 | Value earned relative to planned value |
| Cost-efficiency EAC | 100,000/0.833333… | 120,000 USD | Current cost efficiency persists |
| Remaining-at-budget EAC | 48,000+100,000−40,000 | 108,000 USD | Remaining work performs at its budgeted cost |
| Combined-efficiency EAC | 48,000+60,000/(0.833333…×0.8) | 138,000 USD | Both efficiencies applied to remaining work |

Run [the aligned input](assets/software-evm.json):

```sh
python scripts/earned_value.py --input examples/assets/software-evm.json --format markdown
```

## Funding and forecast decision

At the 120k scenario, the gap is 20k above BAC and 10k above the original 110k total envelope. Mina needs a current remaining-work estimate and actual obligation reconciliation before recommending management's forecast. Selecting 108k because it fits the envelope would be unjustified unless the remaining-at-budget assumption is supported. No EAC formula establishes the pilot's calendar finish.

On 19 October CR-001 later authorizes B2 of 120k: original 100k performance budget + 10k original reserve released into the revised budget + 10k additional authorization beyond the old total envelope. The exact approved scope includes the optional polish deferral; security acceptance remains. The 16 October report stays against B1 and does not imply those decisions had already occurred.

## Double-counting subcase

Additional fictional ledger illustration: a 20k purchase order includes 8k already within actual cost and 12k still unspent. If an ETC already includes that 12k, adding the whole 20k again would duplicate both incurred and remaining amounts. Reconcile the line items before forecasting; these teaching values are not extra Relay costs to add to the table above.

**Repair:** “Reserve makes 120k authorized” misses the 10k gap beyond the total envelope and the reserve-release decision. Show both bridges and obtain the actual authority.

## Graphical companion

Open the [interactive budget workspace](assets/software.html) to compare forecast assumptions, inspect the category register, review funding options or test a validated browser-local draft.

![Static budget snapshot](assets/software.svg)

[Source JSON](assets/software-source.json) · [normalized JSON](assets/software.json) · [CSV register](assets/software.csv). The narrative remains the accessible decision record; the rendered files preserve its fictional cutoff and authority boundary.
