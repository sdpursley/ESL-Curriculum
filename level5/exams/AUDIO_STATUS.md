# Level 5 Exams: Audio Status

The two exam listening files are **not recorded yet**. The scripts are ready; until the files are recorded, the teacher reads the script aloud two times (two or three readers), as the teacher packets say. The website shows "Audio coming soon" for each exam.

| Exam | Script (generated from `build/exam_data.py`) | Speakers → voice clip | Estimated length | Target | Status |
|---|---|---|---|---|---|
| Week 8 Midterm | `build/audio/script_L5_Midterm.py` | Narrator → N, Ms. Hale → Kim, Samir → Marco, Jana → Rosa | about 2:12 | 2:00–3:00 | ☐ to do |
| Week 15 Final | `build/audio/script_L5_Final.py` | Narrator → N, Aisha → Kim, Noah → Marco, Ms. Lane → Rosa, Tom → Sam (Tom speaks only in Part 3) | about 2:38 | 2:00–3:00 | ☐ to do |

The voice clips are the Level 5 lesson clips (`level5/audio/tools/REFS_L5.md`; Kokoro-82M synthetic voices cloned with Chatterbox). Female characters use female clips.

## How to record (the same tools and checks as the Level 5 lessons)

Needs the audio venv (`.venv-audio`), ffmpeg, and the Level 5 reference clips in `level5/audio/tools/refs/` (see `REFS_L5.md`).

```bash
bash level5/exams/build/audio/run_exam_audio_L5.sh Midterm      # build, small.en check, medium.en second opinion, gate, exam length window
# listen to level5/exams/build/audio/out/Midterm/L5_Midterm_listening.mp3 from start to end, then:
bash level5/exams/build/audio/publish_exam_audio_L5.sh Midterm  # MP3 + check JSONs -> level5/exams/audio/, rebuild packets, copy to the website
python3 scripts/export_content.py
```

Do the same with `Final`. Then tick the row above. The gate is the lesson gate (both-checker misses, pitch, clipping, failed sentences, gaps, medium.en present) plus the exam length window in the script (`SETTINGS['LENGTH_S']`). WAV masters and `build/audio/out/` are not committed.
