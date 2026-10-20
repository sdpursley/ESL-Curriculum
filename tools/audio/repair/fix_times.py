# One-off repair script kept as a record/example (see MAINTAINING.md, "Fixing one bad line").
# Run from tools/audio. Input/output file names reflect the Oct 2026 fix and need editing before reuse.
import re,sys
D={'L1':'1:10','L2':'0:58','L3':'1:05','L4':'1:06','L5':'1:17','L6':'1:08','L7':'1:09','L8':'1:09','L9':'0:57','L10':'1:01','L11':'1:05','L12':'1:31','L13':'0:59','Midterm':'1:12','Final':'1:03'}
pat=re.compile(r'\b(L\d+|Midterm|Final)(_listening\.mp3[^\n]{0,40}?)(about|~) ?\d:\d\d')
def fix(s): return pat.sub(lambda m:f"{m[1]}{m[2]}{m[3]} {D[m[1]]}",s)
if __name__=='__main__':
  for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read(); t=fix(s)
    if s!=t: open(f,'w',encoding='utf-8').write(t); print('fixed',f)
