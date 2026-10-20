"""Chatterbox wrapper: voice = path to a reference clip, or 'DEFAULT' (Chatterbox's built-in voice)."""
import os, sys, copy, numpy as np, torch
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools', 'audio')))   # <repo>/tools/audio (processor.py)
import processor as P
from chatterbox.tts import ChatterboxTTS
torch.set_num_threads(int(os.environ.get('NT', '8')))
_m = ChatterboxTTS.from_pretrained(device='cpu'); _default = copy.deepcopy(_m.conds)
def say(text, voice, exag, cfg, seed):
    torch.manual_seed(seed)
    if voice == 'DEFAULT':
        _m.conds = copy.deepcopy(_default); w = _m.generate(text, exaggeration=exag, cfg_weight=cfg)
    else:
        w = _m.generate(text, audio_prompt_path=voice, exaggeration=exag, cfg_weight=cfg)
    return P.resample(w.squeeze().numpy(), _m.sr)
