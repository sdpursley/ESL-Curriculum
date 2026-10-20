"""Remake (or check) the Level 2 Chatterbox voice reference clips in samples/refs/.
Every clip is plain Kokoro-82M output (Apache 2.0): a synthetic voice, not a recording of a real person.
The committed clips are reproduced sample-for-sample by this script (checked October 2026: same length,
correlation 0.99999+ for all 10 clips with kokoro-onnx 0.6.1, kokoro-v1.0.onnx, voices-v1.0.bin).
Usage (from tools/audio):  python make_refs.py --check   # compare the committed clips with fresh Kokoro output
                           python make_refs.py           # rewrite samples/refs/*.wav
Model files: KOKORO_MODEL / KOKORO_VOICES (default models/kokoro-v1.0.onnx, models/voices-v1.0.bin)."""
import os, sys, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
HERE = os.path.dirname(os.path.abspath(__file__))
TEXT = ("Good morning, everyone. Today we are going to talk about our families, our jobs, "
        "and the places where we live. Please listen carefully.")
SPEED = 0.9
VOICES = {"N": "af_sarah", "Rosa": "af_heart", "Sam": "am_michael", "Ana": "af_bella", "Marco": "am_adam",
          "Kim": "af_nova", "Carlos": "am_eric", "Server": "am_puck", "Receptionist": "af_river", "Agent": "af_kore"}
k = Kokoro(os.environ.get('KOKORO_MODEL', 'models/kokoro-v1.0.onnx'), os.environ.get('KOKORO_VOICES', 'models/voices-v1.0.bin'))
check = '--check' in sys.argv; bad = 0
for name, v in VOICES.items():
    a, sr = k.create(TEXT, voice=v, speed=SPEED, lang='en-us')
    path = os.path.join(HERE, 'samples', 'refs', f'{name}.wav')
    if check:
        ref, _ = sf.read(path, dtype='float32')
        same_len = len(ref) == len(a); c = float(np.corrcoef(a[:len(ref)], ref[:len(a)])[0, 1])
        ok = same_len and c > 0.999; bad += not ok
        print(f'{name:13s} {v:11s} len {len(ref)} vs {len(a)}  corr {c:.6f}  {"OK" if ok else "DIFFERENT"}')
    else:
        sf.write(path, a, sr); print('wrote', path)
sys.exit(1 if bad else 0)
