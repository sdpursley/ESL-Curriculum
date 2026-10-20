"""Level 1, Lesson 1 vocabulary pictures (600x420 PNG cards), same helpers and style as Level 2's make_images.py.
Emoji graphics: Twemoji (jdecked/twemoji), CC BY 4.0. ID cards, name tag, speech bubbles, letters and labels drawn in code.
Run from this folder (level1/images/tools/): python make_images_L1.py  -> writes PNGs + images_L1.json into level1/images/
The Level 2 helpers come from tools/images/make_images.py; Twemoji SVGs are downloaded into ./_twemoji_src/ (not committed)."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools', 'images')))
from PIL import ImageDraw
import make_images as MI   # reuses emoji(), row(), canvas(), save(), font()
from make_images import emoji, row, canvas, font, W, H
OUT = os.path.abspath(os.path.join(HERE, '..'))   # level1/images/
def bubble(img, x, y, w, h, text, size=60, tail='left'):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x, y, x+w, y+h), 30, outline=(30,30,30), width=6, fill='white')
    tx = x+40 if tail == 'left' else x+w-70
    d.polygon([(tx, y+h-3), (tx+34, y+h-3), (tx-6 if tail=='left' else tx+40, y+h+46)], fill='white', outline=None)
    d.line((tx, y+h-1, tx-6 if tail=='left' else tx+40, y+h+46), fill=(30,30,30), width=6)
    d.line((tx+34, y+h-1, tx-6 if tail=='left' else tx+40, y+h+46), fill=(30,30,30), width=6)
    d.text((x+w//2, y+h//2), text, font=font(size), fill=(30,30,30), anchor='mm')
def hello():
    img = canvas(); img.alpha_composite(emoji('1f642',230),(50,160)); img.alpha_composite(emoji('1f44b',150),(285,220))
    bubble(img, 300, 30, 250, 120, 'Hi!', 70); return img
def goodbye():
    img = canvas(); img.alpha_composite(emoji('1f6aa',230),(330,150)); img.alpha_composite(emoji('1f6b6',210),(120,170))
    img.alpha_composite(emoji('1f44b',110),(40,170)); bubble(img, 40, 25, 260, 110, 'Bye!', 64); return img
def nametag():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((60,60,540,360), 28, fill=(200,40,40))
    d.text((300,105),'HELLO',font=font(54),fill='white',anchor='mm'); d.text((300,150),'my name is',font=font(30),fill='white',anchor='mm')
    d.rectangle((85,180,515,335), fill='white'); d.text((300,258),'Ana',font=font(96),fill=(30,30,30),anchor='mm')
    return img
def idcard(field):
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((30,45,570,375), 26, outline=(30,30,30), width=6, fill=(235,244,252))
    d.rectangle((33,48,567,105), fill=(31,58,95)); d.text((300,77),'ID CARD',font=font(34),fill='white',anchor='mm')
    d.rounded_rectangle((55,130,205,310), 14, outline=(120,120,120), width=4, fill='white')
    img.alpha_composite(emoji('1f469',130),(65,150))
    rows = [('first','First name','ANA',150),('last','Last name','RUIZ',255)]
    for key, lab, val, y in rows:
        hl = key == field
        if hl: d.rounded_rectangle((220,y-12,555,y+88), 14, fill=(255,224,102), outline=(200,40,40), width=6)
        d.text((235,y+2),lab,font=font(26),fill=(60,60,60) if not hl else (30,30,30))
        d.text((235,y+34),val,font=font(48 if hl else 40),fill=(30,30,30) if hl else (120,120,120))
    return img
def spell():
    img = canvas(); d = ImageDraw.Draw(img); img.alpha_composite(emoji('1f5e3',170),(25,40))
    for i, ch in enumerate('ANA'):
        x = 215 + i*125; d.rounded_rectangle((x,70,x+100,190), 14, outline=(30,58,95), width=6, fill=(234,241,248))
        d.text((x+50,130), ch, font=font(80), fill=(31,58,95), anchor='mm')
    d.text((300,300),'A - N - A',font=font(78),fill=(200,40,40),anchor='mm'); return img
def letter():
    img = canvas(); img.alpha_composite(emoji('1f520',180),(60,40)); img.alpha_composite(emoji('1f524',180),(360,40))
    d = ImageDraw.Draw(img); d.text((300,320),'A  a',font=font(130),fill=(31,58,95),anchor='mm'); return img
def classmate():
    img = canvas(); d = ImageDraw.Draw(img)
    img.alpha_composite(emoji('1f9d1',170),(60,70)); img.alpha_composite(emoji('1f469',170),(370,70))
    img.alpha_composite(emoji('1f9d1-200d-1f3eb',120),(240,20))
    d.rounded_rectangle((40,285,560,320), 8, fill=(181,136,99))     # one shared table
    img.alpha_composite(emoji('1f4d6',90),(100,205)); img.alpha_composite(emoji('1f4d6',90),(410,205))
    return img
def goodbye():
    img = canvas(); img.alpha_composite(emoji('1f6aa',230),(340,150)); img.alpha_composite(emoji('1f6b6',210),(130,170))
    img.alpha_composite(emoji('1f44b',100),(60,190)); bubble(img, 30, 25, 260, 110, 'Bye!', 64); return img
B = []
def add(name, word, fn, codes, note): B.append((name, word, fn, codes, note))
add('L1_hello','hello',hello,['1f642','1f44b'],'smiling face + waving hand, speech bubble "Hi!" (drawn)')
add('L1_goodbye','goodbye',goodbye,['1f6aa','1f6b6','1f44b'],'person walking to a door + waving hand, speech bubble "Bye!" (drawn)')
add('L1_name','name',nametag,[],'"HELLO my name is Ana" name tag (drawn)')
add('L1_first_name','first name',lambda: idcard('first'),['1f469'],'ID card, FIRST NAME field highlighted (card drawn) + woman')
add('L1_last_name','last name',lambda: idcard('last'),['1f469'],'ID card, LAST NAME field highlighted (card drawn) + woman')
add('L1_spell','spell',spell,['1f5e3'],'speaking head + letter tiles A N A and "A - N - A" (drawn)')
add('L1_letter','letter (A, B, C…)',letter,['1f520','1f524'],'capital-letters + small-letters symbols, "A a" (drawn)')
add('L1_teacher','teacher',lambda: row(['1f9d1-200d-1f3eb'],300),['1f9d1-200d-1f3eb'],'teacher at a board')
add('L1_student','student',lambda: row(['1f9d1-200d-1f393','1f4dd'],250),['1f9d1-200d-1f393','1f4dd'],'student (cap) + paper and pencil')
add('L1_classmate','classmate',classmate,['1f9d1','1f469','1f9d1-200d-1f3eb','1f4d6'],'two learners side by side at one table with open books, teacher behind (table drawn)')
add('L1_book','book',lambda: row(['1f4d6','1f4d8'],250),['1f4d6','1f4d8'],'open book + closed blue book')
add('L1_pen','pen',lambda: row(['1f58a'],300),['1f58a'],'pen')
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); meta = []
    for name, word, fn, codes, note in B:
        MI.save(fn(), f'{OUT}/{name}'); meta.append(dict(file=f'{name}.png', lesson='Level1-L1', word=word, twemoji=codes, note=note))
    json.dump(meta, open(f'{OUT}/images_L1.json','w'), indent=1, ensure_ascii=False); print(len(meta),'images')
