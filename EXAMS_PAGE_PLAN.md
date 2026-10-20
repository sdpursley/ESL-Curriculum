# Plan: teacher "Exams" page (prepared, NOT built or published)

Status: design only. No code, routes, or dist changes yet. The v5 lessons and exam files stay off the site until approved.

## Where it goes
- **New route** `#/exams` (`ExamsPage` in `src/App.tsx`), added to `NAV` after "Downloads" with the `ClipboardCheck` icon (lucide-react), label **"Exams"**.
- **Downloads page**: new section "Exams (teachers)" between "Teacher slides" and "Print a lesson", linking to `#/exams`.
- **Home page** "For teachers" card: a one-line link "Midterm (Week 8) and Final Exam (Week 15) packets →".
- **Semester table** on Home: make the Week 8 and Week 15 rows link to `#/exams#midterm` / `#/exams#final`.

## Files (copy into `public/downloads/exams/` when approved)
| Link text | File (source: `/workspace/level2_curriculum/exams/`) | Audience |
|---|---|---|
| Midterm teacher packet (PDF) | `Midterm_Exam_Teacher_Packet.pdf` | Teachers |
| Midterm teacher packet (Word) | `Midterm_Exam_Teacher_Packet.docx` | Teachers (editing) |
| Midterm student test (PDF, no answers) | `Midterm_Student_Test.pdf` | Print for learners |
| Final exam teacher packet (PDF) | `Final_Exam_Teacher_Packet.pdf` | Teachers |
| Final exam teacher packet (Word) | `Final_Exam_Teacher_Packet.docx` | Teachers (editing) |
| Final student test (PDF, no answers) | `Final_Student_Test.pdf` | Print for learners |
| Midterm / Final listening audio | `audio/Midterm_listening.mp3`, `audio/Final_listening.mp3` | Classroom |

## Page layout
1. **H1 "Exams"** + one line: "Week 8: Midterm (Lessons 1–7) and Week 15: Final Exam (Lessons 1–13). For teachers. Print the student tests separately."
2. **Card "Week 8: Midterm"** (anchor `#midterm`): what's in the packet (teacher plan, listening script, interview card + rubric, task cards, listening and grammar tests, score sheet, self-check, answer key) · 3 download rows (DlRow) · audio player (when the MP3 exists, else "audio coming soon: read the script aloud").
3. **Card "Week 15: Final Exam"** (anchor `#final`): same structure.
4. **Card "Week 16: Graduation"**: short text (1-minute talks, certificates); no downloads.
5. **Note box**: "Learners prepare with the Week 8 / Week 15 Review pages in their workbook. Keep teacher packets away from learners (they contain answer keys)."
6. Footer unchanged (© 2026 the authors · CC BY-NC-SA 4.0 · disclaimer).

## Build steps (later)
1. `cp ../exams/*.pdf ../exams/*.docx public/downloads/exams/`
2. Add `ExamsPage`, route, NAV entry, and Downloads/Home links; `sizes` map entries for the new files.
3. `npm run build`, then check the links and that the PDFs open.
