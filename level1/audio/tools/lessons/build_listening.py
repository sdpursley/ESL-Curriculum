"""Level 1 listening builder (Lessons 2-4). Chatterbox TTS on CPU, every voice cloned from a Kokoro-82M clip (see refs.py / REFS.md).
Usage:  python build_listening.py path/to/script_LN.py OUT_STEM
script_LN.py defines: LESSON, VOICES {speaker: clip name, see refs.py}, FEMALE {speakers}, INTRO [sentences], LINES [(spk, text, tts_text|None)], END
Every sentence is ONE whole take (no comma splitting, no splicing, no time-stretch). For each sentence several seeds are tried;
a take passes only if Whisper (faster-whisper small.en) hears exactly the script words, no artifact flags (artifacts.py),
no cut-off edge, confident words, a normal pace, no clipping, and the right voice pitch (female > 165 Hz median, male < 150 Hz).
The best passing take (Whisper confidence + pitch movement) is kept. Settings: EXAG 0.72, CFG 0.32. 1.4 s between speakers."""
import os, sys, json, pickle, hashlib, subprocess, importlib.util, numpy as np, soundfile as sf
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', 'tools', 'audio'))   # <repo>/tools/audio: processor.py, artifacts.py, textnorm.py
sys.path[:0] = [HERE, TOOLS]
import processor as P
from artifacts import detect
from metrics import prosody
from canon import canon
SCRIPT, STEM = sys.argv[1], sys.argv[2]
spec = importlib.util.spec_from_file_location('S', SCRIPT); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
EX = float(os.environ.get('EXAG', '0.72')); CF = float(os.environ.get('CFG', '0.32'))
NCAND = int(os.environ.get('NCAND', '3')); MAXT = int(os.environ.get('MAXT', '16'))
PAUSE_SPK = float(os.environ.get('PAUSE_SPK', '1.4')); PAUSE_SAME = 0.75; PAUSE_SENT = 0.55
from refs import ref_path
def ref(spk): return ref_path(S.VOICES[spk])
EXCLUDE = json.loads(os.environ.get('EXCLUDE', '{}'))        # {"sentence": [seed, ...]} takes rejected by listening / whole-file check
SAME = getattr(S, 'SAME', {})                                 # same-sound spellings Whisper may use (e.g. anna -> ana)
from faster_whisper import WhisperModel
ASR = WhisperModel('small.en', device='cpu', compute_type='int8')
def asr(a):
    x = np.concatenate([P.sil(.3), a, P.sil(.3)])
    x16 = np.interp(np.linspace(0, len(x), int(len(x)*16000/P.SR), endpoint=False), np.arange(len(x)), x).astype(np.float32)
    segs, _ = ASR.transcribe(x16, beam_size=5, language='en', word_timestamps=True, condition_on_previous_text=False)
    ws = [(w.word, w.start-.3, w.end-.3, w.probability) for s in segs for w in (s.words or [])]
    return ws
def split_sents(t, minw=3):
    """Sentences; a sentence under 3 words is joined to its neighbor (Chatterbox garbles 1-2 word inputs)."""
    import re
    ss = [s.strip() for s in re.findall(r'[^.!?]+[.!?]+|[^.!?]+$', t) if s.strip()]
    out = []
    for s in ss:
        if out and len(out[-1].split()) < minw: out[-1] += ' ' + s
        else: out.append(s)
    if len(out) > 1 and len(out[-1].split()) < minw:
        last = out.pop(); out[-1] += ' ' + last
    return out
from engine import say
NCACHE = f'{HERE}/cache'; os.makedirs(NCACHE, exist_ok=True)
LOG = []
def take(display, tts, spk):
    """One sentence -> best passing whole take."""
    target = canon(display, SAME); fem = spk in S.FEMALE; tried = []; passing = []
    excl = EXCLUDE.get(display, [])
    for k in range(MAXT):
        seed = 2026 + k*7919
        ck = f"{NCACHE}/{hashlib.md5(repr((tts, ref(spk), EX, CF, seed)).encode()).hexdigest()}.pkl"
        if os.path.exists(ck): raw = pickle.load(open(ck, 'rb'))
        else: raw = say(tts, ref(spk), EX, CF, seed); pickle.dump(raw, open(ck, 'wb'))
        a = P.trim(raw); _, _, edge = P.speech_bounds(raw)
        ws = asr(a); hyp = canon(' '.join(w for w, *_ in ws), SAME); probs = [p for *_, p in ws] or [0]
        flags, met = detect(a, P.SR, tts, (ws[0][1], ws[-1][2]) if ws else None)
        raw_peak = float(np.abs(raw).max())
        # clipping = flat tops (3+ samples in a row at the same peak value) after leveling; Chatterbox output is float,
        # so a raw peak above 1.0 is not clipping by itself (the take is turned down to -20 LUFS)
        lv = P.norm(a, -20); m = np.abs(lv); flat = int(np.max(np.convolve((m >= 0.98).astype(int), np.ones(3, int), 'valid'), initial=0) >= 3)
        if flat or m.max() >= 0.98: flags.append(f'clipping (leveled peak {m.max():.2f})')
        # the same artifact check as the whole-file check (take with 0.15 s of silence each side, no word times)
        fl2, _ = detect(np.concatenate([P.sil(0.15), P.norm(a, -20), P.sil(0.15)]), P.SR, tts, None)
        flags += [f'(context) {f}' for f in fl2 if not f.startswith('too long') and f not in flags]
        pr = prosody(a); f0 = pr.get('f0_med', 0)
        pitch_ok = (f0 >= 165) if fem else (0 < f0 <= 150)
        ok = hyp == target and not edge and not flags and min(probs) >= 0.5 and pitch_ok and seed not in excl
        score = float(np.mean(probs)) + 0.15*min(pr['f0_st_sd'], 4)
        info = dict(spk=spk, text=display, tts_text=tts, seed=seed, hyp=' '.join(hyp), ok=ok, edge=bool(edge), flags=flags,
                    min_prob=round(min(probs), 2), mean_prob=round(float(np.mean(probs)), 2), dur=round(len(a)/P.SR, 2),
                    raw_peak=round(raw_peak, 3), pitch_ok=pitch_ok, score=round(score, 3), **pr)
        print(json.dumps(info, default=str), flush=True); tried.append(info)
        if ok: passing.append((score, a, info))
        if len(passing) >= NCAND: break
    if passing:
        s, a, info = max(passing, key=lambda x: x[0]); LOG.append(dict(chosen=info, tries=len(tried), passing=len(passing)))
    else:
        best = max(tried, key=lambda i: i['score'] - (0 if i['hyp'] == ' '.join(target) else 5)); info = best
        raw = pickle.load(open(f"{NCACHE}/{hashlib.md5(repr((info['tts_text'], ref(spk), EX, CF, info['seed'])).encode()).hexdigest()}.pkl", 'rb'))
        a = P.trim(raw); LOG.append(dict(chosen=info, tries=len(tried), passing=0, FAILED=True)); print('SENTENCE FAILED', display, flush=True)
    return P.norm(a, -20)
def line(spk, text, tts=None):
    ds = split_sents(text); ts = split_sents(tts) if tts else ds
    assert len(ds) == len(ts), (text, tts)
    seg = []
    for i, (d, t) in enumerate(zip(ds, ts)):
        seg.append(take(d, t, spk))
        if i < len(ds)-1: seg.append(P.sil(PAUSE_SENT))
    return np.concatenate(seg)
parts = [P.sil(0.5), line('Narrator', S.INTRO if isinstance(S.INTRO, str) else ' '.join(S.INTRO)), P.sil(1.6)]; times = []; prev = None
for i, L in enumerate(S.LINES):
    spk, text = L[0], L[1]; tts = L[2] if len(L) > 2 else None
    if i: parts.append(P.sil(PAUSE_SAME if spk == prev else PAUSE_SPK))
    t0 = sum(len(x) for x in parts)/P.SR
    parts.append(line(spk, text, tts)); prev = spk
    times.append((round(t0, 2), round(sum(len(x) for x in parts)/P.SR, 2), spk, text))
parts += [P.sil(1.4), line('Narrator', S.END), P.sil(0.6)]
audio = P.norm(np.concatenate(parts), -16)   # -16 LUFS, like Lesson 1
sf.write(STEM + '_prelimit.wav', audio, P.SR)
# a few loud syllables go above full scale after leveling: a look-ahead limiter (ffmpeg alimiter) turns just those peaks down
# to -1 dBFS instead of clipping them
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', STEM + '_prelimit.wav', '-af', 'alimiter=limit=0.89:attack=5:release=60:level=disabled',
                '-ar', str(P.SR), '-c:a', 'pcm_f32le', STEM + '.wav'], check=True)
os.remove(STEM + '_prelimit.wav'); audio, _ = sf.read(STEM + '.wav', dtype='float32')
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-i', STEM + '.wav', '-ac', '1', '-b:a', '96k',
                '-metadata', f'title=Level 1 Lesson {S.LESSON} Listening', '-metadata',
                'comment=Synthetic voices (Chatterbox TTS, Resemble AI, MIT License, cloned from Kokoro-82M clips; contains an inaudible Perth watermark). Script CC BY-NC-SA 4.0.',
                STEM + '.mp3'], check=True)
json.dump(dict(settings=dict(exag=EX, cfg=CF, pause_between_speakers=PAUSE_SPK, pause_same_speaker=PAUSE_SAME, pause_between_sentences=PAUSE_SENT,
                             voices={k: f'refs/{v}.wav' for k, v in S.VOICES.items()}, asr='faster-whisper small.en'),
               sentences=LOG, line_times=times), open(STEM + '_log.json', 'w'), indent=1, default=str)
nf = sum(1 for l in LOG if l.get('FAILED'))
print('DONE', round(len(audio)/P.SR, 1), 's', 'failed sentences:', nf, flush=True)
