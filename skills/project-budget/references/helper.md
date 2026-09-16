# Earned value helper

```sh
python scripts/earned_value.py --demo --format json
python scripts/earned_value.py --input evm.json --format markdown
```

Required JSON:

```json
{"currency":"USD","as_of":"2026-10-16","pv":50000,"ev":40000,"ac":48000,"bac":100000}
```

All values are cumulative for one baseline, currency, scope, and status date. The date is ISO YYYY-MM-DD. BAC must be positive; PV, EV, and AC are finite and nonnegative. PV and EV cannot exceed BAC for this model. No currency conversion or reserve release is performed.

- CV = EV - AC; SV = EV - PV, both in the input currency.
- CPI = EV / AC; SPI = EV / PV.
- EAC CPI = BAC / CPI, assuming cost efficiency persists.
- EAC CPI×SPI = AC + (BAC-EV)/(CPI×SPI), applying both efficiencies to remaining work.
- EAC remaining-at-budget = AC + BAC-EV, assuming remaining work earns at its budgeted cost.
- VAC CPI = BAC - EAC CPI.

Zero denominators yield null for affected ratios or forecasts, rendered as Unavailable in Markdown. At zero earned value a CPI forecast is unavailable even if a cost variance exists. SV is not calendar delay; SPI at complete scope is one even if the project finished late. The helper produces indicators, not authorization or an automatically selected management forecast. Currency results are floating-point analytics, not an accounting ledger; round only for presentation.


Use `--input -` for stdin. Unknown fields and duplicate JSON keys are errors. Valid results exit 0; invalid input, unsupported values, numeric overflow, or read failures exit 2 with an explanation on stderr. Output goes to stdout, and input files are never changed. The helper uses Python 3.11+ standard library only and works from any current directory when invoked by its path.
