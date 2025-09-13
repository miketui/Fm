#!/usr/bin/env bash

# Build a distributable EPUB from the working tree
# Usage: scripts/build-epub.sh [output_epub_path]

set -euo pipefail

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log() { echo -e "${BLUE}ℹ️  $*${NC}"; }
ok() { echo -e "${GREEN}✅ $*${NC}"; }
warn() { echo -e "${YELLOW}⚠️  $*${NC}"; }
err() { echo -e "${RED}❌ $*${NC}"; }

OUT_PATH=${1:-dist/curls-and-contemplation.epub}

main() {
  log "Preparing EPUB build..."

  # Sanity checks
  local missing=()
  [[ -f mimetype ]] || missing+=("mimetype")
  [[ -f META-INF/container.xml ]] || missing+=("META-INF/container.xml")
  [[ -f OEBPS/content.opf ]] || missing+=("OEBPS/content.opf")
  [[ -f OEBPS/text/nav.xhtml ]] || warn "OEBPS/text/nav.xhtml not found (TOC). Ensure OPF references a nav document."

  if (( ${#missing[@]} > 0 )); then
    err "Missing required files: ${missing[*]}"
    exit 1
  fi

  # Verify OPF references nav doc
  if ! grep -q 'properties="nav"' OEBPS/content.opf; then
    warn "content.opf does not declare a nav item (properties=\"nav\"). Clickable TOC may be degraded."
  else
    ok "OPF declares navigation document"
  fi

  # Build in temp dir
  TMP_BUILD_DIR=$(mktemp -d)
  cleanup() { if [[ -n "${TMP_BUILD_DIR:-}" ]] && [[ -d "$TMP_BUILD_DIR" ]]; then rm -rf "$TMP_BUILD_DIR"; fi; }
  trap cleanup EXIT

  mkdir -p "$TMP_BUILD_DIR/epub/META-INF" "$TMP_BUILD_DIR/epub/OEBPS" "$(dirname "$OUT_PATH")"

  # Copy tree
  cp -R META-INF "$TMP_BUILD_DIR/epub/" \
    && cp -R OEBPS "$TMP_BUILD_DIR/epub/" \
    && cp mimetype "$TMP_BUILD_DIR/epub/mimetype"

  # Zip with correct ordering
  log "Packaging EPUB → $OUT_PATH"
  if command -v zip >/dev/null 2>&1; then
    (cd "$TMP_BUILD_DIR/epub" && {
      rm -f ../book.epub
      zip -X0 ../book.epub mimetype >/dev/null
      zip -Xr9D ../book.epub META-INF OEBPS >/dev/null
    })
  elif command -v python3 >/dev/null 2>&1; then
    log "zip not found; using python3 zipfile fallback"
    python3 - "$TMP_BUILD_DIR/epub" "$TMP_BUILD_DIR/book.epub" <<'PY'
import os, sys, zipfile
src = sys.argv[1]
out = sys.argv[2]
with zipfile.ZipFile(out, 'w') as z:
    # mimetype first, stored (no compression)
    mime_path = os.path.join(src, 'mimetype')
    z.write(mime_path, arcname='mimetype', compress_type=zipfile.ZIP_STORED)
    # add META-INF and OEBPS recursively (deflated)
    for top in ('META-INF', 'OEBPS'):
        base = os.path.join(src, top)
        for root, _, files in os.walk(base):
            for f in files:
                p = os.path.join(root, f)
                arc = os.path.relpath(p, src)
                if arc == 'mimetype':
                    continue
                z.write(p, arcname=arc, compress_type=zipfile.ZIP_DEFLATED)
PY
  else
    err "Neither 'zip' nor 'python3' available to package EPUB"
    exit 1
  fi

  mv "$TMP_BUILD_DIR/book.epub" "$OUT_PATH"
  ok "EPUB built at $OUT_PATH"

  # Optional epubcheck
  if command -v epubcheck >/dev/null 2>&1; then
    log "Running epubcheck validation on output..."
    if epubcheck "$OUT_PATH"; then
      ok "epubcheck passed"
    else
      err "epubcheck reported issues for $OUT_PATH"
      exit 2
    fi
  else
    warn "epubcheck not found. Skipping final validation. Use: npm run validate or npm i -g epubcheck"
  fi
}

main "$@"
