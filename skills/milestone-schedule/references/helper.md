# Schedule helper

```sh
python scripts/schedule.py --demo --format json
python scripts/schedule.py --input schedule.json --format markdown
```

Required JSON:

```json
{"unit":"working_days","tasks":[{"id":"A","duration":2,"predecessors":[]},{"id":"B","duration":4,"predecessors":["A"]},{"id":"C","duration":3,"predecessors":["A"]},{"id":"D","duration":1,"predecessors":["B","C"]}]}
```

Task IDs are unique nonempty strings. Durations are finite nonnegative numbers in one declared unit. Predecessors must exist, be unique within an activity, and form an acyclic network. The network must contain at least one task. Zero duration is permitted for milestones.

The example duration is seven working-day offsets. C has one day of total float. A, B, and D are critical. Results contain earliest and latest starts/finishes, total float, critical activities, and critical edges. They do not enumerate every possible critical path because path count can grow exponentially.

The model uses finish-to-start links without lag, date constraints, working calendars, or resource leveling. Disconnected terminal branches share a common modeled finish. Offsets start at zero; they are not calendar dates. A real calendar forecast needs explicit scheduling of resources, holidays, external constraints, and acceptance gates. Unsupported fields such as lag are rejected rather than silently ignored.


Use `--input -` for stdin. Unknown fields and duplicate JSON keys are errors. Valid results exit 0; invalid input, unsupported values, numeric overflow, or read failures exit 2 with an explanation on stderr. Output goes to stdout, and input files are never changed. The helper uses Python 3.11+ standard library only and works from any current directory when invoked by its path.
