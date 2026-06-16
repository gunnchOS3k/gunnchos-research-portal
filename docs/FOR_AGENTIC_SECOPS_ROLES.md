# For Agentic SecOps Roles

**Lane:** Google / Mandiant — Associate Security Analyst, Agentic Security Operations

## Primary evidence

| Artifact | Link |
|----------|------|
| Alignment doc | [gunnchAI3k/docs/AGENTIC_SECOPS_ALIGNMENT.md](https://github.com/gunnchOS3k/gunnchAI3k/blob/main/docs/AGENTIC_SECOPS_ALIGNMENT.md) |
| GenAI security risks | [docs/GENAI_SECURITY_RISKS.md](https://github.com/gunnchOS3k/gunnchAI3k/blob/main/docs/GENAI_SECURITY_RISKS.md) |
| Privacy / safety | [docs/SECOPS_PRIVACY_AND_SAFETY.md](https://github.com/gunnchOS3k/gunnchAI3k/blob/main/docs/SECOPS_PRIVACY_AND_SAFETY.md) |
| Demo README | [docs/SECOPS_DEMO_README.md](https://github.com/gunnchOS3k/gunnchAI3k/blob/main/docs/SECOPS_DEMO_README.md) |
| Walkthrough | [demo/secops_triage_walkthrough.md](https://github.com/gunnchOS3k/gunnchAI3k/blob/main/demo/secops_triage_walkthrough.md) |

## Mock workflow

```bash
git clone https://github.com/gunnchOS3k/gunnchAI3k.git
cd gunnchAI3k
python3 scripts/secops_mock_ioc_extractor.py \
  --input examples/mock_threat_report.md \
  --output examples/ioc_extraction_output.json
python3 scripts/secops_mock_rule_generator.py
pip install -r requirements-secops.txt
pytest tests/test_secops_mock_ioc_extractor.py tests/test_secops_artifacts_exist.py -q
```

## Skills mapped

| Skill | Portfolio evidence |
|-------|-------------------|
| AI-assisted SOC triage | Structured walkthrough + triage summary template |
| IOC extraction | Offline regex extractor → JSON schema |
| Detection engineering | YARA-L / Sigma **mock** skeletons |
| Response playbooks | [playbooks/](https://github.com/gunnchOS3k/gunnchAI3k/tree/main/playbooks) |
| GenAI safety | Prompt injection, hallucination, leakage controls documented |
| SIEM-style investigation | Mock threat report → structured indicators (not live SIEM) |

## What this does not claim

- Not connected to a real SIEM or production SOC
- No real customer data or live malware analysis
- Not a production automation platform

## Resume bullets

See [ROLE_SPECIFIC_RESUME_BULLETS.md](ROLE_SPECIFIC_RESUME_BULLETS.md#agentic-secops).
