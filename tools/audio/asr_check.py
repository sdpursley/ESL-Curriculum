"""ASR self-check: python asr_check.py ENGINE [L1 ...] [--single]  (--single: one play, checks samples/ENGINE_Lx_single.wav)  -> WER per lesson vs script, list of diffs."""
import sys, os, difflib, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scripts import LESSONS; from textnorm import words
from scripts_v5 import LESSONS as _L5; LESSONS = {**LESSONS, **_L5}
from faster_whisper import WhisperModel
args = [x for x in sys.argv[1:] if not x.startswith('--')]; SINGLE = '--single' in sys.argv
SUFFIX = os.environ.get('SUFFIX', '_single' if SINGLE else '')
eng = args[0]; keys = args[1:] or list(LESSONS)
m = WhisperModel(os.environ.get("ASR_MODEL", "small.en"), device="cpu", compute_type="int8")
import numpy as np, soundfile as sf
def transcribe_by_pauses(path, gap=0.6):
    """Whole-file Whisper can loop/hallucinate on long synthetic dialogues; transcribe each
    pause-separated stretch (~one line) separately and join."""
    a, sr = sf.read(path, dtype='float32')
    if a.ndim > 1: a = a.mean(1)
    f = int(0.01*sr); n = len(a)//f
    db = 20*np.log10(np.sqrt((a[:n*f].reshape(n, f)**2).mean(1)) + 1e-9); sp = db > db.max() - 45
    segs, start, quiet = [], None, 0
    for i, v in enumerate(sp):
        if v:
            if start is None: start = i
            quiet = 0
        elif start is not None:
            quiet += 1
            if quiet*0.01 >= gap: segs.append((start, i - quiet + 1)); start = None; quiet = 0
    if start is not None: segs.append((start, n))
    # merge into windows of <= WIN s (very short snippets make Whisper hallucinate; whole files can loop)
    WIN = float(os.environ.get('ASR_WIN', '15')); merged = []
    for s0, e0 in segs:
        if merged and (e0 - merged[-1][0])*0.01 <= WIN: merged[-1] = (merged[-1][0], e0)
        else: merged.append((s0, e0))
    segs = merged
    out = []
    for s0, e0 in segs:
        x = a[max(0, s0*f - int(0.2*sr)):min(len(a), e0*f + int(0.2*sr))]
        x = np.concatenate([np.zeros(int(0.3*sr), np.float32), x, np.zeros(int(0.3*sr), np.float32)])
        x16 = np.interp(np.linspace(0, len(x), int(len(x)*16000/sr), endpoint=False), np.arange(len(x)), x).astype(np.float32)
        r, _ = m.transcribe(x16, beam_size=5, language="en", condition_on_previous_text=False)
        out.append(" ".join(t.text for t in r))
    return " ".join(out)
d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'samples')
for k in keys:
    intro, lines = LESSONS[k]; dl = " ".join(l for _, l in lines)
    R = words(f"{intro} {dl} That's the end of the listening." if SINGLE else f"{intro} {dl} Listen again. {dl} That's the end of the listening.")
    H = words(transcribe_by_pauses(f"{d}/{eng}_{k}{SUFFIX}.wav"))
    ops = [o for o in difflib.SequenceMatcher(None, R, H, autojunk=False).get_opcodes() if o[0] != 'equal']
    err = sum(max(b-a, dd-c) for _, a, b, c, dd in ops)
    print(f"{k}: WER {err/len(R):.2%} ({err}/{len(R)} words)", [(o, " ".join(R[a:b]), " ".join(H[c:dd])) for o, a, b, c, dd in ops])
    if k == "L1": print("  'where' count ref/hyp:", R.count("where"), H.count("where"))
