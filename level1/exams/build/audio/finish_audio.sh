#!/usr/bin/env bash
# After run_audio.sh: run every check on a finished exam listening file, copy it to level1/exams/audio/, write its README.
# Usage: bash finish_audio.sh Midterm|Final        (all Whisper runs hold the lock file $LOCK, like the build)
set -euo pipefail
N="$1"; A="$(cd "$(dirname "$0")" && pwd)"; X="$(cd "$A/../.." && pwd)"; REPO="$(cd "$X/../.." && pwd)"; T="$REPO/level1/audio/tools/lessons"
PY="${PY:-$REPO/.venv-audio/bin/python}"; LOCK="${LOCK:-/tmp/chatterbox.lock}"; L() { flock "$LOCK" "$PY" "$@"; }
cd "$A"; O="out/L1_${N}_listening"; S="$A/script_L1_$N.py"
test -f "$O.mp3"
L "$T/check_listening.py" "$S" "$O.mp3" "${O}_log.json" "out/L1_${N}_check_results.json" > "out/check_$N.log" 2>&1
L "$T/verify24.py" "$S" "$O.wav" "${O}_log.json" > "out/verify24_$N.log" 2>&1 || true
L "$T/second_opinion.py" "$S" "$O.mp3" > "out/second_$N.log" 2>&1
L "$T/second_opinion_lines.py" "$S" "$O.mp3" "${O}_log.json" > "out/second_lines_$N.log" 2>&1 || true
L "$T/takes_medium.py" "$S" "${O}_log.json" > "out/takes_medium_$N.log" 2>&1 || true
L -u "$T/vote_takes.py" "$S" "${O}_log.json" 3 > "out/vote_$N.log" 2>&1 || true
mkdir -p "$X/audio"
cp -f "$O.mp3" "$X/audio/L1_${N}_listening.mp3"
cp -f "out/L1_${N}_check_results.json" "$X/audio/"
cp -f "${O}_log.json" "$X/audio/L1_${N}_regen_log.json"
python3 "$A/make_exam_audio_readme.py" "$N" "$X" "$S" "$A/out"
echo "FINISH $N: $(python3 -c "import json;d=json.load(open('out/L1_${N}_check_results.json'));print(d['duration_s'],'s WER',d['wer'],'lines',d['lines_ok'],'clipped',d['clipped_samples'],'pitch',d['pitch_median_hz'])") | $(grep -v Warn out/second_$N.log | grep WER | head -1) | $(grep "per-line" out/second_lines_$N.log | head -1) | $(grep "per-take" out/takes_medium_$N.log) | $(grep "^vote:" out/vote_$N.log)"
