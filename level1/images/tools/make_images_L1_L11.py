"""Level 1, Lesson 11 vocabulary pictures (600x420). Twemoji CC BY 4.0; map and street signs drawn."""
import os,sys,json
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'lib'))
from PIL import ImageDraw
import make_images as MI
from make_images import emoji, canvas, font, W, H
OUT=os.path.abspath(sys.argv[1]) if len(sys.argv)>1 else os.path.abspath(os.path.join(HERE, '..'))
INK=(30,30,30); NAVY=(31,58,95); RED=(200,40,40); GREY=(120,120,120); GREEN=(20,140,60)

def one(code,size=280):
    img=canvas(); img.alpha_composite(emoji(code,size),((W-size)//2,(H-size)//2)); return img
def label_sign(text, fill=NAVY, size=48):
    img=canvas(); d=ImageDraw.Draw(img)
    d.rounded_rectangle((80,120,520,300),16,fill=fill,outline=INK,width=5)
    d.text((300,210),text,font=font(size),fill='white',anchor='mm'); return img
def arrow_card(dir):
    img=canvas(); d=ImageDraw.Draw(img)
    if dir=='left':
        d.polygon([(400,210),(200,210),(200,150),(80,210),(200,270),(200,210)],fill=NAVY)
        d.text((300,350),'left',font=font(40),fill=NAVY,anchor='mm')
    else:
        d.polygon([(200,210),(400,210),(400,150),(520,210),(400,270),(400,210)],fill=NAVY)
        d.text((300,350),'right',font=font(40),fill=NAVY,anchor='mm')
    return img
def street_map():
    img=canvas(); d=ImageDraw.Draw(img)
    d.rectangle((40,40,560,380),outline=INK,width=4)
    # streets
    d.line((40,210,560,210),fill=GREY,width=18)
    d.line((300,40,300,380),fill=GREY,width=18)
    places=[(120,100,'bank'),(420,100,'pharmacy'),(120,280,'school'),(420,280,'park')]
    for x,y,name in places:
        d.rounded_rectangle((x-50,y-30,x+50,y+30),8,fill=(234,241,248),outline=NAVY,width=3)
        d.text((x,y),name,font=font(20),fill=NAVY,anchor='mm')
    d.text((300,25),'Main St',font=font(18),fill=INK,anchor='mm')
    return img
def sign(text, fill=RED, fsize=40):
    img=canvas(); d=ImageDraw.Draw(img)
    d.rounded_rectangle((60,100,540,320),14,fill=fill,outline=INK,width=5)
    d.text((300,210),text,font=font(fsize),fill='white',anchor='mm'); return img

B=[]
def add(n,w,fn,c,note,drawn='border only'): B.append((n,w,fn,c,note,drawn))
add('L1_L11_bank','bank',lambda: one('1f3e6'),['1f3e6'],'bank')
add('L1_L11_pharmacy','pharmacy',lambda: one('1f48a'),['1f48a'],'pill (pharmacy)')
add('L1_L11_school','school',lambda: one('1f3eb'),['1f3eb'],'school')
add('L1_L11_hospital','hospital',lambda: one('1f3e5'),['1f3e5'],'hospital')
add('L1_L11_bus_stop','bus stop',lambda: one('1f68f'),['1f68f'],'bus stop')
add('L1_L11_store','store',lambda: one('1f3ea'),['1f3ea'],'convenience store')
add('L1_L11_park','park',lambda: one('1f333'),['1f333'],'tree (park)')
add('L1_L11_restaurant','restaurant',lambda: one('1f37d'),['1f37d'],'fork and knife')
add('L1_L11_street','street',lambda: one('1f6e3'),['1f6e3'],'motorway / street')
add('L1_L11_corner','corner',lambda: label_sign('CORNER',NAVY,48),[],'CORNER label (drawn)','all drawn')
add('L1_L11_left','left',lambda: arrow_card('left'),[],'left arrow (drawn)','all drawn')
add('L1_L11_right','right',lambda: arrow_card('right'),[],'right arrow (drawn)','all drawn')
add('L1_L11_map','street map',street_map,[],'simple street map with places (drawn)','all drawn')
add('L1_L11_sign_exit','EXIT',lambda: sign('EXIT',RED,64),[],'EXIT sign (drawn)','all drawn')
add('L1_L11_sign_push','PUSH / PULL',lambda: sign('PUSH  ·  PULL',NAVY,40),[],'PUSH / PULL sign (drawn)','all drawn')
add('L1_L11_sign_one_way','ONE WAY',lambda: sign('ONE WAY',(20,100,60),48),[],'ONE WAY sign (drawn)','all drawn')

if __name__=='__main__':
    os.makedirs(OUT,exist_ok=True); meta=[]
    for name,word,fn,codes,note,drawn in B:
        MI.save(fn(),f'{OUT}/{name}')
        meta.append(dict(file=f'{name}.png',lesson='Level1-L11',word=word,twemoji=codes,note=note,drawn=drawn))
    json.dump(meta,open(f'{OUT}/images_L1_L11.json','w'),indent=1,ensure_ascii=False)
    print(len(meta),'images')
