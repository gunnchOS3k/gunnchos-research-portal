# C. All 38 release gates

Generated from the October 9 ledger `gates` object, which the accepted revision 2 board still copies. Count: **38**. Passed: **2** (`V1_PUBLIC_SITE_PASS`, `V1_SITE_HUMAN_TASTE_PASS`), both historical and scoped. The other **36** stay false. This pass does not flip any gate.

| Gate | Kind | Passed | Depends on | October 22 disposition |
|---|---|---|---|---|
| `V1_PUBLIC_SITE_PASS` | AUTOMATED | true | — | Historical scoped pass retained. Not re-audited and not expanded. |
| `V1_SITE_HUMAN_TASTE_PASS` | HUMAN | true | — | Historical scoped pass retained. Not a V1 authorization. |
| `V1_MLV_HUMAN_PASS` | HUMAN | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_WAIKE_HUMAN_PASS` | HUMAN | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_ANIME_HUMAN_PASS` | HUMAN | false | — | Remains false. Unmerged Anime drafts are not human acceptance. |
| `V1_PURSUIT_HUMAN_PASS` | HUMAN | false | — | Remains false. Pedestrian #42 is not human acceptance. |
| `V1_ARCHIVE_HUMAN_PASS` | HUMAN | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `HUMAN_SCIENTIFIC_REVIEW_COMPLETE` | HUMAN | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_BEATLINK_HUMAN_PASS` | HUMAN | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_GUNNCHAI_HUMAN_PASS` | HUMAN | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_HARDWARE_DIGITAL_HUMAN_PASS` | HUMAN | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_PASSPORT_HUMAN_PASS` | HUMAN | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_ACCESSIBILITY_HUMAN_PASS` | HUMAN | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_INVITES_HUMAN_PASS` | HUMAN | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `FINAL_CHARACTER_ART_PASS` | HUMAN | false | — | Remains false. Codex art work is unmerged and not approved here. |
| `ANIMATION_TASTE_HUMAN_PASS` | HUMAN | false | — | Remains false. |
| `GAME_FEEL_HUMAN_PASS` | HUMAN | false | — | Remains false. #124 does not change production audio or feel. |
| `VFX_TASTE_HUMAN_PASS` | HUMAN | false | — | Remains false. |
| `SFX_MIX_HUMAN_PASS` | HUMAN | false | — | Remains false. #124 is a delayed-cleanup finding only. |
| `STORY_HUMAN_PASS` | HUMAN | false | — | Remains false. ANI-02 canon recorded earlier is not a new Story gate. |
| `V1_PIXEL_ACCEPTANCE_PASS` | PHYSICAL_OWNER | false | — | Remains false. No device was attached for this pass. |
| `V1_INVITES_PROTOCOL_PASS` | AUTOMATED | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_INVITES_ANIME_PASS` | AUTOMATED | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_INVITES_PURSUIT_PASS` | AUTOMATED | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_INVITES_BEATLINK_PASS` | AUTOMATED | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_INVITES_ARCHIVE_PASS` | AUTOMATED | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_INVITES_MLV_HANDOFF_PASS` | AUTOMATED | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_INVITES_DEVICE_HANDOFF_PASS` | AUTOMATED | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_INVITES_BROWSER_FALLBACK_PASS` | AUTOMATED | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_INVITES_FULL_PASS` | AUTOMATED_AGGREGATE | false | V1_INVITES_PROTOCOL_PASS, V1_INVITES_ANIME_PASS, V1_INVITES_PURSUIT_PASS, V1_INVITES_BEATLINK_PASS, V1_INVITES_ARCHIVE_PASS, V1_INVITES_MLV_HANDOFF_PASS, V1_INVITES_DEVICE_HANDOFF_PASS, V1_INVITES_BROWSER_FALLBACK_PASS | Remains false. No October 22 evidence satisfies this gate. |
| `V1_FULL_FEATURE_MATRIX_PASS` | AUTOMATED_AGGREGATE | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_ARCHIVE_SCIENTIFIC_COVERAGE_PASS` | AUTOMATED_AGGREGATE | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_EXACT_BUILD_DEPLOY_PROVENANCE_PASS` | AUTOMATED_AGGREGATE | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_AUTOMATED_PIPELINE_PASS` | AUTOMATED_AGGREGATE | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `V1_RIGHTS_PROVENANCE_PASS` | AUTOMATED_AGGREGATE | false | — | Remains false. No October 22 evidence satisfies this gate. |
| `RC2_READY` | AUTOMATED_AGGREGATE | false | — | Remains false. |
| `RC2_OWNER_AUTHORIZED` | OWNER_RELEASE | false | — | Remains false. This package does not authorize RC2. |
| `V1_0_0_RELEASE_AUTHORIZED` | OWNER_RELEASE | false | — | Remains false. This package does not authorize V1.0.0. |

`V1_INVITES_FULL_PASS` still depends on eight invite gates, all false. `RC2_OWNER_AUTHORIZED` and `V1_0_0_RELEASE_AUTHORIZED` stay false.
