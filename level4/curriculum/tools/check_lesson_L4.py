"""Lesson checks for a Level 4 lesson (run after the build).  Usage: python check_lesson_L4.py LESSON_DIR_OR_CURRICULUM_DIR N [SCRIPT_DIR] [CREDITS]
Same checks as Level 3 (check_lesson_L3.py), with the Level 4 support rules:
- characters: only the Level 3 set (no decorative emoji; the 😀 🙂 😐 faces only); banned words; '© 2026 the authors' and the published status line
- Spanish only inside an optional '> **Contrast tip (optional):**' box on student pages, at most 1 per lesson; no Spanish on instruction lines
- no instruction icons (no picture outside a table), every linked picture exists and has a CREDITS.md line, 12 New Words pictures
- My Words page has the 'My language' column; Task Words page (optional) at the back
- reading text 150-250 words; writing task 5-8 sentences; exit ticket asks for 3 sentences with a reason
- clock times: Talk Time 7:00-7:15, Read & Write 7:15-7:25, Exit Ticket 7:25-7:30; Talk Time step lists 15, 7-8 and 5-or-fewer versions
- grammar Q&A boxes: two-sided, at most 6 rows each
- listening: 2-3 characters plus the Narrator, script = audio script file, estimated 1:30-2:15, no reductions in the spoken script (gonna / wanna stay in the text tip only),
  female characters on female clips, and the lesson names its MP3
- the PDF page count (27-30)"""
import sys, re, os, json, subprocess, importlib.util
D = sys.argv[1]; N = sys.argv[2]
SD = sys.argv[3] if len(sys.argv) > 3 else f'{D}/build'; CR = sys.argv[4] if len(sys.argv) > 4 else f'{D}/images/CREDITS.md'
md = open(f'{D}/Level4_Lesson{N}.md').read(); lines = md.split('\n'); bad = []
ALLOWED = set('¡©«·»¿áéíñóúÁÉÍÓÚü–—‖•…→★☐✓✗↗↘') | {'😀', '🙂', '😐'}
chars = sorted({c for c in md if ord(c) > 127 and c not in ALLOWED})
if chars: bad.append(f'characters not allowed: {chars}')
for w in ['Inter' + 'cambio', 'secular', 'church', 'God', 'pray', 'prayer', 'Christmas', 'Easter', 'Ramadan', 'Hanukkah', 'temple', 'mosque', 'bible', 'blessed', 'religion', 'religious', 'copyright registration', 'registered copyright', 'Registered']:
    if re.search(r'\b' + w + r'\b', md, re.I): bad.append(f'word found: {w}')
if '© 2026 the authors, licensed under CC BY-NC-SA 4.0' not in md: bad.append('missing © 2026 the authors, CC BY-NC-SA 4.0')
if re.search(r'\{\{|\}\}|\{[A-Z_]+\}|(?<![!\]])\[[a-z][^\]]*\](?!\()', md): bad.append('leftover spec markup ({{…}}, {EST} or [blank])')
if '**Status:** Complete lesson (all 13 Level 4 lessons are published).' not in md: bad.append('missing published status')
mode = None; spanish = []; tips = 0
for i, s in enumerate(lines):
    m = re.match(r'<!--\s*mode:\s*(\w+)', s)
    if m: mode = m.group(1)
    if s.startswith('> **Contrast tip (optional):**'):
        tips += 1
        if mode != 'student': bad.append(f'contrast tip outside student pages, line {i+1}')
        continue
    s_ = re.sub(r'\b[A-ZÁÉÍÓÚ][a-záéíóúñ]*[áéíóúñ][a-záéíóúñ]*\b', 'Name', s)   # invented names like Lucía are fine
    if re.search(r'[¿¡ñáéíóú]|Español|Nota para|\b(escucha|escribe|encierra|trabaja)\b', s_, re.I) and not re.search(r'\b(café|résumé)\b', s):
        spanish.append(i+1)
if spanish: bad.append(f'Spanish-looking lines outside the contrast tip: {spanish}')
if tips > 1: bad.append(f'more than one contrast tip: {tips}')
if re.search(r'^#+ .*\b(icon)\b', md, re.M | re.I): bad.append('instruction icon mention')
imgs = re.findall(r'!\[[^\]]*\]\((images/[^)]+)\)', md)
miss = [p for p in imgs if not os.path.exists(f'{D}/{p}')]
if miss: bad.append(f'missing pictures: {miss}')
nw = md[md.index('### New Words'):md.index('### Partner game')] if '### Partner game' in md else ''
nv = len(re.findall(r'!\[', nw))
if nv != 12: bad.append(f'New Words page has {nv} pictures (want 12)')
for i, s in enumerate(lines):
    if '![' in s and not s.startswith('|'): bad.append(f'picture outside a table (instruction icon?), line {i+1}')
cred = open(CR).read() if os.path.exists(CR) else ''
nocred = [p for p in set(imgs) if os.path.basename(p) not in cred]
if nocred: bad.append(f'pictures without a CREDITS.md line: {nocred}')
if '| Word | My language | My example |' not in md: bad.append('My Words page without the My language column')
if 'Task Words (optional)' not in md: bad.append('no optional Task Words page')
# reading + writing + exit ticket
rw = md[md.index('· Read & Write'):]; box = re.search(r':::box [^\n]*\n(.*?)\n:::', rw, re.S).group(1)
rwords = len(re.sub(r'[*#|]', ' ', box).split())
if not 150 <= rwords <= 250: bad.append(f'reading has {rwords} words (want 150-250)')
if not re.search(r'### C\. .*\(5–8 sentences\)', rw): bad.append('writing task is not 5-8 sentences')
if not re.search(r'### Answer in 3 sentences\. Give a reason\.', md): bad.append('exit ticket is not 3 sentences with a reason')
for t, name in [('7:00–7:15', 'Talk Time'), ('7:15–7:25', 'Read & Write'), ('7:25–7:30', 'Exit Ticket')]:
    if not re.search(rf'^:::step [^\n]*{t}[^\n]*{name}', md, re.M): bad.append(f'no {name} step at {t}')
tt = re.search(r'^:::step [^\n]*7:00–7:15.*?^:::$', md, re.S | re.M).group(0)
for v in ['**15 learners:**', '**7–8 learners:**', '**5 or fewer:**']:
    if v not in tt: bad.append(f'Talk Time step without the {v} version')
# grammar boxes
for m in re.finditer(r'<!-- subst -->\n((?:\|.*\n)+)', md):
    rows = m.group(1).strip().split('\n')[2:]
    if len(rows) > 6: bad.append(f'grammar box with {len(rows)} rows (max 6)')
    if not all('‖' in r for r in rows): bad.append('grammar box row without the two-sided gap')
if f'audio/L4_L{N}_listening.mp3' not in md: bad.append('lesson does not name its listening file')
if 'not recorded yet' in md or 'coming soon' in md or 'no recording yet' in md: bad.append('lesson still says the audio is not recorded')
# listening script = audio script
sec = md[md.index('### Listening script'):md.index('### Answer key')]
got = [(m.group(1), m.group(2).strip()) for m in re.finditer(r'^> \*\*([^*]+):\*\* (.+)$', sec, re.M)]
got = [g for g in got if g[0] != 'Audio']
spk = sorted(set(s for s, _ in got) - {'Narrator'})
if not 2 <= len(spk) <= 3: bad.append(f'want 2-3 characters plus the Narrator: {spk}')
text = ' '.join(t for _, t in got); words = len(text.split()); est = 0.37*words + 1.1*len(got)
if not 90 <= est <= 135: bad.append(f'estimated length {est:.0f} s (want 90-135)')
RED = r"\b(gotta|hafta|hasta|kinda|sorta|gimme|lemme|dunno|whaddaya|wanna|gonna|ya|y'all|'em|outta|lotta|coulda|woulda|shoulda|tryna|cuz|'cause|ain't|d'you|whatcha|gotcha|betcha|doncha|dontcha|wouldja|didja|havya)\b"
other = sorted({w.lower() for w in re.findall(RED, text, re.I)} - {'gonna', 'wanna'})
if other: bad.append(f'reductions other than gonna / wanna: {other}')
sp = f'{SD}/script_L4_L{N}.py'
red = sorted({w.lower() for w in re.findall(r'\b(gonna|wanna)\b', text, re.I)})
if os.path.exists(sp):
    spec = importlib.util.spec_from_file_location('S', sp); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
    want = [('Narrator', S.INTRO)] + [(l[0], l[1]) for l in S.LINES] + [('Narrator', S.END)]
    if got != want: bad.append('listening script in the lesson differs from script_L4_LN.py')
    FEM = {'N', 'Rosa', 'Ana_af_jessica', 'Kim', 'Receptionist'}; MALE = {'Sam', 'Marco', 'Server', 'Carlos'}
    for s, v in S.VOICES.items():
        if v not in FEM | MALE: bad.append(f'{s}: clip {v} is not a Level 4 Kokoro reference clip')
        elif (s in S.FEMALE) != (v in FEM): bad.append(f'{s}: voice gender does not match ({v})')
    voices = {s: S.VOICES[s] for s in spk}
else: bad.append('no audio script yet'); voices = {}
pdf = f'{D}/Level4_Lesson{N}.pdf'
pages = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1)) if os.path.exists(pdf) else None
if pages is not None and not 27 <= pages <= 30: bad.append(f'{pages} PDF pages (want 27-30)')
print(json.dumps(dict(lesson=N, pdf_pages=pages, reading_words=rwords, listening_words=words, listening_estimate=f'{int(est//60)}:{int(round(est%60)):02d}',
                      reductions=red, speakers=voices, contrast_tips=tips, problems=bad), ensure_ascii=False))
sys.exit(1 if bad else 0)
