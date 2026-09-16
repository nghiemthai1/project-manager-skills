# Source mapping and schedule model

Read this before turning an export, screenshot or task list into a timeline. The first deliverable is a mapping record, not a bar chart.

## Classify what the source can establish

| Source | Useful evidence | Do not silently infer |
|---|---|---|
| Scheduling-engine export | Activities, calendars, typed links, constraints and named baselines if actually present | That a table export contains the engine's complete rules or resources |
| Task tracker or roadmap view | IDs, explicit custom planning fields, dates and displayed hierarchy | Created/closed timestamps are planned starts/finishes; a “blocks” link has scheduling semantics |
| Resource calendar | Booking spans and resource availability | Task dependencies or project critical path |
| CSV/TSV/JSON/spreadsheet | Values from named columns at an identifiable snapshot | Locale, timezone, percent scale, omitted rows or meaning of “Due” |
| PDF/image/slide | Visible labels, structure and approximate positions | Exact dates from pixels, hidden dependencies or reliable source metadata |

Record source system/file, export/as-of time when supplied, view/query/filter scope, project namespace and row coverage. A filtered export may omit the predecessor, not prove there is none. If a field is absent, preserve the task in an unscheduled/missing-evidence list. Do not quietly discard it.

Build a mapping table with **source field/path → normalized field → conversion rule → evidence/uncertainty**. “Target end” remains a target unless its approval is evidenced. A user-authorized reconstruction may estimate dates from an image, but mark each reconstructed value and keep the original alongside it.

## Normalized snapshot

Separate project context, task rows, relationships, comparison layers and diagnostics. Keep arbitrary source IDs as strings; never use row positions as identity.

| Object | Required meaning | Optional evidence to preserve |
|---|---|---|
| Snapshot | Title, purpose, source, as-of, version, source coverage, date convention | Export time, query/view, source-system versions, timezone, mapping notes |
| Task | Stable ID, label, kind, display order; dates may be unknown | Parent/WBS, owner, calendar, status, progress meaning/source, source URL, uncertainty |
| Date layer | Explicit kind: target, planning scenario, approved baseline, forecast or actual | Start/finish, baseline decision/version, actual-event evidence, method |
| Dependency | Separate ID, predecessor/successor IDs, FS/SS/FF/SF, lag value/unit/calendar | Source relationship, inferred flag, driving/critical evidence |
| Calendar | ID, timezone/date-only policy, working periods and exceptions | Holiday source, shifts, task-specific override |
| Diagnostics | Affected source ID, problem, display treatment, action required | Missing rows/fields, invalid range, unknown link, unsupported feature |

Keep one source of truth for a field. Display shortening must not change exported IDs. Unknown values are null/explicitly unknown, not zero, today or an empty string that looks like “none.” A summary task is a rollup only when that rule is established; do not stretch parent bars to hide children outside their range.

## Date layers and boundaries

Store date-only values as ISO dates without passing them through a UTC timestamp conversion. For true instants, preserve the offset and establish the display timezone before deriving a date. Do not guess the locale of `03/04/2026`.

Normalize intervals explicitly. In this library's instructional examples, `[start, finish)` excludes the finish boundary. An inclusive final work date is a different contract. Converting it needs the applicable calendar and time convention; Friday's final work period may correspond to a next-working-boundary Monday in a day-based model. Record the conversion and retain the raw value. Do not add one day indiscriminately to every source finish.

Zero duration does not by itself prove a milestone: it may be malformed data. Preserve explicit task kind. A milestone marks an event; its preparation/review effort belongs in actual work rows. Do not infer acceptance from the diamond.

## Validate without silently rescheduling

Check duplicate IDs, missing endpoints, hierarchy cycles, dependency cycles, inverted intervals, invalid dates, progress outside its declared scale and partially missing date pairs. Distinguish errors that prevent trustworthy plotting from warnings that permit a partial view. Emit a diagnostic list with affected IDs and counts.

Compare successor timing only using the actual relationship, lag and calendar. An FS-zero relation differs from SS or elapsed-hours lag. Preserve unsupported links as labeled evidence and route calculation to an appropriate schedule engine. The chart renderer must not flatten every link to FS or recalculate criticality from the currently filtered rows.

Resource overlap is a question about demand, skill and availability. Two simultaneous bars are not proof of overload; two tasks known to require the same person full time are a supported conflict. Show the distinction.

## Deliverable contract

Deliver the mapping, normalized editable data, diagnostics, graphical view and accessible task table together. The reader should trace a displayed bar or warning back to its source field and snapshot. External writeback, source credentials and live synchronization are outside a read-only artifact request.
