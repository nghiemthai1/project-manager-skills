# Lessons Learned: software example

Fictional training scenario. Values and thresholds are examples, not defaults for real projects.

## Lesson: plan acceptance evidence before committing release readiness

Relay's 28 October review lacked recovery-access evidence. The pilot was deferred under D-004 and began after evidence was accepted. The observation supports a practice of explicitly planning acceptance demonstrations and their owners alongside implementation.

It does not prove every release needs an identical review cadence or that adding meetings guarantees readiness. Appropriate timing depends on evidence lead time and the consequence of failure.

An adoption proposal is to add evidence owners and demonstration dates to the next release plan, then inspect whether mandatory gaps are discovered early enough for action. Until tested on another release, label this a proposed practice informed by Relay, not a widely validated organizational standard.

## Repair

**Flawed:** "Always hold more security meetings."

**Corrected:** "Plan decision-relevant acceptance evidence with sufficient lead time, and evaluate whether the chosen review process exposes gaps before the release decision."
