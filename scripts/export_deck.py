"""Export a .pptx deck into a JSON slide description for the in-browser presenter.
Usage: python3 scripts/export_deck.py <deck.pptx> <lesson number>              (Level 2: writes src/decks/lesson<N>.json)
       python3 scripts/export_deck.py <deck.pptx> <lesson number> --level 1    (Level 1: writes src/decks/level1/lesson<N>.json,
                                                                                 pictures matched against public/level1/images/)
       python3 scripts/export_deck.py <deck.pptx> <lesson number> --level 3    (Level 3: src/decks/level3/lesson<N>.json, public/level3/images/) Every shape keeps its exact EMU geometry, fill,
outline, and text runs. Reveal steps come from the pptx animation timeline:
each clickEffect starts a new step; withEffect/afterEffect join the current step."""
import sys, re, json, zipfile, os, posixpath
from lxml import etree
NS={'p':'http://schemas.openxmlformats.org/presentationml/2006/main',
    'a':'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'rel':'http://schemas.openxmlformats.org/package/2006/relationships'}
args=sys.argv[1:]; LEVEL=2
if '--level' in args:
    k=args.index('--level'); LEVEL=int(args[k+1]); del args[k:k+2]
SRC, N = args[0], int(args[1])
HERE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_URL='images/' if LEVEL==2 else f'level{LEVEL}/images/'          # picture URL prefix used by the site
SITE_IMAGES=os.path.join(HERE,'public',*IMG_URL.strip('/').split('/'))
OUT_DIR=os.path.join(HERE,'src','decks') if LEVEL==2 else os.path.join(HERE,'src','decks',f'level{LEVEL}')
z=zipfile.ZipFile(SRC)
X=lambda p: etree.fromstring(z.read(p))
def rels(part):
    d,b=posixpath.split(part); rp=f'{d}/_rels/{b}.rels'
    if rp not in z.namelist(): return {}
    return {r.get('Id'):posixpath.normpath(posixpath.join(d,r.get('Target'))) for r in X(rp).findall('rel:Relationship',NS)}
pres=X('ppt/presentation.xml'); prel=rels('ppt/presentation.xml')
sz=pres.find('p:sldSz',NS); W,H=int(sz.get('cx')),int(sz.get('cy'))
def color(el):
    if el is None: return None
    if el.find('a:noFill',NS) is not None: return None
    c=el.find('a:solidFill/a:srgbClr',NS)
    return '#'+c.get('val') if c is not None else None
# Map pptx media -> identical site image (by CRC of pixel data done at build time is overkill;
# the deck stores the source path in descr, otherwise we match by file name).
from PIL import Image, ImageChops
site_imgs={f:Image.open(os.path.join(SITE_IMAGES,f)).convert('RGB') for f in os.listdir(SITE_IMAGES) if f.endswith('.png')}
def site_image_for(media):
    im=Image.open(z.open(media)).convert('RGB')
    for f,s in site_imgs.items():
        if s.size==im.size and ImageChops.difference(s,im).getbbox() is None: return IMG_URL+f
    raise SystemExit(f'no identical site image for {media}')
def text(sp):
    tb=sp.find('p:txBody',NS)
    if tb is None: return None
    bp=tb.find('a:bodyPr',NS)
    ins=lambda k,d: int(bp.get(k,d))
    paras=[]
    for p in tb.findall('a:p',NS):
        ppr=p.find('a:pPr',NS)
        para={'algn':(ppr.get('algn') if ppr is not None else None) or 'l','runs':[]}
        ls=p.find('a:pPr/a:lnSpc/a:spcPct',NS); para['lnSpc']=int(ls.get('val'))/100000 if ls is not None else 1.0
        sa=p.find('a:pPr/a:spcAft/a:spcPts',NS); para['spcAft']=int(sa.get('val'))/100 if sa is not None else 0
        sb=p.find('a:pPr/a:spcBef/a:spcPts',NS); para['spcBef']=int(sb.get('val'))/100 if sb is not None else 0
        for r in p:
            tag=etree.QName(r).localname
            if tag=='r':
                rp=r.find('a:rPr',NS); t=r.findtext('a:t',default='',namespaces=NS)
                para['runs'].append({'t':t,'sz':int(rp.get('sz','1800'))/100,'b':rp.get('b')=='1','i':rp.get('i')=='1',
                    'color':color(rp) or '#000000'})
            elif tag=='br': para['runs'].append({'br':True})
        end=p.find('a:endParaRPr',NS)
        para['endSz']=int(end.get('sz'))/100 if end is not None and end.get('sz') else (para['runs'][0].get('sz',18) if para['runs'] else 18)
        paras.append(para)
    if not any(r.get('t') for p in paras for r in p['runs']): return None
    return {'anchor':bp.get('anchor','t'),'wrap':bp.get('wrap','square'),
            'ins':[ins('lIns',91440),ins('tIns',45720),ins('rIns',91440),ins('bIns',45720)],'paras':paras}
def shape(el,srels):
    tag=etree.QName(el).localname
    cnv=el.find('.//p:cNvPr',NS); sp_pr=el.find('p:spPr',NS)
    xf=sp_pr.find('a:xfrm',NS); off=xf.find('a:off',NS); ext=xf.find('a:ext',NS)
    s={'id':int(cnv.get('id')),'name':cnv.get('name'),'x':int(off.get('x')),'y':int(off.get('y')),'w':int(ext.get('cx')),'h':int(ext.get('cy'))}
    if xf.get('rot'): s['rot']=int(xf.get('rot'))/60000
    if xf.get('flipH')=='1': s['flipH']=True
    if xf.get('flipV')=='1': s['flipV']=True
    if tag=='pic':
        rid=el.find('.//a:blip',NS).get('{%s}embed'%NS['r'])
        s.update(kind='pic',src=site_image_for(srels[rid]),alt=cnv.get('descr') or '')
        if s['alt'].startswith('/'):   # a file path: L1_hello.png -> 'hello' (Level 1), L3_L1_bad_news.png -> 'bad news' (Level 3)
            stem=os.path.splitext(os.path.basename(s['alt']))[0]
            s['alt']=(re.sub(r'^L\d+_L\d+_','',stem) if LEVEL==3 else stem.split('_',1)[1]).replace('_',' ')
        return s
    g=sp_pr.find('a:prstGeom',NS); s['kind']='sp'; s['geom']=g.get('prst') if g is not None else 'rect'
    gd=sp_pr.find('a:prstGeom/a:avLst/a:gd',NS)
    if gd is not None: s['adj']=int(gd.get('fmla').split()[1])
    s['fill']=color(sp_pr)
    ln=sp_pr.find('a:ln',NS)
    if ln is not None and color(ln): s['line']={'color':color(ln),'w':int(ln.get('w','12700'))}
    t=text(el)
    if t: s['text']=t
    return s
def steps(sld):
    out=[]
    for ctn in sld.iterfind('.//p:timing//p:cTn[@nodeType]',NS):
        nt=ctn.get('nodeType')
        if nt not in ('clickEffect','withEffect','afterEffect'): continue
        assert ctn.get('presetClass')=='entr', 'only entrance effects are supported'
        ids=sorted({int(t.get('spid')) for t in ctn.iterfind('.//p:spTgt',NS)})
        filt={e.get('filter') for e in ctn.iterfind('.//p:animEffect',NS)}
        if nt=='clickEffect' or not out: out.append({'show':[],'effect':'fade' if 'fade' in filt else 'appear'})
        out[-1]['show']+= [i for i in ids if i not in out[-1]['show']]
    return out
slides=[]
for i,sid in enumerate(pres.find('p:sldIdLst',NS),1):
    part=prel[sid.get('{%s}id'%NS['r'])]; sld=X(part); srels=rels(part)
    bg=sld.find('p:cSld/p:bg/p:bgPr',NS)
    shapes=[shape(e,srels) for e in sld.find('p:cSld/p:spTree',NS) if etree.QName(e).localname in ('sp','pic')]
    notes=''
    for t in srels.values():
        if 'notesSlide' in t:
            nx=X(t)
            for sp in nx.iterfind('.//p:sp',NS):
                if sp.find('.//p:ph[@type="body"]',NS) is not None:
                    notes='\n'.join(''.join(r.text or '' for r in p.iterfind('.//a:t',NS)) for p in sp.iterfind('.//a:p',NS)).strip()
    st=steps(sld)
    ids={s['id'] for s in shapes}
    for k in st: assert set(k['show'])<=ids
    runs=[(r['sz'],-k,r['t']) for k,s in enumerate(shapes) if s.get('text') for p in s['text']['paras'] for r in p['runs'] if r.get('t','').strip()]
    best=max(runs)[0] if runs else 0
    title=' '.join(t for sz,_,t in sorted(runs,key=lambda r:-r[1]) if sz==best).strip()
    if len(title)<6 or not re.search('[A-Za-z]{2}',title):  # e.g. slide whose biggest text is a single word ('am')
        title=' '.join(t for sz,_,t in sorted(runs,key=lambda r:-r[1]) if sz==max(r[0] for r in runs if r[0]<best)).strip()
    multi=len({k for sz,k,_ in runs if sz==best})>1
    if LEVEL!=2 and multi:  # Level 1: biggest text is spread over several boxes (e.g. "What's" / "I'm" cards): use the top box with large text
        big=[(sh['y'],sh) for sh in shapes if sh.get('text') and any(r.get('sz',0)>=0.85*best and r.get('t','').strip() for p in sh['text']['paras'] for r in p['runs'])]
        sh=min(big,key=lambda t:t[0])[1]
        top_is_best=any(r.get('sz')==best for p in sh['text']['paras'] for r in p['runs'])   # stacked title boxes ("Classroom" / "Phrases"): keep
        t2='' if top_is_best else ' '.join(r['t'].strip() for p in sh['text']['paras'] for r in p['runs'] if r.get('sz',0)>=0.85*best and r.get('t','').strip())
        if len(t2)>=6 and re.search('[A-Za-z]{2}',t2): title=t2
    slides.append({'n':i,'file':part,'bg':color(bg) or '#FFFFFF','shapes':shapes,'steps':st,'notes':notes,'title':title})
os.makedirs(OUT_DIR,exist_ok=True)
json.dump({'level':LEVEL,'lesson':N,'width':W,'height':H,'source':os.path.basename(SRC),'slides':slides},
          open(os.path.join(OUT_DIR,f'lesson{N}.json'),'w'),ensure_ascii=False,indent=1)
print(len(slides),'slides;',sum(len(s['steps']) for s in slides),'reveal steps;',
      'steps per slide:',{s['n']:len(s['steps']) for s in slides if s['steps']})
chars=sorted({c for s in slides for sh in s['shapes'] if sh.get('text') for p in sh['text']['paras'] for r in p['runs'] for c in r.get('t','') if ord(c)>126})
print('non-ascii chars:',''.join(chars))
