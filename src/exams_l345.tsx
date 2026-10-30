// Levels 3–5: the Exams page (#/level<V>/exams, #midterm, #final) and the milestone link on each level's lesson list.
// Same layout as the Level 1 Exams page (level1.tsx). Exam data comes from src/content_level<V>.json "exams" (scripts/export_content.py),
// built from level<V>/exams/ (see level<V>/exams/build/build_all.sh). Until an exam MP3 is recorded, the page says the audio is coming soon.
import { Link, useLocation } from 'react-router-dom'
import { useEffect } from 'react'
import { ArrowRight, ClipboardCheck, FileAudio, FileText, Headphones, PartyPopper, AlertTriangle } from 'lucide-react'
import type { L1Content, L1Exam } from './content_level1'
import { level3 } from './content_level3'
import { level4 } from './content_level4'
import { level5 } from './content_level5'
import { mb } from './content'
import { Card, SectionTitle, DlRow } from './ui'

type ExamLevel = 3 | 4 | 5
const CONTENT: Record<ExamLevel, L1Content> = { 3: level3, 4: level4, 5: level5 }
const LINK_STYLE: Record<ExamLevel, string> = {
  3: 'text-emerald-800', 4: 'text-amber-800', 5: 'text-rose-800',
}
const KIND_ICON = { pdf: <FileText />, docx: <FileText />, pptx: <FileText />, mp3: <FileAudio /> }
const mmss = (s: number) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`
const examTitle = (e: L1Exam) => `Week ${e.week}: ${e.title}`
const examsOf = (V: ExamLevel): L1Exam[] => CONTENT[V].exams ?? []

/** The exam for a milestone week (8 or 15), if its packet is published. */
export const examFor = (V: ExamLevel, week: number) => examsOf(V).find(e => e.week === week)

/** Milestone link on the lesson list (replaces the "Coming soon" badge once the exam is published). */
export function ExamMilestoneLink({ level, week }: { level: ExamLevel; week: number }) {
  const exam = examFor(level, week)
  if (!exam) return null
  return <Link to={`/level${level}/exams#${exam.key}`} data-exam={exam.key}
    className={`mt-3 inline-flex items-center gap-1 font-semibold hover:underline ${LINK_STYLE[level]}`}>
    Teacher packet and student test <ArrowRight size={16} aria-hidden="true" /></Link>
}

function ExamDownloads({ exam }: { exam: L1Exam }) {
  return (<div className="mb-3 grid gap-3 md:grid-cols-2">
    {exam.downloads.map(d => <DlRow key={d.href} href={d.href} icon={KIND_ICON[d.kind]} title={`${exam.title}: ${d.label}`} meta={`${d.kind.toUpperCase()} · ${mb(d.size)}`} />)}
  </div>)
}

/** #/level<V>/exams (#midterm, #final): Week 8 Midterm and Week 15 Final. */
export function LevelExamsPage({ level }: { level: ExamLevel }) {
  const loc = useLocation()
  useEffect(() => {
    if (!loc.hash) return
    const t = window.setTimeout(() => document.getElementById(loc.hash.slice(1))?.scrollIntoView({ behavior: 'smooth' }), 50)
    return () => window.clearTimeout(t)
  }, [loc.hash])
  const exams = examsOf(level)
  const grad = CONTENT[level].milestones.find(m => m.week === 16)
  const written = (exams[0]?.parts ?? []).map(p => p.part.replace(/<[^>]+>/g, '')).filter(p => /^[A-E]\. /.test(p)).map(p => p.slice(3).toLowerCase())
  return (<div className="max-w-4xl">
    <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">Level {level} exams</h1>
    <p className="mt-2 text-lg text-slate-700">{exams.map(e => `${examTitle(e)} (${e.covers})`).join(' and ')}. For teachers. Each test is one class night: {written.length ? `${written.slice(0, -1).join(', ')}, and ${written[written.length - 1]}` : 'a written test'}, plus a short speaking interview in pairs. Print the student tests separately.</p>
    {exams.map(e => (
      <section key={e.key} id={e.key} className="scroll-mt-24">
        <SectionTitle icon={<ClipboardCheck size={20} />}>{examTitle(e)}</SectionTitle>
        <Card>
          <p className="mb-3 text-lg text-slate-700">The teacher packet has step-by-step directions, a clock-time plan, the listening script, the answer key, the speaking interview card, rubric, task cards and score sheet, the writing rubric, and the can-do self-check.</p>
          <div className="mb-4 overflow-x-auto">
            <table className="w-full text-left text-slate-700">
              <thead><tr className="border-b border-slate-200 text-sm uppercase tracking-wide text-slate-500"><th className="py-2 pr-3">Part</th><th className="py-2 pr-3">What learners do</th><th className="py-2 pr-3">Points</th><th className="py-2">Time</th></tr></thead>
              <tbody>{e.parts.map((p, i) => <tr key={i} className="border-b border-slate-100 align-top">
                <td className="py-2 pr-3" dangerouslySetInnerHTML={{ __html: p.part }} /><td className="py-2 pr-3" dangerouslySetInnerHTML={{ __html: p.what }} />
                <td className="py-2 pr-3" dangerouslySetInnerHTML={{ __html: p.points }} /><td className="py-2" dangerouslySetInnerHTML={{ __html: p.time }} /></tr>)}</tbody>
            </table>
          </div>
          {e.noteHtml && <p className="mb-4 text-slate-600" dangerouslySetInnerHTML={{ __html: e.noteHtml }} />}
          <ExamDownloads exam={e} />
          {e.audio
            ? <div className="audio-box my-4 rounded-2xl bg-blue-50 p-4 ring-1 ring-blue-100">
                <div className="mb-2 flex items-center gap-2 font-semibold text-blue-900"><Headphones size={20} aria-hidden="true" /> {e.title} listening audio{e.audioSeconds ? ` (about ${mmss(e.audioSeconds)})` : ''}</div>
                <audio controls preload="none" src={e.audio} className="no-print w-full">Your browser cannot play audio.</audio>
                <p className="mt-2 text-sm text-slate-600">The conversation is in the file once. Press play again for each listen.</p>
              </div>
            : <div className="mt-4 flex items-start gap-3 rounded-2xl bg-amber-50 p-4 text-amber-950 ring-1 ring-amber-200">
                <Headphones size={20} className="mt-0.5 shrink-0" aria-hidden="true" />
                <p><strong>Listening audio coming soon:</strong> read the script aloud. The script is in the teacher packet.</p>
              </div>}
        </Card>
      </section>))}
    {grad && (<>
      <SectionTitle icon={<PartyPopper size={20} />}>Week 16: {grad.title}</SectionTitle>
      <Card><p className="text-lg text-slate-700">Week 16 is graduation: {grad.note ? grad.note.replace(/;\s*/g, ', ') : 'certificates'}. No new content and no downloads.</p></Card>
    </>)}
    <div className="mt-8 flex items-start gap-3 rounded-2xl border-l-4 border-amber-400 bg-amber-50 p-5 text-lg text-amber-950">
      <AlertTriangle size={22} className="mt-1 shrink-0" aria-hidden="true" />
      <p>Keep teacher packets away from learners (they contain answer keys). The student tests have no answers.</p>
    </div>
  </div>)
}
