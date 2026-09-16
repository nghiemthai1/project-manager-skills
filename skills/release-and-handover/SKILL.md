---
name: release-and-handover
argument-hint: '[cutover plan and service-transfer evidence]'
description: Plan and coordinate authorized release, stabilization and service transfer. Use for software launches
  or IT cutovers with explicit recovery and ownership boundaries.
intent: Coordinate a defined release through readiness, bounded authorization, actual execution, monitored stabilization
  and accepted transfer without gaps in operational responsibility.
type: workflow
theme: transition-and-outcomes
best_for:
  - Coordinate a defined release through readiness, bounded authorization, actual execution, monitored stabilization
    and accepted transfer without gaps in operational responsibility.
scenarios:
  - Coordinate authorized cutover checkpoints, recovery decisions, support transition and accepted operational handover.
estimated_time: Depends on evidence and project scope
frameworks: Cutover checkpoints; recovery limits; service transition; hypercare exit
domain: software-it-project-management
version: 2.1.0
license: MIT
---
# Release and Handover

## Purpose

Carry a defined release through controlled execution and accepted service transfer. Produce an execution sequence, current result log, monitoring/recovery decisions and handover record. A successful deployment command is not proof of a usable stable service, and sending runbooks does not transfer responsibility.

Enter early to prepare a plan even if readiness is incomplete, but live execution requires the actual user authorization and project go decision for its scope. If either is missing, keep the plan draft and recommend the appropriate hold rather than perform an external change.

## Input

Use exact release/version/population/window, readiness record, actual go authority and decision, execution sequence, recovery demonstrations/limits, monitoring, operator roster/access, communications and receiving service owner. Preserve supplied IDs and versions literally. Do not import an example's test, proposed intervention or approval into the current case.

Example: “Prepare the migration cutover and service-transfer workflow from the accepted rehearsal evidence.”

Unknown receiving authority stays unknown; the technical lead is not automatically the service acceptor. A known cutover date can be a target, forecast or approved baseline—use its evidenced state. A recommended hold is not a claimed formal decision. Missing input can still support a useful draft with explicit gates.

## Key Concepts

### Four evidence transitions

Readiness asks whether applicable conditions are satisfied. Go permits defined execution under stated conditions. Execution/monitoring show what actually happened. Handover transfers specified duties through the receiver's acceptance. Different people and dates may govern these transitions. Project closure is another decision afterward.

### Recovery has limits and decision windows

Identify steps that alter data or cause external effects, what can be reversed, what requires restore or forward correction, and when an option stops being viable. A snapshot may recover local state without undoing external messages or transactions. Actual recovery objectives/thresholds must come from the project, not invented defaults.

Put a checkpoint before consequential irreversible work. Record the person authorized to continue, pause or recover, the evidence they inspect and the latest useful decision time. A runbook without tested prerequisites, access and roles is not an executable recovery capability.

### Ownership must cover the whole transition

Confirm immediate monitoring, incident response and recovery coverage before exposure. Enhanced support (often called hypercare) is a defined arrangement with staffing, scope, evidence and exit authority. Full handover may follow stabilization; no period can be ownerless because the project assumes operations has taken over or vice versa.

Prepare handover criteria and documentation before release, but collect post-release results afterward. Do not fabricate stabilization evidence to satisfy an impossible pre-launch checklist.

## Application

### Phase 1 — Establish readiness and authority

**Inputs:** release boundary, applicable gate evidence and decision rights. Review required conditions, exceptions and changed versions. Distinguish recommendation, actual go and user authorization for live actions.

**Outputs:** current readiness/authority record and unresolved blockers. If required evidence is absent, continue planning only; route correction and decision needs.

**Exit:** actual permission and relevant readiness support the defined execution. A sponsor budget or date approval alone cannot satisfy independent acceptance.

### Phase 2 — Prepare executable sequence and coverage

**Inputs:** authorized boundary, environments, operator availability and recovery evidence. For each step identify performer, predecessor/entry condition, action, verification, actual-result field, checkpoint and recovery consequence. Mark assignments proposed until confirmed.

**Outputs:** the [cutover and handover packet](template.md), immediate coverage/escalation roster, communications state and stabilization/transfer criteria. Rehearse consequential coordination where needed; record what the rehearsal actually proves.

**Exit:** operators can access required systems, understand checkpoints and reach decision authorities. No unassigned coverage gap or invented rollback guarantee remains concealed.

### Phase 3 — Execute within the bounded decision

**Inputs:** current go, approved window and ready operators. Execute only authorized actions; drafting a script or checklist is not execution. Record actual time/version/result and deviations as they occur. Inspect the relevant evidence before continuing past checkpoints.

**Outputs:** execution log and actual continue/pause/recovery decisions. If conditions change beyond the decision boundary, obtain the required new decision rather than stretch old permission.

**Exit:** defined execution is verified or recovery/hold is explicitly recorded. Do not report success from the go decision or command exit alone.

### Phase 4 — Stabilize and inspect service behavior

**Inputs:** actual release results, monitoring and agreed support arrangement. Inspect relevant business/technical signals, incidents, reconciliation and operator experience. Use actual thresholds or report them unresolved; no universal error-rate or duration is imposed.

**Outputs:** stabilization evidence, known issues, accepted residual responsibilities and any recovery decision. Distinguish a quiet observation period from proof that unobserved conditions are safe.

**Exit:** agreed transition evidence is met and actual authority accepts the next step. If not, maintain confirmed coverage and decide what changes; do not extend enhanced support indefinitely without owners or funding.

### Phase 5 — Transfer duties and prepare closure

**Inputs:** actual stabilization, usable runbooks/access/training/support routes, residual obligations and receiving-owner criteria. Confirm each transfer's scope and actual acceptance.

**Outputs:** service handover record, accepted residual register, enhanced-support exit decision and closure inputs. Transfer includes who will act, not only where files were sent.

**Exit:** the receiving owner has accepted defined duties and there is no ownership gap. Hand costs, obligations, learning and future benefit review to project closure; a release outcome does not itself close the project.

### When producing a visual

Use the [cutover sequence and transfer gates](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the project source’s evidence and uncertainty in the graphic.

## Examples

Optional worked applications:

- [Relay transition](examples/software.md): pilot, interim coverage, service acceptance and closure are distinct.
- [Northstar cutover](examples/migration.md): current rehearsal evidence precedes go; actual stabilization supports later service transfer.

## Common Pitfalls

- **Go means done:** authorization becomes a completion claim. Record executed result and service verification separately.
- **Rollback fantasy:** snapshots are assumed to reverse external effects. State real limits and the last useful decision point.
- **Handover by email:** documents are sent but nobody accepts duties. Obtain scoped receiver acceptance and retain current coverage until then.
- **Owner gap:** project support stops before operations accepts. Make interim responsibility explicit before rollout.
- **Endless hypercare:** no exit evidence, staffing or authority exists. Define the arrangement and reconsider it at an agreed checkpoint.
- **Old permission stretches:** a material version/window change uses the previous go. Reassess applicability and actual decision scope.

## References

- [Release Readiness](../release-readiness/SKILL.md), [Communication Plan](../communication-plan/SKILL.md) and [Decision Log](../decision-log/SKILL.md) support optional entry and decision records.
- [Organizational Change](../organizational-change/SKILL.md) supports operator adoption; [Project Closure](../project-closure/SKILL.md) receives the final handoff. Use the described artifacts directly when packages are unavailable.
