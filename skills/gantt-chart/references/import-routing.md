# Import and reconstruction routes

Use the route matching the supplied file. These are inspection instructions, not claims that this package includes every vendor parser or connector.

| Input | First action | Mapping questions |
|---|---|---|
| Microsoft Project XML | Inspect task/resource/calendar/link elements and export coverage | Manual tasks, elapsed duration, constraints, baseline selection, inactive/summary rows |
| MPP | Use an available reader or request an XML/table export | Do not rename a binary file or pretend CSV preserves all scheduling rules |
| Primavera XML/XER | Inspect product/export version and actual tables before selecting a supported parser | Activity types, relationship types/lag, calendars, baseline membership, percent-complete basis |
| Jira / roadmap export | Inspect field IDs and link types rather than display names alone | Target versus due fields, hierarchy, plan filters, whether “blocks” is a schedule relation |
| GitHub Projects export | Inspect custom date/iteration fields and stable item/content IDs | Iteration membership is a timebox, not a task span; milestone due dates are markers |
| Smartsheet | Preserve stable row IDs and predecessor objects | Row numbers may change; parent formulas and dependency-managed dates may be computed |
| Asana / monday.com / ClickUp | Inspect actual exported schema, date types and dependency settings | Due-only tasks, date-only versus epoch timestamps, custom fields, automatic shifting rules |
| Azure DevOps | Distinguish iteration dates, custom planning dates and historical snapshots | Do not draw every work item across its full iteration unless the requested view is a timebox roadmap |
| CSV/TSV/XLSX | Inspect header, delimiter/encoding, cell types and locale | Explicit column map, IDs, percent scale, inclusive finish, blank dates, quoted delimiters |
| PDF/image | Ask for source data if available; otherwise perform a labeled reconstruction | Which values can be read exactly, what is inferred, what cannot be recovered |

Never promise a currently unavailable integration. Use the user's installed tools or source export; verify current vendor documentation when implementing an adapter. Keep unmapped consequential fields with diagnostics rather than dropping them to fit the renderer.

For several sources, namespace identity (source/project/ID) without changing the original source ID. State which source owns dates, assignments and calendars; inconsistent snapshots should not look like one synchronized plan.

An import can succeed as a partial artifact: retain undated tasks, show the filter boundary, list missing predecessors and explain which conclusions remain unsupported. An unreadable proprietary file is not permission to manufacture a schedule.
