#!/usr/bin/env bash
# One-time setup for the slide tools (AGENTS.md 6.7). Debian/Ubuntu. Safe to run again.
#   bash scripts/slides/setup_tools.sh
set -euo pipefail
need=()
fonts=$(fc-list : family 2>/dev/null || true)
command -v soffice  >/dev/null || need+=(libreoffice-impress)
command -v pdftoppm >/dev/null || need+=(poppler-utils)
grep -q "Noto Color Emoji" <<<"$fonts" || need+=(fonts-noto-color-emoji)
grep -q "DejaVu Sans" <<<"$fonts" || need+=(fonts-dejavu-core)
if [ ${#need[@]} -gt 0 ]; then sudo apt-get update && sudo apt-get install -y "${need[@]}"; fi
python3 -c "import pptx, lxml, PIL" 2>/dev/null || python3 -m pip install --user -r "$(dirname "$0")/requirements.txt"
# Lexend Deca (SIL Open Font License 1.1), the font of every deck. The repo only has the web font (woff2), which
# LibreOffice cannot use, so install the TTF for rendering. The font is NOT committed to the repo.
if ! fc-match -f "%{family}" "Lexend Deca" | grep -qi "Lexend Deca"; then
  mkdir -p ~/.local/share/fonts
  curl -fsSL "https://github.com/google/fonts/raw/main/ofl/lexenddeca/LexendDeca%5Bwght%5D.ttf" -o ~/.local/share/fonts/LexendDeca.ttf
  fc-cache -f >/dev/null
fi
fc-match "Lexend Deca"; soffice --version; pdftoppm -v 2>&1 | head -1; python3 -c "import pptx; print('python-pptx', pptx.__version__)"
