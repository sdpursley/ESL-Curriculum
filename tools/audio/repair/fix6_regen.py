# One-off repair script kept as a record/example (see MAINTAINING.md, "Fixing one bad line").
# Run from tools/audio. Input/output file names reflect the Oct 2026 fix and need editing before reuse.
import sys, os, json, numpy as np, soundfile as sf
AUDIO=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); sys.path.insert(0,AUDIO); os.chdir(AUDIO)
import processor as P, torch
from textnorm import words
P.MIN_WORDS=3
refs='samples/refs'
JOBS=[('L5','Marco','Oh no. And on Sunday?',['Oh, no. And on Sunday?']),
      ('L6','Sam','Ha! Did you find a job quickly?',['Ha! Did you find a job quickly?','Ha. Did you find a job quickly?']),
      ('L12','Agent','You only need to pay forty-five dollars.',['You only need to pay forty-five dollars!']),
      ('L13','N','Ana gives a short talk at graduation. Listen.',['Ana gives a short talk at graduation. Listen!']),
      ('L13','Ana','Good evening, everyone.',['Good evening, everyone!'])]
say=P.make_engine('chatterbox'); os.makedirs('samples/fix6',exist_ok=True); log=[]
def norm_hyp(h): return words(" ".join(h.split()).replace("o 'clock","o'clock"))
for k,spk,text,alts in JOBS:
    done=False
    for ti,t in enumerate([text]+[x for x in alts if x!=text]):
        for i in range(10 if ti==0 else 6):
            seed=7100+ti*500+i*7919; torch.manual_seed(seed)
            raw=say(t,f'{refs}/{spk}.wav'); P.a_raw_holder[:]=[raw]; a=P.trim(raw)
            ok,info=P.chunk_score(a,t); exact=info['hyp'].split()==words(text)
            print(k,repr(t),seed,ok,exact,info['hyp'],info['flags'],info['probs'],flush=True)
            log.append(dict(key=k,text=t,seed=seed,ok=ok,exact=exact,**{x:info[x] for x in('hyp','flags','probs','sim','edge')}))
            if ok and exact:
                sf.write(f'samples/fix6/{k}_{spk}.wav',a,P.SR); done=True; break
        if done: break
    if not done: print('FAILED',k,text,flush=True)
json.dump(log,open('samples/fix6/regen_log.json','w'),indent=1,default=str)
print('ALLDONE')
