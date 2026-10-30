# level3/drafts: the Level 3 working folder (kept on purpose)

Level 3 Lessons 2–13 were written and recorded here before they were published. **The website does not read this folder**
(`scripts/export_content.py` reads only `level3/curriculum`, `level3/images`, `level3/audio` and `level3/slides`), so nothing
here is served. The published copies are in those four folders.

Why it stays in the repository:

- **`audio/tools/` is the only copy of the Level 3 listening tools** (`run_audio_L3.sh`, `publish_audio_L3.sh`, `audio_gate_L3.py`,
  `make_script_L3.py`, the cast files and the generated `scripts/script_L3_L<N>.py`). The published `level3/audio/L3_L<N>_README.md`
  files and AGENTS.md section 7 point here. Level 4 and Level 5 copied these tools into `level4/audio/tools` and `level5/audio/tools`.
- `audio/` keeps the gate and check results (`*_gate.json`, `*_check_results.json`, logs) from each recording run. The MP3s are the
  same files as the published ones in `level3/audio/`.
- `curriculum/` and `images/` are the working copies the lessons were built from. **The published lesson text is
  `level3/curriculum/Level3_Lesson<N>.md`**; edit that one, not the copy here.

If the Level 3 tools ever move to `level3/audio/tools`, update AGENTS.md section 7 and the `level3/audio/L3_L<N>_README.md` files, then
this folder can be deleted.
