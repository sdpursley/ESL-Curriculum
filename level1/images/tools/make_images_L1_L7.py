"""Level 1, Lesson 7 vocabulary pictures (mostly 600x420 PNG cards; play money 1000x700; receipt page 1000x560).
Emoji graphics: Twemoji (jdecked/twemoji), CC BY 4.0. Clothes recolored in code (HLS); receipts, play money, color swatches, price tags and near/far lines drawn.
Rewritten Oct 21, 2026 after the original build/ folder was removed; regenerates the approved PNGs in images/.
Run: python make_images_L1_L7.py [OUT_DIR]
"""
import os, sys, json, colorsys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, 'lib'))
from PIL import Image, ImageDraw, ImageEnhance
import make_images as MI
from make_images import emoji, canvas, font, W, H
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(HERE, '..'))
INK = (30, 30, 30); NAVY = (31, 58, 95); RED = (200, 40, 40); GREY = (120, 120, 120)
GREEN = (40, 140, 60); YEL = (240, 200, 40); BLUE = (40, 100, 200)

COLORS = {
    'red': (200, 40, 40), 'blue': (40, 100, 200), 'black': (30, 30, 30),
    'white': (245, 245, 245), 'green': (40, 140, 60), 'yellow': (240, 200, 40),
}

def recolor(im, rgb):
    """Map Twemoji colored pixels toward a target RGB (HLS). White items get a grey outline."""
    import numpy as np
    a = np.array(im.convert('RGBA'), dtype=np.float32)
    out = a.copy()
    r, g, b, al = a[:,:,0], a[:,:,1], a[:,:,2], a[:,:,3]
    mx = np.maximum(np.maximum(r, g), b); mn = np.minimum(np.minimum(r, g), b)
    l = (mx + mn) / (2 * 255.0)
    delta = (mx - mn) / 255.0
    s = np.zeros_like(l)
    mask = delta > 0
    s[mask & (l <= 0.5)] = (delta[mask & (l <= 0.5)]) / (2*l[mask & (l <= 0.5)] + 1e-6)
    s[mask & (l > 0.5)] = (delta[mask & (l > 0.5)]) / (2 - 2*l[mask & (l > 0.5)] + 1e-6)
    th, ts, tv = colorsys.rgb_to_hls(*(c/255 for c in rgb))
    # colored pixels: remap hue/sat, keep lightness
    colored = (al >= 20) & (mx >= 40) & (s >= 0.08)
    # near-white fills
    near_white = (al >= 20) & (mx >= 40) & (s < 0.08) & (l > 0.85)
    def hls_to_rgb_arr(h, ll, ss):
        # vectorized-ish via python list for changed pixels only
        ys, xs = np.where(h)
        for y, x in zip(ys, xs):
            nr, ng, nb = colorsys.hls_to_rgb(th, float(ll[y,x]), float(ss[y,x]))
            out[y, x, 0] = nr*255; out[y, x, 1] = ng*255; out[y, x, 2] = nb*255
    ll = np.clip(l * 0.9 + tv * 0.1, 0.15, 0.85)
    ss = np.full_like(l, max(0.35, ts))
    hls_to_rgb_arr(colored, ll, ss)
    if rgb == (245, 245, 245):
        out[near_white, 0:3] = 235
        edge = (al > 20) & (al < 220)
        out[edge, 0:3] = 160
    else:
        ll2 = np.clip(l, 0.25, 0.75); ss2 = np.full_like(l, max(0.4, ts))
        hls_to_rgb_arr(near_white, ll2, ss2)
    return Image.fromarray(out.astype(np.uint8), 'RGBA')

def put(img, im_or_code, size=None, x=0, y=0):
    if isinstance(im_or_code, str):
        im = emoji(im_or_code, size)
    else:
        im = im_or_code
        if size and im.size[0] != size:
            im = im.resize((size, size), Image.Resampling.LANCZOS)
    img.alpha_composite(im, (int(x), int(y))); return img

def cloth(code, color, size=260):
    return recolor(emoji(code, size), COLORS[color])

def card_one(code, color=None, size=280):
    img = canvas(); im = cloth(code, color, size) if color else emoji(code, size)
    img.alpha_composite(im, ((W-im.size[0])//2, (H-im.size[1])//2)); return img

def shoes_pair(color, size=160):
    img = canvas(); im = cloth('1f45f', color, size)
    img.alpha_composite(im, (W//2 - size - 10, (H-size)//2))
    img.alpha_composite(im, (W//2 + 10, (H-size)//2)); return img

def dollar():
    img = canvas(); put(img,'1f4b5',220,40,100)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((300, 140, 560, 280), 14, fill=YEL, outline=RED, width=4)
    d.text((430, 185), '$1', font=font(48), fill=INK, anchor='mm')
    d.text((430, 240), 'one dollar', font=font(28), fill=NAVY, anchor='mm'); return img

def cent():
    img = canvas(); put(img,'1fa99',180,40,120)
    d = ImageDraw.Draw(img)
    d.text((380, 140), '1¢', font=font(56), fill=NAVY, anchor='mm')
    d.text((380, 210), 'one cent', font=font(28), fill=INK, anchor='mm')
    d.text((380, 280), '100¢ = $1', font=font(28), fill=GREY, anchor='mm'); return img

def coin():
    img = canvas()
    for i, x in enumerate((80, 240, 400)): put(img,'1fa99',140,x,140)
    return img

def cash():
    img = canvas(); put(img,'1f4b5',200,60,80); put(img,'1fa99',120,320,200); put(img,'1fa99',100,450,220); return img

def credit_card(): return card_one('1f4b3', size=300)

def receipt_small():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((120, 30, 480, 390), 8, fill='white', outline=INK, width=4)
    d.text((300, 60), 'RECEIPT', font=font(28), fill=NAVY, anchor='mm')
    rows = [('pants', '$15'), ('shirt', '$10'), ('TOTAL', '$25'), ('cash', '$30'), ('change', '$5')]
    y = 110
    for a, b in rows:
        bold = a == 'TOTAL'
        d.text((150, y), a, font=font(28 if not bold else 32), fill=INK if not bold else NAVY, anchor='lm')
        d.text((450, y), b, font=font(28 if not bold else 32), fill=INK if not bold else NAVY, anchor='rm')
        if bold: d.line((150, y-15, 450, y-15), fill=GREY, width=2)
        y += 50
    return img

def colors():
    img = canvas(); d = ImageDraw.Draw(img)
    names = ['red','blue','black','white','green','yellow']
    for i, n in enumerate(names):
        x = 40 + (i % 3) * 190; y = 40 + (i // 3) * 190
        fill = COLORS[n]
        outline = GREY if n == 'white' else INK
        d.rounded_rectangle((x, y, x+160, y+120), 14, fill=fill, outline=outline, width=4)
        d.text((x+80, y+150), n, font=font(28), fill=NAVY, anchor='mm')
    return img

def this_that():
    img = canvas(); d = ImageDraw.Draw(img)
    d.line((300, 30, 300, 390), fill=GREY, width=3)
    # near: big red shirt + hand
    put(img, '1f449', 90, 30, 100)
    img.alpha_composite(cloth('1f455','red',180), (120, 70))
    d.text((150, 300), 'this shirt', font=font(28), fill=NAVY, anchor='mm')
    d.text((150, 340), '(near)', font=font(22), fill=GREY, anchor='mm')
    # far: small blue
    put(img, '1f449', 55, 330, 130)
    img.alpha_composite(cloth('1f455','blue',100), (400, 120))
    d.text((450, 300), 'that shirt', font=font(28), fill=NAVY, anchor='mm')
    d.text((450, 340), '(far)', font=font(22), fill=GREY, anchor='mm')
    return img

def these_those():
    img = canvas(); d = ImageDraw.Draw(img)
    d.line((300, 30, 300, 390), fill=GREY, width=3)
    put(img, '1f449', 90, 20, 90)
    im = cloth('1f45f','black',110)
    img.alpha_composite(im, (100, 100)); img.alpha_composite(im, (180, 100))
    d.text((160, 300), 'these shoes', font=font(26), fill=NAVY, anchor='mm')
    d.text((160, 340), '(near)', font=font(22), fill=GREY, anchor='mm')
    put(img, '1f449', 50, 340, 120)
    im2 = cloth('1f45f','white',70)
    img.alpha_composite(im2, (400, 140)); img.alpha_composite(im2, (460, 140))
    d.text((450, 300), 'those shoes', font=font(26), fill=NAVY, anchor='mm')
    d.text((450, 340), '(far)', font=font(22), fill=GREY, anchor='mm')
    return img

def price_tag(img, price, x=420, y=40):
    d = ImageDraw.Draw(img)
    d.polygon([(x,y),(x+140,y),(x+140,y+70),(x+20,y+70),(x,y+50)], fill=YEL, outline=RED)
    d.ellipse((x+5, y+25, x+20, y+40), fill='white', outline=RED, width=2)
    d.text((x+80, y+35), price, font=font(36), fill=INK, anchor='mm'); return img

def store_item(code, color, price=None, shoes=False):
    if shoes:
        img = shoes_pair(color, 150)
    else:
        img = card_one(code, color, 260)
    if price: price_tag(img, price)
    return img

def play_money():
    img = Image.new('RGBA', (1000, 700), 'white'); d = ImageDraw.Draw(img)
    d.rounded_rectangle((3,3,996,696), 18, outline=(180,190,200), width=4)
    bills = [('$1', GREEN), ('$5', (30,100,60)), ('$10', (20,80,50)), ('$20', (15,70,40))]
    for i, (lab, col) in enumerate(bills):
        for j in range(2):
            x = 40 + i*240; y = 40 + j*150
            d.rounded_rectangle((x, y, x+200, y+120), 10, fill=col, outline=INK, width=3)
            d.text((x+100, y+45), lab, font=font(40), fill='white', anchor='mm')
            d.text((x+100, y+90), 'PLAY MONEY', font=font(16), fill=(200,255,200), anchor='mm')
    coins = [('25¢', (200,160,40)), ('10¢', (180,180,190)), ('5¢', (180,120,60)), ('1¢', (200,100,50))]
    for i, (lab, col) in enumerate(coins):
        for j in range(2):
            x = 80 + i*230; y = 380 + j*140; r = 50
            d.ellipse((x-r, y-r, x+r, y+r), fill=col, outline=INK, width=3)
            d.text((x, y-8), lab, font=font(28), fill=INK, anchor='mm')
            d.text((x, y+22), 'PLAY', font=font(14), fill=GREY, anchor='mm')
    return img.convert('RGB')

def receipt_page():
    img = Image.new('RGBA', (1000, 560), 'white'); d = ImageDraw.Draw(img)
    d.rounded_rectangle((3,3,996,556), 18, outline=(180,190,200), width=4)
    d.rounded_rectangle((200, 30, 800, 520), 8, fill='white', outline=INK, width=4)
    d.text((500, 70), 'MAIN STREET CLOTHES', font=font(28), fill=NAVY, anchor='mm')
    d.text((500, 110), 'RECEIPT', font=font(24), fill=GREY, anchor='mm')
    rows = [('jacket', '$40'), ('dress', '$25'), ('2 shirts', '$18'), ('TOTAL', '$83'), ('cash', '$100'), ('change', '$17')]
    y = 160
    for a, b in rows:
        bold = a == 'TOTAL'
        d.text((240, y), a, font=font(30 if not bold else 34), fill=NAVY if bold else INK, anchor='lm')
        d.text((760, y), b, font=font(30 if not bold else 34), fill=NAVY if bold else INK, anchor='rm')
        if bold: d.line((240, y-12, 760, y-12), fill=GREY, width=2)
        y += 50
    return img.convert('RGB')

B = []
def add(name, word, fn, codes, note, drawn='border only', save_raw=False):
    B.append((name, word, fn, codes, note, drawn, save_raw))

add('L1_L7_dollar','dollar',dollar,['1f4b5'],'banknote + "$1 one dollar" label','label')
add('L1_L7_cent','cent',cent,['1fa99'],'coin + "1¢ one cent" and "100¢ = $1"','labels')
add('L1_L7_coin','coin',coin,['1fa99'],'three coins')
add('L1_L7_cash','cash',cash,['1f4b5','1fa99'],'bills and coins')
add('L1_L7_credit_card','credit card',credit_card,['1f4b3'],'credit card')
add('L1_L7_receipt','receipt',receipt_small,[],'store receipt: pants $15, shirt $10, total $25, cash $30, change $5','all drawn (receipt + text)')
add('L1_L7_shirt','shirt',lambda: card_one('1f455','blue'),['1f455'],'blue shirt')
add('L1_L7_pants','pants',lambda: card_one('1f456','black'),['1f456'],'pants, recolored black','recolor')
add('L1_L7_shoes','shoes',lambda: shoes_pair('red'),['1f45f'],'two red shoes','recolor + two copies')
add('L1_L7_jacket','jacket',lambda: card_one('1f9e5','green'),['1f9e5'],'jacket, recolored green','recolor')
add('L1_L7_dress','dress',lambda: card_one('1f457','yellow'),['1f457'],'dress, recolored yellow','recolor')
add('L1_L7_colors','colors',colors,[],'six color swatches with names: red, blue, black, white, green, yellow','all drawn (swatches + text)')
add('L1_L7_this_that','this / that',this_that,['1f449','1f455'],'hand pointing to a near red shirt (this) and a far blue shirt (that)','recolor, labels, near/far line')
add('L1_L7_these_those','these / those',these_those,['1f449','1f45f'],'hand pointing to near black shoes (these) and far white shoes (those)','recolor, labels, near/far line')
add('L1_L7_shirt_red','red shirt (listening choice)',lambda: card_one('1f455','red'),['1f455'],'red shirt','recolor')
add('L1_L7_shirt_blue','blue shirt (listening choice)',lambda: card_one('1f455','blue'),['1f455'],'blue shirt','recolor')
add('L1_L7_shirt_white','white shirt (listening choice)',lambda: card_one('1f455','white'),['1f455'],'white shirt','recolor')
add('L1_L7_shoes_black','black shoes (listening choice)',lambda: shoes_pair('black'),['1f45f'],'black shoes','recolor + two copies')
add('L1_L7_shoes_white','white shoes (listening choice)',lambda: shoes_pair('white'),['1f45f'],'white shoes','recolor + two copies')
add('L1_L7_shoes_red','red shoes (listening choice)',lambda: shoes_pair('red'),['1f45f'],'red shoes','recolor + two copies')
add('L1_L7_store1_dress_price','store 1: red dress with price tag',lambda: store_item('1f457','red','$25'),['1f457'],'red dress with a price tag $25','recolor + price tag')
add('L1_L7_store1_dress','store 1: red dress, no price',lambda: store_item('1f457','red'),['1f457'],'red dress','recolor')
add('L1_L7_store1_pants_price','store 1: black pants with price tag',lambda: store_item('1f456','black','$18'),['1f456'],'black pants with a price tag $18','recolor + price tag')
add('L1_L7_store1_pants','store 1: black pants, no price',lambda: store_item('1f456','black'),['1f456'],'black pants','recolor')
add('L1_L7_store1_shoes_price','store 1: white shoes with price tag',lambda: store_item('1f45f','white','$35',shoes=True),['1f45f'],'white shoes with a price tag $35','recolor + price tag')
add('L1_L7_store1_shoes','store 1: white shoes, no price',lambda: store_item('1f45f','white',shoes=True),['1f45f'],'white shoes','recolor')
add('L1_L7_store2_jacket_price','store 2: green jacket with price tag',lambda: store_item('1f9e5','green','$40'),['1f9e5'],'green jacket with a price tag $40','recolor + price tag')
add('L1_L7_store2_jacket','store 2: green jacket, no price',lambda: store_item('1f9e5','green'),['1f9e5'],'green jacket','recolor')
add('L1_L7_store2_shirt_price','store 2: yellow shirt with price tag',lambda: store_item('1f455','yellow','$9'),['1f455'],'yellow shirt with a price tag $9','recolor + price tag')
add('L1_L7_store2_shirt','store 2: yellow shirt, no price',lambda: store_item('1f455','yellow'),['1f455'],'yellow shirt','recolor')
add('L1_L7_store2_pants_price','store 2: blue pants with price tag',lambda: store_item('1f456','blue','$22'),['1f456'],'blue pants with a price tag $22','recolor + price tag')
add('L1_L7_store2_pants','store 2: blue pants, no price',lambda: store_item('1f456','blue'),['1f456'],'blue pants','recolor')
add('L1_L7_play_money','play money page',play_money,[],'printable play money: $1, $5, $10, $20 bills and 25¢, 10¢, 5¢, 1¢ coins, all marked PLAY MONEY','all drawn', True)
add('L1_L7_receipt_page','receipt (Letters & Numbers)',receipt_page,[],'receipt: jacket $40, dress $25, 2 shirts $18, total $83, cash $100, change $17','all drawn', True)

if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); meta = []
    for name, word, fn, codes, note, drawn, save_raw in B:
        im = fn()
        if save_raw:
            im.convert('RGB').save(f'{OUT}/{name}.png', optimize=True)
        else:
            MI.save(im if im.mode=='RGBA' else im.convert('RGBA'), f'{OUT}/{name}')
        meta.append(dict(file=f'{name}.png', lesson='Level1-L7', word=word, twemoji=codes, note=note, drawn=drawn))
    json.dump(meta, open(f'{OUT}/images_L1_L7.json', 'w'), indent=1, ensure_ascii=False)
    print(len(meta), 'images ->', OUT)
