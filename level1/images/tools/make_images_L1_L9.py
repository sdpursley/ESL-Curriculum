"""Level 1, Lesson 9 vocabulary pictures (600x420). Twemoji CC BY 4.0; calendar, months strip, appointment card drawn.
Run: python make_images_L1_L9.py [OUT_DIR]
"""
import os, sys, json
HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, os.path.join(HERE, 'lib'))
from PIL import ImageDraw
import make_images as MI
from make_images import emoji, canvas, font, calendar as MI_cal, W, H
OUT=os.path.abspath(sys.argv[1]) if len(sys.argv)>1 else os.path.abspath(os.path.join(HERE, '..'))
INK=(30,30,30); NAVY=(31,58,95); RED=(200,40,40); GREY=(120,120,120); YEL=(255,224,102); BLUE=(100,160,230)

def one(code,size=280):
    img=canvas(); img.alpha_composite(emoji(code,size),((W-size)//2,(H-size)//2)); return img
def two(a,b,sa=180,sb=180):
    img=canvas(); gap=24; tot=sa+sb+gap; x=(W-tot)//2; y=(H-max(sa,sb))//2
    img.alpha_composite(emoji(a,sa),(x,y)); img.alpha_composite(emoji(b,sb),(x+sa+gap,y)); return img

def calendar_card():
    img=MI_cal(highlight=set(), check=False, circle=None)
    # overlay date label
    d=ImageDraw.Draw(img)
    d.rounded_rectangle((200,340,400,400),10,fill=YEL,outline=RED,width=3)
    d.text((300,370),'calendar',font=font(28),fill=INK,anchor='mm'); return img

def month_card():
    img=canvas(); d=ImageDraw.Draw(img)
    d.rounded_rectangle((80,80,520,300),16,fill=NAVY,outline=INK,width=4)
    d.text((300,150),'MONTH',font=font(40),fill='white',anchor='mm')
    d.text((300,230),'May',font=font(64),fill=YEL,anchor='mm'); return img

def date_card():
    img=canvas(); d=ImageDraw.Draw(img)
    img.alpha_composite(emoji('1f4c5',160),(40,80))
    d.rounded_rectangle((240,100,560,300),14,fill=YEL,outline=RED,width=4)
    d.text((400,160),'May 5th',font=font(48),fill=INK,anchor='mm')
    d.text((400,240),'5/5',font=font(40),fill=NAVY,anchor='mm'); return img

def birthday():
    return two('1f382','1f388',200,180)

def appointment():
    img=canvas(); d=ImageDraw.Draw(img)
    d.rounded_rectangle((60,40,540,380),14,fill='white',outline=INK,width=5)
    d.rectangle((63,43,537,110),fill=NAVY)
    d.text((300,76),'APPOINTMENT',font=font(32),fill='white',anchor='mm')
    rows=[('Day','Thursday'),('Date','May 10'),('Time','10:30')]
    y=140
    for a,b in rows:
        d.text((100,y),a,font=font(28),fill=GREY,anchor='lm')
        d.text((500,y),b,font=font(32),fill=NAVY,anchor='rm'); y+=70
    return img

def today():
    img=canvas(); d=ImageDraw.Draw(img)
    img.alpha_composite(emoji('1f4c5',180),(40,100))
    d.rounded_rectangle((260,120,560,300),14,fill=(100,180,100),outline=INK,width=4)
    d.text((410,210),'TODAY',font=font(48),fill='white',anchor='mm'); return img

def tomorrow():
    img=canvas(); d=ImageDraw.Draw(img)
    img.alpha_composite(emoji('1f4c5',180),(40,100))
    d.rounded_rectangle((260,120,560,300),14,fill=BLUE,outline=INK,width=4)
    d.text((410,210),'TOMORROW',font=font(36),fill='white',anchor='mm'); return img

def months():
    img=canvas(); d=ImageDraw.Draw(img)
    names=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for i,n in enumerate(names):
        x=30+(i%4)*145; y=40+(i//4)*120
        d.rounded_rectangle((x,y,x+130,y+90),10,fill=(234,241,248),outline=NAVY,width=3)
        d.text((x+65,y+45),n,font=font(32),fill=NAVY,anchor='mm')
    return img

B=[]
def add(name,word,fn,codes,note,drawn='border only'): B.append((name,word,fn,codes,note,drawn))
add('L1_L9_calendar','calendar',calendar_card,['1f4c5'] if False else [],'week calendar strip (drawn)','all drawn (calendar)')
# calendar uses drawn from MI_cal - no twemoji required; still list 1f4c5 as related? MI_cal is all drawn
add('L1_L9_month','month',month_card,[],'MONTH / May label (drawn)','all drawn (text)')
add('L1_L9_date','date',date_card,['1f4c5'],'calendar + May 5th / 5/5','date label')
add('L1_L9_birthday','birthday',birthday,['1f382','1f388'],'cake + balloon')
add('L1_L9_appointment','appointment',appointment,[],'appointment card: Thursday, May 10, 10:30 (drawn)','all drawn (card + text)')
add('L1_L9_today','today',today,['1f4c5'],'calendar + TODAY label','label')
add('L1_L9_tomorrow','tomorrow',tomorrow,['1f4c5'],'calendar + TOMORROW label','label')
add('L1_L9_sunny','sunny',lambda: one('2600'),['2600'],'sun')
add('L1_L9_rainy','rainy',lambda: one('1f327'),['1f327'],'cloud with rain')
add('L1_L9_cold','cold',lambda: one('1f976'),['1f976'],'cold face')
add('L1_L9_hot','hot',lambda: one('1f975'),['1f975'],'hot face')
add('L1_L9_months','months (Jan–Dec)',months,[],'12 month tiles January–December (drawn)','all drawn (tiles + text)')
add('L1_L9_ordinals','ordinals 1st–5th',lambda: __import__('PIL').Image.new('RGBA',(1,1)),[],'placeholder')

# Fix calendar twemoji and ordinals + cold/hot codes
# Check 1f975 1f976 1f327
if __name__=='__main__':
    # rebuild B without placeholder ordinals - draw ordinals
    def ordinals():
        img=canvas(); d=ImageDraw.Draw(img)
        for i,lab in enumerate(['1st','2nd','3rd','4th','5th']):
            x=40+i*110; d.rounded_rectangle((x,140,x+95,280),12,fill=(234,241,248),outline=NAVY,width=4)
            d.text((x+47,210),lab,font=font(36),fill=NAVY,anchor='mm')
        return img
    B=[t for t in B if t[0]!='L1_L9_ordinals' and t[0]!='L1_L9_calendar']
    B.insert(0,('L1_L9_calendar','calendar',calendar_card,[],'week calendar strip (drawn)','all drawn (calendar)'))
    B.append(('L1_L9_ordinals','ordinals 1st–5th',ordinals,[],'tiles 1st 2nd 3rd 4th 5th (drawn)','all drawn (tiles + text)'))
    # verify weather codes
    for c in ['1f327','1f975','1f976','2600']:
        try: emoji(c,32)
        except Exception as e:
            print('missing',c,e)
    os.makedirs(OUT,exist_ok=True); meta=[]
    for name,word,fn,codes,note,drawn in B:
        MI.save(fn(),f'{OUT}/{name}')
        meta.append(dict(file=f'{name}.png',lesson='Level1-L9',word=word,twemoji=codes,note=note,drawn=drawn))
    json.dump(meta,open(f'{OUT}/images_L1_L9.json','w'),indent=1,ensure_ascii=False)
    print(len(meta),'images ->',OUT)
