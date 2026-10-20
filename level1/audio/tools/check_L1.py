"""Whole-file checks for Level 1 Lesson 1 audio (same method as asr_check_mp3.py):
python check_L1.py path/to/L1_listening.mp3  -> WER vs script, timestamped diffs, repeat check, plus pause/noise/click/clipping checks."""
import sys, os, difflib, json, subprocess, tempfile, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools', 'audio')))  # textnorm.py, artifacts.py
from textnorm import words
from script_L1 import INTRO, LINES, END, plain
from faster_whisper import WhisperModel
import numpy as np, soundfile as sf
m = WhisperModel(os.environ.get("ASR_MODEL", "small.en"), device="cpu", compute_type="int8")
SPOKEN = {'vee': 'v', 'bee': 'b', 'gee': 'g', 'zee': 'z'}
def to_wav(p):
    out = tempfile.mktemp(suffix='.wav'); subprocess.run(['ffmpeg','-v','error','-y','-i',p,'-ac','1','-ar','16000',out], check=True); return out
def transcribe(a, sr, gap=0.6, WIN=15.0):
    f = int(0.01*sr); n = len(a)//f
    db = 20*np.log10(np.sqrt((a[:n*f].reshape(n, f)**2).mean(1)) + 1e-9); sp = db > db.max() - 45
    segs, start, quiet = [], None, 0
    for i, v in enumerate(sp):
        if v:
            if start is None: start = i
            quiet = 0
        elif start is not None:
            quiet += 1
            if quiet*0.01 >= gap: segs.append((start, i-quiet+1)); start=None; quiet=0
    if start is not None: segs.append((start, n))
    merged = []
    for s0, e0 in segs:
        if merged and (e0-merged[-1][0])*0.01 <= WIN: merged[-1] = (merged[-1][0], e0)
        else: merged.append((s0, e0))
    W = []
    for s0, e0 in merged:
        off = max(0, s0*f-int(0.2*sr)); x = a[off:min(len(a), e0*f+int(0.2*sr))]
        x = np.concatenate([np.zeros(int(0.3*sr), np.float32), x, np.zeros(int(0.3*sr), np.float32)])
        r, _ = m.transcribe(x, beam_size=5, language="en", condition_on_previous_text=False, word_timestamps=True)
        for seg in r:
            for w in (seg.words or []):
                for t in words(w.word): W.append((SPOKEN.get(t, t), round(max(0, off/sr + w.start - 0.3), 2), round(w.probability, 2)))
    return W, segs, db
path = sys.argv[1]
wav = to_wav(path); a, sr = sf.read(wav, dtype='float32'); os.remove(wav)
R = words(f"{INTRO} {' '.join(plain(l) for _, l in LINES)} {END}")
W, segs, db = transcribe(a, sr); H = [w for w, _, _ in W]
ops = [o for o in difflib.SequenceMatcher(None, R, H, autojunk=False).get_opcodes() if o[0] != 'equal']
err = sum(max(b-a_, dd-c) for _, a_, b, c, dd in ops)
diffs = [dict(t=W[c][1] if c < len(W) else None, op=o, ref=" ".join(R[a_:b]), hyp=" ".join(H[c:dd]), ctx=" ".join(R[max(0,a_-4):b+4])) for o, a_, b, c, dd in ops]
from collections import Counter
ng = lambda L: Counter(tuple(L[i:i+5]) for i in range(len(L)-4)); cr, ch = ng(R), ng(H)
reps = [" ".join(g) for g in ch if ch[g] > cr[g]]
# low-probability words (possible mumbles)
lowp = [(w, t, p) for w, t, p in W if p < 0.4]
# pauses: noise floor inside pauses >= 0.3 s
f = int(0.01*sr); sp = db > db.max() - 45; pauses = []; run = 0
for i, v in enumerate(list(sp) + [True]):
    if not v: run += 1
    else:
        if run*0.01 >= 0.3: pauses.append((i-run, i))
        run = 0
pause_db = [float(np.median(db[s+15:e-15])) if e-s > 40 else -120.0 for s, e in pauses]   # middle of each pause (skip 150 ms speech tails)
loud_pauses = [(round(s*0.01, 2), round(e*0.01, 2), round(d - db.max(), 1)) for (s, e), d in zip(pauses, pause_db) if d - db.max() > -55]
d = np.abs(np.diff(a)); click = float(d.max()/(np.percentile(d, 99.5)+1e-6))
peak = float(np.abs(a).max()); clip = int((np.abs(a) > 0.985).sum())
gaps = sorted(round((e-s)*0.01, 2) for s, e in pauses)
res = dict(file=path, duration_s=round(len(a)/sr, 2), wer=round(err/len(R), 4), errors=err, ref_words=len(R), diffs=diffs, repeats=reps,
           low_prob_words=lowp, n_pauses=len(pauses), pause_len_min_median_max=[gaps[0], gaps[len(gaps)//2], gaps[-1]] if gaps else None,
           pauses_with_sound_above_minus55dB=loud_pauses, click_ratio=round(click, 1), peak=round(peak, 3), clipped_samples=clip, hyp=" ".join(H))
# per-line checks (needs the line times written by build_L1_audio.py): ASR of each line alone + artifacts.py on each line
LT = os.environ.get('LINE_TIMES')
if LT:
    from artifacts import detect
    per = []
    for t0, t1, spk, line in json.load(open(LT))['line_times']:
        x = a[max(0, int((t0-0.15)*sr)):int((t1+0.15)*sr)]   # small margin so a word at the edge is not cut off
        Wl, _, _ = transcribe(x, sr); hl = [w for w, _, _ in Wl]; rl = words(plain(line))
        fl, met = detect(x, sr, plain(line), None)
        fl = [f_ for f_ in fl if not f_.startswith('too long')]
        per.append(dict(t=t0, spk=spk, line=plain(line), ok=hl == rl, hyp=" ".join(hl), min_prob=min([p_ for *_, p_ in Wl] or [0]), flags=fl))
    res['per_line'] = per
print(json.dumps({k: v for k, v in res.items() if k != 'hyp'}, indent=1)); print('HYP:', res['hyp'])
json.dump(res, open(os.environ.get('OUT', 'L1_check_results.json'), 'w'), indent=1)
