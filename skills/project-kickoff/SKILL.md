---
name: project-kickoff
argument-hint: '[project context and kickoff goals]'
description: Establish mandate, decision rights and a usable working agreement. Use when starting or resetting a
  software or IT project.
intent: Turn a mandate and unresolved planning questions into explicit working agreements, decision records and
  an owned planning handoff.
type: workflow
theme: initiation-and-governance
best_for:
  - Turn a mandate and unresolved planning questions into explicit working agreements, decision records and an owned
    planning handoff.
scenarios:
  - Prepare and run the launch workshop for the project team, then capture working agreements, open decisions and
    actions.
estimated_time: Depends on evidence and project scope
frameworks: Kickoff facilitation; RACI; decision/action separation
domain: software-it-project-management
version: 2.0.0
license: MIT
---
# Project Kickoff

## Purpose

Make the project understandable enough for people to start the right work and recognize decisions they cannot make. A useful kickoff exposes conflicts between the requested outcome, authority, acceptance, capacity and timing. It ends with a working agreement and a planning handoff, even when some questions remain unresolved.

Use it at initiation or after a material reset. A routine status meeting belongs in the control cycle. A disputed technical design may need its own workshop. Do not expand the kickoff until everyone has solved the project.

## Input

Use the mandate or charter, current approval records, scope boundary, affected groups, delivery approach, proposed participants, capacity assumptions and known dependencies. Ask for the decision the session must enable, not a full slide deck. Preserve a requested date as a target unless its approval is evidenced.

Example: “Prepare Northstar's kickoff after charter approval; the supplier handoff and service responsibilities remain unclear.”

Missing mandate, participants or availability need not prevent a draft. Label the session planning/alignment when execution authority is pending. Do not invent an attendee list, consent, resource allocation or meeting booking. Preparing an agenda does not send invitations.

## Key Concepts

### Working agreements connect behavior to evidence

“Communicate openly” is difficult to inspect. “The provider supplies a versioned mapping; the receiver validates its usable condition before the consuming task starts” gives the team a testable agreement. Cover how work enters, how it is accepted, how constraints become visible, and how decisions reach the right authority.

An agreement can be proposed, confirmed, disputed or pending an absent authority. Record that status per item. One participant's silence cannot confirm everyone else's agreement.

### RACI clarifies work; decision rights authorize choices

Use RACI for specific deliverables, then name the separate authorities for scope/funding, business acceptance, security, service transfer and release where relevant. A sponsor's funding decision does not replace technical acceptance. A PM coordinating the kickoff does not gain all approval rights. In Scrum, preserve the Product Owner's backlog accountability and Developers' planning responsibility.

### Read-back reveals false alignment

Ask people to test a consequential scenario: “If recovery evidence fails the day before release, who decides what, and where is that recorded?” This is more useful than asking whether everyone agrees. A contradiction is an output to resolve, not a reason to record fictional consensus.

Scale the session to uncertainty. Stable repeat delivery may need an asynchronous agreement review and a short decision session. Multiple organizations, unclear authority or contested scope usually need facilitated discussion. Neither format changes the approval boundary.

## Application

### Phase 1 — Prepare the decision boundary

**Inputs:** mandate, approval history, affected groups and known conflicts. Distinguish settled decisions from proposals. Identify the people who can supply evidence, perform work and make the required decisions; mark missing representation. Choose asynchronous preparation or a focused session based on the conflicts.

**Output:** a short pre-read and agenda where each topic has a question, needed evidence and intended result. A sample sequence is outcome/scope, authority/acceptance, delivery/dependencies, then read-back. Any timeboxes are proposed facilitation limits, not project estimates.

**Exit:** the facilitator can explain what the session may decide and what must remain pending. If mandate is unresolved, proceed with planning questions while routing authorization separately.

### Phase 2 — Test purpose, boundary and authority

**Inputs:** pre-read and actual participant responses. Read back included/excluded outcomes and current date/funding states. Test disagreement with concrete examples: an extra tenant, missing training, a failed acceptance condition. Separate work ownership from acceptance and change authority.

**Output:** scope/authority agreement rows with source, status and unresolved question. Record an actual decision only with its decider and scope. Do not turn a proposed RACI into accepted staffing.

**Exit:** people can identify the authorized boundary and the route for changing it. A missing authority becomes a named open decision; it does not silently pass.

### Phase 3 — Agree how delivery will work

**Inputs:** boundary, acceptance needs, approach and constraints. Establish near-term planning horizon, feedback opportunities, evidence checkpoints, dependency handoffs, communication purpose and escalation route. Ask what happens when an input is late or a required test fails. Keep resource availability distinct from willingness to help.

**Output:** a working agreement and initial risk/dependency/action records. Preserve different acceptance gates instead of a universal “done.” Schedule detail belongs in integrated planning; the kickoff specifies the inputs needed to build it.

**Exit:** the first planning step has usable inputs or explicit gaps. Owners and dates remain proposed until actually accepted; the meeting date is not every action's due date.

### Phase 4 — Read back and hand off

**Inputs:** discussion notes and draft records. Read decisions, agreements, assumptions and actions separately. Ask the actual authority to correct the decision wording; preserve dissent and conditions. For absent people, record confirmation needed rather than approval.

**Output:** the [kickoff record](template.md), decision/action links, first planning handoff and a proposed review point. Send or book only within existing authorization. An evidence-linked meeting ledger can retain the conversation; the working agreement is its actionable current view.

**Exit:** the recipient can explain the next work, evidence needed, who can decide, and unresolved dependencies. Do not label the integrated baseline approved just because the kickoff finished. At the first review, inspect whether agreements worked and revise them prospectively.

## Examples

Optional worked applications:

- [Relay before baseline approval](examples/software.md): a complete agenda, agreement table and planning handoff without attendance becoming consent.
- [Northstar after charter approval](examples/migration.md): supplier delivery, business acceptance and service readiness remain distinct.

## Common Pitfalls

- **Launch theatre:** introductions and slides consume the session but nobody knows the first decision. Attach an output to every agenda topic and read back open items.
- **Attendance becomes approval:** a list of names is reused as sign-off. Record the exact decision and actual authority; leave absent or silent responses pending.
- **Resource promises by proxy:** a manager volunteers a specialist whose allocation is unknown. Record a capacity-confirmation action before dates depend on it.
- **Everything decided in the room:** an interface debate crowds out scope and authority. Capture its question, evidence and separate workshop owner; continue the kickoff boundary.
- **Reset erases history:** a new kickoff presents an old missed baseline as if it never existed. Carry prior baseline/decision IDs and explain the authorized change.

## References

- [Scrum accountabilities](https://scrumguides.org/scrum-guide.html)
- [Project Charter](../project-charter/SKILL.md), [RACI Matrix](../raci-matrix/SKILL.md) and [Project Governance](../project-governance/SKILL.md) supply mandate and authority inputs.
- [Workshop Facilitation](../workshop-facilitation/SKILL.md) supports a contested session; [Integrated Project Planning](../integrated-project-planning/SKILL.md) receives the handoff.
- [Meeting Knowledge Graph](../meeting-knowledge-graph/SKILL.md) preserves dated evidence when durable meeting memory is needed.

Related skills are optional. If unavailable, create the agreement, decision and handoff artifacts described here.
