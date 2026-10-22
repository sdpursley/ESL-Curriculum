#!/bin/bash
# Copy built Level 4 lessons into the repo (no audio, no venvs, no _twemoji_src).
set -e
S=/workspace/level4_curriculum; R=/workspace/l3site/level4
mkdir -p $R/curriculum/specs $R/curriculum/tools $R/images/tools $R/audio/tools/cast $R/audio/tools/scripts
for d in $S/lesson*/; do
  N=$(basename $d | sed 's/lesson//'); [ -f $d/Level4_Lesson$N.pdf ] || continue
  cp $d/Level4_Lesson$N.md $d/Level4_Lesson$N.docx $d/Level4_Lesson$N.pdf $R/curriculum/
  cp $d/spec_L4_L$N.py $R/curriculum/specs/
  cp $d/images/L4_L${N}_*.png $d/images/images_L4_L$N.json $R/images/
  cp $d/build/make_images_L4_L$N.py $R/images/tools/
  cp $d/build/cast_L4_L$N.json $R/audio/tools/cast/; cp $d/build/script_L4_L$N.py $R/audio/tools/scripts/
done
cp $S/tools/{render_L4.py,std.py,check_lesson_L4.py,md2docx_L4.py,build_lesson_L4.sh,montage_L4.sh,sync_repo_L4.sh,audio_status_L4.py,progress_L4.py} $R/curriculum/tools/
cp $S/tools/{l4img.py,make_credits_L4.py} $R/images/tools/
cp $S/tools/make_script_L4.py $R/audio/tools/ && cp $S/audio_tools/* $R/audio/tools/ && chmod +x $R/audio/tools/*.sh
cp $S/PROGRESS.md $R/curriculum/PROGRESS.md
/workspace/tts/venv_l3img/bin/python $S/tools/make_credits_L4.py $R/images >/dev/null
/workspace/tts/venv_l3img/bin/python $S/tools/audio_status_L4.py /workspace/l3site/level4
