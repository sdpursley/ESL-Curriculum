"""Level 1, Lesson 3 vocabulary pictures (600x420 PNG cards), same card style as Lessons 1-2.
Emoji graphics: Twemoji (jdecked/twemoji), CC BY 4.0. Forms, signs, cards, number tiles and labels drawn in code.
All numbers and addresses on the cards are invented (practice phone numbers start with 555-01).
Run: python make_images_L1_L3.py  -> writes PNGs + images_L1_L3.json into level1/images/ (run it from level1/images/tools/)"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'lib'))   # level1/images/tools/lib: picture helpers (make_images.py, from tools/images/make_images.py)
from PIL import ImageDraw
import make_images as MI
from make_images import emoji, row, canvas, font, W, H
OUT = os.path.abspath(os.path.join(HERE, '..'))   # level1/images/
INK = (30, 30, 30); NAVY = (31, 58, 95); RED = (200, 40, 40); YEL = (255, 224, 102); GREY = (120, 120, 120)
def phone():
    img = canvas(); img.alpha_composite(emoji('1f4f1', 260), (20, 80)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((280, 140, 585, 280), 18, fill=YEL, outline=RED, width=5)
    d.text((432, 210), '555-0142', font=font(52), fill=INK, anchor='mm'); return img
def address():
    img = canvas(); img.alpha_composite(emoji('1f3e0', 250), (25, 110)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((290, 120, 585, 300), 16, fill='white', outline=INK, width=5)
    d.text((437, 175), '210', font=font(64), fill=NAVY, anchor='mm'); d.text((437, 250), 'Pine Street', font=font(40), fill=NAVY, anchor='mm'); return img
def street():
    img = canvas(); img.alpha_composite(emoji('1f6e3', 300), (20, 90)); d = ImageDraw.Draw(img)
    d.rectangle((420, 230, 432, 400), fill=GREY)
    d.rounded_rectangle((320, 120, 585, 230), 12, fill=(20, 110, 60), outline='white', width=5)
    d.text((452, 175), 'Pine St', font=font(54), fill='white', anchor='mm'); return img
def apartment():
    img = canvas(); img.alpha_composite(emoji('1f3e2', 300), (30, 60)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((350, 140, 580, 280), 16, fill='white', outline=INK, width=5)
    d.text((465, 190), 'Apt. 3', font=font(56), fill=NAVY, anchor='mm'); d.text((465, 250), 'apartment', font=font(28), fill=GREY, anchor='mm'); return img
def form_card(rows, hl=None, title='FORM', big=None):
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((40, 25, 560, 395), 14, fill='white', outline=INK, width=5)
    d.rectangle((43, 28, 557, 80), fill=NAVY); d.text((300, 54), title, font=font(34), fill='white', anchor='mm')
    y = 100; step = (380 - y) // len(rows)
    for lab, val in rows:
        h = lab == hl
        if h: d.rounded_rectangle((55, y-6, 545, y+step-10), 10, fill=YEL, outline=RED, width=5)
        d.text((70, y + (step-16)//2), lab, font=font(28 if not h else 32), fill=INK if h else GREY, anchor='lm')
        d.line((250, y+step-22, 530, y+step-22), fill=(160, 160, 160), width=3)
        d.text((260, y + (step-16)//2), val, font=font(30 if not h else 36), fill=NAVY, anchor='lm')
        y += step
    return img
def city():
    return form_card([('Address', '210 Pine St.'), ('City', 'Riverside'), ('ZIP code', '54107')], 'City', 'ADDRESS')
def zipcode():
    img = canvas(); img.alpha_composite(emoji('2709', 250), (25, 90)); d = ImageDraw.Draw(img)
    d.rounded_rectangle((300, 130, 585, 290), 16, fill=YEL, outline=RED, width=5)
    d.text((442, 175), 'ZIP code', font=font(34), fill=INK, anchor='mm'); d.text((442, 240), '54107', font=font(64), fill=NAVY, anchor='mm'); return img
def email():
    img = canvas(); img.alpha_composite(emoji('1f4e7', 230), (185, 20)); d = ImageDraw.Draw(img)
    d.text((300, 335), 'ana@mail.com', font=font(56), fill=NAVY, anchor='mm'); return img
def form():
    img = form_card([('First name', 'ANA'), ('Last name', 'RUIZ'), ('Phone', '555-0142'), ('City', 'RIVERSIDE')], None, 'FORM')
    img.alpha_composite(emoji('270f', 110), (470, 290)); return img
def signature():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((40, 60, 560, 360), 14, fill='white', outline=INK, width=5)
    d.text((70, 110), 'Signature:', font=font(36), fill=INK, anchor='lm'); d.line((70, 290, 530, 290), fill=INK, width=4)
    from PIL import ImageFont   # handwriting: Dancing Script font (SIL Open Font License)
    hand = ImageFont.truetype('/usr/share/fonts/truetype/sand-box/google/Dancing Script/DancingScript-VariableFont_wght.ttf', 96)
    d.text((95, 280), 'Ana Ruiz', font=hand, fill=(20, 60, 160), anchor='ls')
    img.alpha_composite(emoji('1f58a', 120), (430, 140)); return img
def idcard():
    img = canvas(); img.alpha_composite(emoji('1faaa', 300), (150, 40)); d = ImageDraw.Draw(img)
    d.text((300, 375), 'ID', font=font(54), fill=NAVY, anchor='mm'); return img
def zero():
    img = canvas(); d = ImageDraw.Draw(img)
    d.text((140, 200), '0', font=font(230), fill=NAVY, anchor='mm')
    d.text((420, 140), '"zero"', font=font(62), fill=INK, anchor='mm'); d.text((420, 255), '"oh"', font=font(62), fill=RED, anchor='mm')
    return img
def numbers():
    img = canvas(); d = ImageDraw.Draw(img)
    for i, n in enumerate(['21', '30', '45', '50', '78', '100']):
        x = 40 + (i % 3)*180; y = 40 + (i//3)*180
        d.rounded_rectangle((x, y, x+160, y+150), 16, fill=(234, 241, 248), outline=NAVY, width=5)
        d.text((x+80, y+75), n, font=font(70 if n != '100' else 58), fill=NAVY, anchor='mm')
    return img
B = []
def add(name, word, fn, codes, note, drawn='border only'): B.append((name, word, fn, codes, note, drawn))
add('L1_L3_phone_number', 'phone number', phone, ['1f4f1'], 'mobile phone + the practice number 555-0142', 'number label')
add('L1_L3_address', 'address', address, ['1f3e0'], 'house + address sign "210 Pine Street"', 'address sign + text')
add('L1_L3_street', 'street', street, ['1f6e3'], 'road + green street sign "Pine St"', 'street sign + text')
add('L1_L3_apartment', 'apartment (Apt.)', apartment, ['1f3e2'], 'building + door sign "Apt. 3"', 'door sign + text')
add('L1_L3_city', 'city (on a form)', city, [], 'address form, CITY line highlighted (drawn)', 'whole form (drawn) + text')
add('L1_L3_zip_code', 'ZIP code', zipcode, ['2709'], 'envelope + "ZIP code 54107" label', 'label + text')
add('L1_L3_email', 'email', email, ['1f4e7'], 'e-mail envelope + "ana@mail.com"', 'text')
add('L1_L3_form', 'form', form, ['270f'], 'simple form with first name, last name, phone, city filled in + pencil', 'whole form (drawn) + text')
add('L1_L3_signature', 'signature', signature, ['1f58a'], 'signature line with the handwritten name "Ana Ruiz" + pen', 'signature box, line, handwritten name (Dancing Script font, SIL OFL)')
add('L1_L3_id_card', 'ID card', idcard, ['1faaa'], 'identification card + "ID" label', 'text label')
add('L1_L3_zero', 'zero ("oh")', zero, [], 'big 0 with "zero" and "oh" (drawn)', 'all drawn (text)')
add('L1_L3_numbers', 'numbers 21–100', numbers, [], 'number tiles 21, 30, 45, 50, 78, 100 (drawn)', 'all drawn (tiles + text)')
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); meta = []
    for name, word, fn, codes, note, drawn in B:
        MI.save(fn(), f'{OUT}/{name}'); meta.append(dict(file=f'{name}.png', lesson='Level1-L3', word=word, twemoji=codes, note=note, drawn=drawn))
    json.dump(meta, open(f'{OUT}/images_L1_L3.json', 'w'), indent=1, ensure_ascii=False); print(len(meta), 'images')
