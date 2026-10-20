"""Re-record only the bad chunks (new seeds), keep the first take that passes the chunk checks AND an exact isolated ASR match.
Stores the take in the build cache under the normal key, so build_L1_audio.py reuses it."""
import os, sys, hashlib, pickle, json, numpy as np, torch
TOOLS = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'tools', 'audio'))
sys.path.insert(0, TOOLS); import processor as P
from textnorm import words
P.MIN_WORDS = 3
HERE = os.path.dirname(os.path.abspath(__file__)); refs = f'{TOOLS}/samples/refs'
CACHE = f'{HERE}/cache'
def ckey(*a): return f"{CACHE}/{hashlib.md5(repr(a).encode()).hexdigest()}.pkl"
say = P.make_engine('chatterbox'); log = []
JOBS = [(a, b) for a, b in json.loads(os.environ['JOBS'])]
for spk, text in JOBS:
    v = f'{refs}/{spk}.wav'; k = ckey('chunk', text, v, os.environ.get('SEED0'), os.environ.get('EXAG'), os.environ.get('CFG'))
    done = False
    for i in range(14):
        seed = 7100 + i*7919; torch.manual_seed(seed)
        raw = say(text, v); P.a_raw_holder[:] = [raw]; a = P.trim(raw)
        ok, info = P.chunk_score(a, text); exact = [{'anna': 'ana'}.get(w, w) for w in info['hyp'].split()] == words(text)
        print(spk, repr(text), seed, ok, exact, info['hyp'], info['flags'], info['probs'], flush=True)
        log.append(dict(spk=spk, text=text, seed=seed, ok=ok, exact=exact, hyp=info['hyp'], flags=info['flags'], probs=info['probs']))
        if exact and not info['flags'] and not info['edge'] and info['sim'] >= 0.85 and min(info['probs']) >= 0.6:
            pickle.dump(a, open(k, 'wb')); done = True; break
    if not done: print('FAILED', spk, text, flush=True)
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
json.dump(log, open(os.path.join(HERE, 'out', 'fix_chunks_log.json'), 'w'), indent=1); print('FIXDONE', flush=True)
