# Level 1 Lesson 1 audio

| File | What it is |
|---|---|
| `L1_listening.mp3` | **The published classroom file** (96 kbps mono, about -16 LUFS, peak 0.91, 76 s). Intro → conversation once → "That's the end of the listening." |
| `L1_check_results.json` | Whole-file check of the MP3: Whisper (faster-whisper `small.en`) word comparison with the script, plus pause, noise, click and clipping checks. |
| `L1_regen_log.json` | Settings, the chosen take (seed, Whisper result, letter gaps) for every Ana and Carlos line, plus the start/end time of every line. |
| `tools/script_L1.py` | **The listening script** used for the audio (keep it the same as the script in `level1/curriculum/Level1_Lesson1.md`). |
| `tools/build_L1_audio.py` | Builds the WAV + MP3 with Chatterbox (uses the Level 2 pipeline in `tools/audio/`). |
| `tools/check_L1.py` | Checks a finished MP3 against the script (writes `L1_check_results.json`). |
| `tools/fix_chunks.py` | Re-records only the pieces that failed, with new seeds (results go into the build cache). |
| `tools/natural/build_natural.py` | **Builds the published file**: Ana and Carlos as whole-sentence takes (several seeds each, the best take that passes the checks is kept); narrator and receptionist reuse the takes from `build_L1_audio.py`. The exact command is at the top of the file. |
| `tools/natural/engine.py`, `metrics.py` | Chatterbox wrapper and the pitch-movement measure used to pick takes. |
| `tools/natural/kokoro_refs/af_jessica.wav` | **Ana's voice reference clip**: synthetic, made with Kokoro-82M (voice `af_jessica`, Apache 2.0) reading an original text. No human recording. |
| `tools/natural/make_ana_ref.py`, `ana_ref.json` | The script that makes Ana's reference clip with Kokoro, and its details (Kokoro voice, text, license, checksum). |

The WAV master (`L1_listening.wav`) is **not** committed (large file). Keep it on your own computer.

Voices: Chatterbox TTS (Resemble AI, MIT License). Narrator and receptionist: settings `EXAG=0.55 CFG=0.45 SEED0=2026`, cloned from the
reference clips `N` and `Receptionist` in `tools/audio/samples/refs/`. Ana and Carlos: settings `EXAG=0.72 CFG=0.32`, normal pace, longer
pauses between speakers; Carlos is cloned from the `Sam` clip in `tools/audio/samples/refs/` and Ana from `tools/natural/kokoro_refs/af_jessica.wav`.
Every reference clip (`N`, `Receptionist`, `Sam`, `af_jessica`) was made with Kokoro-82M (Apache 2.0), so all the voices are synthetic,
not real people. Every file carries an inaudible Perth watermark.

Names in the script are invented (Ana Ruiz, Carlos Vega).

How to rebuild, check, or **swap in a different recording**: see "Level 1" in `MAINTAINING.md`.
