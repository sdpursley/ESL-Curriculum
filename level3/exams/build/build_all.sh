#!/usr/bin/env bash
# Rebuild everything for this level's exams except the audio (audio: build/audio/run_exam_audio_L<V>.sh, see ../AUDIO_STATUS.md).
# Usage: level<V>/exams/build/build_all.sh [--publish]
#   writes the four Markdown files (level<V>/exams/) and the listening scripts + casts (build/audio/), then DOCX + PDF into build/out/ (not committed);
#   --publish also copies the teacher packets (PDF + DOCX) and student tests (PDF) into public/level<V>/downloads/exams/ for the website.
# Needs: python3 + python-docx, LibreOffice (soffice), poppler-utils (pdfinfo).
set -euo pipefail
B="$(cd "$(dirname "$0")" && pwd)"; X="$(cd "$B/.." && pwd)"; REPO="$(cd "$X/../.." && pwd)"
V="$(basename "$(dirname "$X")" | tr -dc 0-9)"
PUBLISH=0; [ "${1:-}" = "--publish" ] && PUBLISH=1
PY="${PYTHON:-python3}"; SOFFICE="${SOFFICE:-soffice}"; OUT="$B/out"; mkdir -p "$OUT"
L="© 2026 the authors, CC BY-NC-SA 4.0"
"$PY" "$B/make_exam_md.py" "$X"
for K in Midterm Final; do
  W=$([ $K = Midterm ] && echo 8 || echo 15)
  cp "$X/Level${V}_${K}_Student_Test.md" "$X/Level${V}_${K}_Exam_Teacher_Packet.md" "$OUT/"
  "$PY" "$B/md2docx_exam.py" "$OUT/Level${V}_${K}_Student_Test.md" "$OUT/Level${V}_${K}_Student_Test.docx" "Level $V ESL · Week $W ${K/Final/Final Exam} · $L"
  "$PY" "$B/md2docx_exam.py" "$OUT/Level${V}_${K}_Exam_Teacher_Packet.md" "$OUT/Level${V}_${K}_Exam_Teacher_Packet.docx" "Level $V ESL · Week $W · ${K/Final/Final Exam} · Teacher Packet · $L"
  "$SOFFICE" --headless --convert-to pdf --outdir "$OUT" "$OUT/Level${V}_${K}_Student_Test.docx" >/dev/null 2>&1
  "$SOFFICE" --headless --convert-to pdf --outdir "$OUT" "$OUT/Level${V}_${K}_Exam_Teacher_Packet.docx" >/dev/null 2>&1
done
"$PY" "$B/check_consistency.py" "$X" || true
for f in "$OUT"/*.pdf; do echo "$(basename "$f"): $(pdfinfo "$f" | awk '/Pages/{print $2}') pages"; done
if [ "$PUBLISH" = 1 ]; then
  D="$REPO/public/level${V}/downloads/exams"; mkdir -p "$D"
  for K in Midterm Final; do cp "$OUT/Level${V}_${K}_Exam_Teacher_Packet.pdf" "$OUT/Level${V}_${K}_Exam_Teacher_Packet.docx" "$OUT/Level${V}_${K}_Student_Test.pdf" "$D/"; done
  echo "== copied into public/level${V}/downloads/exams/ (now run: python3 scripts/export_content.py)"
fi
