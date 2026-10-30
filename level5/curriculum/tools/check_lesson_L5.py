"""Lesson checks for a Level 5 lesson (run after the build).  Usage: python3 check_lesson_L5.py CURRICULUM_DIR N [SCRIPT_DIR] [CREDITS]
Defaults (from the repository root): CURRICULUM_DIR=level5/curriculum, SCRIPT_DIR=level5/audio/tools/scripts,
CREDITS=level5/images/CREDITS.md + level5/images/CREDITS_L5_LN.md.
Adapted from Level 4's check_lesson_L4.py, with the Level 5 rules (Level5_Scope_and_Sequence.md, sections 2-4):
- characters: no decorative emoji (the 😀 🙂 😐 faces only); banned words; '© 2026 the authors' and a published status line
- English-only student pages: no Spanish lines and no contrast-tip box (mix-ups go in the Common mistakes table)
- no instruction icons (no picture outside a table), every linked picture exists and has a CREDITS.md line, 12 New Words pictures
- reading text 250-400 words (a warning; under 150 or over 500 is a problem); a writing task (C. Write ...); exit ticket asks for about four sentences
- clock times (a step box or a clock-table row): Listening 6:12-6:32, Talk Time 7:00-7:18, Read & Write 7:18-7:25, Exit Ticket 7:25-7:30;
  the teacher plan gives the 15, 7-8 and 5-or-fewer versions
- grammar boxes: at most 6 rows each (Level 5 boxes may be QUESTION | ANSWER tables, so no two-sided gap rule)
- listening: 2-4 characters plus the Narrator, script = audio script file (script_L5_LN.py), full forms only
  (no gonna / wanna or other reductions in the spoken lines), female characters on female clips, and the lesson names its MP3
- length: the gate range 1:10-3:00 is a problem; outside the 2:05-2:40 target is only a warning (soft target, issue #43)
- the PDF page count (20-30)
Prints one JSON line; exit code 1 if there are problems (warnings do not fail)."""
import sys, re, os, json, subprocess, importlib.util
D = sys.argv[1] if len(sys.argv) > 1 else 'level5/curriculum'; N = sys.argv[2] if len(sys.argv) > 2 else '1'
SD = sys.argv[3] if len(sys.argv) > 3 else 'level5/audio/tools/scripts'; CR = sys.argv[4] if len(sys.argv) > 4 else None
IMGROOT = D if os.path.isdir(f'{D}/images') else os.path.join(D, '..')
CRS = [CR] if CR else [os.path.join(IMGROOT, 'images', f) for f in ('CREDITS.md', f'CREDITS_L5_L{N}.md')]
md = open(f'{D}/Level5_Lesson{N}.md').read(); lines = md.split('\n'); bad = []; warn = []
ALLOWED = set('¡©«·»¿áéíñóúÁÉÍÓÚü–—‖•…→★☐✓✗↗↘') | {'😀', '🙂', '😐'}
chars = sorted({c for c in md if ord(c) > 127 and c not in ALLOWED})
if chars: bad.append(f'characters not allowed: {chars}')
for w in ['Inter' + 'cambio', 'secular', 'church', 'God', 'pray', 'prayer', 'Christmas', 'Easter', 'Ramadan', 'Hanukkah', 'temple', 'mosque', 'bible', 'blessed', 'religion', 'religious', 'copyright registration', 'registered with']:
    if re.search(r'\b' + w + r'\b', md, re.I): bad.append(f'word found: {w}')
if '© 2026 the authors, licensed under CC BY-NC-SA 4.0' not in md: bad.append('missing © 2026 the authors, CC BY-NC-SA 4.0')
if re.search(r'\{\{|\}\}|\{[A-Z_]+\}|(?<![!\]])\[[a-z][^\]]*\](?!\()', md): bad.append('leftover spec markup ({{…}}, {EST} or [blank])')
st = re.search(r'^\*\*Status:\*\* (.*)$', md, re.M)
if not st or not st.group(1).startswith('Published'): bad.append('missing published status line')
if re.search(r'draft for review|not published|unpublished|work in progress', md, re.I): bad.append('draft or unpublished wording')
mode = None; spanish = []
for i, s in enumerate(lines):
    m = re.match(r'<!--\s*mode:\s*(\w+)', s)
    if m: mode = m.group(1)
    if s.startswith('> **Contrast tip'): bad.append(f'contrast tip box (Level 5 has none), line {i+1}')
    s_ = re.sub(r'\b[A-ZÁÉÍÓÚ][a-záéíóúñ]*[áéíóúñ][a-záéíóúñ]*\b', 'Name', s)   # invented names like Lucía are fine
    if re.search(r'[¿¡ñáéíóú]|Español|Nota para|\b(escucha|escribe|encierra|trabaja)\b', s_, re.I) and not re.search(r'\b(café|résumé|résumés)\b', s, re.I):
        spanish.append(i+1)
if spanish: bad.append(f'Spanish-looking lines: {spanish}')
if re.search(r'^#+ .*\b(icon)\b', md, re.M | re.I): bad.append('instruction icon mention')
imgs = re.findall(r'!\[[^\]]*\]\((images/[^)]+)\)', md)
miss = [p for p in imgs if not os.path.exists(os.path.join(IMGROOT, p))]
if miss: bad.append(f'missing pictures: {miss}')
nw = md[md.index('### New Words'):md.index('### Partner game')] if '### Partner game' in md else ''
nv = len(re.findall(r'!\[', nw))
if nv != 12: bad.append(f'New Words page has {nv} pictures (want 12)')
for i, s in enumerate(lines):
    if '![' in s and not s.startswith('|'): bad.append(f'picture outside a table (instruction icon?), line {i+1}')
cred = ''.join(open(c).read() for c in CRS if os.path.exists(c))
nocred = [p for p in set(imgs) if os.path.basename(p) not in cred]
if nocred: bad.append(f'pictures without a CREDITS.md line: {nocred}')
# reading + writing + exit ticket
rw = md[re.search(r'^## [^\n]*· Read & Write', md, re.M).start():]; rw = rw[:rw.index('\n## ', 5)] if '\n## ' in rw[5:] else rw
ra = re.search(r'^### A\. Read[^\n]*\n(.*?)^### B\.', rw, re.S | re.M)
rtext = re.sub(r'^:::.*$|<!--.*?-->|^\|[-| ]+\|$', ' ', ra.group(1), flags=re.M) if ra else ''
rwords = len(re.sub(r'[*#|_]', ' ', rtext).split())
if not 150 <= rwords <= 500: bad.append(f'reading has {rwords} words (want 250-400)')
elif not 250 <= rwords <= 400: warn.append(f'reading has {rwords} words (target 250-400; forms and tables count less)')
if not re.search(r'^### C\. .*\bWrite\b', rw, re.M | re.I): bad.append('no writing task (### C. Write ...)')
et = md[md.rindex('· Exit Ticket'):]
if not re.search(r'four sentences', et, re.I): bad.append('exit ticket does not ask for about four sentences')
for t, name in [('6:12–6:32', 'Listening'), ('7:00–7:18', 'Talk Time'), ('7:18–7:25', 'Read & Write'), ('7:25–7:30', 'Exit Ticket')]:
    # a step box (:::step Step 5 · 7:00–7:18 · Talk Time) or a clock-table row (| 7:00–7:18 | Talk Time |)
    if not re.search(rf'^(:::step [^\n]*{t}[^\n]*|\| {t} \|[^\n]*){name}', md, re.M | re.I): bad.append(f'no {name} step or clock row at {t}')
tp = md[md.index('<!-- part: Teacher Plan'):md.index('<!-- part: Student Workbook')]
for v in [r'\b15\b', '7–8', '5 or fewer']:
    if not re.search(v, tp): bad.append(f'teacher plan without the {v} learners version')
# grammar boxes
for m in re.finditer(r'<!-- subst -->\n((?:\|.*\n)+)', md):
    rows = m.group(1).strip().split('\n')[2:]
    if len(rows) > 6: bad.append(f'grammar box with {len(rows)} rows (max 6)')
if f'L5_L{N}_listening.mp3' not in md: bad.append('lesson does not name its listening file')
if re.search(r'not recorded yet|coming soon|no recording yet', md, re.I): bad.append('lesson still says the audio is not recorded')
# listening script = audio script
sec = md[md.index('### Listening script'):md.index('### Answer key')]
got = [(m.group(1), m.group(2).strip()) for m in re.finditer(r'^> \*\*([^*]+):\*\* (.+)$', sec, re.M)]
got = [g for g in got if g[0] != 'Audio']
spk = sorted(set(s for s, _ in got) - {'Narrator'})
if not 2 <= len(spk) <= 4: bad.append(f'want 2-4 characters plus the Narrator: {spk}')
text = ' '.join(t for _, t in got); words = len(text.split()); est = 0.37*words + 1.1*len(got)
m = re.search(r'about (\d+):(\d\d)', sec); real = int(m.group(1))*60 + int(m.group(2)) if m else None
L = real or est
if not 70 <= L <= 180: bad.append(f'length {L:.0f} s outside the gate (70-180 s)')
elif not 125 <= L <= 160: warn.append(f'length {L:.0f} s outside the 2:05-2:40 target (soft, issue #43)')
RED = r"\b(gotta|hafta|hasta|kinda|sorta|gimme|lemme|dunno|whaddaya|wanna|gonna|ya|y'all|'em|outta|lotta|coulda|woulda|shoulda|tryna|cuz|'cause|ain't|d'you|whatcha|gotcha|betcha|doncha|dontcha|wouldja|didja|havya)\b"
red = sorted({w.lower() for w in re.findall(RED, text, re.I)})
if red: bad.append(f'reductions in the spoken script (say the full forms): {red}')
sp = f'{SD}/script_L5_L{N}.py'
if os.path.exists(sp):
    spec = importlib.util.spec_from_file_location('S', sp); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
    want = [('Narrator', S.INTRO)] + [(l[0], l[1]) for l in S.LINES] + [('Narrator', S.END)]
    if got != want: bad.append('listening script in the lesson differs from script_L5_LN.py')
    FEM = {'N', 'Rosa', 'Ana_af_jessica', 'Ana_af_bella', 'Kim', 'Receptionist'}; MALE = {'Sam', 'Marco', 'Server', 'Carlos'}
    for s, v in S.VOICES.items():
        if v not in FEM | MALE: bad.append(f'{s}: clip {v} is not a Level 5 Kokoro reference clip (REFS_L5.md)')
        elif (s in S.FEMALE) != (v in FEM): bad.append(f'{s}: voice gender does not match ({v})')
    voices = {s: S.VOICES.get(s) for s in spk}
else: bad.append('no audio script yet'); voices = {}
pdf = f'{D}/Level5_Lesson{N}.pdf'
pages = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1)) if os.path.exists(pdf) else None
if pages is not None and not 20 <= pages <= 30: bad.append(f'{pages} PDF pages (want 20-30)')
print(json.dumps(dict(lesson=N, pdf_pages=pages, reading_words=rwords, listening_words=words, listening_length=f'{int(L//60)}:{int(round(L%60)):02d}',
                      speakers=voices, problems=bad, warnings=warn), ensure_ascii=False))
sys.exit(1 if bad else 0)
