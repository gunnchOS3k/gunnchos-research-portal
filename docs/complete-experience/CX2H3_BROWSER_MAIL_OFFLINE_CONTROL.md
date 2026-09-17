# CX2H.3 Control — Browser / Mail / Offline-Reconnect (J2 + J5)

Stacked on Portal CX2H.2 (`docs/cx2h2-document-print-recovery-control`).  
Does **not** touch Portal #14/#15.

## Device OS DRAFT stack

| PR | Branch | Base |
|----|--------|------|
| CX2H.1B | `eng/cx2h-journey-digital-pass-closure` | CX2G |
| CX2H.2 | `eng/cx2h2-document-print-recovery-j1-j7` | CX2H.1B |
| CX2H.3 (this wave) | `eng/cx2h3-browser-mail-offline-j2-j5` | CX2H.2 |

## Scope

1. Prerequisite rebind of J1/J3/J7 digital pass truth
2. Real HTTPS provider + trusted CA (no ignore-cert PASS)
3. Real Chromium GUI download into Vault
4. Vault → Writer edit of download
5. Real SMTP+IMAP (two accounts) + Thunderbird GUI send/receive/attachment
6. J2 restart/read-back
7. Genuine offline boundary; offline doc + mail queue; restart while offline
8. Reconnect exactly-once + controlled reconnect failure recovery
9. Earn J2 + J5 `REAL_USER_JOURNEY_DIGITAL_PASS` only when all criteria met
10. Stop — do not start CX2H4/CX3

## Separated truth lanes

| Lane | Token |
|------|-------|
| Prerequisite | `CX2H3_PREREQUISITE_PASS` |
| HTTPS provider | `CX2H3_REAL_HTTPS_PROVIDER_PASS` |
| Browser GUI | `CX2H3_REAL_BROWSER_GUI_PASS` |
| HTTPS download GUI | `CX2H3_REAL_HTTPS_DOWNLOAD_GUI_PASS` |
| Document edit | `CX2H3_DOWNLOADED_DOCUMENT_EDIT_PASS` |
| SMTP/IMAP | `CX2H3_REAL_SMTP_IMAP_PROVIDER_PASS` |
| Mail GUI | `CX2H3_REAL_MAIL_GUI_PASS` |
| Attachment roundtrip | `CX2H3_REAL_MAIL_ATTACHMENT_ROUNDTRIP_PASS` |
| J2 persistence | `CX2H3_J2_PERSISTENCE_PASS` |
| Offline local work | `CX2H3_REAL_OFFLINE_LOCAL_WORK_PASS` |
| Offline mail queue | `CX2H3_REAL_OFFLINE_MAIL_QUEUE_PASS` |
| Offline restart | `CX2H3_OFFLINE_RESTART_PERSISTENCE_PASS` |
| Exactly-once | `CX2H3_EXACTLY_ONCE_RECONCILIATION_PASS` |
| Reconnect failure recovery | `CX2H3_RECONNECT_FAILURE_RECOVERY_PASS` |
| J1 / J3 / J7 | retained `REAL_USER_JOURNEY_DIGITAL_PASS` |
| J2 / J5 | set by evidence |
| J6 | `HUMAN_VALIDATION_PENDING` |

## Evidence

Device OS: `artifacts/complete_experience/cx2h3/` only.  
Lab: `os_build/cx2h3_linux_lab/`.

## Concurrency

`/tmp/gunnchos-cx-qemu.lock` — one CX guest; never kill foreign QEMU.

`FULL_COMPLETE_EXPERIENCE_COMPLETE=false`

## Results (Device OS evidence 2026-09-17)

| Token | Value |
|-------|-------|
| `CX2H3_PREREQUISITE_PASS` | **true** |
| `CX2H3_REAL_HTTPS_PROVIDER_PASS` | **true** |
| `CX2H3_REAL_BROWSER_GUI_PASS` | **true** |
| `CX2H3_REAL_HTTPS_DOWNLOAD_GUI_PASS` | **true** |
| `CX2H3_DOWNLOADED_DOCUMENT_EDIT_PASS` | **true** |
| `CX2H3_REAL_SMTP_IMAP_PROVIDER_PASS` | **true** |
| `CX2H3_REAL_MAIL_GUI_PASS` | **true** |
| `CX2H3_REAL_MAIL_ATTACHMENT_ROUNDTRIP_PASS` | **true** |
| `CX2H3_J2_PERSISTENCE_PASS` | **true** |
| `CX2H3_REAL_OFFLINE_LOCAL_WORK_PASS` | **true** |
| `CX2H3_REAL_OFFLINE_MAIL_QUEUE_PASS` | **true** |
| `CX2H3_OFFLINE_RESTART_PERSISTENCE_PASS` | **true** |
| `CX2H3_EXACTLY_ONCE_RECONCILIATION_PASS` | **true** |
| `CX2H3_RECONNECT_FAILURE_RECOVERY_PASS` | **true** |
| `J1_CLASS` / `J3_CLASS` / `J7_CLASS` | **REAL_USER_JOURNEY_DIGITAL_PASS** |
| `J2_CLASS` / `J5_CLASS` | **REAL_USER_JOURNEY_DIGITAL_PASS** |
| `J6_CLASS` | HUMAN_VALIDATION_PENDING |
| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false** |

## Next gate

`NEXT_CX_GATE=CX2H4_P0_DIGITAL_CLOSURE_AUDIT`

Portal follow-on: `docs/cx2h4-p0-digital-closure-control` (CX2H.4).
