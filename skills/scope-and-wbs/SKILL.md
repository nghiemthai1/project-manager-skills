---
name: scope-and-wbs
argument-hint: '[scope boundary and deliverables]'
description: Define a deliverable-oriented scope breakdown with boundaries and completion evidence. Use when preparing
  estimates or resolving missing, duplicated or expanding project work.
intent: Turn the mandate into complete, nonoverlapping work packages that can be estimated, owned and accepted.
type: component
theme: scope-and-planning
best_for:
  - Turn the mandate into complete, nonoverlapping work packages that can be estimated, owned and accepted.
scenarios:
  - Decompose the approved project scope into deliverable-oriented work packages with boundaries and completion
    evidence.
estimated_time: Depends on evidence and project scope
frameworks: Deliverable-oriented WBS; 100% rule; WBS dictionary
domain: software-it-project-management
version: 2.1.0
---
# Scope and Work Breakdown

## Purpose

Make the project's work boundary explicit before people price it, schedule it or claim it is complete. Produce a deliverable-oriented work breakdown structure, a dictionary for consequential work packages, and a record of exclusions and unresolved decisions. Use for initial planning, a scope review or change-impact analysis.

A WBS organizes what the project must produce and the work needed to produce it. A schedule sequences that work. A backlog orders evolving items. They may share IDs and relationships, but none is automatically a substitute for the others. The output should expose missing integration, assurance and transition work as clearly as missing features.

## Input

Bring the mandate, scope version, outcomes, deliverables, exclusions, acceptance conditions, interfaces and known constraints. A rough list is enough to start. Use inline facts without re-asking; with no input, ask what authorized outcome the breakdown must cover. If scope is disputed, preserve both interpretations as a decision rather than choosing one silently.

Copy supplied mandate, package and requirement identifiers and version strings exactly, including case, punctuation and spacing. Treat these as literal data during editing and compare them against the input before delivery. Prose-formatting substitutions must not alter traceability references.

Example: “Break our SSO pilot into work packages, including recovery evidence and the work needed to operate it.” Do not borrow sample people, costs or commitments from these examples as project facts.

## Key Concepts

### Decompose outcomes, then test completeness

The 100% rule asks whether the children collectively cover the parent's project scope without double counting it. It is a test of coverage and boundaries, not a claim that uncertainty has disappeared. Use stable IDs and meaningful parent/child relationships. Include project management and enabling work when they are part of delivery; a feature-only breakdown misses approvals, environments, migration, training and closure.

A deliverable-oriented label names an observable result, such as “verified attachment mapping,” rather than an activity like “hold data meeting.” Activities can later sit beneath that work package in the schedule. Organizing by phase or team can help views, but keep a single clear scope ownership model so the same integration work is not budgeted twice.

### Stop at a useful work package

A work package is detailed enough when its output, boundary, accountable delivery role, acceptance evidence, estimate basis and interfaces can be understood. Decompose further when hidden variation changes ownership, acceptance or estimation. Do not force every package to the same size or a universal hours rule. If the uncertainty dominates, identify a bounded investigation with its decision output rather than disguising it as a precise build task.

| Dictionary field | What it must make clear |
|---|---|
| Output and boundary | What is produced, included and excluded |
| Completion evidence | Observable criterion and who accepts the result |
| Delivery role | Who prepares/performs the work; proposed versus confirmed |
| Interfaces | Inputs needed and outputs another package consumes |
| Estimate basis | Scope assumptions, unit, method and confidence limits |
| Control link | Source mandate, requirement IDs and change version |

### Preserve scope under progressive elaboration

Near-term packages can have executable detail while later work remains at a planning-package level with assumptions and review points. Do not call undefined work out of scope merely because it has not been decomposed. Conversely, a useful idea is not authorized scope just because someone adds it to the hierarchy. Record material additions, removals and changed acceptance through the actual scope-control process.

## Application

1. **State the boundary.** Identify the mandate/version, included outcomes, explicit exclusions and open scope decisions. Separate approved scope from a proposed addition or optional deferral.
2. **Build the hierarchy.** Group results into a small number of understandable deliverables, then decompose enough to reveal ownership and interfaces. Give every node a stable ID; keep alternative views linked to the same underlying packages.
3. **Write consequential dictionary entries.** Define output, acceptance, owner status, interfaces, assumptions and estimate basis. Use an investigation package where unknowns prevent a responsible delivery estimate.
4. **Audit coverage and overlap.** Walk from each requirement to a package and from each package back to a mandate. Check build, integration, testing, data, security, transition, management and closure as relevant. Ask where each shared handoff is counted once.
5. **Resolve or expose decisions.** A boundary conflict should produce options and the actual decision owner. Keep proposed assignments and acceptance criteria distinct from agreements. Do not remove mandatory work to make the hierarchy fit a target date.
6. **Hand off and maintain.** Pass package IDs to estimation, dependencies, schedule, cost and traceability. When scope changes, update affected packages and retain the prior version and decision reference; do not silently rewrite earlier reports.

Use [the WBS and dictionary template](template.md). The quality review should find no orphan requirement, no unexplained package, no duplicated shared work and no claim of accepted ownership without evidence. Coverage can remain explicitly incomplete while a decision is open; honesty is more useful than a false 100% badge.

### When producing a visual

Use the [deliverable hierarchy](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay scope hierarchy](examples/software.md): a full pilot boundary, detailed recovery package and a controlled optional deferral.
- [Northstar migration packages](examples/migration.md): population, relationships, restore and service transfer cannot hide inside “migration.”

## Common Pitfalls

- **Task list mistaken for scope:** meetings and coding tasks have no defined output. Anchor packages in deliverables and acceptance, then sequence activities separately.
- **Missing transition work:** support, reversal and training do not appear in estimates. Include the outputs needed by the receiving service and their evidence.
- **Double-counted integration:** every team budgets the whole shared handoff. Assign the shared package once and define each contributor's bounded input.
- **Decomposition as certainty:** many rows conceal unknown data quality. Record an investigation, its assumptions and the decision it informs.
- **Quiet scope deletion:** an in-scope “nice to have” disappears without a decision. Retain the approved boundary and route the proposed deferral through change control.

## References

- [Project Charter](../project-charter/SKILL.md): mandate and boundaries.
- [Acceptance and Traceability](../acceptance-and-traceability/SKILL.md): coverage and completion evidence.
- [Estimation Advisor](../estimation-advisor/SKILL.md), [Change Request](../change-request/SKILL.md): estimate and maintain the defined work.

If adjacent skills are unavailable, the scope hierarchy, dictionary and decision record remain usable on their own.
