# Independent extraction passes

When delegated extraction is authorized and available, give every specialist the original ordered ledger. Otherwise perform the same passes sequentially, checking each against the source. Do not give specialists one another's output. Add the existing relevant concepts only for recurring-series comparison.

## Detail

Extract facts, numbers, dates, examples, caveats, assumptions, constraints, dependencies, requirements, references, and topic transitions. Cite turn IDs. Do not summarize.

## Decisions

Extract proposals, decisions, rationale, objections, alternatives, rejected options, thresholds, changes of mind, and unresolved disagreements. Distinguish discussion from commitment. Cite turn IDs.

## Actions

Extract actions, owners, deadlines, dependencies, status, questions, risks, and follow-ups. Use `Unassigned` or `Unspecified` when absent. Cite turn IDs.

## Graph

Identify canonical entities and explicit relationships. Suggest merges with existing concepts, but preserve distinct concepts when identity is uncertain. Cite turn IDs.

## Reconcile

Give the reconciler the ledger, speaker resolutions, all specialist results, and relevant existing concepts. It must:

1. Verify every claim against the ledger.
2. Resolve conflicts from source evidence; otherwise retain the conflict.
3. Deduplicate without losing qualifiers or history.
4. Run a completeness pass for easy-to-lose details.
5. Produce meeting concepts and, when applicable, a series delta.

Parallelism is for independent attention, not majority vote.
