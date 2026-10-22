"""Check PowerPoint decks for the in-browser presenter: every click animation must target a shape that exists on its slide.
Usage: python3 scripts/check_slides.py level1/slides/*.pptx level3/slides/*.pptx public/downloads/slides/*.pptx
Prints one line per deck (OK or the broken slides) and exits 1 if any deck has a broken animation."""
import sys, zipfile, re
fail = 0
for f in sys.argv[1:]:
    z = zipfile.ZipFile(f); bad = 0
    for p in sorted((n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)), key=lambda n: int(re.findall(r'\d+', n)[0])):
        x = z.read(p).decode('utf-8')
        ids = set(re.findall(r'<p:cNvPr[^>]* id="(\d+)"', x)); tg = set(re.findall(r'<p:spTgt spid="(\d+)"', x))
        if tg - ids: bad += 1; print(f, p, 'click animation targets missing shape ids', sorted(tg - ids, key=int))
    print(f, 'OK' if not bad else f'{bad} slide(s) with broken animations'); fail |= bool(bad)
sys.exit(1 if fail else 0)
