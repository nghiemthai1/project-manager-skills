# Synthetic execution evidence

These are fictional challenge inputs and actual saved outputs from independent agent executions during repository development. The executing agents received the named skills and raw requests; they did not receive the shared example scenario guide or numeric test answers. This is separation of execution context, not independence of model vendor or a human field trial.

- [Four pilot requests](requests.md): misleading status pressure, an unsupported critical-path claim, an effort/date guarantee, and a two-meeting knowledge bundle.
- [Thirteen planning/control requests](core-requests.json) and outputs in `core-outputs/`.
- [Thirteen delivery/closure requests](delivery-requests.json) and outputs in `delivery-outputs/`.
- Pilot artifacts in `outputs/`; the meeting bundle has its own [index](outputs/meeting-bundle/index.md).

The first status artifact was too long for the one-screen request. `outputs/status-report-first-pass.md` retains it. The corrected skill was rerun to produce `outputs/status-report.md`. The artifacts are evidence, not canonical templates; proposed roles and dates in them remain proposals.

Review reports preserve first-pass findings; follow-up findings are recorded in [the three-case review](reruns/rerun-review.md) and [integrated-plan review](reruns/integrated-rerun-review.md). Original output directories retain the original runs; use `reruns/` for the corrected affected artifacts.

See [validation](../docs/VALIDATION.md) for review findings and limitations. The automated tests check calculations and selected recorded evidence invariants. They do not rerun an AI model or prove future outputs will match.
