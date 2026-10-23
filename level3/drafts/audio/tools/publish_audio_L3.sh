#!/usr/bin/env bash
# After run_audio_L3.sh N passes (and you listened to the whole file): copy the checked files from tools/out/LN/ into
# level3/drafts/audio/ and write L3_LN_README.md. Copies inside the repo only; nothing reaches the website (level3/drafts/ is not exported).
# Usage: bash level3/drafts/audio/tools/publish_audio_L3.sh N ['notes (markdown): retakes, by-ear checks, accepted single-checker misses']
set -euo pipefail
N="${1:?usage: publish_audio_L3.sh N ['notes']}"
T="$(cd "$(dirname "$0")" && pwd)"; A="$(cd "$T/.." && pwd)"; O="$T/out/L$N"; REPO="$(cd "$T/../../../.." && pwd)"
PY="${PY:-$REPO/.venv-audio/bin/python}"
"$PY" -c "import json,sys;g=json.load(open(sys.argv[1]));sys.exit(0 if g['PASS'] else 'gate did not pass: see '+sys.argv[1])" "$O/L3_L${N}_gate.json"
cp "$O/L3_L${N}_listening.mp3" "$O/L3_L${N}_listening_log.json" "$O/L3_L${N}_check_results.json" "$O/L3_L${N}_second_opinion_medium.txt" "$O/L3_L${N}_gate.json" "$A/"
"$PY" "$T/make_audio_readme_L3.py" "$N" "${2:-}"
echo "copied into $A (MP3 + JSON + README; no WAV). Now put the real length in the listening-script heading of level3/drafts/curriculum/Level3_Lesson$N.md and tick level3/AUDIO_STATUS.md."
