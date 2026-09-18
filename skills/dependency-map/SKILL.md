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
frameworks: Dependency network; interface agreements; local margin; dependency structure matrix; Conway's Law; CPM boundary
domain: software-it-project-management
version: 2.3.0
license: MIT
---
# Dependency Map

## Purpose

Expose what must cross a team or organizational boundary before another party can proceed. Produce a dependency register, a simple network when useful, and actions for late, unusable or unconfirmed handoffs. Use for vendor delivery, internal platform interfaces, approvals, environments and shared-service prerequisites.

A dependency record is a small interface agreement. It should replace “waiting on Platform” with a specific result, provider, receiver, usable condition, dates and next decision. The accompanying renderer turns those records into a provider-to-receiver network, a dependency structure matrix (DSM), an accessible register and portable exports. It does not calculate project finish or CPM float by subtracting two dates.

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

A graph can clarify multiple handoffs, but keep its arrows directional and labeled: **provider → receiver**. Cycles may reveal a real negotiation or iterative exchange that needs staged interfaces; resolve their meaning instead of deleting an inconvenient arrow. Use a table alone when the graph adds no decision value.

### Prioritize without manufacturing precision

Review blocked and failed-verification handoffs first, then negative local gaps, explicit at-risk states, and unresolved provider/date/authority fields. State that ordering as a coordination rule, not a calculated probability or critical path. A dependency can deserve immediate attention even when its effect on the project finish remains unknown.

Use the network to follow chains and cycles. Use the DSM to count repeated provider/receiver seams. Repeated cross-team handoffs can motivate an operating-model discussion under Conway's Law, but a count alone does not prove that organization design caused delay. Use the register for dates, evidence and acceptance detail.

### Treat acceptance as a state transition

Keep `not delivered`, `delivered but unverified`, `verification failed`, `verified but unaccepted`, and `accepted` distinct. Preserve rejected versions and later forecast revisions. Closing an arrow requires the receiver's defined usable condition and actual acceptance evidence, not the provider's completion message.

## Application

1. **Set the boundary.** List material inputs crossing teams, vendors, services or approval bodies. Keep internal task detail in its own plan. Assign stable dependency IDs and identify the consuming activity.
2. **Specify usable delivery.** Record output/version, provider and receiver roles, criteria, verification effort and actual authority. Distinguish known roles from proposed assignments and define missing evidence as an action.
3. **Reconcile timing and status.** Capture needed-by, requested, committed and forecast dates where available, with their sources and as-of dates. Do not replace the provider's forecast with the receiver's wish.
4. **Assess local consequence.** Calculate margin only when units/calendars match. Identify the immediately blocked work and confidence limits. Request integrated schedule analysis before making a final-date claim.
5. **Develop a bounded response.** Compare a smaller usable handoff, staged delivery, validated substitute, resequencing, actual added capacity or escalation. A mock interface is an option only if its limits and replacement validation are explicit; it cannot waive final acceptance.
6. **Choose the decision view.** Use the network for direction, paths and cycles; the DSM for repeated organizational seams; and the register for evidence and dates. Do not force one view to answer all three questions.
7. **Run the control cadence.** Review blocked, negative-gap and unconfirmed handoffs at least at the project's control frequency. Update the record before the meeting, settle changed dates and usable criteria with both sides, and route authority decisions explicitly.
8. **Close and maintain the loop.** Record action owner/status, decision deadline if supported, receiver acceptance and changed forecasts. Preserve rejected deliveries and prior promises. Recheck after scope, interface, resource or calendar changes.

Use [the dependency template](template.md). Each material gap should lead to a decision or evidence request, not only a red arrow. A useful register lets both sides recognize the same deliverable and understand what “done” means.

### When producing a visual

Use the [provider-to-receiver graph](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. Read [dependency graph methods](references/dependency-graph-methods.md) for risk ordering, DSM and CPM boundaries, and [renderer contract](references/renderer.md) before generating files. Preserve the project source’s evidence and uncertainty in the graphic.

Generate a portable example or project view with Python 3.11+:

```sh
python scripts/render_dependency_map.py input.json --output dependency-network
python scripts/render_dependency_map.py --demo --output dependency-network
```

The command writes self-contained HTML, static SVG, normalized JSON and spreadsheet-safe CSV. Use the HTML for graph selection, filters, zoom, a DSM view, persistent evidence details, browser-local dependency editing, visible-row CSV and print/PDF. The editor validates endpoints, dates and commitment evidence; retains cycles for review; recalculates the graph, DSM, register and local metrics; and keeps undoable draft history in that browser. Source exports remain immutable, while separate draft exports disclose their source basis and analysis status.

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
- **Arrow reversal:** drawing receiver-to-provider because the receiver requested the item. The delivery flow is provider → receiver; put requests and escalation in their own fields.
- **Unexplained red:** color implies urgency without the rule or evidence. Show the category text, dates, margin and source, and document the ordering rule.
- **DSM causality:** repeated team-pair cells are treated as proof of organizational failure. Use them to ask where interface design or coordination deserves investigation.
- **False critical path:** a negative handoff margin or long chain is called critical. Require an integrated, method-labeled schedule analysis before displaying CPM results.

## References

- [GAO Schedule Assessment Guide](https://www.gao.gov/products/gao-16-89g): requirements for integrated schedule inference.
- [Dependency graph methods](references/dependency-graph-methods.md), [visual artifact guide](references/visual-artifact.md), and [renderer contract](references/renderer.md): method selection, visual design and portable output.
- [borghei/claude-skills dependency-map](https://github.com/borghei/claude-skills/tree/main/project-management/execution/dependency-map): methodology and left-to-right chart-type reference; this package independently implements its evidence model and renderer.
- [Milestone Schedule](../milestone-schedule/SKILL.md), [RAID Log](../raid-log/SKILL.md), [Escalation Brief](../escalation-brief/SKILL.md): schedule impact, linked controls and authority decisions.
- [Vendor and Procurement](../vendor-procurement/SKILL.md): supplier obligations and acceptance.

If these packages are absent, retain the same provider, receiver, evidence, dates and decision fields in the register.
