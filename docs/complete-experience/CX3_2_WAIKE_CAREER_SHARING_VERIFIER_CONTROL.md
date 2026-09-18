# CX3.2 Control — Real WAIKE Credential Integration + Career Sharing + Verifier

Stacked on Portal CX3.1 (`docs/cx3-credential-wallet-portfolio-control`).  
Does **not** touch Portal #14/#15. Does **not** modify WAIKE release/main. No Device Lab. No merges. No accreditation claims.

## Device OS DRAFT stack

| PR | Branch | Base |
|----|--------|------|
| CX3.1 | `eng/cx3-credential-wallet-portfolio-foundation` | CX2H.4 |
| CX3.2 (this wave) | `eng/cx3-waike-career-sharing-verifier-campaign` | CX3.1 |

## Portal DRAFT stack

| PR | Branch | Base |
|----|--------|------|
| CX3.1 | `docs/cx3-credential-wallet-portfolio-control` | CX2H.4 |
| CX3.2 (this wave) | `docs/cx3-waike-career-sharing-verifier-control` | CX3.1 |

## Scope

### Track A — Real WAIKE earned-credential integration (honest)
1. Discover accepted-main WAIKE (expected merge #16 / `34fb050…`; record actual SHA)
2. Gate with `WAIKE_REAL_EARNED_EVIDENCE_AVAILABLE`
3. Read-only `LearningEvidenceProvider` adapter — no WAIKE writes
4. Real earned credential journey **only** if genuine evidence available
5. Evidence mismatch detection on controlled fixture (not authoritative WAIKE)

### Track B — Career sharing + independent verifier (finish even if Track A blocked)
1. `CareerProfile v1` authority + GUI journey
2. Resume export (HTML/text; PDF if legitimate path available)
3. `PortfolioSharePackage v1`
4. Independent Verifier (no Wallet DB dependency)
5. Verifier GUI, selective disclosure, revocation propagation, offline, no-second-computer
6. Security fail-closed + tests

Stop — do **not** set `FULL_COMPLETE_EXPERIENCE_COMPLETE=true`.

## Separated truth lanes

| Lane | Token |
|------|-------|
| CX3.1 foundation retained | `CX3_1_WALLET_PORTFOLIO_FOUNDATION_PASS` |
| WAIKE real evidence available | `WAIKE_REAL_EARNED_EVIDENCE_AVAILABLE` |
| Read-only provider | `CX3_WAIKE_READ_ONLY_PROVIDER_PASS` |
| Evidence provenance mapping | `CX3_WAIKE_EVIDENCE_PROVENANCE_PASS` |
| WAIKE earned integration | `CX3_WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS` |
| Evidence mismatch detection | `CX3_WAIKE_EVIDENCE_MISMATCH_DETECTION_PASS` |
| Career Profile GUI | `CX3_REAL_CAREER_PROFILE_GUI_PASS` |
| Resume export | `CX3_RESUME_EXPORT_PASS` |
| Share package | `CX3_PORTFOLIO_SHARE_PACKAGE_PASS` |
| Independent verifier | `CX3_INDEPENDENT_VERIFIER_PASS` |
| Verifier GUI | `CX3_REAL_VERIFIER_GUI_PASS` |
| Selective disclosure | `CX3_SELECTIVE_DISCLOSURE_PASS` |
| Revocation propagation | `CX3_VERIFIER_REVOCATION_PROPAGATION_PASS` |
| Offline career/verifier | `CX3_OFFLINE_CAREER_VERIFIER_PASS` |
| No-second-computer | `CX3_NO_SECOND_COMPUTER_CAREER_PASS` |
| Security | `CX3_2_SECURITY_REGRESSION_FREE` |
| Certification claim | always `certification_claimed=false` |

## Evidence

Device OS: `artifacts/complete_experience/cx3_2/` only.  
Lab: `os_build/cx3_2_linux_lab/`.

## Concurrency

`/tmp/gunnchos-cx-qemu.lock` — one CX guest; never kill foreign QEMU.

`FULL_COMPLETE_EXPERIENCE_COMPLETE=false`

## Results (Device OS evidence — filled after campaign run)

| Token | Value |
|-------|-------|
| `CX3_1_WALLET_PORTFOLIO_FOUNDATION_PASS` | **true** |
| `WAIKE_REAL_EARNED_EVIDENCE_AVAILABLE` | **false** |
| `CX3_WAIKE_READ_ONLY_PROVIDER_PASS` | **true** |
| `CX3_WAIKE_EVIDENCE_PROVENANCE_PASS` | **true** |
| `CX3_WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS` | **false** |
| `CX3_WAIKE_EVIDENCE_MISMATCH_DETECTION_PASS` | **true** |
| `CX3_REAL_CAREER_PROFILE_GUI_PASS` | **true** |
| `CX3_RESUME_EXPORT_PASS` | **true** |
| `CX3_PORTFOLIO_SHARE_PACKAGE_PASS` | **true** |
| `CX3_INDEPENDENT_VERIFIER_PASS` | **true** |
| `CX3_REAL_VERIFIER_GUI_PASS` | **true** |
| `CX3_SELECTIVE_DISCLOSURE_PASS` | **true** |
| `CX3_VERIFIER_REVOCATION_PROPAGATION_PASS` | **true** |
| `CX3_OFFLINE_CAREER_VERIFIER_PASS` | **true** |
| `CX3_NO_SECOND_COMPUTER_CAREER_PASS` | **true** |
| `CX3_2_SECURITY_REGRESSION_FREE` | **true** |
| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false** |
| `certification_claimed` | **false** |

### Honest blockers (do not invent PASS)

- WAIKE earned credential integration requires genuine read-only accepted-main completion evidence (Device Lab release-train currently `RELEASE_TRAIN_DEPENDENCY_PENDING`)
- Do **not** claim Open Badges 3 / CLR conformance
- Do **not** claim accreditation, degrees, diplomas, or certifications

## Next gate

When Career/Verifier tokens PASS and WAIKE remains release-dependent:

`NEXT_CX_GATE=CX3_2B_WAIKE_RELEASE_DEPENDENCY_RETRY`

When both Career/Verifier and real WAIKE integration PASS:

`NEXT_CX_GATE=CX3_3_EDUCATION_CAREER_DIGITAL_CLOSURE_AUDIT`

## Accepted-main WAIKE (recorded)

- path: `/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/gunnchos-waike-learning-platform`
- main SHA: `34fb050ccabec813cef4811d64581b32453e1ec2`
- PR #16 ancestry: `True`
- real completion available: `False`
- reason: `RELEASE_TRAIN_DEPENDENCY_PENDING`
- NEXT_CX_GATE: `CX3_2B_WAIKE_RELEASE_DEPENDENCY_RETRY`

