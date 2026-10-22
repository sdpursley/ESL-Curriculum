"""Re-check every line of a finished listening file on the 24 kHz WAV: artifact flags (artifacts.detect) and a padded
small.en transcript with word confidences. Usage: python verify24.py script.py file.wav log.json [substring ...]"""
import sys, os, json, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', 'tools', 'audio'))   # <repo>/tools/audio: processor.py, artifacts.py, textnorm.py
sys.path[:0] = [HERE, TOOLS]
import numpy as np, soundfile as sf, librosa
from artifacts import detect
from canon import canon
from faster_whisper import WhisperModel
spec = importlib.util.spec_from_file_location('S', sys.argv[1]); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
tts = {l[1]: (l[2] if len(l) > 2 else l[1]) for l in S.LINES}; SAME = getattr(S, 'SAME', {})
L = json.load(open(sys.argv[3])); x, sr = sf.read(sys.argv[2]); x = x.astype(np.float32); only = sys.argv[4:]
M = WhisperModel('small.en', device='cpu', compute_type='int8')
for a, b, spk, line in L['line_times']:
    if only and not any(o in line for o in only): continue
    seg = x[int((a-0.15)*sr):int((b+0.15)*sr)]; fl = detect(seg, sr, tts[line], None)[0]
    s16 = librosa.resample(seg, orig_sr=sr, target_sr=16000); pad = np.zeros(8000, np.float32)
    ws = [w for s in M.transcribe(np.concatenate([pad, s16, pad]), word_timestamps=True, language='en', beam_size=5)[0] for w in s.words]
    hyp = canon(' '.join(w.word for w in ws), SAME); ok = hyp == canon(line, SAME)
    print(f"{a:6.2f} {spk:12s} exact={ok} flags24k={fl} minp={min([w.probability for w in ws] or [0]):.2f} | {' '.join(w.word.strip() for w in ws)}")
