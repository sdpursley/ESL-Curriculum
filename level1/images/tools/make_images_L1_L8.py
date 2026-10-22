"""Level 1, Lesson 8 vocabulary pictures (600x420 PNG cards). Twemoji CC BY 4.0; menu card drawn.
Run: python make_images_L1_L8.py [OUT_DIR]
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'lib'))
from PIL import ImageDraw
import make_images as MI
from make_images import emoji, canvas, font, W, H
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(HERE, '..'))
INK=(30,30,30); NAVY=(31,58,95); RED=(200,40,40); GREY=(120,120,120); YEL=(255,224,102)

def one(code, size=280):
    img=canvas(); img.alpha_composite(emoji(code,size), ((W-size)//2,(H-size)//2)); return img
def two(a,b,sa=200,sb=200):
    img=canvas(); gap=30; tot=sa+sb+gap; x=(W-tot)//2; y=(H-max(sa,sb))//2
    img.alpha_composite(emoji(a,sa),(x,y)); img.alpha_composite(emoji(b,sb),(x+sa+gap,y)); return img
def three(codes, size=150):
    img=canvas(); n=len(codes); gap=20; tot=n*size+gap*(n-1); x=(W-tot)//2; y=(H-size)//2
    for c in codes: img.alpha_composite(emoji(c,size),(x,y)); x+=size+gap
    return img
def meal(codes, label):
    img=three(codes, 140); d=ImageDraw.Draw(img)
    d.rounded_rectangle((150,320,450,390),12,fill=NAVY,outline=INK,width=3)
    d.text((300,355), label, font=font(36), fill='white', anchor='mm'); return img
def menu():
    img=canvas(); d=ImageDraw.Draw(img)
    d.rounded_rectangle((40,20,560,400),14,fill='white',outline=INK,width=5)
    d.rectangle((43,23,557,90), fill=RED)
    d.text((300,56), 'TACO TRUCK', font=font(36), fill='white', anchor='mm')
    rows=[('taco','$3'),('beans & rice','$4'),('fruit','$2'),('juice','$2'),('soda','$1'),('pizza slice','$3')]
    y=110
    for a,b in rows:
        d.text((70,y), a, font=font(30), fill=INK, anchor='lm')
        d.text((530,y), b, font=font(30), fill=NAVY, anchor='rm'); y+=45
    return img

B=[]
def add(name,word,fn,codes,note,drawn='border only'): B.append((name,word,fn,codes,note,drawn))
add('L1_L8_breakfast','breakfast',lambda: meal(['1f95a','1f35e','2615'],'breakfast'),['1f95a','1f35e','2615'],'egg + bread + coffee + breakfast label','sign + text')
add('L1_L8_lunch','lunch',lambda: meal(['1f32e','1f964'],'lunch'),['1f32e','1f964'],'taco + drink + lunch label','sign + text')
add('L1_L8_dinner','dinner',lambda: meal(['1f35d','1f37d'],'dinner'),['1f35d','1f37d'],'spaghetti + plate + dinner label','sign + text')
add('L1_L8_beans','beans',lambda: one('1f372',260),['1f372'],'bowl of food (beans/stew)')
add('L1_L8_tortillas','tortillas',lambda: one('1f32e',260),['1f32e'],'taco / tortilla')
add('L1_L8_meat','meat',lambda: one('1f357',260),['1f357'],'meat (poultry leg)')
add('L1_L8_fish','fish',lambda: one('1f41f',260),['1f41f'],'fish')
add('L1_L8_fruit','fruit',lambda: three(['1f34e','1f34c','1f347'],140),['1f34e','1f34c','1f347'],'apple + banana + grapes')
add('L1_L8_vegetables','vegetables',lambda: three(['1f345','1f966','1f955'],140),['1f345','1f966','1f955'],'tomato + broccoli + carrot')
add('L1_L8_juice','juice',lambda: one('1f9c3',260),['1f9c3'],'juice box')
add('L1_L8_soda','soda',lambda: one('1f964',260),['1f964'],'cup with straw (soda)')
add('L1_L8_pizza','pizza',lambda: one('1f355',280),['1f355'],'pizza')
add('L1_L8_menu','picture menu',menu,[],'taco truck menu with prices (drawn, invented)','all drawn (menu + text)')
add('L1_L8_for_here','for here',lambda: two('1f37d','1f6cb',160,160),['1f37d','1f6cb'],'plate + seat (for here)')
add('L1_L8_to_go','to go',lambda: one('1f372',240),['1f372'],'takeout box / bowl')

# fix meat codes properly
if __name__ == '__main__':
    # remap to available twemoji if needed
    avail=set(os.listdir(os.path.join(HERE,'lib','_twemoji_src')))
    # download missing via emoji()
    os.makedirs(OUT, exist_ok=True); meta=[]
    for name,word,fn,codes,note,drawn in B:
        try:
            MI.save(fn(), f'{OUT}/{name}')
        except Exception as e:
            print('FAIL', name, e); raise
        meta.append(dict(file=f'{name}.png', lesson='Level1-L8', word=word, twemoji=codes, note=note, drawn=drawn))
    json.dump(meta, open(f'{OUT}/images_L1_L8.json','w'), indent=1, ensure_ascii=False)
    print(len(meta), 'images ->', OUT)
