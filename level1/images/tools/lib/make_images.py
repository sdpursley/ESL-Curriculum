"""Shared picture helpers (copied from the Level 2 make_images.py; the Level 2 picture list is removed).
Emoji graphics: Twemoji (jdecked/twemoji), CC BY 4.0. Composites/drawings made with PIL.
"""
import os, io, json, urllib.request
import cairosvg
from PIL import Image, ImageDraw, ImageFont
SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), '_twemoji_src')   # download cache for the Twemoji SVGs (created on first run)
os.makedirs(SRC, exist_ok=True)
BASE = 'https://raw.githubusercontent.com/jdecked/twemoji/main/assets/svg/'
W, H = 600, 420
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def font(n): return ImageFont.truetype(F, n)

def emoji(code, size):
    p = f'{SRC}/{code}.svg'
    if not os.path.exists(p):
        urllib.request.urlretrieve(BASE + code + '.svg', p)
    png = cairosvg.svg2png(url=p, output_width=size, output_height=size)
    return Image.open(io.BytesIO(png)).convert('RGBA')

def canvas(): return Image.new('RGBA', (W, H), 'white')

def row(codes, size=None, y=None, img=None, gap=20):
    img = img or canvas()
    n = len(codes); size = size or min(300, int((W - 40 - gap*(n-1)) / n))
    total = n*size + gap*(n-1); x = (W-total)//2; y = (H-size)//2 if y is None else y
    for c in codes:
        e = emoji(c, size); img.alpha_composite(e, (x, y)); x += size + gap
    return img

def arrow(d, x1, y, x2, color=(40,40,40), w=10, both=False):
    d.line((x1, y, x2, y), fill=color, width=w)
    d.polygon([(x2, y), (x2-28, y-18), (x2-28, y+18)], fill=color)
    if both: d.polygon([(x1, y), (x1+28, y-18), (x1+28, y+18)], fill=color)

def calendar(highlight, check=True, circle=None):
    img = canvas(); d = ImageDraw.Draw(img)
    days = ['M','T','W','T','F','S','S']; cw = 74; x0 = (W - 7*cw)//2; y0 = 110
    d.rounded_rectangle((x0-10, 40, x0+7*cw+10, 330), 20, outline=(30,30,30), width=6, fill='white')
    d.rectangle((x0-10, 40, x0+7*cw+10, 95), fill=(200,40,40))
    for i, dd in enumerate(days):
        x = x0 + i*cw
        d.text((x+cw//2, 140), dd, font=font(40), fill=(30,30,30), anchor='mm')
        box = (x+8, 180, x+cw-8, 300)
        hl = i in highlight
        d.rounded_rectangle(box, 10, outline=(30,30,30), width=3, fill=(255,230,120) if hl else 'white')
        if hl and check:
            d.line((x+20, 240, x+34, 262), fill=(20,140,40), width=9); d.line((x+34, 262, x+58, 205), fill=(20,140,40), width=9)
        if circle is not None and i == circle:
            d.ellipse((x-4, 168, x+cw+4, 312), outline=(200,40,40), width=8)
    return img

def clock(h, m, label=None):
    import math
    img = canvas(); d = ImageDraw.Draw(img); cx, cy, r = W//2 - (70 if label else 0), H//2, 170
    d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=(30,30,30), width=10, fill='white')
    for i in range(12):
        a = math.radians(i*30-90); d.line((cx+math.cos(a)*(r-28), cy+math.sin(a)*(r-28), cx+math.cos(a)*(r-8), cy+math.sin(a)*(r-8)), fill=(30,30,30), width=6)
    am = math.radians(m*6-90); ah = math.radians((h%12+m/60)*30-90)
    d.line((cx, cy, cx+math.cos(ah)*95, cy+math.sin(ah)*95), fill=(30,30,30), width=14)
    d.line((cx, cy, cx+math.cos(am)*145, cy+math.sin(am)*145), fill=(30,30,30), width=8)
    d.ellipse((cx-12, cy-12, cx+12, cy+12), fill=(200,40,40))
    if label: d.text((cx+r+90, cy), label, font=font(150), fill=(200,40,40), anchor='mm')
    return img

def save(img, name):
    d = ImageDraw.Draw(img); d.rounded_rectangle((3,3,W-4,H-4), 24, outline=(180,190,200), width=4)
    img.convert('RGB').save(f'{name}.png', optimize=True)

B = {}  # name -> (lesson, word, builder, twemoji codes used, note)
def add(name, lesson, word, fn, codes, note=''): B[name] = (lesson, word, fn, codes, note)
