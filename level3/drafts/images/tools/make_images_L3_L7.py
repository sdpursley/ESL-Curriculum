"""Level 3, Lesson 7 pictures: 12 vocabulary cards (600x420). Invented store; no real brands.
Twemoji (CC BY 4.0) + drawings in code (l3img.py). Usage: python make_images_L3_L7.py OUT_DIR"""
import sys
from PIL import ImageDraw
from l3img import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '..'   # default: level3/drafts/images (never level3/images, which the website publishes)
def cal(img, x, y, w, h, days, mark=None, color=GREEN, size=24):
    """A small drawn week calendar: header bar + day boxes; mark = {index: 'x' | 'check' | 'arrow-from'}"""
    d = ImageDraw.Draw(img); d.rounded_rectangle((x, y, x+w, y+h), 10, fill='white', outline=INK, width=4)
    d.rectangle((x+4, y+4, x+w-4, y+40), fill=RED); bw = (w-20)/len(days)
    for i, t in enumerate(days):
        bx = x+10+i*bw; d.rectangle((bx+3, y+52, bx+bw-3, y+h-10), outline=GREY, width=2); text(img, bx+bw/2, y+72, t, size, INK)
    return bw
def tag(img, x, y, t, color=NAVY, size=30):
    d = ImageDraw.Draw(img); w = 40 + len(t)*size*0.75
    d.rounded_rectangle((x, y, x+w, y+54), 10, fill=color); text(img, x+w/2, y+27, t, size, 'white'); return img
def ret():
    img = canvas(); put(img, '1f9d1', 120, 40, 140); put(img, '1f4e6', 100, 150, 180); arrow(img, 290, 230, 390, 230, NAVY, 9)
    put(img, '1f3ec', 170, 400, 120); label(img, 'return', 372, 44); return img
def exchange():
    img = canvas(); put(img, '1f455', 110, 70, 120); text(img, 125, 260, 'S', 40, NAVY)
    arrow(img, 210, 150, 390, 150, NAVY, 8); arrow(img, 390, 210, 210, 210, NAVY, 8)
    put(img, '1f455', 160, 400, 90); text(img, 480, 280, 'L', 40, NAVY); label(img, 'exchange', 372, 44); return img
def refund():
    img = canvas(); put(img, '1f4b5', 140, 80, 110); arrow(img, 240, 180, 380, 180, NAVY, 9); put(img, '1f91a', 140, 390, 110)
    label(img, 'refund', 352, 44); label(img, '(money back)', 398, 26, GREY); return img
def store_credit():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((110, 60, 490, 290), 24, fill=(60, 130, 90)); text(img, 300, 120, 'STORE CREDIT', 38, 'white')
    text(img, 300, 200, '$24.00', 56, 'white'); text(img, 300, 260, 'Valley Mart', 26, (220, 240, 220))
    label(img, 'store credit', 372, 44); return img
def size():
    img = canvas()
    for i, (s, t) in enumerate([(90, 'S'), (125, 'M'), (160, 'L')]):
        x = 60 + i*170; put(img, '1f455', s, x + (160-s)//2, 230 - s); text(img, x + 80, 285, t, 40, NAVY)
    label(img, 'size', 372, 44); return img
def broken():
    img = canvas(); d = ImageDraw.Draw(img); put(img, '1f4f1', 230, 185, 40)
    for a, b in [((300, 120), (270, 170)), ((270, 170), (320, 200)), ((320, 200), (285, 260)), ((300, 120), (340, 150))]: d.line((*a, *b), fill=INK, width=5)
    label(img, 'broken', 372, 44); return img
def customer():
    img = canvas(); put(img, '1f469', 140, 120, 110); put(img, '1f6cd', 120, 270, 160); put(img, '1f3ec', 120, 420, 60)
    label(img, 'customer', 372, 44); return img
def manager():
    img = canvas(); put(img, '1f9d1-200d-1f4bc', 220, 70, 70); tag(img, 300, 150, 'MANAGER', NAVY, 28)
    label(img, 'manager', 372, 44); return img
def cancel():
    img = canvas(); cal(img, 110, 50, 380, 240, ['Mon', 'Tue', 'Wed']); text(img, 300, 200, '10:00', 26, INK); cross(img, 262, 162, 76, RED, 10)
    label(img, 'cancel', 372, 44); return img
def reschedule():
    img = canvas(); bw = cal(img, 60, 50, 480, 240, ['Mon', 'Tue', 'Wed', 'Thu']); d = ImageDraw.Draw(img)
    text(img, 60+10+bw/2, 200, '10:00', 24, GREY); cross(img, 60+10+bw/2-28, 172, 56, RED, 8)
    text(img, 60+10+3*bw+bw/2, 200, '4:30', 28, GREEN)
    arrow(img, 60+10+bw, 250, 60+10+3*bw, 250, NAVY, 7); label(img, 'reschedule', 362, 42); label(img, '(change the day or time)', 402, 24, GREY); return img
def available():
    img = canvas(); d = ImageDraw.Draw(img)
    for i, (t, ok) in enumerate([('3:00', False), ('4:30', True), ('5:30', False)]):
        y = 50 + i*95; d.rounded_rectangle((130, y, 470, y+75), 14, fill=(225, 245, 230) if ok else (240, 240, 240), outline=GREEN if ok else GREY, width=4)
        text(img, 230, y+38, t, 36, INK); (check if ok else cross)(img, 370, y+12, 50, GREEN if ok else RED, 9)
    label(img, 'available', 372, 44); return img
def stain():
    img = canvas(); d = ImageDraw.Draw(img); put(img, '1f455', 260, 170, 30)
    d.ellipse((330, 170, 385, 215), fill=(130, 85, 40)); d.ellipse((370, 200, 395, 222), fill=(130, 85, 40))
    d.ellipse((318, 158, 400, 232), outline=RED, width=5); label(img, 'stain', 372, 44); return img
B = [
 ('L3_L7_return', 'return', ret, 'a person with a box, an arrow back to a store', 'vocab'),
 ('L3_L7_exchange', 'exchange', exchange, 'a small shirt (S) and a large shirt (L) with arrows both ways (arrows, letters drawn)', 'vocab'),
 ('L3_L7_refund', 'refund', refund, 'money, an arrow to a hand, label "money back"', 'vocab'),
 ('L3_L7_store_credit', 'store credit', store_credit, 'a drawn store credit card "$24.00, Valley Mart" (invented store)', 'vocab'),
 ('L3_L7_size', 'size', size, 'three shirts, S / M / L', 'vocab'),
 ('L3_L7_broken', 'broken', broken, 'a phone with cracks (cracks drawn)', 'vocab'),
 ('L3_L7_customer', 'customer', customer, 'a woman with a shopping bag, a store', 'vocab'),
 ('L3_L7_manager', 'manager', manager, 'an office worker with a MANAGER name tag (tag drawn)', 'vocab'),
 ('L3_L7_cancel', 'cancel', cancel, 'a drawn calendar with an appointment crossed out', 'vocab'),
 ('L3_L7_reschedule', 'reschedule', reschedule, 'a drawn calendar: Monday 10:00 crossed out, an arrow to Thursday 4:30', 'vocab'),
 ('L3_L7_available', 'available', available, 'three time slots; 4:30 checked green, the others crossed (drawn)', 'vocab'),
 ('L3_L7_stain', 'stain', stain, 'a shirt with a brown spot circled (spot drawn)', 'vocab'),
]
if __name__ == '__main__': run(B, 7, OUT)
