"""Extension of asr_check.py for published mp3s: python asr_check_mp3.py L5 ... Midterm Final
Converts each <key>_listening.mp3 to wav (ffmpeg), transcribes by pauses with word timestamps,
aligns vs single-play reference (intro + dialogue + end cue), prints WER + timestamped diffs + repeat check."""
import sys, os, difflib, json, subprocess, tempfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scripts_v5 import LESSONS; from textnorm import words
from faster_whisper import WhisperModel
import numpy as np, soundfile as sf
m = WhisperModel(os.environ.get("ASR_MODEL", "small.en"), device="cpu", compute_type="int8")
D = os.path.dirname(os.path.abspath(__file__))
def to_wav(p):
    out = tempfile.mktemp(suffix='.wav'); subprocess.run(['ffmpeg','-v','error','-y','-i',p,'-ac','1','-ar','16000',out], check=True); return out
def transcribe(path, gap=0.6, WIN=15.0):
    a, sr = sf.read(path, dtype='float32'); f = int(0.01*sr); n = len(a)//f
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
    W = []  # (word, time)
    for s0, e0 in merged:
        off = max(0, s0*f-int(0.2*sr)); x = a[off:min(len(a), e0*f+int(0.2*sr))]
        x = np.concatenate([np.zeros(int(0.3*sr), np.float32), x, np.zeros(int(0.3*sr), np.float32)])
        r, _ = m.transcribe(x, beam_size=5, language="en", condition_on_previous_text=False, word_timestamps=True)
        for seg in r:
            for w in (seg.words or []):
                t = off/sr + w.start - 0.3
                W.append((w.word, max(0, t), w.probability))
    # merge whisper sub-tokens ("o" + "'clock") and expand "$45" before textnorm
    import re; out = []
    for tok, t, p in W:
        if out and tok.strip().startswith("'"): out[-1] = (out[-1][0] + tok.strip(), out[-1][1], min(out[-1][2], p))
        else: out.append((tok.strip(), t, p))
    W = []
    for tok, t, p in out:
        tok = re.sub(r'\$(\d+)', r'\1 dollars', tok)
        for x in words(tok): W.append((x, t, p))
    return W
res = {}
for k in sys.argv[1:]:
    intro, lines = LESSONS[k]; dl = " ".join(l for _, l in lines)
    R = words(f"{intro} {dl} That's the end of the listening.")
    wav = to_wav(f"{D}/{k}_listening.mp3"); W = transcribe(wav); os.remove(wav)
    H = [w for w,_,_ in W]; T = [t for _,t,_ in W]
    ops = [o for o in difflib.SequenceMatcher(None, R, H, autojunk=False).get_opcodes() if o[0] != 'equal']
    err = sum(max(b-a_, dd-c) for _, a_, b, c, dd in ops)
    diffs = []
    for o, a_, b, c, dd in ops:
        t = T[c] if c < len(T) else (T[-1] if T else 0)
        diffs.append(dict(t=round(t,1), op=o, ref=" ".join(R[a_:b]), hyp=" ".join(H[c:dd]),
                          ctx=" ".join(R[max(0,a_-4):b+4]), prob=[round(p,2) for _,_,p in W[c:dd]]))
    # repeat check: any 5-gram of hyp occurring more often than in ref
    from collections import Counter
    ng = lambda L: Counter(tuple(L[i:i+5]) for i in range(len(L)-4))
    cr, ch = ng(R), ng(H); reps = [(" ".join(g), cr[g], ch[g]) for g in ch if ch[g] > cr[g]]
    # line-level: each script line count in hyp
    hs = " ".join(H); lc = [(l, hs.count(" ".join(words(l)))) for _, l in lines if len(words(l)) >= 3]
    res[k] = dict(wer=err/len(R), err=err, n=len(R), diffs=diffs, repeats=reps, lines_twice=[x for x in lc if x[1] > 1], hyp=hs)
    print(f"{k}: WER {err/len(R):.2%} ({err}/{len(R)})", flush=True)
    for d_ in diffs: print("  ", d_, flush=True)
    print("  repeats:", reps, "lines>1:", res[k]['lines_twice'], flush=True)
json.dump(res, open(os.environ.get('OUT', '/workspace/asr_mp3_results.json'), 'w'), indent=1)
