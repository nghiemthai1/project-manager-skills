# Validation record

This newly authored library has numerical regression tests and independent synthetic executions. It has no recorded production field trials. “Battle-tested” would overstate the evidence.

## Reproduce the checks

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

The structural validator checks the exact 30-package inventory, metadata and interface fields, required sections and support files, catalog drift, and repository-local Markdown links. It does not grade teaching quality or verify external links. GitHub Actions runs the same checks on Windows and Ubuntu with Python 3.11 and 3.14.

Local release check: all 30 automated tests pass on Windows. All four Windows/Ubuntu and Python 3.11/3.14 CI jobs also passed; the commit and run are recorded in the [release acceptance ledger](IMPLEMENTATION.md).

## Calculation evidence

The calculation suite covers known results, invalid/missing/unknown inputs, zero denominators, nonfinite values, extreme numeric values, duplicate identifiers, dependency cycles, disconnected work, multiple critical paths, and command-line error behavior. It checks 80 generated six-node DAGs against independent source-to-sink path enumeration and 100 estimation bound cases. Helpers are run from an unrelated working directory; an additional isolation test copies each script and executes it with Python isolated mode.

Earned value tests distinguish monetary schedule variance from elapsed time and demonstrate that SPI=1 at completion does not prove on-time delivery. Capacity tests retain individual overload despite another person's spare capacity. Numeric underflow in earned-value ratios was corrected to return a controlled input error.

## Artifact execution

All 30 skills were exercised against fictional challenge inputs independently of their authored worked examples. Inputs and actual outputs are retained in [evals](../evals/README.md). The four pilot cases were read against their raw requests: the revised status reports failed gates and unchanged baseline; the dependency map declines an unsupported project-delay claim; estimation declines a confidence date without a probability model; meeting memory retains all eight quoted turns, unknown speakers, objections, no invented Friday commitment, and explicit sponsor non-approval.

The first status output failed the requested one-screen length. The skill now specifies approximately 150–250 words and at most three material asks for that request. The independent rerun produced a concise report; both versions remain available. This is a corrected failure, not an unbroken perfect score.

The meeting bundle is a two-meeting synthetic exercise, not an exhaustive OKF conformance certification. Regression checks verify literal source preservation, turn order, selected metadata, evidence-link resolution and the current-state distinction. Preservation of arbitrary legacy custom metadata remains an instruction-level contract; no universal migration or parser is shipped.

## Teaching and scenario consistency

Each package contains framework fit and limits, a usable template, two fictional worked artifacts, and recognizable failures with repairs. The Relay and Northstar walkthroughs preserve baseline history, separate reserve from performance budget, hold failed readiness gates, and identify additional fictional financial/handover exhibits used to support closure. The shorter skill examples correctly leave costs unknown where those exhibits were not supplied.

## Review findings and corrections

Read the retained [planning/control review](../evals/core-review.md), [delivery/closure review](../evals/delivery-review.md), and [teaching review](../evals/teaching-review.md). Reviewers inspected all 30 entrypoints and 60 examples; the maintainer separately read all 30 templates. Some reviewers had authored the outputs they reviewed, as disclosed in the reports.

The review found case contamination in a closure lesson, unconfirmed receiver assignments, imprecise hold/baseline labels, and an integrated plan that put full handover before cutover. Affected instructions were strengthened and affected cases rerun; first passes remain retained. The [three-case rerun review](../evals/reruns/rerun-review.md) records corrected closure, readiness, and handover outputs with its self-review limitations. The [integrated-plan follow-up](../evals/reruns/integrated-rerun-review.md) records the successful sequencing rerun and a remaining receiver-label error corrected by the maintainer, with the unedited artifact preserved. The software status example also used amber while recovery feasibility was unknown under its own stated convention; it now uses provisional red for the required funding intervention. These findings are part of the evidence, not hidden by the final checks.

## Limits and field validation

One challenge per skill is narrow coverage. Same-family model reviewers may share blind spots. Future model behavior, installation discovery in every client, real recordings, contractual/legal adequacy, organization-specific approval rules, resource-leveled schedules, and real project outcomes are not established by these checks. Client installation instructions are documented, not a claim of live testing across clients.

Before relying on this library in an organization, trial it on anonymized completed projects, compare generated decisions to source records with experienced project managers, and record corrections and outcomes. Add new counterexamples when a skill fails. Do not convert a passing structural check into a general reliability claim.
