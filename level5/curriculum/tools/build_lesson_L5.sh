#!/usr/bin/env bash
# Rebuild Level 5 lessons from their Markdown: md -> docx -> pdf -> checks.  Usage (any folder): build_lesson_L5.sh N [N ...]
# Level 5 has no lesson specs: edit level5/curriculum/Level5_LessonN.md by hand, then run this.
# The PDF is rendered with tools/fonts.conf (Calibri -> Liberation Serif, as in the published PDFs), so page breaks stay the same.
# After the build: regenerate the audio script if the listening changed (level5/audio/tools/make_script_L5.py),
# then python3 scripts/export_content.py to copy the docx/pdf to public/level5/downloads.
set -euo pipefail
T="$(cd "$(dirname "$0")" && pwd)"; C="$(dirname "$T")"; R="$(cd "$C/../.." && pwd)"; PY="${PY:-python3}"
W="$(mktemp -d)"; trap 'rm -rf "$W"' EXIT; ln -s "$R/level5/images" "$W/images"
st=0
for N in "$@"; do
  cp "$C/Level5_Lesson$N.md" "$W/"
  (cd "$W" && "$PY" "$T/md2docx_L5.py" "Level5_Lesson$N.md" "Level5_Lesson$N.docx" "Level 5 ESL · Lesson $N" >/dev/null)
  (cd "$W" && FONTCONFIG_FILE="$T/fonts.conf" soffice -env:UserInstallation="file://$W/lo" --headless --convert-to pdf "Level5_Lesson$N.docx" >/dev/null 2>&1)
  cp "$W/Level5_Lesson$N.docx" "$W/Level5_Lesson$N.pdf" "$C/"
  (cd "$R" && "$PY" "$T/check_lesson_L5.py" level5/curriculum "$N") || st=1
done
exit $st
