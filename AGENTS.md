# AGENTS.md: how to build and check new lessons, audio, and exams

This file is for anyone who continues this curriculum without the owner at the keyboard: another AI coding tool or a person.
Follow it exactly. When this file and another doc disagree, this file wins for the rules, and [MAINTAINING.md](MAINTAINING.md) has the longer how-to.
All commands run from the repository root unless a step says `cd`.

**Get the owner's approval before you publish anything** (before merging into `main`: a push to `main` deploys the public website).

**Contents:** [1. Project layout](#1-project-layout) · [2. Content rules](#2-content-rules) · [3. Audio rules](#3-audio-rules) · [4. Audio check rules](#4-audio-check-rules) · [5. Step by step: add a lesson](#5-step-by-step-add-a-lesson-example-level-1-lesson-n-level-3-is-the-same-with-level3--l3) · [6. Slide decks (all levels)](#6-slide-decks-all-levels) · [7. Running audio locally](#7-running-audio-locally-level-3-lessons-213-drafts) · [8. Never commit](#8-never-commit) · [9. Repository rules](#9-repository-rules)

---

## 1. Project layout

The repository is a Vite + React + TypeScript website (HashRouter, deployed to GitHub Pages by `.github/workflows/pages.yml`)
plus the sources and build scripts for three levels of a 5-level adult ESL progression. Levels 4 and 5 are only planned (`Five_Level_Map.md`).

| What | Level 1 (beginner) | Level 2 (high beginner) | Level 3 (low intermediate) |
|---|---|---|---|
| Lesson text (source) | `level1/curriculum/Level1_Lesson<N>.md` (13 lessons) | `curriculum/Level2_Curriculum_v5_public.md` (one book, 13 lessons + exams) | `level3/curriculum/Level3_Lesson<N>.md` |
| Plan for the semester | `level1/curriculum/Level1_Scope_and_Sequence.md` (the website reads the lesson list, weeks, semester table, routine here) | inside the book | `level3/curriculum/Level3_Scope_and_Sequence.md` |
| DOCX + PDF build | `level1/curriculum/build.sh <N> [--publish]` (uses `md2docx_L1.py`) | `curriculum/build.sh` (uses `md2docx.py`, `packets.py`) | `level3/curriculum/build.sh <N> [--publish]` (uses `md2docx_L3.py`) |
| Exams | `level1/exams/` (Markdown, `images/`, `audio/`, `build/`); build: `level1/exams/build/build_all.sh [--publish]` | cut out of the book by `curriculum/build.sh` into `public/downloads/exams/` | not built yet |
| Pictures | `level1/images/` (+ `CREDITS.md`); scripts `level1/images/tools/make_images_L1.py`, `make_images_L1_L<N>.py`, helpers `level1/images/tools/lib/` | `public/images/` (+ `CREDITS.md`); scripts `tools/images/` | `level3/images/` (+ `CREDITS.md`); scripts `level3/images/tools/make_images_L3_L<N>.py` |
| Listening audio | `level1/audio/` (MP3 + check results + READMEs); Lesson 1 scripts `level1/audio/tools/`; Lessons 2–13 and exams use the shared builder `level1/audio/tools/lessons/` | `public/audio/`; scripts `tools/audio/` (`processor.py`, `asr_check*.py`) | `level3/audio/`; scripts `level3/audio/tools/` (`build_L3_L<N>.py`, `check_L3_L<N>.py`, `script_L3_L<N>.py`) |
| Level 3 drafts (Lessons 2–13, not on the website) | | | `level3/drafts/` (`curriculum/`, `images/`, `audio/`, `audio/tools/`); status `level3/AUDIO_STATUS.md`; see section 7 |
| Voice reference clips | `tools/audio/samples/refs/*.wav` and `level1/audio/tools/natural/kokoro_refs/af_jessica.wav` (list: `level1/audio/tools/lessons/REFS.md`) | `tools/audio/samples/refs/` | `tools/audio/samples/refs/` |
| Slide decks (source) | `level1/slides/Level1_Lesson<N>_Slides.pptx` | `public/downloads/slides/Lesson<N>_Slides.pptx` | `level3/slides/Level3_Lesson<N>_Slides.pptx` |
| Website files (generated, don't edit by hand) | `public/level1/` (images, audio, downloads, downloads/slides, downloads/exams) | `public/images/`, `public/audio/`, `public/downloads/` | `public/level3/` |
| Website data (generated) | `src/content_level1.json`, `src/decks/level1/lesson<N>.json` | `src/content.json`, `src/sizes.json`, `src/decks/lesson<N>.json` | `src/content_level3.json`, `src/decks/level3/lesson<N>.json` |
| Page code | `src/level1.tsx` | `src/App.tsx` | `src/level3.tsx` |

Shared scripts:

- `scripts/export_content.py`: writes all the website data (`src/content*.json`, `src/sizes.json`) and copies the Level 1 / Level 3 pictures, MP3s, and PPTX from `level1/`, `level3/` into `public/level1/`, `public/level3/`. It also copies the Level 1 exam MP3s and lists the exam files. It rebuilds Level 2 data too; unchanged sources give byte-identical files.
- `scripts/export_deck.py <pptx> <N> [--level 1|3]`: PowerPoint deck → presenter JSON. It stops if a picture in the deck is not identical to a file in the level's `public/.../images/`.
- `scripts/check_slides.py <pptx ...>`: every click animation targets a shape that exists.
- `scripts/slides/`: the slide deck tools (build a deck from a lesson spec, inspect, check, render, compare). See section 6.
- `scripts/md_parser.py`: Markdown → page HTML (used by `export_content.py`).

Python environments (not committed): `.venv-docs` (`tools/requirements-docs.txt`), `.venv-img` (`tools/images/requirements.txt`: Pillow, cairosvg),
`.venv-audio` (Python 3.11, `tools/audio/requirements.txt`: Chatterbox, faster-whisper; CPU PyTorch). System: LibreOffice (`soffice`), poppler-utils, ffmpeg, DejaVu fonts.

---

## 2. Content rules

**Course shape**

- 5-level progression. Each level is one 16-week semester with **13 lessons**: **Week 8 = midterm**, **Week 15 = final exam**, **Week 16 = graduation** (no new content).
- Class time: **6:00–6:45**, then a break, then **7:00–7:30**. **Level 1 uses 7:15–7:30 for literacy** (letters, numbers, copying, reading).
- Teacher plans give clock times for every step.

**Learners and teachers**

- Adult learners. About 95% speak Spanish, but write for all languages.
- **Level 1:** every student instruction has an English line, a Spanish line, and a `My language: ____` line.
- **Level 3:** no Spanish lines.
- Teachers are volunteers, not experts. Write every step so a first-time volunteer can teach it, and do not require Spanish.
- Lots of pair and group work.
- Grammar goes in **two-sided Q&A boxes** (question side / answer side).
- **Every vocabulary word has a picture:** a Twemoji graphic (CC BY 4.0, https://github.com/jdecked/twemoji) or our own drawing made in code. List every picture in the level's `CREDITS.md`.

**Look**

- No instruction icons and no decorative emoji in lessons, tests, or slides. The only allowed faces are the self-check faces 😀 🙂 😐.
- Tests have **no cover page**.

**Keys**

- Every item is keyed.
- The student pages, the teacher steps, and the answer key must agree, item by item (count, order, answers, points).
- For the exams, `level1/exams/build/check_consistency.py` checks this.

**What must not appear**

- No religious content (holidays, places of worship, prayers, scripture).
- Do not call the curriculum secular.
- Do not name or refer to any other ESL program, curriculum, publisher, or test.
- Keep the line **"© 2026 the authors"** (license CC BY-NC-SA 4.0).
- Make no copyright-registration claims.
- All names, stores, prices, phone numbers, and addresses are invented.

**Publishing:** get the owner's approval first.

---

## 3. Audio rules

**Voices**

- **Chatterbox TTS only** (Resemble AI, MIT License; CPU).
- Every voice is a Chatterbox clone of a committed **synthetic Kokoro-82M reference clip** (Apache 2.0). The clips are listed in `level1/audio/tools/lessons/REFS.md`, and `tools/audio/make_refs.py` makes them.
- Never use recordings of real people, LibriVox or LibriTTS data, Piper voices, or Chatterbox's built-in default voice. `level1/audio/tools/lessons/engine.py` refuses any other reference file.
- Female characters get female voices, and male characters get male voices.

**Character → reference clip (Kokoro voice)**

Level 1, Lesson 1 (`level1/audio/tools/`):

| Character | Clip (Kokoro voice) |
|---|---|
| Narrator | `N` (af_sarah) |
| Receptionist | `Receptionist` (af_river) |
| Ana | `af_jessica` (`level1/audio/tools/natural/kokoro_refs/af_jessica.wav`) |
| Carlos | `Sam` (am_michael) |

Level 1, Lessons 2–13 and exams (`script_L1_L<N>.py`, `level1/exams/build/audio/script_L1_<Midterm|Final>.py`):

| Character | Clip (Kokoro voice) | Where |
|---|---|---|
| Narrator | `N` (af_sarah) | all |
| Rosa | `Rosa` (af_heart) | L2, L5, L10, L12 |
| Marco | `Marco` (am_adam) | L2, L5, L9, L11, L12, Midterm |
| Receptionist | `Receptionist` (af_river) | L3, L6, L9, Midterm |
| Operator | `Receptionist` (af_river) | L12 |
| Kim | `Kim` (af_nova) | L4, L6, L9, Final |
| Carlos | `Sam` (am_michael) | L4, Final |
| Manager | `Sam` (am_michael) | L13 |
| Phone message | `Server` (am_puck) | L6 |
| Server | `Server` (am_puck) | L8 |
| Cashier | `Carlos` (am_eric) | L7 |
| Agent | `Agent` (af_kore) | L10 |
| Ana | `Ana_af_jessica` (af_jessica) | L3, L7, L8, L11, L12, L13 |

`tools/audio/samples/refs/Ana.wav` is the Level 2 Ana clip; Level 1 Ana always uses af_jessica.

Level 3 (`level3/audio/tools/build_L3_L<N>.py`):

| Character | Clip (Kokoro voice) |
|---|---|
| Narrator | `N` (af_sarah) |
| Elena | `Rosa` (af_heart) |
| David | `Sam` (am_michael) |

Level 2: `tools/audio/processor.py` (`VOICES`), clips in `tools/audio/samples/refs/`.

**Settings**

- Levels 1 and 3 use **exaggeration 0.72** and **cfg 0.32** (`EXAG=0.72 CFG=0.32`). The exceptions are the Level 1 Lesson 1 narrator and receptionist (0.55/0.45) and the Level 3 Lesson 1 narrator (0.55/0.40).
- Make each sentence as one **whole-sentence take**. Try several seeds and keep the best take that passes.
- Pauses: **1.3–1.5 s** between speakers (`PAUSE_SPK`, default 1.4).
- Level 2's files used **0.55 / 0.45** (the `processor.py` defaults). Do not re-make Level 2 audio with the Level 1 settings by accident.

**Length**

- The file has a short intro, plays the conversation **once**, then ends ("That's the end of the listening.").
- Level 1: about 1:00–1:20.
- Level 3: up to about 1:30, with up to 3 speakers.
- Write the real length ("about 1:17") in the listening-script heading of the lesson Markdown. For the exams, `make_exam_md.py` reads it from `level1/exams/audio/L1_<Midterm|Final>_check_results.json`, so run `build_all.sh --publish` again after new audio.

**Hard names**

- If Chatterbox says a name wrong, change the spelling in the **voice text only**, so it reads the way it sounds (`tts` text / `SAME` map in the script file).
- Keep the real spelling in the Markdown and the student pages.

## 4. Audio check rules

**Checkers**

- Use **Whisper small.en plus Whisper medium.en** (faster-whisper).
- Run faster-whisper with `compute_type='float32'` and `cpu_threads=1` for the deciding check (`vote_takes.py`).
- int8 with several threads gives different text from run to run when the machine is busy. All Level 1 checkers set `cpu_threads=1`.

**Pass / retake**

- A line **passes if EITHER checker hears it exactly** (after `canon.py` normalizes numbers, prices, times, and dates), **its pitch is in range** (male voices under about 150 Hz median, female voices clearly higher), and it has **no clipping**.
- **Retake a line only when both checkers fail it**, or for pitch, or for clipping.
- `vote_takes.py` runs each checker 3 times on each chosen take. A take is OK if either checker is exact in most of its runs.
- **Spelled letters ("L, I, M, A.") and digit strings always score low.** Check those lines by ear.
- Always listen to the whole file once before publishing.

**Memory**

- **Only one Chatterbox or Whisper process at a time.** Two at once ran out of memory on a 15 GB machine.
- Wrap every run in `flock` on one lock file. Example: `flock /tmp/chatterbox.lock .venv-audio/bin/python ...`. The exam scripts do this with `LOCK=/tmp/chatterbox.lock`.
- Expect **about 20–30 minutes per lesson** on CPU (build plus checks).

**Tools** (`level1/audio/tools/lessons/`)

| Script | What it does |
|---|---|
| `build_listening.py` | Build the file |
| `check_listening.py` | Whole-file check: small.en, pitch, clipping, loudness, pauses |
| `second_opinion.py` | medium.en, whole file |
| `second_opinion_lines.py` | medium.en, line by line |
| `verify24.py` | Lines on the 24 kHz WAV |
| `takes_medium.py` | medium.en on each chosen take |
| `vote_takes.py` | The deciding vote |
| `script_match.py` | The Markdown script and the `script_*.py` file must match |

The repo's `tools/audio/processor.py` is the one to use (resampling, trimming, silence). Some older working copies of `processor.py` had extra engines (Piper, Kitten). They are not supported and must not come back.

---

## 5. Step by step: add a lesson (example: Level 1 Lesson N; Level 3 is the same with `level3` / `L3`)

1. **Content.** Copy the previous lesson to `level1/curriculum/Level1_Lesson<N>.md`.
   - Take the title and week from the scope and sequence, and write the lesson. Keep the `<!-- part: Teacher Plan -->` / `<!-- part: Student Workbook -->` comments and the heading pattern (`## Lesson N (Week W): ...`, `## Lesson N (Week W) · New Words`, `## Lesson N (Week W) · Listening`, …, `## Picture Credits`).
   - Line 4 is the status line: `**Status:** Complete lesson (all 13 Level 1 lessons are published).`
   - Follow every content rule in section 2.
   - Check the keys: student items = teacher steps = answer key.
2. **Pictures.** Write `level1/images/tools/make_images_L1_L<N>.py` (copy the previous one; helpers in `tools/lib/make_images.py`).
   - Run `cd level1/images/tools && ../../../.venv-img/bin/python make_images_L1_L<N>.py`.
   - Link each picture as `images/L1_L<N>_<word>.png`.
   - Draft the credits with `tools/lib/make_credits.py N ../..` and paste the lesson's section into `level1/images/CREDITS.md`.
3. **DOCX/PDF.**
   - Look first: `PYTHON=.venv-docs/bin/python level1/curriculum/build.sh <N>` writes to `level1/curriculum/build/`.
   - Publish: add `--publish` to write to `public/level1/downloads/`.
   - Read the PDF: check the page breaks, every picture is there, and no empty pages.
4. **Audio.**
   - Write `level1/audio/tools/lessons/script_L1_L<N>.py` (`VOICES`, `INTRO`, `LINES`, `OUTRO`; female characters → female clips).
   - Run `python3 script_match.py ../../../curriculum/Level1_Lesson<N>.md script_L1_L<N>.py` and get 0 mismatches.
   - Build and check under the lock:
     ```bash
     cd level1/audio/tools/lessons
     L="flock /tmp/chatterbox.lock ../../../../.venv-audio/bin/python"
     $L build_listening.py script_L1_L<N>.py $PWD/out/L1_L<N>_listening
     $L check_listening.py script_L1_L<N>.py out/L1_L<N>_listening.mp3 out/L1_L<N>_listening_log.json out/L1_L<N>_check_results.json
     $L second_opinion_lines.py script_L1_L<N>.py out/L1_L<N>_listening.mp3 out/L1_L<N>_listening_log.json
     $L vote_takes.py script_L1_L<N>.py out/L1_L<N>_listening_log.json 3
     ```
5. **Checks.**
   - Apply section 4. To retake a line, add `EXCLUDE='{"<sentence>": [<seed>]}'` and build again (the other takes come from `cache/`).
   - Listen to the whole file.
   - Copy into `level1/audio/`:
     - `out/L1_L<N>_listening.mp3`
     - the log, as `L1_L<N>_regen_log.json`
     - the check results, as `L1_L<N>_check_results.json`
   - Write `L1_L<N>_README.md`: voices, settings, results, and the vote line.
   - Put the real length in the Markdown.
6. **Slides.** Make or edit `level1/slides/Level1_Lesson<N>_Slides.pptx` (Level 3 and up: build it with `scripts/slides/build_deck.py`). **Follow section 6** for the format, the notes, and the checks. **Presenter rules:**
   - Each slide title is in the **top title box**, and it is the largest text on the slide. The presenter takes the title from there.
   - **Every click animation targets a shape that exists on that slide.** Check with `python3 scripts/check_slides.py level1/slides/Level1_Lesson<N>_Slides.pptx`.
   - **Answers appear on click.** Questions show first; each answer is an "on click" entrance animation. Each click = one reveal step.
   - Every picture in the deck is byte-identical to a file in `level1/images/`.
   - No decorative emoji or instruction icons.
7. **Site export.**
   - Run `python3 scripts/export_deck.py level1/slides/Level1_Lesson<N>_Slides.pptx <N> --level 1`.
   - Then run `python3 scripts/export_content.py`.
   - If you did not change Level 2, `git status` must show no change to `src/content.json`, `src/sizes.json`, or `src/decks/lesson*.json`. If it does, `git checkout --` them and find out why.
8. **Build.** `npm ci` (once), then `npm run build`. It must pass.
9. **Preview checks.** Run `npm run preview` and open `http://localhost:4173/`. Check:
   - `#/level1/lesson/<N>/student`, `/teacher`, and `/downloads`.
   - `#/level1/present/<N>`: click through every slide. Answers appear on click, there are no empty or stuck steps, and the counter ends on the last slide.
   - `#/level1/downloads`, `#/level1/exams`, and the Level 2 and Level 3 pages.
   - No browser console errors, and every image, PDF, DOCX, PPTX, and MP3 link returns 200.
10. **PR.** Follow section 9 and ask the owner for approval before you merge.

**Exams (Level 1 Week 8 Midterm, Week 15 Final)**

- The items live in `level1/exams/build/exam_data.py`.
- `make_exam_md.py` writes the four Markdown files.
- `build_all.sh` makes pictures → Markdown → DOCX/PDF, then runs `check_consistency.py`, which must report 0 failed.
- `build_all.sh --publish` copies the teacher packets (PDF + DOCX) and the student tests (PDF) into `public/level1/downloads/exams/`.
- Audio:
  - `cd level1/exams/build/audio`
  - `bash run_audio.sh Midterm` (Chatterbox)
  - `bash finish_audio.sh Midterm` (all checks plus the vote; copies the MP3, JSON, and README into `level1/exams/audio/`)
  - To retake a line: `EXCLUDE='{"<sentence>": [<seed>]}' bash run_audio.sh Midterm`, then `finish_audio.sh` again.
- Then run `python3 scripts/export_content.py`. The website reads the parts table from the teacher packet.
- Set `IMGPY=.venv-img/bin/python` for the pictures.
- `BANNED_EXTRA="word1,word2"` adds words to the checker's banned list.

## 6. Slide decks (all levels)

This section is the complete recipe for the teacher slide decks (`.pptx`), from the lesson page to the live presenter.
It is written so that a coding agent with no other context can make a new deck that matches the published ones
**exactly in format** (same slide sizes, shapes, fonts, colors, picture boxes, click reveals, and notes style). Every
number below was measured from the published decks with `scripts/slides/inspect_deck.py`. When this text and a published
deck disagree, the deck wins: inspect it.

**Tools** (all in `scripts/slides/`; set up once with `bash scripts/slides/setup_tools.sh`, see 6.7):

| Script | What it does |
|---|---|
| `build_deck.py` | Builds `Level<V>_Lesson<N>_Slides.pptx` from the previous lesson's deck plus a lesson spec (`level<V>/slides/specs/Level<V>_Lesson<N>.py`). Levels 3, 4, 5. |
| `deckspec.py` | Helpers the specs import (`from deckspec import *`): alt text from `CREDITS.md`, word cards from the lesson's New Words table, the audio and credits wording, the listening script for the notes. |
| `inspect_deck.py` | Prints every slide's kind, shapes (id, name, position, size, fill), text runs (size, bold, color, font), click steps and notes. |
| `lesson_outline.py` | Prints the slide-relevant parts of a lesson Markdown file, in order, to write or check a spec. |
| `check_deck.py` | Rule checks on finished decks (size, slide count, click targets, pictures, emoji, Spanish, forbidden words, lesson numbers, credits line, notes style). |
| `render_deck.sh` | Renders every slide to `slide-NN.jpg` (LibreOffice + pdftoppm). |
| `contact_sheet.py` | All rendered slides on one labeled image; `--compare` puts two decks side by side. |
| `compare_decks.py` | Slide-by-slide structural comparison of two decks (shapes, geometry, text runs, picture bytes, clicks, notes). |
| `requirements.txt`, `setup_tools.sh` | Python packages (python-pptx, lxml, Pillow) and the one-time setup (LibreOffice, poppler, fonts). |

The site scripts are `scripts/check_slides.py` (click targets), `scripts/export_deck.py` (deck → presenter JSON), and `scripts/export_content.py` (site data).

### 6.1 Inputs: the lesson is the only source

- **Lesson text:** `level<V>/curriculum/Level<V>_Lesson<N>.md`. While a lesson is still a draft it may live in `level<V>/drafts/curriculum/` or on a feature branch. Published Level 3 Lessons 1–13 are in `level3/curriculum/`. Draft copies and the audio tools stay in `level3/drafts/` (section 7). A later level's drafts may be on a branch. Read a branch copy without switching: `git show origin/<branch>:level<V>/drafts/curriculum/Level<V>_Lesson<N>.md > /tmp/Level<V>_Lesson<N>.md`, then pass `--md /tmp/Level<V>_Lesson<N>.md`.
- **Pictures:** `level<V>/images/L<V>_L<N>_<name>.png` and the level's `level<V>/images/CREDITS.md` (one table row per file: file, word, what it shows, Twemoji source). The alt text of every picture on the slides is built from that row.
- **Answer keys:** the lesson's teacher plan and answer key sections. Every answer revealed on a slide must be the key's answer, word for word.
- **Everything on a slide comes from the lesson page.** Same words, same order, same item numbers, same answers, same names, same times. Never invent an item, an example, a name, a word, or an answer. If a slide needs text the lesson does not have, change the slide (fewer rows), not the content. If the lesson itself looks wrong, stop and report it; do not "fix" it on the slide.
- `python3 scripts/slides/lesson_outline.py <lesson.md>` prints the parts that go on slides (it leaves out the how-to-use pages, the clock-time table, the word list pages and the credits). `--full` also prints the speaker lines of the listening script.

### 6.2 Template and chaining: always start from an existing deck

Never build a deck from a blank presentation, and never change the theme, slide size, fonts or colors.

| You are making | Start deck (`--start`) | Fallback deck (`--fallback`, for slide kinds or parts the start deck lacks) |
|---|---|---|
| Level V, Lesson N (N ≥ 2) | `level<V>/slides/Level<V>_Lesson<N-1>_Slides.pptx` (the previous lesson) | `level<V>/slides/Level<V>_Lesson1_Slides.pptx` |
| Level V, Lesson 1 (new level) | the last deck of the level below: `level<V-1>/slides/Level<V-1>_Lesson13_Slides.pptx` (or the closest existing deck) | `level<V-1>/slides/Level<V-1>_Lesson1_Slides.pptx` |

`build_deck.py` uses exactly these defaults; for Lesson 1 of a new level you must pass `--start`. Examples: Level 4 Lesson 1 starts from `level3/slides/Level3_Lesson13_Slides.pptx` (fallback `level3/slides/Level3_Lesson1_Slides.pptx`); Level 4 Lesson 2 starts from `level4/slides/Level4_Lesson1_Slides.pptx`. Level 5 Lesson 1 starts from `level4/slides/Level4_Lesson13_Slides.pptx`.

How the builder uses them: every slide of the new deck is a **copy of the first slide of the same kind** in the start deck that has all the standard parts (for example, a `checksay` slide with its `head chip`); kinds or parts missing there come from the fallback deck. Then it rewrites the text, swaps in the lesson's own pictures, adds or removes rows, rebuilds the click animations, and writes the notes. Old slides are removed and unused parts pruned.

**Level 1 decks** (`level1/slides/`) are older, hand-made decks without kind tags or role names, and Level 1 is complete (13 decks). The builder does not handle them. To change a Level 1 deck, edit that deck in place with python-pptx (6.8.4) and keep its layout.

### 6.3 The slide sequence and the exact format

**Common format (all levels).**

- Slide size **13.333 × 7.5 in** (16:9, 12192000 × 6858000 EMU). Every slide uses the layout `DEFAULT`; there are no placeholders: every box is a free shape.
- Font **Lexend Deca** for every text run (bold for titles, numbers and labels).
- Text colors: ink **`1B2236`** (almost all text), accent purple **`5B3FC4`** (highlighted words: `*word*` in the spec), green **`1E6B45`** and red **`B42318`** (Say / Don't say marks); white text on the colored word labels.
- Fills: background **`F1F5FB`** (the credits slide uses `C9B8F2`); cards **`FFFFFF`**; card shadows **`8FAFE3`** (the same card shape offset down-left by about 0.05 in); chips and side panels **`B9D2F7`**; answer boxes and the middle check card **`C9B8F2`**; highlights and answer circles **`FFE28C`**; light panels **`DCE6F5`**. Cards are `round1Rect` / `roundRect`.
- Pictures: the lesson's PNG files (600 × 420 px cards), placed **byte-identical** (never re-encode, crop or recolor them), usually 2.1 × 1.5 in (word cards), 3.0 × 2.1 in (side pictures), 3.6–5.2 in wide (big pictures). Every picture has alt text: `Word: what it shows` from `CREDITS.md`.
- **Titles** are the largest text on the slide and sit in the top/left title box (the presenter reads the title from the largest text).
- **Click reveals:** questions and items show first; each answer, row or highlight appears **on click** (entrance animation). One click = one step. The parts of one row (card, chip, number, text) appear together: the first part is "on click", the rest "with previous". Every animation must target a shape that exists on that slide.
- Slide count: **about 24–27** (Level 1: 23–24; Level 3: 25–27).

**Level 3 sequence (the model for Levels 4 and 5).** Each slide carries its kind in `<p:cSld name="L<V>:<kind>">` and its shapes have role names (`title`, `R1 card`, `R1 ans`, …). Measured from `level3/slides/Level3_Lesson2_Slides.pptx` (26 slides):

| # | Kind | Purpose | Clicks |
|---|---|---|---|
| 1 | `title` | Lesson title, "Lesson N · Level V", "Today you will:" + 3 bullets, picture | none |
| 2 | `goals` | "Today's Goals": the lesson's "I can…" objectives, numbered 01–06 | one per row |
| 3 | `warmup` | Opening Talk (kicker "OPENING TALK · 6:00"), two instruction boxes, picture | one per box |
| 4 | `numlist` | Opening Talk cards (numbered list) | one per row |
| 5–6 | `words` ×2 | New Words: 6 picture cards each (12 words, starred words first, in the lesson's order) | one per card |
| 7 | `check` | Check the Meaning: 3 picture questions, answers on click | one per answer |
| 8 | `before` | Before You Listen: context line, picture, numbered voices, "Listen for:", audio length, "Play 1: Task A" | one per voice |
| 9–10 | `choice` ×2 | Listening A / B: statements with answer options, the right one circled on click | one per row |
| 11 | `gaps` | Listening C: gap sentences, answers on click | one per row |
| 12 | `checksay` | Say It (pronunciation lines) | one per line |
| 13–17 | `qa` / `table` (×5) | Grammar Boxes 1–5: two-sided question / answer boxes, answers on click | one per answer |
| 18–19 | `gaps`, `checksay` | Practice A / B | one per answer |
| 20 | `mistakes` | Common Mistakes: Don't say / Say, the Say side on click | one per row |
| 21 | `drill` | Pair Drill: Student A / Student B | one per side |
| 22 | `talk` | Talk Time: name, grouping, time "7:00–7:12", numbered steps | one per step |
| 23 | `go` | Before You Go "7:12–7:17": 01 Exit ticket, 02 Homework | none |
| 24 | `progress` | Progress Check "7:25": items, answers on click, "D. I can…" box with 😀 🙂 😐 | one per answer |
| 25 | `goodbye` | "Goodbye! See You Next Week!", "Now you can:" + the 3 bullets | none |
| 26 | `credits` | Credits (pictures, names and story, audio and font, © line) | none |

Other lessons add or drop a `words`/`talk`/`table`/`numlist` slide, or use `free` (a grammar box with a line, two example blocks and two side words, e.g. Level 3 Lesson 3 "used to"). Kinds: `title goals warmup numlist words check before choice gaps checksay qa table free mistakes drill talk go progress goodbye credits`.

**Level 3 shape geometry** (left, top in inches; width × height; font size in pt; all Lexend Deca; ink unless noted):

| Kind | Shapes |
|---|---|
| `title` / `goodbye` | left card (white on `8FAFE3` shadow) with `title` at (0.95, 1.45) 6.35 × 2.2, **50 pt bold** (goodbye 44); `lead` 24 bold ("Today you will:" / "Now you can:"); `bullets` 22 with "•  "; right panel `round1Rect` `B9D2F7` at (7.9, 1.0) 4.9 × 5.6 with `pic` (8.45, 1.82) 3.8 × 2.66 and `lesson` 22 bold "Lesson N  ·  Level V" |
| `goals` / `numlist` | `title` at (8.35, 1.95) 40 bold; `side` 20; rows `R<k>` = `shadow` (`8FAFE3`) + `card` (white `round1Rect`) + `chip` (`B9D2F7`) + `num` 36/32 bold "01" + `text` 18–20 (+ `sub` 20 on goals row 1) + `dot` triangle |
| `warmup` | `kicker` 20 bold "OPENING TALK  ·  6:00"; `title` 40 bold; `box1` / `box2` 22; `pic` (7.44, 2.0) 5.2 × 3.64 |
| `words` | `title` 49 bold "New Words" / "More New Words"; `instr` card + `instr` 22; per word `Word picture k` 2.1 × 1.5 and `Word label k` 20 bold white "★ word" (★ = starred word in the lesson); 6 per slide |
| `check` | `title` 43 bold; `sub` 24; rows `R<k>`: `shadow`, `card` (middle card `C9B8F2`), `circle` (`FFE28C`), `num` 25 bold, `q` 18, `pic` 2.1 × 1.5, `ans` 28 bold on `FFE28C` (on click) |
| `before` | `title1` / `title2` 44 bold "Before You" / "Listen"; `context` 20; `pic` (0.175, 2.65) 3.0 × 2.1; voices `R<k>`: `num` 36 bold, `hl` (`FFE28C`, on click), `voice` 22; `listen head` 24 bold "Listen for:", `listen 1/2` 22; `audio` 22 "Audio: about 1:20. It plays once."; `play` 22 "Play 1: Task A" |
| `choice` | `title` 48 bold; `instr` 22; rows `R<k>`: `stmt` 20 + `opt1..4` 20 white on colored chips + `circle` ellipse (on click); optional row picture |
| `gaps` | head card (`head shadow`, `head card`, `head1` / `head2` 20); `title` at (8.8, 1.9) 40 bold; `side` 20; rows `R<k>`: `card`, `chip`, `num` 32 bold, `text` 18, `ans` 20 bold on `C9B8F2` (on click) |
| `checksay` | head card parts; `title` "Say It"; `side`; lines `S<k>`: `card` + `text` 24 (`*STRONG*` part in accent); optional `head chip` / `head num` |
| `qa` | `head` 18 / 28 bold ("Grammar Box k  ·  topic" + question title); `pic` (8.55, 1.25) 3.0 × 2.1; `left panel` white, `right panel` `B9D2F7`; `Q head` / `A head` 20 bold "QUESTION" / "ANSWER"; per row `Highlight k` (`FFE28C`), `Helper k` 22, `Question k` 20, `Answer bg k` white, `Answer k` 17 (on click) |
| `table` | full-height `left panel` `B9D2F7` with `pic` (0.5, 2.5) 3.6 × 2.5 and `head` 20 / 34 bold; `Q head` / `A head`; `Question k` 18; `Answer bg k` `C9B8F2` + `Answer k` 18 (on click) |
| `mistakes` | `title` 43 bold "Common Mistakes"; small `pic` top right; `Dont head` "Don't say" / `Say head` "Say" 22 bold; `Bad k` / `Good k` 16 (Good on click) |
| `drill` | `title` 40 bold "Pair Drill"; `sub` 20; `s1 label` / `s2 label` 22 bold; `s1 body` / `s2 body` 22; `pic` (1.4, 4.0) 3.8 × 2.6 |
| `talk` | `head` 26 / 40 bold ("Talk Time" + activity name); `grouping` 20; `time` 20 "7:00–7:12"; `Step num k` 22 bold on `FFE28C`; `Step k` 20–22; `pic` (0.8, 3.7) 4.2 × 3.0 |
| `go` | `title` 38 bold "Before You Go" + 22 "7:12–7:17"; `pic`; `Num 01/02` 30 bold; `Label 01/02` 22 bold "Exit ticket" / "Homework"; `Body 01/02` 18 |
| `progress` | `title` 43 bold "Progress Check" + "7:25"; `A head` 20 bold; `Bad k` 15 (items), `Good k` 24 (answers, on click); `ican` box "D. I can…", "😀   🙂   😐", "Check one face." + the "I can" lines |
| `credits` | background `C9B8F2`; `title` 54 bold "Credits"; three text boxes `pictures`, `names`, `audio` (16–20 pt headings, 13 pt audio text), the © line last |

To see any value exactly: `python3 scripts/slides/inspect_deck.py level3/slides/Level3_Lesson2_Slides.pptx 8` (slide 8), or `--short` for all slides.

**Level differences.**

| | Level 1 (beginner) | Level 3 (low intermediate), Levels 4–5 |
|---|---|---|
| Deck | 23–24 slides, hand-made (no kind tags), "Slide N" shape names | 25–27 slides, kind tags + role names, built with `build_deck.py` |
| Sequence | title · Today's Goals · Hello + Review · New Words · More New Words · Before You Listen · Listening A/B/C · grammar boxes with the question as title (e.g. "What do you do?") · Preview · practice · Common Mistakes · Talk Time + a 2nd activity (e.g. Find Someone Who) · Before You Go "7:10–7:15" · **literacy block 7:15–7:30** (2–3 slides: "Letters & Numbers · 7:15", e.g. "a or an?", "Letters: Task B", "Read the Signs") · Progress Check "7:25" · "Great Work! See You Next Week!" · Credits | as in the table above; no literacy block; Before You Go 7:12–7:17 |
| Spanish | Student pages have English + Spanish + "My language: ____" lines; the **slides are English only** (no Spanish lines) | no Spanish anywhere |
| Listening | about 1:00–1:20, 2–3 voices | about 1:30 at most, **up to 3 speakers** (Narrator + 2 characters) |

### 6.4 Speaker notes

Every slide has notes for a first-time volunteer teacher. Write them from the lesson's teacher plan, in this order:

1. **Timing line** on the first slide of each step: `Step k · 6:18–6:30 · Listening + "Say it" · 12 min (slides 8 to 12). Individuals, then pairs check.` Following slides of the step start with `Step k, continued.` or with the task (`Play 1 → Task A.`). Breaks and group sizes come from the plan ("15 learners: 7 pairs + 1 group of 3").
2. **What to say and do**, click by click ("Click to show the answer."). Answers are the key's answers.
3. A fallback line where useful ("If behind: one card only.", "No speaker? Read the script with a volunteer at a normal, friendly speed.").
4. **`Lesson plan: (...)`**: the last content line names the lesson parts the slide comes from, e.g. `Lesson plan: Step 3; Listening script; Listening page.` Never name a file (no `Level3_Lesson2.md`, no `AUDIO_STATUS.md`, no `drafts/` path). In the spec you write `f'{SRC} (Step 3; Listening script; Listening page).'` with `SRC = 'Source: Level<V>_Lesson<N>.md'`; `build_deck.py` turns it into the `Lesson plan:` line.
5. The picture credit line for slides with pictures: `Picture: Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), CC BY 4.0 (...); <changes> (images/CREDITS.md).` (`pic_credit(MOD)` in the spec).

**Listening audio and the notes.** The audio sentence in the Before You Listen notes depends on whether `level<V>/audio/L<V>_L<N>_listening.mp3` exists when you build:

- **Recorded:** `The audio (L3_L1_listening.mp3, about 1:31) plays the conversation once. Press play again for play 2. A third play is fine if the class needs it.` and the notes line `Audio: synthetic voices, computer-generated (Chatterbox TTS cloned from Kokoro-82M reference clips). No recordings of real people. The names and the story are invented.`
- **Not recorded yet ("coming soon"):** `The audio (about 1:20) is coming soon. When it is ready, it plays the conversation once; press play again for play 2. Until then, read the listening script (at the end of these notes) with a volunteer.` and **the whole listening script is appended to the Before You Listen notes**, one `Speaker: line` per line, after the heading `Listening script (the audio is coming soon; until then, read it aloud with a volunteer at a normal, friendly speed):`.

Write the recorded sentence in the spec; the builder switches to the coming-soon wording and appends the script automatically when the MP3 is missing. **When the audio arrives, rebuild the deck** (same command): the notes and the credits slide switch to the recorded wording.

### 6.5 Credits slide (always the last slide)

Three boxes, then the license line. The text (from `credits_slide()` in `deckspec.py`):

- **Pictures:** `Vocabulary pictures use Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). <what was changed, from the lesson's Picture Credits>` + `The faces on the Progress Check are standard emoji characters shown with the computer's emoji font.`
- **Names and story:** `<all names in the lesson> are invented names. The listening story is invented.`
- **Audio and font**, recorded: `Audio: synthetic voices made with Chatterbox TTS (MIT License), cloned from short synthetic reference clips made with Kokoro-82M (Apache License 2.0). No recordings of real people were used. Each file carries an inaudible Perth watermark marking it as AI-generated. Font: Lexend Deca (OFL 1.1).`
- **Audio and font**, coming soon: `Audio (coming soon): synthetic voices made with Chatterbox TTS (MIT License), cloned from short synthetic reference clips made with Kokoro-82M (Apache License 2.0). No recordings of real people. Each file will carry an inaudible Perth watermark marking it as AI-generated. Font: Lexend Deca (OFL 1.1).`
- **License line (never change it):** `© 2026 the authors. The authors license this deck under CC BY-NC-SA 4.0.` The notes repeat it as `Course materials: © 2026 the authors, licensed under CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/).` and end with `Lesson plan: Picture Credits. Picture list: images/CREDITS.md.`

### 6.6 Content rules for slides

All of section 2 applies. For slides in particular:

- **No instruction icons and no decorative emoji.** The only emoji are the self-check faces **😀 🙂 😐** on the Progress Check. Plain marks ✓ ✗ ★ ☐ ↗ are allowed where the lesson uses them (★ marks starred words). The published Level 1 Lesson 1 deck still has 👩 / 👨 speaker marks on slides 10–11 (older deck); do not copy them.
- **Pictures:** Twemoji (CC BY 4.0) or drawn in code, made by the level's picture scripts, **listed in the level's `CREDITS.md`**, and placed in the deck **byte-identical** to the file in `level<V>/images/` (the site exporter refuses anything else). Never use a picture from the internet, a stock site or an AI image generator. Every picture needs alt text.
- **No religious content** (holidays, places of worship, prayers, scripture). Never describe the curriculum as "secular". Never name any other ESL program, curriculum, publisher, or test. All names, stores, prices and addresses are invented (as in the lesson).
- **No "Draft" wording** in a published deck: no "Draft", "Draft for review", "TODO", placeholder text, or file names that are not on the site. (A lesson may legitimately use the word "draft" as content, e.g. "write a draft"; that is fine in the notes.)
- Keep "© 2026 the authors"; no copyright-registration claims.
- `scripts/slides/check_deck.py` checks most of this (add the names of other programs or publishers to look for with `--forbid 'Name1,Name2'`; the repository never writes them down); it does not replace reading every slide.

### 6.7 One-time setup

```bash
bash scripts/slides/setup_tools.sh
```

It installs, if missing: LibreOffice Impress (`soffice`), poppler-utils (`pdftoppm`), Noto Color Emoji and DejaVu fonts, the Python packages in `scripts/slides/requirements.txt` (python-pptx ≥ 1.0.2, lxml, Pillow), and the **Lexend Deca** TTF (SIL OFL 1.1, from https://github.com/google/fonts/tree/main/ofl/lexenddeca) into `~/.local/share/fonts` (`fc-cache -f`). The repository only has the web font `src/assets/fonts/LexendDeca-Variable.woff2`, which LibreOffice cannot use; without the TTF, renders use a fallback font and line breaks are wrong. Do not commit the TTF. Check: `fc-match "Lexend Deca"` must print `Lexend Deca`.

### 6.8 Step by step: make a deck (example: Level 3 Lesson N; for Level 4/5 replace `3`)

Work on a feature branch (section 9). Set the numbers once:

```bash
V=3; N=5; P=$((N-1))
```

**1. Read the lesson.** Get the lesson Markdown (6.1) and print the slide parts:

```bash
MD=level$V/curriculum/Level${V}_Lesson$N.md      # or the /tmp copy from a draft branch
python3 scripts/slides/lesson_outline.py $MD | less
```

**2. Check the pictures.** Every picture the deck will show must already be in `level$V/images/` and in `level$V/images/CREDITS.md`:

```bash
ls level$V/images/L${V}_L${N}_*.png; grep -c "L${V}_L${N}_" level$V/images/CREDITS.md
```

**3. Write the spec.** Copy the previous lesson's spec and rewrite it for this lesson:

```bash
cp level$V/slides/specs/Level${V}_Lesson$P.py level$V/slides/specs/Level${V}_Lesson$N.py
```

A spec is a Python file:

```python
"""Level 3 Lesson 5 deck spec. Build: python3 scripts/slides/build_deck.py --level 3 --lesson 5 (AGENTS.md section 6)."""
from deckspec import *
N = 5
DECK_TITLE = "Level 3 Lesson 5: <title from the lesson>"
MOD = '<what was changed in the pictures: from the lesson Picture Credits>'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L3_L5_{stem}.png'            # picture file of this lesson
A = lambda stem: alt(N, I(stem))                # its alt text, from CREDITS.md
SRC = 'Source: Level3_Lesson5.md'               # becomes "Lesson plan: (...)" in the notes
BUL = ['<objective 1>', '<objective 2>', '<objective 3>']   # title + goodbye bullets
W = newwords(N)                                 # the 12 word cards straight from the New Words table
SLIDES = [
  {'kind': 'title', 'title': '<lesson title>', 'bullets': BUL, 'pic': I('<stem>'), 'alt': A('<stem>'),
   'notes': ['Welcome learners as they arrive.', ..., f'{SRC} (Topic; At a glance: Objectives).', PC]},
  ...,
  credits_slide(N, '<all invented names>', '<changes sentence>', [audio_note(N, '1:20')]),
]
```

- Keep the **same list of slides and kinds** as the previous spec unless the lesson's sections differ; then add or remove slides of the matching kind (see 6.3).
- Each slide is a dict: `kind`, the kind's text keys, and `notes` (a list of lines). The keys per kind are in the existing specs (`level3/slides/specs/Level3_Lesson2.py` … `Level3_Lesson13.py` cover every kind) and in the `r_<kind>()` functions of `build_deck.py`. Optional size keys (`title_sz`, `sz`, `asz`, `aw`, `pic_box`, `pitch_max`, …) only fine-tune font sizes, widths and boxes when a lesson's text is longer; start without them and add them only if the render shows overflow.
- Text markup inside strings: `**bold**`, `*accent purple*`, `^regular weight^` (in a bold box).
- Row counts follow the lesson: 6 goals; 12 words (2 slides × 6); 3 meaning checks; the listening items exactly as numbered in the lesson; 5 grammar boxes; up to 7 mistakes; the Progress Check items of the lesson.
- `words(N, [(stem, label, star), ...])` is the manual alternative to `newwords(N)`.

**4. Build** (output goes to `build/slides/`, which is gitignored):

```bash
python3 scripts/slides/build_deck.py --level $V --lesson $N --md $MD --out build/slides/Level${V}_Lesson${N}_Slides.pptx
```

It prints the start, fallback, spec, Markdown, picture folders and whether the audio is ready, then the slide count. Lesson 1 of a new level: add `--start level$((V-1))/slides/Level$((V-1))_Lesson13_Slides.pptx`. Errors name the slide and kind (`slide 12 (checksay): KeyError(...)`): fix the spec.

**5. Check:**

```bash
D=build/slides/Level${V}_Lesson${N}_Slides.pptx
python3 scripts/check_slides.py $D
python3 scripts/slides/check_deck.py --level $V --lesson $N $D
```

Both must print `OK` with no warnings for a new deck.

**6. Render every slide and look at each one:**

```bash
scripts/slides/render_deck.sh $D build/slides/render_L${V}_L${N}
python3 scripts/slides/contact_sheet.py build/slides/render_L${V}_L${N} build/slides/L${V}_L${N}_sheet.jpg
```

(`render_deck.sh` runs `soffice --headless --convert-to pdf` and `pdftoppm -jpeg -r 60`.) Open the contact sheet and **every** `slide-NN.jpg` (an image viewer, or the image-reading tool of your agent). Visual QA checklist, every slide:

- [ ] no text overflows its box, is cut off, or overlaps another shape; no text runs off the slide
- [ ] titles fit on their lines (one or two lines as in the previous deck); nothing is tiny compared with the same slide in the previous deck
- [ ] every picture shows the right word/scene, not stretched; no empty picture frame
- [ ] row counts match the lesson; numbers 01, 02 … are in order; no leftover rows or text from the previous lesson
- [ ] colors, fonts and positions look the same as the same kind of slide in the previous deck (compare: `contact_sheet.py <new> out.jpg --compare <render of the previous deck>`)
- [ ] the renders show **all** text, including answers that appear on click: check that answers sit in their boxes
- [ ] the credits slide has the right names, audio wording and the © line

If something overflows: shorten nothing that comes from the lesson; instead set a smaller size key for that slide (`sz`, `title_sz`, `asz`, …) or a wider box (`aw`, `ow`), rebuild, and render again.

**7. Read the text and notes once, slide by slide,** against the lesson: `python3 scripts/slides/inspect_deck.py $D --short` lists all texts; `python3 - <<'EOF'` with python-pptx can print the notes (`slide.notes_slide.notes_text_frame.text`). Check the timing lines, the answers, and the `Lesson plan:` lines.

**8. Put the deck in place and export it for the site:**

```bash
cp $D level$V/slides/Level${V}_Lesson${N}_Slides.pptx
python3 scripts/export_deck.py level$V/slides/Level${V}_Lesson${N}_Slides.pptx $N --level $V
python3 scripts/export_content.py
git status --short     # expect: the pptx, the spec, src/decks/level$V/lesson$N.json, src/content_level$V.json, public/level$V/downloads/slides/...
```

`export_deck.py` stops if a picture is not byte-identical to a file in `public/level$V/images/` (run `export_content.py` first if you added pictures). It prints the reveal steps per slide: compare them with the clicks you expect.

**9. Build and preview the site:**

```bash
npm ci            # once
npm run build
npm run preview   # http://localhost:4173/
```

**10. Presenter click-through:** open `http://localhost:4173/#/level$V/present/$N`, press → (or click) through every slide: each click reveals one step, answers appear in order, nothing is stuck or empty, the counter ends on the last slide, and the PowerPoint download link works. Also open `#/level$V/lesson/$N` and `#/level$V/downloads`. No browser console errors.

**11. Commit and open a PR** (section 9). Commit the deck, the spec, and the generated site files together.

#### 6.8.1 Reproduce a published deck (to check your setup)

Before your first new deck, rebuild a published one and compare. This was done for all of Level 3 Lessons 2–13: every rebuild was identical to the published deck (`compare_decks.py` "SAME", and identical renders).

```bash
git show origin/level3-L2-13-audio-handoff:level3/drafts/curriculum/Level3_Lesson2.md > /tmp/Level3_Lesson2.md
python3 scripts/slides/build_deck.py --level 3 --lesson 2 --md /tmp/Level3_Lesson2.md --out /tmp/repro/Level3_Lesson2_Slides.pptx
python3 scripts/slides/compare_decks.py level3/slides/Level3_Lesson2_Slides.pptx /tmp/repro/Level3_Lesson2_Slides.pptx   # must print SAME
scripts/slides/render_deck.sh level3/slides/Level3_Lesson2_Slides.pptx /tmp/repro/pub
scripts/slides/render_deck.sh /tmp/repro/Level3_Lesson2_Slides.pptx /tmp/repro/new
python3 scripts/slides/contact_sheet.py /tmp/repro/pub /tmp/repro/compare.jpg --compare /tmp/repro/new
```

Never write a reproduction over a published deck.

#### 6.8.2 Level 4 or Level 5: the first deck

1. Lesson 1 Markdown, pictures and `CREDITS.md` exist under `level4/` (same names as Level 3: `level4/curriculum/Level4_Lesson1.md`, `level4/images/L4_L1_*.png`).
2. Copy the closest Level 3 spec (`level3/slides/specs/Level3_Lesson13.py`) to `level4/slides/specs/Level4_Lesson1.py`; change `N`, `DECK_TITLE`, the `I` prefix (`L4_L1_`), `SRC`, and all content.
3. `python3 scripts/slides/build_deck.py --level 4 --lesson 1 --start level3/slides/Level3_Lesson13_Slides.pptx --md level4/curriculum/Level4_Lesson1.md` (the fallback defaults to `level3/slides/Level3_Lesson1_Slides.pptx`). The slides are tagged `L4:<kind>` and the title reads "Lesson 1 · Level 4".
4. Steps 5–11 as above, plus the site changes in 6.9.

#### 6.8.3 Small fixes to one slide

Change the spec and rebuild the whole deck (steps 4–11). Do not hand-edit a built Level 3+ deck: the next rebuild would undo it.

#### 6.8.4 Editing with python-pptx directly (Level 1, or a one-off fix)

Rules: copy the deck first; change text **inside the existing runs** (keeps font, size, color); never delete and re-add a shape that an animation targets (the click steps point to shape ids: `check_slides.py` fails if an id disappears); swap a picture by replacing the image part's bytes, not the shape.

```python
from pptx import Presentation
prs = Presentation('level1/slides/Level1_Lesson5_Slides.pptx')
s = prs.slides[6]                                   # slide 7
for sh in s.shapes:
    print(sh.shape_id, sh.name, sh.has_text_frame and sh.text_frame.text[:40])
box = next(sh for sh in s.shapes if sh.shape_id == 12)
run = box.text_frame.paragraphs[0].runs[0]
run.text = 'new text from the lesson'               # keep the run: keeps Lexend Deca, size, bold, color
for r in box.text_frame.paragraphs[0].runs[1:]: r.text = ''
pic = next(sh for sh in s.shapes if sh.shape_type == 13)       # a picture; swap its image bytes:
img_part = s.part.related_part(pic._element.blipFill.blip.rEmbed)
img_part._blob = open('level1/images/L1_L5_cashier.png', 'rb').read()   # byte-identical file from the images folder
pic._element.nvPicPr.cNvPr.set('descr', 'Cashier: ...')                 # alt text from CREDITS.md
s.notes_slide.notes_text_frame.text = 'Notes line 1\nNotes line 2'
prs.save('/tmp/Level1_Lesson5_Slides.pptx')
```

Then run steps 5–11 on the saved file. (An image part can be shared by several slides: only swap it if every use should change.)

### 6.9 Site side

**How a lesson appears** (`scripts/export_content.py`, `export_level()` and `lesson_page()`):

- **Ready:** `level<V>/curriculum/Level<V>_Lesson<N>.md` is on `main`. The lesson gets its pages, PDF/DOCX (`level<V>/curriculum/build.sh <N> --publish`), MP3 (if `level<V>/audio/L<V>_L<N>_listening.mp3` exists), and the slides.
- **Slides only:** no lesson Markdown on `main`, but `level<V>/slides/Level<V>_Lesson<N>_Slides.pptx` exists. The lessons list shows **"Slides ready"** and **"Lesson book soon"**; the lesson page shows only the slide card (present + PowerPoint download); the Downloads page lists it under "Teacher slides". Level 3 Lessons 1–13 are ready. This path remains for a lesson that has a deck but no lesson book (`slidesOnly` in `src/level3.tsx`).
- **Coming soon:** neither file.

**From slides-only to fully ready** (the path used for Level 3 Lessons 2–13):

1. Add `level3/curriculum/Level3_Lesson<N>.md` to `main` (plus its pictures and `CREDITS.md` rows if not there yet).
2. `level3/curriculum/build.sh <N> --publish` (PDF + DOCX).
3. If the audio is ready: add `level3/audio/L3_L<N>_listening.mp3` (+ check files, section 4), then **rebuild the deck** (6.8 step 4, same spec): the notes and credits switch to the recorded wording and the script leaves the notes.
4. `export_deck.py`, `export_content.py`, build, preview, PR (6.8 steps 8–11).
5. The Level 3 home and level picker texts count ready lessons automatically (`readyLessons3`, `l3Ready`).

**Adding Level 4 (or 5) to the site.** Copy what Level 3 does; search the code for `level3` / `Level3` / `l3`:

| Where | What to add |
|---|---|
| `scripts/export_content.py` `LEVELS` | a `4: dict(audio=lambda n: f'L4_L{n}_listening.mp3', audio_re=r'^L4_L\d+_listening\.mp3$', routine_end='> **Timing is loose', credit=...)` entry; `export_level(4)` then writes `src/content_level4.json` and copies `level4/images`, `audio`, `slides` into `public/level4/` |
| `scripts/export_deck.py` | nothing: `--level 4` writes `src/decks/level4/lesson<N>.json` and checks pictures against `public/level4/images/` (`IMG_URL`, `OUT_DIR`) |
| `src/presenter/decks.ts` | `level4Files = import.meta.glob('../decks/level4/lesson*.json')`, a `level4Loaders` table, `Level = 1 \| 2 \| 3 \| 4`, and the branch in `table()` |
| `src/presenter/Presenter.tsx` | `import level4 from '../content_level4.json'`, `level4Pptx()`, and the `level === 4` cases (back link, PowerPoint link) |
| `src/config.ts` | `level4PresentHref = (n) => \`#/level4/present/${n}\`` |
| `src/content_level4.ts`, `src/level4.tsx` | copies of `content_level3.ts` / `level3.tsx` with 3 → 4 (home, lessons, lesson page, downloads; the slides-only handling comes with it) |
| `src/App.tsx` | the imports; the nav entry `4: [...]` and the level detection (`path.startsWith('/level4')`); the credit line; the `LevelPicker` card (`l4Ready`); the routes `/level4`, `/level4/lessons`, `/level4/lesson/:n`, `/level4/lesson/:n/:tab`, `/level4/downloads`, `/level4/*`, and `/level4/present/:n` (also in the presenter path check) |
| `AGENTS.md` section 1 | a Level 4 column |

Then `npm run build`, preview every Level 1–4 page, and check that Level 1–3 data stay byte-identical (`git status`).

### 6.10 Branch and publish rules for decks

- One **feature branch** per job (e.g. `level4-L1-slides`), made from the current `origin/main`. Commit the spec, the deck, and the generated site files together.
- Test before pushing: 6.8 steps 5–10 (checks, renders, export, `npm run build`, presenter click-through).
- **Never commit** `node_modules/`, `dist/`, `build/` (renders, rebuilt decks), virtual environments, model weights, WAV files, fonts, or secrets (section 8).
- Push the branch normally (no force-push), open a PR into `main`, and **wait for the owner's approval**. Merge with a **merge commit**, delete the branch, wait for the "Deploy to GitHub Pages" run, and check the live site: `https://sdpursley.github.io/ESL-Curriculum/#/level<V>/present/<N>` clicks through, the PowerPoint link returns 200 (section 9).
- Never change the repository visibility or the Pages settings.

---

## 7. Running audio locally (Level 3 Lessons 2–13 drafts)

Draft copies of Level 3 Lessons 2–13 stay in `level3/drafts/` (`curriculum/`, `images/`, `audio/`, `audio/tools/`). The website does not read
this folder. Published copies are in `level3/curriculum/`, `level3/images/`, and `level3/audio/`. Which lessons still need audio is in [`level3/AUDIO_STATUS.md`](level3/AUDIO_STATUS.md):
**done**, **partial**, or **to-do**, with the lines that remain. Level 3's draft audio is in this repository. For the next level, make a new branch from `main` the same way (`level3-L2-13-audio-handoff` was that branch for Level 3) and run the commands below on that branch. The token-efficient way to run that job on this machine is [Token-efficient local run](#token-efficient-local-run).
All rules in sections 3 and 4 apply. The Level 3 drafts tooling is in `level3/drafts/audio/tools/`:

| File | What it does |
|---|---|
| `scripts/script_L3_L<N>.py` | Line file: `INTRO`, `LINES` (speaker, line text), `END`, `VOICES` (speaker → clip), `FEMALE`, `SAME` (voice-text spellings). Made from the lesson Markdown by `make_script_L3.py <N>` with `cast/cast_L3_L<N>.json` |
| `make_refs_L3.py` | Rebuilds the Kokoro-82M reference clips in `refs/` from their voice ids (`--check` compares them with the committed clips, `--copy` copies those instead). List: `REFS_L3.md` |
| `run_audio_L3.sh <N>` | Build + small.en check + medium.en second opinion + gate, each heavy step under the lock; output in `out/L<N>/` |
| `publish_audio_L3.sh <N> ['notes']` | Only after gate PASS and listening: copies the MP3, log, check results, gate, second opinion into `level3/drafts/audio/` and writes `L3_L<N>_README.md` |
| `build_listening_L3.py`, `engine.py` | Chatterbox whole-sentence takes (seeds 2026 + k·7919, up to `MAXT`=16), take cache in `cache/` |
| `check_listening_L3.py`, `second_opinion_lines.py`, `audio_gate_L3.py`, `whisper_cfg.py`, `canon.py`, `metrics.py` | The checks (section 4) |
| `lockrun.py` | Portable lock (`flock` is not on macOS): `python lockrun.py /tmp/chatterbox.lock <cmd> ...` |

**Prerequisites**

- Python **3.11**, **ffmpeg** on `PATH`, about 10 GB of free disk space (models) and 16 GB RAM. Windows: use WSL (`lockrun.py` needs `fcntl`).
- One virtual environment at the repository root (not committed):
  ```bash
  python3.11 -m venv .venv-audio
  .venv-audio/bin/pip install -U pip
  .venv-audio/bin/pip install -r level3/drafts/audio/tools/requirements.txt   # chatterbox-tts 0.1.7, torch 2.6.0, faster-whisper 1.2.1, kokoro-onnx 0.6.1 ...
  ```
- The checks use **faster-whisper** (small.en and medium.en; downloaded on first use). openai-whisper is not needed. Do not swap it in: its
  text differs, and the pass rule was set with faster-whisper.
- Kokoro model files for `make_refs_L3.py` go in `tools/audio/models/` (not committed):
  `kokoro-v1.0.onnx` and `voices-v1.0.bin` from https://github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0
  (or set `KOKORO_MODEL` / `KOKORO_VOICES`). If kokoro-onnx is not installed, the script uses the PyTorch `kokoro` package.

**Devices and time**

- `TTS_DEVICE=auto` (default) picks **CUDA**, then **MPS** (Apple Silicon), then **CPU** for Chatterbox. Force one with `TTS_DEVICE=cpu|mps|cuda`.
- Whisper runs on the **CPU** with `compute_type=float32` and `cpu_threads=1` (`whisper_cfg.py`; `WHISPER_DEVICE`, `WHISPER_COMPUTE`, `WHISPER_THREADS`).
  This is the deciding setting from section 4, so keep it. faster-whisper has no MPS backend. Use `WHISPER_DEVICE=cuda` only for a quick look, and
  run the check again on the CPU before you publish.
- Expect, for one lesson (about 15 lines, 40–50 takes with the retries): CPU, 8 cores: building 45–60 min (about 1 min per take; Lesson 5 took
  48 min), small.en check about 2 min, medium.en about 4–8 min, so about **1 hour per lesson** and 10–12 hours for the 10 lessons left.
  CUDA: building a few minutes. MPS: building usually 2–4× faster than the CPU (if MPS fails on an operation, use `TTS_DEVICE=cpu`).
  Each retake costs only the rejected lines (the other takes come from `cache/`).
- The same seed gives a **different take on another computer or device**, and the cache does not carry over. Old seeds from
  `AUDIO_STATUS.md` are only notes. Build every lesson that is not done from line 1.

**Commands** (from the repository root; `T=level3/drafts/audio/tools`)

```bash
T=level3/drafts/audio/tools
# 1. reference clips (once): writes $T/refs/*.wav from the Kokoro voice ids; --check must say OK for all 10
.venv-audio/bin/python $T/make_refs_L3.py && .venv-audio/bin/python $T/make_refs_L3.py --check
# 2. record + check + gate one lesson (example: Lesson 6)
bash $T/run_audio_L3.sh 6
#    retake: add the seeds of the takes that failed (sentence text exactly as in the log), then run again
EXCLUDE='{"<sentence>": [<seed>], "<other sentence>": [<seed>, <seed>]}' bash $T/run_audio_L3.sh 6
# 3. listen to $T/out/L6/L3_L6_listening.mp3 from start to end, then publish into level3/drafts/audio/
bash $T/publish_audio_L3.sh 6 'Optional note for the README'
```

`run_audio_L3.sh` stitches the MP3 itself (the builder joins the takes with the pauses, normalizes loudness, writes the WAV master and the
MP3 with ffmpeg). Its last line is the gate summary: `PASS True` is needed. Details: `out/L<N>/L3_L<N>_gate.json`, `build.log`,
`L3_L<N>_check_results.json`, `L3_L<N>_second_opinion_medium.txt`. Use `PY=` for another Python and `LOCK=` for another lock file.
If a lesson's Markdown changes, run `.venv-audio/bin/python $T/make_script_L3.py <N>` first, and rebuild the DOCX/PDF with
`PYTHON=.venv-docs/bin/python level3/drafts/curriculum/build_draft.sh <N> --inplace`. Keep the "Draft for review" wording in the lesson files.

**Rules for these files** (sections 3 and 4, applied to Level 3)

- Voices: Chatterbox clones of the synthetic Kokoro-82M clips in `refs/` only (`engine.py` refuses any other path). Never use real-person voices,
  LibriTTS/LibriVox, Piper, or the Chatterbox default voice. Female characters get female clips (`FEMALE` in the script).
- Settings: **exaggeration 0.72, cfg 0.32** for the characters. The Level 3 **narrator uses 0.55 / 0.40** (built in; do not change).
- **Whole-sentence takes**. Pauses **1.3–1.5 s** between speakers (`PAUSE_SPK`, default 1.3; the gate accepts 1.25–1.6 s).
- Length: **about 1:30 at most** (the gate allows 1:00–1:30), **up to 3 speakers** (Narrator + 2). If it is too long, shorten the lesson
  Markdown and run `make_script_L3.py` again. Do not speed up the audio.
- **Pass rule:** a line passes if **either** small.en **or** medium.en hears it correctly (after `canon.py`), **and** its pitch is OK
  (male median **under 150 Hz**, female 165 Hz or more) **and** it has **no clipping**. Retake only lines that both checkers miss, or for pitch or clipping.
- **Spelled letters and digit strings are checked by ear**, not by the score.
- **Only one heavy model process at a time** (Chatterbox, Whisper, Kokoro). The scripts hold `/tmp/chatterbox.lock`. Do not run two lessons in parallel.
- Listen to the whole file before you publish it, even after `PASS True`.

**Commit the results back** (same branch, no PR, no merge without the owner):

1. `bash $T/publish_audio_L3.sh <N>` copies `L3_L<N>_listening.mp3`, `_listening_log.json`, `_check_results.json`, `_gate.json`,
   `_second_opinion_medium.txt` and `L3_L<N>_README.md` into `level3/drafts/audio/`.
2. Set that lesson's row in `level3/AUDIO_STATUS.md` to **done** (length, gate PASS, retakes), and update the real length in the listening-script heading of `level3/drafts/curriculum/Level3_Lesson<N>.md`.
3. `git status`: commit **only** those files (and changed scripts, if any). **Never commit WAV files**, `refs/`, `cache/`, `out/`, `build/`, `.venv-audio/` or model files.
   ```bash
   git switch <audio-branch> && git pull
   git add level3/drafts/audio/L3_L<N>_* level3/AUDIO_STATUS.md level3/drafts/curriculum/Level3_Lesson<N>.md
   git status --short | grep -iE '\.wav|\.onnx|\.bin|\.pt|venv|cache/|out/' && echo STOP   # must print nothing
   git commit -m "Level 3 Lesson <N> draft listening audio" && git push origin <audio-branch>
   ```
   A normal push only, never force-push. Moving drafts onto the website (into `level3/curriculum/`, `level3/images/`, `level3/audio/`) is a separate step that needs the owner's approval.

### Token-efficient local run

Use this when the owner asks for a level's listening audio on this machine. The recorder is a local script. Start it, then leave it alone. Reading the build log from the chat, or starting a second loop to re-decide takes, spends tokens and does not make the audio. When a line fails the checker and that line is not the grammar the lesson is teaching, rewrite the line and record the lesson again. The steps are under **A line the checker cannot accept** below.

**Branch.** One feature branch holds the lessons that pass. Level 3 used `level3-L2-13-audio-handoff`, made from `main`. Level 4's scripts and tools are not on `main`, so `level4-audio` starts from `origin/level4-lessons` (commit `c48e8c3`). A later level that is already on `main` starts from `main`. Keep the main checkout on `main` and do the recording in a second worktree. Merging the audio branch into `main` needs the owner's approval. A push to `main` deploys the website.

**One job.** Start the driver with `setsid`, in its own session, so clearing a task list does not kill it. One quiet monitor may watch that process. The monitor stays silent until the run finishes, the process dies, no log file under the driver's state directory or `out/` changes for 90 minutes, or a long deadline. Driver scripts live in `~/.grok/long-running-background-tasks/` and are not committed. State for a run (pid, exclude files, stop notes) lives in a directory next to those scripts.

**This computer.** There is no CUDA and no MPS. Set `TTS_DEVICE=cpu`, `NT=2`, `OMP_NUM_THREADS=2`, `MKL_NUM_THREADS=2`, `OPENBLAS_NUM_THREADS=2`, `WHISPER_DEVICE=cpu`, `WHISPER_COMPUTE=float32`, `WHISPER_THREADS=1`, `TOKENIZERS_PARALLELISM=false`, `HF_HUB_DISABLE_TELEMETRY=1`, `TMPDIR=~/.cache/esl-audio-tmp`, and `MALLOC_ARENA_MAX=2`. The virtual environment is the main checkout's `.venv-audio` (Python 3.11). A worktree has no venv; set `PY` to `/home/sdpursley/Projects/ESL-Curriculum/.venv-audio/bin/python`. ffmpeg is `/usr/bin/ffmpeg`.

**One model.** Only one Chatterbox or Whisper process, under `flock` on `/tmp/chatterbox.lock`. Leave the recorder running until it finishes. Finished takes stay in `cache/` and are reused. A second Chatterbox or Whisper ran out of memory on this machine.

**Pass, then push.** Up to 3 gated runs per lesson. Seeds are `2026 + k·7919`, at most 16 (`MAXT`). After the gate says PASS, publish the MP3 and the check files, set the status row and the real length in the listening-script heading, and commit only those files plus the status file and the lesson Markdown. Then `git push -u origin <audio-branch>` (a normal push). The owner reviews the branch after the set is pushed. A person still listens to each MP3 once. The model cannot hear audio.

**A line the checker cannot accept.** One sentence that never passes fails the whole lesson. Level 3 finished after the stuck lines were rewritten, and the good takes already in `cache/` were reused. Do that again. This is the owner's standing rule (2026-10-23): rewrite a failed line the way Level 3 was rewritten, unless that line is the grammar the lesson is teaching. When a sentence has used all 16 seeds and still fails, or the whole-file check misses a line and no unused seed remains:

1. Stop the recorder before you edit. A process that already loaded the script keeps the old line.
2. Rewrite the spoken line and the printed listening script so they say the same words. Keep the grammar. Update every task evidence string, the slide spec, the rebuilt deck, the site text, and that lesson's PDF and DOCX. Then record the lesson again. Unchanged sentences come back from `cache/` in seconds.
3. Say the full form when the checker drops a contraction or a short form and the lesson is teaching the meaning. Level 4 recordings say "going to" and "want to", and "we have" where "we've" disappeared. The Hear It box can still say that people often say gonna and wanna, and that learners only need to recognize those short forms. Do not write that learners will hear a short form the recording does not say.
4. Change a name, a number, or a fragment the checker hears as a different phrase. Level 4 examples: "Park View" was heard as one word, so the page says Parkview; "Aisles one to six" was heard as "IELTS 16", so the line says "Those shelves are done"; "It's one eighteen over seventy-six" matched and still sat under the word-probability cutoff, so the line says the blood pressure looks normal; "March what?" became a full question. The answer key must still be found in the script.
5. Keep the pass rule and the pitch floors (male median under 150 Hz, female 165 Hz or more). Leave `canon.py` as it is. A checker change still needs the owner's decision.

**When a rewrite is not the right fix.** If the stuck words are the grammar point and no other wording still teaches it, or a rewrite has already been recorded and the gate still fails, or the length is outside that level's gate: leave that lesson as it is. Put the MP3, the log, the check JSON, the gate JSON, the second opinion, and a short note on a branch named `level<V>-L<N>-audio-failed`. Leave the WAV, `cache/`, and `out/` uncommitted. Open a GitHub issue that names the lesson, the duration, the sentences that failed, what the checkers heard, and the branch. Label the issue `audio`. Create the label once if it is missing:

```bash
gh label create audio --repo sdpursley/ESL-Curriculum --description "Listening audio builds and checker failures" --color 1d76db
```

If that lesson already has an `audio` issue, comment on it. Do not open a second one. Then continue the other lessons.

**Numbers and reductions.** `canon.py` already treats number words and digits as the same string, so a line can match and still fail the take when a word probability stays under 0.5. Spelled letters and digit strings are checked by ear (section 4). `canon.py` does not treat *gonna* as "going to" or *wanna* as "want to". Write the full form in the spoken script.

**Level 4, with sections 3 and 4.** Tools: `level4/audio/tools/run_audio_L4.sh <N>` (build, small.en, medium.en, gate) and `publish_audio_L4.sh <N> ['notes']`. Narrator **0.55 / 0.40**, characters **0.72 / 0.32**. Whole-sentence takes. Pauses **1.3–1.5 s** (the gate accepts 1.25–1.6). Length gate **1:30–2:15**. The gate fails a heard line only when both checkers miss it. Pitch, clipping, length, gaps, and a sentence that used every seed still fail the gate. A lesson may have more than three voices. Commit message for a passing lesson: `Level 4 Lesson <N> draft listening audio`. The same never-commit check as above: the staged diff must contain no `.wav`, `.onnx`, `.bin`, `.pt`, `venv`, `cache/`, or `out/`.

---

## 8. Never commit

- `node_modules/` or `dist/`
- Python environments (`.venv*`)
- Model weights (`models/`, `*.onnx`, `*.bin`, `*.pt`, `*.safetensors`)
- WAV files, except the committed reference clips in `tools/audio/samples/refs/` and `level1/audio/tools/natural/kokoro_refs/`
- `cache/`, `out/`, or `build/` output folders (including `build/slides/`: rebuilt decks and renders)
- `_twemoji_src/`
- `__pycache__/`
- Secrets or tokens of any kind

`.gitignore` covers most of these. Still check `git status` before every commit.

## 9. Repository rules

- Work on a **feature branch**, then open a **pull request** into `main`.
- Merge with a **merge commit** (not squash or rebase), then delete the branch.
- **Never force-push**, and never rewrite pushed history.
- Do not change the repository visibility or the Pages settings (the Pages source is GitHub Actions).
- Before pushing, search the whole diff for forbidden words: other program, curriculum, or publisher names; "secular"; religious words; and registration claims.
- After the merge:
  - wait for the "Deploy to GitHub Pages" run to succeed;
  - check the live site (https://sdpursley.github.io/ESL-Curriculum/): the changed pages, downloads, and audio return 200, and there are no console errors;
  - check that the presenters of the changed lessons still click through.
- Data for levels you did not touch must stay byte-identical.
