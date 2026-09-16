---
name: project-governance
argument-hint: '[decision rights and escalation context]'
description: Define project decision rights, tolerances and evidence gates. Use when approval, escalation or acceptance
  responsibilities are unclear.
intent: Create a proportionate governance agreement that separates preparation, authority, assurance and acceptance.
type: component
theme: initiation-and-governance
best_for:
  - Create a proportionate governance agreement that separates preparation, authority, assurance and acceptance.
scenarios:
  - 'Use project-governance: Create a proportionate governance agreement that separates preparation, authority,
    assurance and acceptance.'
estimated_time: Depends on evidence and project scope
frameworks: Stage gates; management by exception; delegated authority
domain: software-it-project-management
version: 2.1.0
---
# Project Governance

## Purpose

Make consequential decisions predictable: who prepares them, who decides, what evidence they need, how long they can wait and what happens when the project exceeds delegated boundaries. Produce an operating agreement and decision-rights table rather than a decorative committee chart.

Use at initiation, after an organizational change, or when repeated delays reveal unclear authority. Small projects may need a one-page agreement; a high-consequence migration may need separate technical, business and operational gates. More meetings do not necessarily provide more control.

## Input

Bring the charter, sponsor mandate, organizational approval rules, existing roles, scope/cost/date baselines, acceptance authorities, supplier interfaces and known decision bottlenecks. Use supplied context directly. Partial input is fine: mark unsupported delegation and tolerance values as unresolved. With no context, ask which decision is currently unclear.

Example: “Clarify who can accept the migration, release reserve and approve a changed cutover date. The vendor keeps treating status meetings as sign-off.” Do not invent numerical tolerances or assign a decision to the most senior person merely because no other authority was supplied.

## Key Concepts

### Separate four kinds of responsibility

Preparation assembles facts and options. Decision authority selects within a mandate. Assurance challenges whether the evidence is adequate. Acceptance confirms a defined result or responsibility transfer. One person may hold several roles, but their boundaries must be explicit; a sponsor's funding approval does not automatically waive security or transfer service ownership.

RACI can show delivery assignments; DACI can clarify an individual decision's Driver, Approver, Contributors and Informed parties. Neither framework creates authority. A signed contract or delegation policy may constrain what a table can say. If two independent authorities must accept different outcomes, create separate decisions rather than forcing them into a single ambiguous A cell.

### Management by exception requires a defined envelope

A tolerance is an authorized boundary within which a role may act without referring the decision upward. Define the dimension, baseline, measurement method, threshold, who delegates it and exceptions. Cost, scope, schedule, quality, risk and benefits may have different boundaries. A sample “10%” threshold is not organizational policy.

Escalate a credible forecast breach before an actual breach makes the decision useless. Distinguish a reporting alert from permission to spend or change scope. If no tolerance is supplied, identify the actual decision route and mark delegation unknown; do not halt ordinary drafting while waiting for a governance document.

### Gates are evidence decisions

A gate should answer a bounded question such as whether a specified population may enter production. State the evidence, reviewer, decision maker, conditions and next action for go, hold or rework. A calendar event is a review opportunity, not an automatic pass. Conditional approval must name its condition, owner, deadline and whether execution may start before closure.

## Application

1. **Inventory real decisions.** Start from funding, scope, dates, acceptance, release, risk exceptions, procurement and closure. Include only decisions material to this project. Capture known authority sources and unresolved overlaps.
2. **Design the operating model.** Map preparation, decision, assurance and acceptance separately. Give each decision a bounded owner or an explicit unresolved authority. Identify deputies only when their delegation is evidenced, not merely because they attend the meeting.
3. **Define escalation and tolerances.** For each dimension record what can be handled locally, what must be referred and when. Include a route for urgent unavailable decision makers using actual policies; silence is not approval.
4. **Specify gates and forums.** Define inputs, quorum or required participation if applicable, decision deadlines, output records and hold/rework branches. Use asynchronous decisions where evidence and authority permit; a standing meeting should earn its time.
5. **Walk a disputed case through the design.** Try a forecast budget overrun, failed restore or supplier scope claim. Check that the design produces a timely route without allowing one authority to override another's remit. Resolve contradictions before calling it agreed.
6. **Record and maintain the agreement.** Preserve the approving record, effective version and unresolved items. Link actual decisions to the decision log, assignments to RACI, and controls to status/escalation. Review after mandate, personnel or risk changes.

Use [the governance template](template.md). Quality means a reader can answer who may decide this particular issue, on what evidence, by when and with which limits. A role name without a source or boundary is insufficient.

### When producing a visual

Use the [decision-rights flow](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay approval and acceptance](examples/software.md): sponsor funding, security evidence and service acceptance remain separate.
- [Northstar cutover authority](examples/migration.md): a failed restore holds the gate despite an approved new date and budget.

## Common Pitfalls

- **Sponsor approves everything:** independent assurance disappears under a single escalation route. Retain the actual security, business and service authorities and distinguish their decisions.
- **Meeting attendance becomes consent:** an attendee is assigned duties or recorded as approving without evidence. Record the explicit decision and conditions; attendance belongs in attendance records.
- **Tolerance by habit:** a remembered percentage is treated as policy. Obtain the applicable delegated boundary and identify its baseline and units.
- **Gate by calendar:** a planned go-live becomes an automatic go decision. Recheck current applicable evidence at the gate and retain hold authority.
- **Committee without a decision owner:** debate continues while the last useful decision time passes. Name the actual decider and escalation route; use a committee only where the mandate requires one.

## References

- [RACI Matrix](../raci-matrix/SKILL.md): delivery assignments and row/column audits.
- [Decision Log](../decision-log/SKILL.md): exact decisions, conditions and authority.
- [Escalation Brief](../escalation-brief/SKILL.md): exception decisions with timing and alternatives.
- [GovS 002 Project Delivery](https://www.gov.uk/government/publications/project-delivery-functional-standard): a governance reference, not an assertion that this project falls under UK government rules.

Use the required artifacts directly if adjacent skills are unavailable. Draft governance does not replace the organization's actual delegation.
