# Metadata presentation revision

The owner supplied screenshots contrasting Dean Peters’s flat GitHub frontmatter table with this repository’s nested metadata table. All 42 source headers now use separate rows in the order name, argument-hint, description, intent, type, theme, best_for, scenarios and estimated_time, followed by technical and attribution fields. Lists are native YAML sequences instead of JSON strings. The requested visual structure uses GitHub’s own rendering; no custom CSS or application is added.

All existing metadata values, descriptions and skill bodies were compared with the previous branch commit and preserved. Package-local source notices record the presentation change for the six adaptations. The catalog remains consistent with the unchanged skill types.

The Codex builder normalizes only SKILL.md frontmatter into supported install fields plus string-valued extended metadata. It preserves all field values and the entire Markdown body. All other resources retain the previous byte-preservation/text-normalization behavior. Manual Codex installation now directs readers to the generated ZIP rather than copying the flat authoring headers directly.

Local validation: 44 automated tests pass, including semantic comparisons of all 42 converted install headers, body equality, exact remaining payloads, isolated helpers, flat-layout checks and rejection of string-encoded lists. Both authoring checkers and catalog/link validation pass. The [conversion report](checks.json) also records all 42 extracted packages passing the local Codex skill-creator validator and the rebuilt local candidate hash. Earlier visual candidate hashes remain historical snapshots; this metadata conversion creates a new candidate.

This revision stays on the existing review branch and draft PR. Main-branch promotion and release publication still await the owner approval requested earlier; the presentation request does not grant that approval.
