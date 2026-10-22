# Level 1 Midterm (Week 8): listening audio

| File | What it is |
|---|---|
| `L1_Midterm_listening.mp3` | **The classroom file** (96 kbps mono, -16.8 LUFS, peak 0.891, **1:23**). Intro → the conversation **once** (no repeat inside the file) → "That's the end of the listening." The teacher presses play again for each listen (the packet says 2–3 plays). |
| `L1_Midterm_check_results.json` | Whole-file check: Whisper `small.en` on the whole file and on every line alone, pitch of each voice, pause noise, clicks, clipping, loudness. |
| `L1_Midterm_regen_log.json` | Settings and the chosen take for every sentence (seed, what Whisper heard, confidence, pitch, number of takes tried), plus the start and end time of every line. |

The script is in `Level1_Midterm_Exam_Teacher_Packet.md` ("Listening script") and in `build/audio/script_L1_Midterm.py`; `build/check_consistency.py` checks that they are the same and that every answer is in the audio.

## Voices

All voices are **synthetic**: Chatterbox TTS (Resemble AI, MIT License) on CPU, cloned **only** from short reference clips made with Kokoro-82M (Apache 2.0), the same clips as the Level 1 lessons (`tools/audio/samples/refs/`, see `level1/audio/tools/lessons/REFS.md`). No human recordings, no LibriTTS, no Piper, no Chatterbox default voice. Every file carries an inaudible Perth watermark.

| Character | Reference clip | Made with | Voice | Median pitch in the file |
|---|---|---|---|---|
| Narrator | `tools/audio/samples/refs/N.wav` | Kokoro-82M `af_sarah` | female | 201.6 Hz |
| Receptionist | `tools/audio/samples/refs/Receptionist.wav` | Kokoro-82M `af_river` | female | 191.9 Hz |
| Marco | `tools/audio/samples/refs/Marco.wav` | Kokoro-82M `am_adam` | male | 111.7 Hz |

Female characters have female voices (every take checked: median pitch above 165 Hz); male voices below 150 Hz.

## Settings

Chatterbox `exaggeration 0.72`, `cfg_weight 0.32`. Each sentence is **one whole take** (no splicing inside a sentence, no time-stretching), at normal pace. Pauses: **1.4 s between speakers**, 0.55 s between two sentences of one speaker. Leveled to -16 LUFS; a look-ahead limiter (ffmpeg `alimiter`, -1 dBFS) catches the few peaks.

## Checks

- **Every take** (165 takes tried for 29 sentences): Whisper `small.en` must hear exactly the script words, all words confident (≥ 0.5), no cut-off, no artifact flags, no clipping, normal length, right pitch for the character. The best passing take is kept. **Sentences with no passing take (best take used, then checked by ear and by the whole-file checks):** L, I, M, A.
- **Whole file, small.en:** WER **5.0%** (7 word differences in 139 words: delete "listen" → ""; delete "tuesday and thursday at 630 great" → ""); **13/20 lines** heard exactly when cut out alone.
- **Second opinion, medium.en:** medium.en WER 0.324 (45/139); medium.en per-line WER 0.050 (7/139), 19/22 lines exact.
- **Take vote (the deciding check):** each chosen take alone, Whisper small.en and medium.en, float32, 1 thread, temperature 0, 3 runs each: 29/29 takes OK (majority of 6 runs exact). Whole-file and per-line numbers above can change from run to run on a busy CPU (medium.en sometimes skips long spans), so a single checker miss is not a reason to re-take.
- **Pitch:** Receptionist 191.9 Hz, Marco 111.7 Hz, Narrator 201.6 Hz.
- **Clipping and noise:** clipped samples 0; peak 0.891; click ratio 4.7; pauses with sound above -55 dB: 0; gaps between speakers 1.4–1.4 s.

## Rebuild

```
cd level1/exams/build/audio
NT=3 bash run_audio.sh Midterm          # Chatterbox, CPU; takes are cached in level1/audio/tools/lessons/cache/
bash finish_audio.sh Midterm            # all checks, copy to level1/exams/audio/, this README
```
Names, the school, the clinic, phone numbers, and prices in the script are invented.
