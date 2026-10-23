"""Level 3 picture-card helpers (600x420 PNG). Same card style as Levels 1-2 (tools/images/make_images.py: font, emoji, canvas,
row, arrow, save) and Level 3 Lesson 1 (put, bubble, label), plus a few simple drawing helpers.
Emoji graphics: Twemoji (jdecked/twemoji), CC BY 4.0, downloaded once into ./_twemoji_src/."""
import os, io, urllib.request, math
import cairosvg
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '_twemoji_src'); os.makedirs(SRC, exist_ok=True)
BASE = 'https://raw.githubusercontent.com/jdecked/twemoji/main/assets/svg/'
W, H = 600, 420
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
INK = (30, 30, 30); NAVY = (31, 58, 95); RED = (200, 40, 40); GREEN = (20, 130, 60); GREY = (90, 90, 90); YEL = (255, 236, 160)
USED = set()
def font(n): return ImageFont.truetype(F, n)
def emoji(code, size):
    p = f'{SRC}/{code}.svg'
    if not os.path.exists(p): urllib.request.urlretrieve(BASE + code + '.svg', p)
    USED.add(code)
    png = cairosvg.svg2png(url=p, output_width=size, output_height=size)
    return Image.open(io.BytesIO(png)).convert('RGBA')
def canvas(): return Image.new('RGBA', (W, H), 'white')
def put(img, code, size, x, y, flip=False):
    e = emoji(code, size)
    if flip: e = e.transpose(Image.FLIP_LEFT_RIGHT)     # mirror (e.g. a car facing the other way)
    img.alpha_composite(e, (int(x), int(y))); return img
def row(codes, size=None, y=None, img=None, gap=20):
    img = img or canvas(); n = len(codes); size = size or min(300, int((W - 40 - gap*(n-1)) / n))
    total = n*size + gap*(n-1); x = (W-total)//2; y = (H-size)//2 if y is None else y
    for c in codes: put(img, c, size, x, y); x += size + gap
    return img
def arrow(img, x1, y1, x2, y2, color=INK, w=9):
    d = ImageDraw.Draw(img); d.line((x1, y1, x2, y2), fill=color, width=w)
    a = math.atan2(y2-y1, x2-x1); L = 26
    p1 = (x2 - L*math.cos(a-0.5), y2 - L*math.sin(a-0.5)); p2 = (x2 - L*math.cos(a+0.5), y2 - L*math.sin(a+0.5))
    d.polygon([(x2, y2), p1, p2], fill=color); return img
def bubble(img, x, y, w, h, text, size=40, tail='left', fill='white', color=INK):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x, y, x+w, y+h), 26, outline=INK, width=5, fill=fill)
    tx = x+46 if tail == 'left' else x+w-80; tip = (tx-8, y+h+40) if tail == 'left' else (tx+42, y+h+40)
    if tail:
        d.polygon([(tx, y+h-3), (tx+34, y+h-3), tip], fill=fill)
        d.line((tx, y+h-2, *tip), fill=INK, width=5); d.line((tx+34, y+h-2, *tip), fill=INK, width=5)
    lines = text.split('\n'); lh = size*1.15; y0 = y+h/2-lh*(len(lines)-1)/2
    for i, t in enumerate(lines): d.text((x+w/2, y0+i*lh), t, font=font(size), fill=color, anchor='mm')
    return img
def label(img, text, y=372, size=40, color=NAVY, x=None):
    ImageDraw.Draw(img).text((W//2 if x is None else x, y), text, font=font(size), fill=color, anchor='mm'); return img
def text(img, x, y, t, size=36, color=INK, anchor='mm'):
    ImageDraw.Draw(img).text((x, y), t, font=font(size), fill=color, anchor=anchor); return img
def sign(img, x, y, w, h, t, size=34, fill=NAVY, color='white', r=12):
    d = ImageDraw.Draw(img); d.rounded_rectangle((x, y, x+w, y+h), r, fill=fill)
    lines = t.split('\n'); lh = size*1.15; y0 = y+h/2-lh*(len(lines)-1)/2
    for i, s in enumerate(lines): d.text((x+w/2, y0+i*lh), s, font=font(size), fill=color, anchor='mm')
    return img
def cross(img, x, y, s=60, color=RED, w=12):
    d = ImageDraw.Draw(img); d.line((x, y, x+s, y+s), fill=color, width=w); d.line((x+s, y, x, y+s), fill=color, width=w); return img
def check(img, x, y, s=60, color=GREEN, w=12):
    d = ImageDraw.Draw(img); d.line((x, y+s*0.55, x+s*0.38, y+s), fill=color, width=w); d.line((x+s*0.38, y+s, x+s, y), fill=color, width=w); return img
def form(img, x, y, w, h, title, fields, hl=None, size=24):
    """A simple paper form: title bar + labeled lines; field index hl is highlighted yellow."""
    d = ImageDraw.Draw(img); d.rounded_rectangle((x, y, x+w, y+h), 10, outline=INK, width=4, fill='white')
    d.rectangle((x+4, y+4, x+w-4, y+44), fill=NAVY); d.text((x+w/2, y+24), title, font=font(24), fill='white', anchor='mm')
    fy = y+62; step = (h-70)/max(1, len(fields))
    for i, f in enumerate(fields):
        if i == hl: d.rectangle((x+10, fy-6, x+w-10, fy+step-12), fill=YEL)
        d.text((x+18, fy+step/2-10), f, font=font(size), fill=INK, anchor='lm'); fy += step
    return img
def save(img, path):
    d = ImageDraw.Draw(img); d.rounded_rectangle((3, 3, W-4, H-4), 24, outline=(180, 190, 200), width=4)
    img.convert('RGB').save(path if path.endswith('.png') else path + '.png', optimize=True)
def glasses(img, x, y, size, color=INK):
    """Draw simple glasses on an emoji face pasted at (x, y) with the given size."""
    d = ImageDraw.Draw(img); r = size*0.12; cy = y + size*0.50; w = max(3, int(size*0.035))
    for cx in (x + size*0.34, x + size*0.66): d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=color, width=w)
    d.line((x + size*0.34 + r, cy, x + size*0.66 - r, cy), fill=color, width=w); return img
def person(img, x, base, head, h=1.0, shirt=(70, 120, 190), size=86, specs=False, pants=(60, 60, 70), num=None):
    """A standing figure: Twemoji head on a drawn body. x = left edge of the head, base = y of the feet, h = height factor
    (1.0 average, 1.25 tall, 0.8 short)."""
    d = ImageDraw.Draw(img); body = int(size*1.05*h); legs = int(size*0.95*h)
    top = base - legs - body - int(size*0.9); cx = x + size/2
    d.rounded_rectangle((cx-size*0.42, top+size*0.86, cx+size*0.42, top+size*0.86+body), 16, fill=shirt)
    lw = int(size*0.16)
    d.line((cx-size*0.18, top+size*0.86+body-4, cx-size*0.2, base), fill=pants, width=lw)
    d.line((cx+size*0.18, top+size*0.86+body-4, cx+size*0.2, base), fill=pants, width=lw)
    put(img, head, size, x, top)
    if specs: glasses(img, x, top, size)
    if num is not None:
        d.ellipse((cx-17, base+6, cx+17, base+40), fill='white', outline=NAVY, width=3)
        d.text((cx, base+23), str(num), font=font(22), fill=NAVY, anchor='mm')
    return img
def big_canvas(w, h): return Image.new('RGBA', (w, h), 'white')
def save_any(img, path):
    w, h = img.size; d = ImageDraw.Draw(img); d.rounded_rectangle((3, 3, w-4, h-4), 24, outline=(180, 190, 200), width=4)
    img.convert('RGB').save(path if path.endswith('.png') else path + '.png', optimize=True)
def run(B, lesson, out):
    """B = list of (name, word, fn, note, kind). Writes the PNGs + images_L3_L<lesson>.json (Twemoji codes recorded while drawing)."""
    import json
    os.makedirs(out, exist_ok=True); meta = []
    for name, word, fn, note, kind in B:
        USED.clear(); img = fn()
        (save if img.size == (W, H) else save_any)(img, f'{out}/{name}')
        meta.append(dict(file=f'{name}.png', lesson=f'Level3-L{lesson}', word=word, kind=kind, twemoji=sorted(USED), note=note))
    json.dump(meta, open(f'{out}/images_L3_L{lesson}.json', 'w'), indent=1, ensure_ascii=False); print(len(meta), 'images')
