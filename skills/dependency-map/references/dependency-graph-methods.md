# Dependency graph methods

This reference explains which conclusions each dependency view can support. It draws conceptual inspiration from the [borghei dependency-map package](https://github.com/borghei/claude-skills/tree/main/project-management/execution/dependency-map) and independently applies this repository's stricter evidence semantics.

## Normalize the interface agreement

The minimum coordination record identifies the consumer, provider, result, needed-by date, current expected delivery and status. Add the usable boundary, owners, requested and committed dates, commitment evidence, acceptance state, source and as-of date. These additions prevent common category errors:

- a receiver request is not a provider commitment;
- a provider forecast is not receiver acceptance;
- delivered is not necessarily usable;
- a coordinator is not automatically the technical or contractual authority.

Store one direction in the graph: provider → receiver. The receiver's need remains a field on that edge.

## Use transparent coordination ordering

Sort the review queue using fields the team can inspect:

1. blocked delivery or failed verification;
2. negative local margin where needed-by and forecast are comparable;
3. explicitly at-risk handoffs;
4. unknown provider, owner, usable criteria, date or authority;
5. watch items and accepted items.

This is a review rule, not a risk score. Change it when project tolerances require a different order and document that change.

## Separate local margin from CPM

`local delivery margin = needed-by − forecast` answers whether the current handoff forecast precedes the receiver's stated need. It does not use the complete activity network, durations, constraints, calendars, remaining work or resources. It is therefore not total float, free float, a critical path or a project-finish prediction.

Show CPM results only when an identified scheduling method supplies an integrated network and the result is imported as method-labeled analysis. Preserve the dependency register even then: CPM logic does not prove that a delivered interface is usable or accepted.

## Pair the graph with a DSM

A directed graph makes paths, fan-in, fan-out and cycles legible. A dependency structure matrix places providers on rows and receivers on columns; a cell can show the number of handoffs for that pair. Dense or repeated cells identify coordination seams worth reviewing. Counts do not measure effort, risk or delay unless a separate, valid measure supports that conclusion.

Use the DSM to ask whether interface boundaries, team topology, shared services or governance create repeated coordination costs. Conway's Law is a diagnostic lens: product structures often reflect communication structures. It does not make a pair count proof of causation. Review recurring seams across several periods before proposing an organizational change.

## Run the weekly control loop

Before the review, update forecast, evidence and acceptance fields with their source and as-of time. During the review, start with blocked/failed, negative-gap and unconfirmed records; reconcile date meanings and usable criteria with both sides; record decisions and evidence requests. Afterward, preserve changed forecasts, rejected deliveries and acceptance events rather than overwriting history.

Escalate only the decision beyond the team's authority. Supply the handoff, local evidence, affected receiving work, options and last responsible decision point. Do not claim project delay from a red arrow alone.

## Chart choice

| Question | Primary view | Limitation |
|---|---|---|
| Who provides what to whom? | Directed network | Large graphs need scoped views |
| Where do team seams recur? | DSM | Counts do not prove risk or causality |
| What exactly is late or unconfirmed? | Register | Paths and cycles are harder to see |
| What drives project finish? | Integrated CPM schedule | Needs complete logic, duration and calendar evidence |

## Reference basis

- [borghei/claude-skills dependency-map](https://github.com/borghei/claude-skills/tree/ddca910e95580c63a236303fc1534054f0f14d4c/project-management/execution/dependency-map), inspected at commit `ddca910e95580c63a236303fc1534054f0f14d4c`: provider/consumer records, left-to-right network, weekly operating cadence and DSM/Conway diagnostic ideas used as methodology references. No upstream renderer code is included here.
- [GAO Schedule Assessment Guide](https://www.gao.gov/products/gao-16-89g): integrated schedule and critical-path analysis requirements.
- Melvin E. Conway, “How Do Committees Invent?” (1968): the communication-structure observation now called Conway's Law.
