import { useCallback, useEffect, useLayoutEffect, useRef, useState } from 'react'
import { Link, useParams, useSearchParams } from 'react-router-dom'
import { ChevronLeft, ChevronRight, Maximize, Minimize, StickyNote, LayoutGrid, X, Download } from 'lucide-react'
import { hasDeck, loadDeck, type Level } from './decks'
import type { Deck } from './types'
import { SlideView, EMU } from './SlideView'
import { SLIDES_AVAILABLE, slidePath } from '../config'
import level1 from '../content_level1.json'
import './presenter.css'

/** Level 1: the "Download PowerPoint" link appears when the lesson's .pptx was exported (src/content_level1.json). */
const level1Pptx = (n: number) => (level1.lessons as { n: number; slides?: string }[]).find(l => l.n === n)?.slides || ''

export default function PresenterRoute({ level = 2 }: { level?: Level }) {
  const { n } = useParams()
  const num = Number(n)
  const [deck, setDeck] = useState<Deck | null | undefined>(undefined)
  useEffect(() => {
    let live = true
    if (!hasDeck(num, level)) { setDeck(null); return }
    loadDeck(num, level).then(d => { if (live) setDeck(d) }, () => { if (live) setDeck(null) })
    return () => { live = false }
  }, [num, level])
  if (deck === undefined) return <div className="pz-root" aria-busy="true" />
  if (deck === null) return <div className="pz-missing"><p>Slides for this lesson are not available yet.</p><Link to={level === 1 ? '/level1' : '/level2'}>Back to the course</Link></div>
  return <Presenter key={`${level}-${num}`} deck={deck} level={level} />
}

function Presenter({ deck, level }: { deck: Deck; level: Level }) {
  const label = level === 1 ? `Level 1 · Lesson ${deck.lesson}` : `Lesson ${deck.lesson}`
  const pptx = level === 1 ? level1Pptx(deck.lesson) : SLIDES_AVAILABLE(deck.lesson) ? slidePath(deck.lesson) : ''
  const [params, setParams] = useSearchParams()
  const clampSlide = (v: number) => deck ? Math.min(Math.max(v, 1), deck.slides.length) : 1
  const [pos, setPos] = useState(() => {
    const s = clampSlide(Number(params.get('s') ?? 1))
    const k = Math.max(0, Math.min(Number(params.get('k') ?? 0), deck?.slides[s - 1].steps.length ?? 0))
    return { s, k, from: k }   // `from`: steps at or below this are shown without animation
  })
  const [notes, setNotes] = useState(params.get('notes') === '1')
  const [grid, setGrid] = useState(false)
  const [full, setFull] = useState(false)
  const [scale, setScale] = useState(1)
  const stageRef = useRef<HTMLDivElement>(null)

  const W = deck ? deck.width / EMU : 1280, H = deck ? deck.height / EMU : 720

  const next = useCallback(() => setPos(p => {
    const sl = deck.slides[p.s - 1]
    if (p.k < sl.steps.length) return { s: p.s, k: p.k + 1, from: p.k }
    if (p.s < deck.slides.length) return { s: p.s + 1, k: 0, from: 0 }
    return p
  }), [deck])
  const prev = useCallback(() => setPos(p => {
    if (p.k > 0) return { s: p.s, k: p.k - 1, from: p.k - 1 }
    if (p.s > 1) { const k = deck.slides[p.s - 2].steps.length; return { s: p.s - 1, k, from: k } }
    return p
  }), [deck])
  const go = (s: number) => { setPos({ s: clampSlide(s), k: 0, from: 0 }); setGrid(false) }

  const toggleFull = useCallback(() => {
    if (document.fullscreenElement) document.exitFullscreen()
    else document.documentElement.requestFullscreen?.().catch(() => {})
  }, [])

  useEffect(() => { const f = () => setFull(!!document.fullscreenElement); document.addEventListener('fullscreenchange', f); return () => document.removeEventListener('fullscreenchange', f) }, [])
  useEffect(() => { if (deck) document.title = `${label} slides · ${deck.slides[pos.s - 1].title}` }, [deck, pos.s])
  // follow the URL if someone edits it or uses a link (?s=slide&k=click)
  const qs = params.get('s'), qk = params.get('k')
  const written = useRef('')
  useEffect(() => {
    if (!deck || qs === null || `${qs}:${qk}` === written.current) return
    const s = clampSlide(Number(qs)), k = Math.max(0, Math.min(Number(qk ?? 0), deck.slides[s - 1].steps.length))
    setPos(p => (p.s === s && p.k === k ? p : { s, k, from: k }))
  }, [qs, qk]) // eslint-disable-line react-hooks/exhaustive-deps
  // keep the position in the URL so a refresh (or a link) returns to the same click
  useEffect(() => {
    written.current = `${pos.s}:${pos.k}`
    const q = new URLSearchParams({ s: String(pos.s), k: String(pos.k) }); if (notes) q.set('notes', '1')
    setParams(q, { replace: true })
  }, [pos.s, pos.k, notes]) // eslint-disable-line react-hooks/exhaustive-deps

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.ctrlKey || e.metaKey || e.altKey) return
      switch (e.key) {
        case 'ArrowRight': case 'ArrowDown': case ' ': case 'PageDown': case 'Enter': e.preventDefault(); next(); break
        case 'ArrowLeft': case 'ArrowUp': case 'PageUp': case 'Backspace': e.preventDefault(); prev(); break
        case 'Home': go(1); break
        case 'End': go(deck.slides.length); break
        case 'f': case 'F': toggleFull(); break
        case 'n': case 'N': setNotes(v => !v); break
        case 'g': case 'G': setGrid(v => !v); break
        case 'Escape': setGrid(false); break   // the browser itself leaves fullscreen on Esc
      }
    }
    window.addEventListener('keydown', onKey); return () => window.removeEventListener('keydown', onKey)
  })

  useLayoutEffect(() => {
    const el = stageRef.current; if (!el) return
    const ro = new ResizeObserver(() => setScale(Math.min(el.clientWidth / W, el.clientHeight / H)))
    ro.observe(el); return () => ro.disconnect()
  }, [W, H, notes])

  const slide = deck.slides[pos.s - 1]
  const total = deck.slides.length

  const onStagePointer = (e: React.PointerEvent<HTMLDivElement>) => {
    if (e.button !== 0) return
    if (e.pointerType === 'mouse') { next(); return }   // mouse click anywhere = next
    const r = e.currentTarget.getBoundingClientRect()     // touch / pen: left half = back, right half = next
    if (e.clientX - r.left < r.width / 2) prev(); else next()
  }

  return (
    <div className={`pz-root ${full ? 'pz-full' : ''}`}>
      <div className="pz-stage" ref={stageRef} onPointerUp={onStagePointer} role="region"
        aria-roledescription="slide" aria-label={`Slide ${pos.s} of ${total}: ${slide.title}`}>
        <div className="pz-scaler" style={{ width: W * scale, height: H * scale }}>
          <div style={{ transform: `scale(${scale})`, transformOrigin: '0 0', width: W, height: H }}>
            <SlideView key={pos.s} slide={slide} step={pos.k} animateFrom={pos.from} width={deck.width} height={deck.height} />
          </div>
        </div>
      </div>
      {notes && <aside className="pz-notes" aria-label="Speaker notes"><h2>Notes · slide {pos.s}</h2><p>{slide.notes || 'No notes for this slide.'}</p></aside>}
      <nav className="pz-bar" aria-label="Slide controls">
        <button onClick={prev} aria-label="Previous (Left arrow)" disabled={pos.s === 1 && pos.k === 0}><ChevronLeft /></button>
        <span className="pz-count" aria-live="polite">
          <strong>{pos.s}</strong> / {total}
          {slide.steps.length > 0 && <span className="pz-steps"> · click {pos.k}/{slide.steps.length}</span>}
        </span>
        <button onClick={next} aria-label="Next (Space or Right arrow)" disabled={pos.s === total && pos.k === slide.steps.length}><ChevronRight /></button>
        <span className="pz-title">{slide.title}</span>
        <span className="pz-spacer" />
        <button onClick={() => setGrid(true)} aria-label="All slides (G)" title="All slides (G)"><LayoutGrid /></button>
        <button onClick={() => setNotes(v => !v)} aria-pressed={notes} aria-label="Speaker notes (N)" title="Speaker notes (N)"><StickyNote /></button>
        <button onClick={toggleFull} aria-label={full ? 'Exit full screen (Esc)' : 'Full screen (F)'} title={full ? 'Exit full screen (Esc)' : 'Full screen (F)'}>{full ? <Minimize /> : <Maximize />}</button>
        {pptx && <a href={pptx} download aria-label="Download PowerPoint" title="Download PowerPoint (.pptx)"><Download /></a>}
      </nav>
      {grid && (
        <div className="pz-grid" role="dialog" aria-label="All slides">
          <div className="pz-grid-head"><h2>{label} · {total} slides</h2><button onClick={() => setGrid(false)} aria-label="Close (Esc)"><X /></button></div>
          <ol>
            {deck.slides.map(sl => (
              <li key={sl.n}><button onClick={() => go(sl.n)} aria-current={sl.n === pos.s} aria-label={`Go to slide ${sl.n}: ${sl.title}`}>
                <div className="pz-thumb" style={{ width: 256, height: 144 }}>
                  <div style={{ transform: 'scale(0.2)', transformOrigin: '0 0', width: W, height: H }}>
                    <SlideView slide={sl} step={sl.steps.length} animateFrom={sl.steps.length} width={deck.width} height={deck.height} />
                  </div>
                </div>
                <span>{sl.n}. {sl.title}</span>
              </button></li>))}
          </ol>
        </div>)}
    </div>)
}
