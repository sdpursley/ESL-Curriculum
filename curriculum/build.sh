#!/usr/bin/env bash
# Rebuild the curriculum documents from curriculum/Level2_Curriculum_v5_public.md:
#   Level2_Curriculum_v5_public.docx/.pdf, and the four exam files (teacher packets + student tests, .md/.docx/.pdf).
# Usage: curriculum/build.sh [OUTPUT_DIR]        (default: curriculum/build, which git ignores)
#        curriculum/build.sh --publish            (build, then copy the files the website offers into public/downloads/)
# Needs: python3 with python-docx (pip install -r tools/requirements-docs.txt) and LibreOffice (soffice) for the PDFs.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; REPO="$(dirname "$HERE")"
PUBLISH=0; OUT="$HERE/build"
for a in "$@"; do if [ "$a" = "--publish" ]; then PUBLISH=1; else OUT="$a"; fi; done
PY="${PYTHON:-python3}"; SOFFICE="${SOFFICE:-soffice}"
mkdir -p "$OUT/exams"; OUT="$(cd "$OUT" && pwd)"
cp "$HERE/Level2_Curriculum_v5_public.md" "$OUT/"
ln -sfn "$REPO/public/images" "$OUT/images"          # the Markdown links to images/<file>.png
N=Level2_Curriculum_v5_public
echo "== DOCX: $N"
"$PY" "$HERE/md2docx.py" "$OUT/$N.md" "$OUT/$N.docx" "Level 2 ESL v5"
echo "== exam Markdown"
BUILD_DIR="$OUT" "$PY" "$HERE/packets.py"
for n in Midterm_Exam_Teacher_Packet Final_Exam_Teacher_Packet Midterm_Student_Test Final_Student_Test; do
  echo "== DOCX: $n"
  "$PY" "$HERE/md2docx.py" "$OUT/exams/$n.md" "$OUT/exams/$n.docx" "© 2026 the authors · CC BY-NC-SA 4.0 · Provided as-is, without warranty"
done
echo "== PDF (LibreOffice)"
"$SOFFICE" --headless --convert-to pdf --outdir "$OUT" "$OUT/$N.docx" >/dev/null 2>&1
"$SOFFICE" --headless --convert-to pdf --outdir "$OUT/exams" "$OUT"/exams/*.docx >/dev/null 2>&1
ls -l "$OUT/$N".* "$OUT"/exams/*.pdf
if [ "$PUBLISH" = 1 ]; then
  D="$REPO/public/downloads"; mkdir -p "$D/exams"
  cp "$OUT/$N.pdf" "$OUT/$N.docx" "$D/"
  for f in Midterm_Exam_Teacher_Packet.pdf Midterm_Exam_Teacher_Packet.docx Midterm_Student_Test.pdf \
           Final_Exam_Teacher_Packet.pdf Final_Exam_Teacher_Packet.docx Final_Student_Test.pdf; do cp "$OUT/exams/$f" "$D/exams/"; done
  echo "== copied into public/downloads/ (now run: python3 scripts/export_content.py)"
fi
