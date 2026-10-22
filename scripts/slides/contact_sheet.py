"""Contact sheet: all rendered slides of a deck on one image, labeled with their numbers, for a quick visual check.
Usage: python3 scripts/slides/contact_sheet.py <renderdir> <out.jpg> [--cols 6] [--width 1800]
<renderdir> is the folder render_deck.sh wrote (slide-01.jpg, slide-02.jpg, ...).
Two decks side by side (e.g. a rebuild against the published deck):
  python3 scripts/slides/contact_sheet.py <dirA> <out.jpg> --compare <dirB>   (each row: A slide | B slide)"""
import sys, glob, os, argparse
from PIL import Image, ImageDraw, ImageFont
ap = argparse.ArgumentParser(); ap.add_argument('dir'); ap.add_argument('out')
ap.add_argument('--cols', type=int, default=6); ap.add_argument('--width', type=int, default=1800); ap.add_argument('--compare')
a = ap.parse_args()
def files(d):
    fs = sorted(glob.glob(os.path.join(d, 'slide-*.jpg')))
    if not fs: sys.exit(f'no slide-*.jpg in {d} (run scripts/slides/render_deck.sh first)')
    return fs
A = files(a.dir); B = files(a.compare) if a.compare else None
pairs = list(zip(A, B)) if B else None
if B and len(A) != len(B): print(f'WARNING: {len(A)} vs {len(B)} slides')
cols = 2 if B else a.cols
tw = (a.width - 10 * (cols + 1)) // cols
w0, h0 = Image.open(A[0]).size; th = int(tw * h0 / w0); lab = 22
try: font = ImageFont.truetype('DejaVuSans-Bold.ttf', 16)
except OSError: font = ImageFont.load_default()
cells = [x for p in pairs for x in p] if B else A
rows = (len(cells) + cols - 1) // cols
sheet = Image.new('RGB', (a.width, 10 + rows * (th + lab + 10)), 'white'); d = ImageDraw.Draw(sheet)
for k, f in enumerate(cells):
    r, c = divmod(k, cols); x = 10 + c * (tw + 10); y = 10 + r * (th + lab + 10)
    im = Image.open(f).convert('RGB').resize((tw, th))
    sheet.paste(im, (x, y + lab)); d.rectangle([x, y + lab, x + tw - 1, y + lab + th - 1], outline='#999999')
    name = os.path.basename(f)[6:-4]
    d.text((x, y + 2), (('A ' if c == 0 else 'B ') if B else '') + f'slide {int(name)}', fill='black', font=font)
sheet.save(a.out, quality=85)
print(a.out, f'{len(A)} slides', f'(compared with {a.compare})' if B else '')
