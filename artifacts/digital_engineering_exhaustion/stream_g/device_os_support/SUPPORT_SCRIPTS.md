# Support scripts (digital inventory)

| Script / module | Path | Role |
|-----------------|------|------|
| SupportBundleBuilder | `gunnchos_device_os/cx0/support_bundle.py` | Redacted bundle scaffold |
| SupportLifecycle | `gunnchos_device_os/phase_xv/support_lifecycle` | Bundle tar, EOL, CVE bulletin scaffold |
| support_self_service | `gunnchos_device_os/cont_ix/support_self_service.py` | Self-service flows |
| diagnostics_collect | `gunnchos_device_os/a_pkt003/diagnostics_collect.py` | Diagnostics collect |
| factory RMA tests | `tests/ops/test_rma_support.py` | Digital RMA workflow tests |

Run: `pytest -q tests/ops/test_rma_support.py tests/test_diagnostics_log.py` (when present on branch).
