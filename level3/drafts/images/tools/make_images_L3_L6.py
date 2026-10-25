"""Level 3, Lesson 6 pictures: 12 vocabulary cards (600x420) + 1 activity picture (the weather-alert text message for Read & Write).
Twemoji (CC BY 4.0) + drawings in code (l3img.py). No candles anywhere (fire risk). Usage: python make_images_L3_L6.py OUT_DIR"""
import sys
from PIL import ImageDraw
from l3img import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '..'   # default: level3/drafts/images (never level3/images, which the website publishes)
BLUE = (60, 140, 240)
def phone(img, x, y, w, h, lines, title=None, tcol=RED, size=22):
    d = ImageDraw.Draw(img); d.rounded_rectangle((x, y, x+w, y+h), 28, fill=INK); d.rounded_rectangle((x+14, y+30, x+w-14, y+h-30), 10, fill='white')
    yy = y + 50
    if title: d.rounded_rectangle((x+24, yy, x+w-24, yy+44), 10, fill=tcol); text(img, x+w/2, yy+22, title, size, 'white'); yy += 60
    for t in lines: text(img, x+w/2, yy+12, t, size, INK); yy += size + 12
    return img
def water_bottle(img, x, y, s=1.0):
    d = ImageDraw.Draw(img); w = int(60*s); h = int(150*s)
    d.rectangle((x + w*0.35, y, x + w*0.65, y + h*0.12), fill=(40, 90, 200))
    d.rounded_rectangle((x, y + h*0.12, x + w, y + h), int(14*s), fill=(170, 215, 250), outline=(60, 120, 200), width=4)
    d.rectangle((x + 3, y + h*0.45, x + w - 3, y + h*0.65), fill=(40, 90, 200)); return img
def forecast():
    img = canvas(); put(img, '1f4fa', 220, 50, 70)
    for i, (c, t) in enumerate([('2600', 'Mon'), ('1f327', 'Tue'), ('2744', 'Wed')]):
        put(img, c, 70, 300 + i*95, 120); text(img, 335 + i*95, 215, t, 24, INK)
    label(img, 'forecast', 372, 44); return img
def storm():
    img = canvas(); put(img, '26c8', 250, 175, 40); put(img, '1f4a8', 90, 440, 120); label(img, 'storm', 372, 44); return img
def snowstorm():
    img = canvas(); put(img, '1f328', 220, 90, 40); put(img, '2744', 90, 360, 60); put(img, '2744', 70, 450, 170); put(img, '2603', 120, 340, 190)
    label(img, 'snowstorm', 372, 44); return img
def flood():
    img = canvas(); d = ImageDraw.Draw(img); put(img, '1f3e0', 230, 185, 30)
    d.rectangle((40, 210, 560, 320), fill=(110, 170, 230)); put(img, '1f30a', 100, 60, 200); put(img, '1f30a', 100, 440, 200)
    label(img, 'flood', 372, 44); return img
def heat_wave():
    img = canvas(); put(img, '2600', 160, 40, 40); put(img, '1f321', 160, 220, 80); put(img, '1f975', 150, 400, 120)
    label(img, 'heat wave', 372, 44); return img
def weather_alert():
    img = canvas(); phone(img, 200, 15, 200, 320, ['Storm', 'tonight.', 'Stay home.'], 'ALERT', RED, 24); put(img, '26a0', 80, 440, 40)
    label(img, 'weather alert', 372, 42); return img
def power_outage():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rectangle((0, 0, 600, 330), fill=(40, 45, 70)); put(img, '1f319', 70, 470, 30)
    d.polygon([(150, 150), (300, 50), (450, 150)], fill=(90, 90, 110)); d.rectangle((170, 150, 430, 320), fill=(110, 110, 130))
    for x in (200, 330): d.rectangle((x, 190, x + 70, 250), fill=(20, 20, 30))
    put(img, '1f4a1', 80, 40, 120); cross(img, 50, 130, 60, RED, 10); label(img, 'power outage', 372, 42); return img
def flashlight():
    img = canvas(); d = ImageDraw.Draw(img)
    d.polygon([(215, 160), (570, 30), (570, 290)], fill=(255, 240, 150)); put(img, '1f526', 200, 50, 120, flip=True); label(img, 'flashlight', 372, 44); return img
def battery():
    img = canvas(); put(img, '1f50b', 200, 120, 60); put(img, '1f50b', 150, 330, 100); label(img, 'battery', 372, 44); return img
def emergency_kit():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((60, 110, 340, 320), 20, fill=(200, 60, 60)); d.rectangle((60, 110, 340, 150), fill=(170, 40, 40))
    d.rectangle((185, 180, 215, 280), fill='white'); d.rectangle((150, 215, 250, 245), fill='white')
    put(img, '1f526', 90, 360, 60); put(img, '1f50b', 80, 470, 70); water_bottle(img, 380, 170, 0.9); put(img, '1fa79', 80, 470, 200)
    label(img, 'emergency kit', 372, 42); return img
def bottled_water():
    img = canvas()
    for k in range(4): water_bottle(img, 120 + k*95, 70, 1.6 if k % 2 == 0 else 1.5)
    label(img, 'bottled water', 372, 44); return img
def shelter():
    img = canvas(); put(img, '1f3eb', 220, 60, 50); sign(img, 300, 60, 240, 70, 'SHELTER', 40, GREEN)
    put(img, '1f6b6', 100, 470, 170, flip=True); arrow(img, 460, 300, 300, 300, NAVY, 9); label(img, 'shelter', 372, 44); return img
def alert_text():
    img = big_canvas(700, 900); d = ImageDraw.Draw(img)
    d.rounded_rectangle((120, 20, 580, 880), 50, fill=INK); d.rounded_rectangle((140, 80, 560, 820), 16, fill='white')
    d.rounded_rectangle((160, 100, 540, 170), 14, fill=RED); text(img, 350, 135, 'WEATHER ALERT', 34, 'white')
    lines = ['Green County Alert', 'Monday, 3:15 p.m.', '', 'Heat wave: Tuesday to', 'Friday. It will be very hot,', 'about 100 degrees.', '', 'Drink water. Stay inside', 'from 12:00 to 5:00 p.m.', 'Check on older neighbors.', '', 'Cooling center: Oak Park', 'Library, 9:00 a.m. to', '9:00 p.m.']
    for i, t in enumerate(lines): text(img, 165, 200 + i*38, t, 25, INK, 'lm')
    put(img, '1f975', 90, 430, 705); return img
B = [
 ('L3_L6_forecast', 'forecast', forecast, 'a TV, sun / rain / snow icons with days (labels drawn)', 'vocab'),
 ('L3_L6_storm', 'storm', storm, 'a cloud with lightning and rain, wind', 'vocab'),
 ('L3_L6_snowstorm', 'snowstorm', snowstorm, 'a snow cloud, snowflakes, a snowman', 'vocab'),
 ('L3_L6_flood', 'flood', flood, 'a house with water around it (water drawn), waves', 'vocab'),
 ('L3_L6_heat_wave', 'heat wave', heat_wave, 'the sun, a thermometer, a hot face', 'vocab'),
 ('L3_L6_weather_alert', 'weather alert', weather_alert, 'a drawn phone with an ALERT message, a warning sign', 'vocab'),
 ('L3_L6_power_outage', 'power outage', power_outage, 'a dark house at night (house, sky drawn), a light bulb crossed out, the moon', 'vocab'),
 ('L3_L6_flashlight', 'flashlight', flashlight, 'a flashlight with a light beam (beam drawn)', 'vocab'),
 ('L3_L6_battery', 'battery', battery, 'two batteries', 'vocab'),
 ('L3_L6_emergency_kit', 'emergency kit', emergency_kit, 'a red kit bag (drawn) with a flashlight, batteries, water, a bandage', 'vocab'),
 ('L3_L6_bottled_water', 'bottled water', bottled_water, 'four water bottles (drawn)', 'vocab'),
 ('L3_L6_shelter', 'shelter', shelter, 'a public building with a SHELTER sign, a person walking to it (sign, arrow drawn)', 'vocab'),
 ('L3_L6_alert_text', 'Read & Write: a weather alert text', alert_text, 'a drawn phone with an invented heat-wave alert message, a hot face', 'activity'),
]
if __name__ == '__main__': run(B, 6, OUT)
