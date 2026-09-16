# Visual revision evidence

All projects and challenges here are fictional. No live project systems or installed global skill files were changed. The parent read the owner-installed Gantt guide, its six references and mobile foundation; [hashes](../../catalog/visual-reference.json) identify that reference without creating a runtime dependency.

## Independent executions

One independent evaluator executed two bounded tasks after reading the relevant skill. The [RACI report](original-raci/REPORT.md) and [Gantt report](original-gantt/REPORT.md) retain the original inputs, artifacts and observations, including defects. These are synthetic behavior tests, not field use. The evaluator shared this conversation's broader environment but was given fresh task inputs without the parent's intended answers.

The RACI task tested confirmed A/R, unknown authority, multiple A, absent R and a clean row. Its audit preserved every letter and evidence reference. Five malformed inputs failed before output, and hostile text was escaped. The original report exposed doubled Windows CSV carriage returns and missing role summaries/documentation. These are fixed: writing disables newline translation, role totals/unresolved counts and renderer instructions are included, and role names are searchable.

The Gantt task preserved leap-day/holiday dates, a partial actual, an undated milestone, a violated FS-zero link and an external SS working-day-lag relationship without rescheduling. It also exercised cycles, empty/partial and long-label inputs. The original outputs exposed long-owner row overlap and a null-calendar crash. Both are fixed and covered by regression tests. The [corrected outputs](corrected/) are new files; failed originals were not rewritten to make the earlier run look successful.

## Browser and artifact checks

`node scripts/check_visuals.cjs` uses separately installed development-only Puppeteer and Chrome. It checks both scenarios for Gantt and RACI at 1440×1000, 390×844 and 844×390: no page overflow, working search/reset, native keyboard detail selection, RACI role focus, Gantt scale/comparison controls, and exact decoded export equality against source files. The challenge findings filter hides clean H-8. Eight companion SVGs are checked for text outside the canvas. The [browser report](browser/browser-checks.json) records the actual browser and assertions; viewport screenshots are retained beside it. These are browser assertions and visual inspection, not an accessibility certification.

The parent inspected the generated desktop, portrait and landscape artifacts. An initial RACI landscape overflow was fixed by explicitly positioning visually hidden text. The WBS graphic was changed to a single-level child list with a shared parent spine so lower items do not appear to be children of their peers. Static companions were checked against their source examples for units, cutoff and uncertainty.

[Scale generation data](corrected/scale-generation.json) records 200-row synthetic generation size/time on this Windows host. Only small real browser views are used for acceptance; no virtualization or large-project responsiveness claim follows from the generation probe.

## Automated coverage

Ten visual regression tests join the existing 32 tests. They check source/output consistency, exact identifiers and partial dates, typed timing without mutation, cycles/missing endpoints, invalid calendars/dates/progress, long-owner geometry, RACI confirmation semantics, hostile text and CSV formula protection, and isolated CLI outputs including Windows line endings. Packaging runs all six extracted helpers and compares all payload bytes after documented text normalization. A Windows console-encoding failure found during packaging was fixed by explicitly emitting UTF-8.

Run `python scripts/validate.py --build-catalog`, both authoring check scripts, and `python -m unittest discover -s tests -v`. Automated routing checks verify metadata and curated case availability; this revision does not claim another full model-routing run across all 42 packages.

## Remaining limits

No live Codex-client installation run, assistive-technology certification, physical-phone test, vendor import integration, editable schedule engine or user field trial is claimed. HTML runs offline; SVG and JSON remain usable without JavaScript. Browser print is available but no generated PDF or PNG delivery is claimed by the renderer.

Hosted CI passed all four OS/Python combinations after a Python 3.11 f-string compatibility correction: [run](https://github.com/nghiemthai1/project-manager-skills/actions/runs/35141626680). The [local release candidate](release-candidate.json) was rebuilt after that fix and checked byte-for-byte against canonical payloads. Main promotion and release publication remain subject to the owner approval requested after automatic approval review rejected them.
