# Level 5 Lesson 9 audio: sources and checks

| File | What it is |
|---|---|
| `L5_L9_listening.mp3` | Classroom file (96 kbps mono, 1:50). Narrator intro → conversation **once** → "That's the end of the listening." The teacher presses play again for the second listen. |
| `L5_L9_listening_log.json` | Settings, chosen take (seed, Whisper result, pitch) for every sentence, and each line's start/end time. |
| `L5_L9_check_results.json` | Whole-file and per-line check of the MP3 (Whisper `small.en`, pauses, noise, clicks, clipping, pitch by speaker, loudness). |
| `L5_L9_second_opinion_medium.txt` | Second opinion: Whisper `medium.en` on every line cut from the MP3. |
| `L5_L9_gate.json` | Pass/fail summary of all checks. |

**Speakers (3):** Narrator (female), Aisha (female), Noah (male). Names and story are invented; the script is in `../curriculum/Level5_Lesson9.md`.

## Voices and references

Chatterbox TTS (Resemble AI, MIT License), cloned **only from synthetic reference clips made with Kokoro-82M** (hexgrad, Apache License 2.0); see `tools/REFS_L5.md`:

| Character | Reference clip | Kokoro voice | Voice | Chatterbox settings | Median pitch in the MP3 |
|---|---|---|---|---|---|
| Narrator | `tools/refs/N.wav` | af_sarah | female | exaggeration 0.55, cfg 0.40 | 188.1 Hz (lines –) |
| Aisha | `tools/refs/Kim.wav` | af_nova | female | exaggeration 0.72, cfg 0.32 | 187.1 Hz (lines 174–229 Hz) |
| Noah | `tools/refs/Marco.wav` | am_adam | male | exaggeration 0.72, cfg 0.32 | 124.1 Hz (lines 103–134 Hz) |

No recordings of real people were used (no LibriVox / LibriTTS / LibriTTS-R, no Piper), and neither Chatterbox's built-in default voice nor the "Agent" clip was used. Every file carries an inaudible Perth watermark.

## How it was made and checked

- `tools/build_listening_L5.py` (Level 5 copy of `level1/audio/tools/lessons/build_listening.py`): each sentence is **one whole take** (no splicing, no time-stretching), several seeds per sentence. A take is kept only if Whisper `small.en` hears exactly the script words with good confidence, nothing is cut at the edges, the artifact detector finds nothing, nothing clips, and the pitch fits the character (female ≥ 165 Hz, male ≤ 150 Hz median F0). 84 takes were made for 38 sentences. About 1.4 s between speakers, 0.55 s between two sentences of one speaker.
- `tools/check_listening_L5.py` on the finished MP3: whole-file Whisper `small.en` WER **0.0%** (0/247 words); **18/18 lines** heard exactly on their own with no artifact flags; clipped samples **0** (peak 0.882); click ratio 4.2; loudness -16.7 LUFS; gaps between speakers 1.4–1.4 s; pauses with noise: 0.
- **Second opinion** `tools/second_opinion_lines.py` (Whisper `medium.en`, each line alone): WER 0.4% (1/247), 19/20 lines exact.
- **Pitch check:** every female line ≥ 165 Hz and every male line ≤ 150 Hz: yes.
- **Result:** PASS.
Draft. A person still has to listen to the whole file.

## Rebuild

From the repository root: `bash level5/audio/tools/run_audio_L5.sh 9` (builds the file, then runs the checks and the gate; see "Running audio locally" in AGENTS.md). Takes are cached in `tools/cache/` (not committed), so re-runs are fast. When the gate passes, `bash level5/audio/tools/publish_audio_L5.sh 9` copies `tools/out/L9/L5_L9_*` (mp3, log, check, second opinion, gate) into this folder and writes this README. `tools/scripts/script_L5_L9.py` is generated from the lesson by `tools/make_script_L5.py`, so the audio always matches the script in the lesson.

Script © 2026 the authors, CC BY-NC-SA 4.0.
