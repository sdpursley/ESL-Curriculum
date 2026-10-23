"""Level 3, Lesson 9 pictures: 12 vocabulary cards (600x420) + 1 activity picture (four invented job cards for the Interview Rotation).
Twemoji (CC BY 4.0) + drawings in code (l3img.py). Usage: python make_images_L3_L9.py OUT_DIR"""
import sys
from PIL import ImageDraw
from l3img import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '..'   # default: level3/drafts/images (never level3/images, which the website publishes)
def strength():
    img = canvas(); put(img, '1f4aa', 220, 190, 50); put(img, '2b50', 90, 400, 50); label(img, 'strength', 372, 44); return img
def good_at():
    img = canvas(); put(img, '1f9d1-200d-1f527', 210, 110, 70); bubble(img, 330, 60, 230, 100, "I'm good at\nfixing things.", 28, tail='left')
    check(img, 450, 250, 60); label(img, 'good at', 372, 44); return img
def interested_in():
    img = canvas(); put(img, '1f9d1', 170, 70, 120); put(img, '1f4a1', 90, 230, 50); arrow(img, 270, 230, 360, 230, NAVY, 8)
    put(img, '1f4bb', 170, 380, 130); label(img, 'interested in', 372, 42); return img
def experience():
    img = canvas(); put(img, '1f9f0', 170, 90, 110); d = ImageDraw.Draw(img)
    sign(img, 300, 140, 230, 90, '5 years', 44); label(img, 'experience', 372, 44); return img
def reliable():
    img = canvas(); put(img, '23f0', 170, 50, 100); text(img, 290, 150, 'on time', 40, GREEN, 'lm')
    text(img, 290, 225, 'every day', 34, GREY, 'lm'); label(img, 'reliable', 372, 44); return img
def teamwork():
    img = canvas(); put(img, '1f469', 150, 60, 110); put(img, '1f91d', 130, 235, 150); put(img, '1f468', 150, 390, 110)
    label(img, 'teamwork', 372, 44); return img
def organize():
    img = canvas(); d = ImageDraw.Draw(img)
    for i, c in enumerate([(70, 120, 190), (200, 60, 60), (40, 150, 70)]):
        x = 140 + i*115; d.rectangle((x, 120, x+95, 320), fill=c, outline=INK, width=4); d.rectangle((x+25, 140, x+70, 180), fill='white', outline=INK, width=2); text(img, x+47, 160, 'ABC'[i], 28)
    label(img, 'organize', 372, 44); return img
def solve_problems():
    img = canvas(); put(img, '1f9e9', 140, 90, 110); put(img, '1f9e9', 140, 230, 110, flip=True); arrow(img, 385, 180, 450, 180, NAVY, 8)
    check(img, 500, 180, 60); label(img, 'solve problems', 372, 42); return img
def resume():
    img = canvas(); form(img, 160, 25, 280, 320, 'RÉSUMÉ', ['Name', 'Experience', 'Skills', 'Training'], size=24)
    label(img, 'résumé', 372, 44); return img
def apply():
    img = canvas(); form(img, 110, 30, 260, 300, 'JOB APPLICATION', ['Name', 'Phone', 'Job'], size=20)
    put(img, '270f', 130, 380, 150); label(img, 'apply', 372, 44); return img
def training():
    img = canvas(); put(img, '1f9d1-200d-1f3eb', 220, 60, 60); put(img, '1f9d1', 130, 320, 160); put(img, '1f9d1', 130, 440, 160, flip=True)
    label(img, 'training', 372, 44); return img
def shift():
    img = canvas(); d = ImageDraw.Draw(img)
    put(img, '2600', 120, 80, 40); text(img, 140, 210, '7 a.m.–3 p.m.', 32, INK)
    put(img, '1f319', 110, 400, 45); text(img, 455, 210, '3 p.m.–11 p.m.', 32, INK)
    d.line((300, 50, 300, 260), fill=GREY, width=3); label(img, 'shift', 372, 44); return img
def jobs():
    img = big_canvas(1200, 560); d = ImageDraw.Draw(img); d.rectangle((0, 0, 1200, 560), fill=(236, 240, 246))
    cards = [('1f4e6', 'WAREHOUSE', 'Hill Street Supply', 'Day or night shift'),
             ('1f3e8', 'HOTEL', 'Lakeview Inn', 'Maintenance'),
             ('1f373', 'KITCHEN', 'Corner Café', 'Cook, dishwasher'),
             ('1f9f8', 'CHILDCARE', 'Little Stars Center', 'Assistant')]
    for i, (code, t, place, job) in enumerate(cards):
        x = 25 + i*295; y = 30
        d.rounded_rectangle((x, y, x+270, y+500), 18, fill='white', outline=(150, 160, 180), width=3)
        sign(img, x+15, y+15, 240, 60, t, 30); put(img, code, 150, x+60, y+100)
        text(img, x+135, y+300, place, 24, NAVY); text(img, x+135, y+345, job, 19, GREY)
        d.ellipse((x+105, y+400, x+165, y+460), fill=NAVY); text(img, x+135, y+430, str(i+1), 30, 'white')
    return img
B = [
 ('L3_L9_strength', 'strength', strength, 'a flexed arm and a star', 'vocab'),
 ('L3_L9_good_at', 'good at', good_at, 'a mechanic; bubble "I\'m good at fixing things."; a check mark (bubble, check drawn)', 'vocab'),
 ('L3_L9_interested_in', 'interested in', interested_in, 'a person, a light bulb, an arrow to a laptop', 'vocab'),
 ('L3_L9_experience', 'experience', experience, 'a toolbox and a sign "5 years" (sign drawn)', 'vocab'),
 ('L3_L9_reliable', 'reliable', reliable, 'an alarm clock and "on time every day" (text drawn)', 'vocab'),
 ('L3_L9_teamwork', 'teamwork', teamwork, 'a woman, a handshake, a man', 'vocab'),
 ('L3_L9_organize', 'organize', organize, 'three drawn labeled binders (our drawing)', 'vocab'),
 ('L3_L9_solve_problems', 'solve problems', solve_problems, 'two puzzle pieces (one mirrored), an arrow, a check mark', 'vocab'),
 ('L3_L9_resume', 'résumé', resume, 'a drawn résumé form (name, experience, skills, training)', 'vocab'),
 ('L3_L9_apply', 'apply', apply, 'a drawn job application form and a pencil', 'vocab'),
 ('L3_L9_training', 'training', training, 'a teacher and two learners (one mirrored)', 'vocab'),
 ('L3_L9_shift', 'shift', shift, 'a sun "7 a.m.–3 p.m." and a moon "3 p.m.–11 p.m." (text drawn)', 'vocab'),
 ('L3_L9_job_cards', 'Talk Time: four job cards', jobs, 'four numbered cards: boxes (warehouse), a hotel, a frying pan (kitchen), a teddy bear (childcare); cards and text drawn', 'activity'),
]
if __name__ == '__main__': run(B, 9, OUT)
