"""Write CREDITS.md for Level 4 pictures from every images_L4_L<N>.json in a folder (one combined list, lesson by lesson).
Usage: python make_credits_L4.py IMAGES_DIR [N]   (N is ignored; kept so the build script can pass it)"""
import sys, json, os, glob, re
D = sys.argv[1]
U = 'https://raw.githubusercontent.com/jdecked/twemoji/main/assets/svg/'
files = sorted(glob.glob(f'{D}/images_L4_L*.json'), key=lambda p: int(re.search(r'_L(\d+)\.json', p).group(1)))
secs = []; total = 0
for p in files:
    n = re.search(r'_L(\d+)\.json', p).group(1); meta = json.load(open(p)); total += len(meta)
    nv = sum(1 for m in meta if m.get('kind') == 'vocab')
    rows = [f"| {m['file']} | {m['word']} | {m['note']} | " + (', '.join(f'[{c}]({U}{c}.svg)' for c in m['twemoji']) or 'none (our own drawing)') + ' |' for m in meta]
    secs.append(f"### Lesson {n}\n\n{len(meta)} files: {nv} vocabulary cards" + (f" and {len(meta)-nv} activity picture(s)" if len(meta) > nv else '') +
                f". Made by `tools/make_images_L4_L{n}.py`.\n\n| File | Word / use | What it shows (drawn parts in brackets) | Twemoji source (CC BY 4.0) |\n|---|---|---|---|\n" + '\n'.join(rows))
txt = f"""# Image Credits and Licenses: Level 4

**Status:** Draft for review; not published.

**{total} picture files** for the Level 4 lessons in this folder. Every file is a PNG made by `tools/make_images_L4_L<N>.py` with the card helpers in
`tools/l4img.py` (copied from the Level 3 `l3img.py`; same card style as Levels 1-3). Vocabulary cards are 600×420.

## Sources and licenses

1. **Twemoji graphics.** By Twitter, Inc. and other contributors; maintained fork: jdecked/twemoji, https://github.com/jdecked/twemoji. License: **CC BY 4.0**, https://creativecommons.org/licenses/by/4.0/ (LICENSE-GRAPHICS in the repository). **Changes made:** SVGs were rendered to PNG, resized, and combined on a white card with a border; some cards have added drawings and text labels.
2. **Original drawings** (signs, forms, arrows, lines, simple shapes, text labels), drawn in code for this curriculum with no outside source.
3. **Text labels** use the DejaVu Sans font (free font license, https://dejavu-fonts.github.io/License.html).

No photos or stock-site images are used.

## Attribution line

> Pictures use Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The graphics were resized and combined, and signs and labels were added.

## File-by-file list

""" + '\n\n'.join(secs) + """

Course materials: © 2026 the authors, licensed under CC BY-NC-SA 4.0.
"""
open(f'{D}/CREDITS.md', 'w').write(txt); print('CREDITS.md:', total, 'files')
