#!/usr/bin/env bash
# Build + check + gate the listening file of one Level 4 lesson (Lessons 1-13).  Run from anywhere:
#   bash level4/audio/tools/run_audio_L4.sh N
#   EXCLUDE='{"<sentence>": [<seed>]}' bash level4/audio/tools/run_audio_L4.sh N    # retake: skip seeds the checks rejected
# Steps (each heavy step holds the lock, so only one Chatterbox/Whisper process runs at a time):
#   1 build_listening_L4.py   Chatterbox whole-sentence takes, small.en screening, pitch/clipping/artifact checks -> out/LN/L4_LN_listening.{wav,mp3} + _log.json
#   2 check_listening_L4.py   small.en whole file + each line, pitch per speaker, clipping, pauses, loudness -> L4_LN_check_results.json
#   3 second_opinion_lines.py medium.en on each line -> L4_LN_second_opinion_medium.txt
#   4 audio_gate_L4.py        pass/fail -> L4_LN_gate.json (prints PASS true/false)
# Env: PY (python of the audio venv; default <repo>/.venv-audio/bin/python), LOCK (default /tmp/chatterbox.lock),
#      TTS_DEVICE (auto|cuda|mps|cpu), WHISPER_DEVICE (cpu|cuda), NT (torch CPU threads), EXAG, CFG, PAUSE_SPK, MAXT, NCAND, EXCLUDE.
# Takes are cached in tools/cache/ and the outputs go to tools/out/LN/ (neither is committed).
set -euo pipefail
N="${1:?usage: run_audio_L4.sh N   (N = 1..13)}"
T="$(cd "$(dirname "$0")" && pwd)"; REPO="$(cd "$T/../../.." && pwd)"
PY="${PY:-$REPO/.venv-audio/bin/python}"; LOCK="${LOCK:-/tmp/chatterbox.lock}"
S="$T/scripts/script_L4_L$N.py"; O="$T/out/L$N"; ST="$O/L4_L${N}_listening"
[ -f "$S" ] || { echo "no script $S (run make_script_L4.py $N)"; exit 1; }
command -v ffmpeg >/dev/null || { echo "ffmpeg is not on PATH"; exit 1; }
for c in $("$PY" -c "import importlib.util as u,sys;s=u.spec_from_file_location('S',sys.argv[1]);m=u.module_from_spec(s);s.loader.exec_module(m);print(' '.join(sorted(set(m.VOICES.values()))))" "$S"); do
  [ -f "${L4_REFS:-$T/refs}/$c.wav" ] || { echo "missing reference clip refs/$c.wav: run  $PY $T/make_refs_L4.py  first"; exit 1; }
done
mkdir -p "$O"; cd "$T"
L() { "$PY" "$T/lockrun.py" "$LOCK" "$PY" "$@"; }
echo "== [$(date '+%H:%M')] 1/4 build L$N (log: $O/build.log)"
L build_listening_L4.py "$S" "$ST" > "$O/build.log" 2> "$O/build.err" || { tail -20 "$O/build.err"; exit 1; }
tail -1 "$O/build.log"
echo "== [$(date '+%H:%M')] 2/4 small.en check"
L check_listening_L4.py "$S" "$ST.mp3" "${ST}_log.json" "$O/L4_L${N}_check_results.json" > "$O/check.log" 2>> "$O/build.err"
echo "== [$(date '+%H:%M')] 3/4 medium.en second opinion"
L second_opinion_lines.py "$S" "$ST.mp3" "${ST}_log.json" > "$O/L4_L${N}_second_opinion_medium.txt" 2>> "$O/build.err"
head -1 "$O/L4_L${N}_second_opinion_medium.txt"
echo "== [$(date '+%H:%M')] 4/4 gate"
"$PY" audio_gate_L4.py "$S" "${ST}_log.json" "$O/L4_L${N}_check_results.json" "$O/L4_L${N}_second_opinion_medium.txt" "$O/L4_L${N}_gate.json" > "$O/gate.log"
"$PY" -c "import json,sys;g=json.load(open(sys.argv[1]));print('duration',g['duration'],'| PASS',g['PASS'],'| both-checker misses',len(g['lines_wrong_in_both_checkers']),'| pitch problems',len(g['pitch_problems']),'| clipped',g['clipped_samples'],'| failed sentences',len(g['failed_sentences']),'| gaps',g['gap_between_speakers_s'])" "$O/L4_L${N}_gate.json"
