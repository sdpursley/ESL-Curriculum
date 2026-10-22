"""Level 3, Lesson 3 pictures: 12 vocabulary cards (600x420) + 1 activity picture (the old photo on the Listening page).
Twemoji (CC BY 4.0) + drawings in code (l3img.py). Usage: python make_images_L3_L3.py OUT_DIR"""
import sys
from PIL import ImageDraw
from l3img import *
OUT = sys.argv[1] if len(sys.argv) > 1 else '..'   # default: level3/drafts/images (never level3/images, which the website publishes)
def childhood():
    img = canvas(); put(img, '1f9d2', 170, 50, 60); arrow(img, 250, 145, 360, 145, GREY, 8); put(img, '1f9d1', 170, 390, 60)
    d = ImageDraw.Draw(img); d.rounded_rectangle((30, 40, 240, 250), 20, outline=GREEN, width=6)
    label(img, 'childhood', 300, 44, GREEN); label(img, '= when you were a child', 360, 30, GREY); return img
def village():
    img = canvas(); put(img, '1f3d8', 230, 40, 40); put(img, '1f333', 140, 290, 130); put(img, '1f333', 120, 430, 150); label(img, 'a small village', 370, 42); return img
def farm():
    img = canvas(); put(img, '1f69c', 190, 30, 80); put(img, '1f404', 170, 230, 100); put(img, '1f33e', 150, 420, 110); label(img, 'farm', 370, 46); return img
def river():
    img = canvas(); d = ImageDraw.Draw(img)
    for k in range(3):
        pts = [(x, 250 + k*28 + 18*math.sin(x/45)) for x in range(20, 590, 10)]; d.line(pts, fill=(60, 140, 220), width=22)
    put(img, '1f333', 130, 40, 90); put(img, '1f333', 110, 420, 110); put(img, '1f6f6', 100, 250, 170); label(img, 'river', 385, 46); return img
def climb():
    img = canvas(); d = ImageDraw.Draw(img); put(img, '1f333', 320, 140, 10)
    d.line((280, 112, 480, 100), fill=(105, 60, 30), width=16)                      # a branch
    person(img, 330, 300, '1f9d2', h=0.7, shirt=(230, 120, 40), size=80)             # a child on the trunk, feet off the ground
    d.line((338, 194, 320, 112), fill=(250, 200, 80), width=12); d.line((402, 194, 420, 106), fill=(250, 200, 80), width=12)   # arms up
    label(img, 'climb trees', 385, 44); return img
def chores():
    img = canvas(); put(img, '1f9f9', 160, 30, 70); put(img, '1f9fa', 160, 220, 80); put(img, '1f37d', 150, 410, 85)
    label(img, 'chores', 300, 46); label(img, 'sweep • wash clothes • wash dishes', 360, 26, GREY); return img
def feed():
    img = canvas(); put(img, '1f9d1-200d-1f33e', 200, 30, 60); put(img, '1f33d', 90, 230, 150); put(img, '1f414', 150, 330, 120); put(img, '1f416', 120, 460, 170)
    label(img, 'feed the animals', 372, 42); return img
def radio():
    img = canvas(); put(img, '1f4fb', 260, 170, 30); put(img, '1f3b5', 90, 470, 50); label(img, 'radio', 370, 46); return img
def letter():
    img = canvas(); put(img, '2709', 220, 50, 60); put(img, '1f4ec', 220, 330, 60); label(img, 'a letter (mail)', 370, 42); return img
def landline():
    img = canvas(); put(img, '260e', 250, 175, 40); label(img, 'landline phone', 370, 42); text(img, 520, 110, 'at\nhome', 30, GREY); return img
def jump_rope():
    img = canvas(); d = ImageDraw.Draw(img)
    person(img, 255, 330, '1f467', h=0.75, shirt=(220, 120, 160), size=90)
    d.ellipse((170, 30, 430, 345), outline=(200, 60, 60), width=7)
    for x in (178, 410): d.rounded_rectangle((x, 215, x+14, 255), 5, fill=(90, 60, 30))
    label(img, 'jump rope', 388, 40); return img
def then_now():
    img = canvas(); d = ImageDraw.Draw(img); d.line((300, 30, 300, 330), fill=(160, 160, 160), width=5)
    text(img, 150, 50, 'THEN', 44, GREY); text(img, 450, 50, 'NOW', 44, NAVY)
    put(img, '1f4fb', 110, 30, 110); put(img, '2709', 110, 160, 110); put(img, '1f4f1', 120, 340, 105); put(img, '1f4bb', 110, 465, 110)
    label(img, 'then  /  now', 370, 42); return img
def old_photo():
    img = big_canvas(1000, 560); d = ImageDraw.Draw(img)
    d.rectangle((40, 30, 960, 530), fill=(240, 228, 200), outline=(150, 120, 80), width=10)
    for k in range(2):
        pts = [(x, 420 + k*26 + 14*math.sin(x/50)) for x in range(60, 945, 10)]; d.line(pts, fill=(120, 160, 190), width=20)
    put(img, '1f3e1', 220, 90, 120); put(img, '1f333', 170, 330, 150); put(img, '1f404', 120, 760, 260)
    put(img, '1f467', 120, 520, 250); put(img, '1f467', 110, 640, 260); return img
B = [
 ('L3_L3_childhood', 'childhood', childhood, 'a child, an arrow, an adult; the child is circled, label "childhood = when you were a child" (frame, arrow, labels drawn)', 'vocab'),
 ('L3_L3_village', 'village', village, 'small houses and trees, label "a small village"', 'vocab'),
 ('L3_L3_farm', 'farm', farm, 'a tractor, a cow and a sheaf of rice/grain, label', 'vocab'),
 ('L3_L3_river', 'river', river, 'a blue river with two trees and a small boat (river drawn)', 'vocab'),
 ('L3_L3_climb_trees', 'climb trees', climb, 'a child climbs a big tree and holds a branch (body, arms, branch drawn), label', 'vocab'),
 ('L3_L3_chores', 'chores', chores, 'broom, laundry basket, plate; labels "chores", "sweep • wash clothes • wash dishes"', 'vocab'),
 ('L3_L3_feed_the_animals', 'feed the animals', feed, 'a farmer, corn, a chicken and a pig, label', 'vocab'),
 ('L3_L3_radio', 'radio', radio, 'an old radio + music notes, label', 'vocab'),
 ('L3_L3_letter', 'letter (mail)', letter, 'an envelope + a mailbox, label "a letter (mail)"', 'vocab'),
 ('L3_L3_landline_phone', 'landline phone', landline, 'a telephone with a cord, label, "at home"', 'vocab'),
 ('L3_L3_jump_rope', 'jump rope', jump_rope, 'a girl inside a turning jump rope (rope drawn), label', 'vocab'),
 ('L3_L3_then_now', 'then / now', then_now, 'THEN: radio and letter | NOW: phone and laptop (dividing line and labels drawn)', 'vocab'),
 ('L3_L3_old_photo', 'Listening picture (an old photo)', old_photo, 'an old photo: a farmhouse, a tree, a cow, a river and two girls (photo frame and river drawn)', 'activity'),
]
if __name__ == '__main__': run(B, 3, OUT)
