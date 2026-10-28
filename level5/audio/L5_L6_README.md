# Level 5 Lesson 6 audio: sources and checks

| File | What it is |
|---|---|
| `L5_L6_listening.mp3` | Classroom file (96 kbps mono, 1:41). Narrator intro → conversation **once** → "That's the end of the listening." The teacher presses play again for the second listen. |
| `L5_L6_listening_log.json` | Settings, chosen take (seed, Whisper result, pitch) for every sentence, and each line's start/end time. |
| `L5_L6_check_results.json` | Whole-file and per-line check of the MP3 (Whisper `small.en`, pauses, noise, clicks, clipping, pitch by speaker, loudness). |
| `L5_L6_second_opinion_medium.txt` | Second opinion: Whisper `medium.en` on every line cut from the MP3. |
| `L5_L6_gate.json` | Pass/fail summary of all checks. |

**Speakers (4):** Narrator (female), Jana (female), Nurse Patel (female), Ken (male). Names and story are invented; the script is in `../curriculum/Level5_Lesson6.md`.

## Voices and references

Chatterbox TTS (Resemble AI, MIT License), cloned **only from synthetic reference clips made with Kokoro-82M** (hexgrad, Apache License 2.0); see `tools/REFS_L5.md`:

| Character | Reference clip | Kokoro voice | Voice | Chatterbox settings | Median pitch in the MP3 |
|---|---|---|---|---|---|
| Narrator | `tools/refs/N.wav` | af_sarah | female | exaggeration 0.55, cfg 0.40 | 182.8 Hz (lines 177–183 Hz) |
| Jana | `tools/refs/Rosa.wav` | af_heart | female | exaggeration 0.72, cfg 0.32 | 209.4 Hz (lines 188–250 Hz) |
| Nurse Patel | `tools/refs/Kim.wav` | af_nova | female | exaggeration 0.72, cfg 0.32 | 186.0 Hz (lines 184–203 Hz) |
| Ken | `tools/refs/Sam.wav` | am_michael | male | exaggeration 0.72, cfg 0.32 | 127.2 Hz (lines 122–136 Hz) |

No recordings of real people were used (no LibriVox / LibriTTS / LibriTTS-R, no Piper), and neither Chatterbox's built-in default voice nor the "Agent" clip was used. Every file carries an inaudible Perth watermark.

## How it was made and checked

- `tools/build_listening_L5.py` (Level 5 copy of `level1/audio/tools/lessons/build_listening.py`): each sentence is **one whole take** (no splicing, no time-stretching), several seeds per sentence. A take is kept only if Whisper `small.en` hears exactly the script words with good confidence, nothing is cut at the edges, the artifact detector finds nothing, nothing clips, and the pitch fits the character (female ≥ 165 Hz, male ≤ 150 Hz median F0). 64 takes were made for 35 sentences. About 1.4 s between speakers, 0.55 s between two sentences of one speaker.
- `tools/check_listening_L5.py` on the finished MP3: whole-file Whisper `small.en` WER **0.9%** (2/218 words); **17/17 lines** heard exactly on their own with no artifact flags; clipped samples **0** (peak 0.884); click ratio 4.1; loudness -16.6 LUFS; gaps between speakers 1.4–1.4 s; pauses with noise: 0.
- **Second opinion** `tools/second_opinion_lines.py` (Whisper `medium.en`, each line alone): WER 0.9% (2/218), 18/19 lines exact.
- **Pitch check:** every female line ≥ 165 Hz and every male line ≤ 150 Hz: yes.
- **Result:** PASS.
Draft. A person still has to listen to the whole file.

## Rebuild

From the repository root: `bash level5/audio/tools/run_audio_L5.sh 6` (builds the file, then runs the checks and the gate; see "Running audio locally" in AGENTS.md). Takes are cached in `tools/cache/` (not committed), so re-runs are fast. When the gate passes, `bash level5/audio/tools/publish_audio_L5.sh 6` copies `tools/out/L6/L5_L6_*` (mp3, log, check, second opinion, gate) into this folder and writes this README. `tools/scripts/script_L5_L6.py` is generated from the lesson by `tools/make_script_L5.py`, so the audio always matches the script in the lesson.

Script © 2026 the authors, CC BY-NC-SA 4.0.
