"""Markdown -> HTML helpers used by scripts/export_content.py (taken from the earlier static-site builder).
The functions read the global list L (the Markdown lines); export_content.py sets it before use."""
import re, html, os
L = []   # filled in by export_content.py
def find(prefix,start=0):
    for i in range(start,len(L)):
        if L[i].startswith(prefix): return i
    raise KeyError(prefix)
def sect(a,b,start=0):
    i=find(a,start); j=find(b,i+1) if b else len(L); return L[i+1:j], j
used_imgs=set()
def inline(t):
    t=html.escape(t,quote=False).replace('&lt;br&gt;','<br>')
    def img(m):
        p=m.group(2); used_imgs.add(os.path.basename(p))
        return f'<img src="images/{os.path.basename(p)}" alt="{m.group(1)}" width="300" height="210" loading="lazy">'
    t=re.sub(r'!\[([^\]]*)\]\(([^)]+)\)',img,t)
    t=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',t)
    t=re.sub(r'`([^`]+)`',r'<code>\1</code>',t)
    t=re.sub(r'\*\*([^*]+)\*([^*]+)\*\*\*',r'<strong>\1<em>\2</em></strong>',t)
    t=re.sub(r'\*\*\*([^*]+)\*(?!\*)',r'**<em>\1</em>',t)
    prev=None
    while prev!=t:
        prev=t
        t=re.sub(r'\*\*([^*]+?)\*\*',r'<strong>\1</strong>',t)
        t=re.sub(r'(?<!\*)\*([^*\s](?:[^*]*?[^*\s])?)\*(?!\*\w)',r'<em>\1</em>',t)
    t=re.sub(r'(?<!["=>])(https?://[^\s<)]+)',r'<a href="\1">\1</a>',t)
    return t
def cells(row): return [c.strip() for c in row.strip().strip('|').split('|')]
def table(rows,cls=''):
    hdr=cells(rows[0]); body=[cells(r) for r in rows[2:]]
    if '‖' in hdr:  # two-sided grammar box
        k=hdr.index('‖')
        def grid(side):
            n=len(side[0]); out=[]
            # rowspan calc
            spans=[[1]*n for _ in side]; skip=[[False]*n for _ in side]
            for c in range(n):
                for r in range(len(side)):
                    if side[r][c]=='^':
                        skip[r][c]=True
                        rr=r-1
                        while skip[rr][c]: rr-=1
                        spans[rr][c]+=1
            for r,row in enumerate(side):
                tds=[]
                for c,v in enumerate(row):
                    if skip[r][c] or v=='<': continue
                    cs=1
                    while c+cs<n and row[c+cs]=='<': cs+=1
                    rs=(f' rowspan="{spans[r][c]}"' if spans[r][c]>1 else '')+(f' colspan="{cs}"' if cs>1 else '')
                    tds.append(f'<td{rs}>{inline(v)}</td>')
                out.append('<tr>'+''.join(tds)+'</tr>')
            return '\n'.join(out)
        q=[r[:k] for r in body]; a=[r[k+1:] for r in body]
        return (f'<div class="gbox"><div class="gside q"><div class="glabel">{inline(hdr[0])}</div><table>{grid(q)}</table></div>'
                f'<div class="garrow" aria-hidden="true">→</div>'
                f'<div class="gside a"><div class="glabel">{inline(hdr[k+1])}</div><table>{grid(a)}</table></div></div>')
    vocab=all(not h for h in hdr) and '<img' in inline(rows[2])
    if vocab:
        items=[c for r in body for c in r if c]
        out=[]
        for c in items:
            m=re.match(r'(!\[[^\]]*\]\([^)]+\))<br>(.*)',c)
            out.append(f'<figure class="word">{inline(m.group(1))}<figcaption>{inline(m.group(2))}</figcaption></figure>')
        return '<div class="words">'+'\n'.join(out)+'</div>'
    th=''.join(f'<th scope="col">{inline(h)}</th>' for h in hdr)
    trs=''.join('<tr>'+''.join(f'<td>{inline(v)}</td>' for v in r)+'</tr>\n' for r in body)
    return f'<div class="tablewrap"><table><thead><tr>{th}</tr></thead><tbody>\n{trs}</tbody></table></div>'
def md(lines,shift=0):
    out=[]; i=0; n=len(lines)
    while i<n:
        s=lines[i]; st=s.strip()
        if not st or st.startswith('<!--') or st=='---' or re.fullmatch(r'_+',st) and False: i+=1; continue
        if re.fullmatch(r'_{10,}',st):
            out.append('<div class="writeline"></div>'); i+=1; continue
        m=re.match(r'(#{1,6}) (.*)',s)
        if m:
            lv=min(6,len(m.group(1))+shift); out.append(f'<h{lv}>{inline(m.group(2))}</h{lv}>'); i+=1; continue
        m=re.match(r':::(box|step) ?(.*)',st)
        if m:
            j=i+1
            while lines[j].strip()!=':::': j+=1
            kind,title=m.groups()
            out.append(f'<section class="{kind}"><h4>{inline(title)}</h4>{md(lines[i+1:j])}</section>'); i=j+1; continue
        if st.startswith('|'):
            j=i
            while j<n and lines[j].strip().startswith('|'): j+=1
            out.append(table(lines[i:j])); i=j; continue
        if st.startswith('>'):
            j=i; q=[]
            while j<n and lines[j].strip().startswith('>'): q.append(lines[j].strip()[1:].strip()); j+=1
            cls='note'
            if 'hispanohablantes' in q[0]: cls='note es'
            if q[0].startswith('**Narrator') or re.match(r'\*\*\w+:\*\*',q[0]):
                out.append('<div class="script">'+''.join(f'<p>{inline(x)}</p>' for x in q)+'</div>')
            else:
                attr=' lang="es"' if cls=='note es' else ''
                out.append(f'<aside class="{cls}"{attr}>'+''.join(f'<p>{inline(x)}</p>' for x in q)+'</aside>')
            i=j; continue
        if re.match(r'(- |\d+\. )',st):
            ordered=bool(re.match(r'\d+\.',st)); tag='ol' if ordered else 'ul'
            j=i; items=[]
            while j<n and re.match(r'(- |\d+\. )',lines[j].strip()):
                items.append(re.sub(r'^(- |\d+\. )','',lines[j].strip())); j+=1
            out.append(f'<{tag}>'+''.join(f'<li>{inline(x)}</li>' for x in items)+f'</{tag}>'); i=j; continue
        j=i; p=[]
        while j<n and lines[j].strip() and not re.match(r'(#|\||>|- |\d+\. |:::|---|<!--)',lines[j].strip()):
            p.append(lines[j].strip()); j+=1
        if not p: p=[st]; j=i+1
        out.append(f'<p>{inline(" ".join(p))}</p>'); i=j
    return '\n'.join(out)

