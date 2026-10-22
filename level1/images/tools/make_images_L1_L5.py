"""Level 1, Lesson 5 vocabulary pictures (600x420 PNG cards), same card style as Lessons 1-4.
Emoji graphics: Twemoji (jdecked/twemoji), CC BY 4.0. Register screen, wall paint, workplace signs and labels drawn in code.
Jobs and workplaces are invented for practice (no real store names).
Rewritten Oct 21, 2026 after the original build/ folder was removed; regenerates the approved PNGs in images/.
Run: python make_images_L1_L5.py [OUT_DIR]
  Default OUT_DIR is level1/images/ (run from level1/images/tools/). Pass a temp folder to compare without overwriting.
"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'lib'))
from PIL import ImageDraw
import make_images as MI
from make_images import emoji, canvas, font, W, H
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(HERE, '..'))
INK = (30, 30, 30); NAVY = (31, 58, 95); RED = (200, 40, 40); GREY = (120, 120, 120)

def put(img, code, size, x, y):
    img.alpha_composite(emoji(code, size), (x, y)); return img

def cook():
    img = canvas(); put(img, '1f9d1-200d-1f373', 248, 88, 96); put(img, '1f373', 150, 362, 195); return img
def cleaner():
    img = canvas(); put(img,'1f9d1',200,40,110); put(img,'1f9f9',150,260,140); put(img,'1faa3',140,420,160); return img
def construction():
    img = canvas(); put(img,'1f477',230,50,90); put(img,'1f3d7',200,320,120); return img
def cashier():
    img = canvas(); put(img,'1f9d1',200,103,123); put(img,'1f6d2',180,332,154)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((360, 40, 560, 115), 12, fill=(20,20,20), outline=INK, width=3)
    d.text((460, 78), '$12.50', font=font(40), fill=(80,255,80), anchor='mm'); return img
def driver():
    img = canvas(); put(img,'1f9d1',200,40,110); put(img,'1f69a',220,280,100); return img
def mechanic():
    img = canvas(); put(img,'1f9d1-200d-1f527',230,50,90); put(img,'1f697',200,320,130); return img
def server():
    img = canvas(); put(img,'1f9d1',200,40,110); put(img,'1f37d',140,270,150); put(img,'2615',120,430,160); return img
def nurse():
    img = canvas(); put(img,'1f9d1-200d-2695-fe0f',230,60,90); put(img,'1fa7a',160,340,140); return img
def painter():
    img = canvas(); put(img,'1f9d1',200,40,110); put(img,'1faa3',140,250,180); put(img,'1f58c',130,380,100)
    d = ImageDraw.Draw(img)
    d.rectangle((500, 50, 575, 360), fill=(240,240,240), outline=GREY, width=3)
    d.rectangle((500, 50, 575, 220), fill=(70,150,220)); return img
def factory():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((150, 30, 450, 100), 12, fill=NAVY, outline=INK, width=3)
    d.text((300, 65), 'FACTORY', font=font(40), fill='white', anchor='mm')
    put(img, '1f3ed', 260, 169, 120); return img
def office():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((150, 25, 450, 95), 12, fill=NAVY, outline=INK, width=3)
    d.text((300, 60), 'OFFICE', font=font(40), fill='white', anchor='mm')
    put(img,'1f5a5',180,55,132); put(img,'1f4bc',120,279,191); put(img,'1f4cb',120,435,200); return img
def restaurant():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((100, 25, 500, 95), 12, fill=NAVY, outline=INK, width=3)
    d.text((300, 60), 'RESTAURANT', font=font(34), fill='white', anchor='mm')
    put(img,'1f32e',140,60,150); put(img,'1f37d',140,230,150); put(img,'1f964',140,400,150); return img
def student():
    img = canvas(); put(img,'1f9d1',200,40,110); put(img,'1f4da',150,270,140); put(img,'270f',120,440,160); return img
def homemaker():
    img = canvas(); put(img,'1f9d1',200,40,110); put(img,'1f3e0',180,260,120); put(img,'1f9fa',140,450,160); return img
def sign_now_hiring():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((70, 50, 530, 370), 18, fill=RED, outline=INK, width=5)
    d.text((300, 155), 'NOW', font=font(72), fill='white', anchor='mm')
    d.text((300, 235), 'HIRING', font=font(72), fill='white', anchor='mm')
    d.text((300, 320), 'Cooks  •  Cashiers', font=font(28), fill='white', anchor='mm'); return img
def sign_employees_only():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((80, 70, 520, 350), 16, fill=NAVY, outline=INK, width=5)
    d.text((300, 175), 'EMPLOYEES', font=font(48), fill='white', anchor='mm')
    d.text((300, 255), 'ONLY', font=font(48), fill='white', anchor='mm'); return img

B = []
def add(name, word, fn, codes, note, drawn='border only'):
    B.append((name, word, fn, codes, note, drawn))
add('L1_L5_cook','cook',cook,['1f9d1-200d-1f373','1f373'],'cook + frying pan')
add('L1_L5_cleaner','cleaner (housekeeper)',cleaner,['1f9d1','1f9f9','1faa3'],'person + broom + bucket')
add('L1_L5_construction_worker','construction worker',construction,['1f477','1f3d7'],'construction worker + building crane')
add('L1_L5_cashier','cashier',cashier,['1f9d1','1f6d2'],'person + shopping cart + register screen "$12.50"','register screen + price')
add('L1_L5_driver','driver',driver,['1f9d1','1f69a'],'person + delivery truck')
add('L1_L5_mechanic','mechanic',mechanic,['1f9d1-200d-1f527','1f697'],'mechanic + car')
add('L1_L5_server','server',server,['1f9d1','1f37d','2615'],'person + plate + coffee')
add('L1_L5_nurse','nurse',nurse,['1f9d1-200d-2695-fe0f','1fa7a'],'health worker + stethoscope')
add('L1_L5_painter','painter',painter,['1f9d1','1f58c','1faa3'],'person + paintbrush + paint can + half-painted wall','wall + paint stripe')
add('L1_L5_factory','factory',factory,['1f3ed'],'factory + sign FACTORY','sign + text')
add('L1_L5_office','office',office,['1f5a5','1f4bc','1f4cb'],'computer + briefcase + clipboard + sign OFFICE','sign + text')
add('L1_L5_restaurant','restaurant',restaurant,['1f32e','1f37d','1f964'],'taco + plate + drink + sign RESTAURANT','sign + text')
add('L1_L5_student','student',student,['1f9d1','1f4da','270f'],'person + books + pencil')
add('L1_L5_homemaker','homemaker',homemaker,['1f9d1','1f3e0','1f9fa'],'person + house + laundry basket')
add('L1_L5_sign_now_hiring','sign: NOW HIRING',sign_now_hiring,[],'store window sign NOW HIRING (drawn)','all drawn (sign + text)')
add('L1_L5_sign_employees_only','sign: EMPLOYEES ONLY',sign_employees_only,[],'door sign EMPLOYEES ONLY (drawn)','all drawn (sign + text)')

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); meta = []
    for name, word, fn, codes, note, drawn in B:
        MI.save(fn(), f'{OUT}/{name}')
        meta.append(dict(file=f'{name}.png', lesson='Level1-L5', word=word, twemoji=codes, note=note, drawn=drawn))
    json.dump(meta, open(f'{OUT}/images_L1_L5.json', 'w'), indent=1, ensure_ascii=False)
    print(len(meta), 'images ->', OUT)
