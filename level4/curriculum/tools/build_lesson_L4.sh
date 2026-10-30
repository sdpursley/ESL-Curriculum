#!/bin/bash
# Build one Level 4 lesson locally: spec -> md -> pictures -> script -> docx -> pdf -> checks.  Usage: build_lesson_L4.sh N
# Paths below are the original authoring workspace; copy the result into level4/ with sync_repo_L4.sh.
# fonts.conf renders Calibri as Liberation Serif, as in the published PDFs (keeps the page count).
set -e
N=$1; T=/workspace/level4_curriculum/tools; D=/workspace/level4_curriculum/lesson$N; PY=/workspace/tts/venv_l3img/bin/python
cd $D
$PY $T/render_L4.py $D
[ -f build/make_images_L4_L$N.py ] && $PY build/make_images_L4_L$N.py
$PY $T/make_credits_L4.py $D/images $N
$PY $T/make_script_L4.py $N $D/Level4_Lesson$N.md $D/build/cast_L4_L$N.json $D/build
$PY $T/md2docx_L4.py Level4_Lesson$N.md Level4_Lesson$N.docx "Level 4 ESL · Lesson $N"
FONTCONFIG_FILE="$(dirname "$(readlink -f "$0")")/fonts.conf" soffice --headless --convert-to pdf --outdir $D Level4_Lesson$N.docx >/dev/null 2>&1
$PY $T/check_lesson_L4.py $D $N
