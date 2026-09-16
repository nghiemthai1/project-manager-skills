# Version 2 release acceptance

Released privately as [v2.0.0](https://github.com/nghiemthai1/project-manager-skills/releases/tag/v2.0.0) on 16 September 2026. The release tag resolves to `4e95fbcdbbc1d947aac0b5adc71e9c290962f146`. Later documentation records the verification; it does not change the tagged skill payload.

| Requirement | Evidence and result |
|---|---|
| Deepen every original skill | All 30 original entrypoints, templates and paired examples revised; [inventory](../catalog/library.json), [authoring criteria](AUTHORING.md) and [behavior review](../evals/v2/README.md) retain the scope and substantive checks |
| Add missing project-manager jobs | 12 additions bring the reviewed inventory to 42; each has a guide, template, two examples and interface metadata |
| Follow Dean's skill design method | Seven-section structure, component/interactive/workflow distinctions, adaptive input use, decision branches, framework limits and named failure/repair analysis; all 42 authoring checks pass |
| Closely adapt overlapping jobs | Six pinned-source adaptations compared and licensed; [source review](../evals/v2/SOURCE-REVIEW.md), [manifest](../catalog/upstream-sources.json), per-package SOURCE.md/LICENSE.md |
| Framework visibility | README and catalog have categorized Skill / Focus / Framework tables for all 42 entries |
| Concrete RACI and Gantt artifacts | Filled software/migration matrices; editable Mermaid and rendered SVG charts; [artifact/render review](../evals/v2/controls/README.md) retains rendering correction and resource assumptions |
| Preserve meeting format/history | OKF v0.2 guides/references, ordered ledgers, unknown metadata and stable slugs; [new fixture audit](../evals/v2/meeting-a/maintainer-review.json) plus existing automated evidence tests |
| Behavior and calculations | 42 distinct fictional skill cases, three targeted identifier reruns, 42 unique description-routing requests; 32 numerical/evidence/packaging tests, with limitations and earlier failed outputs retained |
| Portable checks | [Branch CI](https://github.com/nghiemthai1/project-manager-skills/actions/runs/35134925824) and [tag CI](https://github.com/nghiemthai1/project-manager-skills/actions/runs/35135128293): Ubuntu/Windows × Python 3.11/3.14 all passed |
| Dean-style Codex download | [Release build](https://github.com/nghiemthai1/project-manager-skills/actions/runs/35135128309) published pm-skills-codex.zip plus identical codex-project-manager-skills.zip; payload is root AGENTS.md and .agents/skills |
| Private delivery and actual download | Repository isPrivate=true verified through GitHub; release is published, not draft/prerelease; both archives downloaded and checked |
| No app or personal-file changes shipped | Payload contains skills/resources only; root personal meeting folder, TLDR learning files, scratch work, runtime and generated archives remain outside source commits |

## Downloaded package

[Full payload report](../evals/v2/release-payload.json): **244 entries, 42 skills, 42 templates, 84 worked examples, 421,070 bytes**. Every uncompressed file matched canonical source after documented text line-ending normalization. Both release aliases are byte-identical, CRC checks passed and all four extracted helpers ran successfully in isolated Python mode. The RACI/Gantt files and all six adaptation licenses/source notices are included.

SHA-256 of both downloaded release aliases:

```text
2394e64756e027a97e9ffa1f98233779c8283baa05c79759d47ee4e614ab09a6
```

The local Windows ZIP and hosted Linux ZIP had identical uncompressed contents but different compressed sizes in 226 entries. Local zlib-ng and hosted compression runtimes differ. The published digest above identifies the downloaded release; byte reproducibility across different compression implementations is not claimed. Repeat builds within one runtime and alias equality are tested.

## Limits

The behavioral evidence is synthetic and largely same-family, with retained context disclosed; routing used a fresh description-only evaluator and author-curated requests. One case per skill is not exhaustive branch coverage. No production field trials, live installation in every assistant, legal sufficiency of commercial artifacts or guarantees about real project outcomes are claimed. The package is ready to use with supplied project evidence and review, with those limits visible.
