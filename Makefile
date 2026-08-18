.PHONY: bootstrap audit test verify reproduce diagrams uml supervisor-snapshot paper

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

supervisor-snapshot:
	$(PYTHON) scripts/supervisor_snapshot.py

paper:
	@echo "Manuscript SoT lives in research repos; portal indexes research_manuscripts/"
	@test -f research_manuscripts/VENUE_READINESS_MATRIX.md
	@test -f research_manuscripts/paper1_service_continuity/README.md
	@test -f research_manuscripts/paper2_cross_layer_orchestration/README.md
	@test -f research_manuscripts/paper3_tn_ntn_resilience/README.md
