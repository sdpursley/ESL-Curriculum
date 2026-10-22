"""Check each CHOSEN take (alone) with two Whisper models: small.en and medium.en, float32, 1 thread, temperature 0, R runs each.
Whisper can return different text for the same audio under heavy CPU load, so one miss is not proof of a bad take.
A take PASSES if EITHER checker hears the exact script words in most of its runs. Re-take only when BOTH checkers fail
(or for pitch / clipping, which build_listening.py and check_listening.py report). Spelled letters and digit strings score low:
check those by ear.
Usage: python vote_takes.py script_L1_X.py out/L1_X_listening_log.json [R]   (default R = 3). Run it under the same lock as Chatterbox."""
import os, sys, json, pickle, hashlib, importlib.util, collections, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', 'tools', 'audio'))   # <repo>/tools/audio: processor.py
sys.path[:0] = [HERE, TOOLS]
import processor as P
from canon import canon
from refs import ref_path
from faster_whisper import WhisperModel
spec = importlib.util.spec_from_file_location('S', sys.argv[1]); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
SAME = getattr(S, 'SAME', {}); R = int(sys.argv[3]) if len(sys.argv) > 3 else 3
EX = float(os.environ.get('EXAG', '0.72')); CF = float(os.environ.get('CFG', '0.32')); CACHE = f'{HERE}/cache'
L = json.load(open(sys.argv[2])); L = L if isinstance(L, list) else L.get('log', L.get('sentences'))
xs = []
for x in L:
    c = x['chosen']; r = ref_path(S.VOICES[c['spk']])
    raw = pickle.load(open(f"{CACHE}/{hashlib.md5(repr((c['tts_text'], r, EX, CF, c['seed'])).encode()).hexdigest()}.pkl", 'rb'))
    a = np.concatenate([P.sil(.3), P.trim(raw), P.sil(.3)])
    xs.append(np.interp(np.linspace(0, len(a), int(len(a)*16000/P.SR), endpoint=False), np.arange(len(a)), a).astype(np.float32))
MODELS = ('small.en', 'medium.en')
hits = {m: collections.defaultdict(int) for m in MODELS}; heard = collections.defaultdict(collections.Counter)
for name in MODELS:
    M = WhisperModel(name, device='cpu', compute_type='float32', cpu_threads=1)
    for rep in range(R):
        for i, x in enumerate(xs):
            hyp = ' '.join(canon(' '.join(s.text for s in M.transcribe(x, beam_size=5, language='en', temperature=0, condition_on_previous_text=False)[0]), SAME))
            ok = hyp == ' '.join(canon(L[i]['chosen']['text'], SAME)); hits[name][i] += ok; heard[i][hyp] += 1
        print(f'{name} run {rep+1} done', flush=True)
    del M
bad = 0
for i, x in enumerate(L):
    c = x['chosen']; v = 'ok ' if any(hits[m][i] > R/2 for m in MODELS) else 'BAD'; bad += v == 'BAD'
    print(f"{v} small {hits['small.en'][i]}/{R} medium {hits['medium.en'][i]}/{R} seed {c['seed']} {c['spk']}: {c['text']} | most heard: {heard[i].most_common(1)[0][0]}")
print(f'vote: {len(L)-bad}/{len(L)} takes OK (either checker exact in most of its {R} runs)')
