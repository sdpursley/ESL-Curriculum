"""Rule checks for finished decks (AGENTS.md section 6). Run it on every deck you build or edit, before export.
Usage: python3 scripts/slides/check_deck.py --level V --lesson N <deck.pptx>
       python3 scripts/slides/check_deck.py --level V level<V>/slides/*.pptx     (lesson number read from the file name)
Checks (exit 1 if any fails):
  - deck opens; 13.333 x 7.5 in; 20-30 slides; every click animation targets a shape on its slide
  - every shape lies inside the slide; every picture has alt text
  - picture bytes match a file in level<V>/images (the site exporter needs this)
  - emoji: only the faces 😀 🙂 😐 and the marks ✓ ✗ ★ ☐ ↗ (no decorative or instruction icons)
  - Level 2 and up: no Spanish and no 'My language' lines on slides (Level 1 has Spanish on the student pages only)
  - no forbidden words on slides or notes ('secular', 'Draft', 'TODO', 'Lorem', religious words, ...; add the names of
    other programs or publishers with --forbid 'Name1,Name2')
  - title slide says 'Lesson N · Level V'; no other lesson's number in 'Lesson X · Level' lines
  - notes: no pointers to files the site does not have (AUDIO_STATUS, drafts/)
  - warning (not a failure): notes with 'Source: LevelV_LessonN.md (...)' lines. Older decks (all Level 1 decks, Level 3
    Lesson 1) have them; every new deck must use 'Lesson plan: (...).' and show no warning.
  - last slide is the credits slide with '© 2026 the authors' and 'CC BY-NC-SA 4.0'"""
import sys, re, os, glob, hashlib, argparse
from pptx import Presentation
from pptx.util import Emu
ap = argparse.ArgumentParser(); ap.add_argument('--level', type=int, required=True); ap.add_argument('--lesson', type=int)
ap.add_argument('--forbid', default='', help='extra forbidden words, comma-separated (e.g. names of other programs)')
ap.add_argument('decks', nargs='+'); a = ap.parse_args(); V = a.level
OK_EMOJI = set('😀🙂😐✓✗★☐↗')
EMOJI = re.compile('[\U0001F000-\U0001FAFF\u2600-\u27BF\u2B00-\u2BFF\uFE0F]')
FORBIDDEN = ['secular', 'Secular', 'Draft for review', 'DRAFT', 'Lorem', 'TODO', 'XXX', 'AUDIO_STATUS', 'drafts/',
             'church', 'Church', 'prayer', 'Christmas', 'Easter', 'Bible', 'God ', 'registered trademark', '®']
FORBIDDEN += [w.strip() for w in a.forbid.split(',') if w.strip()]
SPANISH = re.compile(r'\b(Español|Spanish|Mi idioma|My language)\b|[¿¡ñ]')
imgs = {}
for f in glob.glob(f'level{V}/images/*.png') + glob.glob(f'level{V}/images/*.jpg'):
    imgs[hashlib.sha1(open(f, 'rb').read()).hexdigest()] = os.path.basename(f)
fail = 0
for path in a.decks:
    n = a.lesson or int(re.search(r'Lesson(\d+)', os.path.basename(path)).group(1))
    prs = Presentation(path); bad = []; warn = set()
    W, H = prs.slide_width, prs.slide_height
    if (round(Emu(W).inches, 2), round(Emu(H).inches, 2)) != (13.33, 7.5): bad.append(f'slide size {Emu(W).inches:.2f}x{Emu(H).inches:.2f} in')
    if not 20 <= len(prs.slides) <= 30: bad.append(f'{len(prs.slides)} slides (expected about 24-27)')
    for i, s in enumerate(prs.slides, 1):
        x = s._element.xml
        ids = set(re.findall(r'<p:cNvPr[^>]* id="(\d+)"', x)); tg = set(re.findall(r'<p:spTgt spid="(\d+)"', x))
        if tg - ids: bad.append(f'slide {i}: click animation targets missing shape ids {sorted(tg - ids)}')
        texts = []
        for sh in s.shapes:
            if sh.left is not None:
                over = max(-sh.left, -sh.top, sh.left + sh.width - W, sh.top + sh.height - H) / 914400
                has_text = sh.has_text_frame and sh.text_frame.text.strip()
                # the design lets plain background panels bleed up to ~0.4 in past the edge; text never leaves the slide
                if over > 0.5 or (has_text and over > 0.01): bad.append(f'slide {i}: shape {sh.name!r} goes {over:.2f} in outside the slide')
            if sh.shape_type == 13:
                if not (sh._element.xpath('.//p:cNvPr')[0].get('descr') or '').strip(): bad.append(f'slide {i}: picture {sh.name!r} has no alt text')
                h = hashlib.sha1(sh.image.blob).hexdigest()
                if imgs and h not in imgs: bad.append(f'slide {i}: picture {sh.name!r} is not byte-identical to any file in level{V}/images')
            if sh.has_text_frame: texts.append(sh.text_frame.text)
        notes = s.notes_slide.notes_text_frame.text if s.has_notes_slide else ''
        st = '\n'.join(texts)
        for m in set(EMOJI.findall(st + notes)) - OK_EMOJI: bad.append(f'slide {i}: emoji {m!r} not allowed')
        if V >= 2 and SPANISH.search(st): bad.append(f'slide {i}: Spanish / My language text on the slide ({SPANISH.search(st).group(0)!r})')
        for w in FORBIDDEN:
            if w in st or w in notes: bad.append(f'slide {i}: forbidden text {w!r}')
        if re.search(r'\bDraft\b', st): bad.append(f'slide {i}: the word "Draft" on the slide')
        for m in re.findall(r'Lesson (\d+)\s*·\s*Level (\d+)', st):
            if (int(m[0]), int(m[1])) != (n, V): bad.append(f'slide {i}: says Lesson {m[0]} · Level {m[1]}')
        if re.search(r'^Source:|\b\w+_Lesson\d+\.md\b', notes): warn.add('notes use "Source: LevelV_LessonN.md (...)" lines; new decks use "Lesson plan: (...)."')
        if i == 1 and V >= 3 and not re.search(rf'Lesson {n}\s*·\s*Level {V}', st): bad.append(f'slide 1: no "Lesson {n} · Level {V}" line')
        if i == len(prs.slides):
            if '© 2026 the authors' not in st or 'CC BY-NC-SA 4.0' not in st: bad.append(f'slide {i} (credits): needs "© 2026 the authors" and "CC BY-NC-SA 4.0"')
    print(path, 'OK' if not bad else f'{len(bad)} problem(s)', f'({len(warn)} warning(s))' if warn else '')
    for b in bad: print('  ' + b)
    for w in sorted(warn): print('  warning: ' + w)
    fail |= bool(bad)
sys.exit(1 if fail else 0)
