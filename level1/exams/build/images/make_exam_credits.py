"""Write images/CREDITS.md from images_L1_exams.json.  Usage: python3 make_exam_credits.py IMAGES_DIR"""
import json, sys, os
D = sys.argv[1]; meta = json.load(open(os.path.join(D, 'images_L1_exams.json')))
U = 'https://raw.githubusercontent.com/jdecked/twemoji/main/assets/svg/'
L = ['# Image Credits and Licenses: Level 1 Midterm and Final Exams', '',
     f'**{len(meta)} picture files** for the Level 1 exam pages. Every file is made by `build/images/make_exam_images.py` with the same card style as the Level 1 lessons (600×420 PNG with a grey border; the two practice cards are 1200 px wide).', '',
     '## Sources and licenses', '',
     '1. **Twemoji graphics.** By Twitter, Inc. and other contributors; maintained fork: jdecked/twemoji, https://github.com/jdecked/twemoji. License: **CC BY 4.0**, https://creativecommons.org/licenses/by/4.0/ (LICENSE-GRAPHICS in the repository). **Changes made:** SVGs were rendered to PNG, resized, and combined on a white card with a border; some cards have added drawings and text.',
     '2. **Original drawings** (clock faces, price tags, the two practice cards, highlight circles), drawn in code for this curriculum with no outside source.',
     '3. **Text on pictures** uses the DejaVu Sans font (free font license, https://dejavu-fonts.github.io/License.html).', '',
     'No photos or stock-site images are used. All names, numbers, and addresses on the cards are invented.', '',
     '## Attribution line', '',
     '> Pictures use Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The graphics were resized and combined, and drawings and labels were added.', '',
     '## File-by-file list', '',
     '| File | Word | What it shows | Twemoji source (CC BY 4.0) | Original drawn parts |', '|---|---|---|---|---|']
for m in meta:
    src = ', '.join(f'[{c}]({U}{c}.svg)' for c in m['twemoji']) or 'none (all drawn)'
    L.append(f"| {m['file']} | {m['word']} | {m['note']} | {src} | {m.get('drawn', 'border only')} |")
open(os.path.join(D, 'CREDITS.md'), 'w').write('\n'.join(L) + '\n'); print('credits', len(meta))
