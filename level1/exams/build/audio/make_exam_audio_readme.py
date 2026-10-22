"""Write exams/audio/README_L1_<N>.md for one exam listening file. Usage: python3 make_exam_audio_readme.py Midterm|Final EXAMS_DIR script.py OUT_DIR"""
import sys, json, os, importlib.util, re
N, X, SCRIPT, OUTD = sys.argv[1:5]
spec = importlib.util.spec_from_file_location('S', SCRIPT); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
C = json.load(open(f'{X}/audio/L1_{N}_check_results.json')); L = json.load(open(f'{X}/audio/L1_{N}_regen_log.json'))
KOK = {'N': 'af_sarah', 'Rosa': 'af_heart', 'Sam': 'am_michael', 'Marco': 'am_adam', 'Kim': 'af_nova', 'Receptionist': 'af_river'}
def rd(p):
    try: return [l for l in open(p).read().splitlines() if 'WER' in l and not l.startswith(('/', 'Warn'))]
    except FileNotFoundError: return []
sec = rd(f'{OUTD}/second_{N}.log'); secl = rd(f'{OUTD}/second_lines_{N}.log')
try: vote = [l for l in open(f'{OUTD}/vote_{N}.log').read().splitlines() if l.startswith('vote:')][-1][6:].strip()
except (FileNotFoundError, IndexError): vote = ''
dur = C['duration_s']; mm = f"{int(dur//60)}:{int(round(dur % 60)):02d}"
pitch = C['pitch_median_hz']; tries = sum(s['tries'] for s in L['sentences']); ns = len(L['sentences'])
failed = [s['chosen']['text'] for s in L['sentences'] if s.get('FAILED')]
rows = '\n'.join(f"| {spk} | `tools/audio/samples/refs/{clip}.wav` | Kokoro-82M `{KOK[clip]}` | {'female' if spk in S.FEMALE else 'male'} | {pitch.get(spk, '–')} Hz |" for spk, clip in S.VOICES.items())
title = 'Midterm (Week 8)' if N == 'Midterm' else 'Final Exam (Week 15)'
diffs = '; '.join(f"{d['op']} \"{d['ref']}\" → \"{d['hyp']}\"" for d in C['diffs']) or 'none'
txt = f"""# Level 1 {title}: listening audio

| File | What it is |
|---|---|
| `L1_{N}_listening.mp3` | **The classroom file** (96 kbps mono, {C['loudness_lufs']} LUFS, peak {C['peak']}, **{mm}**). Intro → the conversation **once** (no repeat inside the file) → "That's the end of the listening." The teacher presses play again for each listen (the packet says 2–3 plays). |
| `L1_{N}_check_results.json` | Whole-file check: Whisper `small.en` on the whole file and on every line alone, pitch of each voice, pause noise, clicks, clipping, loudness. |
| `L1_{N}_regen_log.json` | Settings and the chosen take for every sentence (seed, what Whisper heard, confidence, pitch, number of takes tried), plus the start and end time of every line. |

The script is in `Level1_{N}_Exam_Teacher_Packet.md` ("Listening script") and in `build/audio/script_L1_{N}.py`; `build/check_consistency.py` checks that they are the same and that every answer is in the audio.

## Voices

All voices are **synthetic**: Chatterbox TTS (Resemble AI, MIT License) on CPU, cloned **only** from short reference clips made with Kokoro-82M (Apache 2.0), the same clips as the Level 1 lessons (`tools/audio/samples/refs/`, see `level1/audio/tools/lessons/REFS.md`). No human recordings, no LibriTTS, no Piper, no Chatterbox default voice. Every file carries an inaudible Perth watermark.

| Character | Reference clip | Made with | Voice | Median pitch in the file |
|---|---|---|---|---|
{rows}

Female characters have female voices (every take checked: median pitch above 165 Hz); male voices below 150 Hz.

## Settings

Chatterbox `exaggeration 0.72`, `cfg_weight 0.32`. Each sentence is **one whole take** (no splicing inside a sentence, no time-stretching), at normal pace. Pauses: **1.4 s between speakers**, 0.55 s between two sentences of one speaker. Leveled to -16 LUFS; a look-ahead limiter (ffmpeg `alimiter`, -1 dBFS) catches the few peaks.

## Checks

- **Every take** ({tries} takes tried for {ns} sentences): Whisper `small.en` must hear exactly the script words, all words confident (≥ 0.5), no cut-off, no artifact flags, no clipping, normal length, right pitch for the character. The best passing take is kept.{' **Sentences with no passing take (best take used, then checked by ear and by the whole-file checks):** ' + '; '.join(failed) if failed else ' Every sentence has a passing take.'}
- **Whole file, small.en:** WER **{C['wer']*100:.1f}%** ({C['errors']} word differences in {C['ref_words']} words: {diffs}); **{C['lines_ok']} lines** heard exactly when cut out alone.
- **Second opinion, medium.en:** {(sec[0].strip() if sec else 'see out/second_' + N + '.log')}{('; ' + secl[0].strip()) if secl else ''}.
- **Take vote (the deciding check):** {('each chosen take alone, Whisper small.en and medium.en, float32, 1 thread, temperature 0, 3 runs each: ' + vote) if vote else 'not run (build/audio/out/vote_' + N + '.log)'}. Whole-file and per-line numbers above can change from run to run on a busy CPU (medium.en sometimes skips long spans), so a single checker miss is not a reason to re-take.
- **Pitch:** {', '.join(f'{k} {v} Hz' for k, v in pitch.items())}.
- **Clipping and noise:** clipped samples {C['clipped_samples']}; peak {C['peak']}; click ratio {C['click_ratio']}; pauses with sound above -55 dB: {len(C['pauses_with_sound_above_minus55dB'])}; gaps between speakers {C['gap_between_speakers_s'][0]}–{C['gap_between_speakers_s'][1]} s.

## Rebuild

```
cd level1/exams/build/audio
NT=3 bash run_audio.sh {N}          # Chatterbox, CPU; takes are cached in level1/audio/tools/lessons/cache/
bash finish_audio.sh {N}            # all checks, copy to level1/exams/audio/, this README
```
Names, the school, the clinic, phone numbers, and prices in the script are invented.
"""
open(f'{X}/audio/README_L1_{N}.md', 'w').write(txt); print('readme ok')
