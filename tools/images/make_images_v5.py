"""Vocabulary images for Lessons 5-13 (same pipeline as make_images.py).
Emoji graphics: Twemoji (jdecked/twemoji), CC BY 4.0. Composites/drawings made with PIL.
Run: python make_images_v5.py   (does not touch Lessons 1-4 images)
"""
import json, math
from PIL import ImageDraw
import make_images as m
from make_images import emoji, canvas, row, arrow, font, save, W, H

B = {}
def add(name, lesson, word, fn, codes, note=''): B[name] = (lesson, word, fn, codes, note)
def put(img, code, size, x, y): img.alpha_composite(emoji(code, size), (x, y)); return img

def cal(header, highlight=(), circle=None, arrow_from=None, arrow_to=None, check=False):
    img = canvas(); d = ImageDraw.Draw(img)
    days = ['M','T','W','T','F','S','S']; cw = 74; x0 = (W - 7*cw)//2
    d.rounded_rectangle((x0-10, 30, x0+7*cw+10, 330), 20, outline=(30,30,30), width=6, fill='white')
    d.rectangle((x0-10, 30, x0+7*cw+10, 95), fill=(200,40,40))
    d.text((W//2, 63), header, font=font(40), fill='white', anchor='mm')
    for i, dd in enumerate(days):
        x = x0 + i*cw
        d.text((x+cw//2, 130), dd, font=font(38), fill=(30,30,30), anchor='mm')
        hl = i in highlight
        d.rounded_rectangle((x+8, 165, x+cw-8, 290), 10, outline=(30,30,30), width=3, fill=(255,230,120) if hl else 'white')
        if hl and check:
            d.line((x+20, 230, x+34, 252), fill=(20,140,40), width=9); d.line((x+34, 252, x+58, 195), fill=(20,140,40), width=9)
        if circle is not None and i == circle:
            d.ellipse((x-4, 153, x+cw+4, 302), outline=(200,40,40), width=8)
    if arrow_from is not None:
        xa = x0 + arrow_from*cw + cw//2; xb = x0 + arrow_to*cw + cw//2
        y = 370; d.line((xa, y, xb, y), fill=(40,40,40), width=9)
        s = 1 if xb > xa else -1
        d.polygon([(xb, y), (xb-26*s, y-17), (xb-26*s, y+17)], fill=(40,40,40))
    return img

def timeline(mode, label=None):
    img = canvas(); d = ImageDraw.Draw(img)
    d.line((40, 210, 560, 210), fill=(140,140,140), width=8)
    d.ellipse((270, 180, 330, 240), fill=(200,40,40)); d.text((300, 290), 'NOW', font=font(46), fill=(200,40,40), anchor='mm')
    col = (20, 110, 180)
    if mode == 'past':
        d.line((260, 210, 70, 210), fill=col, width=16); d.polygon([(40,210),(85,180),(85,240)], fill=col)
    elif mode == 'future':
        d.line((340, 210, 530, 210), fill=col, width=16); d.polygon([(560,210),(515,180),(515,240)], fill=col)
    elif mode == 'ago':
        d.ellipse((85, 185, 135, 235), fill=col)
        d.arc((110, 60, 300, 330), 200, 340, fill=col, width=10)
        d.polygon([(110,170),(100,130),(140,150)], fill=col)
        d.text((110, 300), label or '', font=font(40), fill=col, anchor='mm')
    return img

def seq(codes, size=140):
    img = canvas(); d = ImageDraw.Draw(img); n = len(codes); gap = (W - n*size)//(n+1)
    x = gap
    for k, c in enumerate(codes):
        put(img, c, size, x, (H-size)//2)
        if k < n-1: arrow(d, x+size+6, H//2, x+size+gap-6, w=7)
        x += size + gap
    return img

def far():
    img = canvas(); d = ImageDraw.Draw(img); put(img,'1f3e0',150,15,90); put(img,'1f3e2',150,435,90)
    for x in range(175, 420, 34): d.line((x, 330, x+18, 330), fill=(40,40,40), width=9)
    arrow(d, 175, 330, 425, both=True, w=9); return img

def price_tags():
    img = canvas(); d = ImageDraw.Draw(img)
    for k, (p, x) in enumerate([('$9', 40), ('$6', 220), ('$3', 400)]):
        d.rounded_rectangle((x, 120, x+160, 240), 18, outline=(30,30,30), width=6, fill=(255,240,200))
        d.text((x+80, 180), p, font=font(70), fill=(30,30,30), anchor='mm')
    d.ellipse((380, 95, 580, 265), outline=(200,40,40), width=9)
    put(img, '1f947', 100, 430, 290); return img

def closest():
    img = canvas(); d = ImageDraw.Draw(img); put(img,'1f3e0',130,10,140)
    for x in (170, 320, 455): put(img,'1f3ea',110,x,155)
    d.ellipse((150, 125, 300, 290), outline=(200,40,40), width=8); put(img,'1f947',90,180,300); return img

def line_of_people():
    img = canvas(); d = ImageDraw.Draw(img)
    for k in range(4): put(img,'1f9cd',150,30+k*95,120)
    put(img,'1f3e4',140,440,130); return img

def hurt_arm():
    img = row(['1f4aa','1fa79'], 230); d = ImageDraw.Draw(img)
    for k in range(3):
        x = 70 + k*40; d.line((x, 60, x+20, 40), fill=(220,30,30), width=8); d.line((x+20, 40, x+5, 20), fill=(220,30,30), width=8)
    return img

# ---------- Lesson 5 ----------
add('L5_last_weekend','L5','last weekend', lambda: cal('LAST WEEK', [5,6]), [], 'calendar labeled LAST WEEK, Saturday + Sunday highlighted (drawn)')
add('L5_yesterday','L5','yesterday', lambda: cal('THIS WEEK', [2], circle=3, arrow_from=3, arrow_to=2), [], 'calendar: today circled, the day before highlighted, arrow back (drawn)')
add('L5_stayed_home','L5','stayed home', lambda: row(['1f3e0','1f6cb'],250), ['1f3e0','1f6cb'], 'house + couch and lamp')
add('L5_cleaned_the_house','L5','cleaned the house', lambda: row(['1f9f9','1f3e0','2728'],170), ['1f9f9','1f3e0','2728'], 'broom, house, sparkles')
add('L5_visited_family','L5','visited family', lambda: row(['1f697','1f3e0','1f475','1f474'],125), ['1f697','1f3e0','1f475','1f474'], 'car, house, grandmother, grandfather')
add('L5_watched_a_movie','L5','watched a movie', lambda: row(['1f3ac','1f37f'],250), ['1f3ac','1f37f'], 'clapper board + popcorn')
add('L5_cooked','L5','cooked', lambda: row(['1f373','1f958'],250), ['1f373','1f958'], 'frying pan + pan of food')
add('L5_walked','L5','walked (in the park)', lambda: row(['1f6b6','1f3de'],250), ['1f6b6','1f3de'], 'person walking + park')
add('L5_called','L5','called (my mom)', lambda: row(['1f4de','1f475'],250), ['1f4de','1f475'], 'phone + older woman')
add('L5_listened_to_music','L5','listened to music', lambda: row(['1f9d1','1f3a7','1f3b6'],170), ['1f9d1','1f3a7','1f3b6'], 'person, headphones, notes')
add('L5_worked','L5','worked', lambda: row(['1f9d1-200d-1f3ed','23f0'],250), ['1f9d1-200d-1f3ed','23f0'], 'factory worker + alarm clock')
add('L5_relaxed','L5','relaxed', lambda: row(['1f60c','1f3d6'],250), ['1f60c','1f3d6'], 'relieved face + beach')
add('L5_fun','L5','fun', lambda: row(['1f973','1f389'],250), ['1f973','1f389'], 'party face + confetti')
add('L5_boring','L5','boring', lambda: row(['1f611','1f4fa'],250), ['1f611','1f4fa'], 'expressionless face + TV')
add('L5_tired','L5','tired', lambda: row(['1f62b','1f4a4'],250), ['1f62b','1f4a4'], 'tired face + zzz')
add('L5_busy','L5','busy', lambda: row(['1f3c3','1f4c5','23f0'],170), ['1f3c3','1f4c5','23f0'], 'running person, calendar, alarm clock')
# ---------- Lesson 6 ----------
add('L6_grew_up','L6','grew up', lambda: seq(['1f476','1f9d2','1f9d1'],130), ['1f476','1f9d2','1f9d1'], 'baby → child → adult (arrows drawn)')
add('L6_went_to_school','L6','went to school', lambda: row(['1f392','1f3eb'],250), ['1f392','1f3eb'], 'backpack + school')
add('L6_got_a_job','L6','got a job', lambda: row(['1f91d','1f4bc'],250), ['1f91d','1f4bc'], 'handshake + briefcase')
add('L6_first_job','L6','first job', lambda: row(['31-20e3','1f4bc'],250), ['31-20e3','1f4bc'], 'number 1 + briefcase')
add('L6_moved','L6','moved (to a new city)', lambda: row(['1f4e6','1f69a','1f3e0'],170), ['1f4e6','1f69a','1f3e0'], 'box, moving truck, house')
add('L6_found_an_apartment','L6','found an apartment', lambda: row(['1f511','1f3e2'],250), ['1f511','1f3e2'], 'key + apartment building')
add('L6_met','L6','met (a friend)', lambda: row(['1f9d1-200d-1f91d-200d-1f9d1','1f44b'],250), ['1f9d1-200d-1f91d-200d-1f9d1','1f44b'], 'two people + waving hand')
add('L6_got_married','L6','got married', lambda: row(['1f470','1f935','1f48d'],170), ['1f470','1f935','1f48d'], 'bride, person in tuxedo, ring')
add('L6_had_a_baby','L6','had a baby', lambda: row(['1f476','1f37c'],250), ['1f476','1f37c'], 'baby + bottle')
add('L6_bought','L6','bought (a car)', lambda: row(['1f4b5','1f697'],250), ['1f4b5','1f697'], 'money + car')
add('L6_learned','L6','learned (English)', lambda: row(['1f9d1-200d-1f393','1f524'],250), ['1f9d1-200d-1f393','1f524'], 'student + ABC letters')
add('L6_felt_nervous','L6','felt nervous', lambda: row(['1f630'],300), ['1f630'], 'anxious face with sweat')
add('L6_felt_happy','L6','felt happy', lambda: row(['1f604'],300), ['1f604'], 'big smile')
add('L6_ago','L6','ago (5 years ago)', lambda: timeline('ago','5 years'), [], 'timeline: NOW, arrow back to a point labeled 5 years (drawn)')
# ---------- Lesson 7 ----------
add('L7_by_bus','L7','by bus', lambda: row(['1f68c'],300), ['1f68c'], 'bus')
add('L7_by_car','L7','by car', lambda: row(['1f697'],300), ['1f697'], 'car')
add('L7_by_bike','L7','by bike', lambda: row(['1f6b2'],300), ['1f6b2'], 'bicycle')
add('L7_on_foot','L7','on foot (walk)', lambda: row(['1f6b6','1f45f'],250), ['1f6b6','1f45f'], 'person walking + shoe')
add('L7_by_train','L7','by train', lambda: row(['1f686'],300), ['1f686'], 'train')
add('L7_by_taxi','L7','by taxi', lambda: row(['1f695'],300), ['1f695'], 'taxi')
add('L7_traffic','L7','traffic', lambda: row(['1f6a6','1f697','1f699','1f695'],125), ['1f6a6','1f697','1f699','1f695'], 'traffic light + many cars')
add('L7_fast','L7','fast', lambda: row(['1f3ce','1f4a8'],250), ['1f3ce','1f4a8'], 'racing car + dash')
add('L7_slow','L7','slow', lambda: row(['1f422'],300), ['1f422'], 'turtle')
add('L7_cheap','L7','cheap', lambda: row(['1fa99','1f44d'],250), ['1fa99','1f44d'], 'coin + thumbs up')
add('L7_expensive','L7','expensive', lambda: row(['1f4b0','1f4b8'],250), ['1f4b0','1f4b8'], 'money bag + money with wings')
add('L7_far','L7','far', far, ['1f3e0','1f3e2'], 'house and building with a long dotted arrow (drawn)')
def crowded():
    img = canvas(); put(img,'1f68c',230,15,95)
    pts = [(260,60),(330,40),(400,60),(470,45),(290,180),(360,165),(430,180),(500,170),(320,290),(400,280),(480,290)]
    for (x,y) in pts: put(img,'1f9cd',95,x,y)
    return img
add('L7_crowded','L7','crowded', crowded, ['1f68c','1f9cd'], 'bus + a crowd of people')
add('L7_comfortable','L7','comfortable', lambda: row(['1f6cb','1f60c'],250), ['1f6cb','1f60c'], 'couch + relaxed face')
add('L7_how_long','L7','How long does it take?', lambda: row(['23f1','1f68c','2753'],170), ['23f1','1f68c','2753'], 'stopwatch, bus, question mark')
# ---------- Lesson 8 ----------
add('L8_park','L8','park', lambda: row(['1f3de','1f333'],250), ['1f3de','1f333'], 'park + tree')
add('L8_library','L8','library', lambda: row(['1f3db','1f4da'],250), ['1f3db','1f4da'], 'public building + books')
add('L8_supermarket','L8','supermarket', lambda: row(['1f3ec','1f6d2'],250), ['1f3ec','1f6d2'], 'store building + cart')
add('L8_restaurant','L8','restaurant', lambda: row(['1f37d','1f35d'],250), ['1f37d','1f35d'], 'plate with fork and knife + pasta')
add('L8_clinic','L8','clinic', lambda: row(['1f3e5'],300), ['1f3e5'], 'hospital/clinic building')
add('L8_pharmacy','L8','pharmacy', lambda: row(['1f48a','1f3ea'],250), ['1f48a','1f3ea'], 'pill + store')
add('L8_laundromat','L8','laundromat', lambda: row(['1f9fa','1f455','1fae7'],170), ['1f9fa','1f455','1fae7'], 'laundry basket, shirt, bubbles')
add('L8_bank','L8','bank', lambda: row(['1f3e6','1f4b5'],250), ['1f3e6','1f4b5'], 'bank + money')
add('L8_post_office','L8','post office', lambda: row(['1f3e4','2709'],250), ['1f3e4','2709'], 'post office + envelope')
add('L8_gas_station','L8','gas station', lambda: row(['26fd','1f697'],250), ['26fd','1f697'], 'fuel pump + car')
add('L8_bakery','L8','bakery', lambda: row(['1f956','1f950','1f35e'],170), ['1f956','1f950','1f35e'], 'baguette, croissant, bread')
add('L8_the_best','L8','the best', lambda: row(['1f3c6','1f947'],250), ['1f3c6','1f947'], 'trophy + gold medal')
add('L8_the_cheapest','L8','the cheapest', price_tags, ['1f947'], 'three price tags $9 $6 $3, the $3 tag circled (drawn) + gold medal')
add('L8_the_closest','L8','the closest', closest, ['1f3e0','1f3ea','1f947'], 'house and three stores; the nearest store circled (drawn) + medal')
# ---------- Lesson 9 ----------
add('L9_apples','L9','apples', lambda: row(['1f34e','1f34e','1f34e'],170), ['1f34e'], 'three apples')
add('L9_bananas','L9','bananas', lambda: row(['1f34c','1f34c'],250), ['1f34c'], 'bananas')
add('L9_tomatoes','L9','tomatoes', lambda: row(['1f345','1f345','1f345'],170), ['1f345'], 'three tomatoes')
add('L9_onions','L9','onions', lambda: row(['1f9c5','1f9c5'],250), ['1f9c5'], 'onions')
add('L9_eggs','L9','eggs', lambda: row(['1f95a','1f95a','1f95a'],170), ['1f95a'], 'three eggs')
add('L9_rice','L9','rice', lambda: row(['1f35a'],300), ['1f35a'], 'bowl of rice')
add('L9_bread','L9','bread', lambda: row(['1f35e'],300), ['1f35e'], 'bread')
add('L9_milk','L9','milk', lambda: row(['1f95b'],300), ['1f95b'], 'glass of milk')
add('L9_cheese','L9','cheese', lambda: row(['1f9c0'],300), ['1f9c0'], 'cheese')
add('L9_chicken','L9','chicken', lambda: row(['1f357'],300), ['1f357'], 'chicken leg')
add('L9_coffee','L9','coffee', lambda: row(['2615'],300), ['2615'], 'hot coffee')
add('L9_water','L9','water', lambda: row(['1f6b0','1f4a7'],250), ['1f6b0','1f4a7'], 'drinking-water tap + drop')
add('L9_soup','L9','soup', lambda: row(['1f372'],300), ['1f372'], 'pot of soup')
add('L9_sandwich','L9','sandwich', lambda: row(['1f96a'],300), ['1f96a'], 'sandwich')
add('L9_shopping_list','L9','shopping list', lambda: row(['1f4dd','1f6d2'],250), ['1f4dd','1f6d2'], 'list + cart')
add('L9_the_check','L9','the check (the bill)', lambda: row(['1f9fe','1f4b3'],250), ['1f9fe','1f4b3'], 'receipt + credit card')
# ---------- Lesson 10 ----------
add('L10_headache','L10','a headache', lambda: row(['1f915'],300), ['1f915'], 'face with head bandage')
add('L10_stomachache','L10','a stomachache', lambda: row(['1f922'],300), ['1f922'], 'nauseated face')
add('L10_fever','L10','a fever', lambda: row(['1f912','1f321'],250), ['1f912','1f321'], 'face with thermometer + thermometer')
add('L10_cold','L10','a cold', lambda: row(['1f927','1f9fb'],250), ['1f927','1f9fb'], 'sneezing face + tissue roll')
add('L10_cough','L10','a cough', lambda: row(['1f637','1f4a8'],250), ['1f637','1f4a8'], 'face with mask + puff of air')
add('L10_sore_throat','L10','a sore throat', lambda: row(['1f616','1f9e3','1f375'],170), ['1f616','1f9e3','1f375'], 'pained face, scarf, hot tea')
add('L10_toothache','L10','a toothache', lambda: row(['1f9b7','1f623'],250), ['1f9b7','1f623'], 'tooth + pained face')
add('L10_hurts','L10','hurts (My arm hurts.)', hurt_arm, ['1f4aa','1fa79'], 'arm + bandage, red pain marks (drawn)')
add('L10_doctor','L10','doctor', lambda: row(['1f9d1-200d-2695-fe0f','1fa7a'],250), ['1f9d1-200d-2695-fe0f','1fa7a'], 'health worker + stethoscope')
add('L10_dentist','L10','dentist', lambda: row(['1f9b7','1faa5'],250), ['1f9b7','1faa5'], 'tooth + toothbrush')
add('L10_medicine','L10','medicine', lambda: row(['1f48a','1f944'],250), ['1f48a','1f944'], 'pill + spoon')
add('L10_appointment','L10','appointment', lambda: row(['1f4c5','1f552','1f9d1-200d-2695-fe0f'],170), ['1f4c5','1f552','1f9d1-200d-2695-fe0f'], 'calendar, clock, health worker')
add('L10_rest','L10','rest', lambda: row(['1f6cc','1f634'],250), ['1f6cc','1f634'], 'person in bed + sleeping face')
add('L10_drink_water','L10','drink water', lambda: row(['1f9d1','1f6b0','1f4a7'],170), ['1f9d1','1f6b0','1f4a7'], 'person, drinking-water tap, drop')
# ---------- Lesson 11 ----------
add('L11_tonight','L11','tonight', lambda: row(['1f303','1f557'],250), ['1f303','1f557'], 'night city + 8 o’clock')
add('L11_tomorrow','L11','tomorrow', lambda: cal('THIS WEEK', [4], circle=3, arrow_from=3, arrow_to=4), [], 'calendar: today circled, next day highlighted, arrow forward (drawn)')
add('L11_this_weekend','L11','this weekend', lambda: cal('THIS WEEK', [5,6], circle=None), [], 'calendar labeled THIS WEEK, Saturday + Sunday highlighted (drawn)')
add('L11_next_week','L11','next week', lambda: cal('NEXT WEEK', [0,1,2,3,4,5,6]), [], 'calendar labeled NEXT WEEK, all days highlighted (drawn)')
add('L11_go_to_the_movies','L11','go to the movies', lambda: row(['1f3ac','1f39f'],250), ['1f3ac','1f39f'], 'clapper board + tickets')
add('L11_have_a_party','L11','have a party', lambda: row(['1f389','1f388','1f382'],170), ['1f389','1f388','1f382'], 'confetti, balloon, cake')
add('L11_have_a_picnic','L11','have a picnic', lambda: row(['1f9fa','1f96a','1f333'],170), ['1f9fa','1f96a','1f333'], 'basket, sandwich, tree')
add('L11_go_to_the_beach','L11','go to the beach', lambda: row(['1f3d6'],300), ['1f3d6'], 'beach with umbrella')
add('L11_watch_a_game','L11','watch a game', lambda: row(['1f3df','1f4fa'],250), ['1f3df','1f4fa'], 'stadium + TV')
add('L11_visit_friends','L11','visit friends', lambda: row(['1f9d1-200d-1f91d-200d-1f9d1','1f3e0'],250), ['1f9d1-200d-1f91d-200d-1f9d1','1f3e0'], 'two people + house')
add('L11_invite','L11','invite', lambda: row(['1f4e9','1f389'],250), ['1f4e9','1f389'], 'envelope with arrow + confetti')
add('L11_free','L11','free (not busy)', lambda: row(['1f193','1f4c5'],250), ['1f193','1f4c5'], 'FREE button + calendar')
add('L11_id_love_to','L11',"I'd love to!", lambda: row(['1f603','1f44d'],250), ['1f603','1f44d'], 'happy face + thumbs up')
add('L11_sorry_i_cant','L11',"Sorry, I can't.", lambda: row(['1f615','1f645'],250), ['1f615','1f645'], 'confused face + person gesturing no')
# ---------- Lesson 12 ----------
add('L12_pay_a_bill','L12','pay a bill', lambda: row(['1f4a1','1f9fe','1f4b3'],170), ['1f4a1','1f9fe','1f4b3'], 'light bulb (electric bill), bill, card')
add('L12_mail_a_package','L12','mail a package', lambda: row(['1f4e6','1f4ee'],250), ['1f4e6','1f4ee'], 'package + mailbox')
add('L12_fill_out_a_form','L12','fill out a form', lambda: row(['1f4dd','270d'],250), ['1f4dd','270d'], 'form with pencil + writing hand')
add('L12_make_a_phone_call','L12','make a phone call', lambda: row(['1f9d1','1f4de'],250), ['1f9d1','1f4de'], 'person + phone')
add('L12_leave_a_message','L12','leave a message', lambda: row(['1f4f1','1f5e3'],250), ['1f4f1','1f5e3'], 'mobile phone + speaking head')
add('L12_id_card','L12','ID card', lambda: row(['1faaa'],300), ['1faaa'], 'identification card')
add('L12_receipt','L12','receipt', lambda: row(['1f6cd','1f9fe'],250), ['1f6cd','1f9fe'], 'shopping bags + receipt')
add('L12_account_number','L12','account number', lambda: row(['1f522','1f3e6'],250), ['1f522','1f3e6'], 'numbers + bank')
add('L12_customer_service','L12','customer service', lambda: row(['1f9d1-200d-1f4bc','260e'],250), ['1f9d1-200d-1f4bc','260e'], 'office worker + telephone')
add('L12_fix','L12','fix (the sink)', lambda: row(['1f527','1f6b0'],250), ['1f527','1f6b0'], 'wrench + faucet')
add('L12_wait_in_line','L12','wait in line', line_of_people, ['1f9cd','1f3e4'], 'four people in a line at a counter')
add('L12_repeat','L12','Could you repeat that?', lambda: row(['1f442','1f501','2753'],170), ['1f442','1f501','2753'], 'ear, repeat arrows, question mark')
add('L12_spell','L12','Can you spell that?', lambda: row(['1f520','2753'],250), ['1f520','2753'], 'capital letters ABCD + question mark')
add('L12_due_date','L12','due date', lambda: row(['1f4c5','2757'],250), ['1f4c5','2757'], 'calendar + exclamation mark')
# ---------- Lesson 13 ----------
add('L13_in_the_past','L13','in the past', lambda: timeline('past'), [], 'timeline, arrow pointing back from NOW (drawn)')
add('L13_now','L13','now', lambda: timeline('now'), [], 'timeline with NOW dot (drawn)')
add('L13_in_the_future','L13','in the future', lambda: timeline('future'), [], 'timeline, arrow pointing forward from NOW (drawn)')
add('L13_dream','L13','dream', lambda: row(['1f4ad','1f3e1'],250), ['1f4ad','1f3e1'], 'thought bubble + house with garden')
add('L13_goal','L13','goal', lambda: row(['1f3af'],300), ['1f3af'], 'target / bullseye')
add('L13_learn','L13','learn', lambda: row(['1f9d1-200d-1f393','1f4da'],250), ['1f9d1-200d-1f393','1f4da'], 'student + books')
add('L13_improve','L13','improve', lambda: row(['1f4c8'],300), ['1f4c8'], 'chart going up')
add('L13_practice','L13','practice', lambda: row(['1f5e3','1f501'],250), ['1f5e3','1f501'], 'speaking head + repeat arrows')
add('L13_proud','L13','proud', lambda: row(['1f60a','1f3c5'],250), ['1f60a','1f3c5'], 'smiling face + medal')
add('L13_give_a_talk','L13','give a talk', lambda: row(['1f9cd','1f399','1f44f'],170), ['1f9cd','1f399','1f44f'], 'person, studio microphone, clapping hands')
add('L13_graduate','L13','graduate', lambda: row(['1f393','1f4dc'],250), ['1f393','1f4dc'], 'graduation cap + certificate scroll')
add('L13_next_step','L13','next step', lambda: row(['1f463','27a1'],250), ['1f463','27a1'], 'footprints + right arrow')

if __name__ == '__main__':
    old = [x for x in json.load(open('images.json')) if x['lesson'] in ('L1','L2','L3','L4')]
    meta = []; bad = []
    for name, (lesson, word, fn, codes, note) in B.items():
        try:
            save(fn(), name); meta.append(dict(file=f'{name}.png', lesson=lesson, word=word, twemoji=codes, note=note))
        except Exception as e:
            bad.append((name, str(e)))
    json.dump(old + meta, open('images.json','w'), indent=1, ensure_ascii=False)
    print(len(meta), 'new images;', len(bad), 'failed', bad)
