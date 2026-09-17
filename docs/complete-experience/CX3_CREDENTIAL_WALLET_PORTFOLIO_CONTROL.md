# CX3.1 Control — Credential Wallet + Signed Portfolio Foundation

Stacked on Portal CX2H.4 (`docs/cx2h4-p0-digital-closure-control`).  
Does **not** touch Portal #14/#15. Does **not** modify WAIKE release/main. No Device Lab. No merges. No accreditation claims.

## Device OS DRAFT stack

| PR | Branch | Base |
|----|--------|------|
| CX2H.4 | `eng/cx2h4-p0-digital-closure-audit` | CX2H.3 |
| CX3.1 (this wave) | `eng/cx3-credential-wallet-portfolio-foundation` | CX2H.4 |

## Scope

1. Canonical authorities: Wallet + Portfolio
2. Versioned contracts v1: CredentialRecord, EvidenceRecord, IssuerProfile, CredentialStatus, PortfolioArtifact, PortfolioCollection, CredentialExport, PortfolioExport
3. OB3/CLR-inspired adapters with `certification_claimed=false` and **no** conformance claims
4. Real local Ed25519 lab issuer (ephemeral keys; never commit private key)
5. Evidence-bound issuance using real Vault artifact from prior journeys
6. Secure Wallet storage + real Wallet GUI + signed credential journey through UI
7. Tamper detection, revocation/status, offline verify, import/export
8. Portfolio GUI + privacy selective export + portable HTML/manifest package
9. LearningEvidenceProvider v1 seam (`WAIKE_INTEGRATION_SEAM_PASS=true`; earned integration only if genuine read-only accepted-main proven)
10. Security fail-closed + tests; keep J1/J2/J3/J5/J7 PASS, J6 `HUMAN_VALIDATION_PENDING`
11. Stop — do **not** set `FULL_COMPLETE_EXPERIENCE_COMPLETE=true`

## Separated truth lanes

| Lane | Token |
|------|-------|
| Contracts | `CX3_CONTRACTS_V1_PASS` |
| Lab issuer | `CX3_LAB_ISSUER_ED25519_PASS` |
| Evidence-bound issuance | `CX3_EVIDENCE_BOUND_ISSUANCE_PASS` |
| Wallet storage | `CX3_WALLET_STORAGE_PASS` |
| Wallet GUI | `CX3_WALLET_GUI_PASS` |
| Signed journey | `CX3_SIGNED_CREDENTIAL_JOURNEY_PASS` |
| Tamper | `CX3_TAMPER_DETECT_PASS` |
| Revocation | `CX3_REVOCATION_STATUS_PASS` |
| Offline verify | `CX3_OFFLINE_VERIFY_PASS` |
| Import/export | `CX3_IMPORT_EXPORT_PASS` |
| Portfolio GUI | `CX3_PORTFOLIO_GUI_PASS` |
| Privacy export | `CX3_PORTFOLIO_PRIVACY_EXPORT_PASS` |
| Portable package | `CX3_PORTFOLIO_PORTABLE_PACKAGE_PASS` |
| Security | `CX3_SECURITY_FAIL_CLOSED_PASS` |
| OB3/CLR adapters | `CX3_OB3_CLR_ADAPTER_PASS` |
| WAIKE seam | `WAIKE_INTEGRATION_SEAM_PASS` |
| WAIKE earned | `WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS` |
| Foundation | `CX3_1_WALLET_PORTFOLIO_FOUNDATION_PASS` |
| Prior gate | `CX2H4_P0_DIGITAL_CLOSURE_PASS` |
| J1 / J2 / J3 / J5 / J7 | retained `REAL_USER_JOURNEY_DIGITAL_PASS` |
| J6 | `HUMAN_VALIDATION_PENDING` |
| Certification claim | always `certification_claimed=false` |

## Evidence

Device OS: `artifacts/complete_experience/cx3/` only.  
Lab: `os_build/cx3_linux_lab/`.

## Concurrency

`/tmp/gunnchos-cx-qemu.lock` — one CX guest; never kill foreign QEMU.

`FULL_COMPLETE_EXPERIENCE_COMPLETE=false`

## Results (Device OS evidence)

| Token | Value |
|-------|-------|
| `CX2H4_P0_DIGITAL_CLOSURE_PASS` | **true** |
| `CX3_CONTRACTS_V1_PASS` | **true** |
| `CX3_LAB_ISSUER_ED25519_PASS` | **true** |
| `CX3_EVIDENCE_BOUND_ISSUANCE_PASS` | **true** |
| `CX3_WALLET_STORAGE_PASS` | **true** |
| `CX3_WALLET_GUI_PASS` | **true** |
| `CX3_SIGNED_CREDENTIAL_JOURNEY_PASS` | **true** |
| `CX3_TAMPER_DETECT_PASS` | **true** |
| `CX3_REVOCATION_STATUS_PASS` | **true** |
| `CX3_OFFLINE_VERIFY_PASS` | **true** |
| `CX3_IMPORT_EXPORT_PASS` | **true** |
| `CX3_PORTFOLIO_GUI_PASS` | **true** |
| `CX3_PORTFOLIO_PRIVACY_EXPORT_PASS` | **true** |
| `CX3_PORTFOLIO_PORTABLE_PACKAGE_PASS` | **true** |
| `CX3_SECURITY_FAIL_CLOSED_PASS` | **true** |
| `CX3_OB3_CLR_ADAPTER_PASS` | **true** |
| `WAIKE_INTEGRATION_SEAM_PASS` | **true** |
| `WAIKE_EARNED_CREDENTIAL_INTEGRATION_PASS` | **false** |
| `CX3_1_WALLET_PORTFOLIO_FOUNDATION_PASS` | **true** |
| `J1_CLASS` / `J2_CLASS` / `J3_CLASS` / `J5_CLASS` / `J7_CLASS` | **REAL_USER_JOURNEY_DIGITAL_PASS** |
| `J6_CLASS` | HUMAN_VALIDATION_PENDING |
| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false** |
| `certification_claimed` | **false** |

### Honest blockers (do not invent PASS)

- WAIKE earned credential integration requires genuine read-only accepted-main proof (not fabricated)
- Do **not** claim Open Badges 3 / CLR conformance
- Do **not** claim accreditation, degrees, diplomas, or certifications

## Next gate

`NEXT_CX_GATE=CX3_2_WAIKE_REAL_EARNED_CREDENTIAL_INTEGRATION` when wallet foundation PASSes and WAIKE earned remains blocked.
