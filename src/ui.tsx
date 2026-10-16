import { ReactNode } from 'react'
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
