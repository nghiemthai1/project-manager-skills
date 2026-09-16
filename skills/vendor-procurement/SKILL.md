---
name: vendor-procurement
description: Plan supplier selection, acceptance and delivery control. Use when a project depends on purchased services
  or vendor deliverables.
metadata:
  type: workflow
  domain: software-it-project-management
  version: 2.1.0
  intent: Coordinate a supplier engagement from defined need through evidenced delivery and accepted commercial
    handoff.
  frameworks: Make-or-buy analysis; statement of work; weighted supplier evaluation; supplier performance and acceptance
    gates
  best_for: '["Coordinate a supplier engagement from defined need through evidenced delivery and accepted commercial
    handoff."]'
  scenarios: '["Use vendor-procurement: Coordinate a supplier engagement from defined need through evidenced delivery
    and accepted commercial handoff."]'
  estimated_time: Depends on evidence and project scope
---
# Vendor and Procurement Management

## Purpose

Turn a supplier dependency into a managed agreement: a clear need, defensible selection, usable deliverables, evidence-based acceptance and an orderly exit. Use for a new purchase or to repair an existing engagement whose handoffs, obligations or escalation routes are unclear.

The workflow produces decision and control artifacts. It does not assume authority to issue an order, sign terms, contact suppliers, accept work or pay invoices. Use the organization's actual purchasing and contract-review process; drafting the pack is useful even when the commercial authority is unknown.

## Input

Bring the desired outcome, make-or-buy options, existing contract or statement of work, approved funding, supplier candidates, due dates, acceptance requirements, data/interface needs and known procurement authority. Existing engagements may enter at mobilization or control rather than repeating selection.

Example: “Our migration depends on a vendor export. Define the acceptance handoff and how we should handle late or defective delivery.” Use supplied context without re-asking. With no detail, ask whether this is a new selection or an existing delivery problem, then draft the relevant phase with unknowns visible. Do not invent contractual remedies from a generic method.

## Key Concepts

### Buy a defined outcome and its evidence

A statement of work should identify deliverables, boundaries, customer inputs, interfaces, quality/acceptance criteria, milestones, responsibilities, reporting and change handling. “Provide migration support” leaves effort and acceptance ambiguous. A bounded export package might specify file/version, field mapping, agreed population, attachment relationships, transfer method, validation evidence and correction workflow.

Supplier delivery and internal acceptance are different events. The supplier may attest that it completed work; the receiving organization decides whether the contracted or agreed criteria were met. Keep commercial acceptance, technical verification, business acceptance and operational transfer distinct where the engagement requires them.

### Select on eligibility before preference

Mandatory conditions such as required interface support or applicable security evidence are pass/conditional/fail checks. Compare eligible options using agreed criteria, anchors and weights. Define those before inspecting scores. Evaluate whole-life cost, including integration, migration, support, transition overlap and exit; the cheapest quote can require the most internal work.

Weighted scores structure judgment but do not erase uncertainty. Run a sensitivity check when small weight changes reverse the ranking. Missing evidence is not automatically zero capability or a pass; record the outstanding question and whether the organization permits conditional evaluation.

### Commercial form changes risk allocation, not reality

A fixed-price arrangement still needs a stable boundary and change process. Time-and-materials work still needs an authorized limit, useful increments and evidence of progress. Milestone payments need the actual agreed milestone and acceptance terms; never assume the PM may withhold or release payment without checking the agreement and authority. A delivery contact is not necessarily the supplier's authorized commercial representative.

## Application

### Phase 1: Define need and route

Input: project outcome, constraints and internal capability. Compare make, buy, reuse or defer where relevant. Output: bounded requirement and make-or-buy rationale, proposed purchasing route and decision owner. Exit when the need and authority for the next procurement step are clear; if not, retain a draft and resolve that question rather than inventing an approval.

### Phase 2: Evaluate feasible options

Input: approved evaluation approach and supplier evidence. Separate eligibility from scored preferences, record conflicts or missing evidence, compare total costs and test sensitivity. Output: evaluation record with recommendation, alternatives and conditions. Exit: actual award/selection decision by the authorized role, or an explicit request for further evidence. A high score alone does not award a contract.

### Phase 3: Agree and mobilize the work

Input: authorized supplier choice and reviewed agreement. Create a deliverable/acceptance matrix, dependency dates, working contacts, authority boundaries, customer obligations and change/escalation routes. Output: agreed engagement baseline or clearly marked draft gaps. Exit: the parties' actual commitments are documented before those commitments enter the project baseline. Link to Dependency Map, RACI and Acceptance and Traceability where useful.

### Phase 4: Control delivery and exceptions

Input: dated progress evidence, delivered versions, acceptance results and current forecast. Compare expected delivery with needed-by dates and monitor both supplier work and customer dependencies. Output: control record, defects, actions and a decision brief for material exceptions. Branch: accept defined work, request correction, investigate ambiguity or propose a change using actual authority. Do not turn a two-day handoff gap into a two-day project slip without the remaining network.

### Phase 5: Accept, transfer and close

Input: applicable acceptance evidence, residual obligations, invoices/commitments, warranty/support and exit needs. Output: acceptance record, commercial reconciliation and accepted operational ownership. Exit: the right people accept the relevant work and obligations; project closure may retain explicitly transferred obligations rather than pretend all have vanished. If the supplier owns data or access, define the evidenced return/export and access-removal route under the actual agreement.

Use [the engagement template](template.md). At every handoff, identify the receiving role and evidence it needs. Quality means the project can distinguish “promised,” “delivered,” “verified,” “accepted” and “paid” without conflating them.

### When producing a visual

Use the [deliverable and acceptance matrix](references/visual-artifact.md) guidance when a diagram, chart or interactive view would help the decision. It defines the source fields, chart limits, readable mobile view and export checks. Preserve the worked example’s evidence and uncertainty in the graphic.

## Examples

- [Relay identity-provider engagement](examples/software.md): fictional procurement subcase with eligibility, preference scoring and a conditional recommendation.
- [Northstar export control](examples/migration.md): an existing supplier's late mapping and defective export require different actions.

## Common Pitfalls

- **Lowest quote wins by default:** internal integration and exit costs disappear. Compare the same service boundary and whole-life cost categories.
- **Score overrides an eligibility failure:** a strong price compensates for an unmet mandatory interface. Resolve eligibility first and retain the disqualifying or conditional evidence.
- **Contact becomes authority:** an account contact's message is treated as contract approval. Identify the authorized commercial and acceptance roles.
- **Receipt equals acceptance:** files arrive and payment or handover is assumed complete. Verify applicable criteria and record each actual decision separately.
- **Silent customer dependency:** the vendor waits for credentials or test data while reports blame delivery effort. Track both sides' commitments and evidence without inventing causality.
- **Generic remedy invented:** a method recommends penalties or withheld payment without agreement terms. Present the delivery problem and ask the actual commercial authority to apply the real agreement.

## References

- [Dependency Map](../dependency-map/SKILL.md), [RACI Matrix](../raci-matrix/SKILL.md): interface and ownership control.
- [Acceptance and Traceability](../acceptance-and-traceability/SKILL.md), [Change Request](../change-request/SKILL.md): acceptance evidence and authorized changes.
- [Project Business Case](../project-business-case/SKILL.md): compare investment alternatives before commitment.

These handoffs are optional packages. If absent, include their required fields directly in the engagement pack. Organization-specific procurement and contract terms take precedence over illustrative practice.
