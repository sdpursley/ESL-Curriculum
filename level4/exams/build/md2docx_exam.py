"""Markdown -> docx converter for Version 4 (readability layout).
Extra syntax:
  <!-- part: LABEL | Title | Subtitle | Footer text -->  new docx section + divider page
  <!-- mode: student|student-tight|teacher|guide -->                  font sizes / spacing
  <!-- subst --> before a pipe table                    two-sided substitution table
       cells: '‖' gap column, '^' merge with cell above, '<' merge with cell to the left,
       ' / ' inside a cell = stacked options
  :::step Title  ...  :::    boxed activity block (teacher)
  :::box Title   ...  :::    boxed info block
  ---                        page break
  ![alt](path) in table cells, '<br>' line breaks in cells
Level 1 addition (only change from the Level 2 md2docx.py):
  <!-- grid --> before a pipe table                     header-less grid of large centered text (alphabet, letter items)
Levels 3-5 exam changes (copy of level1/exams/build/md2docx_L1_exam.py; the same file is in level3/4/5 exams/build):
  student mode is smaller (12 pt body, 4 pt after a numbered item when an answer line follows) because these tests have
  reading texts; a line that starts with 3 spaces right after a numbered item is its answer-choice line (indented);
  '<br>' inside a paragraph is a line break.
Level 1 exam additions (copy of lesson13/build/md2docx_L1.py; nothing else changed):
  '^^text' as a segment in a picture-table cell          large bold answer-choice text (20 pt)
  student body text 14 pt (lessons: 13 pt)               bigger print for test pages
  numbered items in student mode: 13 pt space after       room between test items
  <!-- pagebreak -->                                     forced page break
  ![alt w=3.6](path)                                     picture width in inches (default: lesson rule)
"""
import re, sys, os
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_BREAK, WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

NAVY=RGBColor(0x1F,0x3A,0x5F); TEAL=RGBColor(0x1B,0x6F,0x7A); GREY=RGBColor(0x55,0x55,0x55)
WHITE=RGBColor(0xFF,0xFF,0xFF); STAR=RGBColor(0xC0,0x7A,0x00)
W=6.7
MODES={'guide':dict(body=11,table=9.5,after=7,line=1.2),
       'teacher':dict(body=11.5,table=10.5,after=7,line=1.2),
       'student':dict(body=11.5,table=11,after=5,line=1.15),
       'student-tight':dict(body=11.5,table=11,after=3,line=1.1)}   # Levels 4-5: longer readings on the same 4 pages
mode='guide'
def M(k): return MODES[mode][k]

SRC,DST,FOOT=sys.argv[1],sys.argv[2],sys.argv[3]
BASE=os.path.dirname(os.path.abspath(SRC))
doc=Document()
for s in doc.styles:
    pass
st=doc.styles['Normal']; st.font.name='Calibri'; st.font.size=Pt(11)
st.element.rPr.rFonts.set(qn('w:eastAsia'),'Calibri')
def setup_section(sec):
    sec.left_margin=sec.right_margin=Inches(0.9); sec.top_margin=Inches(0.85); sec.bottom_margin=Inches(0.8)
setup_section(doc.sections[0])

def set_footer(sec,text):
    sec.footer.is_linked_to_previous=False
    fp=sec.footer.paragraphs[0]; fp.text=''
    for r in list(fp.runs): r._r.getparent().remove(r._r)
    r=fp.add_run(text+'   |   page '); 
    r2=fp.add_run(); f1=OxmlElement('w:fldChar'); f1.set(qn('w:fldCharType'),'begin'); it=OxmlElement('w:instrText'); it.text='PAGE'; f2=OxmlElement('w:fldChar'); f2.set(qn('w:fldCharType'),'end')
    r2._r.append(f1); r2._r.append(it); r2._r.append(f2)
    for x in fp.runs: x.font.size=Pt(8.5); x.font.color.rgb=GREY
set_footer(doc.sections[0],FOOT)

def shade(el,color):
    tcPr=el.get_or_add_tcPr() if hasattr(el,'get_or_add_tcPr') else el.get_or_add_pPr()
    s=OxmlElement('w:shd'); s.set(qn('w:val'),'clear'); s.set(qn('w:color'),'auto'); s.set(qn('w:fill'),color); tcPr.append(s)
def cell_borders(tc,color='8FA3B8',sz='8',sides=('top','left','bottom','right'),val='single'):
    tcPr=tc.get_or_add_tcPr(); b=OxmlElement('w:tcBorders')
    for side in ('top','left','bottom','right'):
        e=OxmlElement('w:'+side)
        if side in sides: e.set(qn('w:val'),val); e.set(qn('w:sz'),sz); e.set(qn('w:color'),color)
        else: e.set(qn('w:val'),'nil')
        b.append(e)
    tcPr.append(b)
def tbl_margins(t,top=60,side=100):
    tblPr=t._tbl.tblPr; m=OxmlElement('w:tblCellMar')
    for s,v in (('top',top),('left',side),('bottom',top),('right',side)):
        e=OxmlElement('w:'+s); e.set(qn('w:w'),str(v)); e.set(qn('w:type'),'dxa'); m.append(e)
    tblPr.append(m)
def no_split(row):
    trPr=row._tr.get_or_add_trPr(); trPr.append(OxmlElement('w:cantSplit'))
def repeat_header(row):
    trPr=row._tr.get_or_add_trPr(); trPr.append(OxmlElement('w:tblHeader'))
def set_widths(t,widths):
    for ci,col in enumerate(t.columns): col.width=widths[ci]
    for ci,gc in enumerate(t._tbl.tblGrid.findall(qn('w:gridCol'))): gc.set(qn('w:w'),str(int(widths[ci].inches*1440)))
    for row in t.rows:
        for ci,c in enumerate(row.cells):
            if ci<len(widths): c.width=widths[ci]
def keep_table(t):
    rows=t.rows
    for ri,row in enumerate(rows):
        if ri==len(rows)-1: break
        for c in row.cells:
            for p in c.paragraphs: p.paragraph_format.keep_with_next=True
def pfmt(p,after=None,before=0,line=None,keep=False):
    f=p.paragraph_format; f.space_after=Pt(M('after') if after is None else after); f.space_before=Pt(before)
    f.line_spacing=line or M('line'); 
    if keep: f.keep_with_next=True

def star_run(p,size,bold):
    rs=p.add_run('★'); rs.bold=bold; rs.font.color.rgb=STAR
    if size: rs.font.size=Pt(size)
    rf=rs._element.get_or_add_rPr().get_or_add_rFonts()
    for a in ('w:ascii','w:hAnsi','w:cs','w:eastAsia'): rf.set(qn(a),'DejaVu Sans')

def inline(p,text,size=None,bold_all=False,color=None):
    bold=False; ital=False; code=False; i=0; buf=''
    def flush():
        nonlocal buf
        if not buf: return
        parts=buf.split('★')
        for k,pt in enumerate(parts):
            if k>0: star_run(p,size,bold or bold_all)
            if pt:
                r=p.add_run(pt); r.bold=bold or bold_all; r.italic=ital
                if code: r.font.name='Consolas'; r.font.color.rgb=RGBColor(0x8B,0x1A,0x1A)
                elif color: r.font.color.rgb=color
                if size: r.font.size=Pt(size)
        buf=''
    while i<len(text):
        if text[i]=='`': flush(); code=not code; i+=1
        elif code: buf+=text[i]; i+=1
        elif text.startswith('<br>',i): flush(); p.add_run().add_break(); i+=4
        elif text.startswith('**',i): flush(); bold=not bold; i+=2
        elif text[i]=='*' and not (i+1<len(text) and text[i+1]==' ' and not ital): flush(); ital=not ital; i+=1
        else: buf+=text[i]; i+=1
    flush()

IMG_RE=re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
def gap_para(after=6):
    p=doc.add_paragraph(); f=p.paragraph_format; f.space_after=Pt(after); f.space_before=Pt(0); f.line_spacing=1.0
    r=p.add_run(); r.font.size=Pt(4)

def parse_rows(rows):
    rows=[r for r in rows if not re.match(r'^\|\s*:?-{2,}',r)]
    return [[c.strip() for c in r.strip().strip('|').split('|')] for r in rows]

def add_table(rows):
    cells=parse_rows(rows); n=max(len(c) for c in cells)
    if any(('![' in c) or ('^^' in c) for r in cells for c in r): return add_pic_table(cells,n)
    t=doc.add_table(rows=len(cells),cols=n); t.style='Table Grid'; t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=False
    tbl_margins(t)
    fs=M('table') - (0.5 if (n>=5 and mode=='guide') else 0)
    head=cells[0][0].lower()
    wts=[]
    for ci in range(n):
        lens=[len(re.sub(r'[*]','',r[ci])) if ci<len(r) else 0 for r in cells]
        wts.append(max(10,min(60,(sum(lens)/len(lens))*0.6+max(lens)*0.4)))
    fixed={}
    if head in ('time','clock time'): fixed[0]=1.15
    for ci in range(n):
        if cells[0][ci].lower() in ('min','minutes'): fixed[ci]=0.55
    rem=W-sum(fixed.values()); tot=sum(w for ci,w in enumerate(wts) if ci not in fixed)
    widths=[Inches(fixed[ci]) if ci in fixed else Inches(rem*wts[ci]/tot) for ci in range(n)]
    set_widths(t,widths)
    for ri,row in enumerate(cells):
        no_split(t.rows[ri])
        if ri==0: repeat_header(t.rows[0])
        for ci in range(n):
            c=t.cell(ri,ci); txt=row[ci] if ci<len(row) else ''
            c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            p=c.paragraphs[0]; pfmt(p,after=0,line=1.1)
            segs=txt.split('<br>')
            for k,seg in enumerate(segs):
                inline(p,seg.strip(),size=fs,bold_all=(ri==0),color=WHITE if ri==0 else None)
                if k<len(segs)-1: p.add_run().add_break()
            if ri==0: shade(c._tc,'1F3A5F')
            elif ri%2==0: shade(c._tc,'EEF4F7')
    if len(cells)<=14: keep_table(t)
    gap_para(10)

def add_pic_table(cells,n):
    if all(not c for c in cells[0]): cells=cells[1:]
    t=doc.add_table(rows=len(cells),cols=n); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=False
    tbl_margins(t,top=80,side=60)
    w=Inches(W/n); set_widths(t,[w]*n)
    for ri,row in enumerate(cells):
        no_split(t.rows[ri])
        for ci in range(n):
            c=t.cell(ri,ci); txt=row[ci] if ci<len(row) else ''
            cell_borders(c._tc,color='C9D3DD',sz='6')
            p=c.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.CENTER; pfmt(p,after=4,before=4,line=1.05)
            segs=[x.strip() for x in txt.split('<br>')]
            for k,seg in enumerate(segs):
                m=IMG_RE.fullmatch(seg)
                if m:
                    wm=re.search(r' w=([\d.]+)$',m.group(1))
                    wd=float(wm.group(1)) if wm else (min(1.75,W/n-0.3) if n>1 else min(5.4,W-0.4))
                    p.add_run().add_picture(os.path.join(BASE,m.group(2)),width=Inches(wd))
                elif seg.startswith('^^'): inline(p,seg[2:],size=20,bold_all=True,color=NAVY)
                elif seg: inline(p,seg,size=13.5 if mode.startswith('student') else 11)
                if k<len(segs)-1: p.add_run().add_break()
    gap_para(10)

def add_subst(rows):
    cells=parse_rows(rows); n=max(len(c) for c in cells)
    for r in cells:
        while len(r)<n: r.append('')
    g=cells[0].index('‖')
    t=doc.add_table(rows=len(cells),cols=n); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=False
    tbl_margins(t,top=70,side=110)
    fs=12.5 if mode.startswith('student') else 11
    cw=0.0085*fs   # inches per character (approx.)
    need=[]; minw=[]
    for ci in range(n):
        if ci==g: need.append(0); minw.append(0); continue
        opts=[re.sub(r'[*]','',o) for r in cells[1:] for o in r[ci].split(' / ') if r[ci] not in ('^','<','')]
        longest=max([len(o) for o in opts] or [3]); word=max([len(w) for o in opts for w in o.split()] or [3])
        need.append(longest*cw+0.3); minw.append(word*cw+0.3)
    gapw=0.22; avail=W-gapw; tot=sum(need)
    if tot<=avail:
        extra=avail-tot; ws=[x+extra*x/tot for x in need]
    else:
        ws=list(minw); rest=avail-sum(minw); slack=[need[k]-minw[k] for k in range(n)]; st=sum(slack) or 1
        ws=[minw[k]+max(0,rest)*slack[k]/st for k in range(n)]
    widths=[Inches(gapw) if ci==g else Inches(ws[ci]) for ci in range(n)]
    set_widths(t,widths)
    for ri,row in enumerate(cells):
        no_split(t.rows[ri])
        for ci in range(n):
            c=t.cell(ri,ci); txt=row[ci]
            if ci==g:
                cell_borders(c._tc,sides=()); continue
            left=ci<g
            if ri==0:
                shade(c._tc,'1F3A5F' if left else '1B6F7A'); cell_borders(c._tc,color='FFFFFF',sz='4')
            else:
                shade(c._tc,'EAF1F8' if left else 'E8F4EC'); cell_borders(c._tc,color='7A8CA0',sz='8')
            c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            if txt in ('^','<'): continue
            opts=[txt] if ri==0 else txt.split(' / ')
            p=c.paragraphs[0]
            for k,o in enumerate(opts):
                if k>0: p=c.add_paragraph()
                pfmt(p,after=1,before=1,line=1.05)
                if ri==0:
                    p.alignment=WD_ALIGN_PARAGRAPH.CENTER; inline(p,o,size=10.5,bold_all=True,color=WHITE)
                else: inline(p,o,size=fs)
    # merges: horizontal then vertical
    for ri,row in enumerate(cells):
        ci=0
        while ci<n:
            if row[ci]=='<':
                o=ci-1
                while row[o]=='<': o-=1
                e=ci
                while e+1<n and row[e+1]=='<': e+=1
                t.cell(ri,o).merge(t.cell(ri,e)); ci=e+1
            else: ci+=1
    for ci in range(n):
        for ri in range(1,len(cells)):
            if cells[ri][ci]=='^':
                o=ri-1
                while cells[o][ci]=='^': o-=1
                t.cell(o,ci).merge(t.cell(ri,ci))
    keep_table(t)
    gap_para(12)

def add_grid(rows):
    cells=parse_rows(rows); n=max(len(c) for c in cells)
    if all(not c for c in cells[0]): cells=cells[1:]
    t=doc.add_table(rows=len(cells),cols=n); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=False
    tbl_margins(t,top=70,side=60); set_widths(t,[Inches(W/n)]*n)
    for ri,row in enumerate(cells):
        no_split(t.rows[ri])
        for ci in range(n):
            c=t.cell(ri,ci); txt=row[ci] if ci<len(row) else ''
            cell_borders(c._tc,color='C9D3DD',sz='6'); c.vertical_alignment=WD_CELL_VERTICAL_ALIGNMENT.CENTER
            if txt: shade(c._tc,'F4F8FB')
            p=c.paragraphs[0]; p.alignment=WD_ALIGN_PARAGRAPH.CENTER; pfmt(p,after=2,before=2,line=1.0)
            segs=txt.split('<br>')
            for k,seg in enumerate(segs):
                inline(p,seg.strip(),size=22 if k==0 else 11,color=NAVY if k==0 else GREY)
                if k<len(segs)-1: p.add_run().add_break()
    keep_table(t); gap_para(12)

def add_box(kind,title,body):
    t=doc.add_table(rows=2,cols=1); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=False
    tbl_margins(t,top=90,side=150); set_widths(t,[Inches(W)])
    h=t.cell(0,0); b=t.cell(1,0)
    color='1B6F7A' if kind=='step' else '1F3A5F'
    if 'NEVER SKIP' in title: color='9A3412'
    if title.startswith('If time'): color='5B6B7A'
    if title.startswith('Break'): color='8A97A6'
    shade(h._tc,color); cell_borders(h._tc,color=color,sz='8')
    shade(b._tc,'F7FAFB'); cell_borders(b._tc,color=color,sz='8')
    p=h.paragraphs[0]; pfmt(p,after=0,line=1.0,keep=True); inline(p,title,size=12 if not mode.startswith('student') else 13,bold_all=True,color=WHITE)
    no_split(t.rows[0]); no_split(t.rows[1]); keep_table(t)
    first=True
    for line in body:
        if not line.strip(): continue
        p=b.paragraphs[0] if first else b.add_paragraph(); first=False
        m=re.match(r'^- (.*)',line)
        if m:
            pfmt(p,after=4,line=1.15); p.paragraph_format.left_indent=Inches(0.22); p.paragraph_format.first_line_indent=Inches(-0.18)
            r=p.add_run('•  '); r.font.color.rgb=TEAL; r.bold=True; r.font.size=Pt(M('body'))
            inline(p,m.group(1),size=M('body'))
        else:
            pfmt(p,after=4,line=1.15); inline(p,line,size=M('body'))
    gap_para(12)

def part_page(label,title,sub,foot):
    global last_break,pending_break
    pending_break=False
    sec=doc.add_section(WD_SECTION.NEW_PAGE); setup_section(sec); set_footer(sec,foot)
    p=doc.add_paragraph(); pfmt(p,before=180,after=6); r=p.add_run(label.upper()); r.bold=True; r.font.size=Pt(16); r.font.color.rgb=TEAL
    p=doc.add_paragraph(); pfmt(p,after=14,line=1.0); r=p.add_run(title); r.bold=True; r.font.size=Pt(34); r.font.color.rgb=NAVY
    bar=doc.add_paragraph(); pPr=bar._p.get_or_add_pPr(); bd=OxmlElement('w:pBdr'); bt=OxmlElement('w:bottom')
    bt.set(qn('w:val'),'single'); bt.set(qn('w:sz'),'24'); bt.set(qn('w:space'),'1'); bt.set(qn('w:color'),'1B6F7A'); bd.append(bt); pPr.append(bd)
    for s in sub.split(' ;; '):
        p=doc.add_paragraph(); pfmt(p,before=10,after=4); inline(p,s,size=14,color=GREY)
    doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE); last_break=True

def flush_break(p=None):
    global pending_break
    if not pending_break: return
    if p is None: doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)
    else: p.paragraph_format.page_break_before=True
    pending_break=False
def heading(lvl,txt):
    global last_break
    p=doc.add_paragraph(); flush_break(p)
    sizes={1:26,2:20,3:15,4:13}; 
    if mode.startswith('student'): sizes={1:24,2:18,3:13.5,4:12.5}
    col=NAVY if lvl<=2 else TEAL
    pfmt(p,before=(0 if last_break else {1:6,2:18,3:16,4:12}[lvl]),after={1:10,2:10,3:6,4:4}[lvl],line=1.05,keep=True)
    inline(p,txt,size=sizes[lvl],bold_all=(lvl!=2 or True),color=col)
    if lvl==2:
        pPr=p._p.get_or_add_pPr(); bd=OxmlElement('w:pBdr'); bt=OxmlElement('w:bottom')
        bt.set(qn('w:val'),'single'); bt.set(qn('w:sz'),'10'); bt.set(qn('w:space'),'4'); bt.set(qn('w:color'),'1B6F7A'); bd.append(bt); pPr.append(bd)
    last_break=False

lines=open(SRC).read().split('\n')
i=0; last_break=True; subst_next=False; first_h1=True; pending_break=False
while i<len(lines):
    L=lines[i]
    if not L.strip(): i+=1; continue
    if L.strip()=='<!-- pagebreak -->':
        pending_break=True; last_break=True; i+=1; continue   # becomes page-break-before on the next paragraph (no blank page when a page is exactly full)
    m=re.match(r'<!--\s*(part|mode|subst|grid)\s*:?\s*(.*?)\s*-->',L.strip())
    if m:
        k,v=m.group(1),m.group(2)
        if k=='mode': mode=v.strip()
        elif k=='subst': subst_next=True
        elif k=='grid': subst_next='grid'
        elif k=='part':
            parts=[x.strip() for x in v.split('|')]; part_page(*parts)
        i+=1; continue
    if L.startswith(':::'):
        flush_break()
        mm=re.match(r'^:::(step|box)\s+(.*)',L); body=[]; i+=1
        while i<len(lines) and lines[i].strip()!=':::': body.append(lines[i]); i+=1
        i+=1; add_box(mm.group(1),mm.group(2),body); last_break=False; continue
    if L.startswith('|'):
        flush_break()
        rows=[]
        while i<len(lines) and lines[i].startswith('|'): rows.append(lines[i]); i+=1
        if subst_next=='grid': add_grid(rows); subst_next=False
        elif subst_next: add_subst(rows); subst_next=False
        else: add_table(rows)
        last_break=False; continue
    if L.strip()=='---':
        if not last_break: pending_break=True
        last_break=True; i+=1; continue
    m=re.match(r'^(#{1,4}) (.*)',L)
    if m: heading(len(m.group(1)),m.group(2)); i+=1; continue
    if L.startswith('>'):
        flush_break()
        grp=[]
        while i<len(lines) and lines[i].startswith('>'): grp.append(lines[i][1:].strip()); i+=1
        t=doc.add_table(rows=1,cols=1); t.alignment=WD_TABLE_ALIGNMENT.CENTER; t.autofit=False; tbl_margins(t,top=90,side=150); set_widths(t,[Inches(W)])
        c=t.cell(0,0); shade(c._tc,'EAF4F4'); cell_borders(c._tc,color='1B6F7A',sz='24',sides=('left',))
        for k,g in enumerate(grp):
            p=c.paragraphs[0] if k==0 else c.add_paragraph(); pfmt(p,after=2,line=1.15); inline(p,g,size=M('body')-0.5)
        gap_para(10); last_break=False; continue
    m=re.match(r'^(\s*)- (.*)',L)
    if m:
        p=doc.add_paragraph(); flush_break(p); pfmt(p,after=4); ind=0.3 if not m.group(1) else 0.6
        p.paragraph_format.left_indent=Inches(ind); p.paragraph_format.first_line_indent=Inches(-0.2)
        r=p.add_run('•  '); r.bold=True; r.font.color.rgb=TEAL; r.font.size=Pt(M('body'))
        inline(p,m.group(2),size=M('body')); i+=1; last_break=False; continue
    m=re.match(r'^(\d+)\. (.*)',L)
    if m:
        opt_next=i+1<len(lines) and lines[i+1].startswith('   ') and lines[i+1].strip()
        p=doc.add_paragraph(); flush_break(p); pfmt(p,after=(2 if opt_next else ({'student':7,'student-tight':5}.get(mode,5))),keep=bool(opt_next)); p.paragraph_format.left_indent=Inches(0.35); p.paragraph_format.first_line_indent=Inches(-0.28)
        r=p.add_run(m.group(1)+'.  '); r.bold=True; r.font.size=Pt(M('body')); r.font.color.rgb=TEAL; inline(p,m.group(2),size=M('body')); i+=1; last_break=False; continue
    if L.startswith('   ') and L.strip():
        p=doc.add_paragraph(); flush_break(p); pfmt(p,after=({'student':5,'student-tight':3}.get(mode,6))); p.paragraph_format.left_indent=Inches(0.35)
        inline(p,L.strip(),size=M('body')); i+=1; last_break=False; continue
    p=doc.add_paragraph(); flush_break(p); pfmt(p); 
    if L.startswith('**Q:'): p.paragraph_format.keep_with_next=True; p.paragraph_format.space_after=Pt(3)
    inline(p,L,size=M('body')); i+=1; last_break=False

doc.save(DST); print('ok')
