# Project Manager Skills

Practical skills for software and IT project managers, written to improve both the work and the judgment behind it.

Start with your decision: define scope, test a delivery forecast, expose a risk, recover a troubled project, or establish whether a release is ready. Each skill explains the framework, when to use it, how to apply it, and recognizable failure modes.

The current library contains **43 skills**, reusable templates, **four calculation helpers**, and **eleven standalone visual renderers**. All 30 original skills have been expanded, with 13 additions covering missing project-management jobs. It includes durable meeting memory in OKF v0.2 format. No application, hosted service, or tracker connection is required.

## Find the skill you need

| Your situation | Start here |
|---|---|
| We need a clear mandate | [Project Charter](skills/project-charter/SKILL.md) |
| Our approach does not fit the work | [Delivery Approach Advisor](skills/delivery-approach-advisor/SKILL.md) |
| Scope keeps expanding | [Scope and Work Breakdown](skills/scope-and-wbs/SKILL.md), then [Change Request](skills/change-request/SKILL.md) |
| The date is doubtful | [Estimation Advisor](skills/estimation-advisor/SKILL.md), [Milestone Schedule](skills/milestone-schedule/SKILL.md) |
| Responsibilities are unclear | [RACI Matrix](skills/raci-matrix/SKILL.md) |
| Project parties are deadlocked | [Conflict Resolution and Negotiation](skills/conflict-resolution-and-negotiation/SKILL.md) |
| We need a timeline or baseline comparison | [Gantt Chart](skills/gantt-chart/SKILL.md) |
| Other teams are blocking us | [Dependency Map](skills/dependency-map/SKILL.md) |
| People are overallocated | [Resource Capacity Plan](skills/resource-capacity-plan/SKILL.md) |
| Reports say green but the evidence does not | [Project Health Diagnostic](skills/project-health-diagnostic/SKILL.md) |
| We need a sponsor decision | [Escalation Brief](skills/escalation-brief/SKILL.md) |
| Meetings keep losing decisions | [Meeting Knowledge Graph](skills/meeting-knowledge-graph/SKILL.md) |
| We may not be ready to release | [Release Readiness](skills/release-readiness/SKILL.md) |
| Delivery is finished but obligations remain | [Project Closure](skills/project-closure/SKILL.md) |

Browse the [complete catalog](catalog/README.md) or follow the [quick start](docs/QUICKSTART.md).

## How the library works

- **Components** create a bounded artifact, such as a charter or decision log.
- **Interactive skills** ask only the missing questions that change the recommendation.
- **Workflows** connect planning, delivery control, release, and closure without requiring every skill to be installed.

Start with Purpose and Input, follow Application, and use Common Pitfalls to review the result. Templates and specialized references support the work as needed.

Each skill has an optional Examples section with fictional worked applications and their downloads. To see how skills connect, follow the [software release](docs/walkthroughs/software.md) or [IT migration](docs/walkthroughs/migration.md) walkthrough.

## Skills and frameworks

<!-- skill-framework-catalog:start -->
### Initiation and governance (6)

| Skill | Focus | Framework |
|---|---|---|
| [Project Intake Advisor](skills/project-intake-advisor/SKILL.md) | Triage requests into a project, change, operational work, or investigation | Request triage; outcome-evidence-action; decision rights |
| [Project Business Case](skills/project-business-case/SKILL.md) | Compare investment options before authorizing delivery | Options appraisal; cost-benefit analysis; sensitivity analysis |
| [Delivery Approach Advisor](skills/delivery-approach-advisor/SKILL.md) | Choose delivery practices that fit uncertainty and governance | Predictive/agile/hybrid tailoring; rolling-wave planning |
| [Project Charter](skills/project-charter/SKILL.md) | Authorize a bounded outcome and management mandate | Project charter; SMART success criteria; assumption analysis |
| [Project Governance](skills/project-governance/SKILL.md) | Define decision rights, tolerances, assurance, and escalation | Stage gates; management by exception; delegated authority |
| [Project Kickoff](skills/project-kickoff/SKILL.md) | Turn the mandate into an operating agreement | Kickoff facilitation; RACI; decision/action separation |

### Stakeholders and collaboration (7)

| Skill | Focus | Framework |
|---|---|---|
| [Stakeholder Identification](skills/stakeholder-identification/SKILL.md) | Find affected people, delivery partners, and decision makers | MITRE stakeholder identification; allies/audiences/influencers; equity lens |
| [Stakeholder Map](skills/stakeholder-map/SKILL.md) | Set engagement priorities and expose missing voices | Power-interest matrix; impact-power matrix; quadrant migration |
| [Stakeholder Engagement Advisor](skills/stakeholder-engagement-advisor/SKILL.md) | Prepare reciprocal engagement for a specific stakeholder | Adaptive Decision Ladder; MITRE engagement canvas; credible proxies |
| [Conflict Resolution and Negotiation](skills/conflict-resolution-and-negotiation/SKILL.md) | Resolve project conflict and negotiate bounded agreements | Interest-based negotiation; BATNA and reservation boundaries; mediation |
| [RACI Matrix](skills/raci-matrix/SKILL.md) | Assign clear work accountability without inventing authority | RACI responsibility assignment matrix; horizontal/vertical role analysis |
| [Communication Plan](skills/communication-plan/SKILL.md) | Choose audience-specific messages, channels, and feedback | Communication matrix; push/pull/interactive communication |
| [Workshop Facilitation](skills/workshop-facilitation/SKILL.md) | Run purposeful guided sessions and handle interruptions | One-question facilitation; guided/context-dump/best-guess modes |

### Scope and planning (7)

| Skill | Focus | Framework |
|---|---|---|
| [Scope and Work Breakdown](skills/scope-and-wbs/SKILL.md) | Decompose complete deliverables and control boundaries | Deliverable-oriented WBS; 100% rule; WBS dictionary |
| [Acceptance and Traceability](skills/acceptance-and-traceability/SKILL.md) | Connect requirements to executed evidence and acceptance | Requirements traceability matrix; verification versus validation |
| [Prioritization Advisor](skills/prioritization-advisor/SKILL.md) | Choose a defensible scope sequencing or tradeoff method | MoSCoW; RICE; weighted scoring; Cost of Delay; Kano |
| [Estimation Advisor](skills/estimation-advisor/SKILL.md) | Select an estimation method and expose uncertainty | Analogous/parametric/bottom-up estimation; three-point PERT; empirical forecasting |
| [Milestone Schedule](skills/milestone-schedule/SKILL.md) | Build feasible logic and milestone forecasts | Critical Path Method; total float; rolling-wave scheduling |
| [Gantt Chart](skills/gantt-chart/SKILL.md) | Design and deliver responsive schedule views from mapped source evidence | Gantt timeline; source normalization; responsive interaction; baseline/forecast comparison |
| [Integrated Project Planning](skills/integrated-project-planning/SKILL.md) | Reconcile scope, schedule, capacity, funding and gates | Integrated baseline planning; progressive elaboration; consistency review |

### Controls and assurance (7)

| Skill | Focus | Framework |
|---|---|---|
| [Dependency Map](skills/dependency-map/SKILL.md) | Secure usable provider-to-receiver handoffs | Dependency network; interface agreements; local margin; dependency structure matrix; Conway's Law; CPM boundary |
| [Resource Capacity Plan](skills/resource-capacity-plan/SKILL.md) | Resolve individual bottlenecks and competing allocations | Capacity-demand analysis; skill constraints; resource leveling options |
| [Project Budget](skills/project-budget/SKILL.md) | Plan and control forecast cost and funding | Cost baseline; contingency versus management reserve; earned value management |
| [Vendor and Procurement Management](skills/vendor-procurement/SKILL.md) | Define vendor selection, deliverables, acceptance and controls | Make-or-buy; weighted supplier evaluation; contract deliverable control |
| [Quality Management Plan](skills/quality-management-plan/SKILL.md) | Plan assurance, verification and defect disposition | Quality planning/assurance/control; verification versus validation; risk-based testing; PDCA |
| [RAID Log](skills/raid-log/SKILL.md) | Maintain actionable risks, assumptions, issues and dependencies | RAID; cause-event-effect; issue lifecycle; assumption validation |
| [Risk Workshop](skills/risk-workshop/SKILL.md) | Discover and select responses to project uncertainty | Premortem; probability-impact matrix; response planning; residual risk |

### Delivery and decisions (9)

| Skill | Focus | Framework |
|---|---|---|
| [Status Report](skills/status-report/SKILL.md) | Report evidence, variance and decisions for the audience | RAG by tolerance; management by exception; baseline/forecast/actual |
| [Decision Log](skills/decision-log/SKILL.md) | Preserve the exact choice, authority, rationale and conditions | DACI; decision records; option analysis |
| [Escalation Brief](skills/escalation-brief/SKILL.md) | Obtain a timely decision beyond delegated authority | SBAR; options and recommendation; last responsible decision point |
| [Meeting Knowledge Graph](skills/meeting-knowledge-graph/SKILL.md) | Preserve evidence-linked meeting history and current state | OKF v0.2; immutable ledgers; attribution confidence; series delta |
| [Sprint Planning](skills/sprint-planning/SKILL.md) | Support a coherent goal and feasible team forecast | Scrum Sprint Planning; Sprint Goal; Definition of Done; capacity |
| [Change Request](skills/change-request/SKILL.md) | Assess and decide changes without laundering baselines | Integrated change control; impact analysis; configuration history |
| [Project Health Diagnostic](skills/project-health-diagnostic/SKILL.md) | Diagnose delivery confidence from conflicting signals | Dimensional health assessment; leading/lagging indicators; causal hypotheses |
| [Project Recovery Advisor](skills/project-recovery-advisor/SKILL.md) | Select a feasible response when the plan fails | Root-cause hypotheses; recovery option appraisal; recovery checkpoints |
| [Delivery Control Cycle](skills/delivery-control-cycle/SKILL.md) | Run a repeatable evidence-to-decision control review | Plan-monitor-control; exception escalation; integrated change control |

### Transition and outcomes (7)

| Skill | Focus | Framework |
|---|---|---|
| [Organizational Change and Adoption](skills/organizational-change/SKILL.md) | Prepare affected people to adopt the delivered change | ADKAR lens; change impact assessment; readiness and reinforcement |
| [Release Readiness](skills/release-readiness/SKILL.md) | Recommend go/hold using current applicable evidence | Readiness gates; exception authority; operational acceptance |
| [Release and Handover](skills/release-and-handover/SKILL.md) | Coordinate authorized execution and accepted service transfer | Cutover checkpoints; recovery limits; service transition; hypercare exit |
| [Retrospective](skills/retrospective/SKILL.md) | Turn observations into testable improvements | PDCA; 5 Whys with evidence; experiment design |
| [Lessons Learned](skills/lessons-learned/SKILL.md) | Capture transferable learning with limits and adoption evidence | After-action review; contextual lessons; knowledge transfer |
| [Benefits Realization](skills/benefits-realization/SKILL.md) | Assign and verify post-delivery business outcomes | Benefits map; leading/lagging measures; ownership and review plan |
| [Project Closure](skills/project-closure/SKILL.md) | Close or terminate only with accepted residual obligations | Closure assurance; financial reconciliation; residual transfer; benefits handoff |
<!-- skill-framework-catalog:end -->

## Calculation helpers

Python 3.11+ standard library only. Each helper lives inside its owning skill and supports JSON input, Markdown/JSON output, and a demo.

```sh
python skills/estimation-advisor/scripts/estimate.py --demo
python skills/resource-capacity-plan/scripts/capacity.py --demo
python skills/milestone-schedule/scripts/schedule.py --demo
python skills/project-budget/scripts/earned_value.py --demo
```

Read the helper's input contract before using it. The schedule helper models an unconstrained finish-to-start network, not calendars or resource leveling. Earned value indicators do not authorize spending or predict calendar delay.

## Installation and maintenance

| Tool | Download | Contents |
|---|---|---|
| Codex | [`pm-skills-codex.zip`](https://github.com/nghiemthai1/project-manager-skills/releases/latest/download/pm-skills-codex.zip) | Installs `.agents/skills` and `AGENTS.md` |

Download the release ZIP and extract into your project root; merge the included `AGENTS.md` with any existing project instructions. See the [Codex ZIP setup](docs/INSTALLATION.md#codex-zip-quick-setup).

[Install selected skills](docs/INSTALLATION.md). Reading Markdown requires no runtime. Python is needed only for optional helpers and repository checks.

For maintainers:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python scripts/check-skill-metadata.py
python scripts/check-skill-triggers.py
python -m unittest discover -s tests -v
```

Read [Authoring](docs/AUTHORING.md), [Frameworks](docs/FRAMEWORKS.md), [Glossary](docs/GLOSSARY.md), and [Validation](docs/VALIDATION.md).

## Validation status

This is a newly authored skill set. Numerical regression tests and independent synthetic project exercises provide evidence of specific behavior. They do not establish a history of production use. The [v2 evaluation record](evals/v2/README.md) retains 42 fictional behavior cases, three targeted reruns and a separate description-routing run. See the validation report for coverage, limitations and corrections.

## Contributing and licensing

Read [contribution.md](contribution.md) to propose improvements or submit a pull request.

Original skills, documentation, and code use [MIT](LICENSE.md), allowing commercial reuse. Six Dean Peters adaptations retain CC BY-NC-SA 4.0 and its noncommercial restriction. See [license scope](LICENSING.md) and [third-party notices](THIRD_PARTY_NOTICES.md) for attribution and package-specific terms.
