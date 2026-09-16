# Relay: asymmetric effort scenarios

Fictional instructional estimate for one bounded integration package, not Relay's full delivery forecast. Assume the same completion rule across scenarios: implementation, review, applicable integration tests and correction of the modeled interface issues. The values are teaching inputs: O=2, M=4, P=12 person-days. Contributor confirmation and actual scheduling availability are not supplied.

| Scenario | Effort | Assumed condition |
|---|---:|---|
| Optimistic | 2 person-days | Stable compatible interface and available test environment |
| Most likely | 4 | Ordinary integration adjustment and review |
| Pessimistic modeled case | 12 | Bounded compatibility rework and repeated testing; catastrophic outages excluded |

## Method and calculation

Three-point estimation is useful because the task boundary is fixed while implementation conditions vary. Triangular mean = (2+4+12)/3 = 6 person-days. PERT mean = (2+4×4+12)/6 = 5. Spread convention = (12−2)/6 ≈ 1.67. The PERT estimate gives more weight to the typical case, so it is lower than the equal-weight mean for these asymmetric inputs.

Neither 5 ± 2×1.67 nor the 2–12 scenario range is an evidenced 95% confidence interval. The inputs do not supply a probability model, validated distribution or deadline probability. The local helper reproduces the three values and conventions; it does not approve or choose one as management's commitment.

## Recommendation and planning handoff

1. Use the PERT convention only if the contributors agree that its weighting suits the planning purpose; otherwise report the scenarios and the alternative mean transparently.
2. Investigate interface compatibility and environment availability because they drive the adverse case. At the canonical 16 October control point, R-001 and I-001 distinguish a possible incompatibility from an actually unavailable environment; do not merge them.
3. Pass person-day effort and waiting assumptions to the real capacity/schedule model. Omar's availability, predecessor readiness and acceptance reviews determine elapsed dates. Do not turn “five person-days” into a promise to finish in one calendar week.

Re-estimate when the interface is confirmed, the environment becomes available, scope changes or early execution provides better actual evidence. The October 30 baseline remains a separate project commitment until an authorized change; this toy task does not compute its finish.

**Repair:** “The helper says five days with 95% confidence” becomes “PERT mean five person-days under stated scenarios; confidence probability and calendar finish are not established.”
