#!/usr/bin/env bash
# Rebuild a Level 3 DRAFT lesson document (DOCX + PDF) from level3/drafts/curriculum/Level3_Lesson<N>.md, then run the lesson checks.
# Usage: level3/drafts/curriculum/build_draft.sh N            build into level3/drafts/curriculum/build/ (not committed)
#        level3/drafts/curriculum/build_draft.sh N --inplace  build, then replace the committed Level3_Lesson<N>.docx/.pdf here
#        level3/drafts/curriculum/build_draft.sh N --images   also redraw the pictures + CREDITS first (needs cairosvg + Pillow + internet)
# Needs: python3 with python-docx (pip install -r tools/requirements-docs.txt) and LibreOffice (soffice) for the PDF.
# Drafts never go to the website: nothing here writes into level3/curriculum, level3/images, level3/audio or public/.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; D="$(cd "$HERE/.." && pwd)"
LESSON=""; INPLACE=0; IMAGES=0
for a in "$@"; do case "$a" in --inplace) INPLACE=1;; --images) IMAGES=1;; *) LESSON="$a";; esac; done
[ -n "$LESSON" ] || { echo "usage: $0 N [--inplace] [--images]"; exit 2; }
PY="${PYTHON:-python3}"; SOFFICE="${SOFFICE:-soffice}"
N="Level3_Lesson${LESSON}"; OUT="$HERE/build"; mkdir -p "$OUT"
if [ "$IMAGES" = 1 ]; then
  ( cd "$D/images/tools" && "$PY" "make_images_L3_L${LESSON}.py" .. && "$PY" make_credits_L3.py "$LESSON" )
fi
cp "$HERE/$N.md" "$OUT/"
ln -sfn "$D/images" "$OUT/images"          # the Markdown links to images/<file>.png
echo "== DOCX: $N"
"$PY" "$HERE/tools/md2docx_L3.py" "$OUT/$N.md" "$OUT/$N.docx" "Level 3 ESL · Lesson ${LESSON}"
echo "== PDF (LibreOffice)"
"$SOFFICE" --headless --convert-to pdf --outdir "$OUT" "$OUT/$N.docx" >/dev/null 2>&1
ls -l "$OUT/$N".docx "$OUT/$N".pdf
if [ "$INPLACE" = 1 ]; then cp "$OUT/$N.docx" "$OUT/$N.pdf" "$HERE/"; echo "== replaced $N.docx/.pdf in level3/drafts/curriculum/"; fi
echo "== lesson checks"
"$PY" "$HERE/tools/check_lesson_L3.py" "$LESSON"
