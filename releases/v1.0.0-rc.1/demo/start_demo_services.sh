#!/usr/bin/env bash
# RC1 career-fair demo bootstrap — one command before the Pixel demo.
# Starts WAIKE Hub (seeded), adb reverse, optional Nearby Edge.
# Prints no secrets. Device alias: PIXEL_V1_DEMO_DEVICE (serial never committed).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
DEMO_DIR="$(cd "$(dirname "$0")" && pwd)"
STATE_DIR="${DEMO_DIR}/.runtime"
mkdir -p "$STATE_DIR"

# Portal may be a nested worktree; default to sibling repos under .../repos/
REPOS_ROOT="$(cd "$ROOT/../../.." && pwd)"
if [[ ! -d "$REPOS_ROOT/gunnchos-waike-learning-platform" ]]; then
  REPOS_ROOT="$(cd "$ROOT/.." && pwd)"
fi
WLP_ROOT="${WAIKE_LP_ROOT:-$REPOS_ROOT/gunnchos-waike-learning-platform}"
WAIKE_OPS_ROOT="${WAIKE_ROOT:-$REPOS_ROOT/waike-research-ops}"
GUNNCHAI_ROOT="${GUNNCHAI_ROOT:-$REPOS_ROOT/gunnchAI3k}"

HUB_PORT="${HUB_PORT:-8010}"
NEARBY_PORT="${NEARBY_PORT:-8791}"
ADB_BIN="${ADB_BIN:-adb}"
PYTHON_BIN="${PYTHON_BIN:-}"

log() { printf '[demo-bootstrap] %s\n' "$*"; }
fail() { printf '[demo-bootstrap] ERROR: %s\n' "$*" >&2; exit 1; }

resolve_python() {
  if [[ -n "$PYTHON_BIN" && -x "$PYTHON_BIN" ]]; then
    return 0
  fi
  for candidate in \
    "$WLP_ROOT/.venv/bin/python" \
    "$WLP_ROOT/.venv/bin/python3" \
    "$(command -v python3 || true)"; do
    if [[ -x "$candidate" ]] && "$candidate" -c 'import fastapi, uvicorn' 2>/dev/null; then
      PYTHON_BIN="$candidate"
      return 0
    fi
  done
  fail "no Python with fastapi/uvicorn found (set PYTHON_BIN to WAIKE LP .venv)"
}

require_exclusive_pixel() {
  # macOS ships Bash 3.2 — avoid mapfile
  local devices device_count
  devices="$("$ADB_BIN" devices | awk 'NR>1 && $2=="device" {print $1}')"
  device_count="$(printf '%s\n' "$devices" | awk 'NF{c++} END{print c+0}')"
  if [[ "$device_count" != "1" ]]; then
    fail "expected exactly one authorized adb device (PIXEL_V1_DEMO_DEVICE); found ${device_count}"
  fi
  export ANDROID_SERIAL="$(printf '%s\n' "$devices" | awk 'NF{print; exit}')"
  # Do not echo raw serial into committed logs; alias only.
  log "exclusive device bound as PIXEL_V1_DEMO_DEVICE"
}

wait_http() {
  local url="$1" timeout="${2:-90}"
  local deadline=$((SECONDS + timeout))
  while (( SECONDS < deadline )); do
    if curl -fsS "$url" >/dev/null 2>&1; then
      return 0
    fi
    sleep 1
  done
  return 1
}

start_hub() {
  [[ -d "$WLP_ROOT/services/hub" ]] || fail "WAIKE LP not found at $WLP_ROOT (set WAIKE_LP_ROOT)"
  [[ -d "$WAIKE_OPS_ROOT" ]] || fail "waike-research-ops not found at $WAIKE_OPS_ROOT (set WAIKE_ROOT)"

  local db="$STATE_DIR/hub_rc1_demo.sqlite3"
  rm -f "$db" "$db"-*

  export WAIKE_ROOT="$WAIKE_OPS_ROOT"
  export PYTHONPATH="$WLP_ROOT/services/hub${PYTHONPATH:+:$PYTHONPATH}"
  export WAIKE_PIXEL_PILOT=true
  export WAIKE_DEV_DB_KEY="${WAIKE_DEV_DB_KEY:-0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef}"

  log "seeding pilot users + 18-track curriculum (credentials stay under $STATE_DIR, gitignored)"
  "$PYTHON_BIN" "$WLP_ROOT/tools/pixel_pilot/create_test_users.py" \
    --db "$db" \
    --credentials "$STATE_DIR/credentials.json" \
    --manifest "$STATE_DIR/ROLE_TEST_MANIFEST.json" \
    --inventory "$STATE_DIR/FULL_18_TRACK_RUNTIME_INVENTORY.json" \
    >/dev/null

  # Launcher: unset WAIKE_PIXEL_PILOT during app.main import (module-level create_app side effect)
  cat > "$STATE_DIR/hub_launcher.py" <<PY
import os
from pathlib import Path
os.environ.pop("WAIKE_PIXEL_PILOT", None)
os.environ.setdefault("WAIKE_DEV_DB_KEY", "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef")
from app.main import HubConfig, create_app
import uvicorn
from app.pilot.full_curriculum_seed import inventory_from_db
db = Path(r"$db")
os.environ["WAIKE_PIXEL_PILOT"] = "true"
app = create_app(
    config=HubConfig(production_auth_enabled=True, fixture_auth_enabled=False, version="rc1-demo"),
    db_path=db,
    seed=False,
)
app.state.curriculum_inventory = inventory_from_db(app.state.db)
app.state.pixel_pilot = True
uvicorn.run(app, host="127.0.0.1", port=$HUB_PORT, log_level="warning")
PY

  if [[ -f "$STATE_DIR/hub.pid" ]] && kill -0 "$(cat "$STATE_DIR/hub.pid")" 2>/dev/null; then
    log "hub already running pid=$(cat "$STATE_DIR/hub.pid")"
  else
    log "starting WAIKE Hub on 127.0.0.1:$HUB_PORT with $PYTHON_BIN"
    nohup "$PYTHON_BIN" "$STATE_DIR/hub_launcher.py" >"$STATE_DIR/hub.log" 2>&1 &
    echo $! >"$STATE_DIR/hub.pid"
  fi

  wait_http "http://127.0.0.1:${HUB_PORT}/healthz" 90 || fail "hub healthz failed — see $STATE_DIR/hub.log"
  log "hub healthy"
}

adb_reverse() {
  require_exclusive_pixel
  "$ADB_BIN" reverse "tcp:${HUB_PORT}" "tcp:${HUB_PORT}"
  "$ADB_BIN" reverse "tcp:${NEARBY_PORT}" "tcp:${NEARBY_PORT}" || true
  local listed
  listed="$("$ADB_BIN" reverse --list 2>/dev/null || true)"
  printf '%s\n' "$listed" | grep -q "tcp:${HUB_PORT}" || fail "adb reverse for hub :${HUB_PORT} not listed"
  # Device images may lack curl; host healthz + reverse listing is sufficient proof.
  log "adb reverse OK (hub:$HUB_PORT listed; host healthz already green)"
}

start_nearby_edge() {
  # Best-effort Nearby Mac AI on accepted-main product-service port.
  if [[ ! -d "$GUNNCHAI_ROOT" ]]; then
    log "gunnchAI root missing — Nearby Edge skipped (honest unavailable on device)"
    echo "unavailable" >"$STATE_DIR/nearby_edge.status"
    return 0
  fi
  if curl -fsS "http://127.0.0.1:${NEARBY_PORT}/health" >/dev/null 2>&1 \
     || curl -fsS "http://127.0.0.1:${NEARBY_PORT}/healthz" >/dev/null 2>&1; then
    log "Nearby Edge already healthy on :$NEARBY_PORT"
    echo "running" >"$STATE_DIR/nearby_edge.status"
    return 0
  fi
  if [[ -f "$GUNNCHAI_ROOT/package.json" ]] && command -v npx >/dev/null 2>&1; then
    log "attempting Nearby Edge / product-service on :$NEARBY_PORT"
    (
      cd "$GUNNCHAI_ROOT"
      nohup npx --yes tsx src/system-layer/product_service/cli.ts serve --port "$NEARBY_PORT" \
        >"$STATE_DIR/nearby_edge.log" 2>&1 &
      echo $! >"$STATE_DIR/nearby_edge.pid"
    ) || true
    if wait_http "http://127.0.0.1:${NEARBY_PORT}/health" 25 \
       || wait_http "http://127.0.0.1:${NEARBY_PORT}/healthz" 5; then
      echo "running" >"$STATE_DIR/nearby_edge.status"
      log "Nearby Edge healthy — use truthful Nearby Mac label in demo"
    else
      echo "unavailable" >"$STATE_DIR/nearby_edge.status"
      log "Nearby Edge did not become healthy — demo must show honest unavailable (no fake AI)"
    fi
  else
    echo "unavailable" >"$STATE_DIR/nearby_edge.status"
    log "Nearby Edge not started (tsx/npx unavailable) — honest unavailable"
  fi
}

write_status() {
  cat >"$STATE_DIR/BOOTSTRAP_STATUS.json" <<JSON
{
  "schema": "RC1_DEMO_BOOTSTRAP_STATUS/v1",
  "device_alias": "PIXEL_V1_DEMO_DEVICE",
  "serial_committed": false,
  "hub_port": $HUB_PORT,
  "hub_health": "http://127.0.0.1:${HUB_PORT}/healthz",
  "nearby_edge_port": $NEARBY_PORT,
  "nearby_edge_status": "$(cat "$STATE_DIR/nearby_edge.status" 2>/dev/null || echo unknown)",
  "credentials_path": "releases/v1.0.0-rc.1/demo/.runtime/credentials.json",
  "secrets_printed": false,
  "notes": "Credentials file is gitignored runtime state. Do not commit."
}
JSON
  log "status → $STATE_DIR/BOOTSTRAP_STATUS.json"
}

# Ensure runtime dir is gitignored
if ! grep -q 'demo/.runtime' "$ROOT/.gitignore" 2>/dev/null; then
  printf '\n# RC1 demo runtime (credentials, pids)\nreleases/v1.0.0-rc.1/demo/.runtime/\n' >>"$ROOT/.gitignore"
fi

require_exclusive_pixel
resolve_python
log "using PYTHON_BIN=$PYTHON_BIN"
start_hub
adb_reverse
start_nearby_edge
write_status

log "READY — run the 3-minute recruiter path on PIXEL_V1_DEMO_DEVICE with no further terminal steps."
log "Learner credentials: see $STATE_DIR/ROLE_TEST_MANIFEST.json (no passwords) + local credentials.json (gitignored)."
