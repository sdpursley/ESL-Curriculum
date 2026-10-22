"""Level 1, Lesson 6 vocabulary pictures (600x420 PNG cards), same card style as Lessons 1-5.
Emoji graphics: Twemoji (jdecked/twemoji), CC BY 4.0. Clock faces, week strips, OPEN/CLOSED and store-hours signs drawn in code.
Rewritten Oct 21, 2026 after the original build/ folder was removed; regenerates the approved PNGs in images/.
Run: python make_images_L1_L6.py [OUT_DIR]
"""
import os, sys, json, math
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'lib'))
from PIL import Image, ImageDraw
import make_images as MI
from make_images import emoji, canvas, font, clock as MI_clock, W, H
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(HERE, '..'))
INK = (30, 30, 30); NAVY = (31, 58, 95); RED = (200, 40, 40); GREY = (120, 120, 120)
GREEN = (20, 140, 60); YEL = (255, 224, 102)

def put(img, code, size, x, y):
    img.alpha_composite(emoji(code, size), (int(x), int(y))); return img

def digiclock(d, x, y, w, h, text, fill=(20,20,20), fg=(80,255,80)):
    d.rounded_rectangle((x, y, x+w, y+h), 10, fill=fill, outline=INK, width=3)
    d.text((x+w//2, y+h//2), text, font=font(min(40, h-16)), fill=fg, anchor='mm')

def clock_card():
    img = canvas(); put(img,'1f570',160,40,100); put(img,'23f0',100,230,80)
    digiclock(ImageDraw.Draw(img), 360, 160, 200, 90, '6:00'); return img

def face_clock(h, m, size=220):
    """drawn analog clock face centred"""
    img = Image.new('RGBA', (size, size), (0,0,0,0)); d = ImageDraw.Draw(img)
    r = size//2 - 4; cx = cy = size//2
    d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=INK, width=8, fill='white')
    for i in range(12):
        a = math.radians(i*30-90)
        d.line((cx+math.cos(a)*(r-22), cy+math.sin(a)*(r-22), cx+math.cos(a)*(r-6), cy+math.sin(a)*(r-6)), fill=INK, width=5)
    am = math.radians(m*6-90); ah = math.radians((h%12+m/60)*30-90)
    d.line((cx, cy, cx+math.cos(ah)*(r*0.55), cy+math.sin(ah)*(r*0.55)), fill=INK, width=10)
    d.line((cx, cy, cx+math.cos(am)*(r*0.8), cy+math.sin(am)*(r*0.8)), fill=INK, width=6)
    d.ellipse((cx-8, cy-8, cx+8, cy+8), fill=RED); return img

def oclock():
    img = canvas(); d = ImageDraw.Draw(img)
    fc = face_clock(9, 0, 220); img.alpha_composite(fc, (40, 80))
    put(img, '1f558', 80, 280, 40)
    digiclock(d, 360, 100, 200, 80, '9:00')
    d.text((460, 220), "nine o'clock", font=font(28), fill=NAVY, anchor='mm'); return img

def thirty():
    img = canvas(); d = ImageDraw.Draw(img)
    fc = face_clock(9, 30, 220); img.alpha_composite(fc, (40, 80))
    put(img, '1f564', 80, 280, 40)
    digiclock(d, 360, 90, 200, 80, '9:30')
    d.text((460, 210), 'nine thirty', font=font(26), fill=NAVY, anchor='mm')
    d.text((460, 250), 'half past nine', font=font(22), fill=GREY, anchor='mm'); return img

def morning():
    img = canvas(); put(img,'1f305',240,50,82); digiclock(ImageDraw.Draw(img), 360, 160, 200, 90, '7:00'); return img
def afternoon():
    img = canvas(); put(img,'2600',240,50,82); digiclock(ImageDraw.Draw(img), 360, 160, 200, 90, '3:00'); return img
def evening():
    img = canvas(); put(img,'1f303',260,42,66); digiclock(ImageDraw.Draw(img), 360, 160, 200, 90, '9:00'); return img

def day():
    img = canvas(); d = ImageDraw.Draw(img)
    put(img,'2600',140,60,80); put(img,'1f319',140,220,80)
    d.rounded_rectangle((380, 120, 560, 280), 14, fill=YEL, outline=RED, width=4)
    d.text((470, 170), 'Monday', font=font(32), fill=INK, anchor='mm')
    d.text((470, 230), '1 day', font=font(36), fill=NAVY, anchor='mm'); return img

def week_strip(highlight, title):
    img = canvas(); d = ImageDraw.Draw(img)
    d.text((300, 40), title, font=font(28), fill=NAVY, anchor='mm')
    days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']; cw = 70; x0 = (W - 7*cw)//2; y0 = 120
    for i, dd in enumerate(days):
        x = x0 + i*cw; hl = i in highlight
        d.rounded_rectangle((x+4, y0, x+cw-4, y0+160), 10, outline=INK, width=3,
                            fill=(100,160,230) if hl else 'white')
        d.text((x+cw//2, y0+50), dd, font=font(22), fill='white' if hl else INK, anchor='mm')
        d.text((x+cw//2, y0+110), str(i+1), font=font(36), fill='white' if hl else NAVY, anchor='mm')
    return img

def week(): return week_strip(range(7), '1 week = 7 days')
def weekend(): return week_strip({5,6}, 'weekend = Sat. + Sun.')

def open_sign():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((40, 100, 360, 320), 16, fill=GREEN, outline=INK, width=5)
    d.text((200, 210), 'OPEN', font=font(72), fill='white', anchor='mm')
    put(img, '1f513', 140, 434, 138); return img

def closed_sign():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((40, 100, 360, 320), 16, fill=RED, outline=INK, width=5)
    d.text((200, 210), 'CLOSED', font=font(56), fill='white', anchor='mm')
    put(img, '1f512', 140, 434, 138); return img

def days_of_week():
    img = canvas(); d = ImageDraw.Draw(img)
    put(img, '1f4c5', 120, 40, 40)
    rows = [('Mon.','Monday'),('Tue.','Tuesday'),('Wed.','Wednesday'),('Thu.','Thursday'),
            ('Fri.','Friday'),('Sat.','Saturday'),('Sun.','Sunday')]
    y = 40
    for short, full in rows:
        d.text((200, y+10), short, font=font(26), fill=GREY, anchor='lm')
        d.text((300, y+10), full, font=font(28), fill=NAVY, anchor='lm'); y += 50
    return img

def time_face(h, m):
    img = canvas(); fc = face_clock(h, m, 300); img.alpha_composite(fc, ((W-300)//2, (H-300)//2)); return img

def hours_sign():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((50, 30, 550, 390), 16, fill='white', outline=INK, width=5)
    d.rectangle((53, 33, 547, 100), fill=NAVY)
    d.text((300, 66), 'STORE HOURS', font=font(36), fill='white', anchor='mm')
    lines = [('Mon.–Fri.', '9 AM – 5 PM'), ('Saturday', '10 AM – 2 PM'), ('Sunday', 'CLOSED')]
    y = 140
    for a, b in lines:
        d.text((90, y), a, font=font(32), fill=INK, anchor='lm')
        col = RED if b == 'CLOSED' else NAVY
        d.text((510, y), b, font=font(32), fill=col, anchor='rm'); y += 70
    return img

B = []
def add(name, word, fn, codes, note, drawn='border only'):
    B.append((name, word, fn, codes, note, drawn))
add('L1_L6_clock','clock',clock_card,['1f570','23f0'],'clock + alarm clock + digital clock 6:00','digital clock + time')
add('L1_L6_oclock',"o'clock",oclock,['1f558'],'drawn clock face 9:00 + small Twemoji clock + digital 9:00 + "nine o\'clock"','drawn clock face + digital clock + text')
add('L1_L6_thirty','thirty (half past)',thirty,['1f564'],'drawn clock face 9:30 + small Twemoji clock + digital 9:30 + "nine thirty / half past nine"','drawn clock face + digital clock + text')
add('L1_L6_morning','morning',morning,['1f305'],'sunrise + 7:00','digital clock')
add('L1_L6_afternoon','afternoon',afternoon,['2600'],'sun + 3:00','digital clock')
add('L1_L6_evening','evening / night',evening,['1f303'],'night city with stars + 9:00','digital clock')
add('L1_L6_day','day',day,['2600','1f319'],'sun + moon + "Monday, 1 day"','day box + text')
add('L1_L6_week','week',week,[],'Mon-Sun strip, all 7 days highlighted (drawn)','all drawn (week strip + text)')
add('L1_L6_weekend','weekend',weekend,[],'Mon-Sun strip, Saturday and Sunday highlighted (drawn)','all drawn (week strip + text)')
add('L1_L6_open','open',open_sign,['1f513'],'green OPEN sign + open lock','sign + text')
add('L1_L6_closed','closed',closed_sign,['1f512'],'red CLOSED sign + closed lock','sign + text')
add('L1_L6_days_of_week','days of the week',days_of_week,['1f4c5'],'calendar + Monday-Sunday with short forms','list of days (text)')
add('L1_L6_time_600','clock 6:00',lambda: time_face(6,0),[],'drawn clock face showing 6:00 (Letters & Numbers)','all drawn (clock face)')
add('L1_L6_time_615','clock 6:15',lambda: time_face(6,15),[],'drawn clock face showing 6:15 (Letters & Numbers)','all drawn (clock face)')
add('L1_L6_time_630','clock 6:30',lambda: time_face(6,30),[],'drawn clock face showing 6:30 (Letters & Numbers)','all drawn (clock face)')
add('L1_L6_time_645','clock 6:45',lambda: time_face(6,45),[],'drawn clock face showing 6:45 (Letters & Numbers)','all drawn (clock face)')
add('L1_L6_hours_sign','store hours sign',hours_sign,[],'store hours sign: OPEN Mon.-Fri. 9 AM-5 PM, Sat. 10 AM-2 PM, Sun. CLOSED (drawn, invented hours)','all drawn (sign + text)')

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); meta = []
    for name, word, fn, codes, note, drawn in B:
        MI.save(fn(), f'{OUT}/{name}')
        meta.append(dict(file=f'{name}.png', lesson='Level1-L6', word=word, twemoji=codes, note=note, drawn=drawn))
    json.dump(meta, open(f'{OUT}/images_L1_L6.json', 'w'), indent=1, ensure_ascii=False)
    print(len(meta), 'images ->', OUT)
