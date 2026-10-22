"""Second opinion on each CHOSEN take by itself (no neighbors): faster-whisper medium.en, beam 5, temperature 0, 1 thread.
Usage: python takes_medium.py script_L1_X.py out/L1_X_listening_log.json   (one line per sentence; MISMATCH lines need a listen,
or vote_takes.py; re-take only when small.en AND medium.en both miss, see AGENTS.md)."""
import os, sys, json, pickle, hashlib, importlib.util, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', 'tools', 'audio'))   # <repo>/tools/audio: processor.py
sys.path[:0] = [HERE, TOOLS]
import processor as P
from canon import canon
from refs import ref_path
spec = importlib.util.spec_from_file_location('S', sys.argv[1]); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
SAME = getattr(S, 'SAME', {}); EX = float(os.environ.get('EXAG', '0.72')); CF = float(os.environ.get('CFG', '0.32'))
CACHE = f'{HERE}/cache'   # the build_listening.py take cache
from faster_whisper import WhisperModel
M = WhisperModel('medium.en', device='cpu', compute_type='int8', cpu_threads=1)
L = json.load(open(sys.argv[2])); L = L if isinstance(L, list) else L.get('log', L.get('sentences'))
bad = 0
for x in L:
    c = x['chosen']; r = ref_path(S.VOICES[c['spk']])
    raw = pickle.load(open(f"{CACHE}/{hashlib.md5(repr((c['tts_text'], r, EX, CF, c['seed'])).encode()).hexdigest()}.pkl", 'rb'))
    a = np.concatenate([P.sil(.3), P.trim(raw), P.sil(.3)])
    x16 = np.interp(np.linspace(0, len(a), int(len(a)*16000/P.SR), endpoint=False), np.arange(len(a)), a).astype(np.float32)
    segs, _ = M.transcribe(x16, beam_size=5, language='en', temperature=0, condition_on_previous_text=False)
    hyp = canon(' '.join(s.text for s in segs), SAME); ok = hyp == canon(c['text'], SAME); bad += not ok
    print(('ok      ' if ok else 'MISMATCH'), c['seed'], c['spk'], '|', c['text'], '|', ' '.join(hyp), flush=True)
print(f'medium.en per-take: {len(L)-bad}/{len(L)} exact')
