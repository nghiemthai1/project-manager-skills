# Maintainer instructions

This repository teaches software and IT project management through skills, worked artifacts, and explicit failure analysis. Read `docs/AUTHORING.md` before changing skill content. Preserve the human learning value along with actionable agent instructions.

Canonical packages are in `skills/`. Do not edit installed copies or unrelated personal files. Keep the existing root meeting-knowledge-graph folder and TLDR learning documents outside commits; the adapted package under skills is the maintained library version.

Use supplied project facts, state unknowns, and preserve distinctions between targets, forecasts, baselines, acceptance, and authority. Do not invent evidence, commitments, or approvals. Synthetic examples must stay labeled fictional.

Run `python scripts/validate.py` and `python -m unittest discover -s tests -v` after relevant changes. If skill metadata changes, rebuild the catalog with `python scripts/validate.py --build-catalog`. Structural checks do not substitute for reading artifacts or verifying calculations and behavior.

Preserve OKF v0.2 meeting memory semantics and unknown metadata. Do not rewrite earlier meeting ledgers to match a later decision. Keep operational helpers standalone, offline, and Python 3.11+ standard library only.

Do not describe new content as field-tested or battle-tested without recorded field evidence. Update validation claims and coverage when behavior changes. The owner has authorized public publication. Keep credentials, client data, and excluded personal workspace files outside commits. Preserve the content and code licenses described in LICENSING.md.

For the requested v2 revision, follow docs/REVISION-2-PLAN.md and the pinned Dean Peters authoring sources. Close adaptations must retain per-package SOURCE.md and LICENSE.md; update catalog/upstream-sources.json. Do not call adapted prose original.
