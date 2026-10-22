#!/usr/bin/env bash
# Rebuild everything for the Level 1 exams except the audio (audio: build/audio/run_audio.sh, then build/audio/finish_audio.sh).
# Usage: level1/exams/build/build_all.sh [--publish]
#   writes the pictures (level1/exams/images/), the four Markdown files (level1/exams/), and DOCX + PDF into level1/exams/build/out/ (not committed);
#   --publish also copies the teacher packets (PDF + DOCX) and student tests (PDF) into public/level1/downloads/exams/ for the website.
# Needs: python3 + python-docx, LibreOffice (soffice), poppler-utils (pdfinfo); the pictures need Pillow + cairosvg (IMGPY, e.g. .venv-img/bin/python).
set -euo pipefail
B="$(cd "$(dirname "$0")" && pwd)"; X="$(cd "$B/.." && pwd)"; REPO="$(cd "$X/../.." && pwd)"
PUBLISH=0; [ "${1:-}" = "--publish" ] && PUBLISH=1
PY="${PYTHON:-python3}"; IMGPY="${IMGPY:-$PY}"; SOFFICE="${SOFFICE:-soffice}"; OUT="$B/out"; mkdir -p "$OUT"
"$IMGPY" "$B/images/make_exam_images.py" "$X/images"
"$PY" "$B/images/make_exam_credits.py" "$X/images"
"$PY" "$B/make_exam_md.py" "$X"
for K in Midterm Final; do
  W=$([ $K = Midterm ] && echo 8 || echo 15)
  cp "$X/Level1_${K}_Student_Test.md" "$X/Level1_${K}_Exam_Teacher_Packet.md" "$OUT/"; ln -sfn "$X/images" "$OUT/images"   # the Markdown links to images/<file>.png
  "$PY" "$B/md2docx_L1_exam.py" "$OUT/Level1_${K}_Student_Test.md" "$OUT/Level1_${K}_Student_Test.docx" "Level 1 ESL · Week $W ${K/Final/Final Exam} · © 2026 the authors, CC BY-NC-SA 4.0 · Pictures: Twemoji, CC BY 4.0 (see CREDITS.md)"
  "$PY" "$B/md2docx_L1_exam.py" "$OUT/Level1_${K}_Exam_Teacher_Packet.md" "$OUT/Level1_${K}_Exam_Teacher_Packet.docx" "Level 1 ESL · Week $W · ${K/Final/Final Exam} · Teacher Packet"
  "$SOFFICE" --headless --convert-to pdf --outdir "$OUT" "$OUT/Level1_${K}_Student_Test.docx" >/dev/null 2>&1
  "$SOFFICE" --headless --convert-to pdf --outdir "$OUT" "$OUT/Level1_${K}_Exam_Teacher_Packet.docx" >/dev/null 2>&1
done
"$PY" "$B/check_consistency.py" "$X" || true
for f in "$OUT"/*.pdf; do echo "$(basename "$f"): $(pdfinfo "$f" | awk '/Pages/{print $2}') pages"; done
if [ "$PUBLISH" = 1 ]; then
  D="$REPO/public/level1/downloads/exams"; mkdir -p "$D"
  for K in Midterm Final; do cp "$OUT/Level1_${K}_Exam_Teacher_Packet.pdf" "$OUT/Level1_${K}_Exam_Teacher_Packet.docx" "$OUT/Level1_${K}_Student_Test.pdf" "$D/"; done
  echo "== copied into public/level1/downloads/exams/ (now run: python3 scripts/export_content.py)"
fi
