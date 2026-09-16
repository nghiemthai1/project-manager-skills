# Northstar: prove usable records, not just equal counts

Fictional artifact as of 6 November 2026. Rehearsal confirms lost attachment links, M-I002, related to earlier risk M-R01. B1 acceptance requires reconciliation of the agreed population, no unexplained high-severity mismatches, demonstrated restore and support-owner acceptance.

| Quality dimension | Method and evidence | Failure implication | Owner / authority boundary |
|---|---|---|---|
| Population coverage | Reconcile agreed source/target population with documented exclusions | Missing/extra records need explanation and disposition | Chen prepares evidence; Saira accepts business outcome |
| Identity and relationships | Check stable IDs and attachment-to-ticket associations, including known failure cases | Equal counts can coexist with broken links | Repair ownership must be confirmed with Beck and technical team |
| Permissions and usable workflow | Exercise representative authorized/unauthorized access and user journeys | Correct data may still be unusable or exposed incorrectly | Business/security authorities as actually defined; do not invent sign-off |
| Restore | Execute recovery using applicable data/configuration and record observed result | An unproven restore cannot satisfy the gate | Rosa requires restore evidence before service responsibility |
| Support readiness | Observe operator use of monitoring, runbooks and escalation | Training attendance alone does not prove capability | Rosa's service acceptance is separate from data delivery |

## Issue-to-retest path

Preserve the export version, failing IDs, observed broken relationships and expected behavior. Define the correction and affected regression scope before accepting a repaired sample. Repeat the failed cases and inspect whether the cause affects other attachment patterns or permission combinations. A sample chosen only because it is easy cannot establish correctness across the population. If full checking is infeasible, document the sample design, coverage gaps and actual acceptance authority for any residual uncertainty.

## Proposed process improvement

Add a supplier/receiver mapping review before the next rehearsal, including relationship invariants and expected failure handling. This is a proposal, not a claim that a meeting already occurred or that Beck accepted a new obligation. Inspect whether the next rehearsal reproduces the specific linkage failure and whether new defects appear; retain the earlier failed result in history.

**Decision:** the current export has an evidenced issue. No later successful rehearsal or acceptance is assumed as of 6 November. A status update should distinguish planned correction, delivered correction, successful retest and authorized acceptance.

**Repair:** “Source count equals target count; accept migration” proves too little. Add relationship, permission, workflow and recovery evidence tied to the actual acceptance boundary.
