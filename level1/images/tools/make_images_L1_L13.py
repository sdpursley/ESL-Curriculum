"""Level 1, Lesson 13 skills / can pictures. Twemoji CC BY 4.0; job application drawn."""
import os,sys,json
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'lib'))
from PIL import ImageDraw
import make_images as MI
from make_images import emoji, canvas, font, W, H
OUT=os.path.abspath(sys.argv[1]) if len(sys.argv)>1 else os.path.abspath(os.path.join(HERE, '..'))
INK=(30,30,30); NAVY=(31,58,95); RED=(200,40,40); GREY=(120,120,120); GREEN=(20,140,60)

def one(code,size=280):
    img=canvas(); img.alpha_composite(emoji(code,size),((W-size)//2,(H-size)//2)); return img
def two(a,b,sa=180,sb=180):
    img=canvas(); gap=24; tot=sa+sb+gap; x=(W-tot)//2; y=(H-max(sa,sb))//2
    img.alpha_composite(emoji(a,sa),(x,y)); img.alpha_composite(emoji(b,sb),(x+sa+gap,y)); return img
def can_cant(label, ok=True):
    img=canvas(); d=ImageDraw.Draw(img)
    col=GREEN if ok else RED
    d.rounded_rectangle((100,80,500,280),20,fill=col,outline=INK,width=5)
    d.text((300,180),label,font=font(64),fill='white',anchor='mm'); return img
def job_app():
    img=canvas(); d=ImageDraw.Draw(img)
    d.rounded_rectangle((40,20,560,400),12,fill='white',outline=INK,width=4)
    d.rectangle((43,23,557,80),fill=NAVY)
    d.text((300,50),'JOB APPLICATION',font=font(28),fill='white',anchor='mm')
    y=100
    for lab in ['Name: _______________','Phone: ______________','Days: ☐ Mon ☐ Tue ☐ Wed','Skills: ☐ cook ☐ drive ☐ clean']:
        d.text((70,y),lab,font=font(26),fill=INK,anchor='lm'); y+=70
    return img

B=[]
def add(n,w,fn,c,note,drawn='border only'): B.append((n,w,fn,c,note,drawn))
add('L1_L13_drive','drive',lambda: one('1f697'),['1f697'],'car (drive)')
add('L1_L13_cook','cook',lambda: one('1f9d1-200d-1f373'),['1f9d1-200d-1f373'],'cook')
add('L1_L13_clean','clean',lambda: one('1f9f9'),['1f9f9'],'broom (clean)')
add('L1_L13_fix','fix (cars)',lambda: two('1f527','1f697',140,160),['1f527','1f697'],'wrench + car')
add('L1_L13_paint','paint',lambda: one('1f58c'),['1f58c'],'paintbrush')
add('L1_L13_computer','use a computer',lambda: one('1f5a5'),['1f5a5'],'desktop computer')
add('L1_L13_speak_english','speak English',lambda: two('1f5e3','1f1fa-1f1f8',160,160),['1f5e3','1f1fa-1f1f8'],'speaking head + US flag')
add('L1_L13_take_care','take care of (kids)',lambda: two('1f9d1','1f9d2',160,160),['1f9d1','1f9d2'],'adult + child')
add('L1_L13_lift','lift (heavy things)',lambda: one('1f4aa'),['1f4aa'],'flexed biceps (lift)')
add('L1_L13_swim','swim',lambda: one('1f3ca'),['1f3ca'],'swimmer')
add('L1_L13_job_interview','job interview',lambda: two('1f9d1-200d-1f4bc','1f4cb',160,160),['1f9d1-200d-1f4bc','1f4cb'],'office worker + clipboard')
add('L1_L13_skill','skill',lambda: one('1f3af'),['1f3af'],'bullseye (skill)')
add('L1_L13_can','I can',lambda: can_cant('I can',True),[],'I can label (drawn)','all drawn')
add('L1_L13_cant',"I can't",lambda: can_cant("I can't",False),[],"I can't label (drawn)",'all drawn')
add('L1_L13_job_application','job application',job_app,[],'simple job application form (drawn)','all drawn')

if __name__=='__main__':
    os.makedirs(OUT,exist_ok=True); meta=[]
    for name,word,fn,codes,note,drawn in B:
        MI.save(fn(),f'{OUT}/{name}')
        meta.append(dict(file=f'{name}.png',lesson='Level1-L13',word=word,twemoji=codes,note=note,drawn=drawn))
    json.dump(meta,open(f'{OUT}/images_L1_L13.json','w'),indent=1,ensure_ascii=False)
    print(len(meta),'images')
