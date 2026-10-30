# Level 3 Exams: Audio Status

The two exam listening files are **not recorded yet**. The scripts are ready; until the files are recorded, the teacher reads the script aloud two times (two readers), as the teacher packets say. The website shows "Audio coming soon" for each exam.

| Exam | Script (generated from `build/exam_data.py`) | Speakers → voice clip | Estimated length | Target | Status |
|---|---|---|---|---|---|
| Week 8 Midterm | `build/audio/script_L3_Midterm.py` | Narrator → N, Elena → Rosa, David → Sam, Clerk → Server | about 1:39 | 1:15–1:50 | ☐ to do |
| Week 15 Final | `build/audio/script_L3_Final.py` | Narrator → N, Sara → Receptionist, Mr. Grant → Sam, Luis → Marco | about 1:33 | 1:15–1:50 | ☐ to do |

The voice clips are the Level 3 lesson clips (`level3/drafts/audio/tools/REFS_L3.md`; Kokoro-82M synthetic voices cloned with Chatterbox). Female characters use female clips.

## How to record (the same tools and checks as the Level 3 lessons)

Needs the audio venv (`.venv-audio`), ffmpeg, and the Level 3 reference clips in `level3/drafts/audio/tools/refs/` (see `REFS_L3.md`).

```bash
bash level3/exams/build/audio/run_exam_audio_L3.sh Midterm      # build, small.en check, medium.en second opinion, gate, exam length window
# listen to level3/exams/build/audio/out/Midterm/L3_Midterm_listening.mp3 from start to end, then:
bash level3/exams/build/audio/publish_exam_audio_L3.sh Midterm  # MP3 + check JSONs -> level3/exams/audio/, rebuild packets, copy to the website
python3 scripts/export_content.py
```

Do the same with `Final`. Then tick the row above. The gate is the lesson gate (both-checker misses, pitch, clipping, failed sentences, gaps, medium.en present) plus the exam length window in the script (`SETTINGS['LENGTH_S']`). WAV masters and `build/audio/out/` are not committed.
