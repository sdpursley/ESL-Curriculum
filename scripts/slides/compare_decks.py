"""Compare two decks slide by slide: slide count, kind tags, every shape (name, type, position, size, fill), every text run
(text, size, bold, color), every picture (SHA-1 of the image bytes, alt text), the click steps, and the notes.
Exit code 0 = same; 1 = differences (listed). Use it to check a rebuild against the published deck.
Usage: python3 scripts/slides/compare_decks.py <a.pptx> <b.pptx> [--ignore-notes]"""
import sys, hashlib
from lxml import etree
from pptx import Presentation
NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
      'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
def describe(path, notes=True):
    prs = Presentation(path); out = []
    for s in prs.slides:
        d = {'tag': s._element.find('p:cSld', NS).get('name'), 'shapes': [], 'steps': []}
        bg = s._element.find('p:cSld/p:bg', NS)
        d['bg'] = etree.tostring(bg).decode() if bg is not None else ''
        ids = {}
        for el in s.shapes._spTree:
            k = etree.QName(el).localname
            if k not in ('sp', 'pic', 'grpSp', 'cxnSp'): continue
            c = el.find('.//p:cNvPr', NS); ids[c.get('id')] = c.get('name')
            xf = el.find('.//a:xfrm', NS)
            geo = tuple(int(v) for v in (xf.find('a:off', NS).get('x'), xf.find('a:off', NS).get('y'),
                                         xf.find('a:ext', NS).get('cx'), xf.find('a:ext', NS).get('cy'))) if xf is not None else ()
            sppr = el.find('p:spPr', NS)
            style = etree.tostring(sppr).decode() if sppr is not None else ''
            if k == 'pic':
                blip = el.find('.//a:blip', NS)
                img = hashlib.sha1(s.part.related_part(blip.get('{%s}embed' % NS['r'])).blob).hexdigest()[:12]
                style = ''
            else: img = ''
            runs = []
            for p in el.iterfind('.//a:p', NS):
                runs.append(etree.tostring(p).decode())
            d['shapes'].append((c.get('name'), k, geo, style, img, c.get('descr') or '', tuple(runs)))
        for ctn in s._element.iterfind('.//p:timing//p:cTn[@nodeType]', NS):
            if ctn.get('nodeType') in ('clickEffect', 'withEffect', 'afterEffect'):
                d['steps'].append((ctn.get('nodeType'), tuple(sorted(ids.get(t.get('spid'), '?') for t in ctn.iterfind('.//p:spTgt', NS)))))
        d['notes'] = s.notes_slide.notes_text_frame.text if (notes and s.has_notes_slide) else ''
        out.append(d)
    return out
if __name__ == '__main__':
    a, b = sys.argv[1], sys.argv[2]; notes = '--ignore-notes' not in sys.argv
    A, B = describe(a, notes), describe(b, notes); diffs = []
    if len(A) != len(B): diffs.append(f'slide count {len(A)} vs {len(B)}')
    for i, (x, y) in enumerate(zip(A, B), 1):
        for key in ('tag', 'bg', 'steps', 'notes'):
            if x[key] != y[key]: diffs.append(f'slide {i}: {key} differs')
        if len(x['shapes']) != len(y['shapes']): diffs.append(f'slide {i}: {len(x["shapes"])} vs {len(y["shapes"])} shapes')
        for sx, sy in zip(x['shapes'], y['shapes']):
            if sx != sy:
                what = [n for n, u, v in zip(('name', 'type', 'geometry', 'shape style', 'picture', 'alt', 'text'), sx, sy) if u != v]
                diffs.append(f'slide {i}: shape {sx[0]!r}: {", ".join(what)} differ')
    print(f'{a} vs {b}: {len(A)} / {len(B)} slides;', 'SAME' if not diffs else f'{len(diffs)} differences')
    for d in diffs[:60]: print('  ' + d)
    sys.exit(1 if diffs else 0)
