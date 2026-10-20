import { ReactNode } from 'react'
import { Download, Star } from 'lucide-react'
export function Card({ children, className = '' }: { children: ReactNode; className?: string }) {
  return <div className={`rounded-2xl border border-slate-200 bg-white p-5 shadow-sm sm:p-6 ${className}`}>{children}</div>
}
export function Html({ html, className = '' }: { html: string; className?: string }) {
  return <div className={`prose-esl ${className}`} dangerouslySetInnerHTML={{ __html: html }} />
}
export function Badge({ children, tone = 'blue' }: { children: ReactNode; tone?: 'blue' | 'green' | 'amber' | 'slate' }) {
  const t = { blue: 'bg-blue-50 text-blue-800 ring-blue-200', green: 'bg-emerald-50 text-emerald-800 ring-emerald-200',
    amber: 'bg-amber-50 text-amber-900 ring-amber-200', slate: 'bg-slate-100 text-slate-700 ring-slate-200' }[tone]
  return <span className={`inline-flex items-center gap-1 rounded-full px-3 py-1 text-sm font-medium ring-1 ${t}`}>{children}</span>
}
export function SectionTitle({ icon, children, id }: { icon: ReactNode; children: ReactNode; id?: string }) {
  return <h2 id={id} className="mb-4 mt-10 flex scroll-mt-24 items-center gap-3 text-2xl font-bold text-slate-900">
    <span className="grid size-10 place-items-center rounded-xl bg-blue-100 text-blue-700" aria-hidden="true">{icon}</span>{children}</h2>
}
export function DlRow({ href, icon, title, meta }: { href: string; icon: JSX.Element; title: string; meta: string }) {
  return <a href={href} download className="flex items-center gap-4 rounded-2xl border border-slate-200 bg-white p-4 shadow-sm transition hover:border-blue-400 hover:shadow-md">
    <span className="grid size-12 shrink-0 place-items-center rounded-xl bg-blue-50 text-blue-700" aria-hidden="true">{icon}</span>
    <span><span className="block text-lg font-semibold text-slate-900">{title}</span><span className="text-slate-600">{meta}</span></span>
    <Download className="ml-auto text-slate-400" aria-hidden="true" /></a>
}
export interface WordCard { img: string; word: string; star: boolean }
export function WordCards({ words, intro = true }: { words: WordCard[]; intro?: boolean }) {
  return (<>
    {intro && <p className="mb-4 text-lg text-slate-700"><em>Look. Listen. Repeat.</em> <Star size={16} className="inline fill-amber-400 text-amber-500" aria-label="star" /> = most important words.</p>}
    <ul className="words-grid grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-4">
      {words.map(w => (
        <li key={w.img} className="word-card overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
          <img src={w.img} alt={w.word} width={600} height={420} loading="lazy" className="aspect-[10/7] w-full object-contain" />
          <div className="flex items-center justify-center gap-1.5 border-t border-slate-100 px-2 py-3 text-center text-lg font-semibold text-slate-900">
            {w.star && <Star size={16} className="shrink-0 fill-amber-400 text-amber-500" aria-label="most important" />}{w.word}
          </div>
        </li>))}
    </ul>
  </>)
}
