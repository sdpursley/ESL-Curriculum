"""Level 3, Lesson 10 pictures: 12 vocabulary cards (600x420) + 1 activity picture (four jumbled 4-step strips for Teach Me in Four Steps).
Twemoji (CC BY 4.0), a few recolored, + drawings in code (l3img.py). Usage: python make_images_L3_L10.py OUT_DIR"""
import sys
from PIL import ImageDraw, ImageOps, Image
from l3img import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '..'   # default: level3/drafts/images (never level3/images, which the website publishes)
def tinted(code, size, rgb):
    e = emoji(code, size); a = e.getchannel('A'); g = ImageOps.grayscale(e.convert('RGB'))
    dark = tuple(int(c*0.35) for c in rgb); light = tuple(min(255, int(c + (255-c)*0.55)) for c in rgb)
    c = ImageOps.colorize(g, dark, light, mid=rgb).convert('RGBA'); c.putalpha(a); return c
def put_t(img, code, size, x, y, rgb): img.alpha_composite(tinted(code, size, rgb), (int(x), int(y))); return img
def button(img, x, y, w, h, t, size=30, fill=GREEN):
    d = ImageDraw.Draw(img); d.rounded_rectangle((x, y, x+w, y+h), h//2, fill=fill, outline=INK, width=4); text(img, x+w/2, y+h/2, t, size, 'white'); return img
def outlet(img, x, y, s=1.0):
    d = ImageDraw.Draw(img); w = int(120*s); d.rounded_rectangle((x, y, x+w, y+int(160*s)), 14, fill=(235, 235, 230), outline=INK, width=4)
    for yy in (y+int(40*s), y+int(100*s)):
        d.rectangle((x+int(35*s), yy, x+int(45*s), yy+int(25*s)), fill=INK); d.rectangle((x+int(75*s), yy, x+int(85*s), yy+int(25*s)), fill=INK)
    return img
def instructions():
    img = canvas(); form(img, 170, 25, 260, 320, 'INSTRUCTIONS', ['1. ______', '2. ______', '3. ______', '4. ______'], size=26)
    label(img, 'instructions', 372, 44); return img
def step():
    img = canvas(); d = ImageDraw.Draw(img)
    for i in range(3):
        x = 140 + i*110; y = 250 - i*70; d.rectangle((x, y, x+110, 320), fill=(120, 160, 210), outline=INK, width=4); text(img, x+55, y+30, str(i+1), 34, 'white')
    put(img, '1f6b6', 100, 262, 82); label(img, 'step', 372, 44); return img
def press():
    img = canvas(); button(img, 190, 220, 220, 90, 'START', 40); put(img, '1f447', 130, 235, 70); label(img, 'press', 372, 44); return img
def plug_in():
    img = canvas(); put(img, '1f50c', 170, 110, 90); arrow(img, 300, 175, 370, 175, NAVY, 8); outlet(img, 390, 90); label(img, 'plug in', 372, 44); return img
def turn_on_off():
    img = canvas(); put(img, '1f4a1', 150, 90, 60); text(img, 165, 250, 'ON', 40, GREEN)
    put_t(img, '1f4a1', 150, 360, 60, (150, 150, 150)); text(img, 435, 250, 'OFF', 40, RED); label(img, 'turn on / turn off', 372, 40); return img
def laundry():
    img = canvas(); put(img, '1f9fa', 200, 120, 90); put(img, '1f455', 130, 340, 70); put(img, '1f9e6', 90, 400, 190); label(img, 'laundry', 372, 44); return img
def detergent():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((220, 80, 380, 320), 24, fill=(60, 120, 200), outline=INK, width=5); d.rectangle((265, 45, 335, 85), fill=(230, 90, 40), outline=INK, width=4)
    d.rectangle((235, 150, 365, 230), fill='white', outline=INK, width=3); text(img, 300, 190, 'DETERGENT', 18, NAVY)
    put(img, '1fae7', 90, 400, 100); label(img, 'detergent', 372, 44); return img
def goggles():
    img = canvas(); put(img, '1f97d', 260, 170, 40); label(img, 'safety goggles', 372, 42); return img
def label_c():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((190, 70, 410, 330), 20, fill=(240, 150, 60), outline=INK, width=5); d.rectangle((215, 30, 385, 75), fill='white', outline=INK, width=4)
    d.rectangle((205, 120, 395, 290), fill='white', outline=INK, width=3)
    for i, t in enumerate(['Take 1 tablet', 'every 8 hours', 'with food.']): text(img, 300, 155+i*45, t, 24, INK)
    label(img, 'label', 372, 44); return img
def tablet():
    img = canvas(); put(img, '1f48a', 200, 200, 60); label(img, 'tablet', 372, 44); return img
def password():
    img = canvas(); d = ImageDraw.Draw(img); put(img, '1f512', 120, 60, 110)
    d.rounded_rectangle((200, 130, 540, 220), 12, fill='white', outline=INK, width=4); text(img, 215, 105, 'Password', 28, NAVY, 'lm')
    text(img, 370, 175, '● ● ● ● ● ●', 34, INK); label(img, 'password', 372, 44); return img
def log_in():
    img = canvas(); put(img, '1f4bb', 230, 70, 60); button(img, 330, 140, 220, 80, 'LOG IN', 34, NAVY); arrow(img, 290, 180, 325, 180, NAVY, 6)
    label(img, 'log in', 372, 44); return img
# Talk Time strips: each panel = (draw function, caption); the panels are shown in a jumbled order with letters A-D.
def p_emoji(code, s=120):
    return lambda img, x, y: put(img, code, s, x+75-s//2+15, y+15)
def p_two(c1, c2, s=95):
    return lambda img, x, y: (put(img, c1, s, x+10, y+25), put(img, c2, s, x+s+10, y+25))
def p_button(t):
    return lambda img, x, y: (button(img, x+25, y+80, 150, 60, t, 26), put(img, '1f447', 80, x+60, y+5))
STRIPS = [  # (title, panels in the RIGHT order, jumbled order shown as A B C D)
 ('1. Washing your hands at work', [(p_emoji('1f6b0'), 'water on'), (p_emoji('1f9fc'), 'soap'), (p_emoji('1f450'), 'wash 20 seconds'), (p_emoji('1f9fb'), 'dry: paper towel')], [2, 0, 3, 1]),
 ('2. Making a pot of coffee', [(p_emoji('1f4a7'), 'add water'), (p_emoji('1f944'), 'add coffee'), (p_button('START'), 'press START'), (p_emoji('2615'), 'pour a cup')], [1, 3, 0, 2]),
 ('3. Sending a photo by phone', [(p_emoji('1f4f7'), 'take a photo'), (p_emoji('1f5bc'), 'choose the photo'), (p_button('SEND'), 'press SEND'), (lambda img, x, y: check(img, x+55, y+40, 90), 'sent!')], [3, 1, 2, 0]),
 ('4. Paying at a parking machine', [(p_button('START'), 'press START'), (lambda img, x, y: sign(img, x+30, y+40, 140, 80, 'No. 12', 32), 'enter your space'), (p_emoji('1f4b3'), 'pay by card'), (p_emoji('1f9fe'), 'take the receipt')], [0, 2, 3, 1]),
]
STRIP_KEY = {s[0]: ''.join('ABCD'[s[2].index(i)] for i in range(4)) for s in STRIPS}
def strips():
    img = big_canvas(1200, 1120); d = ImageDraw.Draw(img); d.rectangle((0, 0, 1200, 1120), fill=(236, 240, 246))
    for r, (title, panels, order) in enumerate(STRIPS):
        y0 = 15 + r*275; text(img, 30, y0+22, title, 32, NAVY, 'lm')
        for j, k in enumerate(order):
            x = 30 + j*290; y = y0+50; f, cap = panels[k]
            d.rounded_rectangle((x, y, x+270, y+215), 16, fill='white', outline=(150, 160, 180), width=3); f(img, x+35, y)
            text(img, x+135, y+185, cap, 24, INK)
            d.ellipse((x+8, y+8, x+52, y+52), fill=NAVY); text(img, x+30, y+30, 'ABCD'[j], 26, 'white')
    return img
B = [
 ('L3_L10_instructions', 'instructions', instructions, 'a drawn instructions sheet with steps 1-4', 'vocab'),
 ('L3_L10_step', 'step', step, 'drawn stairs numbered 1-3 and a person walking', 'vocab'),
 ('L3_L10_press', 'press', press, 'a finger pointing down at a drawn START button', 'vocab'),
 ('L3_L10_plug_in', 'plug in', plug_in, 'a plug, an arrow, a drawn wall outlet', 'vocab'),
 ('L3_L10_turn_on_off', 'turn on / turn off', turn_on_off, 'a light bulb (ON) and the same bulb recolored grey (OFF)', 'vocab'),
 ('L3_L10_laundry', 'laundry', laundry, 'a basket, a shirt, socks', 'vocab'),
 ('L3_L10_detergent', 'detergent', detergent, 'a drawn detergent bottle "DETERGENT" and bubbles', 'vocab'),
 ('L3_L10_safety_goggles', 'safety goggles', goggles, 'goggles', 'vocab'),
 ('L3_L10_label', 'label', label_c, 'a drawn medicine bottle with a label "Take 1 tablet every 8 hours with food."', 'vocab'),
 ('L3_L10_tablet', 'tablet (medicine)', tablet, 'a pill', 'vocab'),
 ('L3_L10_password', 'password', password, 'a lock and a drawn password box', 'vocab'),
 ('L3_L10_log_in', 'log in', log_in, 'a laptop, an arrow, a drawn LOG IN button', 'vocab'),
 ('L3_L10_strips', 'Talk Time: four jumbled step strips', strips, 'four rows of four lettered panels: faucet, soap, open hands, paper towel; water drop, spoon, START button, coffee; camera, framed picture, SEND button, check; START button, space-number sign, card, receipt (buttons, signs, panels drawn)', 'activity'),
]
if __name__ == '__main__':
    run(B, 10, OUT); print('strip key (right order as letters):', STRIP_KEY)
