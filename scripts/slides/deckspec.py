"""Helpers for the per-lesson deck specs (levelV/slides/specs/LevelV_LessonN.py).
A spec starts with `from deckspec import *` and defines N, DECK_TITLE and SLIDES (see AGENTS.md section 6).
scripts/slides/build_deck.py fills CFG before it loads the spec:
  CFG['level']   level number V            CFG['lesson'] lesson number N
  CFG['md']      the lesson Markdown (LevelV_LessonN.md)
  CFG['images']  picture folders, searched in order (levelV/images first)
  CFG['audio']   True when levelV/audio/L<V>_L<N>_listening.mp3 exists (the deck then says the audio is ready)"""
import os, re, glob
CFG = {'level': 3, 'lesson': 1, 'md': '', 'images': [], 'audio': False}
TW = ('Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), '
      'CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/)')
LICENSE = '© 2026 the authors. The authors license this deck under CC BY-NC-SA 4.0.'
AUDIO_CREDIT_READY = ('Audio: synthetic voices made with Chatterbox TTS (MIT License), cloned from short synthetic reference clips made with '
                      'Kokoro-82M (Apache License 2.0). No recordings of real people were used. Each file carries an inaudible Perth '
                      'watermark marking it as AI-generated. Font: Lexend Deca (OFL 1.1).')
AUDIO_CREDIT_SOON = ('Audio (coming soon): synthetic voices made with Chatterbox TTS (MIT License), cloned from short synthetic reference clips '
                     'made with Kokoro-82M (Apache License 2.0). No recordings of real people. Each file will carry an inaudible Perth '
                     'watermark marking it as AI-generated. Font: Lexend Deca (OFL 1.1).')

# ------------------------------------------------------------------ pictures
_credits = None
def _credit_rows():
    """file -> (word, what it shows) from every CREDITS*.md table in the picture folders ('| L3_L2_tall.png | tall | ... |')."""
    global _credits
    if _credits is None:
        _credits = {}
        for d in CFG['images']:
            for f in sorted(glob.glob(os.path.join(d, 'CREDITS*.md'))):
                ncols = 0
                for l in open(f, encoding='utf-8'):
                    cells = [c.strip().replace('\\|', '|') for c in re.split(r'(?<!\\)\|', l.strip())[1:-1]]
                    if not re.match(r'\|\s*L\d+_', l):
                        if l.startswith('|') and not re.match(r'\|\s*:?-', l): ncols = len(cells)   # header row
                        continue
                    extra = len(cells) - ncols if ncols else 0
                    if extra > 0:   # an unescaped '|' inside 'What it shows' (e.g. 'THEN: ... | NOW: ...'): join it back
                        cells[2:3 + extra] = [' | '.join(cells[2:3 + extra])]
                    _credits.setdefault(cells[0], (cells[1], cells[2]))
    return _credits
def alt(n, f, label=None):
    """Alt text for a picture: 'Word: what it shows' (the drawn-parts brackets are left out). Read from CREDITS.md."""
    word, note = _credit_rows()[f]
    note = re.sub(r'\s*\((?:[^()]*drawn[^()]*)\)', '', note).strip().rstrip(',')
    w = label or word
    return f"{w[0].upper() + w[1:]}: {note}"
def pic_credit(mods, plural=False):
    return f"Picture{'s' if plural else ''}: {TW}; {mods} (images/CREDITS.md)."
def words(n, items):
    """items: (file_stem, label, star) -> word cards for the New Words slides."""
    V = CFG['level']
    return [{'file': f'L{V}_L{n}_{stem}.png', 'word': label, 'star': star, 'alt': alt(n, f'L{V}_L{n}_{stem}.png')} for stem, label, star in items]
def newwords(n):
    """The 12 word cards, in order, straight from the lesson's New Words table (![..](images/X.png)<br>★ **word**)."""
    md = open(CFG['md'], encoding='utf-8').read()
    out = []
    for f, lab in re.findall(r'!\[[^\]]*\]\(images/([^)]*)\)<br>([^|]*)', md.split('### New Words', 1)[1].split('###', 1)[0]):
        star = '★' in lab
        label = re.sub(r'\s+', ' ', lab.replace('★', '').replace('**', '')).strip()
        out.append({'file': f, 'word': label, 'star': star, 'alt': alt(n, f, label)})
    assert len(out) == 12, (n, len(out))
    return out

# ------------------------------------------------------------------ audio wording
def audio_note(n, length, recorded=None):
    """The 'Audio: ...' notes line. Ready wording only when the MP3 is in levelV/audio/ (CFG['audio'])."""
    if CFG['audio']:
        return ('Audio: synthetic voices, computer-generated (Chatterbox TTS cloned from Kokoro-82M reference clips). '
                'No recordings of real people. The names and the story are invented.')
    return (f'Audio: the listening audio for this lesson (about {length}) is coming soon. It will use computer-generated voices '
            '(Chatterbox TTS cloned from synthetic Kokoro-82M reference clips); no recordings of real people. Until it is ready, '
            'read the listening script (in the notes of the Before You Listen slide) with a volunteer. The names and the story are invented.')
def listening_script(n):
    """'Speaker: line' for every line of the lesson's '### Listening script' block (added to the Before You Listen notes
    by build_deck.py when the audio is not ready)."""
    md = open(CFG['md'], encoding='utf-8').read().split('\n')
    i = next(k for k, l in enumerate(md) if l.startswith('### Listening script'))
    out = []
    for l in md[i + 1:]:
        if l.startswith('#'): break
        m = re.match(r'^> \*\*([^*:]+):\*\*\s*(.+)$', l)
        if m and m.group(1) != 'Audio': out.append(f'{m.group(1)}: {m.group(2).strip()}')
    assert out, n
    return ['Listening script (the audio is coming soon; until then, read it aloud with a volunteer at a normal, friendly speed):'] + out

# ------------------------------------------------------------------ fixed slides
def ican(lines):
    return ['D. I can…', '😀   🙂   😐', 'Check one face.'] + lines
def credits_slide(n, names, mods, extra_notes=()):
    V = CFG['level']
    return {'kind': 'credits',
            'pictures': [(0, 'Pictures'),
                         (1, 'Vocabulary pictures use Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), '
                             f'licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). {mods}'),
                         (2, "The faces on the Progress Check are standard emoji characters shown with the computer's emoji font.")],
            'names': [(0, 'Names and story'), (1, f'{names} are invented names. The listening story is invented.')],
            'audio': [(0, 'Audio and font'), (1, AUDIO_CREDIT_READY if CFG['audio'] else AUDIO_CREDIT_SOON), (2, LICENSE)],
            'notes': ['Credits. You don\'t need to read this slide in class.',
                      'Pictures: Twemoji graphics by Twitter, Inc. and other contributors, CC BY 4.0; the file-by-file list is in images/CREDITS.md.',
                      *extra_notes,
                      'Course materials: © 2026 the authors, licensed under CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/).',
                      f'Source: Level{V}_Lesson{n}.md (Picture Credits); images/CREDITS.md.']}
