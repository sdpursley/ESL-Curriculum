"""Draft the credits section for one Level 1 lesson from images_L1_L<N>.json.  Usage: python make_credits.py N ../..   (from level1/images/tools/lib)
Writes CREDITS_L1_L<N>.new.md next to the pictures (not committed). Check it, demote its headings by one level, and paste it
over that lesson's section in level1/images/CREDITS.md (one file, one section per lesson)."""
import json, sys, os
N, D = sys.argv[1], sys.argv[2]
meta = json.load(open(os.path.join(D, f'images_L1_L{N}.json')))
U = 'https://raw.githubusercontent.com/jdecked/twemoji/main/assets/svg/'
L = [f'# Image Credits and Licenses: Level 1, Lesson {N} vocabulary', '',
     f'**{len(meta)} picture files** for the Lesson {N} pages. Every file is a 600×420 PNG card made by `level1/images/tools/make_images_L1_L{N}.py`, which reuses the helpers and card style of Lesson 1 and the Level 2 `make_images.py` (copy in `level1/images/tools/lib/`).', '',
     '## Sources and licenses', '',
     '1. **Twemoji graphics.** By Twitter, Inc. and other contributors; maintained fork: jdecked/twemoji, https://github.com/jdecked/twemoji. License: **CC BY 4.0**, https://creativecommons.org/licenses/by/4.0/ (LICENSE-GRAPHICS in the repository). **Changes made:** SVGs were rendered to PNG, resized, and combined on a white card with a border; some cards have added drawings and text labels.',
     '2. **Original drawings** (forms, cards, phone screens, family-tree lines, labels), drawn in code for this curriculum with no outside source.',
     '3. **Text labels** use the DejaVu Sans font (free font license, https://dejavu-fonts.github.io/License.html).', '',
     'No photos or stock-site images are used.', '',
     '## Attribution line', '',
     '> Vocabulary pictures use Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The graphics were resized and combined, and drawings and labels were added.', '',
     '## File-by-file list', '',
     '| File | Word | What it shows | Twemoji source (CC BY 4.0) | Original drawn parts |', '|---|---|---|---|---|']
for m in meta:
    src = ', '.join(f'[{c}]({U}{c}.svg)' for c in m['twemoji']) or 'none (all drawn)'
    L.append(f"| {m['file']} | {m['word']} | {m['note']} | {src} | {m.get('drawn', 'border only')} |")
open(os.path.join(D, f'CREDITS_L1_L{N}.new.md'), 'w').write('\n'.join(L) + '\n'); print('ok', len(meta))
