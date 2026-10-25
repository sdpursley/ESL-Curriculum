"""Level 3, Lesson 5 pictures: 12 vocabulary cards (600x420) + 1 activity picture (the school flyer for Read & Write).
Twemoji (CC BY 4.0) + drawings in code (l3img.py). Usage: python make_images_L3_L5.py OUT_DIR"""
import sys
from PIL import ImageDraw
from l3img import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '..'   # default: level3/drafts/images (never level3/images, which the website publishes)
WOMAN = '1f469'; MAN = '1f9d1'; FAM = '1f468-200d-1f469-200d-1f467'
def fam(img, x, y, s):
    put(img, '1f468', s, x, y); put(img, '1f469', s, x + s*0.9, y); put(img, '1f467', int(s*0.75), x + s*1.85, y + s*0.25); return img
def offer():
    img = canvas(); put(img, '1f64b-200d-2640-fe0f', 200, 40, 120); put(img, '1f9d1', 150, 400, 170); put(img, '1f4e6', 100, 440, 60)
    bubble(img, 200, 30, 230, 80, "I'll help!", 36, tail='left'); label(img, 'offer', 372, 44); return img
def promise():
    img = canvas(); put(img, '1f91d', 190, 205, 120); bubble(img, 150, 20, 300, 80, 'I promise.', 38, tail='left')
    label(img, 'promise', 372, 44); return img
def carry():
    img = canvas(); person(img, 245, 330, MAN, size=100, shirt=(70, 120, 190)); put(img, '1f4e6', 130, 230, 150)
    label(img, 'carry', 372, 44); return img
def set_up():
    img = canvas(); d = ImageDraw.Draw(img)
    for k in range(3): put(img, '1fa91', 70, 40, 60 + k*30)                     # stacked chairs
    arrow(img, 150, 170, 230, 170, NAVY, 8)
    d.rectangle((300, 200, 540, 214), fill=(150, 100, 60)); d.line((315, 214, 315, 300), fill=(150, 100, 60), width=10); d.line((525, 214, 525, 300), fill=(150, 100, 60), width=10)
    for x in (250, 380, 500): put(img, '1fa91', 90, x - 20, 210)
    label(img, 'set up', 372, 44); return img
def clean_up():
    img = canvas(); put(img, '1f9f9', 170, 90, 120); put(img, '1f5d1', 150, 330, 150); put(img, '2728', 70, 480, 60)
    label(img, 'clean up', 372, 44); return img
def bring():
    img = canvas(); person(img, 90, 330, WOMAN, size=100, shirt=(200, 80, 90)); put(img, '1f355', 90, 160, 150)
    arrow(img, 290, 200, 380, 200, NAVY, 8); put(img, '1f3eb', 170, 400, 110); label(img, 'bring', 372, 44); return img
def lend():
    img = canvas(); put(img, MAN, 140, 40, 120); put(img, WOMAN, 140, 420, 120); put(img, '1f527', 90, 255, 70)
    arrow(img, 200, 200, 400, 200, NAVY, 8); label(img, 'lend', 352, 44); label(img, '(give for a short time)', 398, 26, GREY); return img
def give_a_ride():
    img = canvas(); put(img, '1f697', 250, 40, 70); put(img, MAN, 46, 175, 150); put(img, WOMAN, 46, 125, 150)
    arrow(img, 320, 220, 400, 220, NAVY, 8); put(img, '1f3e2', 150, 420, 130); label(img, 'give (someone) a ride', 372, 36); return img
def call_back():
    img = canvas(); put(img, '1f4f1', 160, 60, 110); bubble(img, 250, 60, 310, 110, "I'll call\nyou back.", 36, tail='left')
    label(img, 'call back', 372, 44); return img
def text_msg():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((200, 30, 400, 330), 28, fill=INK); d.rounded_rectangle((214, 60, 386, 300), 10, fill='white')
    d.rounded_rectangle((224, 90, 376, 150), 16, fill=(60, 140, 240)); text(img, 300, 120, 'Hi Rosa!', 24, 'white')
    d.rounded_rectangle((224, 165, 376, 255), 16, fill=(225, 228, 232)); text(img, 300, 210, "I'll bring\nthe drinks.", 22, INK)
    label(img, 'text', 372, 44)
    return img
def school_event():
    img = canvas(); put(img, '1f3eb', 200, 200, 40); put(img, '1f388', 90, 70, 60); put(img, '1f388', 80, 450, 70)
    fam(img, 40, 240, 80); put(img, '1f355', 70, 470, 240); label(img, 'school event', 372, 44); return img
def flyer_card():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rectangle((170, 20, 430, 330), fill=(255, 248, 225), outline=INK, width=4)
    sign(img, 185, 35, 230, 60, 'FAMILY\nNIGHT', 26, (200, 60, 60)); text(img, 300, 130, 'Friday 6:00', 26, INK)
    fam(img, 205, 170, 70); text(img, 300, 290, 'Everyone welcome!', 18, NAVY)
    label(img, 'flyer', 372, 44); return img
def flyer_big():
    img = big_canvas(1000, 760); d = ImageDraw.Draw(img)
    d.rectangle((30, 30, 970, 730), fill=(255, 248, 225), outline=NAVY, width=6)
    sign(img, 60, 60, 880, 120, 'Hillside School\nFAMILY NIGHT', 46, (200, 60, 60))
    fam(img, 385, 568, 88); put(img, '1f355', 110, 820, 560); put(img, '1f388', 100, 80, 200); put(img, '1f388', 100, 820, 200)
    for k, t in enumerate(['Friday, October 16', '6:00 to 8:00 p.m.', 'School gym, 240 Hill Road']): text(img, 500, 250 + k*58, t, 40, INK)
    for k, t in enumerate(['Games  •  Music  •  Pizza', 'Free for all families']): text(img, 500, 470 + k*58, t, 38, NAVY)
    text(img, 500, 690, 'Can you help? Call Carmen: 555-0186', 32, (200, 60, 60)); return img
B = [
 ('L3_L5_offer', 'offer', offer, 'a woman raising her hand, a man with a box; bubble "I\'ll help!" (bubble drawn)', 'vocab'),
 ('L3_L5_promise', 'promise', promise, 'a handshake; bubble "I promise." (bubble drawn)', 'vocab'),
 ('L3_L5_carry', 'carry', carry, 'a person (drawn body) carrying a box', 'vocab'),
 ('L3_L5_set_up', 'set up', set_up, 'stacked chairs, an arrow, chairs around a table (table drawn)', 'vocab'),
 ('L3_L5_clean_up', 'clean up', clean_up, 'a broom, a wastebasket, sparkles', 'vocab'),
 ('L3_L5_bring', 'bring', bring, 'a woman (drawn body) with a pizza, an arrow to a school', 'vocab'),
 ('L3_L5_lend', 'lend', lend, 'a man gives a wrench to a woman (arrow drawn), label "give for a short time"', 'vocab'),
 ('L3_L5_give_a_ride', 'give a ride', give_a_ride, 'a car with two people, an arrow to a building', 'vocab'),
 ('L3_L5_call_back', 'call back', call_back, 'a phone; bubble "I\'ll call you back." (bubble drawn)', 'vocab'),
 ('L3_L5_text', 'text', text_msg, 'a drawn phone with two text messages', 'vocab'),
 ('L3_L5_school_event', 'school event', school_event, 'a school, balloons, a family, pizza', 'vocab'),
 ('L3_L5_flyer', 'flyer', flyer_card, 'a drawn paper flyer "FAMILY NIGHT Friday 6:00" with a family', 'vocab'),
 ('L3_L5_family_night_flyer', 'Read & Write: the school flyer', flyer_big, 'a drawn flyer for a school family night with a family, pizza, balloons (flyer, text drawn)', 'activity'),
]
if __name__ == '__main__': run(B, 5, OUT)
