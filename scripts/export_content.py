# Exports curriculum content from the approved Markdown (v5 public edition) into src/content.json and src/sizes.json,
# and the Level 1 and Level 3 pages (level1/curriculum/*.md, level3/curriculum/*.md) into src/content_level1.json and
# src/content_level3.json (see export_level() at the end).
# Usage (from the repo root): python3 scripts/export_content.py
# Reads curriculum/Level2_Curriculum_v5_public.md. Media already live in public/ (images/, audio/, downloads/);
# run curriculum/build.sh --publish first if you changed the curriculum text and want fresh PDF/DOCX downloads.
import json, os, re, shutil
HERE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MDPATH=os.environ.get('CURRICULUM_MD', os.path.join(HERE,'curriculum','Level2_Curriculum_v5_public.md'))
pub=HERE+'/public'
PUB_DOCS=['Level2_Curriculum_v5_public.pdf','Level2_Curriculum_v5_public.docx']
EXAMS=['Midterm_Exam_Teacher_Packet.pdf','Midterm_Exam_Teacher_Packet.docx','Midterm_Student_Test.pdf',
       'Final_Exam_Teacher_Packet.pdf','Final_Exam_Teacher_Packet.docx','Final_Student_Test.pdf']
g={}; exec(open(os.path.join(HERE,'scripts','md_parser.py'),encoding='utf-8').read(),g)
g['L']=open(MDPATH,encoding='utf-8').read().split('\n')   # parser functions read this global
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
    mp3=f'{pub}/audio/L{n}_listening.mp3'
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
missing=[f for f in sorted(used) if not os.path.exists(f'{pub}/images/{f}')]
if missing: raise SystemExit(f'Missing images in public/images/: {missing}')
for f in PUB_DOCS: sizes[f]=os.path.getsize(f'{pub}/downloads/{f}')
slides=[]
for n in titles:  # teacher slide decks, when they exist (the .pptx files in public/downloads/slides/ are the source)
    f=f'{pub}/downloads/slides/Lesson{n}_Slides.pptx'
    if os.path.exists(f): slides.append(n); sizes[f'Lesson{n}_Slides.pptx']=os.path.getsize(f)
exams=[]
for f in EXAMS:   # teacher exam packets + student tests
    s=f'{pub}/downloads/exams/{f}'
    if os.path.exists(s): sizes[f]=os.path.getsize(s); exams.append(f)
for f in ['Midterm_listening.mp3','Final_listening.mp3']:
    s=f'{pub}/audio/{f}'
    if os.path.exists(s): sizes[f]=os.path.getsize(s)
json.dump(data,open(HERE+'/src/content.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
json.dump(sizes,open(HERE+'/src/sizes.json','w'),indent=1)
open(pub+'/.nojekyll','w').close()
print(len(used),'images;',len(lessons),'lessons; audio for',[l['n'] for l in lessons if l['audio']],'; slides',slides,'; exams',exams)

# ------------------------------------------------------------- Levels 1 and 3 -------------------------------------------------------------
# Level 1 and Level 3 are built one lesson at a time and use the same page layout. For level <V> (1 or 3):
# Sources (edit these):  level<V>/curriculum/Level<V>_Scope_and_Sequence.md   lesson list, titles, weeks, semester table, weekly routine
#                        level<V>/curriculum/Level<V>_Lesson<N>.md            one file per finished lesson (Lesson 1 is the model)
#                        level<V>/images/*.png (+ CREDITS.md), level<V>/audio/<audio name>, level<V>/slides/Level<V>_Lesson<N>_Slides.pptx
#                        audio name: Level 1 = L1_listening.mp3 (Lesson 1) and L1_L<N>_listening.mp3 (Lessons 2+), Level 3 = L3_L<N>_listening.mp3
# The website copies (public/level<V>/images, audio, downloads/slides) are refreshed from those folders by this script.
# PDF/DOCX downloads come from level<V>/curriculum/build.sh <N> --publish (into public/level<V>/downloads/).
# A lesson in the scope and sequence without a Level<V>_Lesson<N>.md file is listed as "coming soon"; if its slide deck
# (level<V>/slides/Level<V>_Lesson<N>_Slides.pptx) exists, it also gets 'slides' + a PowerPoint download (slides-only lesson).
# Output: src/content_level<V>.json
LEVELS={
 1:dict(audio=lambda n:'L1_listening.mp3' if n==1 else f'L1_L{n}_listening.mp3', audio_re=r'^L1_(L\d+_)?listening\.mp3$',
        routine_end='> **Timing is loose',
        credit=('Vocabulary pictures use Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), licensed under '
                'CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The graphics were resized and combined, and ID cards, a name tag, forms, family-tree lines, '
                'signs, clocks, price tags, receipts, play money, speech bubbles, letters, and labels were added.'),
        exams=[('Midterm',8),('Final',15)]),   # level1/exams/: see level1/exams/build/build_all.sh
 3:dict(audio=lambda n:f'L3_L{n}_listening.mp3', audio_re=r'^L3_L\d+_listening\.mp3$',
        routine_end='> **Timing is loose',
        credit=('Vocabulary pictures use Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), licensed under '
                'CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The graphics were resized and combined, and speech bubbles, signs, and labels were added.')),
 # Level 4: the lesson PDF/DOCX are committed next to the Markdown (level4/curriculum/Level4_Lesson<N>.pdf/.docx) and copied into
 # public/level4/downloads/ here (docs=True). Listening MP3s in level4/audio/ are copied into public/level4/audio/.
 4:dict(audio=lambda n:f'L4_L{n}_listening.mp3', audio_re=r'^L4_L\d+_listening\.mp3$',
        routine_end='> **Timing is loose', docs=True,
        credit=('Vocabulary pictures use Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), licensed under '
                'CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The graphics were resized and combined, and signs and labels were added.')),
 5:dict(audio=lambda n:f'L5_L{n}_listening.mp3', audio_re=r'^L5_L\d+_listening\.mp3$',
        routine_end='> **Timing is loose', docs=True,
        credit=('Vocabulary pictures use Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), licensed under '
                'CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The graphics were resized and combined, and signs and labels were added.')),
}
def export_level(V):
    cfg=LEVELS[V]; LV=os.path.join(HERE,f'level{V}'); PV=os.path.join(pub,f'level{V}')
    gv={}; exec(open(os.path.join(HERE,'scripts','md_parser.py'),encoding='utf-8').read(),gv)
    gv['IMG_PREFIX']=f'level{V}/images/'; gv['L1_STYLE']=True
    # 1. refresh the website copies of the media
    media=[('images',r'.+\.png$|^CREDITS\.md$','images'),('audio',cfg['audio_re'],'audio'),('slides',rf'^Level{V}_Lesson\d+_Slides\.pptx$','downloads/slides')]
    if cfg.get('docs'): media.append(('curriculum',rf'^Level{V}_Lesson\d+\.(pdf|docx)$','downloads'))
    for sub_,pat,dst in media:
        os.makedirs(os.path.join(PV,dst),exist_ok=True)
        if not os.path.isdir(os.path.join(LV,sub_)): continue
        for f in sorted(os.listdir(os.path.join(LV,sub_))):
            if re.match(pat,f): shutil.copy2(os.path.join(LV,sub_,f),os.path.join(PV,dst,f))
    size=lambda rel: os.path.getsize(os.path.join(pub,rel)) if os.path.exists(os.path.join(pub,rel)) else 0
    # 2. scope and sequence: lesson list + home-page tables
    gv['L']=open(os.path.join(LV,'curriculum',f'Level{V}_Scope_and_Sequence.md'),encoding='utf-8').read().split('\n')
    S,findv,mdv,inlinev=gv['L'],gv['find'],gv['md'],gv['inline']
    def sectv(a,b): i=findv(a); return S[i+1:findv(b,i+1)]
    out={'semester':mdv(sectv('## 5. The Semester at a Glance','**Grammar in teaching order')),
         'routine':mdv([l for l in sectv('### 4.1 Weekly routine',cfg['routine_end']) if not l.startswith('Teachers and learners')])}
    rows={}; out['milestones']=[]
    for l in sectv('## 5. The Semester at a Glance','**Grammar in teaching order'):   # Week 8 midterm, Week 15 final, Week 16 graduation
        m=re.match(r'\|\s*\d+\s*\|\s*\*\*Week (\d+): (.+?)\*\*\s*\|(.+?)\|(.+?)\|\s*$',l)
        if m: out['milestones'].append(dict(week=int(m.group(1)),title=m.group(2).strip(),note=' · '.join(x.strip() for x in (m.group(3),m.group(4)) if x.strip() not in ('—',''))))
    for l in sectv('## 5. The Semester at a Glance','**Grammar in teaching order'):
        m=re.match(r'\|\s*\d+\s*\|\s*\*\*Lesson (\d+) \(Week (\d+)\):\*\*\s*(.+?)\s*\|(.+?)\|(.+?)\|\s*$',l)
        if m: rows[int(m.group(1))]=dict(week=int(m.group(2)),title=m.group(3).strip(),focus=inlinev(m.group(4).strip()),function=m.group(5).strip())
    lessons=[]
    for n in sorted(rows):
        r=rows[n]; les=dict(n=n,week=r['week'],title=r['title'],focusHtml=r['focus'],function=r['function'],ready=False)
        src=os.path.join(LV,'curriculum',f'Level{V}_Lesson{n}.md')
        if os.path.exists(src): les.update(lesson_page(V,n,src,gv,size)); les['ready']=True
        else:   # no lesson book yet: the teacher slides can still be published on their own (slides only, no PDF/DOCX/MP3)
            pptx=f'level{V}/downloads/slides/Level{V}_Lesson{n}_Slides.pptx'
            if size(pptx): les.update(slides=pptx,downloads=[dict(kind='pptx',href=pptx,label='Teacher slides (PowerPoint)',size=size(pptx))])
        lessons.append(les)
    out['lessons']=lessons
    if cfg.get('exams'): out['exams']=[exam_entry(V,K,W,gv,size) for K,W in cfg['exams']]
    out['credit']=cfg['credit']
    out['creditHtml']=inlinev(out['credit'])
    missing=[f for f in sorted(gv['used_imgs']) if not os.path.exists(os.path.join(PV,'images',f))]
    if missing: raise SystemExit(f'Missing images in level{V}/images/: {missing}')
    json.dump(out,open(HERE+f'/src/content_level{V}.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
    print(f'Level {V}:',len(lessons),'lessons in the plan; built:',[l['n'] for l in lessons if l['ready']],
          '; audio',[l['n'] for l in lessons if l.get('audio')],'; downloads',{l['n']:[d['kind'] for d in l['downloads']] for l in lessons if l['ready']},
          '; slides only',[l['n'] for l in lessons if not l['ready'] and l.get('slides')])

def exam_entry(V,K,W,gv,size):
    """One exam card (Level 1 Week 8 Midterm / Week 15 Final). Sources: level<V>/exams/ (Markdown, audio/);
    the PDF/DOCX come from level<V>/exams/build/build_all.sh --publish (into public/level<V>/downloads/exams/).
    The MP3 is copied here from level<V>/exams/audio/ into public/level<V>/audio/."""
    X=os.path.join(HERE,f'level{V}','exams'); PV=os.path.join(pub,f'level{V}')
    mp3=f'L{V}_{K}_listening.mp3'
    if os.path.exists(os.path.join(X,'audio',mp3)): shutil.copy2(os.path.join(X,'audio',mp3),os.path.join(PV,'audio',mp3))
    P=open(os.path.join(X,f'Level{V}_{K}_Exam_Teacher_Packet.md'),encoding='utf-8').read().split('\n')
    title=re.match(r'# Level \d+ · Week \d+: (.+?): Teacher Packet',P[[i for i,l in enumerate(P) if l.startswith('# ')][0]]).group(1)
    covers=re.match(r'\*\*.+? · (.+?)\*\*',[l for l in P if l.startswith('**') and ' · ' in l][0]).group(1)
    i=P.index('### What the test has'); parts=[]
    for l in P[i+1:]:
        if l.startswith('|'):
            c=[x.strip() for x in l.strip().strip('|').split('|')]
            if c[0] not in ('Part','---'): parts.append(dict(part=gv['inline'](c[0]),what=gv['inline'](c[1]),points=gv['inline'](c[2]),time=gv['inline'](c[3])))
        elif parts: break
    note=[l for l in P[i+1:] if l.startswith('*Covers')]
    cr=os.path.join(X,'audio',f'L{V}_{K}_check_results.json')
    dur=json.load(open(cr))['duration_s'] if os.path.exists(cr) else 0
    files=[]
    for kind,rel,label in [('pdf',f'level{V}/downloads/exams/Level{V}_{K}_Exam_Teacher_Packet.pdf','Teacher packet (PDF): directions, script, answer key, speaking papers'),
                           ('docx',f'level{V}/downloads/exams/Level{V}_{K}_Exam_Teacher_Packet.docx','Teacher packet (DOCX), for editing'),
                           ('pdf',f'level{V}/downloads/exams/Level{V}_{K}_Student_Test.pdf','Student test (PDF), 1 per learner, no answers'),
                           ('mp3',f'level{V}/audio/{mp3}','Listening audio (MP3)')]:
        if size(rel): files.append(dict(kind=kind,href=rel,label=label,size=size(rel)))
    return dict(key=K.lower(),week=W,title=title,covers=covers,parts=parts,noteHtml=gv['inline'](note[0].strip('*')) if note else '',
                audio=f'level{V}/audio/{mp3}' if size(f'level{V}/audio/{mp3}') else '',audioSeconds=round(dur),downloads=files)

def lesson_page(V,n,src,gv,size):
    """One Level 1 / Level 3 lesson page from Level<V>_Lesson<N>.md. Expected layout (see level1/curriculum/Level1_Lesson1.md):
    <!-- part: Teacher Plan ... --> teacher plan ... <!-- part: Student Workbook ... --> '## ...' student pages ... '## Picture Credits'."""
    gv['L']=open(src,encoding='utf-8').read().split('\n')
    M,findv,mdv,inlinev=gv['L'],gv['find'],gv['md'],gv['inline']
    ti=findv('<!-- part: Teacher Plan'); si=findv('<!-- part: Student Workbook',ti); ci=findv('## Picture Credits',si)
    title_re=re.compile(rf'## Lesson {n} \(Week \d+\): ')
    titled=[l for l in M if title_re.match(l)]
    head=next((l for l in M[si:] if title_re.match(l)), titled[0])
    week,title=re.match(rf'## Lesson {n} \(Week (\d+)\): (.+)',head).groups()
    topic=next((l[2:].strip() for l in M[:ti] if l.startswith('> **Topic:**')),'')
    topic=re.sub(r'^\*\*Topic:\*\*\s*','',topic)
    # picture cell: ![alt](images/x.png)<br>(★ )**word**   (Lessons 8+ also write the word without bold)
    word_re=re.compile(r'!\[([^\]]*)\]\(images/([^)]+)\)<br>(★ )?(?:\*\*(.+?)\*\*|([^|*<]+?)(?=\s*(?:\||$)))')
    starts=[i for i in range(si+1,ci) if M[i].startswith('## ')]+[ci]
    sections=[]; words=[]
    heads=[M[a][3:].strip() for a in starts[:-1]]
    talk=[h for h in heads if ' · Talk Time' in h]   # several Talk Time pages (Level 1 Lesson 4): keep their full names
    for a,b in zip(starts,starts[1:]):
        h=M[a][3:].strip(); body=M[a+1:b]; kind='page'
        pics=any(word_re.search(l) for l in body)
        if h.startswith(f'Lesson {n} (Week') and ' · ' in h:
            name=h.split(' · ',1)[1]
            if name in ('New Words', 'Words') and pics: kind='words'
            if name=='Words': name='New Words'
        elif h.startswith(f'Lesson {n} (Week') and (pics or not any(x.startswith(f'Lesson {n} (Week') and x.endswith(' · New Words') for x in heads)):
            name='New Words'; kind='words'
        elif h.startswith(f'Lesson {n} (Week'):   # the lesson title page before a separate New Words page: name it after its first task ('Hello + Review')
            first=next((l[4:] for l in body if l.startswith('### ')),'Warm-up'); name=re.split(r'[:.]',first)[0].strip()
        elif h.startswith('How to Use This Workbook'): name='The Icons'
        else: name=h
        sec={}
        if kind=='words':   # the picture table becomes the word cards on the site: text before it, cards, text after it
            rows_=[k for k,l in enumerate(body) if word_re.search(l)]
            for l in body:
                for m in word_re.finditer(l):
                    gv['used_imgs'].add(m.group(2)); words.append(dict(img=f'level{V}/images/'+m.group(2),word=(m.group(4) or m.group(5)).strip(),star=bool(m.group(3))))
            k0=rows_[0]
            while k0>0 and body[k0-1].strip().startswith('|'): k0-=1      # the empty header row + |---| line of the picture table
            before=[l for l in body[:k0] if l.strip()!='### New Words']
            sec['htmlAfter']=mdv(body[rows_[-1]+1:],1); body=before
        name=name.split(':')[0] if name.startswith('Talk Time') and len(talk)<2 else name
        if name=='Listening': kind='listening'
        sid=re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-')
        sections.append(dict(id=sid,title=name,kind=kind,html=mdv(body,1),**sec))
    teacher=mdv(M[ti+1:si],1)
    mp3=f'level{V}/audio/'+LEVELS[V]['audio'](n)
    pptx=f'level{V}/downloads/slides/Level{V}_Lesson{n}_Slides.pptx'
    dl=[]
    for kind,rel,label in [('pdf',f'level{V}/downloads/Level{V}_Lesson{n}.pdf','PDF, for printing'),
                           ('docx',f'level{V}/downloads/Level{V}_Lesson{n}.docx','Word document (DOCX), for editing'),
                           ('pptx',pptx,'Teacher slides (PowerPoint)'),
                           ('mp3',mp3,'Listening audio (MP3)')]:
        if size(rel): dl.append(dict(kind=kind,href=rel,label=label,size=size(rel)))
    return dict(week=int(week),title=title,topic=inlinev(topic) if topic else '',words=words,
                audio=mp3 if size(mp3) else '',audioSize=size(mp3),sections=sections,teacher=teacher,downloads=dl,
                slides=pptx if size(pptx) else '')

for V in LEVELS:
    if os.path.isdir(os.path.join(HERE,f'level{V}')): export_level(V)
