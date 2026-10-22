"""Chatterbox wrapper. voice = path to a Kokoro-made reference clip in refs/. There is no default-voice option on purpose.
Device: TTS_DEVICE=auto (default: cuda if available, else mps on Apple Silicon, else cpu) or cuda / mps / cpu.
The same seed gives a different take on a different device, so seeds in a log made on one machine do not carry over to another."""
import os, sys, numpy as np, torch
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', 'tools', 'audio'))]   # <repo>/tools/audio/processor.py
import processor as P
from chatterbox.tts import ChatterboxTTS
def _device():
    d = os.environ.get('TTS_DEVICE', 'auto')
    if d != 'auto': return d
    if torch.cuda.is_available(): return 'cuda'
    if getattr(torch.backends, 'mps', None) is not None and torch.backends.mps.is_available(): return 'mps'
    return 'cpu'
DEVICE = _device()
torch.set_num_threads(int(os.environ.get('NT', str(min(8, os.cpu_count() or 4)))))
_m = ChatterboxTTS.from_pretrained(device=DEVICE)
print(f'[engine] Chatterbox on {DEVICE}', file=sys.stderr)
def say(text, voice, exag, cfg, seed):
    assert os.path.exists(voice) and '/refs/' in voice.replace(os.sep, '/'), voice   # only the Kokoro-made clips in refs/
    torch.manual_seed(seed)
    w = _m.generate(text, audio_prompt_path=voice, exaggeration=exag, cfg_weight=cfg)
    return P.resample(w.squeeze().detach().cpu().numpy(), _m.sr)
