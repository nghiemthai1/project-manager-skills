# Install selected skills

## Read without installing

Open a skill folder and read `SKILL.md`. Give its instructions and your project context to an assistant that accepts Markdown. Supporting examples and templates are linked from the entrypoint. A bare Markdown chat does not automatically gain access to local helper scripts.

## Codex

Copy the selected skill folder, including its supporting files, into your project's `.agents/skills/` directory or your user-level `~/.agents/skills/` directory. Keep the skill folder name unchanged. OpenAI documents the skill structure and discovery behavior in [Build skills](https://learn.chatgpt.com/docs/build-skills).

For example, the destination for a selected status-report skill is `.agents/skills/status-report/SKILL.md`. The package also includes optional `agents/openai.yaml` display metadata. Follow your client's current refresh/restart behavior if a newly added skill is not visible.

## Claude Code

Copy the selected skill folder into the project's `.claude/skills/` directory or the user's `~/.claude/skills/` directory. Keep `SKILL.md`, templates, references, examples, and optional scripts together. See [Claude Code skills documentation](https://code.claude.com/docs/en/skills) for current client behavior.

## Copy safely

Do not overwrite a different installed skill with the same name without comparing it first. Install only the skills you need, or copy all 30 if the full workflow is useful. No global configuration changes or live service credentials are required by this library.

The canonical source remains `skills/` in this repository. Installed copies will not update automatically when this repository changes. Record the source commit for reproducibility, then replace selected copies deliberately after review.

## Optional Python helpers

Python 3.11+ is required only to run calculation helpers. They use the standard library and make no network requests. From a skill folder, run its helper with `--help` or `--demo`. From elsewhere, pass the helper's absolute path. Each helper contract documents the JSON fields and limitations.

Repository maintainers also install the pinned YAML parser in `requirements-dev.txt` for validation. That dependency is not needed for the operational helpers.

## Scope of compatibility

The packages follow the [Agent Skills specification](https://agentskills.io/specification). Metadata and standalone helper invocation are checked in this repository. A full live-client acceptance test in every supported assistant is not claimed; client-specific installation behavior follows its current official documentation.
