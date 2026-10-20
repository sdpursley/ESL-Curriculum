import os, sys, numpy as np, soundfile as sf, subprocess
sys.path.insert(0,'.')
from scripts import VOICES, LESSONS
from kokoro_onnx import Kokoro
k = Kokoro(os.environ.get('KOKORO_MODEL', 'models/kokoro-v1.0.onnx'), os.environ.get('KOKORO_VOICES', 'models/voices-v1.0.bin'))
SPEED = 0.9
def say(text, voice):
    a, sr = k.create(text, voice=voice, speed=SPEED, lang='en-us'); return a, sr
def sil(sec, sr=24000): return np.zeros(int(sec*sr), dtype=np.float32)
for key in sys.argv[1:] or LESSONS:
    intro, lines = LESSONS[key]
    a, sr = say(intro, VOICES['N']); parts = [sil(0.5), a, sil(1.2)]
    dlg = []
    for spk, line in lines:
        x, _ = say(line, VOICES[spk]); dlg += [x, sil(0.55)]
    parts += dlg
    a2, _ = say("Listen again.", VOICES['N']); parts += [sil(2.5), a2, sil(1.0)] + dlg
    end, _ = say("That's the end of the listening.", VOICES['N']); parts += [sil(1.0), end, sil(0.5)]
    audio = np.concatenate(parts)
    sf.write(f'{key}_listening.wav', audio, sr)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'{key}_listening.wav','-ac','1','-b:a','96k',
                    '-metadata',f'title=Level 2 {key} Listening','-metadata','comment=Synthetic voice (Kokoro-82M, Apache-2.0). Script CC BY-NC-SA 4.0.',
                    f'{key}_listening.mp3'], check=True)
    print(key, round(len(audio)/sr,1), 'sec')
