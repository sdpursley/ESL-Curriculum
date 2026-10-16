import { CSSProperties } from 'react'
import type { Shape, Slide, TextBody } from './types'

/** 1 logical px = 9525 EMU (96 dpi), so a 16:9 deck is 1280 x 720 px. */
export const EMU = 9525
const px = (emu: number) => emu / EMU
const PT = 96 / 72
/** Lexend Deca's natural line height (hhea ascent+descent / unitsPerEm). */
const LINE = 1.25

function starPoints(n: number, w: number, h: number, inner: number, hf = 1) {
  const pts: string[] = []
  const rx = (w / 2) * hf, ry = h / 2, cx = w / 2, cy = h / 2
  for (let i = 0; i < n * 2; i++) {
    const a = -Math.PI / 2 + (i * Math.PI) / n
    const r = i % 2 === 0 ? 1 : inner
    pts.push(`${cx + Math.cos(a) * rx * r},${cy + Math.sin(a) * ry * r}`)
  }
  return pts.join(' ')
}

/** SVG outline for the preset geometries used by the decks (OOXML presetShapeDefinitions). */
function Geometry({ s }: { s: Shape }) {
  const w = px(s.w), h = px(s.h), ss = Math.min(w, h)
  const fill = s.fill ?? 'none'
  const stroke = s.line ? { stroke: s.line.color, strokeWidth: px(s.line.w) } : {}
  const p = { fill, ...stroke }
  switch (s.geom) {
    case 'roundRect': { const r = ss * (s.adj ?? 16667) / 100000; return <rect width={w} height={h} rx={r} ry={r} {...p} /> }
    case 'round1Rect': { // only the top-right corner is rounded
      const r = ss * (s.adj ?? 16667) / 100000
      return <path d={`M0,0 H${w - r} A${r},${r} 0 0 1 ${w},${r} V${h} H0 Z`} {...p} /> }
    case 'ellipse': return <ellipse cx={w / 2} cy={h / 2} rx={w / 2} ry={h / 2} {...p} />
    case 'triangle': return <polygon points={`${w / 2},0 ${w},${h} 0,${h}`} {...p} />
    case 'line': return <line x1={0} y1={0} x2={w} y2={h} {...stroke} />
    case 'star10': return <polygon points={starPoints(10, w, h, (s.adj ?? 42533) / 50000, 1.05146)} {...p} />
    case 'star32': return <polygon points={starPoints(32, w, h, (s.adj ?? 37500) / 50000)} {...p} />
    case 'mathPlus': {
      const a = s.adj ?? 23520, dx1 = (w * 73490) / 200000, dy1 = (h * 73490) / 200000, d = (ss * a) / 200000
      const cx = w / 2, cy = h / 2
      const pts = [[cx - d, cy - dy1], [cx + d, cy - dy1], [cx + d, cy - d], [cx + dx1, cy - d], [cx + dx1, cy + d], [cx + d, cy + d],
        [cx + d, cy + dy1], [cx - d, cy + dy1], [cx - d, cy + d], [cx - dx1, cy + d], [cx - dx1, cy - d], [cx - d, cy - d]]
      return <polygon points={pts.map(q => q.join(',')).join(' ')} {...p} /> }
    default: return <rect width={w} height={h} {...p} />
  }
}

/** Text rectangle inset defined by the preset geometry (OOXML presetShapeDefinitions), in px: [l, t, r, b]. */
function geomTextInset(s: Shape): [number, number, number, number] {
  const w = px(s.w), h = px(s.h), ss = Math.min(w, h)
  if (s.geom === 'roundRect') { const d = ss * (s.adj ?? 16667) / 100000 * 0.29289; return [d, d, d, d] }
  if (s.geom === 'round1Rect') { const d = ss * (s.adj ?? 16667) / 100000 * 0.29289; return [0, d, d, 0] }
  if (s.geom === 'ellipse') { const dx = (w / 2) * (1 - Math.SQRT1_2), dy = (h / 2) * (1 - Math.SQRT1_2); return [dx, dy, dx, dy] }
  return [0, 0, 0, 0]
}

function Text({ t, g }: { t: TextBody; g: [number, number, number, number] }) {
  const [l, tp, r, b] = t.ins.map((v, i) => px(v) + g[i])
  const justify = t.anchor === 'ctr' ? 'center' : t.anchor === 'b' ? 'flex-end' : 'flex-start'
  return (
    <div className="pz-text" style={{ padding: `${tp}px ${r}px ${b}px ${l}px`, justifyContent: justify,
      whiteSpace: t.wrap === 'none' ? 'nowrap' : 'pre-wrap' }}>
      {t.paras.map((p, i) => (
        <p key={i} style={{ textAlign: p.algn === 'ctr' ? 'center' : p.algn === 'r' ? 'right' : p.algn === 'just' ? 'justify' : 'left',
          lineHeight: LINE * p.lnSpc, marginTop: p.spcBef * PT, marginBottom: p.spcAft * PT,
          fontSize: p.runs.length ? undefined : p.endSz * PT, minHeight: p.runs.some(r => r.t) ? undefined : `${p.endSz * PT * LINE * p.lnSpc}px` }}>
          {p.runs.map((r, j) => r.br ? <br key={j} /> :
            <span key={j} style={{ fontSize: (r.sz ?? 18) * PT, fontWeight: r.b ? 700 : 400, fontStyle: r.i ? 'italic' : undefined, color: r.color }}>{r.t}</span>)}
        </p>))}
    </div>)
}

export function ShapeView({ s, hidden, animate }: { s: Shape; hidden: boolean; animate: boolean }) {
  const style: CSSProperties = { left: px(s.x), top: px(s.y), width: Math.max(px(s.w), 0.01), height: Math.max(px(s.h), 0.01),
    transform: s.rot ? `rotate(${s.rot}deg)` : undefined }
  const cls = `pz-shape ${hidden ? 'pz-hidden' : ''} ${animate && !hidden ? 'pz-fade' : ''}`
  if (s.kind === 'pic') return (
    <div className={cls} style={style} data-name={s.name}>
      <img src={s.src} alt={s.alt} draggable={false} className="pz-card" />
    </div>)
  const flip = s.flipH || s.flipV ? `scale(${s.flipH ? -1 : 1},${s.flipV ? -1 : 1})` : undefined
  return (
    <div className={cls} style={style} data-name={s.name} aria-hidden={s.text ? undefined : true}>
      <svg width="100%" height="100%" viewBox={`0 0 ${px(s.w) || 0.01} ${px(s.h) || 0.01}`} preserveAspectRatio="none"
        style={{ transform: flip, transformOrigin: 'center' }} overflow="visible" aria-hidden="true"><Geometry s={s} /></svg>
      {s.text && <Text t={s.text} g={geomTextInset(s)} />}
    </div>)
}

/** Renders a slide at its native 1280x720 size; the caller scales it. */
export function SlideView({ slide, step, animateFrom, width, height }:
  { slide: Slide; step: number; animateFrom: number; width: number; height: number }) {
  // shapes that appear on a later click than `step` are hidden
  const revealAt = new Map<number, number>()
  slide.steps.forEach((st, k) => st.show.forEach(id => { if (!revealAt.has(id)) revealAt.set(id, k + 1) }))
  return (
    <div className="pz-slide" style={{ width: px(width), height: px(height), background: slide.bg }}>
      {slide.shapes.map(s => {
        const at = revealAt.get(s.id) ?? 0
        return <ShapeView key={s.id} s={s} hidden={at > step} animate={at > animateFrom && at <= step} />
      })}
    </div>)
}
