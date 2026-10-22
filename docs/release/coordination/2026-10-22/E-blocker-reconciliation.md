# E. B01–B14 blocker reconciliation

Source of previous status: `docs/release/campaigns/2026-10-19/BLOCKERS.json` on `1f4ca20190c99dde5712e9e490ec81e05f1122dd`. That file was not edited. No blocker is closed. B02 stays **CRITICAL**.

"Changes since the last accepted release matrix" means changes relative to `docs/release/campaigns/2026-10-19/RELEASE_MATRIX.json`. Unmerged drafts are evidence, not acceptance.

## B01 — CRITICAL — Archive scientific denominator

- Previous status: full scientific denominator, authentic snapshots, and maps absent. Owner: external data/license owner plus Archive engineer.
- New evidence: no new evidence.
- Change since the matrix: none in this pass.
- Deficiency: accepted production-readiness and global-ingestion reports still have no fixture denominator. Not re-executed here.
- Resolved portion: none.
- Remaining acceptance: all pinned-source records, ICS, maps audits, and qualified review.
- Next action: ARC-01 approved acquisition, then ARC-02 ingestion, then ARC-03 maps and scientific audit.

## B02 — CRITICAL — Anime full V1 scope

- Previous status: full gameplay, presentation, and export scope not accepted. Owner: Anime engineer and owner.
- New evidence: Anime drafts #124–#130, all unmerged. Codex PR #123 head is still `7c25c2996f8adcee97ec2187a14bfc578d8681bf`. See G and H.
- Change since the matrix: the matrix pinned an older Anime candidate (`30c6f2c8`). The art branch tip is now `7c25c299`, still unmerged. Cursor drafts add narrow input, save, replay, packaging, and a shutdown finding. None is accepted main.
- Deficiency: ordinary route, form, combat, KO, throw, acting, OVA, export, and owner approval are still open. #124–#130 do not cover that matrix. Wave jobs that ran on those drafts are not green (I).
- Resolved portion, narrow and unaccepted: #129 reads `rules.stocks`, `rules.cpu_level`, and `rules.timer` into stocks, cpu level, and match timer. #130 writes and reads `user://aa_private_match_replay.json`. #126 adds three device-0 actions. #127 maps one grab bit. #128 serves a posted second-client frame while still forcing grab false. #125 adds importer sidecars. #124 explains delayed audio cleanup. **None of this closes B02.**
- Remaining acceptance: the full ordinary route/form/combat/KO/throw/acting/OVA/export matrix and owner approval.
- Next action: Codex continues art on its own branch. Cursor Engineering reviews the sequence in H. This coordination pass does not implement either lane.

## B03 — CRITICAL — WAIKE 18-course delivery

- Previous status: full 18-course program and public delivery path incomplete. Owner: curriculum/platform engineers and educator owner.
- New evidence: no new evidence. The prior handoff still blocks trusted live replay on an authorized current localhost CA/leaf chain.
- Change since the matrix: none verified here.
- Deficiency: Lessons-to-Home failure and incomplete 18-track assessment, offline, and education evidence stand as recorded. Not re-browsed here.
- Resolved portion: none. The existing local delivery repair must not be duplicated.
- Remaining acceptance: 18-track declared assessment, offline, integration, and education evidence.
- Next action: owner provisions approved trust. Review the existing private payload. Do not bypass TLS.

## B04 — CRITICAL — BeatLink public party server

- Previous status: public party server unavailable. Owner: BeatLink engineer, operator, and owner.
- New evidence: no new evidence.
- Change since the matrix: none.
- Deficiency: public gateway Play states party creation disabled, as recorded. Not re-probed here.
- Resolved portion: none.
- Remaining acceptance: two real clients create, join, ready, reconnect, and show results, plus explicit human party acceptance.
- Next action: accept a rights-safe real room and session backend with the current party flow.

## B05 — CRITICAL — Unified invites

- Previous status: required unified invite acceptance absent. Owner: cross-product engineers and owner.
- New evidence: no new evidence. Anime #127/#128 are PartyLink host-frame drafts, not `https://gunnchos.com/i/<opaque-token>`.
- Change since the matrix: none.
- Deficiency: invalid invite route behavior remains the recorded 404 probe. Not re-probed here.
- Resolved portion: none.
- Remaining acceptance: eight invite automated tokens, exact deployment provenance, and owner usability.
- Next action: INV-01 shared contract, then adapters, then mobile and browser acceptance.

## B06 — EXTERNAL — No physical target

- Previous status: no physical target connected. Owner: device owner.
- New evidence: no new evidence. `adb` was not run. No device was claimed.
- Change since the matrix: none.
- Deficiency: the recorded `adb devices -l` empty result stands.
- Resolved portion: none.
- Remaining acceptance: exact candidate hash, package, signature, launch, handoff, and physical owner acceptance.
- Next action: owner supplies an authorized device and a signer-safe install path. No clear and no uninstall.

## B07 — HIGH — Device OS RC1 source versus APK

- Previous status: annotated RC1 tag `438aaf2` does not equal released build manifest `2218ead`. Owner: release engineer and owner.
- New evidence: no new evidence.
- Change since the matrix: none. The matrix still records this discrepancy.
- Deficiency: source, tag, and artifact identity still disagree in the accepted record.
- Resolved portion: none. History was not retagged.
- Remaining acceptance: one consistent source, tag, build, and artifact chain.
- Next action: preserve the old tag and reconcile identity in a new candidate manifest.

## B08 — HIGH — 3k MLV auth and private sharing

- Previous status: production auth, full world, and private-sharing acceptance absent. Owner: MLV engineer, operator, and owner.
- New evidence: no new evidence.
- Change since the matrix: none.
- Deficiency: GitHub OAuth unavailable banner and local-test-identity limit stand as recorded.
- Resolved portion: none.
- Remaining acceptance: every declared region and campus, private-sharing denial, and owner review.
- Next action: full-world and real-auth sharing matrix on an authorized host.

## B09 — HIGH — Eight-edition rights and editorial release

- Previous status: eight-edition rights, editorial, and accessibility release pending. Owner: publication owner and reviewers.
- New evidence: no new evidence. The accepted campaign already recorded eight EPUBCheck passes and an empty public catalog.
- Change since the matrix: none.
- Deficiency: rights, editorial, audience, and accessibility approvals are still absent.
- Resolved portion: none. Hash-verified review EPUBs are not a release.
- Remaining acceptance: those approvals, with separate web and EPUB source hashes.
- Next action: keep manuscripts private and wait for an explicit publication decision.

## B10 — HIGH — Passport Pass2U

- Previous status: site PR 18 remains open. Owner: site engineer and owner.
- New evidence: no new evidence. PR 18 was not re-reviewed in this pass.
- Change since the matrix: none verified here.
- Deficiency: current-head runtime, privacy, QR, and physical Pass2U checks remain open.
- Resolved portion: none.
- Remaining acceptance: current-head runtime privacy and QR, plus a physical Pass2U and event owner check.
- Next action: reconcile the old candidate with current accepted site. Keep the iPhone gate open.

## B11 — HIGH — FieldKit Standards Watch

- Previous status: Standards Watch fails before the claim firewall because YAML is missing. Owner: release and FieldKit maintainer.
- New evidence: no new dispatch. Candidate `92d0864ab263d3fbe1b162b2cdda1bb2404ccc55` stays undispatched, as the October 22 handoff required.
- Change since the matrix: the matrix already pointed at draft repair `ddf90ab`. This pass does not move that repair onto accepted main.
- Deficiency: the accepted-main scheduled failure remains unrepaired on the accepted branch.
- Resolved portion: none on accepted main. A local repair existing elsewhere is not this dispatch and is not merged here.
- Remaining acceptance: an accepted repair and a scheduled-workflow run, with no truth-claim promotion.
- Next action: leave `92d0864` undispatched until a separate publication and dispatch authorization exists.

## B12 — EXTERNAL — Disk reserve

- Previous status: insufficient disk for the established heavy-export guard. Owner: workspace owner.
- New evidence: `df -h /` during this pass reported **Avail 15Gi** on `/dev/disk3s1s1`. That is under the 18 GiB reserve.
- Change since the matrix: the free-space figure is newly measured and still short of the guard.
- Deficiency: heavy Godot export, asset import, and large installs remain blocked by the reserve.
- Resolved portion: none. No cleanup was performed.
- Remaining acceptance: documented adequate capacity before any heavy export.
- Next action: owner-controlled capacity recovery. Do not delete archives or active worktrees.

## B13 — HIGH — Human, security, accessibility, rights, release approvals

- Previous status: full human, security, accessibility, rights, and release approvals open. Owner: owner and security, rights, and educator reviewers.
- New evidence: no new approval. Gate file still has 36 of 38 gates false. The two true gates are the historical website passes.
- Change since the matrix: none.
- Deficiency: CI and unmerged drafts do not grant approval.
- Resolved portion: none.
- Remaining acceptance: explicit scope-bound approvals and all aggregate dependencies.
- Next action: owner review against exact builds. Do not treat this packet as that review.

## B14 — CRITICAL — No accepted RC2 candidate

- Previous status: no complete accepted cross-repo RC2 candidate. Owner: release owner. October 19 disposition: NO-GO.
- New evidence: this coordination branch is another unmerged draft. It does not publish RC2.
- Change since the matrix: more unmerged Anime and Pedestrian drafts exist. They are not an RC2 manifest.
- Deficiency: required blockers B01–B13 are still open, and there is no reproducible accepted RC2 source, build, dependency, and rollback manifest.
- Resolved portion: none.
- Remaining acceptance: that manifest and an owner RC2 decision.
- Next action: resolve the required blockers, then re-pin accepted mains. Do not tag RC2.
