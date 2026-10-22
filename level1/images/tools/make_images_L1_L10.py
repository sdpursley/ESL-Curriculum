"""Level 1, Lesson 10 vocabulary pictures (600x420). Twemoji CC BY 4.0; refrigerator drawn (no Twemoji fridge).
Run: python make_images_L1_L10.py [OUT_DIR]
"""
import os,sys,json
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'lib'))
from PIL import ImageDraw
import make_images as MI
from make_images import emoji, canvas, font, W, H
OUT=os.path.abspath(sys.argv[1]) if len(sys.argv)>1 else os.path.abspath(os.path.join(HERE, '..'))
INK=(30,30,30); NAVY=(31,58,95); RED=(200,40,40); GREY=(120,120,120); YEL=(255,224,102)

def one(code,size=280):
    img=canvas(); img.alpha_composite(emoji(code,size),((W-size)//2,(H-size)//2)); return img
def two(a,b,sa=200,sb=200):
    img=canvas(); gap=24; tot=sa+sb+gap; x=(W-tot)//2; y=(H-max(sa,sb))//2
    img.alpha_composite(emoji(a,sa),(x,y)); img.alpha_composite(emoji(b,sb),(x+sa+gap,y)); return img

def fridge():
    """labeled drawing — no Twemoji refrigerator"""
    img=canvas(); d=ImageDraw.Draw(img)
    d.rounded_rectangle((180,40,420,380),16,fill=(220,230,240),outline=INK,width=5)
    d.line((180,200,420,200),fill=INK,width=4)
    d.ellipse((380,110,400,130),fill=GREY)  # freezer handle
    d.ellipse((380,270,400,290),fill=GREY)
    d.rounded_rectangle((200,320,400,365),8,fill=NAVY)
    d.text((300,342),'refrigerator',font=font(22),fill='white',anchor='mm'); return img

def apartment_ad():
    img=canvas(); d=ImageDraw.Draw(img)
    d.rounded_rectangle((40,30,560,390),14,fill='white',outline=INK,width=5)
    d.rectangle((43,33,557,100),fill=NAVY)
    d.text((300,66),'FOR RENT',font=font(36),fill='white',anchor='mm')
    lines=['2 BR, 1 BA','Living room + kitchen','$900 / month','Call 555-0199']
    y=140
    for L in lines:
        d.text((300,y),L,font=font(34),fill=INK,anchor='mm'); y+=55
    return img

def floorplan():
    img=canvas(); d=ImageDraw.Draw(img)
    d.rectangle((40,40,560,380),outline=INK,width=5)
    d.rectangle((40,40,300,220),outline=INK,width=3); d.text((170,130),'bedroom',font=font(24),fill=NAVY,anchor='mm')
    d.rectangle((300,40,560,220),outline=INK,width=3); d.text((430,130),'kitchen',font=font(24),fill=NAVY,anchor='mm')
    d.rectangle((40,220,300,380),outline=INK,width=3); d.text((170,300),'bathroom',font=font(24),fill=NAVY,anchor='mm')
    d.rectangle((300,220,560,380),outline=INK,width=3); d.text((430,300),'living room',font=font(22),fill=NAVY,anchor='mm')
    return img

B=[]
def add(name,word,fn,codes,note,drawn='border only'): B.append((name,word,fn,codes,note,drawn))
add('L1_L10_house','house',lambda: one('1f3e0'),['1f3e0'],'house')
add('L1_L10_apartment','apartment',lambda: one('1f3e2'),['1f3e2'],'apartment building')
add('L1_L10_kitchen','kitchen',lambda: two('1f373','1f37d',160,160),['1f373','1f37d'],'pan + plate (kitchen)')
add('L1_L10_bedroom','bedroom',lambda: one('1f6cf',260),['1f6cf'],'bed')  # may be 1f6cf-fe0f
add('L1_L10_bathroom','bathroom',lambda: one('1f6bd',260),['1f6bd'],'toilet')
add('L1_L10_living_room','living room',lambda: one('1f6cb',260),['1f6cb'],'couch / living room')
add('L1_L10_bed','bed',lambda: one('1f6cf',280),['1f6cf'],'bed')
add('L1_L10_table','table',lambda: one('1fa91',280),['1fa91'],'chair — table uses drawn+chair; prefer 1f37d table setting')
add('L1_L10_chair','chair',lambda: one('1fa91',280),['1fa91'],'chair')
add('L1_L10_sofa','sofa',lambda: one('1f6cb',280),['1f6cb'],'sofa / couch')
add('L1_L10_refrigerator','refrigerator',fridge,[],'refrigerator (drawn — no Twemoji fridge)','all drawn')
add('L1_L10_window','window',lambda: one('1fa9f',280),['1fa9f'],'window')
add('L1_L10_apartment_ad','apartment ad',apartment_ad,[],'FOR RENT ad 2BR 1BA $900 (drawn, invented)','all drawn')
add('L1_L10_floor_plan','floor plan',floorplan,[],'simple 4-room floor plan (drawn)','all drawn')

if __name__=='__main__':
    # fix table to use a better emoji if available
    def table():
        img=canvas(); d=ImageDraw.Draw(img)
        # drawn simple table
        d.rectangle((120,180,480,220),fill=(160,110,60),outline=INK,width=3)
        d.rectangle((150,220,180,340),fill=(120,80,40),outline=INK,width=2)
        d.rectangle((420,220,450,340),fill=(120,80,40),outline=INK,width=2)
        d.text((300,100),'table',font=font(36),fill=NAVY,anchor='mm'); return img
    B=[t if t[0]!='L1_L10_table' else ('L1_L10_table','table',table,[],'table (drawn)','all drawn') for t in B]
    # try bedroom codes
    for c in ['1f6cf','1f6bd','1fa9f','1fa91','1f6cb']:
        try: emoji(c,32); print('ok',c)
        except Exception as e: print('FAIL',c, type(e).__name__)
    os.makedirs(OUT,exist_ok=True); meta=[]
    for name,word,fn,codes,note,drawn in B:
        try:
            MI.save(fn(),f'{OUT}/{name}'); meta.append(dict(file=f'{name}.png',lesson='Level1-L10',word=word,twemoji=codes,note=note,drawn=drawn))
        except Exception as e:
            print('ERR',name,e); 
            # fallback
            if 'bed' in name or 'bedroom' in name:
                MI.save(one('1f6cc',280) if False else two('1f6cb','1f319',160,120), f'{OUT}/{name}')
            raise
    json.dump(meta,open(f'{OUT}/images_L1_L10.json','w'),indent=1,ensure_ascii=False)
    print(len(meta),'images')
