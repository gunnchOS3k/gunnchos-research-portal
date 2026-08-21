.PHONY: bootstrap audit test verify reproduce diagrams uml supervisor-snapshot paper code-health-r5-s1

PYTHON ?= python3

bootstrap:
	@echo "stdlib-only audit; optional: $(PYTHON) -m pip install pyyaml pytest"

audit:
	$(PYTHON) scripts/audit_portfolio.py --portal-root .

test:
	$(PYTHON) scripts/validate_supervisor_ready.py
	$(PYTHON) -m pytest -q tests/test_audit_portfolio.py

code-health-r5-s1: test
	$(PYTHON) scripts/run_r5_s1_mutation_kills.py
	$(PYTHON) scripts/write_r5_s1_evidence.py

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
