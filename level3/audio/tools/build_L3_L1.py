"""Level 3 Lesson 1 listening build. Whole-line Chatterbox takes (no splicing, no time-stretching), several seeds per line;
a take must pass Whisper (exact words), edge and artifact checks; the best passing take (confidence + pitch movement) is kept.
Voices: synthetic Kokoro-82M reference clips only (<repo>/tools/audio/samples/refs/): Elena=Rosa (af_heart), David=Sam (am_michael), Narrator=N (af_sarah).
Plays the conversation ONCE. Out: out/L3_L1_listening.wav/.mp3 + _log.json (out/ and cache/ are not committed).
Run from level3/audio/tools/ with the audio environment (section 5 of MAINTAINING.md); the published file was made with:
  PAUSE_SPK=1.2 MAXT=24 EXCLUDE='{"<line>": [<seed>, ...]}' python build_L3_L1.py
  (EXCLUDE = takes the whole-file check rejected; two takes after the first run. The seed chosen for every line is in ../L3_L1_listening_log.json.)
  LINE_TIMES=out/L3_L1_listening_log.json python check_L3_L1.py out/L3_L1_listening.mp3
then copy out/L3_L1_listening.mp3, out/L3_L1_listening_log.json and the check JSON into level3/audio/.
textnorm.py here = tools/audio/textnorm.py + one fix (Whisper writes "OK" as "okay"); it is found first on the path."""
import os, sys, json, pickle, hashlib, subprocess, numpy as np, soundfile as sf
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools', 'audio'))   # <repo>/tools/audio (processor, artifacts, refs)
sys.path[:0] = [HERE, TOOLS]
import processor as P
from textnorm import words
from artifacts import detect
from metrics import prosody
from engine import say
from script_L3_L1 import INTRO, LINES, END, plain
REF = {'Elena': 'Rosa', 'David': 'Sam', 'Narrator': 'N'}
SET = {'Elena': (0.72, 0.32), 'David': (0.72, 0.32), 'Narrator': (0.55, 0.40)}   # (exaggeration, cfg)
VOICE = {k: f'{TOOLS}/samples/refs/{v}.wav' for k, v in REF.items()}
NCAND = int(os.environ.get('NCAND', '1')); MAXT = int(os.environ.get('MAXT', '12'))
PAUSE_SPK = float(os.environ.get('PAUSE_SPK', '1.4'))   # 1.3-1.5 s between speakers
# pitch gate: female voices (Elena, Narrator) need median F0 >= 165 Hz, male (David) <= 150 Hz
F0_OK = {'Elena': lambda f: f >= 165, 'Narrator': lambda f: f >= 165, 'David': lambda f: f <= 150}
NAMES = {'elena', 'david'}
EXCLUDE = json.loads(os.environ.get('EXCLUDE', '{}'))
CACHE = f'{HERE}/cache'; os.makedirs(CACHE, exist_ok=True)
def asr(a):
    P.chunk_score(a, 'x')
    x = np.concatenate([P.sil(.3), a, P.sil(.3)])
    x16 = np.interp(np.linspace(0, len(x), int(len(x)*16000/P.SR), endpoint=False), np.arange(len(x)), x).astype(np.float32)
    segs, _ = P._asr.transcribe(x16, beam_size=5, language='en', word_timestamps=True, condition_on_previous_text=False)
    return [(t, w.start-.3, w.end-.3, w.probability) for s in segs for w in (s.words or []) for t in words(w.word)]
LOG = []
def line_take(text, spk):
    ex, cf = SET[spk]; target = words(text); passing, tried = [], []
    for k in range(MAXT):
        seed = 2026 + k*7919
        ck = f"{CACHE}/{hashlib.md5(repr((text, VOICE[spk], ex, cf, seed)).encode()).hexdigest()}.pkl"
        if os.path.exists(ck): raw = pickle.load(open(ck, 'rb'))
        else: raw = say(text, VOICE[spk], ex, cf, seed); pickle.dump(raw, open(ck, 'wb'))
        P.a_raw_holder[:] = [raw]; a = P.trim(raw); _, _, edge = P.speech_bounds(raw)
        ws = asr(a); hyp = [w for w, *_ in ws]; probs = [p for *_, p in ws] or [0]
        flags, _ = detect(a, P.SR, text, (ws[0][1], ws[-1][2]) if ws else None)
        flags = [f for f in flags if not f.startswith('too long')]
        pr = prosody(a)
        # names are often heard correctly but with lower Whisper confidence: they need >= 0.25, every other word >= 0.5
        pn = [p for w, *_, p in ws if w not in NAMES] or [0]; pnm = [p for w, *_, p in ws if w in NAMES] or [1]
        ok = hyp == target and not edge and not flags and min(pn) >= 0.5 and min(pnm) >= 0.25 and ('f0_med' in pr and F0_OK[spk](pr['f0_med']))
        score = float(np.mean(probs)) + 0.15*min(pr['f0_st_sd'], 4)
        info = dict(spk=spk, line=text, seed=seed, hyp=' '.join(hyp), ok=ok, edge=bool(edge), flags=flags, min_prob=round(min(probs), 2),
                    mean_prob=round(float(np.mean(probs)), 2), dur=round(len(a)/P.SR, 2), wps=round(len(target)/max(len(a)/P.SR, .1), 2), score=round(score, 3), **pr)
        print(json.dumps(info, default=str), flush=True); tried.append((info, a))
        if ok and seed not in EXCLUDE.get(text, []): passing.append((score, a, info))
        if len(passing) >= NCAND: break
    if passing:
        _, a, info = max(passing, key=lambda x: x[0]); LOG.append(dict(chosen=info, tries=len(tried), passing=len(passing)))
    else:
        info, a = max(tried, key=lambda x: x[0]['score']); LOG.append(dict(chosen=info, tries=len(tried), passing=0, FAILED=True))
        print('LINE FAILED', spk, text, flush=True)
    return P.norm(a, -20)
# the narrator intro is long for one take (Whisper kept dropping 'Lesson one'), so it is made as 3 natural sentence-group takes
INTRO_PARTS = ['Lesson one. Listening.', 'Elena and David are neighbors.', "It's Saturday morning, and they're at the laundromat. Listen."]
assert words(' '.join(INTRO_PARTS)) == words(INTRO)
intro = []
for i, t in enumerate(INTRO_PARTS):
    intro.append(line_take(t, 'Narrator'))
    if i < len(INTRO_PARTS)-1: intro.append(P.sil(0.55))
parts = [P.sil(0.5), P.norm(np.concatenate(intro), -20), P.sil(1.4)]; times = []
for spk, line in LINES:
    t0 = sum(len(x) for x in parts)/P.SR
    parts.append(line_take(plain(line), spk))
    times.append((round(t0, 2), round(sum(len(x) for x in parts)/P.SR, 2), spk, plain(line))); parts.append(P.sil(PAUSE_SPK))
parts += [P.sil(0.6), line_take(END, 'Narrator'), P.sil(0.6)]
audio = np.clip(P.norm(np.concatenate(parts), -16), -0.98, 0.98)
OUT = f'{HERE}/out'; os.makedirs(OUT, exist_ok=True); stem = f'{OUT}/L3_L1_listening'
sf.write(stem + '.wav', audio, P.SR)
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', stem + '.wav', '-af', 'volume=-1dB', '-ac', '1', '-b:a', '96k',
                '-metadata', 'title=Level 3 Lesson 1 Listening: Tell Me More', '-metadata',
                'comment=Synthetic voices (Chatterbox TTS, Resemble AI, MIT License, cloned from Kokoro-82M synthetic references, Apache 2.0; inaudible Perth watermark). Script (c) 2026 the authors, CC BY-NC-SA 4.0.',
                stem + '.mp3'], check=True)
json.dump(dict(settings=dict(refs=REF, exag_cfg=SET, pause_between_lines=PAUSE_SPK), lines=LOG, line_times=times),
          open(stem + '_log.json', 'w'), indent=1, default=str)
print('DONE', round(len(audio)/P.SR, 1), 's', flush=True)
