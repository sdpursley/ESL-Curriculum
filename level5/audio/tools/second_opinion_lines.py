"""Second-opinion ASR per line: faster-whisper medium.en on each line cut from the final MP3 (times from the build log),
plus the intro and end. Use when whole-file long-form decoding drops or loops (a decoder problem, not the audio).
Usage: python second_opinion_lines.py script.py file.mp3 log.json"""
import sys, os, json, importlib.util, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, librosa
from canon import canon
from whisper_cfg import model
spec = importlib.util.spec_from_file_location('S', sys.argv[1]); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
SAME = getattr(S, 'SAME', {}); LT = json.load(open(sys.argv[3]))['line_times']
x, sr = librosa.load(sys.argv[2], sr=16000)
segs = [(0.0, LT[0][0] - 0.5, 'Narrator', S.INTRO if isinstance(S.INTRO, str) else ' '.join(S.INTRO))] + [tuple(l) for l in LT] + [(LT[-1][1] + 0.5, len(x)/sr, 'Narrator', S.END)]
M = model('medium.en'); err = tot = 0; bad = []
for a, b, spk, line in segs:
    clip = np.concatenate([np.zeros(int(0.6*sr), np.float32), x[max(0, int((a-0.3)*sr)):int((b+0.3)*sr)], np.zeros(int(0.6*sr), np.float32)])
    h = canon(' '.join(s.text for s in M.transcribe(clip, beam_size=5, language='en', condition_on_previous_text=False)[0]), SAME)
    r = canon(line, SAME); ops = [o for o in difflib.SequenceMatcher(None, r, h, autojunk=False).get_opcodes() if o[0] != 'equal']
    e = sum(max(q-p, t-s) for _, p, q, s, t in ops); err += e; tot += len(r)
    if e: bad.append((spk, line, ' '.join(h)))
print(f'medium.en per-line WER {err/tot:.3f} ({err}/{tot}), {len(segs)-len(bad)}/{len(segs)} lines exact')
for b in bad: print('  ', b)
