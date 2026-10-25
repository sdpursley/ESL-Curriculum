"""Write level3/drafts/images/CREDITS_L3_LN.md for a Level 3 draft lesson from images_L3_LN.json (same layout as Lesson 1's CREDITS.md).
Usage: python make_credits_L3.py N"""
import sys, json, os
N = sys.argv[1]; I = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # level3/drafts/images
meta = json.load(open(f'{I}/images_L3_L{N}.json'))
U = 'https://raw.githubusercontent.com/jdecked/twemoji/main/assets/svg/'
rows = []
for m in meta:
    src = ', '.join(f'[{c}]({U}{c}.svg)' for c in m['twemoji']) or 'none (our own drawing)'
    rows.append(f"| {m['file']} | {m['word']} | {m['note']} | {src} |")
extra = [m for m in meta if m.get('kind') != 'vocab']
nv = len(meta) - len(extra)
intro = f"**{len(meta)} picture files** for Lesson {N}: {nv} vocabulary cards for the New Words page" + (f" and {len(extra)} activity picture(s) for the student pages" if extra else '') + "."
txt = f"""# Image Credits and Licenses: Level 3, Lesson {N}

{intro} Every file is a PNG made by `tools/make_images_L3_L{N}.py` with the card helpers in `tools/l3img.py` (the same helpers and card style as the Level 1 and Level 2 `make_images.py` and Level 3 Lesson 1). Vocabulary cards are 600×420.

## Sources and licenses

1. **Twemoji graphics.** By Twitter, Inc. and other contributors; maintained fork: jdecked/twemoji, https://github.com/jdecked/twemoji. License: **CC BY 4.0**, https://creativecommons.org/licenses/by/4.0/ (LICENSE-GRAPHICS in the repository). **Changes made:** SVGs were rendered to PNG, resized, and combined on a white card with a border; some cards have added drawings and text labels.
2. **Original drawings** (speech bubbles, signs, forms, arrows, lines, simple shapes, text labels), drawn in code for this curriculum with no outside source.
3. **Text labels** use the DejaVu Sans font (free font license, https://dejavu-fonts.github.io/License.html).

No photos or stock-site images are used.

## Attribution line

> Pictures use Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The graphics were resized and combined, and speech bubbles, signs, and labels were added.

## File-by-file list

| File | Word / use | What it shows (drawn parts in brackets) | Twemoji source (CC BY 4.0) |
|---|---|---|---|
""" + '\n'.join(rows) + """

Course materials: © 2026 the authors, licensed under CC BY-NC-SA 4.0.
"""
open(f'{I}/CREDITS_L3_L{N}.md', 'w').write(txt); print(f'CREDITS_L3_L{N}.md:', len(meta), 'files')
