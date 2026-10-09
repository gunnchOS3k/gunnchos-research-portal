# gunnchOS V1 Full-Completion Plan
**Revision date:** October 4, 2026  
**Policy change:** Representative gold slices are rejected as a definition of V1 completion.

## 1. New completion policy

Official V1 now requires **full completion of the entire owner-approved V1 software and digital-engineering scope**.

A gold slice, representative campus, sample course, sample story route, single lap, or partial roster can be useful during development, but it cannot be used to declare the corresponding V1 domain complete.

This does **not** mean every long-term roadmap idea becomes V1. The first release-control task is to lock the declared V1 scope for every domain. After that scope lock:

- every feature marked **V1 Required** must be completed, integrated, evidenced and accepted;
- a feature can leave V1 only through an explicit owner scope decision;
- no automation/agent may silently reinterpret an incomplete V1 feature as “future work”;
- physical/regulatory/manufacturing work already defined as outside V1 remains outside V1.

## 2. 3k MLV policy change

The prior plan used Gary and selected spaces as a V1-quality gold slice while allowing other campuses to remain structurally shallower. That acceptance model is withdrawn.

For official V1, the intended spatial world must be completed across:

- Commons
- My Home
  - Exterior / Yard
  - Living / Front Room
  - Media Room
  - Office / Workbench
  - Bedroom / Logoff
- Gallery Pavilion
  - Gallery Lobby
  - Local Culture
  - Rotating Institution
  - 7GC Exchange
  - Public Community
  - My Gallery
- Campus Transit
- Gary
- Ghana
- Guyana
- Geelong
- Ruhr
- Gaza
- Graham Land

Each campus must reach the owner-approved V1 completeness standard for its declared:
- arrival/exterior,
- civic/lobby,
- learning/lab,
- museum/gallery/archive,
- showcase/community,
- return/navigation,
- local identity and provenance,
- accessibility/mobile/state behavior.

No campus is considered complete simply because it is reachable.

## 3. Full-completion implications across the rest of the ecosystem

### WAIKE
Do not accept one sample course journey as proof of completion. Validate the entire declared V1 learner product, all 18 tracks, supported assessment lifecycles, offline sync/restart/conflict/receipt behavior, and declared gunnchAI/standards/device integrations.

### Anime Aggressors
Do not accept one approved character or one story segment as completion. Lock the declared V1 roster/forms/story/move scope and complete the full roster art, promised variants, story routes, combat/move/animation/effects presentation, and owner review.

### Pedestrian Pursuit
One exact lap remains useful as a diagnostic, but it is no longer the completion definition. Lock the declared V1 course/mode/item scope and close the entire gameplay matrix before owner fun/course approval.

### Device OS / Pixel
Complete the declared V1 OS/capsule integration scope, then freeze and physically validate the entire exact installable V1 candidate set.

### Hardware digital engineering
All four digital device concepts must reach the owner-approved V1 digital-design level. Physical EVT/DVT/PVT/certification/manufacturing still remain outside official V1.

### Research / 7GC
Every research project included in V1 must satisfy its truthful public evidence contract. Missing evidence must remain explicitly unavailable rather than fabricated.

## 4. Release sequence

1. Lock the complete V1 scope.
2. Create the authoritative evidence index.
3. Close the public-site accepted-main/deployment gap.
4. Reconcile 3k MLV PR #9.
5. Complete the entire V1 spatial world.
6. Complete the entire declared WAIKE V1 product.
7. Complete the entire declared Anime Aggressors V1 product.
8. Complete the entire declared Pedestrian Pursuit V1 product.
9. Complete Archive of Life / BeatLink declared V1 scope.
10. Complete Device OS V1 scope.
11. Complete all four digital hardware concepts to V1 design acceptance.
12. Complete public research/7GC evidence and integrations.
13. Freeze the exact Pixel candidate set and physically accept it.
14. Refresh the full V1 readiness board/evidence index.
15. Run the complete cross-repo automated acceptance matrix.
16. Freeze the complete-scope RC2 manifest.
17. Owner authorizes and publishes RC2.
18. Run a no-new-features final acceptance cycle.
19. Owner explicitly authorizes official V1.
20. Publish `v1.0.0`.

## 5. Codex takeover from Cursor

Codex can continue the repository work, but it should be treated as a **repository-state handoff**, not a magical continuation of Cursor's conversation history.

The durable state Codex can inherit is:
- files in the same local folder,
- Git branches,
- commits,
- uncommitted working-tree changes,
- stashes,
- worktrees,
- repository configuration/remotes,
- GitHub PR/CI state when connected.

What it will not automatically inherit is the private conversational reasoning/history from the Cursor agent.

### Important warning from the current Cursor screenshot

The Cursor workspace shows outstanding local changes:

`Changes +13 -1286`

Do not delete, reset, or clean that workspace until we know which repository owns those changes and whether they contain work that was never committed.

### Find the local 3k MLV folder

On the Mac, open Terminal and run:

```bash
mdfind 'kMDItemFSName == "3k-mlv"c'
```

For each path returned:

```bash
git -C "/path/from/above" remote -v
git -C "/path/from/above" status --short
git -C "/path/from/above" branch --show-current
```

The correct repository should show the `gunnchOS3k/3k-mlv` GitHub remote.

Then in Codex:

1. **New project**
2. **Use an existing folder**
3. Choose that exact local `3k-mlv` folder.
4. Keep **Ask for approval** enabled.
5. Give Codex a read-only continuity audit first.

### First Codex continuity task

```text
Work only in this repository.

This is a handoff from a Cursor-based development workflow. Do not assume Cursor's conversational history is available. Reconstruct the durable state from Git and the filesystem.

First perform a READ-ONLY continuity audit.

Report:
- repository root
- remotes
- current branch
- git status
- staged and unstaged changes
- untracked files
- local branches
- worktrees
- stashes
- current origin/main
- current branch vs origin/main divergence
- whether draft PR #9 branch world/spatial-commons-neighborhood-v1 exists locally/remotely
- whether any local changes appear to be unfinished Cursor work

Do not modify, checkout, merge, reset, clean, stash, commit, push, or delete anything yet.

The V1 policy has changed: representative 'gold slice' completion is rejected. We are completing the entire owner-approved V1 software/digital scope. Do not use earlier gold-slice acceptance criteria as release completion criteria.

After the audit, stop and ask for approval.
```

If the local repo cannot be found or is clean and contains no unique Cursor work, we can use Codex Cloud/GitHub against `gunnchOS3k/3k-mlv`. Cloud can continue committed GitHub state, but local uncommitted Cursor edits must first be preserved or intentionally discarded.

## 6. Final rule

From this revision forward:

> **Full completion means the full declared V1 scope, not a reference slice.**

The tracker accompanying this plan is the operational control plane. Do not mark a domain complete until every required row for that domain is Delivered and all required human gates are explicitly approved.
