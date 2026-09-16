---
name: dependency-map
argument-hint: '[handoffs, providers, receivers, and dates]'
description: Define cross-team handoffs, usable acceptance and timing gaps. Use when external deliverables, approvals
  or shared services may block project work.
intent: Make provider-to-receiver dependencies actionable with evidence, dates, acceptance and an explicit decision
  route.
type: component
theme: controls-and-assurance
best_for:
  - Make provider-to-receiver dependencies actionable with evidence, dates, acceptance and an explicit decision
    route.
scenarios:
  - Map cross-team handoffs with provider, receiver, needed-by date, expected delivery and acceptance evidence.
estimated_time: Depends on evidence and project scope
frameworks: Dependency network; interface agreements; local margin versus float
domain: software-it-project-management
version: 2.1.0
---
# Dependency Map

## Purpose

Expose what must cross a team or organizational boundary before another party can proceed. Produce a dependency register, a simple network when useful, and actions for late, unusable or unconfirmed handoffs. Use for vendor delivery, internal platform interfaces, approvals, environments and shared-service prerequisites.

A dependency record is a small interface agreement. It should replace “waiting on Platform” with a specific result, provider, receiver, usable condition, dates and next decision. It does not calculate project finish or CPM float by subtracting two dates.

## Input

Bring the workstreams, exchanged deliverables/decisions, providers, receiving work, acceptance criteria, needed-by dates, expected delivery, confirmation evidence and known schedule links. Use supplied facts directly. With no detail, ask what input the blocked work needs; with one-sided information, draft the record and mark the other side unconfirmed.

Example: “Platform forecasts the audit interface for 22 October, but integration needs it on 20 October. Define the handoff and next actions.” A requested date is not a provider commitment; a provider forecast is not automatically receiver acceptance.

## Key Concepts

### Define the usable handoff

A delivery label such as “API ready” can mean code complete to the provider and a tested, documented, accessible interface to the receiver. Resolve that semantic gap before relying on the date. State version/scope, access, format, evidence and correction expectations proportionately. Separate provider completion, delivery, receiver verification and acceptance.

Identify contacts and actual responsibility boundaries. A vendor contact may coordinate without authority to bind a contract; a PM may coordinate without accepting technical correctness. Mark proposed receiving assignments and authority gaps explicitly. Do not name an engineer as acceptor solely because they appear downstream on a chart.

### Dates answer different questions

| Date or state | Meaning |
|---|---|
| Needed-by | Receiver's required input timing and its schedule basis |
| Requested | Date asked of the provider, not yet agreed |
| Committed | An evidenced undertaking within the provider's authority, with conditions |
| Expected/forecast | Current predicted delivery, with as-of date and basis |
| Accepted | Actual receiver decision for the defined handoff; may occur after delivery |

Needed-by must allow applicable validation and review before consuming work starts. If the date means “delivered for validation” rather than “accepted usable input,” say so. Otherwise a nominal on-time file arrival can still block the downstream activity.

### Local margin is not total float

For comparable dates on a stated calendar, `local delivery margin = needed-by − expected delivery`. A negative value identifies a gap. If 20 October is needed and 22 October expected, the margin is −2 calendar days. This does not establish project delay, criticality or total float. Those require the integrated network, calendars, constraints and remaining work.

A graph can clarify multiple handoffs, but keep its arrows directional and labeled. Cycles may reveal a real negotiation or iterative exchange that needs staged interfaces; resolve their meaning instead of deleting an inconvenient arrow. Use a table alone when the graph adds no decision value.

## Application

1. **Set the boundary.** List material inputs crossing teams, vendors, services or approval bodies. Keep internal task detail in its own plan. Assign stable dependency IDs and identify the consuming activity.
2. **Specify usable delivery.** Record output/version, provider and receiver roles, criteria, verification effort and actual authority. Distinguish known roles from proposed assignments and define missing evidence as an action.
3. **Reconcile timing and status.** Capture needed-by, requested, committed and forecast dates where available, with their sources and as-of dates. Do not replace the provider's forecast with the receiver's wish.
4. **Assess local consequence.** Calculate margin only when units/calendars match. Identify the immediately blocked work and confidence limits. Request integrated schedule analysis before making a final-date claim.
5. **Develop a bounded response.** Compare a smaller usable handoff, staged delivery, validated substitute, resequencing, actual added capacity or escalation. A mock interface is an option only if its limits and replacement validation are explicit; it cannot waive final acceptance.
6. **Close and maintain the loop.** Record action owner/status, decision deadline if supported, receiver acceptance and changed forecasts. Preserve rejected deliveries and prior promises. Recheck after scope, interface, resource or calendar changes.

Use [the dependency template](template.md). Each material gap should lead to a decision or evidence request, not only a red arrow. A useful register lets both sides recognize the same deliverable and understand what “done” means.

### When producing a visual

Use the [provider-to-receiver graph](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the project source’s evidence and uncertainty in the graphic.

## Examples

Optional worked applications:

- [Relay audit handoff](examples/software.md): a two-day local gap, incomplete confirmation and options that preserve final validation.
- [Northstar mapping and export](examples/migration.md): late mapping, a later actual linkage defect and receiver acceptance remain distinct.

## Common Pitfalls

- **Ownerless arrow:** a broad team name has no accountable contact or receiver. Identify the boundary owners or expose the unresolved assignment.
- **Delivered but unusable:** a sent file is treated as acceptance. Define the receiver's usable condition and retain validation time.
- **Float by subtraction:** local margin is reported as project critical-path delay. Keep the local calculation and request complete schedule analysis.
- **Stale agreement:** a promise survives a changed interface or scope. Reconfirm the changed boundary and retain the old record.
- **Mock becomes final evidence:** a temporary substitute is accepted as proof of the real integration. State its limits and required later verification.
- **Diagram overload:** hundreds of internal tasks hide the external decisions. Map only relevant boundaries and keep detail elsewhere.

## References

- [GAO Schedule Assessment Guide](https://www.gao.gov/products/gao-16-89g): requirements for integrated schedule inference.
- [Milestone Schedule](../milestone-schedule/SKILL.md), [RAID Log](../raid-log/SKILL.md), [Escalation Brief](../escalation-brief/SKILL.md): schedule impact, linked controls and authority decisions.
- [Vendor and Procurement](../vendor-procurement/SKILL.md): supplier obligations and acceptance.

If these packages are absent, retain the same provider, receiver, evidence, dates and decision fields in the register.
