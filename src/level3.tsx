// Level 3 pages: overview, lesson list, lesson page (Student / Teacher / Downloads tabs), downloads.
// Same layout as Level 1 (level1.tsx). Lesson text comes from src/content_level3.json (scripts/export_content.py); page wording lives here.
import { Link, Navigate, useParams } from 'react-router-dom'
import * as Tabs from '@radix-ui/react-tabs'
import { ArrowLeft, ArrowRight, BookOpen, CalendarDays, Clock, Download, FileAudio, FileText, Headphones, MonitorPlay,
  Presentation, Printer, Users, Star, MessageSquareText, NotebookPen, ListChecks, Footprints, Hourglass, CheckSquare, PenLine, Languages } from 'lucide-react'
import type { ReactNode } from 'react'
import type { L1Lesson, L1Section } from './content_level1'
import { level3, readyLessons3 as readyLessons } from './content_level3'
import { mb } from './content'
import { Card, Html, SectionTitle, DlRow, WordCards } from './ui'
import { level3PresentHref } from './config'
import { examFor, ExamMilestoneLink } from './exams_l345'
import { hasDeck } from './presenter/decks'

const lessonHref = (n: number, tab?: string) => `/level3/lesson/${n}${tab ? `/${tab}` : ''}`
const SECTION_ICON: Record<string, ReactNode> = {
  'task-words': <ListChecks size={20} />, 'how-our-class-works': <Clock size={20} />, 'new-words': <Star size={20} />,
  'my-words': <Languages size={20} />, listening: <Headphones size={20} />, grammar: <MessageSquareText size={20} />,
  'talk-time': <Footprints size={20} />, homework: <NotebookPen size={20} />, 'read-write': <PenLine size={20} />,
  'progress-check': <CheckSquare size={20} />,
}
const KIND_ICON = { pdf: <FileText />, docx: <FileText />, pptx: <Presentation />, mp3: <FileAudio /> }
const firstReady = readyLessons[0]
/** Lessons without a lesson book yet whose teacher slides are published (slides only: no student pages, PDF/DOCX, or audio yet). */
const slidesOnly = level3.lessons.filter(l => !l.ready && !!l.slides)
const range = (ls: { n: number }[]) => ls.length === 1 ? `Lesson ${ls[0].n}` : `Lessons ${ls[0].n}–${ls[ls.length - 1].n}`
const readyNote = readyLessons.length === 13 ? 'All 13 lessons are ready.'
  : (readyLessons.length === 1 ? 'Lesson 1 is ready.' : `Lessons 1–${readyLessons.length} are ready.`) + ` Lessons ${readyLessons.length + 1}–13 are coming soon.`

export function Level3Home() {
  return (<>
    <section className="mb-8 rounded-2xl border border-sky-100 border-l-4 border-l-emerald-300 bg-gradient-to-r from-sky-50 to-emerald-50 px-4 py-4 sm:px-8 sm:py-6">
      <span className="inline-block rounded-full bg-white/80 px-2.5 py-0.5 text-xs font-semibold text-slate-600 ring-1 ring-slate-200">Free · Low intermediate · 16 weeks</span>
      <h1 className="mt-2 text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl">🌳 Level 3 Adult ESL</h1>
      <p className="mt-2 max-w-2xl text-[15px] leading-snug text-slate-700 sm:text-lg sm:leading-relaxed">A free course for adults who finished Level 2: keep a conversation going, give reasons, describe people, tell what happened, make offers and promises, and handle problems at home, at work, and in town. 13 lessons with pictures, listening, grammar, reading and writing, and full teacher plans.</p>
      <p className="mt-2 text-sm font-medium text-emerald-800">{readyNote}{slidesOnly.length > 0 && ` Teacher slides for ${range(slidesOnly)} are ready now.`}</p>
      <div className="mt-3 flex flex-row flex-wrap gap-2">
        {firstReady && <Link to={lessonHref(firstReady.n)} className="btn whitespace-nowrap bg-blue-600 !gap-1.5 !px-3 !py-2 !text-sm text-white sm:!px-4 sm:!text-base hover:bg-blue-700">Start Lesson {firstReady.n} <ArrowRight size={18} aria-hidden="true" /></Link>}
        <Link to="/level3/downloads" className="btn whitespace-nowrap border border-slate-300 bg-white !gap-1.5 !px-3 !py-2 !text-sm text-slate-700 sm:!px-4 sm:!text-base hover:bg-slate-50"><Download size={18} aria-hidden="true" /> Downloads</Link>
      </div>
    </section>
    <SectionTitle icon={<BookOpen size={20} />}>Lessons</SectionTitle>
    <Level3Grid />
    <SectionTitle icon={<CalendarDays size={20} />}>16-week semester plan</SectionTitle>
    <Card><Html html={level3.semester} /></Card>
    <SectionTitle icon={<Clock size={20} />}>Class routine (same every week)</SectionTitle>
    <Card><Html html={level3.routine} /></Card>
    <div className="mt-10 grid gap-6 lg:grid-cols-2">
      <div><SectionTitle icon={<Users size={20} />}>For students</SectionTitle><Card>
        <ul className="list-disc space-y-2 pl-6 text-lg text-slate-700">
          <li>Instructions are short and in English. The Task Words page explains them, with a Spanish and a "My language" column.</li>
          <li>Write new words in your language on the My Words page.</li>
          <li>Listen to the audio on your phone. Play it again if you need to.</li>
          <li>Homework takes about 15 minutes.</li>
        </ul></Card></div>
      <div><SectionTitle icon={<Presentation size={20} />}>For teachers</SectionTitle><Card>
        <p className="mb-2 text-lg font-semibold text-slate-800">Teachers do not need to speak Spanish.</p>
        <p className="text-lg text-slate-700">Teach in English. Show, point, and give one more example. Each lesson has a clock-time teacher plan, slides you can present in the browser, listening audio, and printable student pages, including a Read &amp; Write page.</p>
      </Card></div>
    </div>
  </>)
}

function Milestone({ week, title, note }: { week: number; title: string; note: string }) {
  return (
    <div className="rounded-2xl border border-dashed border-emerald-200 bg-emerald-50/50 p-5">
      <div className="text-sm font-semibold uppercase tracking-wide text-emerald-700">Week {week}</div>
      <div className="mt-1 text-xl font-bold text-slate-800">{title === 'Graduation' ? '🎓 ' : '📝 '}{title}</div>
      <div className="mt-2 text-slate-600">{note}</div>
      {title !== 'Graduation' && (examFor(3, week) ? <ExamMilestoneLink level={3} week={week} /> : <div className="mt-3"><SoonBadge /></div>)}
    </div>)
}

const SoonBadge = ({ label = 'Coming soon' }: { label?: string }) => <span className="inline-flex items-center gap-1 rounded-full bg-white px-3 py-1 text-sm font-semibold text-emerald-800 ring-1 ring-emerald-200"><Hourglass size={14} aria-hidden="true" /> {label}</span>
const SlidesBadge = () => <span className="inline-flex items-center gap-1 rounded-full bg-indigo-50 px-3 py-1 text-sm font-semibold text-indigo-800 ring-1 ring-indigo-200"><MonitorPlay size={14} aria-hidden="true" /> Slides ready</span>

export function Level3Grid() {
  const items: ReactNode[] = [], placed = new Set<number>()
  const milestone = (m: typeof level3.milestones[number]) => { placed.add(m.week); items.push(<Milestone key={`m${m.week}`} {...m} />) }
  for (const l of level3.lessons) {
    for (const m of level3.milestones) if (m.week < l.week && !placed.has(m.week)) milestone(m)   // Week 8 midterm sits between Lessons 7 and 8
    items.push(l.ready
      ? <Link key={l.n} to={lessonHref(l.n)} className="group rounded-2xl border border-slate-200 bg-white p-5 shadow-sm transition hover:-translate-y-0.5 hover:border-blue-400 hover:shadow-md">
          <div className="text-sm font-semibold uppercase tracking-wide text-blue-700">Lesson {l.n} · Week {l.week}</div>
          <div className="mt-1 text-xl font-bold text-slate-900">{l.title}</div>
          <div className="mt-2 text-slate-600">{l.function}</div>
          <div className="mt-4 grid grid-cols-2 gap-2">{(l.words ?? []).slice(0, 2).map(w =>
            <img key={w.img} src={w.img} alt="" className="aspect-[10/7] w-full rounded-lg border border-slate-100 object-contain" />)}</div>
        </Link>
      : <Link key={l.n} to={lessonHref(l.n)} className="rounded-2xl border border-dashed border-slate-300 bg-slate-50/70 p-5 transition hover:border-emerald-300">
          <div className="text-sm font-semibold uppercase tracking-wide text-slate-500">Lesson {l.n} · Week {l.week}</div>
          <div className="mt-1 text-xl font-bold text-slate-700">{l.title}</div>
          <div className="mt-2 text-slate-500">{l.function}</div>
          <div className="mt-3 flex flex-wrap gap-2">{l.slides ? <SlidesBadge /> : null}<SoonBadge label={l.slides ? 'Lesson book soon' : undefined} /></div>
        </Link>)
  }
  for (const m of level3.milestones) if (!placed.has(m.week)) milestone(m)
  return <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">{items}</div>
}

export function Level3LessonsPage() {
  return (<>
    <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">Level 3 lessons</h1>
    <p className="mt-2 mb-6 text-lg text-slate-700">13 lessons over 16 weeks. Week 8 is the midterm, Week 15 is the final exam, and Week 16 is graduation. {readyNote}{slidesOnly.length > 0 && ` The teacher slides for ${range(slidesOnly)} are ready: open a lesson to present them or download the PowerPoint.`}</p>
    <Level3Grid />
  </>)
}

function AudioPlayer({ lesson }: { lesson: L1Lesson }) {
  if (!lesson.audio) return (
    <div className="audio-box my-4 flex items-start gap-3 rounded-2xl bg-amber-50 p-4 text-amber-950 ring-1 ring-amber-200">
      <Headphones size={20} className="mt-0.5 shrink-0" aria-hidden="true" />
      <p><strong>Audio coming soon.</strong> Until then, the teacher reads the listening script aloud (it is in the Teacher tab).</p>
    </div>)
  return (
    <div className="audio-box my-4 rounded-2xl bg-blue-50 p-4 ring-1 ring-blue-100">
      <div className="mb-2 flex items-center gap-2 font-semibold text-blue-900"><Headphones size={20} aria-hidden="true" /> Listen: the conversation plays once. Press play again to listen again.</div>
      <audio controls preload="none" src={lesson.audio} className="no-print w-full">Your browser cannot play audio.</audio>
      <a href={lesson.audio} download className="link no-print mt-2 inline-flex items-center gap-1 text-sm"><Download size={14} aria-hidden="true" /> Download MP3 ({mb(lesson.audioSize ?? 0)})</a>
    </div>)
}

function PresentButtons({ lesson }: { lesson: L1Lesson }) {
  return <span className="inline-flex flex-wrap gap-2">
    {hasDeck(lesson.n, 3) && <a href={level3PresentHref(lesson.n)} target="_blank" rel="noopener" className="btn bg-indigo-600 text-white hover:bg-indigo-700"><MonitorPlay size={18} aria-hidden="true" /> Present Lesson {lesson.n}<span className="sr-only"> (opens in a new tab)</span></a>}
    {lesson.slides && <a href={lesson.slides} download className="btn bg-emerald-600 text-white hover:bg-emerald-700"><Presentation size={18} aria-hidden="true" /> Download PowerPoint (.pptx)</a>}
  </span>
}

function StudentSection({ s, lesson }: { s: L1Section; lesson: L1Lesson }) {
  return (<>
    <SectionTitle id={s.id} icon={SECTION_ICON[s.id] ?? <FileText size={20} />}>{s.title}</SectionTitle>
    {s.kind === 'words'
      ? <><Card className="mb-4"><Html html={s.html} /></Card><WordCards words={lesson.words ?? []} intro={false} />{s.htmlAfter && <Card className="mt-4"><Html html={s.htmlAfter} /></Card>}</>
      : <Card>{s.kind === 'listening' && <AudioPlayer lesson={lesson} />}<Html html={s.html} /></Card>}
    <div className="page-break" />
  </>)
}

function DownloadList({ lesson }: { lesson: L1Lesson }) {
  return <div className="grid gap-3 md:grid-cols-2">
    {(lesson.downloads ?? []).map(d => <DlRow key={d.href} href={d.href} icon={KIND_ICON[d.kind]} title={`Lesson ${lesson.n}: ${d.label}`} meta={`${d.kind.toUpperCase()} · ${mb(d.size)}`} />)}
  </div>
}

const tabCls = 'flex items-center gap-2 rounded-xl px-4 py-2.5 text-lg font-semibold text-slate-600 transition data-[state=active]:bg-white data-[state=active]:text-blue-700 data-[state=active]:shadow-sm hover:text-slate-900 sm:px-5'

export function Level3LessonPage() {
  const { n, tab } = useParams()
  const lesson = level3.lessons.find(l => String(l.n) === n)
  if (!lesson) return <Navigate to="/level3" replace />
  const idx = level3.lessons.indexOf(lesson)
  const prev = level3.lessons[idx - 1], next = level3.lessons[idx + 1]
  const pager = (
    <nav aria-label="Lessons" className="no-print mt-10 flex justify-between gap-4 text-lg">
      {prev ? <Link className="link inline-flex items-center gap-1" to={lessonHref(prev.n)}><ArrowLeft size={18} aria-hidden="true" /> Lesson {prev.n}</Link> : <Link className="link inline-flex items-center gap-1" to="/level3"><ArrowLeft size={18} aria-hidden="true" /> Level 3</Link>}
      {next ? <Link className="link inline-flex items-center gap-1" to={lessonHref(next.n)}>Lesson {next.n} <ArrowRight size={18} aria-hidden="true" /></Link> : <Link className="link inline-flex items-center gap-1" to="/level3/downloads">Downloads <ArrowRight size={18} aria-hidden="true" /></Link>}
    </nav>)
  const header = (
    <div>
      <div className="text-sm font-semibold uppercase tracking-wide text-blue-700">Level 3 · Lesson {lesson.n} · Week {lesson.week}</div>
      <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">{lesson.title}</h1>
      <p className="mt-1 text-lg text-slate-600">{lesson.function}</p>
    </div>)
  if (!lesson.ready) return (<>
    <div className="mb-6">{header}</div>
    {lesson.slides && <Card className="mb-6 max-w-3xl bg-emerald-50/60">
      <div className="mb-3"><SlidesBadge /></div>
      <p className="text-lg text-slate-700">The teacher slides for this lesson are ready. <strong>Present</strong> opens them in a new browser tab (press N for the teacher notes). The student pages, the full teacher plan, the PDF and Word files, and the listening audio are coming soon; until the audio is ready, the teacher reads the listening script aloud (it is in the notes of the Before You Listen slide).</p>
      <div className="mt-4"><PresentButtons lesson={lesson} /></div>
    </Card>}
    <Card className="max-w-3xl">
      <div className="mb-3"><SoonBadge label={lesson.slides ? 'Lesson book coming soon' : undefined} /></div>
      <p className="text-lg text-slate-700">{lesson.slides ? 'The lesson book is not built yet.' : 'This lesson is not built yet.'} Here is the plan:</p>
      <p className="mt-3 text-lg"><strong>Grammar Q&amp;A focus:</strong> <span className="prose-esl" dangerouslySetInnerHTML={{ __html: lesson.focusHtml }} /></p>
      <p className="mt-3 text-lg"><Link className="link font-semibold" to="/level3/lessons">See all Level 3 lessons →</Link></p>
    </Card>
    {pager}
  </>)
  const active = tab === 'teacher' || tab === 'downloads' ? tab : 'student'
  const sections = lesson.sections ?? []
  return (<>
    <div className="mb-6 flex flex-wrap items-end justify-between gap-4">
      {header}
      <button onClick={() => window.print()} className="btn no-print border border-slate-300 bg-white text-slate-700 hover:bg-slate-50"><Printer size={18} aria-hidden="true" /> Print this tab</button>
    </div>
    {lesson.topic && <p className="no-print -mt-2 mb-6 max-w-3xl rounded-xl bg-emerald-50 px-4 py-2 text-lg text-slate-700 ring-1 ring-emerald-100"><strong>Topic:</strong> <span dangerouslySetInnerHTML={{ __html: lesson.topic }} /></p>}
    <Tabs.Root value={active} onValueChange={v => { window.location.hash = `#/level3/lesson/${lesson.n}/${v}` }}>
      <Tabs.List aria-label="Lesson sections" className="no-print mb-6 inline-flex flex-wrap gap-1 rounded-2xl bg-slate-100 p-1.5">
        <Tabs.Trigger value="student" className={tabCls}><Users size={20} aria-hidden="true" /> Student</Tabs.Trigger>
        <Tabs.Trigger value="teacher" className={tabCls}><Presentation size={20} aria-hidden="true" /> Teacher</Tabs.Trigger>
        <Tabs.Trigger value="downloads" className={tabCls}><Download size={20} aria-hidden="true" /> Downloads</Tabs.Trigger>
      </Tabs.List>
      <Tabs.Content value="student" className="outline-none">
        <nav aria-label="On this page" className="no-print mb-2 flex flex-wrap gap-2">
          {sections.map(s =>
            <a key={s.id} href={`#${s.id}`} onClick={e => { e.preventDefault(); document.getElementById(s.id)?.scrollIntoView({ behavior: 'smooth' }) }}
              className="rounded-full bg-blue-50 px-4 py-1.5 font-medium text-blue-800 hover:bg-blue-100">{s.title}</a>)}
        </nav>
        {sections.map(s => <StudentSection key={s.id} s={s} lesson={lesson} />)}
      </Tabs.Content>
      <Tabs.Content value="teacher" className="outline-none">
        <Card className="mb-6 bg-emerald-50/60"><div className="flex flex-wrap items-center gap-3">
          <span className="font-semibold text-emerald-900">Teacher materials:</span>
          <PresentButtons lesson={lesson} />
          {lesson.audio && <a href={lesson.audio} download className="btn no-print border border-slate-300 bg-white text-slate-700 hover:bg-slate-50"><FileAudio size={18} aria-hidden="true" /> Listening MP3</a>}
        </div></Card>
        <Card><Html html={lesson.teacher ?? ''} className="teacher" /></Card>
      </Tabs.Content>
      <Tabs.Content value="downloads" className="outline-none">
        <p className="mb-4 max-w-3xl text-lg text-slate-700">The PDF and Word files have the teacher plan and all the student pages for Lesson {lesson.n}. Print the Student Pages part for learners.</p>
        <DownloadList lesson={lesson} />
        <SectionTitle icon={<MonitorPlay size={20} />}>Present in the browser</SectionTitle>
        <p className="mb-4 text-lg text-slate-700"><strong>Present</strong> opens the slides in a new browser tab: click or press Space / → for the next step, ← to go back, F for full screen, N for notes.</p>
        <PresentButtons lesson={lesson} />
      </Tabs.Content>
    </Tabs.Root>
    {pager}
  </>)
}

export function Level3DownloadsPage() {
  const soon = level3.lessons.filter(l => !l.ready && !l.slides)
  return (<>
    <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">Level 3 downloads</h1>
    <p className="mt-2 text-lg text-slate-700">For each finished lesson: the lesson document (teacher plan + student pages) as PDF and Word, the teacher slides, and the listening audio. Each audio file has a short intro and plays the conversation once; play it again if needed.</p>
    {readyLessons.map(l => (<section key={l.n}>
      <SectionTitle icon={<BookOpen size={20} />}>Lesson {l.n}: {l.title}</SectionTitle>
      <DownloadList lesson={l} />
      <div className="mt-4"><PresentButtons lesson={l} /></div>
    </section>))}
    {slidesOnly.length > 0 && <>
      <SectionTitle icon={<Presentation size={20} />}>Teacher slides: {range(slidesOnly)}</SectionTitle>
      <p className="mb-4 max-w-3xl text-lg text-slate-700">The slides for these lessons are ready. The lesson books (PDF and Word) and the listening audio are coming soon; until the audio is ready, read the listening script aloud (it is in the notes of the Before You Listen slide).</p>
      {slidesOnly.map(l => (<section key={l.n} className="mb-6">
        <h3 className="mb-2 text-xl font-bold text-slate-800"><Link className="link" to={lessonHref(l.n)}>Lesson {l.n}: {l.title}</Link></h3>
        <DownloadList lesson={l} />
        <div className="mt-3"><PresentButtons lesson={l} /></div>
      </section>))}
    </>}
    {soon.length > 0 && <p className="mt-8 text-lg text-slate-700"><strong>{range(soon)}:</strong> coming soon.</p>}
    <SectionTitle icon={<Printer size={20} />}>Print a lesson</SectionTitle>
    <p className="text-lg text-slate-700">Open a lesson, choose the Student or Teacher tab, and press <strong>Print this tab</strong>. Menus and audio players are hidden on paper.</p>
  </>)
}
