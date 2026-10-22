"""Second-opinion ASR: faster-whisper medium.en on the whole MP3, compared with the script.  Usage: python second_opinion.py script.py file.mp3"""
import sys, os, importlib.util, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canon import canon
from faster_whisper import WhisperModel
spec = importlib.util.spec_from_file_location('S', sys.argv[1]); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
SAME = getattr(S, 'SAME', {})
segs, _ = WhisperModel('medium.en', device='cpu', compute_type='int8').transcribe(sys.argv[2], beam_size=5, language='en', condition_on_previous_text=False)
H = canon(' '.join(s.text for s in segs), SAME)
R = canon((S.INTRO if isinstance(S.INTRO, str) else ' '.join(S.INTRO)) + ' ' + ' '.join(L[1] for L in S.LINES) + ' ' + S.END, SAME)
ops = [o for o in difflib.SequenceMatcher(None, R, H, autojunk=False).get_opcodes() if o[0] != 'equal']
err = sum(max(b-a, d-c) for _, a, b, c, d in ops)
print(f'medium.en WER {err/len(R):.3f} ({err}/{len(R)})')
for o, a, b, c, d in ops: print(' ', o, '|', ' '.join(R[a:b]), '->', ' '.join(H[c:d]), '| ctx:', ' '.join(R[max(0, a-3):b+3]))
