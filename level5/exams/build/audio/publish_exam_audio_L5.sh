#!/usr/bin/env bash
# After run_exam_audio_L5.sh K passes (and you listened to the whole file): copy the checked files into level5/exams/audio/
# (MP3 with the exam title in its metadata + the check JSONs; no WAV), rebuild the packets so the script heading shows the real length,
# and copy them to the website. Then run python3 scripts/export_content.py so the Exams page shows the player, and tick ../../AUDIO_STATUS.md.
# Usage: bash level5/exams/build/audio/publish_exam_audio_L5.sh Midterm|Final
set -euo pipefail
K="${1:?usage: publish_exam_audio_L5.sh Midterm|Final}"
A="$(cd "$(dirname "$0")" && pwd)"; X="$(cd "$A/../.." && pwd)"; REPO="$(cd "$X/../.." && pwd)"; V="$(basename "$(dirname "$X")" | tr -dc 0-9)"
PY="${PY:-$REPO/.venv-audio/bin/python}"; O="$A/out/$K"; B="L${V}_$K"; D="$X/audio"; mkdir -p "$D"
"$PY" -c "import json,sys;g=json.load(open(sys.argv[1]));sys.exit(0 if g['PASS'] else 'gate did not pass: see '+sys.argv[1])" "$O/${B}_gate.json"
TITLE="$("$PY" -c "import importlib.util as u,sys;s=u.spec_from_file_location('S',sys.argv[1]);m=u.module_from_spec(s);s.loader.exec_module(m);print(m.TITLE)" "$A/script_$B.py")"
ffmpeg -loglevel error -y -i "$O/${B}_listening.mp3" -c copy -map_metadata 0 -metadata title="Level $V $K Exam Listening: $TITLE" "$D/${B}_listening.mp3"
cp "$O/${B}_listening_log.json" "$O/${B}_check_results.json" "$O/${B}_second_opinion_medium.txt" "$O/${B}_gate.json" "$D/"
bash "$X/build/build_all.sh" --publish
echo "copied into $D (MP3 + JSON; no WAV) and rebuilt the packets. Now: python3 scripts/export_content.py, and tick level$V/exams/AUDIO_STATUS.md."
