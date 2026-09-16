# Release acceptance ledger

Target: 30 original software/IT project management skills, two worked scenarios per skill, four standalone calculation helpers, adapted OKF meeting memory, private GitHub delivery.

This ledger records release evidence. Unchecked items are incomplete, not implied by a passing structural check.

- [x] 30 skills and metadata complete
- [x] 30 templates and 60 worked examples reviewed
- [x] Framework selection, reasoning, failure modes, and corrections reviewed for every skill
- [x] Four calculation helpers and documented JSON interfaces complete
- [x] Calculation and adversarial tests pass
- [x] Meeting memory compatibility and recurring-series scenarios pass
- [x] Two integrated walkthroughs reconcile across artifacts
- [x] Catalog, installation, glossary, authoring guidance, changelog complete
- [x] Portable validation and GitHub Actions pass
- [x] Private repository created and remote commit verified
- [x] Final requirement audit complete

## Truthfulness

This is a newly authored library. Synthetic scenario testing demonstrates specified behavior under those scenarios; it does not establish field use, organizational adoption, or general reliability. Do not advertise the library as battle-tested until documented field trials support that claim.

## Release evidence — 16 September 2026

The implementation commit is `3b2fb670ea755188dfd9e82cb085d2cb93ba4c5f`. Its remote `main` SHA matched the local commit, and GitHub reported `isPrivate: true` for [the repository](https://github.com/nghiemthai1/project-manager-skills). The initial [CI run](https://github.com/nghiemthai1/project-manager-skills/actions/runs/35110014245) passed all four Windows/Ubuntu × Python 3.11/3.14 jobs, including structural validation and all 30 automated tests. This evidence entry is a subsequent documentation-only update.

| Requirement | Inspected evidence |
|---|---|
| 30 complete skill packages | [Generated catalog](../catalog/README.md), validated metadata and exact filesystem inventory; 18 component, 6 interactive, 6 workflow packages |
| Framework reasoning and anti-patterns | [Teaching review](../evals/teaching-review.md) covers all 30 entrypoints and 60 examples; [follow-up](../evals/reruns/integrated-rerun-review.md) resolves the identified RAG inconsistency |
| 30 usable templates | Maintainer read all 30 `template.md` files; templates distinguish evidence, proposals, authority and unknowns according to artifact type |
| Four portable helpers | [Calculation tests](../tests/test_calculations.py), copied-script isolated-mode tests in [evidence tests](../tests/test_evidence.py), four-platform/version CI matrix |
| Behavioral exercises | All 30 raw requests and actual artifacts in [evals](../evals/README.md); first-pass failures, corrected reruns, editorial correction and review limitations retained |
| OKF meeting memory | [Two-meeting bundle](../evals/outputs/meeting-bundle/index.md), source-turn/order and metadata/link regression checks; arbitrary legacy metadata preservation is an instruction contract, not an exhaustive automated migration test |
| Coherent lifecycle examples | [Relay](walkthroughs/software.md) and [Northstar](walkthroughs/migration.md) distinguish targets, forecasts, baselines and actuals; reserve bridges and additional closure exhibits reconcile |
| Installation and maintenance | [Installation](INSTALLATION.md), [Authoring](AUTHORING.md), [Frameworks](FRAMEWORKS.md), [Glossary](GLOSSARY.md), [Changelog](../CHANGELOG.md), local-link validation |
| Private GitHub delivery | Private visibility verified through GitHub API; local/remote implementation commit match; green CI linked above |
| Scope and preservation | Markdown library plus optional offline helpers, no application or tracker integration. Git index inspection confirms original root meeting folder, TLDR documents, virtual environment and working scratch files are excluded |

The final audit found no unresolved implementation deliverable. The evidence supports a reviewed and scenario-tested initial release, with the [validation limits](VALIDATION.md) intact. Production field history is not claimed.
