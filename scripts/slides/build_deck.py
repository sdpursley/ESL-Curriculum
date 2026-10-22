"""Slide deck builder for Levels 3, 4, 5 (and any level whose decks carry slide-kind tags).

Builds levelV/slides/LevelV_LessonN_Slides.pptx from the PREVIOUS lesson's deck. Every slide of the new deck is a copy of
the start deck's slide of the same kind (same shapes, colors, fonts, sizes); the builder only re-writes the text, swaps
in the lesson's own picture files (byte-identical), re-flows rows when a lesson has more or fewer items, rebuilds the
click animations so that every click targets a shape that exists, and writes the speaker notes.
The lesson content comes from a spec file, levelV/slides/specs/LevelV_LessonN.py (see AGENTS.md section 6).

Usage (from the repository root):
  python3 scripts/slides/build_deck.py --level 3 --lesson 2 --out /tmp/deck/Level3_Lesson2_Slides.pptx
Options (defaults in brackets):
  --start     deck to copy from            [levelV/slides/LevelV_Lesson<N-1>_Slides.pptx]
  --fallback  deck for slide kinds/parts the start deck lacks  [levelV/slides/LevelV_Lesson1_Slides.pptx; for Lesson 1:
              level<V-1>/slides/Level<V-1>_Lesson1_Slides.pptx; else --start]
  --spec      lesson spec                  [levelV/slides/specs/LevelV_LessonN.py]
  --md        lesson Markdown              [levelV/curriculum/LevelV_LessonN.md, else levelV/drafts/curriculum/...]
  --images    picture folder(s), comma-separated  [levelV/images (+ levelV/drafts/images if it exists)]
  --out       output deck                  [build/slides/LevelV_LessonN_Slides.pptx]
Slide kinds are stored in each slide's <p:cSld name="L<V>:<kind>">; shapes are found by their names (role names such as
'title', 'R1 text', 'R2 ans'). Inspect any deck with scripts/slides/inspect_deck.py."""
import copy, io, re, sys, os, math, importlib.util
from lxml import etree
from pptx import Presentation
from PIL import Image

P = 'http://schemas.openxmlformats.org/presentationml/2006/main'
A = 'http://schemas.openxmlformats.org/drawingml/2006/main'
R = 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
NS = {'p': P, 'a': A, 'r': R}
E = 914400
INK, ACC = '1B2236', '5B3FC4'
def q(ns, t): return '{%s}%s' % (ns, t)

# ---------------------------------------------------------------- Level 3 Lesson 1 normalization (shape ids -> role names)
# The published Level 3 Lesson 1 deck was made by hand before this builder existed: its shapes have generic names.
# normalize() gives them role names and kind tags the first time it is used as a start/fallback deck. Every deck made by
# this builder (Level 3 Lessons 2-13, and Level 4/5 decks chained from them) is already tagged, so this is skipped.
L1_KINDS = ['title', 'goals', 'warmup', 'numlist', 'words', 'words', 'check', 'before', 'choice', 'choice', 'gaps',
            'checksay', 'qa', 'table', 'qa', 'free', 'gaps', 'mistakes', 'drill', 'talk', 'go', 'progress', 'goodbye', 'credits']
def _rows(**cols):
    m = {}
    for role, ids in cols.items():
        for k, i in enumerate(ids, 1):
            if i: m[i] = f'R{k} {role}'
    return m
def M(*ds):
    out = {}
    for d in ds: out.update(d)
    return out
_NUM = M(_rows(card=[3, 4, 5, 6, 7], text=[8, 11, 13, 15, 17], dot=[10, 12, 14, 16, 18], chip=[19, 21, 23, 25, 27],
                  num=[20, 22, 24, 26, 28]), {2: 'R1 shadow', 29: 'title', 30: 'side'})
NORM = {
    'title': {4: 'pic', 5: 'lesson', 8: 'title', 9: 'lead', 10: 'bullets'},
    'goodbye': {4: 'pic', 5: 'lesson', 8: 'title', 9: 'lead', 10: 'bullets'},
    'goals': M(_NUM, {9: 'R1 sub'}),
    'numlist': M(_NUM),
    'warmup': {8: 'kicker', 7: 'title', 9: 'box1', 14: 'box2', 15: 'pic'},
    'words': {8: 'title', 13: 'instr', 9: 'instr card'},
    'check': M(_rows(shadow=[4, 10, 16], card=[5, 11, 17], circle=[6, 12, 18], num=[7, 13, 19], q=[8, 14, 20],
                        pic=[101, 102, 103], ans=[25, 26, 27]), {2: 'title', 3: 'sub'}),
    'before': M(_rows(num=[11, 13, 15], hl=[25, 29, 33], voice=[27, 31, 35]), {8: 'title1', 9: 'title2', 10: 'context', 24: 'pic', 37: 'listen head', 39: 'listen 1',
                      41: 'listen 2', 43: 'audio', 46: 'play', 17: 'line 1', 18: 'line 2'}),
    'choice': {6: 'title', 7: 'instr'},
    'gaps': M(_rows(card=[4, 5, 6, 7, 50, 55], text=[11, 13, 15, 17, 51, 58], chip=[21, 23, 25, 27, 52, 56],
                       num=[22, 24, 26, 28, 53, 57], ans=[34, 35, 36, 37, 54, 59]), {29: 'title', 30: 'side', 8: 'head1', 9: 'head2', 2: 'head shadow', 3: 'head card'}),
    'checksay': M(_rows(card=[4, 5, 36], text=[11, 13, 39], chip=[21, 23, 37], num=[22, 24, 38], ans=[34, 35, 40]), {29: 'title', 30: 'side', 2: 'head shadow', 3: 'head card', 8: 'head1', 9: 'head2',
                        19: 'head chip', 20: 'head num', 6: 'S1 card', 15: 'S1 text', 7: 'S2 card', 17: 'S2 text'}),
    'qa': {7: 'head', 18: 'pic', 19: 'Q head', 20: 'A head', 8: 'left panel', 2: 'right panel'},
    'table': {7: 'head', 8: 'Q head', 11: 'A head', 17: 'pic', 4: 'left panel'},
    'free': {8: 'head', 21: 'pic', 9: 'line1', 10: 'ex1', 11: 'line2', 12: 'ex2', 13: 'side1', 17: 'side2'},
    'mistakes': {11: 'title', 21: 'pic'},
    'drill': {6: 'title', 25: 'sub', 13: 's1 label', 60: 's1 body', 17: 's2 label', 70: 's2 body', 26: 'pic'},
    'talk': {7: 'head', 8: 'grouping', 11: 'time', 18: 'pic'},
    'go': {6: 'title', 16: 'pic'},  # Num 01 / Label 01 / Body 01 / Num 02 / Label 02 / Body 02 keep their names
    'progress': {11: 'title', 62: 'ican', 22: 'A head', 23: 'Ans head'},
    'credits': {7: 'title', 15: 'pictures', 16: 'names', 17: 'audio'},
}

def cnv(el): return el.find('.//' + q(P, 'cNvPr'))
def sp_tree(slide): return slide.shapes._spTree
def shapes(slide): return [e for e in sp_tree(slide) if etree.QName(e).localname in ('sp', 'pic', 'grpSp', 'cxnSp')]
def kind_of(slide):
    m = re.match(r'^L\d+:(.+)$', slide._element.find(q(P, 'cSld')).get('name') or '')
    return m.group(1) if m else ''

def normalize(prs):
    sl = list(prs.slides)
    if kind_of(sl[0]):  # already a normalized (chained) deck
        return
    assert len(sl) == 24, 'expected the 24-slide Lesson 1 deck'
    for slide, kind in zip(sl, L1_KINDS):
        m = NORM.get(kind, {})
        for e in shapes(slide):
            c = cnv(e)
            if int(c.get('id')) in m: c.set('name', m[int(c.get('id'))])
        if kind == 'choice':  # Statement k / True k / False k / Circle k
            for e in shapes(slide):
                c = cnv(e); mm = re.match(r'(Statement|True|False|Circle) (\d+)$', c.get('name'))
                if mm: c.set('name', f"R{mm.group(2)} " + {'Statement': 'stmt', 'True': 'opt1', 'False': 'opt2', 'Circle': 'circle'}[mm.group(1)])
        slide._element.find(q(P, 'cSld')).set('name', 'L3:' + kind)

# ---------------------------------------------------------------- slide copy
def dup(prs, src):
    layout = next((l for l in prs.slide_layouts if l.name == src.slide_layout.name), prs.slide_layouts[0])
    new = prs.slides.add_slide(layout)
    tree = sp_tree(new)
    for el in list(tree)[2:]: tree.remove(el)
    for el in list(sp_tree(src))[2:]: tree.append(copy.deepcopy(el))
    sc, nc = src._element.find(q(P, 'cSld')), new._element.find(q(P, 'cSld'))
    bg = sc.find(q(P, 'bg'))
    if bg is not None: nc.insert(0, copy.deepcopy(bg))
    nc.set('name', sc.get('name', ''))
    for blip in tree.iter(q(A, 'blip')):
        part = src.part.related_part(blip.get(q(R, 'embed')))
        _, rid = new.part.get_or_add_image_part(io.BytesIO(part.blob))
        blip.set(q(R, 'embed'), rid)
    return new

# ---------------------------------------------------------------- shape helpers
def find(slide, name, must=True):
    for e in shapes(slide):
        if cnv(e).get('name') == name: return e
    if must: raise KeyError(f'{kind_of(slide)}: no shape {name!r}')
def findre(slide, pat): return [e for e in shapes(slide) if re.match(pat, cnv(e).get('name'))]
def remove(el): el.getparent().remove(el)
def next_id(slide): return max(int(cnv(e).get('id')) for e in shapes(slide)) + 1
def clone(slide, proto, name, after=None):
    el = copy.deepcopy(proto); c = cnv(el); c.set('id', str(next_id(slide))); c.set('name', name)
    sp_tree(slide).append(el); return el
def sid(el): return int(cnv(el).get('id'))
def xfrm(el): return el.find(q(P, 'spPr')).find(q(A, 'xfrm'))
def geom(el, x=None, y=None, w=None, h=None):
    xf = xfrm(el); off, ext = xf.find(q(A, 'off')), xf.find(q(A, 'ext'))
    if x is not None: off.set('x', str(int(round(x * E))))
    if y is not None: off.set('y', str(int(round(y * E))))
    if w is not None: ext.set('cx', str(int(round(w * E))))
    if h is not None: ext.set('cy', str(int(round(h * E))))
def getgeom(el):
    xf = xfrm(el); off, ext = xf.find(q(A, 'off')), xf.find(q(A, 'ext'))
    return int(off.get('x')) / E, int(off.get('y')) / E, int(ext.get('cx')) / E, int(ext.get('cy')) / E

# ---------------------------------------------------------------- text
TOK = re.compile(r'(\*\*.+?\*\*|\*.+?\*|\^.+?\^)')
def parse(s):
    out = []
    for t in TOK.split(s):
        if not t: continue
        if t.startswith('**') and t.endswith('**') and len(t) > 4: out.append((t[2:-2], 'b'))
        elif t.startswith('*') and t.endswith('*') and len(t) > 2: out.append((t[1:-1], 'acc'))
        elif t.startswith('^') and t.endswith('^') and len(t) > 2: out.append((t[1:-1], 'reg'))
        else: out.append((t, 'base'))
    return out
def _color(rpr):
    c = rpr.find(q(A, 'solidFill') + '/' + q(A, 'srgbClr'))
    return c.get('val') if c is not None else None
def _set_color(rpr, val):
    sf = rpr.find(q(A, 'solidFill'))
    if sf is None:
        sf = etree.Element(q(A, 'solidFill')); rpr.insert(0, sf)
    for ch in list(sf): sf.remove(ch)
    etree.SubElement(sf, q(A, 'srgbClr')).set('val', val)
def _base_rpr(p):
    runs = p.findall(q(A, 'r'))
    for r in runs:
        rp = r.find(q(A, 'rPr'))
        if rp is not None and _color(rp) == INK: return rp
    if runs and runs[0].find(q(A, 'rPr')) is not None: return runs[0].find(q(A, 'rPr'))
    e = p.find(q(A, 'endParaRPr'))
    if e is not None:
        rp = copy.deepcopy(e); rp.tag = q(A, 'rPr'); return rp
    rp = etree.Element(q(A, 'rPr')); rp.set('lang', 'en-US'); return rp
def _styled(base, style, sz):
    rp = copy.deepcopy(base); rp.tag = q(A, 'rPr')
    if style == 'b': rp.set('b', '1')
    elif style == 'acc': rp.set('b', '1'); _set_color(rp, ACC)
    elif style == 'reg': rp.set('b', '0'); _set_color(rp, INK)
    if sz: rp.set('sz', str(int(round(sz * 100))))
    return rp
def fill(el, paras, sz=None):
    """paras: list of str | (proto paragraph index, str) | (index, str, size)."""
    tb = el.find(q(P, 'txBody'))
    protos = tb.findall(q(A, 'p'))
    new = []
    for i, para in enumerate(paras):
        st, s, psz = (i, para, sz) if isinstance(para, str) else (para[0], para[1], para[2] if len(para) > 2 else sz)
        proto = protos[min(st, len(protos) - 1)]
        p = etree.Element(q(A, 'p'))
        ppr = proto.find(q(A, 'pPr'))
        if ppr is not None: p.append(copy.deepcopy(ppr))
        base = _base_rpr(proto)
        for line_no, line in enumerate(s.split('\n')):
            if line_no:
                br = etree.SubElement(p, q(A, 'br')); br.append(_styled(base, 'base', psz))
            for t, style in parse(line):
                r = etree.SubElement(p, q(A, 'r')); r.append(_styled(base, style, psz))
                etree.SubElement(r, q(A, 't')).text = t
        end = copy.deepcopy(base); end.tag = q(A, 'endParaRPr')
        for ch in list(end): end.remove(ch)
        if psz: end.set('sz', str(int(round(psz * 100))))
        p.append(end)
        new.append(p)
    for p in protos: tb.remove(p)
    for p in new: tb.append(p)
def set_runs(el, texts, para=0):
    p = el.find(q(P, 'txBody')).findall(q(A, 'p'))[para]
    runs = p.findall(q(A, 'r'))
    for r, t in zip(runs, texts): r.find(q(A, 't')).text = t
    for r in runs[len(texts):]: p.remove(r)
def set_sz(el, sz):
    for rp in el.iter(q(A, 'rPr'), q(A, 'endParaRPr')): rp.set('sz', str(int(round(sz * 100))))
def clear_text(el):
    tb = el.find(q(P, 'txBody'))
    if tb is None: return
    for p in tb.findall(q(A, 'p'))[1:]: tb.remove(p)
    p = tb.find(q(A, 'p'))
    for r in p.findall(q(A, 'r')) + p.findall(q(A, 'br')): p.remove(r)

# ---------------------------------------------------------------- pictures
IMG_DIRS = []
def img_path(name):
    for d in IMG_DIRS:
        f = os.path.join(d, name)
        if os.path.exists(f): return f
    raise FileNotFoundError(name)
def set_pic(slide, el, name, alt, box):
    path = img_path(name)
    _, rid = slide.part.get_or_add_image_part(path)
    el.find('.//' + q(A, 'blip')).set(q(R, 'embed'), rid)
    c = cnv(el); c.set('descr', alt); c.set('name', cnv(el).get('name'))
    w, h = Image.open(path).size
    x, y, bw, bh = box
    if w / h > bw / bh: nw, nh = bw, bw * h / w
    else: nw, nh = bh * w / h, bh
    geom(el, x + (bw - nw) / 2, y + (bh - nh) / 2, nw, nh)
    sr = el.find('.//' + q(A, 'srcRect'))
    if sr is not None: sr.getparent().remove(sr)

# ---------------------------------------------------------------- animations
def set_steps(slide, steps):
    """steps: list of lists of shape elements (or ids); each list = one click (first = click, rest = with)."""
    sld = slide._element
    t = sld.find(q(P, 'timing'))
    if t is not None: sld.remove(t)
    steps = [[x if isinstance(x, int) else sid(x) for x in st] for st in steps if st]
    if not steps: return
    n = [2]
    def nid(): n[0] += 1; return n[0]
    pars = []
    for st in steps:
        a, b = nid(), nid()
        effs = []
        for j, spid in enumerate(st):
            c, d, e = nid(), nid(), nid()
            effs.append(f'<p:par><p:cTn id="{c}" presetID="10" presetClass="entr" presetSubtype="0" fill="hold" nodeType="{"clickEffect" if j == 0 else "withEffect"}"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst><p:set><p:cBhvr><p:cTn id="{d}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl><p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr><p:to><p:strVal val="visible"/></p:to></p:set><p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="{e}" dur="400"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect></p:childTnLst></p:cTn></p:par>')
        pars.append(f'<p:par><p:cTn id="{a}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst><p:par><p:cTn id="{b}" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>{"".join(effs)}</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>')
    xml = (f'<p:timing xmlns:p="{P}"><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>'
           f'<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>{"".join(pars)}</p:childTnLst></p:cTn>'
           '<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
           '<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>'
           '</p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>')
    el = etree.fromstring(xml)
    ext = sld.find(q(P, 'extLst'))
    if ext is not None: ext.addprevious(el)
    else: sld.append(el)

# ---------------------------------------------------------------- row helper
def take_protos(slide, roles, idx=(1, 2)):
    """Copy row prototypes (R<idx> <role>) and delete every R<k> shape. Returns {(k, role): element}."""
    pr = {}
    for k in idx:
        for role in roles:
            e = find(slide, f'R{k} {role}', must=False)
            if e is None and k != idx[0]: e = pr.get((idx[0], role))
            if e is not None: pr[(k, role)] = copy.deepcopy(e)
    for e in findre(slide, r'R\d+ '): remove(e)
    return pr
def put(slide, pr, k, role, name, x, y, w, h, proto_k=None):
    pk = proto_k if proto_k is not None else (1 if k == 1 else 2)
    pe = next((pr[key] for key in ((pk, role), (1, role), (2, role)) if pr.get(key) is not None), None)
    el = clone(slide, pe, name)
    geom(el, x, y, w, h); return el

# ---------------------------------------------------------------- renderers
def r_title(s, d, ctx):
    fill(find(s, 'title'), [d['title']], sz=d.get('title_sz'))
    fill(find(s, 'lead'), [d.get('lead', 'Today you will:' if s is not None and kind_of(s) == 'title' else 'Now you can:')])
    fill(find(s, 'bullets'), ['•  ' + b for b in d['bullets']], sz=d.get('bullet_sz'))
    fill(find(s, 'lesson'), [f"Lesson {ctx['N']}  ·  Level {ctx['LEVEL']}"])
    set_pic(s, find(s, 'pic'), d['pic'], d['alt'], (8.45, 1.82, 3.8, 2.66))
    set_steps(s, [])

def r_numlist(s, d, ctx):
    goals = kind_of(s) == 'goals'
    fill(find(s, 'title'), d['title'], sz=d.get('title_sz'))
    fill(find(s, 'side'), d['side'], sz=d.get('side_sz'))
    pr = take_protos(s, ['shadow', 'card', 'text', 'sub', 'dot', 'chip', 'num'])
    rows = d['rows']; n = len(rows)
    tall = goals and isinstance(rows[0], (list, tuple))
    top = d.get('top', 2.226 if goals else 2.64); bottom = d.get('bottom', 6.413 if n <= 5 else 6.95)
    if n > 5 and 'top' not in d: top = 1.45 if goals else 2.2
    gap = 0.119
    if tall:
        h1 = 1.076; h = min(0.659, (bottom - top - (n - 1) * gap - h1) / (n - 1))
    else:
        h = min(0.659 if not goals else 0.78, (bottom - top - (n - 1) * gap) / n); h1 = h
    y = top; steps = []
    def tsz_for(t): return d.get('sz', 20 if len(re.sub(r'[*^]', '', t)) <= 30 and h >= 0.6 else 18)
    for k, row in enumerate(rows, 1):
        hh = h1 if k == 1 else h
        lab = d.get('labels', [f'{i:02d}' for i in range(1, n + 1)])[k - 1]
        els = []
        if k == 1:
            els.append(put(s, pr, 1, 'shadow', 'R1 shadow', 0.596, y + 0.063, 6.81, hh))
        els.append(put(s, pr, k, 'card', f'R{k} card', 1.732, y, 5.611, hh))
        els.append(put(s, pr, k, 'chip', f'R{k} chip', 0.596, y, 1.137, hh))
        nb = put(s, pr, k, 'num', f'R{k} num', 0.751, y + (hh - min(0.707, hh)) / 2, 1.213, min(0.707, hh)); fill(nb, [lab]); els.append(nb)
        if k == 1 and tall:
            t = put(s, pr, 1, 'text', 'R1 text', 1.98, y + 0.074, 4.85, 0.42); fill(t, [rows[0][0]], sz=d.get('sz', 20 if len(rows[0][0]) <= 28 else 18))
            sb = put(s, pr, 1, 'sub', 'R1 sub', 2.08, y + 0.514, 4.75, 0.45); fill(sb, [rows[0][1]], sz=d.get('sz', 20))
            els += [t, sb]
        else:
            t = put(s, pr, k, 'text', f'R{k} text', 1.98, y, 4.85, hh, proto_k=2); rt = row if isinstance(row, str) else row[0]; fill(t, [rt], sz=tsz_for(rt)); els.append(t)
        els.append(put(s, pr, k, 'dot', f'R{k} dot', 6.957, y + 0.146, 0.097, 0.084))
        steps.append(els); y += hh + gap
    set_steps(s, steps if d.get('animate', True) else [])

def r_warmup(s, d, ctx):
    fill(find(s, 'kicker'), [d['kicker']])
    fill(find(s, 'title'), d['title'], sz=d.get('title_sz'))
    fill(find(s, 'box1'), d['box1'], sz=d.get('box_sz'))
    fill(find(s, 'box2'), d['box2'], sz=d.get('box_sz'))
    if d.get('box1_geom'): geom(find(s, 'box1'), *d['box1_geom'])
    if d.get('box2_geom'): geom(find(s, 'box2'), *d['box2_geom'])
    set_pic(s, find(s, 'pic'), d['pic'], d['alt'], d.get('pic_box', (7.437, 2.301, 5.2, 3.64)))
    set_steps(s, [[find(s, 'box2')]] if d.get('reveal', True) else [])

def r_words(s, d, ctx):
    fill(find(s, 'title'), [d['title']], sz=d.get('title_sz'))
    fill(find(s, 'instr'), d['instr'])
    if d.get('instr_w'):
        geom(find(s, 'instr card'), w=d['instr_w']); geom(find(s, 'instr'), w=d['instr_w'] - 0.45)
    words = d['words']; steps = []
    cells = [(1.584, 2.5), (5.534, 2.5), (9.484, 2.5), (1.584, 4.72), (5.534, 4.72), (9.484, 4.72)]
    for k in range(1, 7):
        pic, lab = find(s, f'Word picture {k}'), find(s, f'Word label {k}')
        if k > len(words): remove(pic); remove(lab); continue
        w = words[k - 1]; cx, cy = cells[k - 1]
        set_pic(s, pic, w['file'], w['alt'], (cx, cy, 2.1, 1.47))
        text = ('*★* ' if w.get('star') else '') + w['word']
        fill(lab, [text], sz=w.get('sz', 20 if len(w['word']) <= 15 else 18))
        steps.append([lab])
    set_steps(s, steps)

def r_check(s, d, ctx):
    fill(find(s, 'title'), [d['title']]); fill(find(s, 'sub'), [d['sub']])
    steps = []
    for k, it in enumerate(d['items'], 1):
        fill(find(s, f'R{k} q'), [it['q']], sz=it.get('q_sz'))
        set_pic(s, find(s, f'R{k} pic'), it['pic'], it['alt'], (1.95 + 4 * (k - 1), 2.8, 2.1, 1.47))
        a = find(s, f'R{k} ans'); fill(a, [it['a']], sz=it.get('a_sz', 28 if len(it['a']) <= 8 else (22 if len(it['a']) <= 14 else 18))); steps.append([a])
    set_steps(s, steps)

def r_before(s, d, ctx):
    fill(find(s, 'title1'), [d.get('title1', 'Before You')]); fill(find(s, 'title2'), [d.get('title2', 'Listen')])
    fill(find(s, 'context'), [d['context']], sz=d.get('context_sz'))
    set_pic(s, find(s, 'pic'), d['pic'], d['alt'], d.get('pic_box', (0.175, 2.65, 3.0, 2.1)))
    for k, v in enumerate(d['voices'], 1): fill(find(s, f'R{k} voice'), [v])
    fill(find(s, 'listen head'), [d.get('listen_head', 'Listen for:')])
    fill(find(s, 'listen 1'), [d['listen'][0]], sz=d.get('listen_sz')); fill(find(s, 'listen 2'), [d['listen'][1]], sz=d.get('listen_sz'))
    fill(find(s, 'audio'), [d['audio']], sz=d.get('audio_sz'))
    fill(find(s, 'play'), [d.get('play', 'Play 1: *Task A*')])
    set_steps(s, [[find(s, f'R{k} hl')] for k in range(1, 4)])

def r_choice(s, d, ctx):
    fill(find(s, 'title'), [d['title']], sz=d.get('title_sz'))
    fill(find(s, 'instr'), d['instr'], sz=d.get('instr_sz'))
    for e in findre(s, r'Row picture'): remove(e)
    pr = take_protos(s, ['stmt', 'opt1', 'opt2', 'circle'], idx=(1,))
    rows = d['rows']; n = len(rows)
    top, bottom = 3.4, 7.0
    pitch = min(0.88, (bottom - top) / n); h = min(0.58, pitch - 0.08)
    nopt = max(len(r[1]) for r in rows)
    ow = d.get('ow', 1.5 if nopt <= 2 else 1.1); og = d.get('og', 0.4 if nopt <= 2 else 0.25)
    right = d.get('right', 12.0)
    x0 = 0.55
    if d.get('pic'):
        pb = d['pic_box']; x0 = pb[0] + pb[2] + 0.25
    ssz = d.get('sz', 22 if n <= 4 and nopt <= 2 else 20)
    steps = []
    for k, (stmt, opts, ans) in enumerate(rows, 1):
        y = top + (k - 1) * pitch
        ox = [right - (len(opts) - j) * ow - (len(opts) - j - 1) * og for j in range(len(opts))]
        st = put(s, pr, k, 'stmt', f'R{k} stmt', x0, y, ox[0] - 0.2 - x0, h, proto_k=1); fill(st, [stmt], sz=ssz)
        for j, o in enumerate(opts):
            oe = put(s, pr, k, 'opt1', f'R{k} opt{j + 1}', ox[j], y, ow, h, proto_k=1); fill(oe, [o], sz=d.get('osz', 20 if len(o) <= 8 else 17))
        for a in ([ans] if isinstance(ans, int) else (ans or [])):
            c = put(s, pr, k, 'circle', f'R{k} circle' + ('' if isinstance(ans, int) else f' {a}'), ox[a] - 0.14, y - 0.06, ow + 0.28, h + 0.12, proto_k=1)
            steps.append([c]) if isinstance(ans, int) or a == ans[0] else steps[-1].append(c)
    set_steps(s, steps)
    if d.get('pic'):
        add_picture(s, d['pic'], d['alt'], d['pic_box'], ctx)

def add_picture(s, name, alt, box, ctx):
    """Add a picture by cloning the pic element of a stock slide in this deck (any slide with a pic)."""
    pe = ctx['pic_proto']
    el = clone(s, pe, 'Row picture')
    set_pic(s, el, name, alt, box)
    # keep pictures behind the text: move right after the background shapes
    return el

def r_gaps(s, d, ctx):
    fill(find(s, 'title'), d['title'], sz=d.get('title_sz')); fill(find(s, 'side'), d['side'], sz=d.get('side_sz'))
    fill(find(s, 'head1'), [d['head1']]); fill(find(s, 'head2'), [d['head2']], sz=d.get('head2_sz'))
    pr = take_protos(s, ['card', 'text', 'chip', 'num', 'ans'], idx=(1,))
    rows = d['rows']; n = len(rows)
    hy = d.get('head_y', 1.476 if n <= 5 else 1.176)
    geom(find(s, 'head card'), y=hy); geom(find(s, 'head shadow'), y=hy + 0.063)
    geom(find(s, 'head1'), y=hy + 0.074); geom(find(s, 'head2'), y=hy + 0.514)
    top = hy + 1.076 + 0.07; bottom = 7.1
    pitch = min(0.86, (bottom - top) / n); h = min(0.78, pitch - 0.08)
    aw = d.get('aw', 1.6); ax = 8.28 - aw
    tsz = d.get('sz', 18 if h >= 0.62 else 16)
    steps = []
    hs = d.get('heights'); yy = top
    for k, (txt, ans) in enumerate(rows, 1):
        y = top + (k - 1) * pitch
        if hs: h = hs[k - 1]; y = yy; yy += h + 0.08
        put(s, pr, k, 'card', f'R{k} card', 1.732, y, 6.6, h, proto_k=1)
        put(s, pr, k, 'chip', f'R{k} chip', 0.596, y, 1.137, h, proto_k=1)
        nb = put(s, pr, k, 'num', f'R{k} num', 0.751, y + (h - 0.64) / 2, 1.213, 0.64, proto_k=1)
        fill(nb, [d.get('labels', [str(i) for i in range(1, n + 1)])[k - 1]])
        t = put(s, pr, k, 'text', f'R{k} text', 1.98, y, ax - 0.08 - 1.98, h, proto_k=1); fill(t, [txt], sz=tsz)
        a = put(s, pr, k, 'ans', f'R{k} ans', ax, y + (h - 0.5) / 2, aw, 0.5, proto_k=1)
        fill(a, [ans], sz=d.get('asz', 20 if len(ans) <= 9 else (17 if len(ans) <= 14 else 15))); steps.append([a])
    set_steps(s, steps)

def r_checksay(s, d, ctx):
    fill(find(s, 'title'), d['title'], sz=d.get('title_sz')); fill(find(s, 'side'), d['side'], sz=d.get('side_sz'))
    fill(find(s, 'head1'), [d['head1']], sz=d.get('head_sz')); fill(find(s, 'head2'), [d['head2']], sz=d.get('head_sz'))
    pr = take_protos(s, ['card', 'text', 'chip', 'num', 'ans'], idx=(1,))
    sp = {k: copy.deepcopy(find(s, f'S1 {k}')) for k in ('card', 'text')}
    for e in findre(s, r'S\d+ '): remove(e)
    hy = d.get('head_y', 1.776)
    for nm, dy in (('head card', 0), ('head shadow', 0.063), ('head chip', 0), ('head1', 0.074), ('head2', 0.514)):
        geom(find(s, nm), y=hy + dy)
    geom(find(s, 'head num'), y=hy + 0.143)
    if d.get('head_chip'):
        fill(find(s, 'head num'), [d['head_chip']], sz=d.get('head_chip_sz'))
    else:
        remove(find(s, 'head chip')); remove(find(s, 'head num'))
        geom(find(s, 'head card'), x=0.596, w=6.747)
        geom(find(s, 'head1'), x=0.85, w=6.2); geom(find(s, 'head2'), x=0.95, w=6.1)
    rows, says = d.get('rows', []), d.get('says', [])
    y = hy + 1.076 + 0.118
    h = d.get('h', 0.659); gap = 0.119
    steps = []
    aw = d.get('aw', 1.42); ax = 7.28 - aw
    for k, (lab, txt, ans) in enumerate(rows, 1):
        put(s, pr, k, 'card', f'R{k} card', 1.732, y, 5.611, h, proto_k=1)
        put(s, pr, k, 'chip', f'R{k} chip', 0.596, y, 1.137, h, proto_k=1)
        nb = put(s, pr, k, 'num', f'R{k} num', 0.751, y + (h - 0.64) / 2, 1.213, 0.64, proto_k=1); fill(nb, [lab])
        t = put(s, pr, k, 'text', f'R{k} text', 1.98, y, ax - 0.08 - 1.98, h, proto_k=1); fill(t, [txt], sz=d.get('sz', 18))
        a = put(s, pr, k, 'ans', f'R{k} ans', ax, y + (h - 0.5) / 2, aw, 0.5, proto_k=1); fill(a, [ans], sz=d.get('asz', 18)); steps.append([a])
        y += h + gap
    if rows: y += 0.1
    sh = d.get('say_h', 0.659)
    for k, txt in enumerate(says, 1):
        c = clone(s, sp['card'], f'S{k} card'); geom(c, 0.6, y, 7.4, sh)
        t = clone(s, sp['text'], f'S{k} text'); geom(t, 0.85, y, 6.95, sh); fill(t, [txt], sz=d.get('say_sz', 20))
        y += sh + gap
    set_steps(s, steps)

def r_qa(s, d, ctx):
    fill(find(s, 'head'), d['head'], sz=None)
    if d.get('title_sz'): set_sz_para(find(s, 'head'), 1, d['title_sz'])
    set_pic(s, find(s, 'pic'), d['pic'], d['alt'], d.get('pic_box', (8.55, 1.25, 3.0, 2.1)))
    fill(find(s, 'Q head'), [d.get('qhead', 'QUESTION')], sz=d.get('head_sz')); fill(find(s, 'A head'), [d.get('ahead', 'ANSWER')], sz=d.get('head_sz'))
    if d.get('head_w'): geom(find(s, 'Q head'), x=1.62, w=d['head_w']); geom(find(s, 'A head'), x=7.6, w=d['head_w'])
    protos = {r: copy.deepcopy(find(s, f'{r} 1')) for r in ('Highlight', 'Helper', 'Question', 'Answer bg', 'Answer')}
    for e in findre(s, r'(Highlight|Helper|Question|Answer bg|Answer) \d+$'): remove(e)
    rows = d['rows']; n = len(rows)
    top, bottom = 4.3, 6.98
    pitch = min(d.get('pitch_max', 0.85), (bottom - top) / n); h = pitch - 0.05
    small = pitch < 0.8
    hw = d.get('hw', 1.9); qx = 1.62 + hw + 0.1; qw = 6.57 - qx
    steps = []
    for k, (helper, ques, ans) in enumerate(rows, 1):
        y = top + (k - 1) * pitch + 0.05
        if helper:
            hl = clone(s, protos['Highlight'], f'Highlight {k}'); geom(hl, 1.62, y + (h - min(0.6, h - 0.1)) / 2, hw, min(0.6, h - 0.1))
            he = clone(s, protos['Helper'], f'Helper {k}'); geom(he, 1.62, y, hw, h); fill(he, [helper], sz=d.get('hsz', 20 if small or len(helper) > 9 else 22))
            qe = clone(s, protos['Question'], f'Question {k}'); geom(qe, qx, y, qw, h)
        else:
            qe = clone(s, protos['Question'], f'Question {k}'); geom(qe, 1.62, y, 4.95, h)
        fill(qe, [ques], sz=d.get('qsz', 18 if small else 20))
        bg = clone(s, protos['Answer bg'], f'Answer bg {k}'); geom(bg, 7.6, y, 4.95, h)
        an = clone(s, protos['Answer'], f'Answer {k}'); geom(an, 7.6, y, 4.95, h)
        fill(an, ans if isinstance(ans, list) else [ans], sz=d.get('asz', 17 if small else 19))
        steps.append([an, bg])
    set_steps(s, steps)

def set_sz_para(el, idx, sz):
    p = el.find(q(P, 'txBody')).findall(q(A, 'p'))[idx]
    for rp in p.iter(q(A, 'rPr'), q(A, 'endParaRPr')): rp.set('sz', str(int(sz * 100)))

def r_table(s, d, ctx):
    fill(find(s, 'head'), d['head'])
    if d.get('title_sz'): set_sz_para(find(s, 'head'), 1, d['title_sz'])
    fill(find(s, 'Q head'), [d.get('qhead', 'SOMEONE SAYS')]); fill(find(s, 'A head'), [d.get('ahead', 'YOU ASK A FOLLOW-UP')], sz=d.get('head_sz'))
    if d.get('head_sz'): set_sz(find(s, 'Q head'), d['head_sz'])
    set_pic(s, find(s, 'pic'), d['pic'], d['alt'], d.get('pic_box', (0.5, 2.477, 3.638, 2.547)))
    protos = {r: copy.deepcopy(find(s, f'{r} 1')) for r in ('Question', 'Answer bg', 'Answer')}
    for e in findre(s, r'(Question|Answer bg|Answer) \d+$'): remove(e)
    rows = d['rows']; n = len(rows)
    top, bottom = 2.5, 7.2
    pitch = min(d.get('pitch_max', 0.78), (bottom - top) / n); h = pitch - 0.08
    lw = d.get('lw', 3.05); ax = 5.62 + lw + 0.08; aw = 13.05 - ax
    geom(find(s, 'A head'), x=ax, w=aw); geom(find(s, 'Q head'), x=5.65, w=lw)
    steps = []
    for k, (left, right) in enumerate(rows, 1):
        y = top + (k - 1) * pitch
        qe = clone(s, protos['Question'], f'Question {k}'); geom(qe, 5.62, y, lw, h); fill(qe, [left], sz=d.get('lsz', 18 if pitch >= 0.7 else 16))
        bg = clone(s, protos['Answer bg'], f'Answer bg {k}'); geom(bg, ax, y, aw, h)
        an = clone(s, protos['Answer'], f'Answer {k}'); geom(an, ax, y, aw, h)
        fill(an, right if isinstance(right, list) else [right], sz=d.get('rsz', 18 if pitch >= 0.7 else 16))
        steps.append([an, bg])
    set_steps(s, steps)

def r_free(s, d, ctx):
    fill(find(s, 'head'), d['head'])
    if d.get('title_sz'): set_sz_para(find(s, 'head'), 1, d['title_sz'])
    set_pic(s, find(s, 'pic'), d['pic'], d['alt'], d.get('pic_box', (0.7, 3.37, 2.38, 1.667)))
    fill(find(s, 'line1'), [d['line1']], sz=d.get('line_sz')); fill(find(s, 'ex1'), d['ex1'], sz=d.get('ex_sz'))
    fill(find(s, 'line2'), [d['line2']], sz=d.get('line_sz')); fill(find(s, 'ex2'), d['ex2'], sz=d.get('ex_sz'))
    steps = [[find(s, 'ex1')], [find(s, 'ex2')]]
    for k in (1, 2):
        e = find(s, f'side{k}')
        if d.get(f'side{k}'):
            fill(e, d[f'side{k}']); steps[k - 1].append(e)
            if d.get('side_sz'): set_sz_para(e, 0, d['side_sz'])
        else: remove(e)
    set_steps(s, steps)

def r_mistakes(s, d, ctx):
    fill(find(s, 'title'), [d.get('title', 'Common Mistakes')])
    set_pic(s, find(s, 'pic'), d['pic'], d['alt'], (11.5, 1.45, 1.7, 1.19))
    protos = {r: copy.deepcopy(find(s, f'{r} 1')) for r in ('Bad', 'Good')}
    for e in findre(s, r'(Bad|Good) \d+$'): remove(e)
    rows = d['rows']
    sz = d.get('sz', 17)
    def lines(r):
        bad, good = r
        g = good if isinstance(good, list) else [good]
        clean = lambda t: re.sub(r'[*^]', '', t)
        return max(math.ceil(len(clean(bad)) * sz / 17 / 30), sum(math.ceil(len(clean(x)) * sz / 17 / 52) for x in g), 1)
    hs = [0.3 * lines(r) * sz / 17 + 0.25 for r in rows]
    top, bottom = 2.7, 7.1
    gap = 0.07
    while sum(hs) + gap * (len(rows) - 1) > bottom - top and sz > 14:
        sz -= 1; hs = [0.3 * lines(r) * sz / 17 + 0.22 for r in rows]
    y = top; steps = []
    for k, ((bad, good), h) in enumerate(zip(rows, hs), 1):
        b = clone(s, protos['Bad'], f'Bad {k}'); geom(b, 1.0, y, 3.55, h); fill(b, [bad], sz=sz)
        g = clone(s, protos['Good'], f'Good {k}'); geom(g, 5.25, y, 5.9, h); fill(g, good if isinstance(good, list) else [good], sz=sz)
        steps.append([g]); y += h + gap
    set_steps(s, steps)

def r_drill(s, d, ctx):
    fill(find(s, 'title'), [d.get('title', 'Pair Drill')]); fill(find(s, 'sub'), [d['sub']], sz=d.get('sub_sz'))
    fill(find(s, 's1 label'), [d['s1_label']], sz=d.get('label_sz')); fill(find(s, 's1 body'), d['s1_body'], sz=d.get('body_sz'))
    fill(find(s, 's2 label'), [d['s2_label']], sz=d.get('label_sz')); fill(find(s, 's2 body'), d['s2_body'], sz=d.get('body_sz'))
    set_pic(s, find(s, 'pic'), d['pic'], d['alt'], d.get('pic_box', (1.394, 4.025, 3.773, 2.641)))
    set_steps(s, [])

def r_talk(s, d, ctx):
    fill(find(s, 'head'), d['head'])
    if d.get('sub_sz'): set_sz_para(find(s, 'head'), 1, d['sub_sz'])
    fill(find(s, 'grouping'), d['grouping'], sz=d.get('grouping_sz'))
    fill(find(s, 'time'), [d.get('time', '7:00–7:12')])
    set_pic(s, find(s, 'pic'), d['pic'], d['alt'], d.get('pic_box', (0.794, 3.739, 4.246, 2.972)))
    steps = []
    for k, st in enumerate(d['steps'], 1):
        e = find(s, f'Step {k}'); fill(e, st, sz=d.get('step_sz'))
        steps.append([find(s, f'Step num {k}'), e])
    set_steps(s, steps)

def r_go(s, d, ctx):
    set_runs(find(s, 'title'), [d.get('title', 'Before You Go   '), d.get('time', '7:12–7:17')])
    set_pic(s, find(s, 'pic'), d['pic'], d['alt'], d.get('pic_box', (0.85, 2.9, 3.3, 2.31)))
    fill(find(s, 'Label 01'), [d.get('label1', 'Exit ticket')]); fill(find(s, 'Body 01'), d['body1'], sz=d.get('body_sz'))
    fill(find(s, 'Label 02'), [d.get('label2', 'Homework')]); fill(find(s, 'Body 02'), d['body2'], sz=d.get('body_sz'))
    ly, by, bh = (3.25, 3.85, 2.7) if d.get('compact') else (3.65, 4.35, 2.4)
    for nm in ('Num 01', 'Label 01', 'Num 02', 'Label 02'): geom(find(s, nm), y=ly)
    for nm in ('Body 01', 'Body 02'): geom(find(s, nm), y=by, h=bh)
    set_steps(s, [])

def r_progress(s, d, ctx):
    set_runs(find(s, 'title'), ['Progress Check   ', d.get('time', '7:25')])
    fill(find(s, 'A head'), [d['ahead']], sz=d.get('ahead_sz')); fill(find(s, 'Ans head'), [d.get('anshead', 'Answer')])
    fill(find(s, 'ican'), d['ican'], sz=None)
    if d.get('ican_sz'):
        ps = find(s, 'ican').find(q(P, 'txBody')).findall(q(A, 'p'))
        for p in ps[3:]:
            for rp in p.iter(q(A, 'rPr'), q(A, 'endParaRPr')): rp.set('sz', str(int(d['ican_sz'] * 100)))
    protos = {r: copy.deepcopy(find(s, f'{r} 1')) for r in ('Bad', 'Good')}
    for e in findre(s, r'(Bad|Good) \d+$'): remove(e)
    rows = d['rows']; n = len(rows)
    top, bottom = 4.2, 6.85
    pitch = min(0.62, (bottom - top) / n) if not d.get('stacked') else (bottom - top) / n
    h = pitch - 0.04
    steps = []
    for k, (item, ans) in enumerate(rows, 1):
        y = top + (k - 1) * pitch
        b = clone(s, protos['Bad'], f'Bad {k}'); geom(b, 0.95, y, 5.95, h); fill(b, item if isinstance(item, list) else [item], sz=d.get('sz', 17))
        g = clone(s, protos['Good'], f'Good {k}'); geom(g, 7.4, y, 1.6, h); fill(g, [ans], sz=d.get('asz', 24 if len(ans) <= 3 else 17))
        steps.append([g])
    set_steps(s, steps)

def r_credits(s, d, ctx):
    fill(find(s, 'pictures'), d['pictures'], sz=None)
    fill(find(s, 'names'), d['names']); fill(find(s, 'audio'), d['audio'])
    set_steps(s, [])

RENDER = {'title': r_title, 'goodbye': r_title, 'goals': r_numlist, 'numlist': r_numlist, 'warmup': r_warmup,
          'words': r_words, 'check': r_check, 'before': r_before, 'choice': r_choice, 'gaps': r_gaps,
          'checksay': r_checksay, 'qa': r_qa, 'table': r_table, 'free': r_free, 'mistakes': r_mistakes,
          'drill': r_drill, 'talk': r_talk, 'go': r_go, 'progress': r_progress, 'credits': r_credits}

def publish_line(t, audio_ready):
    """Notes wording for the public site: never name a file the site does not have, never point to unpublished files."""
    if not audio_ready:
        t = re.sub(r'The audio \(L\d+_L\d+_listening\.mp3, about ([\d:]+)[^)]*\) plays (?:(.*?) )?once\. Press play again for play 2\. A third play is fine if the class needs it\.',
                   lambda m: f'The audio (about {m.group(1)}) is coming soon. When it is ready, it plays {(m.group(2) + " ") if m.group(2) else ""}once; press play again for play 2. Until then, read the listening script (at the end of these notes) with a volunteer.', t)
    t = re.sub(r'^Source: Level\d+_Lesson\d+\.md \((.*)\)\.?$', r'Lesson plan: \1.', t)
    t = re.sub(r'^Source: Level\d+_Lesson\d+\.md \((.*)\); images/CREDITS\.md\.$', r'Lesson plan: \1. Picture list: images/CREDITS.md.', t)
    return t

def set_notes(slide, lines, audio_ready):
    tf = slide.notes_slide.notes_text_frame
    tf.text = '\n'.join(publish_line(l, audio_ready) for l in lines)

def load_spec(spec_path, cfg):
    """Fill deckspec.CFG, then run the spec file (it does `from deckspec import *`)."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import deckspec
    deckspec.CFG.update(cfg)
    spec_mod = importlib.util.spec_from_file_location('spec', spec_path); spec = importlib.util.module_from_spec(spec_mod)
    spec_mod.loader.exec_module(spec)
    return spec

def build(start, spec_path, out, fallback=None, cfg=None):
    cfg = cfg or {}
    spec = load_spec(spec_path, cfg)
    LEVEL = cfg.get('level', 3); audio_ready = cfg.get('audio', False)
    IMG_DIRS[:] = cfg.get('images', [])
    fallback = fallback or start
    prs = Presentation(start); normalize(prs)
    orig = list(prs.slides)
    fb = Presentation(fallback); normalize(fb)
    def names(sl): return {cnv(e).get('name') for e in shapes(sl)}
    def required(sl):
        k = kind_of(sl)
        return {nm for nm in names(sl) if k == 'words' or not (re.match(r'^(R([3-9]|\d\d)|S[2-9]) ', nm) or re.search(r' ([2-9]|\d\d)$', nm))}
    req = {}
    for sl in fb.slides: req.setdefault(kind_of(sl), required(sl))
    protos, from_fb = {}, []
    for kind in req:
        cand = [sl for sl in orig if kind_of(sl) == kind and req[kind] <= names(sl)]
        if cand: protos[kind] = cand[0]
        else:
            protos[kind] = next(sl for sl in fb.slides if kind_of(sl) == kind); from_fb.append(kind)
    if from_fb and fallback != start: print('kinds taken from the fallback deck (not complete in the start deck):', ', '.join(from_fb))
    missing = sorted({sd['kind'] for sd in spec.SLIDES} - set(protos))
    if missing: raise SystemExit(f'no slide of kind {missing} in the start or fallback deck')
    pic_proto = None
    for sl in orig:
        for e in shapes(sl):
            if etree.QName(e).localname == 'pic': pic_proto = copy.deepcopy(e); break
        if pic_proto is not None: break
    ctx = {'N': spec.N, 'LEVEL': LEVEL, 'pic_proto': pic_proto}
    for i, sd in enumerate(spec.SLIDES, 1):
        kind = sd['kind']
        src = protos[kind]
        new = dup(prs, src)
        new._element.find(q(P, 'cSld')).set('name', f'L{LEVEL}:{kind}')
        try:
            RENDER[kind](new, sd, ctx)
        except Exception as ex:
            raise SystemExit(f'slide {i} ({kind}): {ex!r}')
        notes = list(sd['notes'])
        if kind == 'before' and not audio_ready: notes += spec.listening_script(spec.N)
        set_notes(new, notes, audio_ready)
    lst = prs.slides._sldIdLst
    for sld in list(lst)[:len(orig)]:
        prs.part.drop_rel(sld.rId); lst.remove(sld)
    prs.core_properties.title = spec.DECK_TITLE
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    prs.save(out)
    prune_package(out)
    print(out, len(spec.SLIDES), 'slides')

def prune_package(path):
    """Drop package parts that no relationship reaches any more (pictures and slides of the start deck that were
    removed) and their [Content_Types].xml overrides. Keeps the file small; PowerPoint and LibreOffice open it as before."""
    import zipfile, posixpath, shutil, tempfile
    z = zipfile.ZipFile(path); names = set(z.namelist())
    RELNS = 'http://schemas.openxmlformats.org/package/2006/relationships'
    data = {n: z.read(n) for n in names}
    # 1. picture relationships a slide no longer uses (its picture was swapped for the lesson's own file)
    for n in names:
        m = re.match(r'ppt/slides/(slide\d+\.xml)$', n)
        if not m: continue
        rp = f'ppt/slides/_rels/{m.group(1)}.rels'
        if rp not in data: continue
        used = set(re.findall(rb'r:(?:embed|id|link|pict)="(rId\d+)"', data[n]))
        rels = etree.fromstring(data[rp]); changed = False
        for r in list(rels):
            if r.get('Type', '').endswith('/image') and r.get('Id').encode() not in used:
                rels.remove(r); changed = True
        if changed: data[rp] = etree.tostring(rels, xml_declaration=True, encoding='UTF-8', standalone=True)
    keep, todo = {'[Content_Types].xml', '_rels/.rels'}, ['']
    while todo:
        part = todo.pop(); d, b = posixpath.split(part)
        rp = posixpath.join(d, '_rels', b + '.rels') if part else '_rels/.rels'
        if rp not in names: continue
        keep.add(rp)
        for r in etree.fromstring(data[rp]).iter('{%s}Relationship' % RELNS):
            if r.get('TargetMode') == 'External': continue
            t = r.get('Target')
            t = t.lstrip('/') if t.startswith('/') else posixpath.normpath(posixpath.join(d, t))
            if t in names and t not in keep: keep.add(t); todo.append(t)
    drop = names - keep
    ct = etree.fromstring(data['[Content_Types].xml'])
    for o in list(ct):
        if o.get('PartName') and o.get('PartName').lstrip('/') in drop: ct.remove(o)
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix='.pptx').name
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as w:
        for i in z.infolist():
            if i.filename in drop: continue
            w.writestr(i, etree.tostring(ct, xml_declaration=True, encoding='UTF-8', standalone=True) if i.filename == '[Content_Types].xml' else data[i.filename])
    z.close(); os.chmod(tmp, 0o644); shutil.move(tmp, path)

def main():
    import argparse
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--level', type=int, required=True); ap.add_argument('--lesson', type=int, required=True)
    for k in ('start', 'fallback', 'spec', 'md', 'images', 'out'): ap.add_argument('--' + k)
    a = ap.parse_args(); V, N = a.level, a.lesson
    first = lambda *ps: next((p for p in ps if p and os.path.exists(p)), None)
    deck = lambda n: f'level{V}/slides/Level{V}_Lesson{n}_Slides.pptx'
    start = a.start or (deck(N - 1) if N > 1 else None)
    if not start or not os.path.exists(start):
        raise SystemExit(f'start deck not found: {start!r}. Lesson 1 of a new level needs --start (the last deck of the level below).')
    # fallback = this level's Lesson 1 deck; for Lesson 1 of a new level, the Lesson 1 deck of the level below
    fallback = a.fallback or first(deck(1) if N > 1 else None, f'level{V-1}/slides/Level{V-1}_Lesson1_Slides.pptx') or start
    spec = a.spec or f'level{V}/slides/specs/Level{V}_Lesson{N}.py'
    md = a.md or first(f'level{V}/curriculum/Level{V}_Lesson{N}.md', f'level{V}/drafts/curriculum/Level{V}_Lesson{N}.md')
    if not md: raise SystemExit('lesson Markdown not found: pass --md')
    images = a.images.split(',') if a.images else [d for d in (f'level{V}/images', f'level{V}/drafts/images') if os.path.isdir(d)]
    out = a.out or f'build/slides/Level{V}_Lesson{N}_Slides.pptx'
    audio = os.path.exists(f'level{V}/audio/L{V}_L{N}_listening.mp3')
    print(f'Level {V} Lesson {N}: start={start} fallback={fallback} spec={spec} md={md} images={images} audio ready={audio}')
    build(start, spec, out, fallback, dict(level=V, lesson=N, md=md, images=images, audio=audio))

if __name__ == '__main__':
    main()
