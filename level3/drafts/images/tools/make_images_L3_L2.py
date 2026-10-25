"""Level 3, Lesson 2 pictures: 12 vocabulary cards (600x420) + 2 activity pictures (listening Task A, Talk Time crowd).
Twemoji (CC BY 4.0) + drawings in code (l3img.py). Usage: python make_images_L3_L2.py OUT_DIR"""
import sys
from PIL import ImageDraw
from l3img import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '..'   # default: level3/drafts/images (never level3/images, which the website publishes)
WC = '1f469-200d-1f9b1'; MC = '1f468-200d-1f9b1'; WS = '1f471-200d-2640-fe0f'; MB = '1f9d4-200d-2642-fe0f'; WO = '1f469'; MA = '1f471-200d-2642-fe0f'; MA2 = '1f9d1'
def vmeasure(img, x, y0, y1, color=NAVY):
    d = ImageDraw.Draw(img); d.line((x, y0, x, y1), fill=color, width=6)
    for y, s in ((y0, 1), (y1, -1)): d.polygon([(x, y), (x-14, y+s*24), (x+14, y+s*24)], fill=color)
    return img
def two_heights(tall):
    img = canvas(); size = 80; base = 395
    if tall:
        person(img, 200, base, MA2, h=1.35, shirt=(70, 120, 190), size=size); person(img, 390, base, MA2, h=1.0, shirt=(170, 170, 170), size=size)
        top = base - int(size*0.95*1.35) - int(size*1.05*1.35) - int(size*0.9); vmeasure(img, 160, top, base); text(img, 85, 200, 'tall', 46, NAVY)
    else:
        person(img, 150, base, MA2, h=1.0, shirt=(170, 170, 170), size=size); person(img, 330, base, MA2, h=0.72, shirt=(70, 120, 190), size=size)
        top = base - int(size*0.95*0.72) - int(size*1.05*0.72) - int(size*0.9); vmeasure(img, 450, top, base); text(img, 522, 290, 'short', 40, NAVY)
    return img
def curly():
    img = canvas(); put(img, WC, 230, 50, 40); put(img, MC, 230, 320, 40); label(img, 'curly hair', 370, 44); return img
def straight():
    img = canvas(); put(img, WS, 230, 50, 40); put(img, '1f471-200d-2642-fe0f', 230, 320, 40); label(img, 'straight hair', 370, 44); return img
def beard():
    img = canvas(); put(img, MB, 270, 165, 30); label(img, 'a beard', 370, 44); return img
def specs():
    img = canvas(); put(img, '1f453', 200, 40, 70); put(img, WO, 230, 320, 40); glasses(img, 320, 40, 230); label(img, 'glasses', 370, 44); return img
def friendly():
    img = canvas(); put(img, '1f60a', 190, 60, 150); put(img, '1f44b', 120, 250, 200)
    bubble(img, 240, 30, 330, 120, 'Hi! Welcome!', 40, tail='left'); label(img, 'friendly', 385, 40); return img
def shy():
    img = canvas(); put(img, '1fae3', 220, 60, 60); put(img, '1f9d1', 150, 400, 110)
    bubble(img, 330, 20, 200, 80, 'Hi!', 36, tail='right'); text(img, 170, 320, '...hi', 36, GREY); label(img, 'shy', 385, 44); return img
def funny():
    img = canvas(); put(img, '1f61c', 180, 50, 150); put(img, '1f602', 150, 270, 170); put(img, '1f923', 130, 440, 190)
    bubble(img, 40, 20, 260, 100, 'Ha ha ha!', 38); label(img, 'funny', 395, 40); return img
def hardworking():
    img = canvas(); put(img, '1f477-200d-2640-fe0f', 200, 40, 50); put(img, '1f4e6', 150, 260, 110); put(img, '1f4aa', 130, 430, 90)
    label(img, 'works hard', 360, 44); return img
def patient():
    img = canvas(); put(img, '1f60c', 200, 60, 50); put(img, '23f3', 160, 330, 70)
    text(img, 420, 270, '30 min', 40, GREY); label(img, 'waits calmly', 360, 44); return img
def quiet():
    img = canvas(); put(img, '1f92b', 200, 60, 50); put(img, '1f4d6', 170, 340, 70); label(img, "doesn't talk much", 360, 40); return img
PEOPLE_A = [('a', MB, 1.3, (60, 110, 180), True), ('b', WS, 0.8, (200, 90, 90), False), ('c', MC, 1.0, (90, 160, 90), False), ('d', WC, 1.0, (150, 110, 190), True)]
def listening_people():
    img = big_canvas(1200, 560)
    for i, (k, head, h, shirt, g) in enumerate(PEOPLE_A):
        x = 110 + i*280; person(img, x, 470, head, h=h, shirt=shirt, size=110, specs=g)
        text(img, x+55, 515, k, 44, NAVY)
    return img
# crowd: (head, height, shirt, glasses). Numbers 1-12 (the Talk Time cards and answer key use these numbers)
RED_ = (205, 60, 60); BLUE = (60, 110, 190); GRN = (60, 150, 80); YLW = (230, 190, 40); PUR = (140, 90, 180); ORG = (235, 130, 40); GRY = (150, 150, 150)
CROWD = [(WC, 1.3, RED_, True), (MB, 1.0, BLUE, False), (WS, 0.8, GRN, False), (MA, 1.3, YLW, True), (WO, 1.0, PUR, False), (MC, 0.8, ORG, True),
         (WS, 1.3, BLUE, True), (MB, 1.3, GRN, True), (WC, 0.8, YLW, False), (MC, 1.3, RED_, False), (WO, 0.8, GRY, True), (MA, 1.0, GRN, False)]
def crowd():
    img = big_canvas(1400, 1000); d = ImageDraw.Draw(img)
    text(img, 700, 50, 'BUS STATION', 46, 'white'); d.rounded_rectangle((470, 18, 930, 82), 12, fill=NAVY); text(img, 700, 50, 'BUS STATION', 46, 'white')
    for i, (head, h, shirt, g) in enumerate(CROWD):
        r, c = divmod(i, 6); x = 50 + c*225; base = 470 + r*460
        person(img, x, base, head, h=h, shirt=shirt, size=110, specs=g, num=i+1)
    return img
B = [
 ('L3_L2_tall', 'tall', lambda: two_heights(True), 'a tall person next to a person of average height; height arrow and label "tall" (bodies, arrow, label drawn)', 'vocab'),
 ('L3_L2_short', 'short', lambda: two_heights(False), 'a person of average height next to a short person; height arrow and label "short" (bodies, arrow, label drawn)', 'vocab'),
 ('L3_L2_curly_hair', 'curly hair', curly, 'a woman and a man with curly hair, label', 'vocab'),
 ('L3_L2_straight_hair', 'straight hair', straight, 'a woman and a man with straight hair, label', 'vocab'),
 ('L3_L2_beard', 'beard', beard, 'a man with a beard, label', 'vocab'),
 ('L3_L2_glasses', 'glasses', specs, 'a pair of glasses + a woman wearing glasses (glasses on the face drawn), label', 'vocab'),
 ('L3_L2_friendly', 'friendly', friendly, 'smiling face + waving hand, bubble "Hi! Welcome!" (bubble drawn)', 'vocab'),
 ('L3_L2_shy', 'shy', shy, 'a face peeking from behind its hand answers a quiet "...hi" to a person saying "Hi!" (bubble, text drawn)', 'vocab'),
 ('L3_L2_funny', 'funny', funny, 'a joking face and two laughing faces, bubble "Ha ha ha!" (bubble drawn)', 'vocab'),
 ('L3_L2_hardworking', 'hardworking', hardworking, 'a woman worker, a box and a strong arm, label "works hard"', 'vocab'),
 ('L3_L2_patient', 'patient', patient, 'a calm face + an hourglass, "30 min", label "waits calmly"', 'vocab'),
 ('L3_L2_quiet', 'quiet', quiet, 'a face saying "shh" + an open book, label "doesn\'t talk much"', 'vocab'),
 ('L3_L2_listening_people', 'Listening Task A (people a-d)', listening_people, 'four standing people a-d: tall man with beard and glasses; short woman with long straight hair; man with curly hair; woman with curly hair and glasses (bodies, glasses, letters drawn)', 'activity'),
 ('L3_L2_crowd', 'Talk Time crowd picture (people 1-12)', crowd, 'twelve numbered people at a bus station, different heights, hair, beards, glasses and shirt colors (bodies, glasses, sign, numbers drawn)', 'activity'),
]
if __name__ == '__main__': run(B, 2, OUT)
