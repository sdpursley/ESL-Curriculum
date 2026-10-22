# Level 1 Lesson 13 audio (`L1_L13_*` files in this folder)

| File | What it is |
|---|---|
| `L1_L13_listening.mp3` | **The classroom file** (96 kbps mono, -16.8 LUFS, peak 0.913, 1:08). Intro → the conversation **once** (no repeat) → "That's the end of the listening." The teacher presses play again for the next listen. |
| `L1_L13_check_results.json` | Whole-file check of the MP3: Whisper (faster-whisper `small.en`) on the whole file and on every line alone, pitch of each voice, pause noise, clicks, clipping, loudness. |
| `L1_L13_regen_log.json` | Settings and the chosen take for every sentence (seed, what Whisper heard, confidence, pitch, how many takes were tried), plus the start and end time of every line. |

## Voices

All voices are **synthetic**: Chatterbox TTS (Resemble AI, MIT License) cloned **only** from short reference clips made with Kokoro-82M (Apache 2.0). No recordings of real people, and never Chatterbox's built-in default voice. Every file carries an inaudible Perth watermark.

| Character | Reference clip | Made with | Voice | Median pitch in the file |
|---|---|---|---|---|
| Narrator | `tools/audio/samples/refs/N.wav` | Kokoro-82M `af_sarah` | female | 190.3 Hz |
| Manager | `tools/audio/samples/refs/Sam.wav` | Kokoro-82M `am_michael` | male | 133.8 Hz |
| Ana | `level1/audio/tools/natural/kokoro_refs/af_jessica.wav` | Kokoro-82M `af_jessica` | female | 216.1 Hz |

Female voices are checked to be clearly female (median pitch above 165 Hz for every take); male voices below 150 Hz.

## Settings

Chatterbox `exaggeration 0.72`, `cfg_weight 0.32`, CPU. Each sentence is **one whole take** (no comma splitting, no letter splicing, no time-stretching), at normal pace. Pauses: **1.4 s between speakers**, 0.55 s between two sentences of the same speaker. Whole file leveled to -16 LUFS; a look-ahead limiter (ffmpeg `alimiter`, -1 dBFS) catches the few peaks, so nothing is clipped.

## Checks (what was done)

- **Every take** (167 takes tried for 24 sentences): Whisper `small.en` must hear exactly the script words; all words confident (≥ 0.5); no cut-off start or end; no artifact flags (`artifacts.py`: drones, breaths, sound outside the words, clicks, hiss, high whine; checked on the take alone and with silence around it); no clipping; normal length; voice pitch right for the character. Of the passing takes, the clearest and most natural (confidence + pitch movement) is kept.
- **Whole file:** WER **3.4%** (4 errors in 119 words), **14/14 lines** heard exactly on their own; clipped samples: 0; peak 0.913; click ratio 4.9; no noise in the pauses; gaps between speakers 1.4–1.4 s.
Expanded to L5–7 depth; dialogue ≥1:00.
see VOICES in script

## Rebuild

From `level1/audio/tools/lessons/`, with the audio environment from section 5 of MAINTAINING.md (CPU; takes are cached in `cache/`, output goes to `out/`; neither is committed):

```
../../../../.venv-audio/bin/python script_match.py ../../../curriculum/Level1_Lesson13.md script_L1_L13.py
../../../../.venv-audio/bin/python build_listening.py script_L1_L13.py $PWD/out/L1_L13_listening
../../../../.venv-audio/bin/python check_listening.py script_L1_L13.py out/L1_L13_listening.mp3 out/L1_L13_listening_log.json out/L1_L13_check_results.json
../../../../.venv-audio/bin/python second_opinion.py script_L1_L13.py out/L1_L13_listening.mp3
```

Then copy `out/L1_L13_listening.mp3` into `level1/audio/`, with `out/L1_L13_listening_log.json` as `L1_L13_regen_log.json` and the check JSON as `L1_L13_check_results.json`.
The WAV master is not committed. `script_L1_L13.py` is the listening script used for the audio; keep it the same as the script in `Level1_Lesson13.md`. Names in the script are invented.
