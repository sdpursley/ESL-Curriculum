#!/usr/bin/env bash
# Rebuild the Level 1 lesson documents (DOCX + PDF) from the Markdown in level1/curriculum/.
# Usage: level1/curriculum/build.sh [N]             build Lesson N (default 1) into level1/curriculum/build/ (not committed)
#        level1/curriculum/build.sh [N] --publish   build, then copy the PDF/DOCX into public/level1/downloads/ for the website
# Needs: python3 with python-docx (pip install -r tools/requirements-docs.txt) and LibreOffice (soffice) for the PDF.
# md2docx_L1.py = the Level 2 converter (curriculum/md2docx.py) plus one table type: <!-- grid --> (alphabet / letter grids).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; REPO="$(cd "$HERE/../.." && pwd)"
PUBLISH=0; LESSON=1
for a in "$@"; do if [ "$a" = "--publish" ]; then PUBLISH=1; else LESSON="$a"; fi; done
PY="${PYTHON:-python3}"; SOFFICE="${SOFFICE:-soffice}"
N="Level1_Lesson${LESSON}"; OUT="$HERE/build"; mkdir -p "$OUT"
cp "$HERE/$N.md" "$OUT/"
ln -sfn "$REPO/level1/images" "$OUT/images"          # the Markdown links to images/<file>.png
echo "== DOCX: $N"
"$PY" "$HERE/md2docx_L1.py" "$OUT/$N.md" "$OUT/$N.docx" "Level 1 ESL · Lesson ${LESSON}"
echo "== PDF (LibreOffice)"
"$SOFFICE" --headless --convert-to pdf --outdir "$OUT" "$OUT/$N.docx" >/dev/null 2>&1
ls -l "$OUT/$N".docx "$OUT/$N".pdf
if [ "$PUBLISH" = 1 ]; then
  D="$REPO/public/level1/downloads"; mkdir -p "$D"
  cp "$OUT/$N.pdf" "$OUT/$N.docx" "$D/"
  echo "== copied into public/level1/downloads/ (now run: python3 scripts/export_content.py)"
fi
