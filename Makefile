.PHONY: bootstrap audit test verify reproduce diagrams uml

PYTHON ?= python3

bootstrap:
	@echo "stdlib-only audit; optional: $(PYTHON) -m pip install pyyaml"

audit:
	$(PYTHON) scripts/audit_portfolio.py --portal-root .

test:
	$(PYTHON) scripts/validate_supervisor_ready.py

verify: audit test
	@echo "portal control-plane verify complete (docs/gates only; not CONTACT_SUPERVISOR_READY)"

reproduce: verify
	@test -f portfolio/supervisor_ready_manifest.yaml
	@test -f docs/phd/PORTFOLIO_READINESS_DASHBOARD.md

diagrams: uml

uml:
	@echo "GitHub renders Mermaid in docs/uml/current/*.md"
	@echo "Optional PlantUML: ./docs/uml/render_plantuml.sh"
