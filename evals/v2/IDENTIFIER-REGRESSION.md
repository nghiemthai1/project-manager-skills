# Identifier preservation defect and regression

Date: 16 September 2026. This record corrects the earlier broad statement that every inspected artifact had no material execution failure. Original evaluation outputs remain unchanged.

## Observed failure

One evaluator applied a global PowerShell prose-spacing replacement to Markdown:

```powershell
$content -replace '([a-z])(?=[0-9])','$1 '
```

PowerShell's replacement matching was case-insensitive. The transformation altered supplied literal identifiers even though the skills required stable references:

| Original execution | Supplied literal | Altered output | Consequence |
|---|---|---|---|
| [Acceptance traceability](planning-a/acceptance-and-traceability.md) | `BC-R7`, `v1`, `v2` | `BC-R 7`, `v 1`, `v 2` | Requirement/version references corrupted; incorrect claim they were preserved |
| [Status report](decisions-a/status-report.md) and its appendix | `VB1` | `VB 1` | Baseline reference corrupted |
| [Decision log](decisions-a/decision-log.md) | `V-D1` | `V-D 1` | Source decision ID corrupted despite otherwise correct history reasoning |

The evaluator's retained execution-history audit confirmed the formatter on 16 Markdown files across controls-additions, planning-a, planning-c, coordination-a and decisions-a. It also changed generated IDs/version labels in the quality-plan and kickoff outputs, and path prose in the planning-a log. Actual filesystem paths and JSON helper inputs were not renamed. The original controls RACI/Gantt run had no such formatter call in the retained history and its checked IDs remained intact. No claim of an exhaustive audit of all earlier v1 evaluations is made. Another agent authored the advisors run; absence of matching corruption in a targeted scan is not proof of its execution history.

This is an evaluator execution failure, not an ambiguous input. The maintainer initially missed it while checking reasoning and calculations. Treat the three affected original executions as failed for traceability, not as passes because their substantive recommendations were sound.

## Correction and rerun

Authoring instructions, the packaged consumer AGENTS.md, and the affected acceptance/scope/status/decision guides now explicitly require exact case, punctuation and spacing for supplied identifiers, versions, paths and URLs. They forbid global prose-formatting substitutions across literal data and require comparison against the input. Original raw outputs were retained instead of silently repaired.

The same raw acceptance, status and decision cases were executed again with the revised guides. The maintainer read all three saved artifacts and checked both literal references and the decision logic:

- [Acceptance rerun](identifier-retest/acceptance-and-traceability.md): `BC-R7`, `v1`, `v2` preserved; prior sample pass stays historical and current failures/absent acceptance remain visible.
- [Status rerun](identifier-retest/status-report.md): `VB1` preserved; 223-word executive report, failed required gate, conditional 133.33k forecast and 23.33k reserve-inclusive gap retained.
- [Decision rerun](identifier-retest/decision-log.md): `V-D1` preserved; immediate 15k additional funding approval does not change the date or restore requirement, and the 4 December forecast is not approval.

Logs: [acceptance/status](identifier-retest/execution-log.md) and [decision](identifier-retest/decision-execution-log.md). These are targeted non-blind regressions with retained evaluator context and awareness of the identifier issue. They support the narrow correction; they do not establish fresh-context or field reliability. Newly generated labels in the earlier raw artifacts remain visible as originally produced.
