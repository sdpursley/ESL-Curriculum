"""Lesson checks for a Level 3 draft lesson in level3/drafts/ (run after the build).  Usage: python check_lesson_L3.py N
(BANNED_EXTRA="word1,word2" adds words to the banned list, as in the Level 1 checkers.)
- characters: only the ones Lesson 1 uses (no decorative emoji; the 😀 🙂 😐 self-check faces only)
- words that must not appear (religious words, other program names via BANNED_EXTRA, 'secular', copyright-registration claims), '© 2026 the authors' present
- Level 3 language rule: no Spanish line under instructions; Spanish only in the one 'Nota para hispanohablantes' note (student pages)
- no instruction icons (no image outside the New Words / activity tables), every linked picture exists, 12 vocabulary pictures
- every picture has a CREDITS.md line; the listening script in the lesson = audio/script_L3_LN.py
- the PDF page count"""
import sys, re, os, json, subprocess, importlib.util
N = sys.argv[1]; B = os.path.dirname(os.path.abspath(__file__)); L = os.path.dirname(B); R = os.path.dirname(L)   # tools/ -> curriculum/ -> drafts/
md = open(f'{L}/Level3_Lesson{N}.md').read(); lines = md.split('\n'); bad = []
ALLOWED = set('¡©«·»¿áéíñóúÁÉÍÓÚü–—‖•…→★☐✓✗↗↘') | {'😀', '🙂', '😐'}
chars = sorted({c for c in md if ord(c) > 127 and c not in ALLOWED})
if chars: bad.append(f'characters not allowed: {chars}')
EXTRA = [w.strip() for w in os.environ.get('BANNED_EXTRA', '').split(',') if w.strip()]
for w in EXTRA + ['secular', 'church', 'God', 'pray', 'prayer', 'Christmas', 'Easter', 'Ramadan', 'Hanukkah', 'temple', 'mosque', 'bible', 'blessed', 'religion', 'religious', 'copyright registration', 'registered copyright', 'Registered']:
    if re.search(r'\b' + w + r'\b', md, re.I): bad.append(f'word found: {w}')
if '© 2026 the authors' not in md: bad.append('missing © 2026 the authors')
mode = None; spanish = []; notas = 0
for i, s in enumerate(lines):
    m = re.match(r'<!--\s*mode:\s*(\w+)', s)
    if m: mode = m.group(1)
    if s.startswith('> **Nota para hispanohablantes:**'):
        notas += 1
        if mode != 'student': bad.append(f'Spanish note outside student pages, line {i+1}')
        continue
    if re.search(r'[¿¡ñáéíóú]|Español|\b(escucha|escribe|encierra|trabaja)\b', s, re.I) and not re.search(r'\b(café|résumé)\b', s):
        spanish.append(i+1)
if spanish: bad.append(f'Spanish-looking lines outside the one Spanish note: {spanish}')
if notas != 1: bad.append(f'expected exactly 1 Spanish note, found {notas}')
if 'Tip for speakers of other languages' not in md: bad.append('missing tip for speakers of other languages')
imgs = re.findall(r'!\[[^\]]*\]\((images/[^)]+)\)', md)
miss = [p for p in imgs if not os.path.exists(f'{R}/{p}')]
if miss: bad.append(f'missing pictures: {miss}')
nw = md[md.index('### New Words'):md.index('### Partner game')] if '### Partner game' in md else ''
nv = len(re.findall(r'!\[', nw))
if nv != 12: bad.append(f'New Words page has {nv} pictures (want 12)')
for i, s in enumerate(lines):
    if '![' in s and not s.startswith('|'): bad.append(f'picture outside a table (instruction icon?), line {i+1}')
CF = f'{R}/images/CREDITS_L3_L{N}.md'
cred = open(CF).read() if os.path.exists(CF) else ''
nocred = [p for p in set(imgs) if os.path.basename(p) not in cred]
if nocred: bad.append(f'pictures without a CREDITS.md line: {nocred}')
# listening script = audio script
sp = f'{R}/audio/tools/scripts/script_L3_L{N}.py'
if os.path.exists(sp):
    spec = importlib.util.spec_from_file_location('S', sp); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
    sec = md[md.index('### Listening script'):md.index('### Answer key')]
    got = [(m.group(1), m.group(2).strip()) for m in re.finditer(r'^> \*\*([^*]+):\*\* (.+)$', sec, re.M)]
    got = [g for g in got if g[0] != 'Audio']
    want = [('Narrator', S.INTRO)] + [(l[0], l[1]) for l in S.LINES] + [('Narrator', S.END)]
    if got != want: bad.append('listening script in the lesson differs from audio/script_L3_LN.py')
    if len(set(s for s, _ in got)) > 3: bad.append(f'more than 3 speakers: {sorted(set(s for s, _ in got))}')
else: bad.append('no audio script yet')
pdf = f'{L}/Level3_Lesson{N}.pdf'
pages = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1)) if os.path.exists(pdf) else None
print(json.dumps(dict(lesson=N, pdf_pages=pages, problems=bad), indent=1, ensure_ascii=False))
sys.exit(1 if bad else 0)
