"""Level 3, Lesson 11 pictures: 12 vocabulary cards (600x420) + 1 activity picture (six invented event cards for Star Ratings).
The -ing / -ed cards show the thing (left, "-ing") and the person's feeling (right, "-ed"). Twemoji (CC BY 4.0) + drawings in code (l3img.py).
Usage: python make_images_L3_L11.py OUT_DIR"""
import sys, math
from PIL import ImageDraw
from l3img import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '..'   # default: level3/drafts/images (never level3/images, which the website publishes)
def pair(thing, face, ing, ed):
    def f():
        img = canvas(); d = ImageDraw.Draw(img)
        put(img, thing, 170, 75, 45); put(img, face, 150, 375, 55); arrow(img, 265, 130, 350, 130, NAVY, 7)
        text(img, 160, 255, 'It was ' + ing + '.', 26, GREY); text(img, 450, 255, 'I was ' + ed + '.', 26, GREY)
        label(img, ing + ' / ' + ed, 365, 36); return img
    return f
def star(d, cx, cy, r, fill):
    pts = []
    for i in range(10):
        a = -math.pi/2 + i*math.pi/5; rr = r if i % 2 == 0 else r*0.45; pts.append((cx + rr*math.cos(a), cy + rr*math.sin(a)))
    d.polygon(pts, fill=fill, outline=INK)
def festival():
    img = canvas(); put(img, '1f3aa', 210, 195, 40); put(img, '1f388', 100, 80, 70); put(img, '1f32e', 100, 420, 150); label(img, 'festival', 372, 44); return img
def concert():
    img = canvas(); put(img, '1f3a4', 160, 110, 80); put(img, '1f3b8', 180, 300, 70); put(img, '1f3b6', 80, 480, 40); label(img, 'concert', 372, 44); return img
def museum():
    img = canvas(); put(img, '1f3db', 230, 110, 50); put(img, '1f5bc', 140, 370, 120); label(img, 'museum', 372, 44); return img
def fair():
    img = canvas(); put(img, '1f3a1', 250, 175, 40); label(img, 'fair', 372, 44); return img
def review():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((100, 40, 500, 310), 16, fill='white', outline=INK, width=4)
    for i in range(5): star(d, 160 + i*70, 110, 30, (250, 190, 30) if i < 4 else (220, 220, 220))
    text(img, 300, 190, '"Great food!', 32, INK); text(img, 300, 240, 'The music was fun."', 32, INK)
    label(img, 'review (stars)', 372, 42); return img
def events():
    img = big_canvas(1200, 760); d = ImageDraw.Draw(img); d.rectangle((0, 0, 1200, 760), fill=(236, 240, 246))
    cards = [('1f32e', 'Food Festival', 'Riverside Park, Sat.'), ('1f3b5', 'Music in the Park', 'free concert, Fri.'),
             ('1f697', 'Old Cars Show', 'City Museum, Sun.'), ('1f3a1', 'Fall Fair', 'Hill School, Sat.'),
             ('1f4bb', 'Computer Workshop', 'Oak Park Library, Tue.'), ('26bd', 'Soccer Game', 'City Field, Sun.')]
    for i, (code, t, sub) in enumerate(cards):
        x = 25 + (i % 3)*390; y = 20 + (i // 3)*370
        d.rounded_rectangle((x, y, x+370, y+350), 18, fill='white', outline=(150, 160, 180), width=3)
        put(img, code, 140, x+115, y+25); text(img, x+185, y+200, t, 32 if len(t) < 16 else 27, NAVY); text(img, x+185, y+245, sub, 24, GREY)
        for k in range(5): star(d, x+85 + k*50, y+300, 20, 'white')
        d.ellipse((x+12, y+12, x+60, y+60), fill=NAVY); text(img, x+36, y+36, str(i+1), 28, 'white')
    return img
B = [
 ('L3_L11_exciting', 'exciting / excited', pair('1f3a2', '1f929', 'exciting', 'excited'), 'a roller coaster, an arrow, a star-struck face', 'vocab'),
 ('L3_L11_boring', 'boring / bored', pair('1f4c3', '1f971', 'boring', 'bored'), 'a long page, an arrow, a yawning face', 'vocab'),
 ('L3_L11_interesting', 'interesting / interested', pair('1f4d6', '1f9d0', 'interesting', 'interested'), 'an open book, an arrow, a face with a monocle', 'vocab'),
 ('L3_L11_confusing', 'confusing / confused', pair('1f5fa', '1f615', 'confusing', 'confused'), 'a map, an arrow, a confused face', 'vocab'),
 ('L3_L11_relaxing', 'relaxing / relaxed', pair('1f3d6', '1f60c', 'relaxing', 'relaxed'), 'a beach, an arrow, a relieved face', 'vocab'),
 ('L3_L11_tiring', 'tiring / tired', pair('1f3c3', '1f62b', 'tiring', 'tired'), 'a runner, an arrow, a tired face', 'vocab'),
 ('L3_L11_surprising', 'surprising / surprised', pair('1f381', '1f62e', 'surprising', 'surprised'), 'a gift, an arrow, a surprised face', 'vocab'),
 ('L3_L11_festival', 'festival', festival, 'a tent, a balloon, a taco', 'vocab'),
 ('L3_L11_concert', 'concert', concert, 'a microphone, a guitar, music notes', 'vocab'),
 ('L3_L11_museum', 'museum', museum, 'a classical building and a framed picture', 'vocab'),
 ('L3_L11_fair', 'fair', fair, 'a Ferris wheel', 'vocab'),
 ('L3_L11_review', 'review (stars)', review, 'a drawn review card: 4 of 5 stars, "Great food! The music was fun."', 'vocab'),
 ('L3_L11_event_cards', 'Talk Time: six event cards', events, 'six numbered cards: a taco, music notes, a car, a Ferris wheel, a laptop, a soccer ball; cards, stars, text drawn', 'activity'),
]
if __name__ == '__main__': run(B, 11, OUT)
