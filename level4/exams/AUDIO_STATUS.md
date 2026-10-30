# Level 4 Exams: Audio Status

The two exam listening files are **not recorded yet**. The scripts are ready; until the files are recorded, the teacher reads the script aloud two times (two readers), as the teacher packets say. The website shows "Audio coming soon" for each exam.

| Exam | Script (generated from `build/exam_data.py`) | Speakers → voice clip | Estimated length | Target | Status |
|---|---|---|---|---|---|
| Week 8 Midterm | `build/audio/script_L4_Midterm.py` | Narrator → N, Amina → Rosa, Ms. Park → Receptionist, Omar → Sam | about 1:57 | 1:30–2:15 | ☐ to do |
| Week 15 Final | `build/audio/script_L4_Final.py` | Narrator → N, Diane Lee → Receptionist, Mrs. Lopez → Kim, Caller → Carlos | about 1:52 | 1:30–2:15 | ☐ to do |

The voice clips are the Level 4 lesson clips (`level4/audio/tools/REFS_L4.md`; Kokoro-82M synthetic voices cloned with Chatterbox). Female characters use female clips.

## How to record (the same tools and checks as the Level 4 lessons)

Needs the audio venv (`.venv-audio`), ffmpeg, and the Level 4 reference clips in `level4/audio/tools/refs/` (see `REFS_L4.md`).

```bash
bash level4/exams/build/audio/run_exam_audio_L4.sh Midterm      # build, small.en check, medium.en second opinion, gate, exam length window
# listen to level4/exams/build/audio/out/Midterm/L4_Midterm_listening.mp3 from start to end, then:
bash level4/exams/build/audio/publish_exam_audio_L4.sh Midterm  # MP3 + check JSONs -> level4/exams/audio/, rebuild packets, copy to the website
python3 scripts/export_content.py
```

Do the same with `Final`. Then tick the row above. The gate is the lesson gate (both-checker misses, pitch, clipping, failed sentences, gaps, medium.en present) plus the exam length window in the script (`SETTINGS['LENGTH_S']`). WAV masters and `build/audio/out/` are not committed.
