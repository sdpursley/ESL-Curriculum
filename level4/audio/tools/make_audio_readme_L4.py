"""Write level4/audio/L4_LN_README.md from the build log, the check JSON, the medium.en second opinion and the gate JSON.
Usage: python make_audio_readme_L4.py N ['notes (markdown, may be empty)']   (run by publish_audio_L4.sh)"""
import sys, json, importlib.util, os
N = sys.argv[1]; NOTES = sys.argv[2] if len(sys.argv) > 2 else ''
B = os.path.dirname(os.path.abspath(__file__)); A = os.path.dirname(B)
spec = importlib.util.spec_from_file_location('S', f'{B}/scripts/script_L4_L{N}.py'); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
C = json.load(open(f'{A}/L4_L{N}_check_results.json')); G = json.load(open(f'{A}/L4_L{N}_gate.json')); L = json.load(open(f'{A}/L4_L{N}_listening_log.json'))
KOK = {'N': 'af_sarah', 'Rosa': 'af_heart', 'Sam': 'am_michael', 'Marco': 'am_adam', 'Receptionist': 'af_river', 'Ana_af_jessica': 'af_jessica',
       'Ana_af_bella': 'af_bella', 'Server': 'am_puck', 'Kim': 'af_nova', 'Carlos': 'am_eric'}
SET = lambda spk: 'exaggeration 0.55, cfg 0.40' if spk == 'Narrator' else 'exaggeration 0.72, cfg 0.32'
per = {}
for p in C['per_line']: per.setdefault(p['spk'], []).append(p['f0_med'])
def prange(spk):
    v = [x for x in per.get(spk, []) if x]
    return f"{min(v):.0f}–{max(v):.0f} Hz" if v else '–'
rows = '\n'.join(f"| {spk} | `tools/refs/{clip}.wav` | {KOK[clip]} | {'female' if spk in S.FEMALE else 'male'} | {SET(spk)} | {G['pitch_median_hz'].get(spk, '–')} Hz (lines {prange(spk)}) |" for spk, clip in S.VOICES.items())
med = G['medium_per_line']
speakers = ', '.join(f"{k} ({'female' if k in S.FEMALE else 'male'})" for k in S.VOICES)
txt = f"""# Level 4 Lesson {N} audio: sources and checks

| File | What it is |
|---|---|
| `L4_L{N}_listening.mp3` | Classroom file (96 kbps mono, {G['duration']}). Narrator intro → conversation **once** → "That's the end of the listening." The teacher presses play again for the second listen. |
| `L4_L{N}_listening_log.json` | Settings, chosen take (seed, Whisper result, pitch) for every sentence, and each line's start/end time. |
| `L4_L{N}_check_results.json` | Whole-file and per-line check of the MP3 (Whisper `small.en`, pauses, noise, clicks, clipping, pitch by speaker, loudness). |
| `L4_L{N}_second_opinion_medium.txt` | Second opinion: Whisper `medium.en` on every line cut from the MP3. |
| `L4_L{N}_gate.json` | Pass/fail summary of all checks. |

**Speakers ({len(S.VOICES)}):** {speakers}. Names and story are invented; the script is in `../curriculum/Level4_Lesson{N}.md`.

## Voices and references

Chatterbox TTS (Resemble AI, MIT License), cloned **only from synthetic reference clips made with Kokoro-82M** (hexgrad, Apache License 2.0); see `tools/REFS_L4.md`:

| Character | Reference clip | Kokoro voice | Voice | Chatterbox settings | Median pitch in the MP3 |
|---|---|---|---|---|---|
{rows}

No recordings of real people were used (no LibriVox / LibriTTS / LibriTTS-R, no Piper), and neither Chatterbox's built-in default voice nor the "Agent" clip was used. Every file carries an inaudible Perth watermark.

## How it was made and checked

- `tools/build_listening_L4.py` (Level 4 copy of `level1/audio/tools/lessons/build_listening.py`): each sentence is **one whole take** (no splicing, no time-stretching), several seeds per sentence. A take is kept only if Whisper `small.en` hears exactly the script words with good confidence, nothing is cut at the edges, the artifact detector finds nothing, nothing clips, and the pitch fits the character (female ≥ 165 Hz, male ≤ 150 Hz median F0). {G['takes_tried']} takes were made for {G['sentences']} sentences. About 1.4 s between speakers, 0.55 s between two sentences of one speaker.
- `tools/check_listening_L4.py` on the finished MP3: whole-file Whisper `small.en` WER **{C['wer']*100:.1f}%** ({G['small_whole_file_errors']} words); **{C['lines_ok']} lines** heard exactly on their own with no artifact flags; clipped samples **{C['clipped_samples']}** (peak {C['peak']}); click ratio {C['click_ratio']}; loudness {C['loudness_lufs']} LUFS; gaps between speakers {G['gap_between_speakers_s'][0]}–{G['gap_between_speakers_s'][1]} s; pauses with noise: {len(G['noisy_pauses'])}.
- **Second opinion** `tools/second_opinion_lines.py` (Whisper `medium.en`, each line alone): WER {med['wer']*100:.1f}% ({med['errors']}/{med['words']}), {med['exact']} lines exact.
- **Pitch check:** every female line ≥ 165 Hz and every male line ≤ 150 Hz: {'yes' if not G['pitch_problems'] else 'NO: ' + str(G['pitch_problems'])}.
- **Result:** {'PASS' if G['PASS'] else 'NOT PASSED: see the gate file'}.
{NOTES}

## Rebuild

From the repository root: `bash level4/audio/tools/run_audio_L4.sh {N}` (builds the file, then runs the checks and the gate; see "Running audio locally" in AGENTS.md). Takes are cached in `tools/cache/` (not committed), so re-runs are fast. When the gate passes, `bash level4/audio/tools/publish_audio_L4.sh {N}` copies `tools/out/L{N}/L4_L{N}_*` (mp3, log, check, second opinion, gate) into this folder and writes this README. `tools/scripts/script_L4_L{N}.py` is generated from the lesson by `tools/make_script_L4.py`, so the audio always matches the script in the lesson.

Script © 2026 the authors, CC BY-NC-SA 4.0.
"""
open(f'{A}/L4_L{N}_README.md', 'w').write(txt); print('README ok')
