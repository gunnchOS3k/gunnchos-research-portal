# For Access Risk Security Roles

**Lane:** Google PRISM / Access Risk Security Engineer

## Primary evidence

| Artifact | Link |
|----------|------|
| Alignment doc | [gunnchos-device-os/docs/ACCESS_RISK_INTELLIGENCE_ALIGNMENT.md](https://github.com/gunnchOS3k/gunnchos-device-os/blob/main/docs/ACCESS_RISK_INTELLIGENCE_ALIGNMENT.md) |
| Security invariants | [docs/SECURITY_INVARIANTS.md](https://github.com/gunnchOS3k/gunnchos-device-os/blob/main/docs/SECURITY_INVARIANTS.md) |
| Zero-trust model | [docs/ZERO_TRUST_DEVICE_ACCESS_MODEL.md](https://github.com/gunnchOS3k/gunnchos-device-os/blob/main/docs/ZERO_TRUST_DEVICE_ACCESS_MODEL.md) |
| Access graph model | [security/access-risk/ACCESS_GRAPH_MODEL.md](https://github.com/gunnchOS3k/gunnchos-device-os/blob/main/security/access-risk/ACCESS_GRAPH_MODEL.md) |
| Risk report (mock) | [security/access-risk/risk_report_example.md](https://github.com/gunnchOS3k/gunnchos-device-os/blob/main/security/access-risk/risk_report_example.md) |
| Walkthrough | [demo/access_risk_walkthrough.md](https://github.com/gunnchOS3k/gunnchos-device-os/blob/main/demo/access_risk_walkthrough.md) |

## Mock workflow

```bash
git clone https://github.com/gunnchOS3k/gunnchos-device-os.git
cd gunnchos-device-os
python3 security/access-risk/attack_path_model.py
python3 security/access-risk/least_privilege_recommender.py
python3 -m pytest tests/test_access_risk_model.py -q
```

## Skills mapped

| Skill | Portfolio evidence |
|-------|-------------------|
| IAM modeling | Mock identities, resources, bindings JSON |
| Attack path analysis | `attack_path_model.py` graph + risky paths |
| Least privilege | `least_privilege_recommender.py` markdown table |
| Access governance | Security invariants + zero-trust doc |
| Device/cloud risk | gunnchOS console role separation (student/educator/research/admin) |

## What this does not claim

- Not production PRISM or enterprise IAM integration
- Mock bindings only — no real tenant data
- Not a certified secure device deployment

## Resume bullets

See [ROLE_SPECIFIC_RESUME_BULLETS.md](ROLE_SPECIFIC_RESUME_BULLETS.md#access-risk).
