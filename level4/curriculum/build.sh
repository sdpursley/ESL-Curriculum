#!/usr/bin/env bash
# Rebuild the Level 4 scope doc (.docx + .pdf) with the Level 3 builder.
set -euo pipefail
cd "$(dirname "$0")"
python3 ../../level3/curriculum/md2docx_L3.py Level4_Scope_and_Sequence.md Level4_Scope_and_Sequence.docx "Level 4 ESL · Scope and Sequence · Draft for review"
soffice --headless --convert-to pdf --outdir . Level4_Scope_and_Sequence.docx
