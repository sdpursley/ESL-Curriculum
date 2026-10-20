# Level 1 Lesson 1 audio

| File | What it is |
|---|---|
| `L1_listening.mp3` | **The published classroom file** (96 kbps mono, about -16 LUFS, peak 0.92, 77 s). Intro → conversation once → "That's the end of the listening." |
| `L1_check_results.json` | Whole-file check of the MP3: Whisper (faster-whisper `small.en`) word comparison with the script, plus pause, noise, click and clipping checks. |
| `L1_regen_log.json` | Which pieces were re-recorded during the build, plus the start/end time of every line. |
| `tools/script_L1.py` | **The listening script** used for the audio (keep it the same as the script in `level1/curriculum/Level1_Lesson1.md`). |
| `tools/build_L1_audio.py` | Builds the WAV + MP3 with Chatterbox (uses the Level 2 pipeline in `tools/audio/`). |
| `tools/check_L1.py` | Checks a finished MP3 against the script (writes `L1_check_results.json`). |
| `tools/fix_chunks.py` | Re-records only the pieces that failed, with new seeds (results go into the build cache). |

The WAV master (`L1_listening.wav`) is **not** committed (large file). Keep it on your own computer.

Voices: Chatterbox TTS (Resemble AI, MIT License), settings `EXAG=0.55 CFG=0.45 SEED0=2026`, cloned from the reference
clips in `tools/audio/samples/refs/` (N = Narrator, Receptionist, Ana, Carlos). Every file carries an inaudible Perth watermark.
Names in the script are invented (Ana Ruiz, Carlos Vega).

How to rebuild, check, or **swap in a different recording**: see "Level 1" in `MAINTAINING.md`.
