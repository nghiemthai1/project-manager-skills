# Install selected skills

## Read without installing

Open a skill folder and read `SKILL.md`. Give its instructions and your project context to an assistant that accepts Markdown. Supporting examples and templates are linked from the entrypoint. A bare Markdown chat does not automatically gain access to local helper scripts.

## Codex ZIP quick setup

1. Open the [latest release](https://github.com/nghiemthai1/project-manager-skills/releases/latest) while signed in with repository access.
2. Download [pm-skills-codex.zip](https://github.com/nghiemthai1/project-manager-skills/releases/latest/download/pm-skills-codex.zip).
3. Extract its contents into your project root. If `AGENTS.md` or a same-named skill already exists, extract to a temporary folder first and merge deliberately.
4. Confirm this layout, including the hidden `.agents` folder:

```text
.agents/
  skills/
    project-charter/
      SKILL.md
    ...
AGENTS.md
```

5. Open Codex in that project and ask: “Use the project-charter skill to turn these notes into a draft charter.”

The ZIP contains all 42 complete skill folders, including templates, examples and optional helpers. Its `AGENTS.md` provides usage guidance for your project; repository maintainer instructions stay in the source repository. Downloading alone does not install anything: extraction places the files in the discovery location.

For an authenticated CLI download:

```sh
gh release download --repo nghiemthai1/project-manager-skills --pattern pm-skills-codex.zip
```

## Codex manual setup

Copy the selected skill folder from the extracted Codex ZIP, including its supporting files, into your project's `.agents/skills/` directory or your user-level `~/.agents/skills/` directory. Keep the skill folder name unchanged. If working from a source checkout, build the ZIP first: the source headers use flat fields for readable GitHub previews, and the builder normalizes extended fields into Codex metadata. OpenAI documents the skill structure and discovery behavior in [Build skills](https://learn.chatgpt.com/docs/build-skills).

For example, the destination for a selected status-report skill is `.agents/skills/status-report/SKILL.md`. The package also includes optional `agents/openai.yaml` display metadata. Follow your client's current refresh/restart behavior if a newly added skill is not visible.

## Claude Code

Copy the selected skill folder into the project's `.claude/skills/` directory or the user's `~/.claude/skills/` directory. Keep `SKILL.md`, templates, references, examples, and optional scripts together. See [Claude Code skills documentation](https://code.claude.com/docs/en/skills) for current client behavior.

## Copy safely

Do not overwrite a different installed skill with the same name without comparing it first. Install only the skills you need, or copy all 42 if the full workflow is useful. No global configuration changes or live service credentials are required by this library.

The canonical source remains `skills/` in this repository. Installed copies will not update automatically when this repository changes. Record the source commit for reproducibility, then replace selected copies deliberately after review.

## Optional Python helpers

Python 3.11+ is required only to run calculation helpers and visual renderers. They use the standard library and make no network requests. From a skill folder, run its helper with `--help` or `--demo`. From elsewhere, pass the helper's absolute path. Each helper contract documents the JSON fields and limitations.

Repository maintainers also install the pinned YAML parser in `requirements-dev.txt` for validation and package building. That dependency is not needed for the operational helpers or reading the installed skills.

## Scope of compatibility

The Codex install packages use the metadata layout of the [Agent Skills specification](https://agentskills.io/specification). Source Markdown uses Dean-style flat authoring fields so GitHub renders separate readable rows and native lists. The build preserves every field value and the complete skill body while normalizing the install header. Metadata and standalone helper invocation are checked in this repository. A full live-client acceptance test in every supported assistant is not claimed; client-specific installation behavior follows its current official documentation.

## Build a release package

Install `requirements-dev.txt`, then run `python scripts/build_codex.py`. It writes `dist/codex/codex-project-manager-skills.zip` and the identical download alias `dist/codex/pm-skills-codex.zip`. Generated archives are excluded from source commits. Packaging tests compare every resource byte after text normalization, verify that transformed SKILL.md headers retain all field values and unchanged bodies, and execute helpers from the extracted archive.

The release workflow validates and packages on pull requests and main pushes. Pushing a new `v*` tag publishes both ZIPs as GitHub Release assets after the checks pass. Use a new version tag for each release; the README's latest-release link stays the same.

Archive bytes repeat within the same Python/compression runtime. Different compression libraries can produce different ZIP bytes for identical extracted files. Verify the digest published for the release asset; the v2 download audit separately compares every extracted payload byte with canonical source.
