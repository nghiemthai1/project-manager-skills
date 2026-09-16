# Writing a skill that improves judgment

The reader should finish with an artifact they can use and a better explanation of the decision behind it. An instruction such as "create a risk register" accomplishes neither without defining what belongs in that register and what changes after someone reads it.

## Teach the decision

Start with the job the reader needs to do. Name the framework only after showing which uncertainty it resolves. Define unfamiliar terms at their first meaningful use. Explain what the framework cannot establish.

For example, a dependency's expected delivery two days before its needed-by date gives two days of local delivery margin. It does not prove two days of total float in the integrated schedule. The reader should learn which additional schedule information is required before making that second claim.

## Standard structure

Each `SKILL.md` has Purpose, Input, Key Concepts, Application, Examples, Common Pitfalls, and References sections. Keep the essential teaching in the entrypoint. Put substantial worked artifacts and specialized procedures in linked files, with a sentence explaining when to open each one.

Use `name` and `description` in YAML frontmatter. Nest string-valued `type`, `domain`, and `version` inside `metadata`. Allowed types are component, interactive, and workflow. A component creates a bounded artifact; an interactive skill selects a course of action; a workflow coordinates a sequence of artifacts and decisions.

Every skill includes a template and examples for the software release and IT migration described in [the scenario guide](SCENARIOS.md). An interactive template captures questions, evidence, options, and a recommendation. A workflow template captures phases, entry conditions, handoffs, and exit evidence. Do not label a blank form a worked example.

## Writing conventions

- Use short active sentences and specific nouns. Keep reasoning that explains a consequential choice.
- Use tables for comparisons and artifact fields, ordered lists for sequences, and prose for explanations.
- Say when a method fits, when to use another method, and what information would change the recommendation.
- Show a flawed artifact, explain its practical consequence, and repair it with evidence.
- Give failure modes recognizable symptoms. Avoid lists of generic warnings repeated across unrelated skills.
- Distinguish guidance from rules. State the reason for a mandatory gate, such as authorization to accept residual release risk.
- Identify fictional example values as examples. A sample RAG threshold or reserve is not an industry standard.
- Avoid unverified claims of certification, production readiness, time saved, or field adoption.

## Interaction

Read the user's supplied material before asking questions. Missing information is not always a reason to stop: produce a useful partial draft with unknowns when possible. Ask only when the answer changes the artifact or recommendation. In guided mode ask one focused question at a time, normally no more than three to five material questions. Offer distinct options with tradeoffs and accept freeform answers.

Separate requests to draft from authority to approve, send, schedule, purchase, or update a live system. Preserve approvals already given; do not invent an extra approval loop for ordinary drafting.

## Evidence and portable artifacts

Facts need an identifiable input, dated record, or calculation. Assumptions need an owner for validation and a consequence if wrong. Forecasts need an as-of date and method. An approved baseline needs the decision record that established it. Preserve IDs and previous baselines when updating artifacts.

Use fictional data only in examples. An agent running a skill must never carry example people, amounts, thresholds, or approvals into a real project as facts.

Each skill folder must work when copied independently. Links to other skills are recommendations, not hidden runtime dependencies. If an adjacent skill is unavailable, describe the required handoff artifact in plain language. Put optional executable helpers within the owning skill and avoid network access.

## Review before merging

Run structural validation and calculation tests. Then review the actual artifact against the user's purpose. A document with all the right headings can still recommend the wrong action. Use counterexamples: contradictory status data, an unapproved date, unavailable capacity, a disputed decision, and a failed release gate.

Keep original text and code original. Link technical methods for verification without copying explanatory passages from external publications. Before adding third-party material later, inspect its license and retain any required notices.
