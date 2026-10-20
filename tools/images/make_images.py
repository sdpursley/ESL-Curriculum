"""Builds vocabulary images for Lessons 1-4.
Emoji graphics: Twemoji (jdecked/twemoji), CC BY 4.0. Composites/drawings made with PIL.
"""
import os, io, json, urllib.request
import cairosvg
from PIL import Image, ImageDraw, ImageFont
SRC = '_twemoji_src'   # download cache for the Twemoji SVGs (created on first run)
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

# ---------- Lesson 1 ----------
add('L1_from','L1','from', lambda: (lambda i: (i.alpha_composite(emoji('1f4cd',150),(330,40)), i)[1])(row(['1f30e'],300)), ['1f30e','1f4cd'], 'globe + location pin')
add('L1_live','L1','live (I live on…)', lambda: row(['1f9cd','1f3e0'],250), ['1f9cd','1f3e0'], 'person + house')
add('L1_work','L1','work', lambda: row(['1f477','1f9d1-200d-1f4bc'],250), ['1f477','1f9d1-200d-1f4bc'], 'construction worker + office worker')
add('L1_job','L1','job', lambda: row(['1f9d1-200d-1f373','1f9d1-200d-1f527','1f9d1-200d-1f3eb'],170), ['1f9d1-200d-1f373','1f9d1-200d-1f527','1f9d1-200d-1f3eb'], 'cook, mechanic, teacher')
add('L1_neighborhood','L1','neighborhood', lambda: row(['1f3d8','1f333','1f3ea'],170), ['1f3d8','1f333','1f3ea'], 'houses, tree, corner store')
def married_single():
    img = row(['1f491'],230, y=60); img2 = canvas()
    img2.alpha_composite(emoji('1f491',220),(40,70)); img2.alpha_composite(emoji('1f48d',90),(170,280))
    img2.alpha_composite(emoji('1f9cd',220),(350,70))
    d = ImageDraw.Draw(img2); d.line((300,50,300,370), fill=(150,150,150), width=5)
    d.text((150,390),'married',font=font(34),fill=(30,30,30),anchor='mb'); d.text((460,390),'single',font=font(34),fill=(30,30,30),anchor='mb')
    return img2
add('L1_married_single','L1','married / single', married_single, ['1f491','1f48d','1f9cd'], 'couple + ring | one person (small labels)')
add('L1_kids','L1','kids (children)', lambda: row(['1f467','1f466','1f9d2'],170), ['1f467','1f466','1f9d2'], 'girl, boy, child')
def siblings():
    img = canvas(); d = ImageDraw.Draw(img)
    img.alpha_composite(emoji('1f468',120),(170,20)); img.alpha_composite(emoji('1f469',120),(310,20))
    d.line((300,140,300,190), fill=(60,60,60), width=6); d.line((150,190,450,190), fill=(60,60,60), width=6)
    d.line((150,190,150,215), fill=(60,60,60), width=6); d.line((450,190,450,215), fill=(60,60,60), width=6)
    img.alpha_composite(emoji('1f466',150),(75,215)); img.alpha_composite(emoji('1f467',150),(375,215))
    d.text((150,405),'brother',font=font(32),fill=(30,30,30),anchor='mb'); d.text((450,405),'sister',font=font(32),fill=(30,30,30),anchor='mb')
    return img
add('L1_brother_sister','L1','brother / sister', siblings, ['1f468','1f469','1f466','1f467'], 'family tree: parents, then a boy and a girl (small labels)')
def hometown():
    img = row(['1f3d8'],260, y=110); img.alpha_composite(emoji('1f4cd',120),(240,10)); img.alpha_composite(emoji('1f476',110),(470,290)); return img
add('L1_hometown','L1','hometown', hometown, ['1f3d8','1f4cd','1f476'], 'town + pin + baby (where you were born / grew up)')
def near():
    img = canvas(); img.alpha_composite(emoji('1f3e0',200),(95,110)); img.alpha_composite(emoji('1f3eb',200),(305,110))
    d = ImageDraw.Draw(img); arrow(d,200,350,400,both=True); return img
add('L1_near','L1','near', near, ['1f3e0','1f3eb'], 'house close to a school, short two-way arrow')
add('L1_nice_to_meet_you','L1','Nice to meet you', lambda: row(['1f642','1f91d','1f60a'],170), ['1f642','1f91d','1f60a'], 'two smiling faces + handshake')
add('L1_what_about_you','L1','What about you?', lambda: row(['1faf5','2753'],250), ['1faf5','2753'], 'finger pointing at you + question mark')

# ---------- Lesson 2 ----------
add('L2_get_up','L2','get up', lambda: row(['23f0','1f971'],250), ['23f0','1f971'], 'alarm clock + yawning face')
add('L2_take_a_shower','L2','take a shower', lambda: row(['1f6bf','1f9fc'],250), ['1f6bf','1f9fc'], 'shower + soap')
add('L2_get_dressed','L2','get dressed', lambda: row(['1f455','1f456','1f45f'],170), ['1f455','1f456','1f45f'], 'shirt, jeans, shoes')
add('L2_have_breakfast','L2','have breakfast', lambda: row(['1f305','1f963','2615'],170), ['1f305','1f963','2615'], 'sunrise, cereal bowl, coffee')
add('L2_take_the_bus','L2','take the bus', lambda: row(['1f9cd','1f68c'],250), ['1f9cd','1f68c'], 'person + bus')
add('L2_drive','L2','drive', lambda: row(['1f697'],300), ['1f697'], 'car')
add('L2_start_work','L2','start work', lambda: row(['1f556','1f3e2'],250), ['1f556','1f3e2'], 'seven o’clock + workplace building')
add('L2_take_a_break','L2','take a break', lambda: row(['2615','1f36a','1fa91'],170), ['2615','1f36a','1fa91'], 'coffee, cookie, chair')
def pickup():
    img = canvas(); img.alpha_composite(emoji('1f3eb',170),(20,120)); d = ImageDraw.Draw(img); arrow(d,200,210,280)
    img.alpha_composite(emoji('1f467',130),(290,140)); img.alpha_composite(emoji('1f466',130),(420,140)); return img
add('L2_pick_up_the_kids','L2','pick up the kids', pickup, ['1f3eb','1f467','1f466'], 'school → kids')
add('L2_cook_dinner','L2','cook dinner', lambda: row(['1f9d1-200d-1f373','1f372'],250), ['1f9d1-200d-1f373','1f372'], 'cook + pot of food')
add('L2_do_the_dishes','L2','do the dishes', lambda: row(['1f37d','1f9fd','1fae7'],170), ['1f37d','1f9fd','1fae7'], 'plate, sponge, bubbles')
add('L2_go_to_bed','L2','go to bed', lambda: row(['1f6cc','1f319'],250), ['1f6cc','1f319'], 'person in bed + moon')
add('L2_every_day','L2','every day', lambda: calendar(range(7)), [], 'calendar, all 7 days checked (drawn)')
add('L2_on_weekends','L2','on weekends', lambda: calendar([5,6]), [], 'calendar, Saturday + Sunday highlighted (drawn)')
add('L2_in_the_morning','L2','in the morning', lambda: row(['1f305'],300), ['1f305'], 'sunrise')
add('L2_at_night','L2','at night', lambda: row(['1f303','1f319'],250), ['1f303','1f319'], 'night city with stars + moon')

# ---------- Lesson 3 ----------
add('L3_soccer','L3','soccer', lambda: row(['26bd','1f945'],250), ['26bd','1f945'], 'ball + goal')
add('L3_cooking','L3','cooking', lambda: row(['1f9d1-200d-1f373','1f373'],250), ['1f9d1-200d-1f373','1f373'], 'cook + frying pan')
add('L3_dancing','L3','dancing', lambda: row(['1f483','1f57a'],250), ['1f483','1f57a'], 'woman and man dancing')
add('L3_shopping','L3','shopping', lambda: row(['1f6d2','1f6cd'],250), ['1f6d2','1f6cd'], 'cart + shopping bags')
add('L3_cleaning','L3','cleaning', lambda: row(['1f9f9','1f9fd','1faa3'],170), ['1f9f9','1f9fd','1faa3'], 'broom, sponge, bucket')
add('L3_gardening','L3','gardening', lambda: row(['1f9d1-200d-1f33e','1f331','1f33b'],170), ['1f9d1-200d-1f33e','1f331','1f33b'], 'gardener, seedling, sunflower')
add('L3_fixing_things','L3','fixing things', lambda: row(['1f9d1-200d-1f527','1f6e0'],250), ['1f9d1-200d-1f527','1f6e0'], 'mechanic + tools')
add('L3_watching_tv','L3','watching TV / movies', lambda: row(['1f4fa','1f37f'],250), ['1f4fa','1f37f'], 'TV + popcorn')
add('L3_walking','L3','walking', lambda: row(['1f6b6','1f333'],250), ['1f6b6','1f333'], 'person walking + tree')
add('L3_reading','L3','reading', lambda: row(['1f9d1','1f4d6'],250), ['1f9d1','1f4d6'], 'person + open book')
def videocall():
    img = canvas(); d = ImageDraw.Draw(img)
    d.rounded_rectangle((200,30,400,390), 30, outline=(30,30,30), width=10, fill=(225,240,255))
    img.alpha_composite(emoji('1f600',150),(225,110)); img.alpha_composite(emoji('1f44b',110),(420,150)); return img
add('L3_video_calls','L3','video calls', videocall, ['1f600','1f44b'], 'smiling face on a phone screen + waving hand (phone drawn)')
add('L3_music','L3','music', lambda: row(['1f3a7','1f3b6'],250), ['1f3a7','1f3b6'], 'headphones + music notes')
add('L3_kind_of','L3','What kind of (music)?', lambda: (lambda i: (i.alpha_composite(emoji('2753',120),(470,10)), i)[1])(row(['1f3b8','1f3ba','1f941','1f3bb'],120)), ['1f3b8','1f3ba','1f941','1f3bb','2753'], 'guitar, trumpet, drum, violin + question mark')

# ---------- Lesson 4 ----------
add('L4_waiting_for_the_bus','L4','waiting (for the bus)', lambda: row(['1f9cd','1f68f','231b'],170), ['1f9cd','1f68f','231b'], 'person, bus stop, hourglass')
add('L4_cooking','L4','cooking (now)', lambda: row(['1f9d1-200d-1f373','1f373'],250), ['1f9d1-200d-1f373','1f373'], 'same as L3 cooking')
add('L4_working_late','L4','working late', lambda: row(['1f9d1-200d-1f4bb','1f319'],250), ['1f9d1-200d-1f4bb','1f319'], 'person at laptop + moon')
add('L4_doing_homework','L4','doing homework', lambda: row(['1f9d2','1f4dd','1f4da'],170), ['1f9d2','1f4dd','1f4da'], 'child, memo with pencil, books')
add('L4_watching_tv','L4','watching TV', lambda: row(['1f4fa','1f37f'],250), ['1f4fa','1f37f'], 'same as L3')
add('L4_looking_at','L4','looking at', lambda: row(['1f440','1f4c4'],250), ['1f440','1f4c4'], 'eyes + page')
add('L4_calling','L4','calling (on the phone)', lambda: row(['1f4de','1f4f1'],250), ['1f4de','1f4f1'], 'phone receiver + mobile phone')
def coming():
    img = canvas(); img.alpha_composite(emoji('1f68d',260),(40,80)); img.alpha_composite(emoji('1f9cd',200),(380,140)); return img
add('L4_coming','L4','coming (The bus is coming.)', coming, ['1f68d','1f9cd'], 'oncoming bus + waiting person')
def rightnow():
    img = canvas(); d = ImageDraw.Draw(img); d.line((40,230,560,230), fill=(120,120,120), width=8)
    d.ellipse((260,190,340,270), fill=(200,40,40)); d.text((300,150),'NOW',font=font(80),fill=(200,40,40),anchor='mb')
    img.alpha_composite(emoji('1f9d1-200d-1f373',110),(245,280)); return img
add('L4_right_now','L4','right now', rightnow, ['1f9d1-200d-1f373'], 'timeline with a red dot labeled NOW (drawn) + cook')
add('L4_today','L4','today', lambda: calendar([], check=False, circle=3), [], 'calendar with one day circled (drawn)')
add('L4_what_time','L4','What time is it? (It’s 5:45.)', lambda: clock(5,45,'?'), [], 'clock showing 5:45 + question mark (drawn)')

if __name__ == '__main__':
    meta = []
    for name, (lesson, word, fn, codes, note) in B.items():
        save(fn(), name); meta.append(dict(file=f'{name}.png', lesson=lesson, word=word, twemoji=codes, note=note))
    json.dump(meta, open('images.json','w'), indent=1, ensure_ascii=False)
    print(len(meta), 'images')
