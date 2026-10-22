"""Level 1, Lesson 2 vocabulary pictures (600x420 PNG cards), same card style as Lesson 1 and Level 2.
Emoji graphics: Twemoji (jdecked/twemoji), CC BY 4.0. Labels and arrows drawn in code.
Run: python make_images_L1_L2.py  -> writes PNGs + images_L1_L2.json into level1/images/ (run it from level1/images/tools/)"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'lib'))   # level1/images/tools/lib: picture helpers (make_images.py, from tools/images/make_images.py)
from PIL import ImageDraw
import make_images as MI
from make_images import emoji, row, canvas, font, W, H
OUT = os.path.abspath(os.path.join(HERE, '..'))   # level1/images/
INK = (30, 30, 30); NAVY = (31, 58, 95); RED = (200, 40, 40)
def label(img, text, y=395, size=44, color=NAVY):
    ImageDraw.Draw(img).text((W//2, y), text, font=font(size), fill=color, anchor='mb'); return img
def flag(code):
    img = canvas(); img.alpha_composite(emoji(code, 330), ((W-330)//2, (H-330)//2)); return img
def country():
    img = canvas(); img.alpha_composite(emoji('1f5fa', 250), (175, 10))
    for i, c in enumerate(['1f1f2-1f1fd', '1f1ec-1f1f9', '1f1fa-1f1f8']):
        img.alpha_composite(emoji(c, 130), (95 + i*150, 265))
    return img
def city():
    img = canvas(); img.alpha_composite(emoji('1f3d9', 300), (40, 60)); img.alpha_composite(emoji('1f3e2', 200), (350, 160)); return img
def person(codes, word, size=230):
    img = row(codes, size, y=40); return label(img, word, 400, 70, RED)
def how_old():
    img = canvas(); img.alpha_composite(emoji('1f382', 260), (60, 70)); img.alpha_composite(emoji('2753', 200), (340, 100)); return img
B = []
def add(name, word, fn, codes, note, drawn='border only'): B.append((name, word, fn, codes, note, drawn))
add('L1_L2_country', 'country', country, ['1f5fa', '1f1f2-1f1fd', '1f1ec-1f1f9', '1f1fa-1f1f8'], 'world map + three flags (Mexico, Guatemala, United States)')
add('L1_L2_city', 'city', city, ['1f3d9', '1f3e2'], 'city buildings + office building')
add('L1_L2_mexico', 'Mexico', lambda: flag('1f1f2-1f1fd'), ['1f1f2-1f1fd'], 'flag of Mexico')
add('L1_L2_guatemala', 'Guatemala', lambda: flag('1f1ec-1f1f9'), ['1f1ec-1f1f9'], 'flag of Guatemala')
add('L1_L2_honduras', 'Honduras', lambda: flag('1f1ed-1f1f3'), ['1f1ed-1f1f3'], 'flag of Honduras')
add('L1_L2_el_salvador', 'El Salvador', lambda: flag('1f1f8-1f1fb'), ['1f1f8-1f1fb'], 'flag of El Salvador')
add('L1_L2_colombia', 'Colombia', lambda: flag('1f1e8-1f1f4'), ['1f1e8-1f1f4'], 'flag of Colombia')
add('L1_L2_united_states', 'the United States', lambda: flag('1f1fa-1f1f8'), ['1f1fa-1f1f8'], 'flag of the United States')
add('L1_L2_he', 'he', lambda: person(['1f468'], 'he', 280), ['1f468'], 'man + the word "he" (drawn label)', 'text label "he"')
add('L1_L2_she', 'she', lambda: person(['1f469'], 'she', 280), ['1f469'], 'woman + the word "she" (drawn label)', 'text label "she"')
add('L1_L2_they', 'they', lambda: person(['1f468', '1f469', '1f9d1'], 'they', 170), ['1f468', '1f469', '1f9d1'], 'man, woman, person + the word "they" (drawn label)', 'text label "they"')
add('L1_L2_how_old', 'How old?', how_old, ['1f382', '2753'], 'birthday cake + question mark')
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); meta = []
    for name, word, fn, codes, note, drawn in B:
        MI.save(fn(), f'{OUT}/{name}'); meta.append(dict(file=f'{name}.png', lesson='Level1-L2', word=word, twemoji=codes, note=note, drawn=drawn))
    json.dump(meta, open(f'{OUT}/images_L1_L2.json', 'w'), indent=1, ensure_ascii=False); print(len(meta), 'images')
