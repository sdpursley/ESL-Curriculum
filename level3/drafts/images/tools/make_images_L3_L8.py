"""Level 3, Lesson 8 pictures: 12 vocabulary cards (600x420) + 1 activity picture (the Lost and Found box: 12 numbered items,
some almost the same). Twemoji (CC BY 4.0), some recolored, + drawings in code (l3img.py). Usage: python make_images_L3_L8.py OUT_DIR"""
import sys
from PIL import ImageDraw, ImageOps, Image
from l3img import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '..'   # default: level3/drafts/images (never level3/images, which the website publishes)
def tinted(code, size, rgb, flip=False):
    """Twemoji recolored to one color (keeps shading): grayscale -> dark..light version of rgb, same alpha."""
    e = emoji(code, size); a = e.getchannel('A'); g = ImageOps.grayscale(e.convert('RGB'))
    dark = tuple(int(c*0.35) for c in rgb); light = tuple(min(255, int(c + (255-c)*0.55)) for c in rgb)
    c = ImageOps.colorize(g, dark, light, mid=rgb).convert('RGBA'); c.putalpha(a)
    return c.transpose(Image.FLIP_LEFT_RIGHT) if flip else c
def put_t(img, code, size, x, y, rgb): img.alpha_composite(tinted(code, size, rgb), (int(x), int(y))); return img
def wallet(img, x, y, s, color=(110, 70, 40)):
    d = ImageDraw.Draw(img); w, h = int(200*s), int(130*s)
    d.rounded_rectangle((x, y, x+w, y+h), int(18*s), fill=color, outline=INK, width=max(2, int(4*s)))
    d.rounded_rectangle((x+w*0.55, y+h*0.3, x+w+int(10*s), y+h*0.7), int(10*s), fill=tuple(min(255, c+40) for c in color), outline=INK, width=max(2, int(3*s)))
    d.ellipse((x+w*0.8, y+h*0.43, x+w*0.88, y+h*0.57), fill=(230, 200, 80)); return img
def wallet_c():
    img = canvas(); wallet(img, 160, 100, 1.4); label(img, 'wallet', 372, 44); return img
def purse():
    img = canvas(); put(img, '1f45c', 240, 180, 50); label(img, 'purse', 372, 44); return img
def keys():
    img = canvas(); put(img, '1f511', 200, 120, 70); put(img, '1f511', 160, 290, 110); label(img, 'keys', 372, 44); return img
def umbrella():
    img = canvas(); put(img, '2602', 250, 175, 40); label(img, 'umbrella', 372, 44); return img
def backpack():
    img = canvas(); put(img, '1f392', 250, 175, 40); label(img, 'backpack', 372, 44); return img
def sunglasses():
    img = canvas(); put(img, '1f576', 270, 165, 30); label(img, 'sunglasses', 372, 44); return img
def headphones():
    img = canvas(); put(img, '1f3a7', 250, 175, 40); label(img, 'headphones', 372, 44); return img
def gloves():
    img = canvas(); put(img, '1f9e4', 250, 175, 40); label(img, 'gloves', 372, 44); return img
def scarf():
    img = canvas(); put(img, '1f9e3', 250, 175, 40); label(img, 'scarf', 372, 44); return img
def lost_found():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rectangle((120, 150, 480, 320), fill=(205, 160, 105), outline=INK, width=4); sign(img, 150, 200, 300, 70, 'LOST & FOUND', 34)
    put(img, '2602', 100, 130, 60); put(img, '1f392', 100, 250, 55); put(img, '1f9e3', 90, 370, 70)
    label(img, 'lost and found', 372, 42); return img
def belong_to():
    img = canvas(); put(img, '1f469', 150, 50, 110); bubble(img, 230, 30, 300, 80, "It's mine.", 36, tail='left')
    arrow(img, 220, 220, 340, 220, NAVY, 8); put(img, '1f45c', 150, 370, 140); label(img, 'belong to', 372, 44); return img
def describe():
    img = canvas(); put(img, '1f9d1', 140, 40, 150); bubble(img, 190, 20, 380, 100, "It's big and blue,\nwith a zipper.", 30, tail='left')
    put_t(img, '1f392', 130, 400, 160, (50, 110, 200)); label(img, 'describe', 372, 44); return img
def box():
    img = big_canvas(1200, 900); d = ImageDraw.Draw(img); d.rectangle((0, 0, 1200, 900), fill=(240, 228, 205))
    sign(img, 380, 20, 440, 70, 'LOST & FOUND', 40)
    cells = [lambda x, y: put_t(img, '1f392', 150, x+50, y+10, (50, 110, 200)),     # 1 big blue backpack
             lambda x, y: put_t(img, '1f392', 100, x+75, y+50, (200, 40, 40)),      # 2 small red backpack
             lambda x, y: put_t(img, '2602', 140, x+55, y+15, (40, 40, 45)),        # 3 black umbrella
             lambda x, y: put_t(img, '2602', 140, x+55, y+15, (210, 40, 40)),       # 4 red umbrella
             lambda x, y: (put(img, '1f511', 120, x+40, y+30), put(img, '2b50', 60, x+150, y+90)),   # 5 keys + star
             lambda x, y: (put(img, '1f511', 120, x+40, y+30), put(img, '2764', 60, x+150, y+90)),   # 6 keys + heart
             lambda x, y: put(img, '1f576', 160, x+45, y+5),                        # 7 sunglasses
             lambda x, y: put(img, '1f453', 160, x+45, y+5),                        # 8 glasses
             lambda x, y: wallet(img, x+50, y+50, 0.8, (40, 40, 45)),               # 9 black wallet
             lambda x, y: wallet(img, x+50, y+50, 0.8, (120, 75, 40)),              # 10 brown wallet
             lambda x, y: put(img, '1f9e3', 150, x+50, y+10),                       # 11 red scarf
             lambda x, y: put_t(img, '1f9e3', 150, x+50, y+10, (40, 150, 70))]      # 12 green scarf
    for i, f in enumerate(cells):
        x = 30 + (i % 4)*290; y = 110 + (i // 4)*260
        d.rounded_rectangle((x, y, x+270, y+240), 16, fill='white', outline=(160, 140, 110), width=3); f(x, y)
        d.ellipse((x+10, y+190, x+50, y+230), fill=NAVY); text(img, x+30, y+210, str(i+1), 24, 'white')
    return img
B = [
 ('L3_L8_wallet', 'wallet', wallet_c, 'a drawn brown wallet', 'vocab'),
 ('L3_L8_purse', 'purse', purse, 'a handbag', 'vocab'),
 ('L3_L8_keys', 'keys', keys, 'two keys', 'vocab'),
 ('L3_L8_umbrella', 'umbrella', umbrella, 'an umbrella', 'vocab'),
 ('L3_L8_backpack', 'backpack', backpack, 'a backpack', 'vocab'),
 ('L3_L8_sunglasses', 'sunglasses', sunglasses, 'sunglasses', 'vocab'),
 ('L3_L8_headphones', 'headphones', headphones, 'headphones', 'vocab'),
 ('L3_L8_gloves', 'gloves', gloves, 'gloves', 'vocab'),
 ('L3_L8_scarf', 'scarf', scarf, 'a scarf', 'vocab'),
 ('L3_L8_lost_and_found', 'lost and found', lost_found, 'a drawn box "LOST & FOUND" with an umbrella, a backpack, a scarf', 'vocab'),
 ('L3_L8_belong_to', 'belong to', belong_to, 'a woman, bubble "It\'s mine.", an arrow to a handbag (bubble drawn)', 'vocab'),
 ('L3_L8_describe', 'describe', describe, 'a person; bubble "It\'s big and blue, with a zipper."; a backpack (recolored blue)', 'vocab'),
 ('L3_L8_lost_box', 'Talk Time: the Lost and Found box', box, '12 numbered items: backpacks, umbrellas, keys, sunglasses, glasses, wallets, scarves (some emoji recolored; wallets, tiles drawn)', 'activity'),
]
if __name__ == '__main__': run(B, 8, OUT)
