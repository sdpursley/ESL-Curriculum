"""Make Ana's voice reference clip, kokoro_refs/af_jessica.wav, with Kokoro-82M (hexgrad, Apache 2.0).
The clip is synthetic: the Kokoro voice af_jessica reads a short original text written for this project. No human recording is used.
Chatterbox (build_natural.py, ANA=af_jessica) copies Ana's voice from this clip. The WAV is committed (16 s, about 0.75 MB),
so you only need this script to remake it.
Needs kokoro-onnx (pip install kokoro-onnx==0.6.1) and the model files kokoro-v1.0.onnx + voices-v1.0.bin
(https://github.com/thewh1teagle/kokoro-onnx/releases), by default in <repo>/tools/audio/models/ (not committed).
Run:  python make_ana_ref.py        (or set KOKORO_MODEL / KOKORO_VOICES to the model files)"""
import os, json, hashlib, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
HERE = os.path.dirname(os.path.abspath(__file__))
MODELS = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', 'tools', 'audio', 'models'))
k = Kokoro(os.environ.get('KOKORO_MODEL', f'{MODELS}/kokoro-v1.0.onnx'), os.environ.get('KOKORO_VOICES', f'{MODELS}/voices-v1.0.bin'))
VOICE, SPEED, SR = 'af_jessica', 1.0, 24000
TEXT = ["Oh, hi! It's so nice to see you again.", "How was your weekend?", "Mine was really good, thanks.",
        "I went to the park with my sister, and we had lunch by the lake.", "Then it started to rain, so we ran all the way home!",
        "Next time, you should come with us."]
parts = []
for s in TEXT:   # one sentence at a time, with short natural pauses
    a, sr = k.create(s, voice=VOICE, speed=SPEED, lang='en-us'); assert sr == SR
    parts += [a.astype(np.float32), np.zeros(int((0.45 if s.endswith(('?', '!')) else 0.35)*SR), np.float32)]
a = np.concatenate([np.zeros(int(0.15*SR), np.float32)] + parts[:-1] + [np.zeros(int(0.2*SR), np.float32)])
a = (a/np.abs(a).max()*0.9).astype(np.float32)
os.makedirs(f'{HERE}/kokoro_refs', exist_ok=True); out = f'{HERE}/kokoro_refs/{VOICE}.wav'; sf.write(out, a, SR)
meta = dict(name=VOICE, file=f'kokoro_refs/{VOICE}.wav', kokoro_voice=VOICE, speed=SPEED, dur=round(len(a)/SR, 1), text=' '.join(TEXT),
            source='Kokoro-82M (hexgrad, https://huggingface.co/hexgrad/Kokoro-82M) via kokoro-onnx 0.6.1, model kokoro-v1.0.onnx + voices-v1.0.bin; synthetic voice, no human recording',
            license='Apache-2.0', sha256=hashlib.sha256(open(out, 'rb').read()).hexdigest())
json.dump(meta, open(f'{HERE}/ana_ref.json', 'w'), indent=1); print(out, meta['dur'], 's', meta['sha256'])
