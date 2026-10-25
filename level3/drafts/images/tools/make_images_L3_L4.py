"""Level 3, Lesson 4 pictures: 12 vocabulary cards (600x420) + 3 activity pictures (two Talk Time street scenes, the Read & Write
picture story). Simple and non-graphic: small dents only, no injuries. Twemoji (CC BY 4.0) + drawings in code (l3img.py).
Usage: python make_images_L3_L4.py OUT_DIR"""
import sys
from PIL import ImageDraw
from l3img import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '..'   # default: level3/drafts/images (never level3/images, which the website publishes)
CAR = '1f697'; CAR2 = '1f699'; TRUCK = '1f69a'
def dent_mark(img, x, y, r=26, color=RED):
    d = ImageDraw.Draw(img); d.ellipse((x-r, y-r, x+r, y+r), outline=color, width=5)
    d.arc((x-12, y-8, x+12, y+14), 200, 340, fill=INK, width=4); return img
def motion(img, x, y, n=3, color=GREY):
    d = ImageDraw.Draw(img)
    for k in range(n): d.line((x, y + k*22, x + 50, y + k*22), fill=color, width=5)
    return img
def accident():
    img = canvas(); put(img, CAR2, 220, 50, 60, flip=True); put(img, CAR, 220, 300, 70); dent_mark(img, 305, 210)
    label(img, 'a small accident', 340, 40); label(img, 'no one is hurt', 385, 28, GREY); return img
def roads(img, cx, cy, w=120, color=(120, 120, 125)):
    d = ImageDraw.Draw(img); W_, H_ = img.size
    d.rectangle((0, cy - w//2, W_, cy + w//2), fill=color); d.rectangle((cx - w//2, 0, cx + w//2, H_), fill=color)
    for x in range(0, W_, 50):
        if abs(x - cx) > w//2 + 10: d.line((x, cy, x + 25, cy), fill='white', width=4)
    for y in range(0, H_, 50):
        if abs(y - cy) > w//2 + 10: d.line((cx, y, cx, y + 25), fill='white', width=4)
    return img
def intersection():
    img = canvas(); roads(img, 300, 180); put(img, '1f6a6', 70, 390, 20); put(img, CAR, 80, 60, 140)
    sign(img, 160, 345, 280, 56, 'intersection', 36, 'white', NAVY); return img
def traffic_light():
    img = canvas(); put(img, '1f6a6', 260, 60, 30); text(img, 430, 110, 'red = stop', 30, RED); text(img, 430, 170, 'yellow = slow', 30, (190, 140, 0)); text(img, 430, 230, 'green = go', 30, GREEN)
    label(img, 'traffic light', 370, 40); return img
def stop_sign():
    img = canvas(); put(img, '1f6d1', 250, 175, 30); label(img, 'stop sign', 370, 42); return img
def hit():
    img = canvas(); put(img, CAR, 190, 330, 90); put(img, CAR2, 190, 120, 90, flip=True); motion(img, 30, 160); dent_mark(img, 335, 205, 22)
    arrow(img, 140, 80, 300, 80, NAVY, 8); label(img, 'hit (a car)', 360, 42); return img
def dent():
    img = canvas(); put(img, CAR, 300, 150, 10); dent_mark(img, 230, 215, 34); label(img, 'a dent', 370, 44); return img
def driver():
    img = canvas(); put(img, CAR, 300, 150, 30); put(img, '1f9d1', 44, 348, 160); label(img, 'driver', 370, 44); return img
def police_officer():
    img = canvas(); put(img, '1f46e', 230, 40, 50); put(img, '1f693', 230, 320, 60); label(img, 'police officer', 370, 40); return img
def witness():
    img = canvas(); put(img, '1f9cd-200d-2640-fe0f', 210, 40, 70); put(img, '1f440', 80, 190, 60)
    put(img, CAR2, 150, 290, 130); put(img, CAR, 150, 430, 140); bubble(img, 240, 30, 290, 80, 'I saw it.', 34, tail='left')
    label(img, 'witness', 370, 44); return img
def insurance_card():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((90, 50, 510, 300), 22, fill=(234, 241, 248), outline=NAVY, width=6)
    d.rectangle((96, 56, 504, 106), fill=NAVY); text(img, 300, 81, 'INSURANCE CARD', 30, 'white')
    for i, t in enumerate(['Name: ____________', 'Policy #: ________', 'Car: ____________']): text(img, 120, 140 + i*48, t, 28, INK, 'lm')
    put(img, '1f697', 90, 400, 180); label(img, 'insurance card', 370, 40); return img
def report():
    img = canvas(); form(img, 80, 30, 330, 300, 'ACCIDENT REPORT', ['Date:', 'Time:', 'Place:', 'What happened?'], size=26)
    put(img, '1f4dd', 140, 430, 140); label(img, 'report', 375, 44); return img
def wet_floor():
    img = canvas(); d = ImageDraw.Draw(img)
    d.polygon([(150, 330), (230, 60), (310, 330)], fill=(250, 210, 30), outline=INK); text(img, 230, 200, 'WET\nFLOOR', 30, INK)
    d.ellipse((300, 300, 560, 345), fill=(170, 210, 240)); put(img, '1f4a7', 70, 390, 230); put(img, '1f4a7', 60, 470, 250)
    label(img, 'wet floor', 385, 40); return img
# --- Talk Time street scenes (Witness) ---
def scene_street():
    img = big_canvas(1200, 800); d = ImageDraw.Draw(img); roads(img, 600, 430, 170)
    for k in range(6): d.rectangle((520 + k*28, 520, 536 + k*28, 600), fill='white')          # crosswalk
    put(img, '1f6a6', 110, 700, 220); sign(img, 60, 40, 330, 60, 'MAIN STREET', 34)
    put(img, CAR, 170, 180, 330); put(img, CAR2, 170, 830, 330)                               # cars on the road
    put(img, '1f6b6-200d-2640-fe0f', 120, 545, 470)                                            # woman crossing the street
    put(img, '1f6b4-200d-2642-fe0f', 130, 980, 560)                                            # man riding a bike
    put(img, '1f6b6-200d-2642-fe0f', 120, 60, 640); put(img, '1f415', 80, 180, 690)            # man walking a dog
    put(img, '1f9cd-200d-2640-fe0f', 120, 960, 120); sign(img, 1080, 110, 90, 50, 'BUS', 26, GREEN)   # woman waiting for the bus
    put(img, '1f468', 100, 330, 140); put(img, '1f4f1', 50, 420, 160)                           # man talking on the phone
    put(img, '1f366', 60, 230, 560); put(img, '1f467', 90, 270, 560)                           # girl eating ice cream
    return img
def scene_parking():
    img = big_canvas(1200, 800); d = ImageDraw.Draw(img); d.rectangle((0, 0, 1200, 800), fill=(200, 200, 205))
    for x in range(100, 1200, 200): d.line((x, 40, x, 260), fill='white', width=6); d.line((x, 540, x, 760), fill='white', width=6)
    sign(img, 420, 300, 360, 60, 'FRESH MART PARKING', 30)
    put(img, CAR, 150, 125, 90); put(img, CAR2, 150, 725, 90); put(img, TRUCK, 150, 925, 600)
    put(img, '1f469', 110, 330, 400); put(img, '1f6d2', 110, 430, 420)                         # woman pushing a cart
    put(img, '1f468', 110, 860, 400); put(img, '1f4e6', 90, 960, 430)                          # man carrying a box
    put(img, '1f3c3-200d-2640-fe0f', 120, 120, 560)                                             # woman running
    put(img, '1f9d1', 100, 560, 600); put(img, '2615', 60, 650, 640)                           # person drinking coffee
    put(img, '1f415', 80, 400, 640)                                                             # a dog
    dent_mark(img, 780, 170, 30); return img
def story():
    img = big_canvas(1400, 420); d = ImageDraw.Draw(img)
    caps = ['8:10 a.m.\nLee was driving\nto work.', 'He stopped at\na stop sign.', 'He was waiting.\nA truck hit his car.', 'A small dent.\nNo one was hurt.']
    for i in range(4):
        x = 20 + i*345; d.rounded_rectangle((x, 20, x + 330, 400), 18, outline=NAVY, width=5)
        text(img, x + 30, 52, str(i+1), 34, NAVY)
        for k, t in enumerate(caps[i].split('\n')): text(img, x + 165, 300 + k*32, t, 26, INK)
    put(img, CAR, 150, 110, 100); motion(img, 40, 160, 2)
    put(img, CAR, 140, 440, 110); put(img, '1f6d1', 90, 590, 80)
    put(img, CAR, 130, 830, 120); put(img, TRUCK, 130, 715, 120, flip=True); arrow(img, 735, 100, 800, 100, NAVY, 6)
    put(img, CAR, 160, 1145, 100); dent_mark(img, 1170, 190, 24)
    return img
B = [
 ('L3_L4_accident', 'accident', accident, 'two cars touching, a small dent circled, labels "a small accident", "no one is hurt" (dent mark, labels drawn)', 'vocab'),
 ('L3_L4_intersection', 'intersection', intersection, 'two crossing roads seen from above, a car and a traffic light (roads drawn)', 'vocab'),
 ('L3_L4_traffic_light', 'traffic light', traffic_light, 'a traffic light; "red = stop", "yellow = slow", "green = go"', 'vocab'),
 ('L3_L4_stop_sign', 'stop sign', stop_sign, 'a stop sign, label', 'vocab'),
 ('L3_L4_hit', 'hit (a car)', hit, 'one car moves into another car (motion lines, arrow, small dent drawn), label', 'vocab'),
 ('L3_L4_dent', 'dent', dent, 'a car with a small dent circled (dent mark drawn), label', 'vocab'),
 ('L3_L4_driver', 'driver', driver, 'a person in a car, label', 'vocab'),
 ('L3_L4_police_officer', 'police officer', police_officer, 'a police officer and a police car, label', 'vocab'),
 ('L3_L4_witness', 'witness', witness, 'a woman, eyes, two cars; bubble "I saw it." (bubble drawn)', 'vocab'),
 ('L3_L4_insurance_card', 'insurance card', insurance_card, 'a drawn card "INSURANCE CARD" with Name / Policy # / Car lines + a car', 'vocab'),
 ('L3_L4_report', 'report', report, 'a drawn form "ACCIDENT REPORT" (Date, Time, Place, What happened?) + a pencil and paper', 'vocab'),
 ('L3_L4_wet_floor', 'wet floor', wet_floor, 'a yellow "WET FLOOR" sign, a puddle and water drops (sign, puddle drawn)', 'vocab'),
 ('L3_L4_street', 'Talk Time picture 1: Main Street', scene_street, 'a street corner: two cars, a traffic light, a woman crossing, a man on a bike, a man with a dog, a woman at the bus stop, a man on the phone, a girl with ice cream (roads, crosswalk, signs drawn)', 'activity'),
 ('L3_L4_parking_lot', 'Talk Time picture 2: a parking lot', scene_parking, 'a store parking lot: cars, a truck, a woman with a shopping cart, a man with a box, a woman running, a person with coffee, a dog, a small dent (lot, signs drawn)', 'activity'),
 ('L3_L4_story', 'Read & Write picture story', story, 'four panels: driving to work at 8:10; stopping at a stop sign; a truck hits the car; a small dent, no one hurt (panels, captions, arrow, dent drawn)', 'activity'),
]
if __name__ == '__main__': run(B, 4, OUT)
