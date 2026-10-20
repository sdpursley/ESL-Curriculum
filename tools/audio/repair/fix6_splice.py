# One-off repair script kept as a record/example (see MAINTAINING.md, "Fixing one bad line").
# Run from tools/audio. Input/output file names reflect the Oct 2026 fix and need editing before reuse.
import numpy as np, soundfile as sf, pyloudnorm as pyln, subprocess, sys
sys.path.insert(0,'.'); import processor as P  # run from tools/audio
J={'L5':('Marco',41.89,43.27),'L6':('Sam',34.97,37.0),'L13':('Ana',7.74,9.52)}
for k,(spk,s,e) in J.items():
    a,sr=sf.read(f'backup_pre_fix6/chatterbox_{k}.wav',dtype='float32')
    n,_=sf.read(f'samples/fix6/{k}_{spk}.wav',dtype='float32')
    b0,b1,_=P.speech_bounds(n); core=n[b0:b1].copy(); fd=int(.01*sr); core[:fd]*=np.linspace(0,1,fd); core[-fd:]*=np.linspace(1,0,fd)
    s0,e0=int(s*sr),int(e*sr); old=a[s0:e0]; M=pyln.Meter(sr)
    core*=10**((M.integrated_loudness(old)-M.integrated_loudness(core))/20)
    out=np.clip(np.concatenate([a[:s0],core,a[e0:]]),-0.98,0.98)
    sf.write(f'samples/chatterbox_{k}.wav',out,sr)
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f'samples/chatterbox_{k}.wav','-ac','1','-b:a','96k','-metadata',f'title=Level 2 {k} Listening (chatterbox)',f'{k}_listening.mp3'],check=True)
    print(k,'old',round(len(a)/sr,2),'new',round(len(out)/sr,2),'chunk',round((e0-s0)/sr,2),'->',round(len(core)/sr,2),'peak',round(abs(out).max(),3))
