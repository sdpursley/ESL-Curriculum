#!/bin/bash
# montage_L4.sh N [first last] -> /tmp/l4_LN_mont.png
N=$1; F=${2:-1}; T=${3:-30}
D=/workspace/level4_curriculum/lesson$N; rm -rf /tmp/l4m$N; mkdir -p /tmp/l4m$N
pdftoppm -r 30 -f $F -l $T -png $D/Level4_Lesson$N.pdf /tmp/l4m$N/p
/workspace/tts/venv_l3img/bin/python - <<PY
from PIL import Image; import glob
fs=sorted(glob.glob('/tmp/l4m$N/p*.png')); ims=[Image.open(f) for f in fs]; w,h=ims[0].size; c=8
m=Image.new('RGB',(w*c,h*((len(ims)+c-1)//c)),'white')
for i,im in enumerate(ims): m.paste(im,((i%c)*w,(i//c)*h))
m.save('/tmp/l4_L${N}_mont.png'); print(len(ims),'pages')
PY
