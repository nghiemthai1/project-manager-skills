# Visual artifacts release 2.1

The RACI matrix and Gantt chart now have prominent README links and runnable offline artifacts for both fictional projects. Four interactive HTML files include full SVG, JSON and CSV downloads. Two standard-library Python renderers make the same outputs from new project data; guides explain inputs, limitations and actual inspection.

This revision also adds 33 package-local visual contracts, an explicit routing decision for all 42 skills, and eight rendered graphical companions with editable sources. The library still contains 42 skills, 42 templates and 84 primary worked examples. There are now six standalone helpers: four calculators and two renderers. No app, server or live project integration is required.

The installed global Gantt skill served as a capability reference and was not modified. Its mapped file hashes, mobile foundation, limitations and original implementation boundary are recorded in the [upgrade record](VISUAL-UPGRADE.md). Existing Dean adaptation notices and licenses remain in their packages.

## Validation

Local Windows validation: 42 automated tests, 42 metadata/trigger-readiness checks, repository links/catalog, and both core skill-creator validations pass. Browser tests cover the four interactive artifacts across desktop/portrait/landscape, native keyboard details, search/reset, role focus, Gantt scale/comparison controls, exact full-export equality and eight static SVG boundaries. Independent fictional RACI/Gantt executions and retained defects/corrections are in the [visual evaluation](../evals/visual/README.md).

No large-project performance guarantee, live client installation, screen-reader certification, physical-phone testing or field-tested claim is made. Gantt is a date-only snapshot reader, not a scheduling engine or editor. Missing source evidence remains unknown.

## Distribution

The private release will retain both `pm-skills-codex.zip` and `codex-project-manager-skills.zip`. Extracting adds `.agents/skills` and project-facing `AGENTS.md`; merge existing project instructions as explained in [installation](INSTALLATION.md). HTML is now part of the packaged text payload. Payload verification and hosted CI references will be appended after the release exists.

## Verified release candidate

Commit `25c5ab0e39653986f2ddd0496412db0c22cc9e06` passes [all four hosted jobs](https://github.com/nghiemthai1/project-manager-skills/actions/runs/35141626680). The [local candidate report](../evals/visual/release-candidate.json) records the archive hash, exact payload comparison and six extracted helper executions. The first Python 3.11 run exposed an f-string parsing incompatibility in RACI search; the correction preserves identical generated artifacts and passes the full matrix.

Automatic approval review rejected main-branch promotion and publication of v2.1.0 pending explicit owner approval. The review branch and local ZIP are complete; no main promotion or release tag was performed. Downloading the existing latest GitHub release still retrieves v2.0.0 until publication is approved and completes.
