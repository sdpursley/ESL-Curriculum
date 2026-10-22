"""Whole-file check of a finished listening MP3 (same method as Lesson 1's check_L1.py).
Usage: python check_listening.py script_LN.py file.mp3 file_log.json OUT.json
Whisper (faster-whisper small.en) on the whole file vs the script (WER, diffs, repeats, low-confidence words), then each line alone
(using the line times in the build log), plus pause noise, clicks, clipping, peak, loudness, and the voice pitch of each speaker."""
import sys, os, difflib, json, subprocess, tempfile, importlib.util, numpy as np, soundfile as sf, pyloudnorm as pyln
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', 'tools', 'audio'))   # <repo>/tools/audio: processor.py, artifacts.py, textnorm.py
sys.path[:0] = [HERE, TOOLS]
from canon import canon
from artifacts import detect
from metrics import prosody
from faster_whisper import WhisperModel
SCRIPT, MP3, LOGF, OUT = sys.argv[1:5]
spec = importlib.util.spec_from_file_location('S', SCRIPT); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
SAME = getattr(S, 'SAME', {})
m = WhisperModel('small.en', device='cpu', compute_type='int8')
wav = tempfile.mktemp(suffix='.wav'); subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', MP3, '-ac', '1', '-ar', '16000', wav], check=True)
a, sr = sf.read(wav, dtype='float32'); os.remove(wav)
def tr(x):
    x = np.concatenate([np.zeros(int(0.3*sr), np.float32), x, np.zeros(int(0.3*sr), np.float32)])
    r, _ = m.transcribe(x, beam_size=5, language='en', condition_on_previous_text=False, word_timestamps=True)
    return [(w.word, w.start-0.3, w.probability) for s in r for w in (s.words or [])]
LT = json.load(open(LOGF))['line_times']
# whole file in ~15 s windows cut at pauses (the line boundaries)
bounds = [0.0] + [t1 + 0.3 for _, t1, _, _ in LT] + [len(a)/sr]
wins = []; s0 = 0.0
for b in bounds[1:]:
    if b - s0 >= 12 or b == bounds[-1]: wins.append((s0, b)); s0 = b
W = []
for x0, x1 in wins:
    for w, t, p in tr(a[int(x0*sr):int(x1*sr)]): W.append((w, round(x0+t, 2), round(p, 2)))
INTRO = S.INTRO if isinstance(S.INTRO, str) else ' '.join(S.INTRO)
R = canon(INTRO + ' ' + ' '.join(L[1] for L in S.LINES) + ' ' + S.END, SAME)
H = canon(' '.join(w for w, _, _ in W), SAME)
ops = [o for o in difflib.SequenceMatcher(None, R, H, autojunk=False).get_opcodes() if o[0] != 'equal']
err = sum(max(b-a_, d-c) for _, a_, b, c, d in ops)
diffs = [dict(op=o, ref=' '.join(R[a_:b]), hyp=' '.join(H[c:d]), ctx=' '.join(R[max(0, a_-4):b+4])) for o, a_, b, c, d in ops]
lowp = [(w.strip(), t, p) for w, t, p in W if p < 0.4]
# per line
per = []; pitch = {}
for t0, t1, spk, line in LT:
    x = a[max(0, int((t0-0.15)*sr)):int((t1+0.15)*sr)]
    Wl = tr(x); hl = canon(' '.join(w for w, _, _ in Wl), SAME); rl = canon(line, SAME)
    fl, _ = detect(x, sr, line, None); fl = [f for f in fl if not f.startswith('too long')]
    x24 = np.interp(np.linspace(0, len(x), int(len(x)*24000/sr), endpoint=False), np.arange(len(x)), x).astype(np.float32)
    pr = prosody(x24); pitch.setdefault(spk, []).append(pr.get('f0_med', 0))
    per.append(dict(t=t0, spk=spk, line=line, ok=hl == rl, hyp=' '.join(hl), min_prob=round(min([p for *_, p in Wl] or [0]), 2), flags=fl, f0_med=pr.get('f0_med')))
# narrator intro/end pitch
x = a[:int(LT[0][0]*sr)]; x24 = np.interp(np.linspace(0, len(x), int(len(x)*24000/sr), endpoint=False), np.arange(len(x)), x).astype(np.float32)
pitch.setdefault('Narrator', []).append(prosody(x24).get('f0_med', 0))
# pauses, noise, clicks, clipping
f = int(0.01*sr); n = len(a)//f; db = 20*np.log10(np.sqrt((a[:n*f].reshape(n, f)**2).mean(1)) + 1e-9); sp = db > db.max() - 45
pauses = []; run = 0
for i, v in enumerate(list(sp) + [True]):
    if not v: run += 1
    else:
        if run*0.01 >= 0.3: pauses.append((i-run, i))
        run = 0
pdb = [float(np.median(db[s+15:e-15])) if e-s > 40 else -120.0 for s, e in pauses]
loud = [(round(s*0.01, 2), round(e*0.01, 2), round(d-db.max(), 1)) for (s, e), d in zip(pauses, pdb) if d-db.max() > -55]
d = np.abs(np.diff(a)); click = float(d.max()/(np.percentile(d, 99.5)+1e-6))
spk_gaps = [round(LT[i+1][0]-LT[i][1], 2) for i in range(len(LT)-1) if LT[i+1][2] != LT[i][2]]
res = dict(file=os.path.basename(MP3), duration_s=round(len(a)/sr, 2), wer=round(err/len(R), 4), errors=err, ref_words=len(R), diffs=diffs,
           low_prob_words=lowp, lines_ok=f"{sum(p['ok'] for p in per)}/{len(per)}", lines_with_flags=[p for p in per if p['flags']],
           lines_not_exact=[p for p in per if not p['ok']],
           pitch_median_hz={k: round(float(np.median([v for v in vs if v])), 1) for k, vs in pitch.items()},
           gap_between_speakers_s=[min(spk_gaps), max(spk_gaps)] if spk_gaps else None,
           pauses_with_sound_above_minus55dB=loud, click_ratio=round(click, 1), peak=round(float(np.abs(a).max()), 3),
           clipped_samples=int((np.abs(a) > 0.985).sum()), loudness_lufs=round(pyln.Meter(sr).integrated_loudness(a), 1),
           per_line=per, hyp=' '.join(H))
json.dump(res, open(OUT, 'w'), indent=1, default=str)
print(json.dumps({k: v for k, v in res.items() if k not in ('per_line', 'hyp')}, indent=1, default=str))
