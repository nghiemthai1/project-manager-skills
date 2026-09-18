# Provider-to-receiver visual design

Read this when a dependency decision benefits from a graph. The visual must preserve the register's evidence rather than turn incomplete records into confident geometry.

## Start from the decision

Use a left-to-right network to answer **who must provide what to whom, and which chain or cycle needs coordination?** Use a DSM to answer **which provider/receiver seams recur?** Use the register to answer **what are the exact dates, usable criteria, owners and sources?** A single artifact can offer all three views, but each view keeps its own meaning.

Arrows always run **provider → receiver**. Label every edge with its literal dependency ID and expose the handoff name in a persistent detail panel. Show node type and owner without implying that a coordinator has contractual or acceptance authority.

## Required source contract

At snapshot level retain title, as-of date, version, source, scope and calendar unit. Each node needs an ID, label, type, owner and source. Each dependency needs:

- dependency ID, provider and receiver IDs;
- handed-off result and observable usable criteria;
- needed-by, requested, committed and forecast dates as separate nullable fields;
- commitment evidence when a committed date exists;
- operating status and acceptance state;
- provider-side and receiver-side owners, source and note.

Do not substitute `unknown` with a guessed date or omit an unresolved provider. Add an explicit unknown node when the boundary is known but its provider is not.

## State and emphasis

Use text plus color for every state. A useful deterministic order is blocked/verification failed, negative local gap, explicit at-risk, unconfirmed, watch, accepted. Call this a coordination order. Do not label it probability, severity, float or criticality unless those values come from an identified method and complete source.

A local margin is `needed-by − forecast` in the declared unit. Display `not calculable` when either date is missing. A negative result means only that the current forecast is after the receiver's stated need.

Selection should reveal the edge, provider, receiver and immediately connected chain while retaining a visible way to restore all links. Filters must state `visible / total` counts. If a selection falls outside the filter, move to the first visible dependency and disclose the filtered scope through the count.

## Layout and scale

Use a deterministic layered layout so the same data produces the same drawing. Keep cycles visible; placing a cyclic group in a shared column is preferable to deleting an edge or inventing precedence. Route crossings behind nodes, give edge labels a solid background and keep graph labels short. Put full criteria and evidence in the detail panel and register.

For a small network, render every material handoff. With dozens of nodes, start from a filtered domain, selected chain or DSM and make the scope explicit. Route live, collaborative or very large dependency models to suitable graph tooling rather than claiming this small offline renderer covers them.

## Interaction and responsive behavior

The HTML view should provide search, status and party filters; a negative-gap/blocked focus; link focus; zoom; graph/DSM switching; visible-slice CSV; print/PDF; and persistent details. A local draft editor may change the dependency agreement fields while holding stable IDs and the node inventory fixed. It must validate endpoints, self-links, states, dates and commitment evidence; retain and warn on directed cycles; preserve immutable source exports; and label draft exports and locally changed records. Graph, DSM, register and displayed metrics must recalculate from the saved draft. Edge and node selection must work with Enter or Space. Escape should clear the review filters. Hover may reinforce state but cannot be the only way to retrieve evidence.

At phone width, keep controls and details in one column, preserve a deliberate horizontal scroll region for the graph or matrix, and turn the register into labeled cards. In landscape, keep touch targets usable and avoid page-level horizontal overflow. The graph can be wider than its bounded scroll container.

## Accessibility and delivery

Include an accessible table containing every visible field, readable focus styles, non-color labels and an SVG title/description. Keep graph marks keyboard reachable. Treat browser print as a report surface: title, scope, as-of date, filters and method boundary must remain visible.

Deliver the editable source JSON, normalized JSON, full CSV, static SVG and self-contained HTML together. The browser-local draft must keep before/after history, support sequential undo and offer a confirmed full restore to source. Draft JSON should state its source basis and revalidation requirement. The toolbar CSV may reflect current filters; label it as visible. Permanent downloads preserve the complete source snapshot. Guard spreadsheet cells beginning with formula characters.

Open the actual files. Compare IDs, directions, dates, margins, states and sources with the input. Inspect desktop, portrait and landscape sizes; test empty filters, keyboard selection, view switching, zoom, invalid edits, cycle retention, draft persistence, undo, restore, source/draft export separation, visible CSV and print layout. If rendering was unavailable, say visual inspection was not performed.
