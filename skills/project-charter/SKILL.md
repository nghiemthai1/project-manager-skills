---
name: project-charter
argument-hint: '[project mandate and boundaries]'
description: Define the project mandate, boundaries, success and authority. Use when starting a project or clarifying
  what delivery is authorized to achieve.
intent: Create a decision-ready project mandate with measurable outcomes, scope boundaries and explicit authority.
type: component
theme: initiation-and-governance
best_for:
  - Create a decision-ready project mandate with measurable outcomes, scope boundaries and explicit authority.
scenarios:
  - 'Use project-charter: Create a decision-ready project mandate with measurable outcomes, scope boundaries and
    explicit authority.'
estimated_time: Depends on evidence and project scope
frameworks: Project charter; SMART success criteria; assumptions and constraints; delegated authority
domain: software-it-project-management
version: 2.0.0
---
# Project Charter

## Purpose

Turn a mandate into a concise agreement about why the project exists, what it must deliver, how success will be judged and who can authorize decisions. Use before detailed planning, when an initiative is treated as approved without an actual mandate, or when a major change requires the original purpose to be revisited.

A charter is useful when it makes choices explicit. It should let the sponsor decide whether the project deserves authority and resources, and let the PM recognize when a request exceeds that authority. It is not a detailed project plan, contract, product requirements document or retrospective justification for work already performed.

## Input

Bring the sponsor's request, business problem, expected outcome, known boundaries, constraints, potential stakeholders and any existing authorization. A one-paragraph mandate is enough for a first draft. A business case can supply the rationale and option choice, but is not a prerequisite for writing a useful draft with gaps.

Example: “Draft a charter for migrating the service desk. Active tickets and attachments are in scope; analytics is out. We have an approved cutover target but no agreed acceptance measures.”

Read the supplied context as answers already given. If no context exists, ask what change the project should produce and for whom. Do not ask the user to run a kickoff before drafting. Mark unsupported budget, date, success measure and authority fields as proposed or unknown.

## Key Concepts

### Need, output, outcome and benefit

| Concept | Question | Example | Common confusion |
|---|---|---|---|
| Need | What problem or opportunity justifies intervention? | Enterprise access administration is unreliable | Naming a preferred tool as the problem |
| Output | What will the project hand over? | One-tenant SAML access and recovery procedures | Treating installed software as the business outcome |
| Outcome | What observable change should the output enable? | Authorized users can access and recover the service in agreed workflows | Using an activity count as success |
| Benefit | What later value should be measured in use? | A validated reduction in access-support burden | Claiming savings before measuring the baseline and result |

Keep the causal chain plausible and testable. “Deploy system, therefore save 30%” is an assumption until a baseline, measurement method and operational conditions support it. The charter names a benefit owner even when benefit measurement continues after project closure.

### Success criteria that can be evaluated

Use SMART as a prompt for specificity, measurement, feasibility, relevance and timing, not as a demand to invent numeric precision. A criterion needs an observable result, evidence source, owner and review point. “Migration accepted” is circular. “Agreed ticket population and relationships reconcile with explicitly dispositioned exceptions, accepted by the business owner before cutover” identifies how acceptance will be judged; the actual thresholds still require agreement.

Separate deliverable acceptance, project performance and later benefits. The service owner may accept a usable service while the sponsor still needs to assess an overrun. A revised budget does not erase performance against the original authorization.

### Scope is a boundary, not a task inventory

State included outcomes and important exclusions, then identify interfaces and assumptions. Explain why a tempting adjacent request is outside scope. Include transition, training, assurance and closure responsibilities where required; “development complete” rarely defines the entire project.

Use Scope and WBS for detailed decomposition. Avoid including technical solution detail that is still an option under investigation. If solution choice is unmade, charter an investigation or a bounded outcome rather than quietly freezing one implementation.

### Constraints, assumptions and tolerances

A constraint is a real boundary supported by evidence, such as an authorized funding limit or non-negotiable operating window. A wish is a target until the authority and feasibility basis are established. An assumption is a proposition the plan relies on; give it a validation owner, review point and consequence if false.

A tolerance defines the variation a named role may handle without escalation. Do not invent a standard “10%” PM tolerance or infer that being called PM grants spending authority. If delegation is missing, record the decision needed and operate within the actual authorization supplied.

## Application

1. **Extract the mandate and decision.** Identify the sponsor, problem, affected group, desired outcome and approval status. Separate existing authorization from the new decision this charter requests. For an already approved project, cite the source rather than manufacturing a new signature requirement.
2. **Define the boundary and options.** List included deliverables, explicit exclusions and interfaces. Where choice is unresolved, show the decision or investigation required. Confirm that acceptance and transition work are not omitted merely because they are not development tasks.
3. **Build success and acceptance criteria.** For each material result, identify evidence, authority and timing. Separate delivery acceptance, schedule/cost performance and later benefits. Mark proposed measures and unknown thresholds as such.
4. **State feasibility assumptions and governance.** Record high-level target milestones, estimate ranges, funding basis, reserve treatment, key risks and dependencies. Name delegated decisions and escalation routes with their actual source. Do not convert an estimate into a commitment because the template has a date field.
5. **Review the decision packet.** Check whether scope, success, money, dates and authority agree. Present unresolved conditions and the consequences of approval, deferral or a bounded investigation. Obtain only the approval needed for the stated mandate; drafting does not authorize spending or external work.
6. **Record and hand off.** Preserve the actual decision, scope, approver, date and reference. Hand the charter to kickoff and integrated planning. If not approved, hand off a draft and open-decision list, not a fictional baseline. Later changes retain the original charter and link the decision that changed it.

Use [the charter template](template.md). A useful charter can fit a few pages; substantial option economics belong in Project Business Case, detailed responsibilities in RACI Matrix, and executable planning in Integrated Project Planning.

### Quality review

Can the sponsor tell what is being authorized? Can a delivery lead identify excluded work? Can an acceptance owner explain what evidence is required? Can the PM recognize a decision outside their delegation? Can the benefit owner identify a later review? If not, improve those fields rather than polishing the title page.

## Examples

- [Relay software charter](examples/software.md): a complete proposed charter before baseline approval, with measured acceptance still requiring agreement.
- [Northstar migration charter](examples/migration.md): an existing approved mandate is summarized without expanding scope or inventing tolerances.

## Common Pitfalls

- **Solution masquerading as purpose:** “Implement tool X” offers no reason to prefer it. Describe the operational need and outcome, then identify whether tool choice is approved or still an option.
- **All goals are benefits:** a project promises immediate savings, adoption and every service improvement. Separate what the project can deliver from what operations must realize and measure afterward.
- **Scope by implication:** archive access is included, so a stakeholder assumes all historical analytics are included. State the retrieval boundary and the explicit analytics exclusion.
- **Date authority by formatting:** a target entered in a milestone table becomes an approved commitment. Label target, estimate, forecast or baseline and cite the actual decision.
- **Signature fiction:** names in an approval table are treated as signed consent. Show requested approvers separately from decisions actually recorded.
- **Governance vacuum:** the PM is told to “own delivery” but cannot resolve funding or capacity conflicts. Record the delegation gap and an escalation route; do not invent authority to compensate.

## References

- [Project Business Case](../project-business-case/SKILL.md): test investment rationale and options.
- [Project Governance](../project-governance/SKILL.md): detail authority, tolerances and gates.
- [Scope and WBS](../scope-and-wbs/SKILL.md): decompose included work.
- [Acceptance and Traceability](../acceptance-and-traceability/SKILL.md): connect requirements to executed evidence.
- [Benefits Realization](../benefits-realization/SKILL.md): own and measure later value.
- [Project Kickoff](../project-kickoff/SKILL.md): establish the working agreement.

Related skills are optional. Their artifacts can be prepared directly from the requirements here if a package is unavailable.
