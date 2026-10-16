import { useEffect, useState } from 'react'
import { Link, NavLink, Route, Routes, useLocation, useParams, Navigate } from 'react-router-dom'
import * as Tabs from '@radix-ui/react-tabs'
import { BookOpen, CalendarDays, Clock, Download, FileText, GraduationCap, Headphones, Home, Info, Menu,
  MessageSquareText, NotebookPen, Presentation, Printer, Users, X, Star, ArrowLeft, ArrowRight, FileAudio, MonitorPlay,
  ClipboardCheck, PartyPopper, AlertTriangle } from 'lucide-react'
import { content, sizes, mb, Lesson } from './content'
import { Card, Html, Badge, SectionTitle } from './ui'
import { SLIDES_AVAILABLE, slidePath, presentHref, examPath, LICENSE_URL, DISCLAIMER } from './config'
import { hasDeck } from './presenter/decks'
import { lazy, Suspense } from 'react'
const Presenter = lazy(() => import('./presenter/Presenter'))

const NAV = [
  { to: '/', label: 'Home', icon: Home },
  { to: '/lessons', label: 'Lessons', icon: BookOpen },
  { to: '/downloads', label: 'Downloads', icon: Download },
  { to: '/exams', label: 'Exams', icon: ClipboardCheck },
  { to: '/about', label: 'About', icon: Info },
]

function Header() {
  const [open, setOpen] = useState(false)
  const loc = useLocation()
  useEffect(() => { setOpen(false); window.scrollTo(0, 0) }, [loc.pathname])
  const cls = ({ isActive }: { isActive: boolean }) => clsFor(isActive)
  const clsFor = (isActive: boolean) =>
    `flex items-center gap-2 rounded-lg px-3 py-2 text-base font-medium transition ${isActive ? 'bg-blue-600 text-white' : 'text-slate-700 hover:bg-slate-100'}`
  return (
    <header className="no-print sticky top-0 z-20 border-b border-slate-200 bg-white/90 backdrop-blur">
      <div className="mx-auto flex max-w-6xl items-center justify-between gap-4 px-4 py-3">
        <Link to="/" className="flex items-center gap-2 text-lg font-bold text-slate-900">
          <span className="grid size-9 place-items-center rounded-xl bg-blue-600 text-white"><GraduationCap size={20} aria-hidden="true" /></span>
          Level 2 Adult ESL
        </Link>
        <nav aria-label="Main" className="hidden gap-1 lg:flex">
          {NAV.map(n => <NavLink key={n.to} to={n.to} end={n.to === "/"} className={({ isActive }) => clsFor(isActive || (n.to === '/lessons' && loc.pathname.startsWith('/lesson/')))}>{n.label}</NavLink>)}
        </nav>
        <button className="rounded-lg p-2 text-slate-700 hover:bg-slate-100 lg:hidden" aria-expanded={open}
          aria-controls="mobile-nav" aria-label={open ? 'Close menu' : 'Open menu'} onClick={() => setOpen(!open)}>
          {open ? <X /> : <Menu />}
        </button>
      </div>
      {open && <nav id="mobile-nav" aria-label="Main" className="grid gap-1 border-t border-slate-200 px-4 py-3 lg:hidden">
        {NAV.map(n => <NavLink key={n.to} to={n.to} end={n.to === "/"} className={cls}><n.icon size={18} aria-hidden="true" />{n.label}</NavLink>)}
      </nav>}
    </header>)
}

function Footer() {
  return (
    <footer className="mt-16 border-t border-slate-200 bg-slate-50 text-sm text-slate-600">
      <div className="mx-auto max-w-6xl space-y-2 px-4 py-8">
        <p>© 2026 the authors. The authors license these course materials under <a className="link" href={LICENSE_URL}>CC BY-NC-SA 4.0</a>. Audio: Chatterbox TTS by Resemble AI (MIT License); synthetic voices with an inaudible Perth watermark.</p>
        <p dangerouslySetInnerHTML={{ __html: content.creditHtml }} />
        <p>{DISCLAIMER} <Link className="link no-print" to="/about">About &amp; Credits</Link></p>
      </div>
    </footer>)
}

function HomePage() {
  return (<>
    <section className="mb-8 rounded-2xl border border-sky-100 border-l-4 border-l-violet-300 bg-gradient-to-r from-sky-50 to-violet-50 px-4 py-4 sm:px-8 sm:py-6">
      <span className="inline-block rounded-full bg-white/80 px-2.5 py-0.5 text-xs font-semibold text-slate-600 ring-1 ring-slate-200">Free · High beginner · 16 weeks</span>
      <h1 className="mt-2 text-2xl font-bold tracking-tight text-slate-900 sm:text-3xl">Level 2 Adult ESL</h1>
      <p className="mt-2 max-w-2xl text-[15px] leading-snug text-slate-700 sm:text-lg sm:leading-relaxed">A free, practical course for high-beginner adult English learners. 13 lessons with pictures, listening, grammar, and full teacher plans.</p>
      <div className="mt-3 flex flex-row flex-nowrap gap-2">
        <Link to="/lesson/1" className="btn whitespace-nowrap bg-blue-600 !gap-1.5 !px-3 !py-2 !text-sm text-white sm:!px-4 sm:!text-base hover:bg-blue-700">Start Lesson 1 <ArrowRight size={18} aria-hidden="true" /></Link>
        <Link to="/downloads" className="btn whitespace-nowrap border border-slate-300 bg-white !gap-1.5 !px-3 !py-2 !text-sm text-slate-700 sm:!px-4 sm:!text-base hover:bg-slate-50"><Download size={18} aria-hidden="true" /> Downloads</Link>
      </div>
    </section>
    <SectionTitle icon={<BookOpen size={20} />}>Lessons</SectionTitle>
    <LessonGrid />
    <SectionTitle icon={<CalendarDays size={20} />}>16-week semester plan</SectionTitle>
    <Card><Html html={semesterHtml} /></Card>
    <SectionTitle icon={<Clock size={20} />}>Class routine (same every week)</SectionTitle>
    <Card><Html html={content.routine} /></Card>
    <div className="mt-10 grid gap-6 lg:grid-cols-2">
      <div><SectionTitle icon={<Users size={20} />}>For students</SectionTitle><Card><Html html={content.studentHowTo} /></Card></div>
      <div><SectionTitle icon={<Presentation size={20} />}>For teachers</SectionTitle><Card>
        <p className="mb-2 text-lg font-semibold text-slate-800">Teachers do not need to speak Spanish.</p>
        <p className="mb-4 text-lg"><Link className="link font-semibold" to="/exams">Midterm (Week 8) and Final Exam (Week 15) packets →</Link></p>
        <Html html={content.teacherGuide} /></Card></div>
    </div>
  </>)
}

// Week 8 / Week 15 rows of the semester table link to the Exams page.
const semesterHtml = content.semester
  .replace('<strong>Week 8: Midterm</strong>', '<a class="link" href="#/exams#midterm"><strong>Week 8: Midterm</strong></a>')
  .replace('<strong>Week 15: Final Exam</strong>', '<a class="link" href="#/exams#final"><strong>Week 15: Final Exam</strong></a>')

function LessonGrid() {
  return (
    <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-4">
      {content.lessons.map(l => (
        <Link key={l.n} to={`/lesson/${l.n}`} className="group rounded-2xl border border-slate-200 bg-white p-5 shadow-sm transition hover:-translate-y-0.5 hover:border-blue-400 hover:shadow-md">
          <div className="text-sm font-semibold uppercase tracking-wide text-blue-700">Lesson {l.n} · Week {l.week}</div>
          <div className="mt-1 text-xl font-bold text-slate-900">{l.title}</div>
          <div className="mt-2 text-slate-600">{l.grammar}</div>
          <div className="mt-4 grid grid-cols-2 gap-2">{l.words.slice(0, 2).map(w =>
            <img key={w.img} src={w.img} alt="" className="aspect-[10/7] w-full rounded-lg border border-slate-100 object-contain" />)}</div>
        </Link>))}
    </div>)
}

function LessonsPage() {
  return (<>
    <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">Lessons</h1>
    <p className="mt-2 mb-6 text-lg text-slate-700">13 lessons over 16 weeks. Week 8 is the midterm, Week 15 is the final exam, and Week 16 is graduation (see <Link className="link" to="/exams">Exams</Link>).</p>
    <LessonGrid />
  </>)
}

function WordCards({ lesson }: { lesson: Lesson }) {
  return (<>
    <p className="mb-4 text-lg text-slate-700"><em>Look. Listen. Repeat.</em> <Star size={16} className="inline fill-amber-400 text-amber-500" aria-label="star" /> = most important words.</p>
    <ul className="words-grid grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-4">
      {lesson.words.map(w => (
        <li key={w.img} className="word-card overflow-hidden rounded-2xl border border-slate-200 bg-white shadow-sm">
          <img src={w.img} alt={w.word} width={600} height={420} loading="lazy" className="aspect-[10/7] w-full object-contain" />
          <div className="flex items-center justify-center gap-1.5 border-t border-slate-100 px-2 py-3 text-center text-lg font-semibold text-slate-900">
            {w.star && <Star size={16} className="shrink-0 fill-amber-400 text-amber-500" aria-label="most important" />}{w.word}
          </div>
        </li>))}
    </ul>
  </>)
}

function AudioComingSoon({ what = 'The listening audio' }: { what?: string }) {
  return (
    <div className="audio-box my-4 flex items-start gap-3 rounded-2xl bg-amber-50 p-4 text-amber-950 ring-1 ring-amber-200">
      <Headphones size={20} className="mt-0.5 shrink-0" aria-hidden="true" />
      <p><strong>Audio coming soon.</strong> {what} is not ready yet. Until then, the teacher reads the listening script aloud (it is in the Teacher tab).</p>
    </div>)
}

function AudioPlayer({ lesson }: { lesson: Lesson }) {
  if (!lesson.audio) return <AudioComingSoon what={`The Lesson ${lesson.n} audio`} />
  return (
    <div className="audio-box my-4 rounded-2xl bg-blue-50 p-4 ring-1 ring-blue-100">
      <div className="mb-2 flex items-center gap-2 font-semibold text-blue-900"><Headphones size={20} aria-hidden="true" /> Listen: play the audio again if needed.</div>
      <audio controls preload="none" src={lesson.audio} className="no-print w-full">Your browser cannot play audio.</audio>
      <a href={lesson.audio} download className="link no-print mt-2 inline-flex items-center gap-1 text-sm"><Download size={14} aria-hidden="true" /> Download MP3 ({mb(sizes[`L${lesson.n}_listening.mp3`])})</a>
    </div>)
}

function SlidesLink({ n, compact = false }: { n: number; compact?: boolean }) {
  const present = hasDeck(n) && <a href={presentHref(n)} target="_blank" rel="noopener" className="btn bg-indigo-600 text-white hover:bg-indigo-700"><MonitorPlay size={18} aria-hidden="true" /> Present Lesson {n}<span className="sr-only"> (opens in a new tab)</span></a>
  if (SLIDES_AVAILABLE(n)) return <span className="inline-flex flex-wrap gap-2">{present}
    <a href={slidePath(n)} download className="btn bg-emerald-600 text-white hover:bg-emerald-700"><Presentation size={18} aria-hidden="true" /> Download PowerPoint (.pptx)</a></span>
  return <span className="inline-flex flex-wrap gap-2">{present}<span className={`inline-flex items-center gap-2 rounded-xl border border-dashed border-slate-300 px-4 py-2 text-slate-500 ${compact ? 'text-sm' : ''}`} aria-disabled="true">
    <Presentation size={18} aria-hidden="true" /> Lesson {n} teacher slides: <strong className="font-semibold">coming soon</strong></span></span>
}

const tabCls = 'flex items-center gap-2 rounded-xl px-5 py-2.5 text-lg font-semibold text-slate-600 transition data-[state=active]:bg-white data-[state=active]:text-blue-700 data-[state=active]:shadow-sm hover:text-slate-900'

function LessonPage() {
  const { n, tab } = useParams()
  const lesson = content.lessons.find(l => String(l.n) === n)
  if (!lesson) return <Navigate to="/" replace />
  const active = tab === 'teacher' ? 'teacher' : 'student'
  const prev = content.lessons.find(l => l.n === lesson.n - 1), next = content.lessons.find(l => l.n === lesson.n + 1)
  return (<>
    <div className="mb-6 flex flex-wrap items-end justify-between gap-4">
      <div>
        <div className="text-sm font-semibold uppercase tracking-wide text-blue-700">Lesson {lesson.n} · Week {lesson.week}</div>
        <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">{lesson.title}</h1>
        <p className="mt-1 text-lg text-slate-600">{lesson.grammar}</p>
      </div>
      <button onClick={() => window.print()} className="btn no-print border border-slate-300 bg-white text-slate-700 hover:bg-slate-50"><Printer size={18} aria-hidden="true" /> Print this tab</button>
    </div>
    <Tabs.Root value={active} onValueChange={v => { window.location.hash = `#/lesson/${lesson.n}/${v}` }}>
      <Tabs.List aria-label="Lesson sections" className="no-print mb-6 inline-flex gap-1 rounded-2xl bg-slate-100 p-1.5">
        <Tabs.Trigger value="student" className={tabCls}><Users size={20} aria-hidden="true" /> Student</Tabs.Trigger>
        <Tabs.Trigger value="teacher" className={tabCls}><Presentation size={20} aria-hidden="true" /> Teacher</Tabs.Trigger>
      </Tabs.List>
      <Tabs.Content value="student" className="outline-none">
        <nav aria-label="On this page" className="no-print mb-2 flex flex-wrap gap-2">
          {[['words', 'New Words'], ['listening', 'Listening'], ['grammar', 'Grammar'], ['homework', 'Homework']].map(([id, t]) =>
            <a key={id} href={`#${id}`} onClick={e => { e.preventDefault(); document.getElementById(id)?.scrollIntoView({ behavior: 'smooth' }) }}
              className="rounded-full bg-blue-50 px-4 py-1.5 font-medium text-blue-800 hover:bg-blue-100">{t}</a>)}
        </nav>
        <SectionTitle id="words" icon={<Star size={20} />}>New Words</SectionTitle>
        <WordCards lesson={lesson} />
        <div className="page-break" />
        <SectionTitle id="listening" icon={<Headphones size={20} />}>Listening</SectionTitle>
        <Card><AudioPlayer lesson={lesson} /><Html html={lesson.listening} /></Card>
        <div className="page-break" />
        <SectionTitle id="grammar" icon={<MessageSquareText size={20} />}>Grammar</SectionTitle>
        <Card><Html html={lesson.grammarHtml} /></Card>
        <div className="page-break" />
        <SectionTitle id="homework" icon={<NotebookPen size={20} />}>Homework</SectionTitle>
        <Card><Html html={lesson.homework} /></Card>
      </Tabs.Content>
      <Tabs.Content value="teacher" className="outline-none">
        <Card className="mb-6 bg-emerald-50/60"><div className="flex flex-wrap items-center gap-3">
          <span className="font-semibold text-emerald-900">Teacher materials:</span>
          <SlidesLink n={lesson.n} />
          {lesson.audio
            ? <a href={lesson.audio} download className="btn no-print border border-slate-300 bg-white text-slate-700 hover:bg-slate-50"><FileAudio size={18} aria-hidden="true" /> Listening MP3</a>
            : <span className="inline-flex items-center gap-2 rounded-xl border border-dashed border-amber-300 bg-amber-50 px-4 py-2 text-amber-900"><FileAudio size={18} aria-hidden="true" /> Audio coming soon: read the script aloud</span>}
        </div></Card>
        <Card><Html html={lesson.teacher} className="teacher" /></Card>
      </Tabs.Content>
    </Tabs.Root>
    <nav aria-label="Lessons" className="no-print mt-10 flex justify-between gap-4 text-lg">
      {prev ? <Link className="link inline-flex items-center gap-1" to={`/lesson/${prev.n}`}><ArrowLeft size={18} aria-hidden="true" /> Lesson {prev.n}</Link> : <Link className="link inline-flex items-center gap-1" to="/"><ArrowLeft size={18} aria-hidden="true" /> Home</Link>}
      {next ? <Link className="link inline-flex items-center gap-1" to={`/lesson/${next.n}`}>Lesson {next.n} <ArrowRight size={18} aria-hidden="true" /></Link> : <Link className="link inline-flex items-center gap-1" to="/downloads">Downloads <ArrowRight size={18} aria-hidden="true" /></Link>}
    </nav>
  </>)
}

function DlRow({ href, icon, title, meta }: { href: string; icon: JSX.Element; title: string; meta: string }) {
  return <a href={href} download className="flex items-center gap-4 rounded-2xl border border-slate-200 bg-white p-4 shadow-sm transition hover:border-blue-400 hover:shadow-md">
    <span className="grid size-12 shrink-0 place-items-center rounded-xl bg-blue-50 text-blue-700" aria-hidden="true">{icon}</span>
    <span><span className="block text-lg font-semibold text-slate-900">{title}</span><span className="text-slate-600">{meta}</span></span>
    <Download className="ml-auto text-slate-400" aria-hidden="true" /></a>
}

const noAudioRange = () => {
  const ns = content.lessons.filter(l => !l.audio).map(l => l.n)
  return ns.length > 1 && ns[ns.length - 1] - ns[0] === ns.length - 1 ? `${ns[0]}–${ns[ns.length - 1]}` : ns.join(', ')
}

function DownloadsPage() {
  const { pdf, docx } = content.downloads
  return (<>
    <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">Downloads</h1>
    <SectionTitle icon={<FileText size={20} />}>Full curriculum (Version 5, public edition)</SectionTitle>
    <p className="mb-4 text-lg text-slate-700">Program guide, teacher plans, student workbook for Lessons 1–13, review pages, and the midterm and final exam packets in one document. Print the student workbook part for learners.</p>
    <div className="grid gap-3 md:grid-cols-2">
      <DlRow href={`downloads/${pdf}`} icon={<FileText />} title="PDF, for printing" meta={mb(sizes[pdf])} />
      <DlRow href={`downloads/${docx}`} icon={<FileText />} title="Word document (DOCX), for editing" meta={mb(sizes[docx])} />
    </div>
    <SectionTitle icon={<Headphones size={20} />}>Listening audio</SectionTitle>
    <p className="mb-4 text-lg text-slate-700">Each file has a short intro and plays the conversation once. Play the audio again if needed. Play from a phone and a small speaker.</p>
    <div className="grid gap-3 md:grid-cols-2">
      {content.lessons.filter(l => l.audio).map(l => <DlRow key={l.n} href={l.audio} icon={<FileAudio />} title={`Lesson ${l.n}: ${l.title}`} meta={`MP3 · ${mb(sizes[`L${l.n}_listening.mp3`])}`} />)}
    </div>
    {content.lessons.some(l => !l.audio) && <p className="mt-3 text-lg text-slate-700"><strong>Lessons {noAudioRange()}:</strong> audio coming soon. Until then, read the listening script aloud (Teacher tab of each lesson).</p>}
    <SectionTitle icon={<Presentation size={20} />}>Teacher slides</SectionTitle>
    <p className="mb-4 text-lg text-slate-700"><strong>Present</strong> opens the slides in a new browser tab: click or press Space / → for the next step, ← to go back, F for full screen, N for notes. Works offline once the page has loaded.</p>
    <div className="grid gap-3">{content.lessons.map(l => <div key={l.n} className="flex flex-wrap items-center gap-3"><span className="w-24 font-semibold text-slate-800">Lesson {l.n}</span><SlidesLink n={l.n} /></div>)}</div>
    <SectionTitle icon={<ClipboardCheck size={20} />}>Exams (teachers)</SectionTitle>
    <p className="mb-4 text-lg text-slate-700">Midterm (Week 8) and Final Exam (Week 15): teacher packets with answer keys, plus student tests to print. <Link className="link font-semibold" to="/exams">Go to the Exams page →</Link></p>
    <SectionTitle icon={<Printer size={20} />}>Print a lesson</SectionTitle>
    <p className="text-lg text-slate-700">Open a lesson, choose the Student or Teacher tab, and press <strong>Print this tab</strong>. Menus and audio players are hidden on paper.</p>
  </>)
}

const EXAMS = [
  { id: 'midterm', week: 'Week 8: Midterm', scope: 'Lessons 1–7', prefix: 'Midterm', packet: 'Midterm_Exam_Teacher_Packet', student: 'Midterm_Student_Test', audio: 'Midterm_listening.mp3' },
  { id: 'final', week: 'Week 15: Final Exam', scope: 'Lessons 1–13', prefix: 'Final exam', packet: 'Final_Exam_Teacher_Packet', student: 'Final_Student_Test', audio: 'Final_listening.mp3' },
]
const fileMeta = (f: string, kind: string) => sizes[f] ? `${kind} · ${mb(sizes[f])}` : kind

function ExamsPage() {
  const loc = useLocation()
  useEffect(() => {
    if (!loc.hash) return
    const t = window.setTimeout(() => document.getElementById(loc.hash.slice(1))?.scrollIntoView({ behavior: 'smooth' }), 50)
    return () => window.clearTimeout(t)
  }, [loc.hash])
  return (<div className="max-w-4xl">
    <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">Exams</h1>
    <p className="mt-2 text-lg text-slate-700">Week 8: Midterm (Lessons 1–7) and Week 15: Final Exam (Lessons 1–13). For teachers. Print the student tests separately.</p>
    {EXAMS.map(e => (
      <section key={e.id} id={e.id} className="scroll-mt-24">
        <SectionTitle icon={<ClipboardCheck size={20} />}>{e.week}</SectionTitle>
        <Card>
          <p className="mb-4 text-lg text-slate-700">Review stations + exam ({e.scope}). The teacher packet has the teacher plan, listening script, speaking interview card and rubric, task cards, listening and grammar tests, score sheet, can-do self-check, and answer key.</p>
          <div className="grid gap-3 md:grid-cols-2">
            <DlRow href={examPath(`${e.packet}.pdf`)} icon={<FileText />} title={`${e.prefix} teacher packet (PDF)`} meta={fileMeta(`${e.packet}.pdf`, 'PDF, for printing')} />
            <DlRow href={examPath(`${e.packet}.docx`)} icon={<FileText />} title={`${e.prefix} teacher packet (Word)`} meta={fileMeta(`${e.packet}.docx`, 'DOCX, for editing')} />
            <DlRow href={examPath(`${e.student}.pdf`)} icon={<Printer />} title={`${e.prefix} student test (PDF, no answers)`} meta={fileMeta(`${e.student}.pdf`, 'Print for learners')} />
          </div>
          {sizes[e.audio]
            ? <div className="audio-box my-4 rounded-2xl bg-blue-50 p-4 ring-1 ring-blue-100">
                <div className="mb-2 flex items-center gap-2 font-semibold text-blue-900"><Headphones size={20} aria-hidden="true" /> {e.prefix} listening audio</div>
                <audio controls preload="none" src={`audio/${e.audio}`} className="no-print w-full">Your browser cannot play audio.</audio>
              </div>
            : <div className="mt-4 flex items-start gap-3 rounded-2xl bg-amber-50 p-4 text-amber-950 ring-1 ring-amber-200">
                <Headphones size={20} className="mt-0.5 shrink-0" aria-hidden="true" />
                <p><strong>Listening audio coming soon:</strong> read the script aloud. The script is in the teacher packet.</p>
              </div>}
        </Card>
      </section>))}
    <SectionTitle icon={<PartyPopper size={20} />}>Week 16: Graduation</SectionTitle>
    <Card><p className="text-lg text-slate-700">Certificates, 1-minute graduation talks (prepared in Lesson 13), and a celebration. No new content and no downloads. Talks are optional: learners can read from their paper, speak with a partner, or say two sentences.</p></Card>
    <div className="mt-8 flex items-start gap-3 rounded-2xl border-l-4 border-amber-400 bg-amber-50 p-5 text-lg text-amber-950">
      <AlertTriangle size={22} className="mt-1 shrink-0" aria-hidden="true" />
      <p>Learners prepare with the Week 8 / Week 15 Review pages in their workbook. Keep teacher packets away from learners (they contain answer keys).</p>
    </div>
  </div>)
}

function AboutPage() {
  return (<div className="max-w-3xl">
    <h1 className="text-3xl font-extrabold tracking-tight text-slate-900 sm:text-4xl">About &amp; Credits</h1>
    <p className="mt-4 text-lg text-slate-700">This is a free curriculum for Level 2 (high-beginner) adult English classes, written by volunteers for community programs. It focuses on practical daily life: work, family, health, shopping, and community services.</p>
    <SectionTitle icon={<FileText size={20} />}>License for our materials</SectionTitle>
    <p className="text-lg text-slate-700">© 2026 the authors. The authors license the lesson text, teacher plans, workbook pages, original drawings (calendars, clock, timeline, phone frame, arrows, lines, labels), and audio files under <a className="link" href={LICENSE_URL}>Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)</a>. You may share and adapt them for noncommercial purposes, with credit, and you must share adaptations under the same license. Program names and logos are not covered by this license. Third-party parts listed below keep their own licenses.</p>
    <SectionTitle icon={<Star size={20} />}>Picture credits</SectionTitle>
    <blockquote className="rounded-r-2xl border-l-4 border-blue-500 bg-blue-50 p-5 text-lg text-slate-800" dangerouslySetInnerHTML={{ __html: content.creditHtml }} />
    <p className="mt-4 text-lg text-slate-700">The vocabulary pictures are modified versions of the original Twemoji graphics: the SVGs were rendered to PNG, resized, and combined with other emoji on a white card with a border, and some cards have added arrows, lines, calendars, clocks, or text labels. The Twemoji parts remain under CC BY 4.0. Text labels use the DejaVu Sans font (free font license). No photos or stock images are used.</p>
    <SectionTitle icon={<Headphones size={20} />}>Audio</SectionTitle>
    <p className="text-lg text-slate-700">The listening audio was made with the free Chatterbox text-to-speech model by Resemble AI (MIT License). The voices are synthetic, not real people, and each file carries an inaudible Perth watermark that marks it as AI-generated. The short voice reference clips Chatterbox used were made with Kokoro-82M (Apache 2.0).</p>
    <SectionTitle icon={<Presentation size={20} />}>Fonts</SectionTitle>
    <p className="text-lg text-slate-700">The teacher slides and the in-browser presenter use the Lexend Deca font by The Lexend Project Authors, licensed under the <a className="link" href="https://openfontlicense.org">SIL Open Font License 1.1</a>.</p>
    <SectionTitle icon={<FileText size={20} />}>Disclaimer</SectionTitle>
    <p className="text-lg text-slate-700">These materials are provided as-is for educational use, without warranty of any kind.</p>
  </div>)
}

export default function App() {
  const loc = useLocation()
  if (loc.pathname.startsWith('/present/')) return (
    <Suspense fallback={<div style={{ background: '#1b2236', position: 'fixed', inset: 0 }} />}>
      <Routes><Route path="/present/:n" element={<Presenter />} /></Routes>
    </Suspense>)
  return (<div className="flex min-h-screen flex-col bg-slate-50/40">
    <a href="#main" onClick={e => { e.preventDefault(); document.getElementById('main')?.focus() }} className="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:z-50 focus:rounded-lg focus:bg-white focus:p-3">Skip to content</a>
    <Header />
    <main id="main" tabIndex={-1} className="mx-auto w-full max-w-6xl flex-1 px-4 py-8 outline-none sm:py-10">
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/lesson/:n" element={<LessonPage />} />
        <Route path="/lesson/:n/:tab" element={<LessonPage />} />
        <Route path="/lessons" element={<LessonsPage />} />
        <Route path="/downloads" element={<DownloadsPage />} />
        <Route path="/exams" element={<ExamsPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </main>
    <Footer />
  </div>)
}
