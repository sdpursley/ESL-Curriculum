# One-off repair script kept as a record/example (see MAINTAINING.md, "Fixing one bad line").
# Run from tools/audio. Input/output file names reflect the Oct 2026 fix and need editing before reuse.
import sys, os, numpy as np, soundfile as sf, torch, pyloudnorm as pyln, subprocess
sys.path.insert(0,'.'); import processor as P  # run from tools/audio
from faster_whisper import WhisperModel
from textnorm import words
say=P.make_engine('chatterbox'); W=WhisperModel("small.en",device="cpu",compute_type="int8")
a,sr=sf.read('backup_pre_fix6/chatterbox_L12_pre_lopez.wav',dtype='float32'); S,E=int(42.85*sr),int(43.56*sr); M=pyln.Meter(sr)
def asr(x):
    x=np.concatenate([np.zeros(int(.3*sr),np.float32),x,np.zeros(int(.3*sr),np.float32)])
    x16=np.interp(np.linspace(0,len(x),int(len(x)*16000/sr),endpoint=False),np.arange(len(x)),x).astype(np.float32)
    r,_=W.transcribe(x16,beam_size=5,language='en',condition_on_previous_text=False,word_timestamps=True)
    return [(w.word.strip(),round(w.probability,2)) for g in r for w in g.words]
def splice(n):
    b0,b1,_=P.speech_bounds(n); c=n[b0:b1].copy(); fd=int(.01*sr); c[:fd]*=np.linspace(0,1,fd); c[-fd:]*=np.linspace(1,0,fd)
    old=np.concatenate([a[S:E]]*3); c3=np.concatenate([c]*3)  # short clips: loop for loudness meter (as processor.norm)
    c*=10**((M.integrated_loudness(old)-M.integrated_loudness(c3))/20)
    return np.clip(np.concatenate([a[:S],c,a[E:]]),-.98,.98), len(c)
trials=[]
for sp in ['Lo-pez.','Low-pez.','Lopes.','LOH-pez.','Lopez!']:
    for ex,cf in [('0.55','0.45'),('0.4','0.5')]:
        for i in range(5): trials.append((sp,ex,cf,9300+i*7919+13))
for sp,ex,cf,seed in trials:
    os.environ['EXAG']=ex; os.environ['CFG']=cf; torch.manual_seed(seed)
    raw=say(sp,'samples/refs/Sam.wav'); P.a_raw_holder[:]=[raw]; n=P.trim(raw)
    ok,info=P.chunk_score(n,'Lopez.'); out,L=splice(n); d=L-(E-S)
    iso=asr(out[S:S+L]); ctx=asr(out[int(39.3*sr):int(46.3*sr)+d])
    isow=[x for w,_ in iso for x in words(w)]
    good=ok and info['hyp'] in('lopez','lopes') and isow in(['lopez'],['lopes']) and any(words(w)==['lopez'] for w,_ in ctx)
    print('TRY',repr(sp),ex,cf,seed,ok,info['hyp'],info['flags'],'iso',iso,'ctx',ctx,flush=True)
    if good:
        sf.write('samples/chatterbox_L12.wav',out,sr)
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i','samples/chatterbox_L12.wav','-ac','1','-b:a','96k','-metadata','title=Level 2 L12 Listening','-metadata','comment=Synthetic voices (Chatterbox TTS, Resemble AI, MIT License; contains an inaudible Perth watermark). Script CC BY-NC-SA 4.0.','L12_listening.mp3'],check=True)
        print('KEPT',repr(sp),ex,cf,seed,'dur',len(out)/sr); break
else: print('FAILED')
