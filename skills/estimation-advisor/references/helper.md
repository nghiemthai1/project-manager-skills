# Three-point helper

Run from the installed skill folder:

```sh
python scripts/estimate.py --demo --format json
python scripts/estimate.py --input estimate.json --format markdown
```

Use `--input -` to read JSON from stdin. Required fields:

```json
{"unit":"person_days","optimistic":2,"most_likely":4,"pessimistic":12}
```

Values are finite nonnegative numbers, with optimistic <= most_likely <= pessimistic. Strings and booleans are rejected as numeric values. Unknown and duplicate fields are rejected. The unit is a nonempty label shared by all three values; the helper performs no conversions.

The output includes the three inputs, triangular mean, PERT mean, and PERT spread heuristic. In the example these are 6, 5, and 1.6666666667. The helper does not calculate confidence intervals or deadline probabilities. Effort does not become duration without capacity and schedule assumptions.

Exit status 0 means a calculation was produced; 2 means invalid input or a read failure. JSON output uses null for unavailable values where relevant; this helper normally has none. Calculation overflow is an error. Results are printed to stdout and no input files are changed.
