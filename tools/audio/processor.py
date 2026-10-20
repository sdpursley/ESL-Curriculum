"""Engine-agnostic listening-audio builder: clause-level synthesis + controlled pauses + loudness normalization.
Usage: python processor.py ENGINE [L1 L2 ...]   (ENGINE = chatterbox | kokoro)
chatterbox: the published voices, cloned only from the synthetic Kokoro-made clips in samples/refs/ (see make_refs.py).
kokoro: plain Kokoro-82M voices (Apache 2.0), used for early drafts.
No engine or voice trained on recordings of real people is supported here (no Piper/LibriTTS voices,
no Chatterbox built-in default voice).
Outputs samples/<ENGINE>_<L>.mp3 (never touches the original L*_listening.mp3)."""
import re, sys, os, subprocess, numpy as np, soundfile as sf, pyloudnorm as pyln
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scripts import LESSONS
from scripts_v5 import LESSONS as _L5
LESSONS = {**LESSONS, **_L5}
SINGLE = os.environ.get('SINGLE', '0') == '1'   # conversation plays once (no 'Listen again')
SR = 24000
PAUSE = dict(comma=0.40, sentence=0.65, speaker=0.95, after_intro=1.5, between_plays=3.0, lead=0.5)
SPEED = 0.9
MIN_WORDS = 1
ENGINE_VOICES = {
 "kokoro": {"N":"af_sarah","Rosa":"af_heart","Sam":"am_michael","Ana":"af_bella","Marco":"am_adam","Kim":"af_nova","Carlos":"am_eric","Server":"am_puck","Receptionist":"af_river","Agent":"af_kore"},
 "chatterbox": {},   # filled in __main__ with samples/refs/<character>.wav (Kokoro-made clips of the voices above)
}

def chunks(line):
    """Split into (text, pause_after) by sentence then comma."""
    out = []
    for s in re.findall(r'[^.!?]+[.!?]*', line):
        s = s.strip()
        if not s: continue
        parts = [p.strip() for p in re.split(r'(?<=,)\s+', s) if p.strip()]
        for i, p in enumerate(parts):
            out.append((p, PAUSE['comma'] if i < len(parts)-1 else PAUSE['sentence']))
    if out: out[-1] = (out[-1][0], 0.0)
    if MIN_WORDS > 1:   # merge very short chunks (Chatterbox garbles 1-2 word inputs)
        m = []
        for t, p in out:
            if m and len(m[-1][0].split()) < MIN_WORDS: m[-1] = (m[-1][0] + " " + t, p)
            else: m.append((t, p))
        if len(m) > 1 and len(m[-1][0].split()) < MIN_WORDS: t, p = m.pop(); m[-1] = (m[-1][0] + " " + t, p)
        out = m
    return out

TRIM_PAD = 0.10     # keep 100 ms around detected speech (protects wh-, h-, f-, s- onsets & final consonants)
def speech_bounds(a, rel_db=-50):
    """10 ms frame RMS; speech = frames within rel_db of the loudest frame (gentle: -50 dB)."""
    f = int(0.01*SR); n = len(a)//f
    if n == 0: return 0, len(a), False
    rms = np.sqrt((a[:n*f].reshape(n, f)**2).mean(1) + 1e-12); db = 20*np.log10(rms)
    on = np.where(db > db.max() + rel_db)[0]
    if len(on) == 0: return 0, len(a), False
    edge = on[0] <= 1 or on[-1] >= n-2      # speech touching the raw buffer edge => engine itself cut a word
    return on[0]*f, (on[-1]+1)*f, edge
def trim(a, pad=TRIM_PAD):
    s, e, _ = speech_bounds(a)
    s, e = max(0, s-int(pad*SR)), min(len(a), e+int(pad*SR))
    a = a[s:e].copy(); fd = int(0.01*SR)
    a[:fd] *= np.linspace(0,1,fd); a[-fd:] *= np.linspace(1,0,fd)   # 10 ms fades, no hard cut
    return a

def resample(a, sr):
    if sr == SR: return a.astype(np.float32)
    x = np.linspace(0, len(a), int(len(a)*SR/sr), endpoint=False)
    return np.interp(x, np.arange(len(a)), a).astype(np.float32)

def make_engine(name):
    if name == "kokoro":
        from kokoro_onnx import Kokoro
        k = Kokoro(os.environ.get('KOKORO_MODEL', 'models/kokoro-v1.0.onnx'), os.environ.get('KOKORO_VOICES', 'models/voices-v1.0.bin'))
        return lambda t, v: resample(*k.create(t, voice=v, speed=SPEED, lang='en-us'))
    if name == "chatterbox":
        import torch; from chatterbox.tts import ChatterboxTTS
        torch.set_num_threads(int(os.environ.get('NT','8'))); m = ChatterboxTTS.from_pretrained(device="cpu")
        # Chatterbox voices come from short reference clips (made with Kokoro; Apache-2.0) in samples/refs/.
        # Always pass a reference clip: without one Chatterbox falls back to its built-in default voice (not allowed).
        def say(t, v):
            if not v or not os.path.isfile(v): raise ValueError(f"Chatterbox needs a Kokoro-made reference clip, got {v!r}")
            return _gen(t, v)
        _gen = lambda t, v: resample(m.generate(t, audio_prompt_path=v, exaggeration=float(os.environ.get('EXAG','0.55')), cfg_weight=float(os.environ.get('CFG','0.45'))).squeeze().numpy(), m.sr)
        return say

CHECK = os.environ.get('CLIP_CHECK', '1') == '1'
REGEN_LOG = []
_asr = None
def chunk_score(a, text):
    """Return (ok, info). ASR the chunk (with silence guard) and verify first/last words are present & confident."""
    global _asr
    from textnorm import words; import difflib
    if _asr is None:
        from faster_whisper import WhisperModel
        _asr = WhisperModel("small.en", device="cpu", compute_type="int8")
    pad = np.zeros(int(0.3*SR), np.float32)
    x = np.concatenate([pad, a, pad])
    x16 = np.interp(np.linspace(0, len(x), int(len(x)*16000/SR), endpoint=False), np.arange(len(x)), x).astype(np.float32)
    segs, _ = _asr.transcribe(x16, beam_size=5, language="en", word_timestamps=True, condition_on_previous_text=False)
    ws = [w for s_ in segs for w in (s_.words or [])]
    hyp = words(" ".join(w.word for w in ws)); ref = words(text)
    sim = difflib.SequenceMatcher(None, ref, hyp).ratio() if ref else 1
    first_ok = bool(hyp) and hyp[0] == ref[0]; last_ok = bool(hyp) and hyp[-1] == ref[-1]
    probs = (ws[0].probability, ws[-1].probability) if ws else (0, 0)
    _, _, edge = speech_bounds(a_raw_holder[0]) if a_raw_holder else (0, 0, False)
    from artifacts import detect
    wt = (ws[0].start*16000/16000 - 0.3, ws[-1].end - 0.3) if ws else None
    flags, met = detect(a, SR, text, wt)
    if len(hyp) > len(ref): flags.append(f"extra words: {' '.join(hyp)}")
    ok = first_ok and last_ok and sim >= 0.85 and min(probs) >= 0.35 and not edge and not flags
    return ok, dict(text=text, hyp=" ".join(hyp), sim=round(sim, 2), probs=[round(p, 2) for p in probs], edge=bool(edge),
                    flags=flags, score=sim + 0.5*(first_ok+last_ok) + 0.3*min(probs) - (0.5 if edge else 0) - 0.6*len(flags))
a_raw_holder = []
def synth_checked(say, text, voice, tries=int(os.environ.get('TRIES', '4'))):
    best = None
    for k in range(tries):
        try:
            import torch; torch.manual_seed(int(os.environ.get('SEED0','1000')) + k*7919)
        except ImportError: pass
        raw = say(text, voice); a_raw_holder[:] = [raw]; a = trim(raw)
        if not CHECK: return a
        ok, info = chunk_score(a, text)
        if k == 0 and not ok: info['first_take_flagged'] = True
        if k == 0: best_first = {kk: info[kk] for kk in ('hyp','flags','probs','sim')}
        if best is None or info['score'] > best[1]['score']: best = (a, info)
        if ok:
            if k: REGEN_LOG.append(dict(attempt=k+1, why_first_failed=best_first, **info))
            return a
    REGEN_LOG.append(dict(attempt=f"{tries} (best kept, still flagged)", why_first_failed=best_first, **best[1]))
    return best[0]

meter = pyln.Meter(SR)
def norm(a, target):
    if len(a) < SR*0.5: a2 = np.concatenate([a, a, a])
    else: a2 = a
    l = meter.integrated_loudness(a2)
    return (a * 10**((target - l)/20)).astype(np.float32) if np.isfinite(l) else a

def sil(s): return np.zeros(int(s*SR), np.float32)

def build(engine, key, say, voices):
    def line_audio(text, spk):
        seg = []
        for t, p in chunks(text):
            seg += [synth_checked(say, t, voices[spk]), sil(max(0.08, p - 2*TRIM_PAD*0.6))]
        return norm(np.concatenate(seg), -20)   # per-line leveling -> consistent voices
    intro, lines = LESSONS[key]
    dlg = []
    for i, (spk, line) in enumerate(lines):
        dlg += [line_audio(line, spk), sil(PAUSE['speaker'])]
    parts = [sil(PAUSE['lead']), line_audio(intro, 'N'), sil(PAUSE['after_intro'])] + dlg
    if not SINGLE: parts += [sil(PAUSE['between_plays']), line_audio("Listen again.", 'N'), sil(1.2)] + dlg
    parts += [sil(1.2), line_audio("That's the end of the listening.", 'N'), sil(0.6)]
    audio = norm(np.concatenate(parts), -16)          # final: -16 LUFS (spoken-word web standard)
    audio = np.clip(audio, -0.98, 0.98)
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'samples'); wav = f'{d}/{engine}_{key}.wav'
    sf.write(wav, audio, SR)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',wav,'-ac','1','-b:a','96k','-metadata',f'title=Level 2 {key} Listening ({engine})',f'{d}/{engine}_{key}.mp3'], check=True)
    # 25 s excerpt from the start of the first dialogue play
    start = (PAUSE['lead'] + len(parts[1])/SR + PAUSE['after_intro']) - 0.3
    subprocess.run(['ffmpeg','-y','-loglevel','error','-ss',f'{start:.2f}','-t','25','-i',wav,'-af','afade=t=out:st=24:d=1','-ac','1','-b:a','96k',f'{d}/{engine}_{key}_excerpt25s.mp3'], check=True)
    print(engine, key, round(len(audio)/SR,1), 's ->', wav)
    import json; json.dump(REGEN_LOG, open(f'{d}/{engine}_{key}_regen_log.json','w'), indent=1, default=str)
    print('regenerated/flagged chunks:', json.dumps(REGEN_LOG, indent=1, default=str)); REGEN_LOG.clear()

if __name__ == "__main__":
    global_ = None
    eng = sys.argv[1]
    if eng not in ENGINE_VOICES: sys.exit(f"unknown engine {eng!r}: use chatterbox or kokoro")
    voices = ENGINE_VOICES[eng]; keys = sys.argv[2:] or list(LESSONS)
    if eng == "chatterbox":
        globals()["MIN_WORDS"] = 3
        d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'samples', 'refs')
        voices = {k: f'{d}/{k}.wav' for k in ENGINE_VOICES['kokoro']}
    say = make_engine(eng)
    for k in keys: build(eng, k, say, voices)
