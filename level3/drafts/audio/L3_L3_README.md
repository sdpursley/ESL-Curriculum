# Level 3 Lesson 3 audio: sources and checks

| File | What it is |
|---|---|
| `L3_L3_listening.mp3` | Classroom file (96 kbps mono, 1:15). Narrator intro → conversation **once** → "That's the end of the listening." The teacher presses play again for the second listen. |
| `L3_L3_listening_log.json` | Settings, chosen take (seed, Whisper result, pitch) for every sentence, and each line's start/end time. |
| `L3_L3_check_results.json` | Whole-file and per-line check of the MP3 (Whisper `small.en`, pauses, noise, clicks, clipping, pitch by speaker, loudness). |
| `L3_L3_second_opinion_medium.txt` | Second opinion: Whisper `medium.en` on every line cut from the MP3. |
| `L3_L3_gate.json` | Pass/fail summary of all checks. |

**Speakers (3):** Narrator (female), Daniel (male), Teresa (female). Names and story are invented; the script is in `../curriculum/Level3_Lesson3.md`.

## Voices and references

Chatterbox TTS (Resemble AI, MIT License), cloned **only from synthetic reference clips made with Kokoro-82M** (hexgrad, Apache License 2.0); see `tools/REFS_L3.md`:

| Character | Reference clip | Kokoro voice | Voice | Chatterbox settings | Median pitch in the MP3 |
|---|---|---|---|---|---|
| Narrator | `tools/refs/N.wav` | af_sarah | female | exaggeration 0.55, cfg 0.40 | 174.5 Hz (lines –) |
| Daniel | `tools/refs/Server.wav` | am_puck | male | exaggeration 0.72, cfg 0.32 | 137.4 Hz (lines 118–148 Hz) |
| Teresa | `tools/refs/Ana_af_bella.wav` | af_bella | female | exaggeration 0.72, cfg 0.32 | 213.6 Hz (lines 197–228 Hz) |

No recordings of real people were used (no LibriVox / LibriTTS / LibriTTS-R, no Piper), and neither Chatterbox's built-in default voice nor the "Agent" clip was used. Every file carries an inaudible Perth watermark.

## How it was made and checked

- `tools/build_listening_L3.py` (Level 3 copy of `level1/audio/tools/lessons/build_listening.py`): each sentence is **one whole take** (no splicing, no time-stretching), several seeds per sentence. A take is kept only if Whisper `small.en` hears exactly the script words with good confidence, nothing is cut at the edges, the artifact detector finds nothing, nothing clips, and the pitch fits the character (female ≥ 165 Hz, male ≤ 150 Hz median F0). 62 takes were made for 23 sentences. About 1.4 s between speakers, 0.55 s between two sentences of one speaker.
- `tools/check_listening_L3.py` on the finished MP3: whole-file Whisper `small.en` WER **0.0%** (0/176 words); **15/15 lines** heard exactly on their own with no artifact flags; clipped samples **0** (peak 0.884); click ratio 4.5; loudness -16.6 LUFS; gaps between speakers 1.3–1.3 s; pauses with noise: 0.
- **Second opinion** `tools/second_opinion_lines.py` (Whisper `medium.en`, each line alone): WER 0.0% (0/176), 17/17 lines exact.
- **Pitch check:** every female line ≥ 165 Hz and every male line ≤ 150 Hz: yes.
- **Result:** PASS.
Gate PASS on this computer (CPU, float32). A person still needs to listen to the whole file once.

## Rebuild

From the repository root: `bash level3/drafts/audio/tools/run_audio_L3.sh 3` (builds the file, then runs the checks and the gate; see "Running audio locally" in AGENTS.md). Takes are cached in `tools/cache/` (not committed), so re-runs are fast. When the gate passes, `bash level3/drafts/audio/tools/publish_audio_L3.sh 3` copies `tools/out/L3/L3_L3_*` (mp3, log, check, second opinion, gate) into this folder and writes this README. `tools/scripts/script_L3_L3.py` is generated from the lesson by `tools/make_script_L3.py`, so the audio always matches the script in the lesson.

Script © 2026 the authors, CC BY-NC-SA 4.0.
