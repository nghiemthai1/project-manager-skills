# Relay: proposed RACI before baseline approval

Open the **[interactive artifact](assets/software.html)**, **[SVG](assets/software.svg)**, [editable JSON](assets/software-source.json), or [CSV](assets/software.csv). The HTML runs offline in a browser and coordinates matrix, row-audit and role-profile views; GitHub's file viewer may require downloading it first. [Renderer instructions](../references/renderer.md) explain regeneration and supported behavior.

Fictional training artifact. As of 29 September 2026, before D-001. This matrix adds proposed working assignments for discussion; it does not claim that these assignments, funding, or the 30 October target are approved. Known roles come from the scenario; detailed RACI letters below remain proposed.

Legend: R performs; A owns result; C consulted; I informed; A/R does both; — no assignment in this draft.

| Deliverable / decision | Ada: sponsor | Mina: PM | Omar: engineering | Priya: product | Lena: security | Theo: service |
|---|---|---|---|---|---|---|
| Integrated baseline proposal | C | A/R | C | C | C | C |
| Baseline approval decision | A | R: prepare record | C | C | C | C |
| SAML implementation and engineering evidence | I | C | A/R | C | C | I |
| Backlog ordering | I | C | C | A/R | C | C |
| Security acceptance decision | I | I | R: supply evidence | C | A/R | C |
| Service handover acceptance | I | R: coordinate packet | C | C | C | A/R |
| Material scope/funding change decision | A | R: impact packet | C | C | C | C |

## Boundaries that prevent misuse

Mina's proposed A for the baseline proposal concerns preparation quality, not authority to approve funding. Ada's baseline decision does not replace Lena's security acceptance or Theo's service acceptance. The security row combines Lena's review execution and decision ownership; Omar remains responsible for supplying applicable evidence. “R: supply evidence” and “R: coordinate packet” are deliberately narrower than the decision itself.

The matrix does not assign Sprint forecasts to Mina: Developers retain their Scrum planning accountabilities. It is not a resource plan; Omar's multiple roles require a separate check of hours, skills and timing.

## Review findings and next actions

| Finding | Consequence | Proposed action / owner | Confirmation status |
|---|---|---|---|
| Pilot go/no-go authority not specified in this source set | Cannot infer permission to release from an approved baseline | Mina to obtain the release authority and add a separate row before readiness review | Open; date unspecified |
| Pilot tenant administrators absent from named participant set | User impact could be missed despite technically valid acceptance | Priya to identify representative administrators and propose C involvement in workflow acceptance | Proposed |
| Detailed assignments have not been confirmed | The table cannot be used as an accepted staffing commitment | Mina to review bounded responsibilities with each named role at kickoff | Proposed; no meeting invitation sent |

## Confirmation record

Version RACI-0.1, draft on 29 September. No assignment confirmation supplied. A later D-001 approval establishes only its recorded baseline scope; it must not be used to claim retrospective confirmation of every cell.

**Repair:** “Ada is A on every row because she sponsors the project” obscures separate technical and service authorities. Give Ada the decisions within her mandate and retain Lena's and Theo's distinct acceptance rows.
