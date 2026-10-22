#!/usr/bin/env bash
# Render every slide of a deck to JPEG so you can look at it (AGENTS.md section 6).
# Usage: scripts/slides/render_deck.sh <deck.pptx> <outdir> [dpi=60]
#   -> <outdir>/<deck>.pdf and <outdir>/slide-01.jpg, slide-02.jpg, ...
# Needs LibreOffice (soffice) and poppler (pdftoppm). Fonts: Lexend Deca must be installed (the slide font) and an emoji
# font (Noto Color Emoji) for the faces 😀 🙂 😐; without Lexend Deca text renders in a fallback font and line breaks lie.
set -euo pipefail
deck=${1:?usage: render_deck.sh deck.pptx outdir [dpi]}; out=${2:?outdir}; dpi=${3:-60}
command -v soffice >/dev/null || { echo "soffice not found: install LibreOffice (apt-get install -y libreoffice-impress)"; exit 2; }
command -v pdftoppm >/dev/null || { echo "pdftoppm not found: apt-get install -y poppler-utils"; exit 2; }
if ! fc-match -f "%{family}" "Lexend Deca" | grep -qi "Lexend Deca"; then
  echo "WARNING: font 'Lexend Deca' is not installed; renders will not match PowerPoint. See AGENTS.md 6.7 (fonts)." >&2
fi
mkdir -p "$out"
rm -f "$out"/slide-*.jpg
prof=$(mktemp -d)   # private LibreOffice profile: avoids clashes with a running soffice
soffice -env:UserInstallation=file://$prof --headless --convert-to pdf --outdir "$out" "$deck" >/dev/null 2>&1
rm -rf "$prof"
pdf="$out/$(basename "${deck%.*}").pdf"
[ -s "$pdf" ] || { echo "LibreOffice did not write $pdf"; exit 1; }
pdftoppm -jpeg -r "$dpi" "$pdf" "$out/slide"
# pdftoppm names files slide-1.jpg or slide-01.jpg depending on the page count: normalize to two digits
for f in "$out"/slide-*.jpg; do
  n=$(basename "$f" .jpg); n=${n#slide-}; mv -n "$f" "$out/slide-$(printf %02d "$((10#$n))").jpg" 2>/dev/null || true
done
echo "$(ls "$out"/slide-*.jpg | wc -l) slides rendered to $out/slide-NN.jpg (pdf: $pdf)"
