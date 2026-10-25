"""Make the Level 3 voice reference clips in refs/ (not committed: *.wav is in .gitignore) from their Kokoro-82M voice ids.
Every clip is plain Kokoro-82M output (hexgrad, Apache 2.0): a synthetic voice, not a recording of a person. Chatterbox clones the
voice from the clip. Never put any other file in refs/ (no recordings of real people, no LibriTTS/LibriVox, no Piper, and never
Chatterbox's built-in default voice); engine.py only accepts a file inside refs/.

The recipes are the ones that made the committed clips the Level 3 Lesson 4 and 5 audio was built from:
  - 9 clips: tools/audio/make_refs.py (one fixed text, speed 0.9)  -> same as tools/audio/samples/refs/<name>.wav
  - Ana_af_jessica: level1/audio/tools/natural/make_ana_ref.py     -> same as level1/audio/tools/natural/kokoro_refs/af_jessica.wav
  - Ana_af_bella = the Level 2 "Ana" clip (af_bella, recipe 1)

Usage (from the repository root, with the audio venv):
  python level3/drafts/audio/tools/make_refs_L3.py            # write refs/*.wav from the voice ids
  python level3/drafts/audio/tools/make_refs_L3.py --check    # also compare each new clip with the committed repo clip
  python level3/drafts/audio/tools/make_refs_L3.py --copy     # no Kokoro needed: copy the committed repo clips (byte-identical)
Engine: kokoro-onnx 0.6.1 (pip install kokoro-onnx==0.6.1) with kokoro-v1.0.onnx + voices-v1.0.bin from
https://github.com/thewh1teagle/kokoro-onnx/releases (default folder <repo>/tools/audio/models/, not committed; or set
KOKORO_MODEL / KOKORO_VOICES). This reproduces the committed clips (correlation 0.9999+). If kokoro-onnx is not installed, the
PyTorch package `kokoro` (pip install kokoro, KPipeline) is used instead; it is the same Kokoro-82M model and voices, but its output is
not sample-identical, so --check will report DIFFERENT (the clips are still valid synthetic references)."""
import os, sys, shutil, numpy as np, soundfile as sf
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
OUT = os.environ.get('L3_REFS', f'{HERE}/refs'); SR = 24000
TEXT = ("Good morning, everyone. Today we are going to talk about our families, our jobs, "
        "and the places where we live. Please listen carefully.")
ANA_TEXT = ["Oh, hi! It's so nice to see you again.", "How was your weekend?", "Mine was really good, thanks.",
            "I went to the park with my sister, and we had lunch by the lake.", "Then it started to rain, so we ran all the way home!",
            "Next time, you should come with us."]
# clip name in refs/ -> (Kokoro voice id, recipe, committed copy in the repo)
CLIPS = {
    'N':              ('af_sarah',   'fixed', 'tools/audio/samples/refs/N.wav'),
    'Rosa':           ('af_heart',   'fixed', 'tools/audio/samples/refs/Rosa.wav'),
    'Sam':            ('am_michael', 'fixed', 'tools/audio/samples/refs/Sam.wav'),
    'Ana_af_bella':   ('af_bella',   'fixed', 'tools/audio/samples/refs/Ana.wav'),
    'Ana_af_jessica': ('af_jessica', 'ana',   'level1/audio/tools/natural/kokoro_refs/af_jessica.wav'),
    'Kim':            ('af_nova',    'fixed', 'tools/audio/samples/refs/Kim.wav'),
    'Receptionist':   ('af_river',   'fixed', 'tools/audio/samples/refs/Receptionist.wav'),
    'Marco':          ('am_adam',    'fixed', 'tools/audio/samples/refs/Marco.wav'),
    'Server':         ('am_puck',    'fixed', 'tools/audio/samples/refs/Server.wav'),
    'Carlos':         ('am_eric',    'fixed', 'tools/audio/samples/refs/Carlos.wav'),
}
os.makedirs(OUT, exist_ok=True)
if '--copy' in sys.argv:
    for name, (_, _, rel) in CLIPS.items():
        shutil.copyfile(f'{REPO}/{rel}', f'{OUT}/{name}.wav'); print('copied', rel, '->', f'{OUT}/{name}.wav')
    sys.exit(0)

try:
    from kokoro_onnx import Kokoro
    M = os.path.join(REPO, 'tools', 'audio', 'models')
    _k = Kokoro(os.environ.get('KOKORO_MODEL', f'{M}/kokoro-v1.0.onnx'), os.environ.get('KOKORO_VOICES', f'{M}/voices-v1.0.bin'))
    ENGINE = 'kokoro-onnx'
    def tts(text, voice, speed):
        a, sr = _k.create(text, voice=voice, speed=speed, lang='en-us'); assert sr == SR; return a.astype(np.float32)
except ImportError:
    from kokoro import KPipeline   # PyTorch Kokoro-82M (hexgrad); downloads the model from Hugging Face on first use
    _p = KPipeline(lang_code='a'); ENGINE = 'kokoro (PyTorch)'
    print('kokoro-onnx not installed: using the PyTorch kokoro package (valid clips, but not sample-identical to the committed ones)')
    def tts(text, voice, speed):
        return np.concatenate([np.asarray(r.audio if hasattr(r, 'audio') else r[2], dtype=np.float32) for r in _p(text, voice=voice, speed=speed)])

def make(voice, recipe):
    if recipe == 'fixed': return tts(TEXT, voice, 0.9)
    parts = []   # make_ana_ref.py: one sentence at a time, short pauses, 0.15 s lead, 0.2 s tail, peak 0.9
    for s in ANA_TEXT:
        parts += [tts(s, voice, 1.0), np.zeros(int((0.45 if s.endswith(('?', '!')) else 0.35)*SR), np.float32)]
    a = np.concatenate([np.zeros(int(0.15*SR), np.float32)] + parts[:-1] + [np.zeros(int(0.2*SR), np.float32)])
    return (a/np.abs(a).max()*0.9).astype(np.float32)

check = '--check' in sys.argv; bad = 0
for name, (voice, recipe, rel) in CLIPS.items():
    a = make(voice, recipe); path = f'{OUT}/{name}.wav'; sf.write(path, a, SR)
    line = f'{name:15s} {voice:11s} {len(a)/SR:5.1f} s  -> {path}'
    if check:
        ref, _ = sf.read(f'{REPO}/{rel}', dtype='float32'); n = min(len(ref), len(a))
        c = float(np.corrcoef(a[:n], ref[:n])[0, 1]); ok = len(ref) == len(a) and c > 0.999; bad += not ok
        line += f'  vs {rel}: len {len(ref)} vs {len(a)} corr {c:.6f} {"OK" if ok else "DIFFERENT"}'
    print(line)
print(f'{ENGINE}: {len(CLIPS)} clips in {OUT}' + (f', {bad} different from the committed clips' if check else ''))
sys.exit(1 if bad else 0)
