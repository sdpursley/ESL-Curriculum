"""Level 3, Lesson 13 pictures: 12 vocabulary cards (600x420) + 1 activity picture (the Goal Ladder).
Twemoji (CC BY 4.0) + drawings in code (l3img.py). Usage: python make_images_L3_L13.py OUT_DIR"""
import sys
from PIL import ImageDraw
from l3img import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '..'   # default: level3/drafts/images (never level3/images, which the website publishes)
def plan():
    img = canvas(); put(img, '1f5d3', 170, 110, 80); put(img, '1f4cb', 170, 320, 80); label(img, 'plan', 372, 44); return img
def hope():
    img = canvas(); put(img, '1f9d1', 150, 90, 150); bubble(img, 260, 30, 270, 150, '', 30, tail='left'); put(img, '1f3e0', 110, 340, 50)
    put(img, '1f91e', 90, 110, 60); label(img, 'hope', 372, 44); return img
def decide():
    img = canvas(); d = ImageDraw.Draw(img); put(img, '1f9d1', 130, 60, 160)
    arrow(img, 230, 230, 420, 110, NAVY, 9); arrow(img, 230, 230, 420, 300, GREY, 9); check(img, 450, 70, 60)
    label(img, 'decide', 372, 44); return img
def diploma():
    img = canvas(); put(img, '1f4dc', 190, 110, 80); put(img, '1f393', 170, 320, 90); label(img, 'diploma', 372, 44); return img
def certificate():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rectangle((110, 50, 490, 320), fill=(255, 250, 235), outline=(180, 140, 60), width=8); text(img, 300, 105, 'CERTIFICATE', 38, NAVY)
    d.line((170, 175, 430, 175), fill=GREY, width=3); d.line((170, 215, 430, 215), fill=GREY, width=3); put(img, '1f3f5', 90, 380, 220)
    label(img, 'certificate', 372, 44); return img
def career():
    img = canvas(); put(img, '1f4bc', 160, 110, 110); put(img, '1f4c8', 190, 300, 70); label(img, 'career', 372, 44); return img
def promotion():
    img = canvas(); put(img, '1f9d1-200d-1f4bc', 170, 70, 120); arrow(img, 260, 290, 360, 130, GREEN, 12)
    sign(img, 370, 70, 190, 70, 'MANAGER', 32); label(img, 'promotion', 372, 44); return img
def save_money():
    img = canvas(); put(img, '1f4b0', 170, 90, 100); arrow(img, 280, 190, 360, 190, NAVY, 8); put(img, '1f3e6', 170, 370, 100); label(img, 'save money', 372, 44); return img
def own_business():
    img = canvas(); put(img, '1f3ea', 220, 120, 60); sign(img, 360, 140, 160, 70, 'OPEN', 38, GREEN); label(img, 'own business', 372, 44); return img
def license():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((90, 70, 510, 320), 22, fill=(225, 238, 250), outline=NAVY, width=5); d.rectangle((90, 70, 510, 125), fill=NAVY)
    text(img, 300, 98, 'DRIVER LICENSE', 30, 'white'); put(img, '1f9d1', 120, 120, 150); put(img, '1f697', 130, 330, 150)
    label(img, "driver's license", 372, 42); return img
def computer_class():
    img = canvas(); put(img, '1f9d1-200d-1f3eb', 180, 80, 80); put(img, '1f4bb', 170, 330, 120); label(img, 'computer class', 372, 42); return img
def college():
    img = canvas(); put(img, '1f3eb', 220, 120, 70); sign(img, 360, 90, 200, 90, 'COMMUNITY\nCOLLEGE', 26); label(img, 'community college', 372, 40); return img
def ladder():
    img = big_canvas(1200, 900); d = ImageDraw.Draw(img); d.rectangle((0, 0, 1200, 900), fill=(240, 244, 250))
    d.line((300, 60, 300, 860), fill=(140, 95, 55), width=22); d.line((620, 60, 620, 860), fill=(140, 95, 55), width=22)
    rungs = [(760, 'STEP 1', "I'll…", 'something you will do soon'), (480, 'STEP 2', "I'm going to…", 'your plan'), (200, 'TOP', 'I hope to…', 'your goal')]
    for y, t, s, sub in rungs:
        d.line((300, y, 620, y), fill=(140, 95, 55), width=18); sign(img, 680, y-70, 440, 140, t + '\n' + s, 38)
        text(img, 900, y+100, '(' + sub + ')', 28, GREY)
    put(img, '2b50', 140, 390, 20); put(img, '1f9d1', 130, 395, 625)
    return img
B = [
 ('L3_L13_plan', 'plan', plan, 'a calendar and a clipboard', 'vocab'),
 ('L3_L13_hope', 'hope', hope, 'a person with crossed fingers and a thought bubble with a house (bubble drawn)', 'vocab'),
 ('L3_L13_decide', 'decide', decide, 'a person, two drawn arrows, a check mark on one', 'vocab'),
 ('L3_L13_diploma', 'diploma', diploma, 'a scroll and a graduation cap', 'vocab'),
 ('L3_L13_certificate', 'certificate', certificate, 'a drawn certificate and a rosette', 'vocab'),
 ('L3_L13_career', 'career', career, 'a briefcase and a chart going up', 'vocab'),
 ('L3_L13_promotion', 'promotion', promotion, 'an office worker, an arrow up, a sign "MANAGER" (arrow, sign drawn)', 'vocab'),
 ('L3_L13_save_money', 'save money', save_money, 'a money bag, an arrow, a bank', 'vocab'),
 ('L3_L13_own_business', 'own business', own_business, 'a store and a sign "OPEN" (sign drawn)', 'vocab'),
 ('L3_L13_drivers_license', "driver's license", license, 'a drawn license card (not a real design) with a person and a car', 'vocab'),
 ('L3_L13_computer_class', 'computer class', computer_class, 'a teacher and a laptop', 'vocab'),
 ('L3_L13_community_college', 'community college', college, 'a school building and a sign "COMMUNITY COLLEGE" (sign drawn)', 'vocab'),
 ('L3_L13_goal_ladder', 'Talk Time: the Goal Ladder', ladder, "a drawn 3-step ladder: STEP 1 I'll…, STEP 2 I'm going to…, TOP I hope to…; a person and a star", 'activity'),
]
if __name__ == '__main__': run(B, 13, OUT)
