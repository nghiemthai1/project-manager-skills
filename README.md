# Project Manager Skills

Practical skills for software and IT project managers, written to improve both the work and the judgment behind it.

Start with your decision: define scope, test a delivery forecast, expose a risk, recover a troubled project, or establish whether a release is ready. Each skill explains the method, its limits, a worked application, and recognizable failure modes.

This private library contains **30 skills**, **30 templates**, **60 worked examples**, and **four standalone calculation helpers**. It includes durable meeting memory in OKF v0.2 format. No application, hosted service, or tracker connection is required.

## Find the skill you need

| Your situation | Start here |
|---|---|
| We need a clear mandate | [Project Charter](skills/project-charter/SKILL.md) |
| Our approach does not fit the work | [Delivery Approach Advisor](skills/delivery-approach-advisor/SKILL.md) |
| Scope keeps expanding | [Scope and Work Breakdown](skills/scope-and-wbs/SKILL.md), then [Change Request](skills/change-request/SKILL.md) |
| The date is doubtful | [Estimation Advisor](skills/estimation-advisor/SKILL.md), [Milestone Schedule](skills/milestone-schedule/SKILL.md) |
| Other teams are blocking us | [Dependency Map](skills/dependency-map/SKILL.md) |
| People are overallocated | [Resource Capacity Plan](skills/resource-capacity-plan/SKILL.md) |
| Reports say green but the evidence does not | [Project Health Diagnostic](skills/project-health-diagnostic/SKILL.md) |
| We need a sponsor decision | [Escalation Brief](skills/escalation-brief/SKILL.md) |
| Meetings keep losing decisions | [Meeting Knowledge Graph](skills/meeting-knowledge-graph/SKILL.md) |
| We may not be ready to release | [Release Readiness](skills/release-readiness/SKILL.md) |
| Delivery is finished but obligations remain | [Project Closure](skills/project-closure/SKILL.md) |

Browse the [complete catalog](catalog/README.md), follow the [quick start](docs/QUICKSTART.md), or read the [software release](docs/walkthroughs/software.md) and [IT migration](docs/walkthroughs/migration.md) walkthroughs.

## How the library works

- **Components** create a bounded artifact, such as a charter or decision log.
- **Interactive skills** ask only the missing questions that change the recommendation.
- **Workflows** connect planning, delivery control, release, and closure without requiring every skill to be installed.

Every entrypoint includes Purpose, Input, Key Concepts, Application, Examples, Common Pitfalls, and References. The learning is part of the skill: read why an approach fits, what it cannot prove, and how a misleading artifact is repaired.

The two example projects are fictional. Their values are teaching inputs, not default thresholds, commitments, or approvals for your project.

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

Download while signed in to GitHub with access to this private repository. Extract into your project root; merge the included `AGENTS.md` with any existing project instructions. See the [Codex ZIP setup](docs/INSTALLATION.md#codex-zip-quick-setup).

[Install selected skills](docs/INSTALLATION.md). Reading Markdown requires no runtime. Python is needed only for optional helpers and repository checks.

For maintainers:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

Read [Authoring](docs/AUTHORING.md), [Frameworks](docs/FRAMEWORKS.md), [Glossary](docs/GLOSSARY.md), and [Validation](docs/VALIDATION.md).

## Validation status

This is a newly authored skill set. Numerical regression tests and independent synthetic project exercises provide evidence of specific behavior. They do not establish a history of production use. See the validation report for exact coverage, limitations, and the record of corrections.

Private repository. No public redistribution license is granted in this release.
