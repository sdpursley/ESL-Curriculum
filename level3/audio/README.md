# Level 3 Lesson 1 audio: sources and checks

| File | What it is |
|---|---|
| `L3_L1_listening.mp3` | Classroom file (96 kbps mono, 1:31). Narrator intro → conversation **once** → "That's the end of the listening." The teacher presses play again for the second listen. |
| `L3_L1_listening_log.json` | Settings, chosen take (seed, Whisper result, pitch) for every line, and each line's start/end time. |
| `L3_L1_check_results.json` | Whole-file and per-line check of the MP3 (Whisper `small.en` word comparison, pause, noise, click, clipping, pitch by speaker). |

**Speakers (3):** Narrator, Elena (female), David (male). Names and story are invented; the script is in `level3/curriculum/Level3_Lesson1.md` (and `tools/script_L3_L1.py`).

## Voices and references

Chatterbox TTS (Resemble AI, MIT License), cloned **only from synthetic reference clips made with Kokoro-82M** (hexgrad, Apache License 2.0):

| Character | Reference clip | Kokoro voice | Chatterbox settings |
|---|---|---|---|
| Narrator | `tools/audio/samples/refs/N.wav` | af_sarah | exaggeration 0.55, cfg 0.40 |
| Elena | `tools/audio/samples/refs/Rosa.wav` | af_heart | exaggeration 0.72, cfg 0.32 |
| David | `tools/audio/samples/refs/Sam.wav` | am_michael | exaggeration 0.72, cfg 0.32 |

No recordings of real people were used (no audiobook or speech-dataset voices), and neither Chatterbox's built-in default voice nor the "Agent" clip was used. Every file carries an inaudible Perth watermark.

## How it was made and checked

- `tools/build_L3_L1.py`: one whole-sentence take per line (several seeds; normal pace, no splicing or time-stretching). A take is kept only if Whisper hears exactly the script words, nothing is cut at the edges, the artifact detector finds nothing, and the pitch fits the character (female ≥ 165 Hz, male ≤ 150 Hz median F0). About 1.4 s between speakers.
- `tools/check_L3_L1.py`: checks the finished MP3. Result: every line passes Whisper on its own with no artifact flags; no clipping; median pause between speakers 1.41 s. Median pitch: Elena 229 Hz (lowest line 187 Hz), David 124 Hz (highest line 146 Hz), Narrator 171–205 Hz.

Script © 2026 the authors, CC BY-NC-SA 4.0.
