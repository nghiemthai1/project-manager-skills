# Beacon delivery approach — proposed operating agreement

**Recommend rolling-wave hybrid planning with short technical learning cycles, monthly user validation and a controlled recovery/security gate.** The end-quarter date is a sponsor-requested target, not an approved baseline. A deadline cannot make uncertain data quality or changing vendor formats stable.

No as-of date, exact quarter-end date, named decision authorities or confirmed specialist allocation was supplied. This recommendation is not an agreed team commitment.

| Dimension | Evidence | Consequence |
|---|---|---|
| Technical uncertainty | Data quality uncertain | Start with bounded profiling and migration trials; do not freeze speculative detail |
| Interfaces | Vendor format updates weekly | Version inputs, inspect each change and assess compatibility before planning dependent work |
| Feedback | Users available once per month | Distinguish technical evidence available sooner from business validation that waits for monthly access |
| Capacity | One shared specialist; capacity unconfirmed | Confirm allocation and queues before promising any cycle's scope |
| Governance | Recovery/security gate required; no approved date baseline | Preserve gate evidence and authority separately from sponsor timing preference |

## Alternatives
1. **Preferred hybrid:** adaptive data/interface investigation with explicit vendor handoffs and release gates. It fits the two different feedback speeds and protects acceptance.
2. **Predictive emphasis:** useful later for a stable cutover sequence, but a detailed fixed plan now would be vulnerable to weekly format changes and unknown data conditions.
3. **Adaptive emphasis alone:** frequent technical increments can help, but two-week ceremonies cannot create unavailable user feedback or specialist capacity. A Scrum declaration is unsupported without its actual roles, usable increments and operating capability.
4. **Bounded investigation first:** use within the preferred approach to establish whether representative data and vendor changes can be handled and what remains blocked.

## Proposed practices
| Workstream | Planning horizon / practice | Inspectable output and feedback | Proposed owner / authority | Controlled boundary and exit evidence |
|---|---|---|---|---|
| Data quality and migration behavior | Detail only the next feasible technical cycle; later work by outcomes and uncertainties | Versioned sample, profiling findings, migration results, exceptions and repeatable checks | Technical lead unassigned; specialist contributes only within confirmed allocation | Do not infer all-data correctness from a sample; agree coverage and completion criteria |
| Vendor interface | Review weekly format changes; track usable-version expectations and impact | Version comparison, compatibility results and acknowledged provider/receiver handoff | Vendor contact and receiver authority unassigned | No assumed format freeze; accept an input version only with relevant checks |
| User workflow validation | Prepare a coherent slice and questions for each actual monthly user window | Observed task results and explicit business feedback | User representative/acceptance authority unconfirmed | Technical testing does not substitute for business acceptance; exact review date to secure |
| Recovery/security | Collect evidence incrementally and maintain a gate pack | Applicable recovery demonstration and required security evidence | Gate owners/decider must be identified | Gate cannot be waived by choosing an iteration cadence or reaching quarter-end |
| Integrated coordination | Update near-term allocation/dependencies after vendor changes and learning | Feasible work queue, unresolved waits and a forecast with assumptions | PM/coordinator and delegated authority unconfirmed | Target remains distinct from forecast and any later approved baseline |

## Early trial
**Propose one bounded representative migration slice spanning a current vendor format and one subsequent weekly update**, followed by review at the next available monthly user window. This defines the learning boundary, not a guaranteed two-week duration. Confirm sample access, specialist allocation, effort/time cap and review dates before starting.

A proposed technical lead should produce:
- sampled data-quality findings, repeatable migration/linkage checks and recorded exceptions;
- evidence of what changes when the vendor updates its format, including rework and specialist demand;
- a usable workflow slice with questions for users;
- initial recovery/security evidence gaps for the relevant reviewers.

Measure technical learning, rework, specialist effort/queue time and unresolved user-dependent questions. Exit with findings and a credible next planning decision, not an asserted complete migration or stable scope.

Revisit the approach if changes repeatedly invalidate increments, technical work accumulates awaiting users, or specialist queues dominate elapsed time. Options include negotiating vendor stability windows or delegated user feedback, but neither is available until confirmed. If trial evidence and confirmed capacity cannot support the end-quarter target, present scope/date/resource alternatives to the actual authority.

**Next decision:** confirm the specialist's usable allocation and the next monthly user slot, name the acceptance/governance owners, and agree the trial limit. Hand this practice table and resulting evidence into integrated planning. Fixed two-week delivery commitments remain unsupported.
