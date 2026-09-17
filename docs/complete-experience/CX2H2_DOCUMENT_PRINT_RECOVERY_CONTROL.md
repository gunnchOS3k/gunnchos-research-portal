# CX2H.2 Control — Document / Print / Recovery (J1 + J7)

Stacked on Portal CX2H.1B (`docs/cx2h-journey-digital-pass-control`).  
Does **not** touch Portal #14/#15.

## Device OS DRAFT stack

| PR | Branch | Base |
|----|--------|------|
| CX2H.1B recovery | `eng/cx2h-journey-digital-pass-closure` | CX2G |
| CX2H.2 (this wave) | `eng/cx2h2-document-print-recovery-j1-j7` | CX2H.1B |

## Scope

1. Recover CX2H.1B reviewability (strict J3 Flatpak window/version proof) via DRAFT PRs
2. Real Writer GUI → Vault ODT → PDF export → CUPS/IPP digital print
3. Vault/Care GUI backup → destructive delete/corrupt → GUI restore → Writer reopen
4. Earn J1 + J7 `REAL_USER_JOURNEY_DIGITAL_PASS` only when all criteria met
5. Stop — do not attempt J2/J5; do not start CX3

## Separated truth lanes

| Lane | Token |
|------|-------|
| Shell + J3 prereq | `CX2H_SHELL_PREREQ_PASS` + `J3_CLASS=REAL_USER_JOURNEY_DIGITAL_PASS` |
| Writer GUI | `CX2H2_REAL_WRITER_GUI_PASS` |
| Vault file provider | `CX2H2_REAL_VAULT_FILE_PASS` |
| PDF export GUI | `CX2H2_REAL_PDF_EXPORT_GUI_PASS` |
| CUPS/IPP provider | `CX2H2_REAL_IPP_PROVIDER_PASS` |
| Print GUI | `CX2H2_REAL_IPP_PRINT_GUI_PASS` |
| Backup GUI | `CX2H2_REAL_BACKUP_GUI_PASS` |
| Restore GUI | `CX2H2_REAL_RESTORE_GUI_PASS` |
| Persistence | `CX2H2_PERSISTENCE_PASS` |
| Physical printer | `CX2H2_PHYSICAL_PRINTER_PENDING=true` (always) |
| J1 / J7 | `J1_CLASS` / `J7_CLASS` |
| J2 / J5 | `BLOCKED` |
| J6 | `HUMAN_VALIDATION_PENDING` |
| Human a11y | `CX2H_HUMAN_A11Y_PENDING=true` |

## Evidence

Device OS: `artifacts/complete_experience/cx2h2/` only.  
Lab: `os_build/cx2h2_linux_lab/` (CX2H overlay child).

## Concurrency

`/tmp/gunnchos-cx-qemu.lock` — one CX guest; never kill foreign QEMU.

`FULL_COMPLETE_EXPERIENCE_COMPLETE=false`

## Results (Device OS evidence 2026-09-17T15:21:41Z)

| Token | Value |
|-------|-------|
| `CX2H2_REAL_WRITER_GUI_PASS` | **true** |
| `CX2H2_REAL_VAULT_FILE_PASS` | **true** |
| `CX2H2_REAL_PDF_EXPORT_GUI_PASS` | **true** (`gui_live_uno_writer_pdf_Export`) |
| `CX2H2_REAL_IPP_PROVIDER_PASS` | **true** (CUPS/IPP `CX2H2_Digital_IPP` cups-pdf) |
| `CX2H2_REAL_IPP_PRINT_GUI_PASS` | **true** |
| `CX2H2_REAL_BACKUP_GUI_PASS` | **true** |
| `CX2H2_REAL_RESTORE_GUI_PASS` | **true** |
| `CX2H2_PERSISTENCE_PASS` | **true** |
| `CX2H2_PHYSICAL_PRINTER_PENDING` | **true** |
| `J1_CLASS` | **REAL_USER_JOURNEY_DIGITAL_PASS** |
| `J3_CLASS` | **REAL_USER_JOURNEY_DIGITAL_PASS** (1B preserved) |
| `J7_CLASS` | **REAL_USER_JOURNEY_DIGITAL_PASS** |
| `J2_CLASS` / `J5_CLASS` | BLOCKED |
| `J6_CLASS` | HUMAN_VALIDATION_PENDING |
| `FULL_COMPLETE_EXPERIENCE_COMPLETE` | **false** |

## Next gate

`NEXT_CX_GATE=CX2H3_BROWSER_MAIL_OFFLINE_J2_J5`
