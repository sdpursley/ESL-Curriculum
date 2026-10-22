#!/usr/bin/env bash
# Build the Level 1 exam listening files with Chatterbox (CPU). Usage: bash run_audio.sh [Midterm|Final ...]   (default: Midterm Final)
# Uses the shared Level 1 builder level1/audio/tools/lessons/build_listening.py (takes are cached in that folder's cache/, not committed).
# Every Chatterbox or Whisper run holds the lock file $LOCK, so only one such process runs at a time (two at once ran out of memory on a 15 GB machine).
# Then run finish_audio.sh for each file. Output: build/audio/out/ (not committed).
set -uo pipefail
A="$(cd "$(dirname "$0")" && pwd)"; REPO="$(cd "$A/../../../.." && pwd)"; T="$REPO/level1/audio/tools/lessons"
PY="${PY:-$REPO/.venv-audio/bin/python}"; LOCK="${LOCK:-/tmp/chatterbox.lock}"
cd "$A"; mkdir -p out
for X in "${@:-Midterm Final}"; do
  for N in $X; do
    echo "=== build $N $(date)"
    NT=${NT:-3} flock "$LOCK" "$PY" "$T/build_listening.py" "$A/script_L1_$N.py" "$A/out/L1_${N}_listening" > "out/build_$N.log" 2>&1
    tail -1 "out/build_$N.log"
  done
done
