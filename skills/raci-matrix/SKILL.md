---
name: raci-matrix
argument-hint: '[deliverables, roles, and assignment evidence]'
description: Build and visualize responsibility matrices with assignment evidence. Use when deliverable ownership,
  accountability, consultation or notification is unclear.
intent: Produce an auditable responsibility matrix and usable graphical artifacts with explicit work boundaries,
  confirmation state, accessible inspection and editable source.
type: component
theme: stakeholders-and-collaboration
best_for:
  - Assign clear responsibilities for defined deliverables and expose unresolved authority.
scenarios:
  - 'Use raci-matrix: Assign clear responsibilities for defined deliverables and expose unresolved authority.'
estimated_time: Depends on evidence and project scope
frameworks: RACI; responsibility assignment matrix; horizontal and vertical role analysis
domain: software-it-project-management
version: 2.2.0
license: MIT
---
# RACI Matrix

## Purpose

Build a responsibility assignment matrix that people can use to coordinate delivery. Use it at kickoff, after a reorganization, when vendor and internal ownership conflict, or when work is repeatedly delayed by unclear responsibility. The output is a deliverable-by-role grid, a source/confirmation register, and a short list of unresolved assignments.

RACI does not replace a project schedule, staffing plan, acceptance criteria or decision log. It tells people how they relate to the work. It does not prove they have capacity or that an approval occurred. For a single contested decision, DACI in Decision Log may be more useful than a large RACI.

## Input

Bring the deliverable list or WBS, named people or roles, authority/delegation records, current handoffs and known ownership disputes. Drafts and partial lists are useful. If nothing is supplied, ask which project outcome or handoff needs ownership first; do not invent a team.

Example: “Create a RACI for migration rehearsal, cutover, operations handover and closure. The vendor says it owns all acceptance.”

Use facts supplied in the invocation as answers already given. If the user only wants a matrix, draft with proposed assignments and unresolved cells rather than forcing a workshop. Ask only for authority information that changes a consequential assignment.

## Key Concepts

### Four distinct relationships

| Code | Meaning | Question it answers | Evidence to seek |
|---|---|---|---|
| R — Responsible | Performs or coordinates the specified work | Who does this? | Role agreement, accepted assignment and actual execution boundary |
| A — Accountable | Owns the result and has authority for that row | Who answers for this result? | Delegation, mandate or agreed process authority |
| C — Consulted | Provides two-way input before the relevant work or decision | Whose contribution changes the result? | A specific expertise, dependency or affected perspective |
| I — Informed | Receives one-way information at a useful trigger | Who needs to know the outcome? | A defined downstream action or communication need |

Use one clearly identified A per bounded row as the default RACI convention. Several R assignments can be appropriate if their subwork is explicit. A/R is acceptable when one person both owns and performs the same bounded work. A can be held by an authorized role or governance body; “everyone” is not a substitute for that authority.

If two approvals are independently required, split the work into distinct rows—for example security acceptance and business acceptance—rather than forcing either authority into a decorative C role. Keep a separate release-decision row when the release authority considers both inputs. Where authority is unknown, leave A unresolved and identify who must confirm it.

### Row granularity determines usefulness

“Deliver project” is too broad to diagnose a handoff. “Press button 37” is too detailed for a governance matrix. Choose observable deliverables, acceptance decisions and consequential handoffs at the level where different responsibilities matter. Use the WBS to check coverage, including enabling work, vendor interfaces, assurance, training and transition.

Do not put informal technical leadership and formal acceptance authority in the same column without naming which capacity applies. For Scrum work, a project manager's coordination role does not replace Product Owner ordering or Developers' planning accountabilities.

### Two audits, different questions

**Horizontal review:** scan each row for missing R, absent or conflicting A, overlapping R boundaries, excessive C, and missing I recipients. A row with no R is unstaffed work; a row with no known A is unresolved ownership.

**Vertical review:** scan each person/role column for concentration of R/A, incompatible duties, consultation bottlenecks and a stakeholder listed only as I despite material impact. RACI counts are not a utilization calculation; use capacity planning before concluding overload or spare capacity.

A matrix becomes operational only when people understand and accept their assignments. Label it draft/proposed until that confirmation exists. Silence after an email is not acceptance.

Use the declared, reviewable tests in [RACI audit methods](references/raci-audit-methods.md). A structural rule such as “one A per bounded row” can identify a governance question. A concentration threshold can identify where to ask about capacity or decision bottlenecks. Neither kind of rule proves the answer.

## Application

1. **Bound the matrix.** Identify scope version, date, purpose and decision rights. Choose rows from actual deliverables and handoffs. Split rows where acceptance authority or work boundary differs.
2. **Draft assignments from evidence.** Populate R, A, C and I with the source or rationale for each material assignment. Keep unknowns visible. Suggest plausible assignments as proposals without promoting them to facts.
3. **Audit rows and columns.** Check the horizontal and vertical failure patterns above. Compare supplier obligations with internal acceptance responsibilities. Check absent affected groups against the stakeholder map.
4. **Resolve conflicts with the right people.** Ask the actual authority to clarify conflicting A assignments; ask delivery leads to divide shared R work. If unresolved, record the conflict, interim coordination route and consequence. Do not settle a dispute merely by choosing a tidier table.
5. **Confirm and connect.** Record who confirmed which assignments and when. Link observable acceptance criteria, the communication trigger for I, and any resource allocation decision. Drafting the matrix does not send messages or assign work in a live system.
6. **Maintain the agreement.** Revisit when scope, personnel, supplier boundaries or governance change. Preserve prior versions and confirmation records; do not backdate a reassignment into an earlier missed handoff.

Use the [matrix template](template.md). The final package should include the readable grid, role definitions, unresolved assignments and a confirmation/version log. If the user wants CSV or a spreadsheet, preserve those semantics in separate columns or companion sheets rather than dropping caveats to fit cells.

### Produce the visual artifact

When the user wants a graphical matrix, follow [the visual model and design contract](references/visual-model-and-design.md). Keep relationship letters, narrower work duties and confirmation state separate in the data and display. Use a stable row/role grid, restrained redundant color, a visible proposed/confirmed legend and an audit register. Pair the matrix with horizontal row audit and vertical role-profile views; neither may silently rewrite the matrix. A/R counts are not utilization.

Choose the output for the audience: a readable static SVG/PDF for a report, a spreadsheet for cell-based collaboration, or self-contained HTML for search, workstream and confirmation filters, role focus, row audit, role profiles and persistent cell details. Preserve a full accessible table and editable source. A phone-width view should provide deliverable/role cards or a focused slice, not tiny text. Show active filters, hidden columns and a reset; keyboard users must be able to inspect the same duties as pointer users.

Use [the artifact acceptance checklist](references/artifact-review.md) on actual generated files. Compare every letter, work boundary and confirmation state against the source, inspect desktop/portrait/landscape, and verify export scope. If a renderer is unavailable, label the table/source a draft rather than claim that a graphic was produced.

### Included offline renderer

Use [the renderer contract](references/renderer.md) when producing a standalone artifact from normalized JSON. The included [Python helper](scripts/render_raci.py) writes self-contained HTML, a full SVG, source JSON and long-form CSV with Python 3.11+ and no external packages. The HTML provides matrix, row-audit and role-profile views plus full and visible-slice exports. Map the supplied project data to the input contract, then inspect the actual outputs. Its supported scope is deliberately smaller than a live assignment or capacity-management application.

### Quality check before delivery

Can a new team member find who performs the work, who owns the result, who contributes and who receives the outcome? Does every A refer to a real or explicitly proposed authority? Are independent acceptance decisions separate? Are vendor completion and internal acceptance distinguishable? Does the matrix show where confirmation is still needed?

## Examples

Optional worked applications:

- [Software release](examples/software.md): a complete draft RACI separates engineering delivery, security acceptance, service handover and sponsor decisions.
- [IT migration](examples/migration.md): a vendor deliverable is kept distinct from business acceptance and operational transfer.

## Common Pitfalls

- **Two competing A assignments:** a row names both sponsor and service owner as final authority, so each expects the other to act. Split the distinct decisions or confirm a single accountable role for the actual shared outcome.
- **Everyone is C:** routine work waits for an expanding review group. Define the contribution needed, its timing and whether a person only needs the result as I; do not remove a required reviewer to reduce the count.
- **Vendor owns acceptance:** a supplier marks its own delivery complete and the project assumes business readiness. Keep supplier delivery R/A separate from the organization's acceptance and go/no-go rows.
- **One A manufactured for neatness:** an unresolved role is assigned to the PM because the template expects a letter. Mark the gap and route the authority decision; a blank with a resolution action is more truthful.
- **RACI as capacity proof:** someone appears on two rows, so the report declares them overloaded. Inspect effort and timing; the matrix reveals a question, not the utilization answer.
- **Paper agreement:** a sponsor approves the document but the named participants never accept their work. Record role confirmation and resource commitments separately from document endorsement.

## References

- [Project Kickoff](../project-kickoff/SKILL.md): establish the working agreement.
- [Scope and WBS](../scope-and-wbs/SKILL.md): derive bounded deliverable rows.
- [Decision Log](../decision-log/SKILL.md): use DACI for a specific choice.
- [Resource Capacity Plan](../resource-capacity-plan/SKILL.md): test whether the assignments are feasible.
- [Stakeholder Map](../stakeholder-map/SKILL.md): check affected voices and authority assumptions.

Related packages are optional. If they are unavailable, request the corresponding source artifact rather than stopping the matrix.
