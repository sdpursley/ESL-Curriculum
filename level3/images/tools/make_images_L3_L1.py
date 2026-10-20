"""Level 3, Lesson 1 vocabulary pictures (600x420 PNG cards), same helpers and style as Levels 1-2 (make_images.py).
Emoji graphics: Twemoji (jdecked/twemoji), CC BY 4.0. Speech bubbles, signs and labels drawn in code.
Run from this folder (level3/images/tools/): python make_images_L3_L1.py  -> writes L3_L1_*.png + images_L3_L1.json into level3/images/
The Level 2 helpers come from tools/images/make_images.py; Twemoji SVGs are downloaded into ./_twemoji_src/ (not committed)."""
import os, sys, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools', 'images')))
from PIL import ImageDraw
import make_images as MI
from make_images import emoji, row, canvas, font, W, H
OUT = os.path.abspath(os.path.join(HERE, '..'))   # level3/images/
INK = (30, 30, 30); NAVY = (31, 58, 95); RED = (200, 40, 40); GREEN = (20, 130, 60)
def put(img, code, size, x, y): img.alpha_composite(emoji(code, size), (x, y))
def bubble(img, x, y, w, h, text, size=40, tail='left', fill='white', color=INK):
    d = ImageDraw.Draw(img)
    d.rounded_rectangle((x, y, x+w, y+h), 26, outline=INK, width=5, fill=fill)
    tx = x+46 if tail == 'left' else x+w-80; tip = (tx-8, y+h+40) if tail == 'left' else (tx+42, y+h+40)
    d.polygon([(tx, y+h-3), (tx+34, y+h-3), tip], fill=fill)
    d.line((tx, y+h-2, *tip), fill=INK, width=5); d.line((tx+34, y+h-2, *tip), fill=INK, width=5)
    lines = text.split('\n'); lh = size*1.15; y0 = y+h/2-lh*(len(lines)-1)/2
    for i, t in enumerate(lines): d.text((x+w/2, y0+i*lh), t, font=font(size), fill=color, anchor='mm')
def label(img, text, y=372, size=40, color=NAVY):
    ImageDraw.Draw(img).text((W//2, y), text, font=font(size), fill=color, anchor='mm')
def neighbor():
    img = canvas(); put(img, '1f3e0', 190, 40, 40); put(img, '1f3e1', 190, 370, 40)
    put(img, '1f469', 130, 70, 230); put(img, '1f44b', 80, 200, 250)
    put(img, '1f468', 130, 400, 230); put(img, '1f44b', 80, 320, 250)
    ImageDraw.Draw(img).line((300, 70, 300, 380), fill=(150, 150, 150), width=5); return img
def coworker():
    img = canvas(); put(img, '1f469-200d-1f373', 210, 70, 50); put(img, '1f468-200d-1f373', 210, 320, 50)
    d = ImageDraw.Draw(img); d.rounded_rectangle((40, 280, 560, 312), 8, fill=(181, 136, 99)); label(img, 'same job, same place', 360, 34); return img
def small_talk():
    img = canvas(); put(img, '1f469', 150, 50, 240); put(img, '1f468', 150, 400, 240); put(img, '2600', 90, 255, 270)
    bubble(img, 20, 25, 270, 150, 'Nice day,\nisn\'t it?', 38); bubble(img, 330, 50, 250, 120, 'Yes, it is!', 38, tail='right'); return img
def follow_up():
    img = canvas(); put(img, '1f469', 140, 40, 255); put(img, '1f468', 140, 420, 255)
    bubble(img, 15, 20, 330, 110, 'I got a new job.', 36)
    bubble(img, 250, 150, 335, 95, 'Really? Where?', 38, tail='right', fill=(255, 236, 160))
    put(img, '2753', 80, 260, 300); return img
def reason():
    img = canvas(); put(img, '1f914', 150, 30, 50); put(img, '1f4a1', 150, 420, 40)
    d = ImageDraw.Draw(img); d.text((300, 120), 'Why?', font=font(70), fill=RED, anchor='mm')
    d.rounded_rectangle((40, 230, 560, 380), 22, outline=NAVY, width=6, fill=(234, 241, 248))
    d.text((300, 285), 'Because it\'s cheap.', font=font(42), fill=NAVY, anchor='mm')
    d.text((300, 340), '= the reason', font=font(32), fill=(90, 90, 90), anchor='mm'); return img
def good_news():
    img = canvas(); put(img, '1f604', 200, 60, 40); put(img, '1f389', 200, 330, 40); label(img, 'Good news!', 340, 60, GREEN); return img
def bad_news():
    img = canvas(); put(img, '1f61f', 200, 60, 40); put(img, '1f327', 200, 330, 40); label(img, 'Bad news…', 340, 60, RED); return img
def chat():
    img = canvas(); put(img, '1f9d1', 170, 40, 200); put(img, '1f469', 170, 390, 200); put(img, '1f4ac', 150, 225, 30)
    put(img, '2615', 90, 255, 290); return img
def introduce():
    img = canvas(); put(img, '1f468', 140, 30, 230); put(img, '1f449', 80, 175, 270); put(img, '1f469', 140, 260, 230); put(img, '1f9d1', 140, 430, 230)
    bubble(img, 15, 20, 330, 120, 'This is Ana.', 42); bubble(img, 330, 40, 255, 110, 'Nice to\nmeet you!', 36, tail='right'); return img
def community_center():
    img = canvas(); put(img, '1f3e2', 230, 40, 70); put(img, '1f9d1-200d-1f91d-200d-1f9d1', 170, 370, 150)
    d = ImageDraw.Draw(img); d.rounded_rectangle((60, 20, 540, 80), 12, fill=NAVY)
    d.text((300, 50), 'COMMUNITY CENTER', font=font(38), fill='white', anchor='mm')
    d.text((470, 370), 'classes • events', font=font(26), fill=(90, 90, 90), anchor='mm'); return img
def volunteer():
    img = canvas(); put(img, '1f64b-200d-2640-fe0f', 200, 40, 60); put(img, '1f4e6', 140, 270, 150); put(img, '1f96b', 120, 430, 170)
    d = ImageDraw.Draw(img); d.rounded_rectangle((60, 300, 280, 360), 12, fill=GREEN); d.text((170, 330), 'VOLUNTEER', font=font(32), fill='white', anchor='mm')
    d.text((420, 60), 'helps for free', font=font(30), fill=(90, 90, 90), anchor='mm'); return img
def get_along():
    img = canvas(); put(img, '1f60a', 150, 40, 70); put(img, '1f91d', 170, 215, 130); put(img, '1f604', 150, 410, 70)
    label(img, 'friendly together', 360, 38); return img
B = []
def add(name, word, fn, codes, note): B.append((name, word, fn, codes, note))
add('L3_L1_neighbor', 'neighbor', neighbor, ['1f3e0', '1f3e1', '1f469', '1f468', '1f44b'], 'two houses side by side; a woman and a man in front wave to each other (dividing line drawn)')
add('L3_L1_coworker', 'coworker', coworker, ['1f469-200d-1f373', '1f468-200d-1f373'], 'two cooks at the same counter, label "same job, same place" (counter + label drawn)')
add('L3_L1_small_talk', 'small talk', small_talk, ['1f469', '1f468', '2600'], 'two people, sun, speech bubbles "Nice day, isn\'t it?" / "Yes, it is!" (drawn)')
add('L3_L1_follow_up_question', 'follow-up question', follow_up, ['1f469', '1f468', '2753'], 'bubble "I got a new job." then highlighted bubble "Really? Where?" + question mark (bubbles drawn)')
add('L3_L1_reason', 'reason', reason, ['1f914', '1f4a1'], 'thinking face + light bulb; "Why?" and a box "Because it\'s cheap. = the reason" (drawn)')
add('L3_L1_good_news', 'good news', good_news, ['1f604', '1f389'], 'happy face + party popper, label "Good news!"')
add('L3_L1_bad_news', 'bad news', bad_news, ['1f61f', '1f327'], 'worried face + rain cloud, label "Bad news…"')
add('L3_L1_chat', 'chat', chat, ['1f9d1', '1f469', '1f4ac', '2615'], 'two people, speech balloon, coffee cup')
add('L3_L1_introduce', 'introduce', introduce, ['1f468', '1f449', '1f469', '1f9d1'], 'a man points to a woman and introduces her to a third person; bubbles "This is Ana." / "Nice to meet you!" (drawn)')
add('L3_L1_community_center', 'community center', community_center, ['1f3e2', '1f9d1-200d-1f91d-200d-1f9d1'], 'building + two people holding hands, sign "COMMUNITY CENTER", "classes • events" (drawn)')
add('L3_L1_volunteer', 'volunteer', volunteer, ['1f64b-200d-2640-fe0f', '1f4e6', '1f96b'], 'woman raising her hand, boxes and canned food, green "VOLUNTEER" badge, "helps for free" (drawn)')
add('L3_L1_get_along', 'get along', get_along, ['1f60a', '1f91d', '1f604'], 'two smiling faces + handshake, label "friendly together"')
if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True); meta = []
    for name, word, fn, codes, note in B:
        MI.save(fn(), f'{OUT}/{name}'); meta.append(dict(file=f'{name}.png', lesson='Level3-L1', word=word, twemoji=codes, note=note))
    json.dump(meta, open(f'{OUT}/images_L3_L1.json', 'w'), indent=1, ensure_ascii=False); print(len(meta), 'images')
