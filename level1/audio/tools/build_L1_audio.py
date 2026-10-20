"""Build Level 1 Lesson 1 listening audio with the Level 2 Chatterbox pipeline (processor.py helpers, same refs/settings).
Run: SINGLE=1 TRIES=6 SEED0=2026 EXAG=0.55 CFG=0.45 python build_L1_audio.py
Differences from Level 2 (beginner pace): longer pauses; spelled names {R, U, I, Z.} are made as one piece, checked
letter-by-letter with Whisper, then extra silence is inserted between letters."""
import os, sys, re, json, subprocess, numpy as np, soundfile as sf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# Level 2 pipeline (processor.py, textnorm.py, artifacts.py) and voice reference clips live in <repo>/tools/audio/
TOOLS = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools', 'audio'); sys.path.insert(1, os.path.abspath(TOOLS))
import processor as P
from textnorm import words
from artifacts import detect
from script_L1 import INTRO, LINES, END
P.MIN_WORDS = 3
P.PAUSE.update(comma=0.50, sentence=0.80, speaker=1.15, after_intro=1.6, lead=0.5)
LETTER_GAP = float(os.environ.get('LETTER_GAP', '0.38'))
SPELL_TRIES = int(os.environ.get('SPELL_TRIES', '28'))
SR = P.SR; HERE = os.path.dirname(os.path.abspath(__file__))
refs = f'{os.path.abspath(TOOLS)}/samples/refs'; V = {k: f'{refs}/{k}.wav' for k in ('N', 'Receptionist', 'Ana', 'Carlos')}
say = P.make_engine('chatterbox')
LOG = []
import hashlib, pickle
CACHE = f'{HERE}/cache'; os.makedirs(CACHE, exist_ok=True)
def ckey(*a): return f"{CACHE}/{hashlib.md5(repr(a).encode()).hexdigest()}.pkl"
_synth = P.synth_checked
def synth_cached(say_, text, voice):
    k = ckey('chunk', text, voice, os.environ.get('SEED0'), os.environ.get('EXAG'), os.environ.get('CFG'))
    if os.path.exists(k): return pickle.load(open(k, 'rb'))
    a = _synth(say_, text, voice); pickle.dump(a, open(k, 'wb')); return a
SPOKEN = {'vee': 'v', 'bee': 'b', 'ee': 'e', 'gee': 'g', 'ay': 'a', 'eye': 'i', 'zee': 'z', 'are': 'r', 'you': 'u'}

def asr_words(a):
    P.chunk_score(a, 'x')  # makes sure the Whisper model is loaded
    x = np.concatenate([np.zeros(int(.3*SR), np.float32), a, np.zeros(int(.3*SR), np.float32)])
    x16 = np.interp(np.linspace(0, len(x), int(len(x)*16000/SR), endpoint=False), np.arange(len(x)), x).astype(np.float32)
    segs, _ = P._asr.transcribe(x16, beam_size=5, language='en', word_timestamps=True, condition_on_previous_text=False)
    out = []
    for s in segs:
        for w in (s.words or []):
            for t in words(w.word): out.append((t, w.start-0.3, w.end-0.3, w.probability))
    return out

def spread(a, ws, gap, dip_db=-28):
    """Insert `gap` s of silence between letters, at the quietest 10 ms frame between two letters.
    Only where there is a real dip (<= dip_db below the chunk peak), so a letter is never cut in half."""
    f = int(0.01*SR); n_all = len(a)//f
    db = 20*np.log10(np.sqrt((a[:n_all*f].reshape(n_all, f)**2).mean(1)) + 1e-9); rel = db - db.max()
    cuts = []
    for (_, _, e0, _), (_, s1, _, _) in zip(ws, ws[1:]):
        lo, hi = max(0, int((min(e0, s1)-0.12)/0.01)), min(n_all, int((max(e0, s1)+0.12)/0.01))
        if hi - lo < 2: continue
        k = lo + int(np.argmin(rel[lo:hi]))
        if rel[k] <= dip_db: cuts.append(k*f + f//2)
    parts, prev = [], 0
    fd = int(0.008*SR)
    for c in cuts:
        seg = a[prev:c].copy(); seg[-fd:] *= np.linspace(1, 0, fd)
        if prev: seg[:fd] *= np.linspace(0, 1, fd)
        parts += [seg, P.sil(gap)]; prev = c
    seg = a[prev:].copy(); seg[:fd] *= np.linspace(0, 1, fd); parts.append(seg)
    return np.concatenate(parts), len(cuts)

VARIANTS = {'V, E, G, A.': ['V, E, G, A.', 'Vee, E, G, A.', 'Vee. Ee. Gee. Ay.', 'Vee, ee, gee, ay.']}
FIRST_SEEDS = {'R, U, I, Z.': [65378]}   # seed found in the first run (saves time); then the normal seed list
def spell(text, voice, gap):
    target = words(text); k_ = ckey('spell', text, voice)
    if os.path.exists(k_):
        a, ws, info = pickle.load(open(k_, 'rb')); out, nc = spread(a, ws, gap)
        if [SPOKEN.get(w, w) for w, *_ in asr_words(out)] != words(text): out, nc = a, 0
        LOG.append(dict(info, kind='spell (cached take, re-spaced)', gap=gap, gaps_inserted=nc)); return out
    variants = VARIANTS.get(text, [text, text.replace(',', '.')])
    seeds = FIRST_SEEDS.get(text, []) + [int(os.environ.get('SEED0', '2026')) + k*7919 for k in range(SPELL_TRIES)]
    best = None
    for k, seed in enumerate(seeds):
        t = variants[k % len(variants)] if k >= len(FIRST_SEEDS.get(text, [])) else text
        import torch; torch.manual_seed(seed)
        raw = say(t, voice); P.a_raw_holder[:] = [raw]; a = P.trim(raw)
        ws = asr_words(a); ws = [(SPOKEN.get(w, w) if len(target) == len(ws) else w, s0, e0, p) for w, s0, e0, p in ws]
        hyp = [w for w, *_ in ws]
        _, _, edge = P.speech_bounds(raw)
        flags, _ = detect(a, SR, t, (ws[0][1], ws[-1][2]) if ws else None)
        flags = [x for x in flags if not x.startswith('too long')]
        ok = hyp == target and not edge and not flags and min([p for *_, p in ws] or [0]) >= 0.3
        info = dict(text=t, seed=seed, hyp=' '.join(hyp), flags=flags, edge=bool(edge), probs=[round(p, 2) for *_, p in ws])
        print('SPELL', info, ok, flush=True)
        if ok:
            out, nc = spread(a, ws, gap); ws2 = [SPOKEN.get(w, w) for w, *_ in asr_words(out)]
            info['spread_hyp'] = ' '.join(ws2); info['gaps_inserted'] = nc
            if ws2 != target:
                print('  spread changed ASR ->', ws2, '- keeping the natural spacing of this take', flush=True); out = a; info['gaps_inserted'] = 0
            pickle.dump((a, ws, info), open(k_, 'wb'))
            LOG.append(dict(kind='spell', attempt=k+1, gap=gap, **info)); return out
        if best is None: best = (a, info)
    LOG.append(dict(kind='spell', attempt=f'{len(seeds)} (FAILED, first take kept)', **best[1])); print('SPELL FAILED', text, flush=True); return best[0]

def line_audio(line, spk, gap=None):
    seg = []; gap = LETTER_GAP if gap is None else gap
    pieces = [p for p in re.split(r'(\{[^}]*\})', line) if p.strip()]
    for pi, piece in enumerate(pieces):
        last_piece = pi == len(pieces)-1
        if piece.startswith('{'):
            seg += [spell(piece.strip('{}'), V[spk], gap)]
            if not last_piece: seg.append(P.sil(P.PAUSE['sentence']))
        else:
            cs = P.chunks(piece.strip())
            for ci, (t, p) in enumerate(cs):
                if ci == len(cs)-1 and not last_piece: p = P.PAUSE['sentence']
                seg += [synth_cached(say, t, V[spk]), P.sil(max(0.08, p - 2*P.TRIM_PAD*0.6))]
    return P.norm(np.concatenate(seg), -20)

parts = [P.sil(P.PAUSE['lead']), line_audio(INTRO, 'N'), P.sil(P.PAUSE['after_intro'])]
times = []
for spk, line in LINES:
    t0 = sum(len(x) for x in parts)/SR
    parts += [line_audio(line, spk, gap=0.55 if line.startswith('Yes, of course. {') else None)]   # the repeat is spelled more slowly
    times.append((round(t0, 2), round(sum(len(x) for x in parts)/SR, 2), spk, line)); parts.append(P.sil(P.PAUSE['speaker']))
parts += [P.sil(0.3), line_audio(END, 'N'), P.sil(0.6)]
audio = np.clip(P.norm(np.concatenate(parts), -16), -0.98, 0.98)
OUT = os.environ.get('OUT_DIR', f'{HERE}/out'); os.makedirs(OUT, exist_ok=True)
sf.write(f'{OUT}/L1_listening.wav', audio, SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', f'{OUT}/L1_listening.wav', '-af', 'volume=-1dB', '-ac', '1', '-b:a', '96k',
                '-metadata', 'title=Level 1 L1 Listening', '-metadata',
                'comment=Synthetic voices (Chatterbox TTS, Resemble AI, MIT License; contains an inaudible Perth watermark). Script CC BY-NC-SA 4.0.',
                f'{OUT}/L1_listening.mp3'], check=True)
json.dump(dict(regen=LOG + P.REGEN_LOG, line_times=times), open(f'{OUT}/L1_regen_log.json', 'w'), indent=1, default=str)
print('DONE', round(len(audio)/SR, 1), 's', flush=True)
