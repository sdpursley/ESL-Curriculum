"""Natural-voice versions of the L1 listening (Ana + Carlos remade; narrator + receptionist reuse the approved takes).
Each Ana/Carlos line is made as ONE whole take (no comma splitting, no letter splicing, no time-stretching).
For every line, several seeds are tried; takes must pass Whisper (exact words) + artifact checks; the passing take
with the best score (confidence + pitch movement) is kept.
Env: VER=A|B|final  ANA=<ref name or DEFAULT>  CARLOS=<ref name>  EXAG  CFG  NCAND (passing takes wanted)  MAXT (max tries)
The published file (October 2026), from level1/audio/tools/natural/ with the audio environment (section 5 of MAINTAINING.md):
  1. ../build_L1_audio.py must have run once (its cache/ holds the narrator + receptionist takes), and fetch_ana_ref.py once.
  2. VER=final ANA=Ana_LTTSR1580 CARLOS=Sam EXAG=0.72 CFG=0.32 MAXT_SPELL=36 RUIZ_VARIANTS='["R, U, I, Zee.", "R, U, I, Z."]' \
     EXCLUDE='{"Thank you. Goodbye!": [17864]}' python build_natural.py      # -> out/L1_listening_final.wav/.mp3 + _log.json
  3. cd .. && LINE_TIMES=natural/out/L1_listening_final_log.json python check_L1.py natural/out/L1_listening_final.mp3
"Zee" and "Vee" are only what the voice is given (they come out as clear letters); the written script stays Z and V."""
import os, sys, json, pickle, hashlib, subprocess, re, numpy as np, soundfile as sf
HERE = os.path.dirname(os.path.abspath(__file__)); L1T = os.path.dirname(HERE)          # level1/audio/tools (script_L1.py, cache/)
TOOLS = os.path.abspath(os.path.join(L1T, '..', '..', '..', 'tools', 'audio'))            # <repo>/tools/audio (processor, textnorm, artifacts, refs)
sys.path[:0] = [HERE, L1T, TOOLS]
import processor as P
from textnorm import words
from artifacts import detect
from script_L1 import INTRO, LINES, END, plain
from metrics import prosody
VER = os.environ['VER']; EX = float(os.environ['EXAG']); CF = float(os.environ['CFG'])
NCAND = int(os.environ.get('NCAND', '3')); MAXT = int(os.environ.get('MAXT', '14')); MAXT_SPELL = int(os.environ.get('MAXT_SPELL', '24'))
REFS = f'{TOOLS}/samples/refs'
def ref(n):   # 'DEFAULT', a path to a .wav, a clip in natural/refs/ (Ana_LTTSR1580, from fetch_ana_ref.py), or a name in tools/audio/samples/refs/
    if n == 'DEFAULT' or n.endswith('.wav'): return n
    return f'{HERE}/refs/{n}.wav' if os.path.exists(f'{HERE}/refs/{n}.wav') else f'{REFS}/{n}.wav'
VOICE = {'Ana': ref(os.environ['ANA']), 'Carlos': ref(os.environ['CARLOS'])}
PAUSE_SPK = float(os.environ.get('PAUSE_SPK', '1.3'))      # silence between speakers (longer pauses BETWEEN lines)
REC_PAUSE = dict(comma=0.30, sentence=0.45)                # receptionist/narrator joins (approved takes, tighter joins)
# what the TTS is given (written script stays the same)
# ("..." made Chatterbox repeat letters, so only commas are used)
TTS_TEXT = {'V, E, G, A.': ['Vee, E, G, A.'], 'R, U, I, Z.': json.loads(os.environ.get('RUIZ_VARIANTS', '["R, U, I, Z."]'))}
def quiet_gaps(a, L, thr=-35):
    """Natural silence between spelled letters: longest run of 10 ms frames below thr dB (re peak) between letter midpoints."""
    f = int(0.01*P.SR); n = len(a)//f
    db = 20*np.log10(np.sqrt((a[:n*f].reshape(n, f)**2).mean(1)) + 1e-9); q = (db - db.max()) < thr
    out = []
    for x, y in zip(L, L[1:]):
        lo, hi = int(max(0, (x[1]+x[2])/2)/0.01), int(min(n*0.01, (y[1]+y[2])/2)/0.01)
        best = run = 0
        for v in q[lo:hi]: run = run+1 if v else 0; best = max(best, run)
        out.append(round(best*0.01, 2))
    return out
LETTERS = {'vee': 'v', 'bee': 'b', 'ee': 'e', 'gee': 'g', 'ay': 'a', 'eye': 'i', 'zee': 'z', 'are': 'r', 'you': 'u'}   # only for spelled lines
SAME = {'anna': 'ana'}   # same sound, different spelling
# ---------- approved narrator/receptionist takes from the original build cache ----------
CACHE = f'{L1T}/cache'   # filled by build_L1_audio.py (approved narrator + receptionist takes)
def old_chunk(text, voice):
    k = f"{CACHE}/{hashlib.md5(repr(('chunk', text, voice, '2026', '0.55', '0.45')).encode()).hexdigest()}.pkl"
    return pickle.load(open(k, 'rb'))
P.MIN_WORDS = 3; P.PAUSE.update(comma=0.50, sentence=0.80)
def old_line(text, spk):
    seg = []; cs = P.chunks(text)
    for i, (t, p) in enumerate(cs):
        seg.append(old_chunk(t, f'{REFS}/{spk}.wav'))
        if i < len(cs)-1: seg.append(P.sil(REC_PAUSE['comma'] if t.endswith(',') else REC_PAUSE['sentence']))
    return P.norm(np.concatenate(seg), -20)
# ---------- new whole-line takes ----------
from engine import say
def asr(a, spelled=False):
    P.chunk_score(a, 'x')
    x = np.concatenate([P.sil(.3), a, P.sil(.3)])
    x16 = np.interp(np.linspace(0, len(x), int(len(x)*16000/P.SR), endpoint=False), np.arange(len(x)), x).astype(np.float32)
    segs, _ = P._asr.transcribe(x16, beam_size=5, language='en', word_timestamps=True, condition_on_previous_text=False)
    M = {**SAME, **(LETTERS if spelled else {})}
    return [(M.get(t, t), w.start-.3, w.end-.3, w.probability) for s in segs for w in (s.words or []) for t in words(w.word)]
NCACHE = f'{HERE}/cache'; os.makedirs(NCACHE, exist_ok=True)
LOG = []
def new_line(line, spk, exclude=()):
    target = words(plain(line)); spelled = '{' in line
    exclude = list(exclude) + json.loads(os.environ.get('EXCLUDE', '{}')).get(plain(line), [])   # takes rejected by the whole-file check
    variants = TTS_TEXT.get(plain(line), [plain(line)])
    passing, tried = [], []
    for k in range(MAXT_SPELL if spelled else MAXT):
        t = variants[k % len(variants)]; seed = 2026 + k*7919
        ck = f"{NCACHE}/{hashlib.md5(repr((t, VOICE[spk], EX, CF, seed)).encode()).hexdigest()}.pkl"
        if os.path.exists(ck): raw = pickle.load(open(ck, 'rb'))
        else: raw = say(t, VOICE[spk], EX, CF, seed); pickle.dump(raw, open(ck, 'wb'))
        P.a_raw_holder[:] = [raw]; a = P.trim(raw); _, _, edge = P.speech_bounds(raw)
        ws = asr(a, spelled); hyp = [w for w, *_ in ws]; probs = [p for *_, p in ws] or [0]
        flags, _ = detect(a, P.SR, t, (ws[0][1], ws[-1][2]) if ws else None)
        flags = [f for f in flags if not f.startswith('too long')]
        # spelled letters: need a clear (>= 0.12 s) natural break between letters
        letter_gaps = []
        if spelled:
            L = [w for w in ws if len(w[0]) == 1]
            letter_gaps = quiet_gaps(a, L)
        pr = prosody(a)
        ok = hyp == target and not edge and not flags and min(probs) >= (0.3 if spelled else 0.5) and (not spelled or min(letter_gaps or [0]) >= 0.08)
        score = float(np.mean(probs)) + 0.15*min(pr['f0_st_sd'], 4) + (1.5*min(min(letter_gaps or [0]), 0.35) if spelled else 0)
        info = dict(spk=spk, line=plain(line), tts_text=t, seed=seed, hyp=' '.join(hyp), ok=ok, edge=bool(edge), flags=flags,
                    min_prob=round(min(probs), 2), mean_prob=round(float(np.mean(probs)), 2), letter_gaps=letter_gaps, dur=round(len(a)/P.SR, 2),
                    score=round(score, 3), **pr)
        print(json.dumps(info, default=str), flush=True); tried.append(info)
        if ok and seed not in exclude: passing.append((score, a, info))
        if len(passing) >= NCAND: break
    if passing:
        s, a, info = max(passing, key=lambda x: x[0]); LOG.append(dict(chosen=info, tries=len(tried), passing=len(passing)))
    else:
        b = max(range(len(tried)), key=lambda i: tried[i]['score']); info = tried[b]
        raw = pickle.load(open(f"{NCACHE}/{hashlib.md5(repr((info['tts_text'], VOICE[spk], EX, CF, info['seed'])).encode()).hexdigest()}.pkl", 'rb'))
        a = P.trim(raw); LOG.append(dict(chosen=info, tries=len(tried), passing=0, FAILED=True)); print('LINE FAILED', line, flush=True)
    return P.norm(a, -20)
parts = [P.sil(0.5), old_line(INTRO, 'N'), P.sil(1.6)]; times = []
for spk, line in LINES:
    t0 = sum(len(x) for x in parts)/P.SR
    m = re.match(r'^(.*\S)\s+(\{.*\})$', line)
    if spk in VOICE and m:
        # "Yes, of course. {V, E, G, A.}": the sentence and the spelling are two natural takes joined at the sentence break,
        # and the spelling is a DIFFERENT good take from the first time (an exact copy would sound mechanical)
        first = new_line(m.group(1), spk)
        used = [l['chosen']['seed'] for l in LOG if l['chosen']['line'] == plain(m.group(2))]
        parts.append(P.norm(np.concatenate([first, P.sil(0.45), new_line(m.group(2), spk, exclude=used)]), -20))
    else:
        parts.append(new_line(line, spk) if spk in VOICE else old_line(plain(line), spk))
    times.append((round(t0, 2), round(sum(len(x) for x in parts)/P.SR, 2), spk, line)); parts.append(P.sil(PAUSE_SPK))
parts += [P.sil(0.3), old_line(END, 'N'), P.sil(0.6)]
audio = np.clip(P.norm(np.concatenate(parts), -16), -0.98, 0.98)
OUT = f'{HERE}/out'; os.makedirs(OUT, exist_ok=True); stem = f'{OUT}/L1_listening_final' if VER == 'final' else f'{OUT}/L1_listening_option{VER}'
sf.write(stem + '.wav', audio, P.SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', stem + '.wav', '-af', 'volume=-1dB', '-ac', '1', '-b:a', '96k',
                '-metadata', f'title=Level 1 L1 Listening (option {VER})', '-metadata',
                'comment=Synthetic voices (Chatterbox TTS, Resemble AI, MIT License; contains an inaudible Perth watermark). Script CC BY-NC-SA 4.0.',
                stem + '.mp3'], check=True)
json.dump(dict(settings=dict(ver=VER, ana=os.environ['ANA'], carlos=os.environ['CARLOS'], exag=EX, cfg=CF, pause_between_lines=PAUSE_SPK),
               lines=LOG, line_times=times), open(stem + '_log.json', 'w'), indent=1, default=str)
print('DONE', VER, round(len(audio)/P.SR, 1), 's', flush=True)
