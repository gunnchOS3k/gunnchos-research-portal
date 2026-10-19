# v1.0.0 Change Control and Scope Freeze Protocol

## Goal
Stop the last push from becoming endless feature development while preserving every idea.

## Before scope freeze
Every new item must:
1. receive a scope ID;
2. enter the scope ledger;
3. receive a v1 disposition;
4. identify affected repos;
5. identify acceptance/evidence;
6. identify owner action.

## After scope freeze
Only these may enter v1:
- release-blocking defect
- security/privacy issue
- data-loss issue
- build/deploy breakage
- legal/rights blocker
- owner-explicit essential scope correction

Everything else moves to post-v1.

## Decision test
1. Does absence break an already-promised v1 journey?
2. Is it needed for security/privacy/data integrity/release truth?
3. Is it only more ambitious/prettier/broader?
4. Does it require new physical/regulatory/vendor/scientific/institutional work?
5. Can it wait without breaking a v1 promise?

Default: if nobody can explain which v1 promise breaks, defer it.

## WIP rule
Maximum three high-impact implementation lanes at once.

Current recommended WIP:
1. Anime #118 G7 + owner acceptance
2. 3k MLV public hosting
3. Pedestrian #39 owner review

## Freeze trigger
Owner sets:

```text
V1_SCOPE_FROZEN=true
```

After that, non-blocking new features default to post-v1.
