#!/usr/bin/env bash
# Record + check + gate the listening file of one exam (Midterm or Final) with this level's lesson audio tools.  Run from anywhere:
#   bash level3/exams/build/audio/run_exam_audio_L3.sh Midterm      (or Final)
#   EXCLUDE='{"<sentence>": [<seed>]}' bash ...run_exam_audio_L3.sh Final   # retake: skip seeds the checks rejected
# Same 4 steps as the lessons (build_listening -> check_listening -> second_opinion_lines -> audio_gate), then exam_gate.py
# re-checks the length against the exam window in the script (SETTINGS['LENGTH_S']), because the lesson gate has the lesson window.
# Env: PY (default <repo>/.venv-audio/bin/python), LOCK (default /tmp/chatterbox.lock), plus the lesson tools' env (TTS_DEVICE, EXAG, CFG, ...).
# Reference clips: the level's tools/refs/<voice>.wav (make them with the level's make_refs script first). Output: build/audio/out/<K>/ (not committed).
set -euo pipefail
K="${1:?usage: run_exam_audio_L3.sh Midterm|Final}"
A="$(cd "$(dirname "$0")" && pwd)"; REPO="$(cd "$A/../../../.." && pwd)"; V="$(basename "$(cd "$A/../../.." && pwd)" | tr -dc 0-9)"
if [ "$V" = 3 ]; then T="$REPO/level3/drafts/audio/tools"; else T="$REPO/level$V/audio/tools"; fi
PY="${PY:-$REPO/.venv-audio/bin/python}"; LOCK="${LOCK:-/tmp/chatterbox.lock}"
S="$A/script_L${V}_$K.py"; O="$A/out/$K"; B="L${V}_$K"; ST="$O/${B}_listening"
[ -f "$S" ] || { echo "no script $S (run level$V/exams/build/build_all.sh)"; exit 1; }
command -v ffmpeg >/dev/null || { echo "ffmpeg is not on PATH"; exit 1; }
for c in $("$PY" -c "import importlib.util as u,sys;s=u.spec_from_file_location('S',sys.argv[1]);m=u.module_from_spec(s);s.loader.exec_module(m);print(' '.join(sorted(set(m.VOICES.values()))))" "$S"); do
  [ -f "$T/refs/$c.wav" ] || { echo "missing reference clip $T/refs/$c.wav: make the Level $V reference clips first (see the level's REFS_L$V.md)"; exit 1; }
done
mkdir -p "$O"; cd "$T"
L() { "$PY" "$T/lockrun.py" "$LOCK" "$PY" "$@"; }
echo "== [$(date '+%H:%M')] 1/5 build $B (log: $O/build.log)"
L build_listening_L$V.py "$S" "$ST" > "$O/build.log" 2> "$O/build.err" || { tail -20 "$O/build.err"; exit 1; }
tail -1 "$O/build.log"
echo "== [$(date '+%H:%M')] 2/5 small.en check"
L check_listening_L$V.py "$S" "$ST.mp3" "${ST}_log.json" "$O/${B}_check_results.json" > "$O/check.log" 2>> "$O/build.err"
echo "== [$(date '+%H:%M')] 3/5 medium.en second opinion"
L second_opinion_lines.py "$S" "$ST.mp3" "${ST}_log.json" > "$O/${B}_second_opinion_medium.txt" 2>> "$O/build.err"
head -1 "$O/${B}_second_opinion_medium.txt"
echo "== [$(date '+%H:%M')] 4/5 lesson gate"
"$PY" audio_gate_L$V.py "$S" "${ST}_log.json" "$O/${B}_check_results.json" "$O/${B}_second_opinion_medium.txt" "$O/${B}_gate.json" > "$O/gate.log"
echo "== [$(date '+%H:%M')] 5/5 exam length window"
"$PY" "$A/exam_gate.py" "$S" "$O/${B}_gate.json"
