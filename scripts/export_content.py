# Exports curriculum content from the approved Markdown (v5 public edition) into src/content.json
# and copies used assets into public/. Reuses the parser from webbuild/build.py.
import json, os, re, shutil
SRC='/workspace/level2_curriculum'; HERE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MDFILE='Level2_Curriculum_v5_public.md'
PUB_DOCS=['Level2_Curriculum_v5_public.pdf','Level2_Curriculum_v5_public.docx']
EXAMS=['Midterm_Exam_Teacher_Packet.pdf','Midterm_Exam_Teacher_Packet.docx','Midterm_Student_Test.pdf',
       'Final_Exam_Teacher_Packet.pdf','Final_Exam_Teacher_Packet.docx','Final_Student_Test.pdf']
code=open(SRC+'/webbuild/build.py',encoding='utf-8').read()
code=code[:code.index('NAV=[')]
g={}; exec(code,g)
g['L']=open(f'{SRC}/{MDFILE}',encoding='utf-8').read().split('\n')   # parser functions read this global
L,find,md,inline,used=g['L'],g['find'],g['md'],g['inline'],g['used_imgs']
def sect(a,b,start=0):
    i=find(a,start); j=find(b,i+1); return L[i+1:j]
data={}
data['semester']=md(sect('## 1. The Semester at a Glance','---'))
data['routine']=md(sect('### 2.1 Clock-time template','### 2.3'),1)
data['teacherGuide']=md(sect('## 5. Teacher Guide','## Lesson 1 ('))
wb=find('## How to Use This Workbook')
data['studentHowTo']=md(L[wb+1:find('## Lesson 1 (',wb)])
titles={1:('Nice to Meet You','be vs. do questions'),2:('A Day in My Life','Simple present, frequency words'),
 3:('Free Time','like / love / hate + -ing'),4:('Right Now','Present continuous'),
 5:('Last Weekend','Past of be; simple past (regular -ed)'),6:('My Story','Irregular past; Did you…?; ago'),
 7:('Getting Around','Comparatives; How long does it take?'),8:('The Best Place in Town','Superlatives; recommending places'),
 9:('Food and Shopping','Count / noncount; some / any; How much / many; I\'d like'),10:('Health','I have a cold; My ___ hurts; should / shouldn\'t'),
 11:('Making Plans','be going to; invitations; present continuous for plans'),12:('Getting Things Done','have to / need to; Can / Could you…?; phone calls'),
 13:('Then, Now, and Next','Past, present, and future together; graduation talk')}
week=lambda n: n if n<=7 else n+1     # Week 8 = midterm, Week 15 = final, Week 16 = graduation
lessons=[]; sizes={}
for n,(t,gram) in titles.items():
    w=week(n); head=f'## Lesson {n} (Week {w})'
    ti=find(f'{head}: {t}'); tj=find('## ',ti+1)
    si=find(f'{head}: {t}',wb)
    p={k:find(f'{head} · {k}',si) for k in ['Listening','Grammar','Homework']}
    end=find('## ',p['Homework']+1)
    words=[]
    for l in L[si+1:p['Listening']]:
        for m in re.finditer(r'!\[([^\]]*)\]\(images/([^)]+)\)<br>(★ )?\*\*(.+?)\*\*',l):
            used.add(m.group(2)); words.append(dict(img='images/'+m.group(2),word=m.group(4),star=bool(m.group(3))))
    mp3=f'{SRC}/audio/L{n}_listening.mp3'
    has_audio=os.path.exists(mp3)
    if has_audio: sizes[f'L{n}_listening.mp3']=os.path.getsize(mp3)
    lessons.append(dict(n=n,title=t,grammar=gram,week=w,words=words,
        audio=f'audio/L{n}_listening.mp3' if has_audio else '',
        listening=md(L[p['Listening']+1:p['Grammar']],1),
        grammarHtml=md(L[p['Grammar']+1:p['Homework']],1),
        homework=md(L[p['Homework']+1:end],1),
        teacher=md(L[ti+1:tj],1)))
data['lessons']=lessons
data['credit']=('Vocabulary pictures use Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The graphics were resized and combined, and arrows, calendars, clocks, and labels were added.')
data['creditHtml']=inline(data['credit'])
data['downloads']={'pdf':PUB_DOCS[0],'docx':PUB_DOCS[1]}
pub=HERE+'/public'
for d in ['images','audio','downloads']:
    shutil.rmtree(f'{pub}/{d}',ignore_errors=True); os.makedirs(f'{pub}/{d}')
os.makedirs(pub+'/downloads/slides',exist_ok=True); os.makedirs(pub+'/downloads/exams',exist_ok=True)
for f in sorted(used): shutil.copy(f'{SRC}/images/{f}',f'{pub}/images/')
for l in lessons:
    if l['audio']: shutil.copy(f'{SRC}/{l["audio"]}',f'{pub}/audio/')
for f in PUB_DOCS:
    shutil.copy(f'{SRC}/{f}',f'{pub}/downloads/'); sizes[f]=os.path.getsize(f'{SRC}/{f}')
slides=[]
for n in titles:  # teacher slide decks, when they exist
    f=f'{SRC}/slides/Lesson{n}_Slides.pptx'
    if os.path.exists(f): shutil.copy(f,f'{pub}/downloads/slides/'); slides.append(n); sizes[f'Lesson{n}_Slides.pptx']=os.path.getsize(f)
exams=[]
for f in EXAMS:   # teacher exam packets + student tests
    s=f'{SRC}/exams/{f}'
    if os.path.exists(s): shutil.copy(s,f'{pub}/downloads/exams/'); sizes[f]=os.path.getsize(s); exams.append(f)
for f in ['Midterm_listening.mp3','Final_listening.mp3']:
    s=f'{SRC}/audio/{f}'
    if os.path.exists(s): shutil.copy(s,f'{pub}/audio/'); sizes[f]=os.path.getsize(s)
json.dump(data,open(HERE+'/src/content.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(sizes,open(HERE+'/src/sizes.json','w'),indent=1)
open(pub+'/.nojekyll','w').close()
print(len(used),'images;',len(lessons),'lessons; audio for',[l['n'] for l in lessons if l['audio']],'; slides',slides,'; exams',exams)
