#!/usr/bin/env bash
# Temporary public URL via Cloudflare Quick Tunnel (demo only).
# Requires: python3, cloudflared in PATH (https://github.com/cloudflare/cloudflared/releases)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT/publish"
python3 -m http.server 8765 &
HTTP_PID=$!
cleanup() {
  kill "$HTTP_PID" 2>/dev/null || true
}
trap cleanup EXIT INT TERM
sleep 1
exec cloudflared tunnel --url http://127.0.0.1:8765
