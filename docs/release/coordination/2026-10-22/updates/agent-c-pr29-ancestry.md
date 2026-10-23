# Agent C update — WAIKE pull request 29 ancestry

This file is an additive coordination note. It does not edit `BLOCKERS.json`, `CURRENT.json`, `RELEASE_MATRIX`, or the A–O denominator documents. Denominators stay **16** components, **108** features, **38** gates, and **43** tickets. No blocker is marked closed.

Rechecked with `gh` on 2026-10-22 before this note was written. Pull request 29 was still open and still a draft. The live head matched the expected SHA recorded below.

## Pull request

- URL: https://github.com/gunnchOS3k/gunnchos-waike-learning-platform/pull/29
- Branch: `eng/cursor-v1-agent-c-learn`
- Expected head: `6f6e1d2c0b6bd9f3434e7fe44dd4bfcac5d823c9`
- Live head: `6f6e1d2c0b6bd9f3434e7fe44dd4bfcac5d823c9` (matches)
- The pull request remains an open draft and a **STACK**, not a minimal release candidate.
- `origin/main` remains `2641042936f3b965daccb11091c80cbc6fa64f91`.

## Lesson-read fix

The lesson-read fix is only `f668ea40a32c3d991a7ba42d9be5d836356b1dbb`.

Cherry-pick onto main was aborted: `BrowserLearning.tsx` is absent on main. Do not split it.

## Pins

Pins were **NOT** changed. Do not retarget either pin.

- Workflow checkout `63ba9f25ac6b8d8d1b6dd118923566fd51c57b62` is on GitHub.
- Stack `PIN.json` remains `33a101852f4fefb0eb239bcffa60a65d71102e2c`. That SHA is not on GitHub. It is a later curriculum generation.
- 51 `lesson.md` files differ.

## What was and was not run

- Practice evaluator test passed: formative, earned 0, persisted false. That result is not a grade. It is not a live evaluator.
- Instructor case "denies answer keys and other sections" passed (1 passed, 32 skipped). That case is a client search filter only. Product code is unchanged. The note commit is `6f6e1d2c0b6bd9f3434e7fe44dd4bfcac5d823c9`.
- Trusted replay was not run. It is blocked on an owner-provisioned localhost CA and leaf. TLS was not bypassed. gunnchAI was not called.
- Free space is about 12 GiB, under the 18 GiB reserve. No npm install was run.

## Release position

B03 stays open. B02 remains **CRITICAL**. V1.0.0 and RC2 remain **NOT READY** and **NOT AUTHORIZED**. REL-03 must not be taken.
