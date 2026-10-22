"""Level 1, Lesson 4 vocabulary pictures (600x420 PNG cards), same card style as Lessons 1-3.
Emoji graphics: Twemoji (jdecked/twemoji), CC BY 4.0. Light-blue highlight circles, ring line and labels drawn in code.
The person the word names is BIG with a light-blue circle; the other people are small, so the relation is clear.
Run: python make_images_L1_L4.py  -> writes PNGs + images_L1_L4.json into level1/images/ (run it from level1/images/tools/)"""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'lib'))   # level1/images/tools/lib: picture helpers (make_images.py, from tools/images/make_images.py)
from PIL import ImageDraw
import make_images as MI
from make_images import emoji, canvas, font, W, H
OUT = os.path.abspath(os.path.join(HERE, '..'))   # level1/images/
YEL = (255, 224, 102); RED = (200, 40, 40); NAVY = (31, 58, 95); INK = (30, 30, 30)
WOMAN, MAN, GIRL, BOY, BABY, OLDW, OLDM, FAM, RING = '1f469', '1f468', '1f467', '1f466', '1f476', '1f475', '1f474', '1f46a', '1f48d'
HL = (205, 228, 250)
def person(img, code, x, y, size, hl=False):
    """one person; hl = the person the word names (light-blue circle + navy ring behind)"""
    if hl:
        d = ImageDraw.Draw(img); pad = size//9
        d.ellipse((x-pad, y-pad, x+size+pad, y+size+pad), fill=HL, outline=NAVY, width=6)
    img.alpha_composite(emoji(code, size), (x, y))
def layout(items):
    """items: list of (code, size, hl); placed left to right, bottoms aligned, centred on the card"""
    gap = 40; tot = sum(s for _, s, _ in items) + gap*(len(items)-1); x = (W - tot)//2; base = (H + max(s for _, s, _ in items))//2 + 15
    img = canvas()
    for code, size, hl in items:
        person(img, code, x, base - size, size, hl); x += size + gap
    return img
def T(c, s=190): return (c, s, True)
def O(c, s=120): return (c, s, False)
def couple(target, other):
    img = layout([T(target, 190), O(other, 150)])
    img.alpha_composite(emoji(RING, 80), (W//2 - 10, 20)); return img

from PIL import Image
GREY = (120, 120, 120); LINE = (90, 90, 90)
def draw_people(img, d, nodes):
    for key, (code, x, y, label, sub) in nodes.items():
        if code: img.alpha_composite(emoji(code, 110), (x - 55, y - 55))
        else: d.rounded_rectangle((x-60, y-60, x+60, y+60), 14, fill=(245, 247, 250), outline=GREY, width=3)
        if label is None: d.line((x-75, y+100, x+75, y+100), fill=INK, width=3)
        else: d.text((x, y+88), label, font=font(30), fill=NAVY if label.isupper() else INK, anchor='mm')
        if sub: d.text((x, y+122), sub, font=font(24), fill=GREY, anchor='mm')
def family_tree(nodes, pairs, kids, title=None, size=(1000, 660)):
    """pairs: list of (a, b) joined by a line; kids: list of ((a, b), [children]) -> a line down from the pair to each child"""
    img = Image.new('RGBA', size, 'white'); d = ImageDraw.Draw(img)
    d.rounded_rectangle((4, 4, size[0]-5, size[1]-5), 18, outline=(180, 190, 200), width=4)
    if title: d.text((size[0]//2, 38), title, font=font(34), fill=NAVY, anchor='mm')
    for a, b in pairs:
        xa, ya = nodes[a][1:3]; xb, yb = nodes[b][1:3]
        d.line((xa + 68, ya, xb - 68, yb), fill=LINE, width=5)
    for (a, b), ch in kids:
        xa, ya = nodes[a][1:3]; xb = nodes[b][1]; mx = (xa + xb)//2
        ys = [nodes[c][2] for c in ch]; top = min(ys) - 85; d.line((mx, ya, mx, top), fill=LINE, width=5)
        xs = [nodes[c][1] for c in ch]
        if len(ch) > 1 or xs[0] != mx: d.line((min(xs + [mx]), top, max(xs + [mx]), top), fill=LINE, width=5)
        for c in ch: d.line((nodes[c][1], top, nodes[c][1], nodes[c][2] - 62), fill=LINE, width=5)
    draw_people(img, d, nodes); return img
def tree_carlos():
    N = {'gm': (OLDW, 330, 110, None, 'mother'), 'gf': (OLDM, 670, 110, None, 'father'),
         'c': (MAN, 330, 360, 'CARLOS', None), 'w': (WOMAN, 670, 360, None, 'wife'),
         's': (BOY, 250, 610, None, 'son'), 'd': (GIRL, 500, 610, None, 'daughter'), 'b': (BABY, 750, 610, None, 'baby')}
    return family_tree(N, [('gm', 'gf'), ('c', 'w')], [(('gm', 'gf'), ['c']), (('c', 'w'), ['s', 'd', 'b'])], size=(1000, 770))
def tree_blank():
    N = {'m': (None, 330, 100, 'mother', None), 'f': (None, 670, 100, 'father', None),
         'sib': (None, 160, 350, 'brother / sister', None), 'me': (None, 500, 350, 'ME', None), 'sp': (None, 840, 350, 'husband / wife', None),
         'k1': (None, 500, 600, 'son / daughter', None), 'k2': (None, 840, 600, 'son / daughter', None)}
    img = family_tree(N, [('m', 'f'), ('me', 'sp')], [(('m', 'f'), ['sib', 'me']), (('me', 'sp'), ['k1', 'k2'])], size=(1000, 720))
    return img
def card_family():
    N = {'m': (OLDW, 330, 140, 'Lucia, 68', 'mother'), 'f': (OLDM, 670, 140, 'Tomas, 70', 'father'),
         'me': (WOMAN, 330, 390, 'ANA, 35', 'me'), 'h': (MAN, 670, 390, 'Miguel, 37', 'husband'),
         's': (BOY, 380, 640, 'Diego, 9', 'son'), 'd': (GIRL, 620, 640, 'Mia, 4', 'daughter')}
    return family_tree(N, [('m', 'f'), ('me', 'h')], [(('m', 'f'), ['me']), (('me', 'h'), ['s', 'd'])], title="Picture-card family: Ana's family", size=(1000, 800))
B = []
def add(name, word, fn, codes, note, drawn=None): B.append((name, word, fn, codes, note, drawn))
add('L1_L4_mother', 'mother', lambda: layout([T(WOMAN), O(GIRL)]), [WOMAN, GIRL], 'woman (big, blue circle) with her daughter (small)')
add('L1_L4_father', 'father', lambda: layout([T(MAN), O(BOY)]), [MAN, BOY], 'man (big, blue circle) with his son (small)')
add('L1_L4_parents', 'parents', lambda: layout([T(WOMAN, 170), T(MAN, 170), O(GIRL, 105)]), [WOMAN, MAN, GIRL], 'woman + man (big, blue circles) with their child (small)')
add('L1_L4_husband', 'husband', lambda: couple(MAN, WOMAN), [MAN, WOMAN, RING], 'man (big, blue circle), his wife (small), wedding ring')
add('L1_L4_wife', 'wife', lambda: couple(WOMAN, MAN), [WOMAN, MAN, RING], 'woman (big, blue circle), her husband (small), wedding ring')
add('L1_L4_son', 'son', lambda: layout([O(WOMAN, 130), O(MAN, 130), T(BOY, 160)]), [BOY, WOMAN, MAN], 'boy (big, blue circle) with his parents (small)')
add('L1_L4_daughter', 'daughter', lambda: layout([O(WOMAN, 130), O(MAN, 130), T(GIRL, 160)]), [GIRL, WOMAN, MAN], 'girl (big, blue circle) with her parents (small)')
add('L1_L4_children', 'children (kids)', lambda: layout([O(WOMAN, 140), T(GIRL, 150), T(BOY, 150)]), [GIRL, BOY, WOMAN], 'girl + boy (big, blue circles) with their mother (small)')
add('L1_L4_brother', 'brother', lambda: layout([T(BOY, 190), O(GIRL, 140)]), [BOY, GIRL], 'boy (big, blue circle) with his sister (small)')
add('L1_L4_sister', 'sister', lambda: layout([T(GIRL, 190), O(BOY, 140)]), [GIRL, BOY], 'girl (big, blue circle) with her brother (small)')
add('L1_L4_baby', 'baby', lambda: layout([T(BABY, 240)]), [BABY], 'baby (big, blue circle)')
add('L1_L4_grandmother', 'grandmother', lambda: layout([T(OLDW), O(GIRL, 110)]), [OLDW, GIRL], 'old woman (big, blue circle) with her grandchild (small)')
add('L1_L4_grandfather', 'grandfather', lambda: layout([T(OLDM), O(BOY, 110)]), [OLDM, BOY], 'old man (big, blue circle) with his grandchild (small)')
add('L1_L4_family', 'family', lambda: layout([T(MAN, 120), T(WOMAN, 120), T(GIRL, 90), T(BOY, 90)]), [MAN, WOMAN, GIRL, BOY], 'family: man, woman, girl and boy, all with circles')
add('L1_L4_tree_carlos', "Carlos's family tree (listening Task B)", tree_carlos, [OLDW, OLDM, MAN, WOMAN, BOY, GIRL, BABY], 'family tree: Carlos, his parents, his wife and 3 children; blank lines for the names', 'tree lines, blank lines, labels')
add('L1_L4_tree_blank', 'blank family tree (Talk Time)', tree_blank, [], 'empty family tree boxes: mother, father, brother/sister, ME, husband/wife, son/daughter (all drawn)', 'all drawn (boxes, lines, labels)')
add('L1_L4_card_family', "picture-card family (Talk Time option)", card_family, [OLDW, OLDM, WOMAN, MAN, BOY, GIRL], "invented family with names and ages: Lucia 68, Tomas 70, Ana 35, Miguel 37, Diego 9, Mia 4", 'tree lines, names, ages, title')
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); meta = []
    for name, word, fn, codes, note, drawn in B:
        im = fn()
        if im.size == (W, H): MI.save(im, f'{OUT}/{name}')
        else: im.convert('RGB').save(f'{OUT}/{name}.png', optimize=True)   # big trees: own border already drawn
        meta.append(dict(file=f'{name}.png', lesson='Level1-L4', word=word, twemoji=codes, note=note, drawn=drawn or ('light-blue highlight circles' + (' + ring layout' if RING in codes else ''))))
    json.dump(meta, open(f'{OUT}/images_L1_L4.json', 'w'), indent=1, ensure_ascii=False); print(len(meta), 'images')
