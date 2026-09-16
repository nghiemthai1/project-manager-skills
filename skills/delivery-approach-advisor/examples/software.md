# Relay: adaptive implementation inside a bounded pilot

Fictional recommendation prepared 29 September 2026, before D-001. The intended pilot includes SAML, audit events, recovery, guidance and reversible rollout; SCIM is excluded. October 30 is a target until Ada approves the baseline. Mina coordinates, Priya is product owner, Omar leads engineering, Lena security and Theo service.

## Context-dump reading

The user has supplied the pilot outcome and distinct acceptance roles. Do not ask them to choose agile versus waterfall. Interface behavior and recovery evidence need early verification; cross-team audit delivery and reviewer availability could constrain progress. Actual user/reviewer cadence, staffing and team Scrum practice are not supplied, so the recommendation cannot promise two-week increments or call the team a Scrum Team by default.

## Numbered recommendation

1. **Preferred: adaptive implementation with controlled pilot gates.** Use small inspectable integrations and recovery rehearsals, while retaining explicit scope, funding and security/service boundaries.
2. **Alternative: predictive emphasis for stable subpackages.** Where interface and criteria are sufficiently known, schedule the bounded work and reviews explicitly; do not force uncertain integration into a falsely detailed plan.
3. **Enabling action:** confirm access to the pilot representatives, platform interface evidence and acceptance reviewers before fixing the feedback cadence.

| Workstream | Proposed practice | Evidence/decision | Boundary |
|---|---|---|---|
| SAML and audit integration | Small integrated slices with receiver feedback | Demonstrated behavior and corrected interface assumptions | Does not add SCIM or new tenants |
| Recovery and reversal | Early rehearsal using applicable configuration | Lena's security evidence and Theo's operational input | Demonstration is not automatic acceptance |
| Pilot planning | Rolling near-term detail plus named dependencies | Current feasible forecast and funding basis | Target is not yet an approved baseline |
| Governance | Versioned scope and actual decision records | Ada's eventual mandate/funding decision and separate acceptances | No approval inferred from kickoff discussion |

## Trial and reassessment

Propose one early integration/recovery evidence cycle before locking the detailed plan. Exact dates and owners for trial tasks must be confirmed. Inspect whether the result was usable, whether a real receiver reviewed it and whether the feedback changed an important assumption. Repeatedly waiting for an unavailable reviewer suggests changing access/cadence, not adding more ceremonies.

**Repair:** “The pilot is fixed-date, therefore every requirement is known” confuses a target with knowledge. Preserve the date objective while planning explicit learning and approval boundaries.
