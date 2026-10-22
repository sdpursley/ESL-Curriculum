"""Level 1, Lesson 12 body / health pictures. Twemoji CC BY 4.0; back/stomach and emergency card drawn."""
import os,sys,json
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'lib'))
from PIL import ImageDraw
import make_images as MI
from make_images import emoji, canvas, font, W, H
OUT=os.path.abspath(sys.argv[1]) if len(sys.argv)>1 else os.path.abspath(os.path.join(HERE, '..'))
INK=(30,30,30); NAVY=(31,58,95); RED=(200,40,40); GREY=(120,120,120); YEL=(255,224,102)

def one(code,size=280):
    img=canvas(); img.alpha_composite(emoji(code,size),((W-size)//2,(H-size)//2)); return img
def body_label(region):
    """simple body outline with label"""
    img=canvas(); d=ImageDraw.Draw(img)
    # stick figure torso
    d.ellipse((250,40,350,140),outline=INK,width=5)  # head
    d.line((300,140,300,280),fill=INK,width=8)  # body
    d.line((300,180,220,240),fill=INK,width=6); d.line((300,180,380,240),fill=INK,width=6)  # arms
    d.line((300,280,240,380),fill=INK,width=6); d.line((300,280,360,380),fill=INK,width=6)  # legs
    labels={'back':(420,200),'stomach':(300,220)}
    x,y=labels[region]
    d.ellipse((x-12,y-12,x+12,y+12),fill=RED)
    d.rounded_rectangle((40,320,560,390),10,fill=YEL,outline=RED,width=3)
    d.text((300,355),region,font=font(40),fill=INK,anchor='mm'); return img
def medicine():
    img=canvas(); d=ImageDraw.Draw(img)
    d.rounded_rectangle((80,40,520,380),14,fill='white',outline=INK,width=5)
    d.rectangle((83,43,517,100),fill=NAVY)
    d.text((300,70),'MEDICINE',font=font(32),fill='white',anchor='mm')
    for i,line in enumerate(['Take 2 tablets.','Every 6 hours.','With water.']):
        d.text((300,160+i*60),line,font=font(34),fill=INK,anchor='mm')
    return img
def emergency_card():
    img=canvas(); d=ImageDraw.Draw(img)
    d.rounded_rectangle((40,40,560,380),14,fill='white',outline=RED,width=5)
    d.rectangle((43,43,557,100),fill=RED)
    d.text((300,70),'MY EMERGENCY CARD',font=font(26),fill='white',anchor='mm')
    rows=[('Name','ANA RUIZ'),('Address','210 Pine St'),('Phone','555-0142'),('Emergency','555-0199')]
    y=130
    for a,b in rows:
        d.text((70,y),a,font=font(24),fill=GREY,anchor='lm')
        d.text((530,y),b,font=font(28),fill=NAVY,anchor='rm'); y+=55
    return img

B=[]
def add(n,w,fn,c,note,drawn='border only'): B.append((n,w,fn,c,note,drawn))
add('L1_L12_head','head',lambda: one('1f9d1',260),['1f9d1'],'person (head)')
add('L1_L12_eye','eye',lambda: one('1f441',260),['1f441'],'eye')
add('L1_L12_ear','ear',lambda: one('1f442',260),['1f442'],'ear')
add('L1_L12_mouth','mouth',lambda: one('1f444',260),['1f444'],'mouth')
add('L1_L12_arm','arm',lambda: one('1f4aa',260),['1f4aa'],'flexed biceps (arm)')
add('L1_L12_hand','hand',lambda: one('270b',260),['270b'],'raised hand')
add('L1_L12_leg','leg',lambda: one('1f9b5',260),['1f9b5'],'leg')
add('L1_L12_foot','foot',lambda: one('1f9b6',260),['1f9b6'],'foot')
add('L1_L12_back','back',lambda: body_label('back'),[],'body drawing labeled back','all drawn')
add('L1_L12_stomach','stomach',lambda: body_label('stomach'),[],'body drawing labeled stomach','all drawn')
add('L1_L12_sick','sick',lambda: one('1f912',280),['1f912'],'face with thermometer')
add('L1_L12_doctor','doctor',lambda: one('1f9d1-200d-2695-fe0f',280),['1f9d1-200d-2695-fe0f'],'health worker')
add('L1_L12_medicine_label','medicine label',medicine,[],'Take 2 tablets / Every 6 hours (drawn)','all drawn')
add('L1_L12_emergency_card','emergency card',emergency_card,[],'My Emergency Card with invented info (drawn)','all drawn')

if __name__=='__main__':
    os.makedirs(OUT,exist_ok=True); meta=[]
    for name,word,fn,codes,note,drawn in B:
        try:
            MI.save(fn(),f'{OUT}/{name}')
        except Exception as e:
            print('FAIL',name,e); 
            # try alternate codes
            raise
        meta.append(dict(file=f'{name}.png',lesson='Level1-L12',word=word,twemoji=codes,note=note,drawn=drawn))
    json.dump(meta,open(f'{OUT}/images_L1_L12.json','w'),indent=1,ensure_ascii=False)
    print(len(meta),'images')
