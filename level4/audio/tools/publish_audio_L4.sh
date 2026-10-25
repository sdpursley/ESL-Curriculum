#!/usr/bin/env bash
# After run_audio_L4.sh N passes (and you listened to the whole file): copy the checked files from tools/out/LN/ into
# level4/audio/ and write L4_LN_README.md. Copies inside the repo only; nothing reaches the website (level4/ is not exported).
# Usage: bash level4/audio/tools/publish_audio_L4.sh N ['notes (markdown): retakes, by-ear checks, accepted single-checker misses']
set -euo pipefail
N="${1:?usage: publish_audio_L4.sh N ['notes']}"
T="$(cd "$(dirname "$0")" && pwd)"; A="$(cd "$T/.." && pwd)"; O="$T/out/L$N"; REPO="$(cd "$T/../../.." && pwd)"
PY="${PY:-$REPO/.venv-audio/bin/python}"
"$PY" -c "import json,sys;g=json.load(open(sys.argv[1]));sys.exit(0 if g['PASS'] else 'gate did not pass: see '+sys.argv[1])" "$O/L4_L${N}_gate.json"
cp "$O/L4_L${N}_listening.mp3" "$O/L4_L${N}_listening_log.json" "$O/L4_L${N}_check_results.json" "$O/L4_L${N}_second_opinion_medium.txt" "$O/L4_L${N}_gate.json" "$A/"
"$PY" "$T/make_audio_readme_L4.py" "$N" "${2:-}"
echo "copied into $A (MP3 + JSON + README; no WAV). Now put the real length in the listening-script heading of level4/curriculum/Level4_Lesson$N.md and tick level4/AUDIO_STATUS.md."
