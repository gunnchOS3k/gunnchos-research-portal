# For RTL Verification Roles

**Lane:** Google Digital Design Verification / RTL / UVM

## Primary evidence

| Artifact | Link |
|----------|------|
| Lab README | [console_rtl_verification_lab/README.md](https://github.com/gunnchOS3k/eg3573-ece-6443-sram-bist-project/blob/main/console_rtl_verification_lab/README.md) |
| Verification plan | [docs/VERIFICATION_PLAN.md](https://github.com/gunnchOS3k/eg3573-ece-6443-sram-bist-project/blob/main/console_rtl_verification_lab/docs/VERIFICATION_PLAN.md) |
| Coverage plan | [docs/COVERAGE_PLAN.md](https://github.com/gunnchOS3k/eg3573-ece-6443-sram-bist-project/blob/main/console_rtl_verification_lab/docs/COVERAGE_PLAN.md) |
| UVM roadmap | [docs/UVM_ROADMAP.md](https://github.com/gunnchOS3k/eg3573-ece-6443-sram-bist-project/blob/main/console_rtl_verification_lab/docs/UVM_ROADMAP.md) |
| Hardware alignment | [docs/CONSOLE_HARDWARE_ALIGNMENT.md](https://github.com/gunnchOS3k/eg3573-ece-6443-sram-bist-project/blob/main/console_rtl_verification_lab/docs/CONSOLE_HARDWARE_ALIGNMENT.md) |
| SRAM BIST RTL | [rtl/gunnchos_sram_bist.sv](https://github.com/gunnchOS3k/eg3573-ece-6443-sram-bist-project/blob/main/console_rtl_verification_lab/rtl/gunnchos_sram_bist.sv) |
| Framebuffer regblock | [rtl/gunnchos_framebuffer_regblock.sv](https://github.com/gunnchOS3k/eg3573-ece-6443-sram-bist-project/blob/main/console_rtl_verification_lab/rtl/gunnchos_framebuffer_regblock.sv) |

## Mock / smoke workflow

```bash
git clone https://github.com/gunnchOS3k/eg3573-ece-6443-sram-bist-project.git
cd eg3573-ece-6443-sram-bist-project/console_rtl_verification_lab
python3 scripts/check_required_files.py
python3 -m pytest tests/test_required_files.py -q
./scripts/run_sim_smoke.sh   # optional if iverilog installed
```

## Skills mapped

| Skill | Portfolio evidence |
|-------|-------------------|
| SystemVerilog RTL | SRAM/BIST + framebuffer register block |
| Directed testbenches | Smoke TBs in `tb/` |
| SVA properties | `sva/` bind-style assertions |
| Verification planning | VERIFICATION_PLAN.md |
| Coverage planning | COVERAGE_PLAN.md (goals — not fabricated tool %) |
| UVM readiness | UVM_ROADMAP.md — **not** full UVM impl |
| Memory/display reasoning | MEMORY_SYSTEM_ARCHITECTURE.md |

## Related console repos

- [gunnchos-hardware-industrial-design](https://github.com/gunnchOS3k/gunnchos-hardware-industrial-design)
- [gunnchos-device-os](https://github.com/gunnchOS3k/gunnchos-device-os)

## What this does not claim

- Not tape-out ready silicon
- UVM environment not fully implemented
- Simulation log in `results/` is **sample expected output** unless re-run locally

## Resume bullets

See [ROLE_SPECIFIC_RESUME_BULLETS.md](ROLE_SPECIFIC_RESUME_BULLETS.md#rtl-verification).
