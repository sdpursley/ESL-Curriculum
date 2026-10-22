"""Level 1 exam pictures (Midterm Week 8, Final Week 15).
Twemoji graphics (jdecked/twemoji, CC BY 4.0) resized and combined on white cards, plus original drawings made in code
(clock faces, practice ID cards, price tags). Same card style as the Level 1 lessons (600x420, grey rounded border).
No text on a picture gives away a test answer. Usage: python3 make_exam_images.py [OUT_DIR]   (default ../../images)"""
import os, sys, json, math
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'images', 'tools', 'lib')))   # make_images.py: the Level 1 lesson picture helpers
from PIL import Image, ImageDraw
import make_images as MI
from make_images import emoji, canvas, font, W, H
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(HERE, '..', '..', 'images'))
INK = (30, 30, 30); NAVY = (31, 58, 95); GREY = (110, 110, 110); RED = (200, 40, 40); BLUE = (210, 230, 250)

def one(code, size=280):
    img = canvas(); img.alpha_composite(emoji(code, size), ((W-size)//2, (H-size)//2)); return img
def many(codes, size=None, gap=20):
    return MI.row(codes, size=size, gap=gap)
def big_small(big, smalls, bs=250, ss=130):
    """one big person with a light-blue circle + small people beside (same idea as the Lesson 4 family cards)"""
    img = canvas(); d = ImageDraw.Draw(img)
    tot = bs + 30 + ss; x = (W - tot)//2; y = (H - bs)//2
    d.ellipse((x-15, y-15, x+bs+15, y+bs+15), fill=BLUE)
    img.alpha_composite(emoji(big, bs), (x, y))
    yy = (H - len(smalls)*ss - (len(smalls)-1)*10)//2
    for c in smalls:
        img.alpha_composite(emoji(c, ss), (x+bs+30, yy)); yy += ss + 10
    return img
def clock(h, m):
    img = canvas(); d = ImageDraw.Draw(img); cx, cy, r = W//2, H//2, 180
    d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=INK, width=10, fill='white')
    for i in range(12):
        a = math.radians(i*30-90); w = 9 if i % 3 == 0 else 5
        d.line((cx+math.cos(a)*(r-34), cy+math.sin(a)*(r-34), cx+math.cos(a)*(r-10), cy+math.sin(a)*(r-10)), fill=INK, width=w)
    for n in (12, 3, 6, 9):
        a = math.radians(n*30-90); d.text((cx+math.cos(a)*(r-62), cy+math.sin(a)*(r-62)), str(n), font=font(34), fill=INK, anchor='mm')
    am = math.radians(m*6-90); ah = math.radians((h % 12 + m/60)*30-90)
    d.line((cx, cy, cx+math.cos(ah)*92, cy+math.sin(ah)*92), fill=INK, width=16)
    d.line((cx, cy, cx+math.cos(am)*140, cy+math.sin(am)*140), fill=INK, width=8)
    d.ellipse((cx-13, cy-13, cx+13, cy+13), fill=RED)
    return img
def phone_digits():
    img = canvas(); d = ImageDraw.Draw(img)
    img.alpha_composite(emoji('1f4f1', 260), (50, 80))
    d.text((440, 210), '555-0123', font=font(52), fill=INK, anchor='mm'); return img
def price_tag(code, price, size=250):
    img = canvas(); d = ImageDraw.Draw(img)
    img.alpha_composite(emoji(code, size), (60, (H-size)//2))
    x0, y0, x1, y1 = 360, 140, 560, 280
    d.polygon([(x0, (y0+y1)//2), (x0+40, y0), (x1, y0), (x1, y1), (x0+40, y1)], fill=(255, 236, 150), outline=INK)
    d.line([(x0, (y0+y1)//2), (x0+40, y0), (x1, y0), (x1, y1), (x0+40, y1), (x0, (y0+y1)//2)], fill=INK, width=5)
    d.ellipse((x0+30, (y0+y1)//2-9, x0+48, (y0+y1)//2+9), outline=INK, width=4)
    d.text(((x0+x1)//2+22, (y0+y1)//2), price, font=font(58), fill=INK, anchor='mm'); return img

CW, CH = 1200, 760
def id_card(title, fields, photo, color):
    """big practice card (drawn); invented information only"""
    CH = 270 + 98*len(fields)
    img = Image.new('RGBA', (CW, CH), 'white'); d = ImageDraw.Draw(img)
    d.rounded_rectangle((20, 20, CW-20, CH-20), 36, fill=(250, 252, 255), outline=INK, width=6)
    d.rounded_rectangle((20, 20, CW-20, 130), 36, fill=color); d.rectangle((20, 90, CW-20, 130), fill=color)
    d.text((CW//2, 75), title, font=font(54), fill='white', anchor='mm')
    d.rounded_rectangle((60, 170, 340, 470), 20, fill=(225, 235, 245), outline=INK, width=4)
    img.alpha_composite(emoji(photo, 240), (80, 200))
    y = 175
    for lab, val in fields:
        d.text((390, y), lab, font=ImageFont_reg(30), fill=GREY, anchor='la')
        d.text((390, y+34), val, font=font(46), fill=INK, anchor='la'); y += 98
    d.text((CW//2, CH-60), 'PRACTICE CARD: invented information', font=ImageFont_reg(28), fill=GREY, anchor='mm')
    return img
def ImageFont_reg(n):
    from PIL import ImageFont; return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', n)
def save_big(img, name):
    d = ImageDraw.Draw(img); img.convert('RGB').save(f'{name}.png', optimize=True)

B = []
def add(n, word, fn, codes, note, drawn='border only', big=False): B.append((n, word, fn, codes, note, drawn, big))
# ---- Midterm (Lessons 1-7)
add('L1_EX_flag_mexico', 'Mexico', lambda: one('1f1f2-1f1fd'), ['1f1f2-1f1fd'], 'flag of Mexico')
add('L1_EX_flag_guatemala', 'Guatemala', lambda: one('1f1ec-1f1f9'), ['1f1ec-1f1f9'], 'flag of Guatemala')
add('L1_EX_flag_honduras', 'Honduras', lambda: one('1f1ed-1f1f3'), ['1f1ed-1f1f3'], 'flag of Honduras')
add('L1_EX_job_cook', 'cook', lambda: many(['1f9d1-200d-1f373', '1f373'], 230), ['1f9d1-200d-1f373', '1f373'], 'cook + frying pan')
add('L1_EX_job_driver', 'driver', lambda: many(['1f9d1', '1f69a'], 230), ['1f9d1', '1f69a'], 'person + delivery truck')
add('L1_EX_job_cashier', 'cashier', lambda: many(['1f9d1', '1f6d2'], 230), ['1f9d1', '1f6d2'], 'person + shopping cart')
add('L1_EX_kids_1', '1 child', lambda: many(['1f9d2'], 300), ['1f9d2'], 'one child')
add('L1_EX_kids_2', '2 children', lambda: many(['1f467', '1f466'], 250), ['1f467', '1f466'], 'two children (girl + boy)')
add('L1_EX_kids_3', '3 children', lambda: many(['1f467', '1f466', '1f9d2'], 175), ['1f467', '1f466', '1f9d2'], 'three children')
add('L1_EX_clock_600', '6:00', lambda: clock(6, 0), [], 'clock face showing 6:00 (drawn)', 'all drawn')
add('L1_EX_clock_630', '6:30', lambda: clock(6, 30), [], 'clock face showing 6:30 (drawn)', 'all drawn')
add('L1_EX_clock_730', '7:30', lambda: clock(7, 30), [], 'clock face showing 7:30 (drawn)', 'all drawn')
add('L1_EX_teacher', 'teacher', lambda: one('1f9d1-200d-1f3eb'), ['1f9d1-200d-1f3eb'], 'teacher at a board')
add('L1_EX_phone_number', 'phone number', phone_digits, ['1f4f1'], 'mobile phone + practice number 555-0123', 'number label')
add('L1_EX_daughter', 'daughter', lambda: big_small('1f467', ['1f469', '1f468']), ['1f467', '1f469', '1f468'], 'girl (big, blue circle) with her parents (small)', 'blue circle')
add('L1_EX_nurse', 'nurse', lambda: many(['1f9d1-200d-2695-fe0f', '1fa7a'], 230), ['1f9d1-200d-2695-fe0f', '1fa7a'], 'health worker + stethoscope')
add('L1_EX_morning', 'morning', lambda: one('1f305'), ['1f305'], 'sunrise (morning)')
add('L1_EX_shoes', 'shoes', lambda: one('1f45f'), ['1f45f'], 'shoes')
add('L1_EX_card_rosa', 'practice ID card', lambda: id_card('PRACTICE ID CARD', [('FIRST NAME', 'Rosa'), ('LAST NAME', 'Diaz'), ('PHONE', '555-0173'), ('ADDRESS', '48 Lake Street'), ('CITY', 'Riverside'), ('ZIP CODE', '54107')], '1f469', NAVY), ['1f469'], 'practice ID card, invented person and address (card drawn) + woman', 'card, text', True)
add('L1_EX_tag_shirt', 'shirt $15', lambda: price_tag('1f455', '$15'), ['1f455'], 'shirt + price tag $15', 'price tag')
add('L1_EX_tag_jacket', 'jacket $40', lambda: price_tag('1f9e5', '$40'), ['1f9e5'], 'jacket + price tag $40', 'price tag')
add('L1_EX_tag_shoes', 'shoes $30', lambda: price_tag('1f45f', '$30'), ['1f45f'], 'shoes + price tag $30', 'price tag')
add('L1_EX_tag_pants', 'pants $20', lambda: price_tag('1f456', '$20'), ['1f456'], 'pants + price tag $20', 'price tag')
# ---- Final (all lessons, focus 8-13)
add('L1_EX_eye', 'eye', lambda: one('1f441'), ['1f441'], 'eye')
add('L1_EX_ear', 'ear', lambda: one('1f442'), ['1f442'], 'ear')
add('L1_EX_hand', 'hand', lambda: one('270b'), ['270b'], 'raised hand')
add('L1_EX_clock_900', '9:00', lambda: clock(9, 0), [], 'clock face showing 9:00 (drawn)', 'all drawn')
add('L1_EX_clock_930', '9:30', lambda: clock(9, 30), [], 'clock face showing 9:30 (drawn)', 'all drawn')
add('L1_EX_clock_1030', '10:30', lambda: clock(10, 30), [], 'clock face showing 10:30 (drawn)', 'all drawn')
add('L1_EX_bank', 'bank', lambda: one('1f3e6'), ['1f3e6'], 'bank')
add('L1_EX_park', 'park', lambda: many(['1f333', '1f333'], 230), ['1f333'], 'two trees (park)')
add('L1_EX_school', 'school', lambda: one('1f3eb'), ['1f3eb'], 'school')
add('L1_EX_sunny', 'sunny', lambda: one('2600'), ['2600'], 'sun')
add('L1_EX_rainy', 'rainy', lambda: one('1f327'), ['1f327'], 'cloud with rain')
add('L1_EX_hot', 'hot', lambda: one('1f975'), ['1f975'], 'hot face')
add('L1_EX_taco', 'taco', lambda: one('1f32e'), ['1f32e'], 'taco')
add('L1_EX_juice', 'juice', lambda: one('1f9c3'), ['1f9c3'], 'juice box')
add('L1_EX_pizza', 'pizza', lambda: one('1f355'), ['1f355'], 'pizza')
add('L1_EX_drive', 'drive', lambda: one('1f697'), ['1f697'], 'car (drive)')
add('L1_EX_fish', 'fish', lambda: one('1f41f'), ['1f41f'], 'fish')
add('L1_EX_birthday', 'birthday', lambda: many(['1f382', '1f388'], 230), ['1f382', '1f388'], 'cake + balloon')
add('L1_EX_bed', 'bed', lambda: one('1f6cf'), ['1f6cf'], 'bed')
add('L1_EX_pharmacy', 'pharmacy', lambda: many(['1f3ea', '1f48a'], 230), ['1f3ea', '1f48a'], 'store building + pill (pharmacy)')
add('L1_EX_foot', 'foot', lambda: one('1f9b6'), ['1f9b6'], 'foot')
add('L1_EX_swim', 'swim', lambda: one('1f3ca'), ['1f3ca'], 'swimmer')
add('L1_EX_card_carlos', 'practice information card', lambda: id_card('PRACTICE CARD', [('NAME', 'Carlos Vega'), ('ADDRESS', '35 Oak Street'), ('PHONE', '555-0157'), ('DATE OF BIRTH', '07/14/1990'), ('DAYS I CAN WORK', 'Monday, Wednesday, Friday'), ('SKILLS', 'I can cook. I can drive.')], '1f468', (27, 111, 122)), ['1f468'], 'practice information card, invented person (card drawn) + man', 'card, text', True)
add('L1_EX_skill_drive', 'drive', lambda: one('1f697'), ['1f697'], 'car (drive)')
add('L1_EX_skill_cook', 'cook', lambda: one('1f9d1-200d-1f373'), ['1f9d1-200d-1f373'], 'cook')
add('L1_EX_skill_clean', 'clean', lambda: one('1f9f9'), ['1f9f9'], 'broom (clean)')
add('L1_EX_skill_computer', 'use a computer', lambda: one('1f5a5'), ['1f5a5'], 'desktop computer')

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); meta = []
    for name, word, fn, codes, note, drawn, big in B:
        (save_big if big else MI.save)(fn(), f'{OUT}/{name}')
        meta.append(dict(file=f'{name}.png', word=word, twemoji=codes, note=note, drawn=drawn))
    json.dump(meta, open(f'{OUT}/images_L1_exams.json', 'w'), indent=1, ensure_ascii=False)
    print(len(meta), 'images')
