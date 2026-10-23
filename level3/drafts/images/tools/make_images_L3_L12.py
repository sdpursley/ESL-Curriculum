"""Level 3, Lesson 12 pictures: 12 vocabulary cards (600x420) + 1 activity picture (an apartment with 6 problems for the "Find something" game).
Twemoji (CC BY 4.0), one recolored, + drawings in code (l3img.py). Usage: python make_images_L3_L12.py OUT_DIR"""
import sys
from PIL import ImageDraw, ImageOps, Image
from l3img import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '..'   # default: level3/drafts/images (never level3/images, which the website publishes)
BLUE = (70, 140, 220)
def tinted(code, size, rgb):
    e = emoji(code, size); a = e.getchannel('A'); g = ImageOps.grayscale(e.convert('RGB'))
    dark = tuple(int(c*0.35) for c in rgb); light = tuple(min(255, int(c + (255-c)*0.55)) for c in rgb)
    c = ImageOps.colorize(g, dark, light, mid=rgb).convert('RGBA'); c.putalpha(a); return c
def drops(d, pts, r=12):
    for x, y in pts: d.ellipse((x-r, y-r, x+r, y+r*1.4), fill=BLUE); d.polygon([(x-r*0.9, y-2), (x+r*0.9, y-2), (x, y-r*2)], fill=BLUE)
def sink_d(img, x, y, s=1.0, leak=False):
    d = ImageDraw.Draw(img); w = int(260*s); h = int(110*s)
    d.rectangle((x-int(20*s), y, x+w+int(20*s), y+int(18*s)), fill=(210, 190, 160), outline=INK, width=3)
    d.pieslice((x, y-h+int(18*s), x+w, y+h+int(18*s)), 0, 180, fill=(235, 240, 245), outline=INK, width=4)
    fx = x+w//2; d.rectangle((fx-int(8*s), y-int(70*s), fx+int(8*s), y), fill=(160, 165, 175), outline=INK, width=3)
    d.rectangle((fx-int(8*s), y-int(70*s), fx+int(60*s), y-int(55*s)), fill=(160, 165, 175), outline=INK, width=3)
    d.rectangle((fx-int(10*s), y+h, fx+int(10*s), y+h+int(80*s)), fill=(160, 165, 175), outline=INK, width=3)
    if leak: drops(d, [(fx+int(30*s), y+h+int(40*s)), (fx-int(35*s), y+h+int(75*s))], int(11*s)); d.ellipse((fx-int(90*s), y+h+int(95*s), fx+int(90*s), y+h+int(120*s)), fill=(150, 200, 240))
def heater_d(img, x, y, s=1.0):
    d = ImageDraw.Draw(img); w = int(260*s); h = int(150*s)
    d.rounded_rectangle((x, y, x+w, y+h), 12, fill=(235, 235, 235), outline=INK, width=4)
    for i in range(7): xx = x+int(20*s)+i*int(34*s); d.rounded_rectangle((xx, y+int(12*s), xx+int(22*s), y+h-int(12*s)), 8, fill='white', outline=INK, width=2)
def alarm_d(img, x, y, s=1.0, beep=False):
    d = ImageDraw.Draw(img); r = int(60*s)
    d.ellipse((x-r, y-r//2, x+r, y+r//2), fill=(245, 245, 245), outline=INK, width=4); d.ellipse((x-int(10*s), y-int(10*s), x+int(10*s), y+int(10*s)), fill=RED)
    if beep: text(img, x+int(130*s), y+int(10*s), 'BEEP!', int(30*s), RED)
def landlord():
    img = canvas(); put(img, '1f468-200d-1f4bc', 190, 90, 70); put(img, '1f3e2', 170, 320, 90); label(img, 'landlord', 372, 44); return img
def repair_person():
    img = canvas(); put(img, '1f9d1-200d-1f527', 210, 110, 60); put(img, '1f9f0', 150, 340, 140); label(img, 'repair person', 372, 42); return img
def request():
    img = canvas(); form(img, 100, 25, 400, 320, 'MAINTENANCE REQUEST', ['Apt.', 'Problem', 'Since', 'Best time'], hl=1, size=24); label(img, 'maintenance request', 372, 38); return img
def leak():
    img = canvas(); d = ImageDraw.Draw(img); d.rectangle((60, 90, 540, 130), fill=(160, 165, 175), outline=INK, width=4)
    d.line((300, 90, 300, 130), fill=INK, width=4); drops(d, [(300, 175), (285, 245), (318, 300)], 14); label(img, 'leak', 372, 44); return img
def sink():
    img = canvas(); sink_d(img, 170, 140); label(img, 'sink', 372, 44); return img
def toilet():
    img = canvas(); put(img, '1f6bd', 250, 175, 40); label(img, 'toilet', 372, 44); return img
def heater():
    img = canvas(); heater_d(img, 110, 110); put(img, '1f321', 130, 390, 110); label(img, 'heater', 372, 44); return img
def bulb():
    img = canvas(); put(img, '1f4a1', 250, 175, 40); label(img, 'light bulb', 372, 44); return img
def lock():
    img = canvas(); put(img, '1f512', 230, 185, 50); label(img, 'lock', 372, 44); return img
def smoke_alarm():
    img = canvas(); d = ImageDraw.Draw(img); d.rectangle((0, 0, 600, 60), fill=(225, 228, 235)); alarm_d(img, 230, 95, 1.6, beep=True)
    put(img, '1f4a8', 120, 150, 180); label(img, 'smoke alarm', 372, 44); return img
def mouse():
    img = canvas(); put(img, '1f401', 260, 170, 50); label(img, 'mouse', 372, 44); return img
def cockroach():
    img = canvas(); put(img, '1fab3', 230, 185, 50); label(img, 'cockroach', 372, 44); return img
def apartment():
    img = big_canvas(1200, 800); d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 1200, 600), fill=(246, 236, 214)); d.rectangle((0, 600, 1200, 800), fill=(200, 170, 130)); d.line((0, 600, 1200, 600), fill=INK, width=4)
    d.rectangle((0, 0, 1200, 40), fill=(225, 228, 235))
    alarm_d(img, 600, 60, 1.0, beep=True)                                                   # 1 smoke alarm beeping
    d.line((300, 40, 300, 110), fill=INK, width=4); img.alpha_composite(tinted('1f4a1', 90, (140, 140, 140)), (255, 105)); text(img, 300, 230, 'off', 26, GREY)  # 2 bulb out
    sink_d(img, 70, 420, 0.8, leak=True)                                                    # 3 leaking sink
    heater_d(img, 450, 430, 0.9); put(img, '2744', 60, 520, 350)                           # 4 cold heater
    d.rectangle((900, 200, 1080, 600), fill=(150, 100, 60), outline=INK, width=4); put(img, '1f513', 60, 1010, 380)  # 5 open / broken lock
    put(img, '1fab3', 70, 760, 250)                                                         # 6 cockroach on the wall
    put(img, '1f401', 110, 760, 640)                                                        # 7 mouse on the floor
    put(img, '1fab4', 130, 330, 470); put(img, '1fa91', 150, 1010, 620); put(img, '1f5bc', 120, 640, 160)  # fine: plant, chair, picture
    return img
B = [
 ('L3_L12_landlord', 'landlord', landlord, 'a man in work clothes and an apartment building', 'vocab'),
 ('L3_L12_repair_person', 'repair person', repair_person, 'a mechanic and a toolbox', 'vocab'),
 ('L3_L12_maintenance_request', 'maintenance request', request, 'a drawn request form with "Problem" highlighted', 'vocab'),
 ('L3_L12_leak', 'leak', leak, 'a drawn pipe with water drops', 'vocab'),
 ('L3_L12_sink', 'sink', sink, 'a drawn sink and faucet', 'vocab'),
 ('L3_L12_toilet', 'toilet', toilet, 'a toilet', 'vocab'),
 ('L3_L12_heater', 'heater', heater, 'a drawn heater and a thermometer', 'vocab'),
 ('L3_L12_light_bulb', 'light bulb', bulb, 'a light bulb', 'vocab'),
 ('L3_L12_lock', 'lock', lock, 'a lock', 'vocab'),
 ('L3_L12_smoke_alarm', 'smoke alarm', smoke_alarm, 'a drawn smoke alarm "BEEP!" and a puff of smoke', 'vocab'),
 ('L3_L12_mouse', 'mouse', mouse, 'a mouse', 'vocab'),
 ('L3_L12_cockroach', 'cockroach', cockroach, 'a cockroach', 'vocab'),
 ('L3_L12_apartment', 'Talk Time: the apartment with problems', apartment, 'a drawn room: smoke alarm "BEEP!", a light bulb recolored grey, a leaking sink, a heater and a snowflake, a door with an open lock, a cockroach, a mouse, a plant, a chair, a picture', 'activity'),
]
if __name__ == '__main__': run(B, 12, OUT)
