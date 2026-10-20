#!/usr/bin/env bash
# Rebuild the Level 3 lesson documents (DOCX + PDF) from the Markdown in level3/curriculum/.
# Usage: level3/curriculum/build.sh [N]             build Lesson N (default 1) into level3/curriculum/build/ (not committed)
#        level3/curriculum/build.sh [N] --publish   build, then copy the PDF/DOCX into public/level3/downloads/ for the website
# Needs: python3 with python-docx (pip install -r tools/requirements-docs.txt) and LibreOffice (soffice) for the PDF.
# md2docx_L3.py = a copy of level1/curriculum/md2docx_L1.py (the Level 2 converter plus <!-- grid --> tables; <!-- subst --> marks the
# two-sided grammar boxes).
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; REPO="$(cd "$HERE/../.." && pwd)"
PUBLISH=0; LESSON=1
for a in "$@"; do if [ "$a" = "--publish" ]; then PUBLISH=1; else LESSON="$a"; fi; done
PY="${PYTHON:-python3}"; SOFFICE="${SOFFICE:-soffice}"
N="Level3_Lesson${LESSON}"; OUT="$HERE/build"; mkdir -p "$OUT"
cp "$HERE/$N.md" "$OUT/"
ln -sfn "$REPO/level3/images" "$OUT/images"          # the Markdown links to images/<file>.png
echo "== DOCX: $N"
"$PY" "$HERE/md2docx_L3.py" "$OUT/$N.md" "$OUT/$N.docx" "Level 3 ESL · Lesson ${LESSON}"
echo "== PDF (LibreOffice)"
"$SOFFICE" --headless --convert-to pdf --outdir "$OUT" "$OUT/$N.docx" >/dev/null 2>&1
ls -l "$OUT/$N".docx "$OUT/$N".pdf
if [ "$PUBLISH" = 1 ]; then
  D="$REPO/public/level3/downloads"; mkdir -p "$D"
  cp "$OUT/$N.pdf" "$OUT/$N.docx" "$D/"
  echo "== copied into public/level3/downloads/ (now run: python3 scripts/export_content.py)"
fi
