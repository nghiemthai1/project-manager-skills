# Contributing

Help project managers make better decisions. Useful contributions clarify a framework, repair a misleading instruction, improve an artifact, or add a missing project-management skill.

## Propose a change

Open an issue for a substantial new skill or change in scope. Explain the project decision, the gap in the current library, and the proposed outcome. For a small correction, submit a focused pull request directly.

For a bug, include the affected skill or helper, the smallest sanitized input, the observed result, and the expected result. Keep client data, credentials, and private meeting records out of issues and pull requests.

## Work in the right place

Fork the repository and create a branch. Edit canonical packages under `skills/`. Read [Authoring](docs/AUTHORING.md) before changing a skill and use [the catalog](catalog/README.md) to check for overlap.

Keep the purpose, framework, application, and failure modes in the skill guide. Link optional worked material once from its Examples section. Store demonstration inputs and outputs in `examples/`, with supporting files in `examples/assets/`. Reserve package-level `assets/` for reusable production resources.

Preserve project facts, unknowns, and source references. Keep targets, forecasts, approved baselines, acceptance, and authority distinct. Label fictional data. Keep optional helpers offline, standalone, and compatible with Python 3.11+ using the standard library.

For a new skill, update `catalog/library.json`, add relevant trigger cases in `evals/trigger-cases.json`, and include the package resources required by the authoring guide. Record sources and licenses for adapted material.

## Check the change

From the repository root:

```sh
python -m pip install -r requirements-dev.txt
python scripts/validate.py
python scripts/check-skill-metadata.py
python scripts/check-skill-triggers.py
python -m unittest discover -s tests -v
```

If skill metadata or the catalog changes, run `python scripts/validate.py --build-catalog` before the checks. For packaging changes, also run `python scripts/build_codex.py` and inspect the extracted files.

Review the resulting artifact against its input. For calculations, verify meaningful boundaries and invariants. For visual changes, inspect the rendered output and test affected controls and exports. Structural checks alone do not establish teaching quality or project correctness.

## Submit the pull request

Describe the problem, the resulting behavior, and the checks performed. Include limitations or unverified behavior where relevant. Keep unrelated cleanup separate. Do not describe a change as field-tested without recorded evidence.

AI-assisted contributions follow the same standard. Review generated prose, calculations, source claims, and licensing before submitting. Maintainers review scope, correctness, clarity, and attribution before merging.

## Contribution license

Submit only material you have permission to contribute. Your contributions use the license applying to the affected files: MIT for original material, and CC BY-NC-SA 4.0 for the six Dean-derived packages. Existing third-party notices take precedence. Preserve attribution, license files, and change notices. See [Licensing](LICENSING.md) and [Third-party material](THIRD_PARTY_NOTICES.md).
