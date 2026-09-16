# RAID Log: software example

Fictional training scenario. Values and thresholds are examples, not defaults for real projects.

## Entries at 16 October

- R-001, risk: interface incompatibility could prevent SSO integration and threaten pilot acceptance. Probability is not supplied; assess with Omar rather than inventing a percentage.
- I-001, issue: the test environment is currently unavailable, preventing planned verification. Omar owns technical remediation; Mina coordinates the consequence.
- DEP-001, dependency: audit interface expected 22 October, needed 20 October, with receiver acceptance outstanding.
- A-001, proposed assumption to validate: the available test environment represents the pilot's identity-provider behavior. Its owner and validation date need confirmation.

## Reasoning

The environment outage is not the same event as potential incompatibility. Keeping them separate stops a repaired environment from being mistaken for proof that the interface is compatible.

## Repair

**Flawed:** "Risk: environment down. Mitigation: hope it returns."

**Corrected:** "I-001 is a current blocker. Record restoration evidence and its delivery impact; retain compatibility as a separate uncertainty."
