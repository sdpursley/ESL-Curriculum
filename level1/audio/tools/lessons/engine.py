"""Chatterbox wrapper (CPU). voice = path to a Kokoro-made reference clip (refs.py). There is no default-voice option on purpose."""
import os, sys, numpy as np, torch
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', 'tools', 'audio'))   # <repo>/tools/audio: processor.py, artifacts.py, textnorm.py
sys.path[:0] = [HERE, TOOLS]
import processor as P
from refs import allowed
from chatterbox.tts import ChatterboxTTS
torch.set_num_threads(int(os.environ.get('NT', '8')))
_m = ChatterboxTTS.from_pretrained(device='cpu')
def say(text, voice, exag, cfg, seed):
    assert allowed(voice), f'not a Kokoro reference clip: {voice}'
    torch.manual_seed(seed)
    w = _m.generate(text, audio_prompt_path=voice, exaggeration=exag, cfg_weight=cfg)
    return P.resample(w.squeeze().numpy(), _m.sr)
