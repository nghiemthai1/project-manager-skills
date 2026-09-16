# Estimation Advisor: software example

Fictional training scenario. Values and thresholds are examples, not defaults for real projects.

## Guided decision

**Mina:** "Can we promise the audit integration in four days? We think it is between two and twelve person-days."

**Advisor:** "Is the main uncertainty the interface behavior, the amount of work, or team availability?"

**Mina:** "The interface is changing. For the currently understood work, Omar estimates O=2, M=4, P=12 person-days."

**Advisor:** "Use a three-point effort estimate for that bounded scope, plus an investigation of interface compatibility. Do not promise a duration until capacity and waiting are included."

## Worked result

Triangular mean = (2+4+12)/3 = 6 person-days. PERT mean = (2+16+12)/6 = 5 person-days. PERT spread heuristic = 10/6 = 1.6667 person-days.

The two central estimates differ because PERT gives more weight to the typical scenario. Neither makes the four-day promise credible. Mina records interface stability as an assumption and asks Omar to define the investigation's exit evidence.

## Repair

**Flawed:** "Five days, 95% confidence, guaranteed next week."

**Corrected:** "PERT central effort estimate five person-days for the stated scope; deadline confidence is unmeasured. Validate interface behavior and available capacity before forecasting completion."
