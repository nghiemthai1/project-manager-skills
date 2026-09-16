---
name: resource-capacity-plan
description: Compare complete demand with realistic availability, skills and timing. Use when staffing, competing
  assignments or a shared specialist may make a plan infeasible.
metadata:
  type: component
  domain: software-it-project-management
  version: 2.1.0
  intent: Expose person-level capacity constraints and develop explicit allocation, scope or sequence options without
    assuming interchangeable people.
  frameworks: Capacity-demand analysis; skill constraints; resource leveling options
  best_for: '["Expose person-level capacity constraints and develop explicit allocation, scope or sequence options
    without assuming interchangeable people."]'
  scenarios: '["Check next weeks assignments against each persons available hours, leave, support load and specialist
    constraints."]'
  estimated_time: Depends on evidence and project scope
---
# Resource Capacity Plan

## Purpose

Determine whether the proposed work can be staffed within a stated period and identify the real decisions when it cannot. Produce an availability/demand table, skill and timing checks, feasible options and allocation status. Use for sprint preparation, rehearsal planning, shared specialists or cross-project coordination.

The artifact proposes or records assignments; it does not grant authority over another manager's staff. Team headcount and aggregate spare hours cannot establish that the required person is available at the needed time with the needed skill.

## Input

Bring a common planning period, people or defined roles, gross hours, leave, non-project overhead, all assignments, effort estimates, skill needs and timing constraints. Reuse supplied context. Partial input supports a qualified draft; if nothing is supplied, ask which work and period need a feasibility decision. Missing other-project allocations remain unknown, not zero.

Example: “Can Omar support the pilot while retaining the support rotation? Check both his hours and the integration window.” Use hour-based analysis when effort inputs are meaningful; empirical team flow may be a better forecast when detailed individual allocations would be speculative.

## Key Concepts

### Reconcile the arithmetic before interpreting it

For one person and period, modeled availability = gross hours − leave − overhead. Demand is the sum of all included allocations; remaining = availability − demand. Overload is the positive part of demand − availability. Every category appears once: operational support can be a deduction or an allocation, but not both. State which convention is used.

Load percentage is demand/availability when availability is positive. Zero availability means the ratio is unavailable, not automatically zero; positive demand then represents an obvious shortage. The [offline helper](scripts/capacity.py) enforces finite nonnegative inputs and reports individual overload even when the team has spare hours. Read [its contract](references/helper.md); it cannot discover omitted assignments or infer skills and daily calendars.

### Capacity has skill, timing and uncertainty

| Check | What the arithmetic alone misses |
|---|---|
| Skill fit | Spare security hours do not automatically perform integration engineering |
| Timing | Two tasks may need the same specialist during the same four-hour window despite fitting the weekly total |
| Prerequisites | Access, environment or a provider handoff can make nominal hours unusable |
| Onboarding | New capacity may consume supervision and require time before productive work |
| Unplanned demand | Support interruptions need an evidenced allowance or scenario; no universal utilization percentage is assumed |
| Completeness | Missing cross-project work can make a positive balance misleading |

Separate known availability, estimated demand and proposed allocation. An estimate from an agent is not a team commitment. Do not convert story points to hours using a universal exchange rate, or compare teams using point velocity as productivity.

### Resolve constraints through explicit options

Resource leveling changes the sequence to respect availability and may move finish. Resource smoothing tries to resolve peaks within available schedule flexibility; it requires the actual network and does not create float. Adding capacity works only if the skill, start, access and supervision are real. Overtime, deferral and reassignment have costs and authorities; none should appear as a silent arithmetic fix.

A scenario can be useful before confirmation. Label it, state what must be agreed and retain the current case alongside it. If data are incomplete, report “feasible under these assumptions” or an unresolved constraint rather than an unconditional staffing verdict.

## Application

1. **Define period and completeness.** Align dates, hours conventions and scope. Inventory all relevant assignments and the source/as-of of availability. Mark missing allocations and role vacancies explicitly.
2. **Build the baseline comparison.** Separate gross hours, leave, overhead and demand. Reconcile duplicate categories and include review, integration, transition and support where required by the scope.
3. **Calculate and inspect each person.** Use the helper for supported hourly inputs, then examine overloads and unknowns. Aggregate totals summarize but cannot cancel an individual's constraint.
4. **Test skill and calendar feasibility.** Map critical skills to timed work, check intra-period peaks and prerequisites, and include onboarding/supervision. Cross-check the schedule rather than treating every remaining hour as fungible.
5. **Compare options.** Show the amount and timing of demand to defer, resequence, reassign or resource. State scope/date/quality/cost effects, actual approving roles and the evidence required for each option. Preserve mandatory acceptance work.
6. **Record and refresh.** Keep proposed and confirmed allocations separate. Recalculate confirmed changes or label a what-if. Feed the accepted availability/constraints to scheduling and review when scope, leave, support load or commitments change.

Use [the capacity template](template.md). Quality means the reader can find the constrained skill/person/time, understand the demand basis and identify the decision that could resolve it. A polished utilization chart is not enough.

### When producing a visual

Use the [per-person demand versus availability](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay staffing comparison](examples/software.md): aggregate spare hours conceal Omar's overload; includes runnable input.
- [Northstar rehearsal capacity](examples/migration.md): a support reassignment is a conditional option, not free vendor capacity.

## Common Pitfalls

- **100% before interruption:** gross hours are all committed while leave/support are ignored. Use evidenced deductions or expose the uncertainty.
- **Double haircut:** the same support duty reduces availability and appears in demand. Reconcile categories once before acting on the result.
- **Fungible people:** spare hours from an unrelated skill erase a bottleneck. Check capability and actual timing.
- **Nominal staffing:** a new hire or vendor is productive immediately on paper. Confirm start, access, competence and supervision cost.
- **False certainty from blank data:** absent allocations are entered as zero. Retain unknowns and qualify feasibility.
- **Accepted by spreadsheet:** a balanced scenario is reported as staffed. Obtain the actual resource decision before updating the committed plan.

## References

- [Scrum Guide](https://scrumguides.org/scrum-guide.html): team forecasting and accountabilities where Scrum applies.
- [Milestone Schedule](../milestone-schedule/SKILL.md), [Sprint Planning](../sprint-planning/SKILL.md), [Project Recovery Advisor](../project-recovery-advisor/SKILL.md): sequence, forecast and respond to constraints.

These packages are optional; retain the period, hours, skill/timing checks and assignment status when using the template alone.
