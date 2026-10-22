# Maintaining the ESL Curriculum (Levels 1, 2 and 3)

This guide explains how to change and rebuild everything in this repository: the curriculum book (PDF/DOCX),
the exams, the website, the slide decks, the vocabulary pictures, and the listening audio.
Sections 1–7 are about **Level 2** (and the website in general). **Level 1** has its own section: [section 8](#8-level-1); **Level 3** is [section 9](#9-level-3).
You do not need to be a programmer. Copy the commands as written, and run them from the repository folder.

**[AGENTS.md](AGENTS.md)** is the short, exact handoff guide (layout, content rules, voices, audio checks, step-by-step for a new lesson
or exam, how to build slide decks for any level in its section 6, repository rules) for another AI coding tool or a person continuing the work. Read it first; this file has the longer how-to.

## What is where

| Folder / file | What it is |
|---|---|
| `curriculum/Level2_Curriculum_v5_public.md` | **The curriculum text.** The book, the exam packets, and the website lesson pages all come from this file. |
| `curriculum/build.sh` | Rebuilds the book (DOCX + PDF) and the four exam files from the Markdown. |
| `curriculum/md2docx.py`, `curriculum/packets.py` | Helpers used by `build.sh` (Markdown → Word; cutting the exam packets out of the book). |
| `public/images/` | The 181 vocabulary pictures, plus `CREDITS.md` (picture sources and licenses). |
| `public/audio/` | The 15 listening MP3s (Lessons 1–13, midterm, final). |
| `public/downloads/` | Files people download from the site: the book, `exams/`, and `slides/` (the PowerPoint decks). |
| `src/` | Website code. `src/content.json` = lesson pages, `src/decks/` = slides for the in-browser presenter. |
| `scripts/export_content.py` | Copies the curriculum text into `src/content.json` for the website. |
| `scripts/export_deck.py` | Turns a PowerPoint deck into `src/decks/lessonN.json` for the in-browser presenter. |
| `tools/images/` | Scripts that drew the vocabulary pictures. |
| `tools/audio/` | Scripts that made the listening audio with Chatterbox, plus the voice reference clips. |
| `level1/` | **Level 1 sources**: `curriculum/` (lesson Markdown, scope and sequence, build script), `images/`, `audio/`, `slides/`, `exams/` (midterm and final). See section 8. |
| `public/level1/` | Level 1 files the website serves (pictures, MP3, PDF/DOCX/PPTX downloads). Refreshed from `level1/` by the scripts; don't edit here. |
| `src/content_level1.json`, `src/decks/level1/` | Level 1 lesson pages and presenter slides (generated). Level 1 page code: `src/level1.tsx`. |
| `level3/`, `public/level3/`, `src/content_level3.json`, `src/decks/level3/` | **Level 3**, laid out the same way as Level 1 (page code: `src/level3.tsx`). See section 9. |
| `Five_Level_Map.md` | Planning map for all five levels. |

## One-time setup

You need:

- **Git** and a GitHub login with access to this repository.
- **Node.js 20** (for the website): https://nodejs.org
- **Python 3.11 or newer**.
- **LibreOffice** (makes the PDFs): https://www.libreoffice.org
- For audio only: **ffmpeg**, and a computer with about 8 GB of RAM and 5 GB of free disk space.

Then, in the repository folder:

```bash
npm ci                                              # website packages
python3 -m venv .venv-docs
.venv-docs/bin/pip install -r tools/requirements-docs.txt    # python-docx, lxml, Pillow
```

(On Windows, use `.venv-docs\Scripts\pip` instead of `.venv-docs/bin/pip`. The `.sh` script needs Git Bash or WSL.)

When a command below says `python3`, use `.venv-docs/bin/python` if you made the virtual environment.

## 1. Edit lesson text and rebuild the book and exams

1. Open `curriculum/Level2_Curriculum_v5_public.md` in any text editor (VS Code works well, and GitHub's web editor works too).
   Keep the headings exactly as they are (for example `## Lesson 3 (Week 3): Free Time`, `## Lesson 3 (Week 3) · Grammar`).
   The build scripts and the website find each part by these headings. Comments like `<!-- part: ... -->` and
   `<!-- mode: ... -->` control the layout; leave them alone.
2. Rebuild:

   ```bash
   PYTHON=.venv-docs/bin/python curriculum/build.sh            # output goes to curriculum/build/ (not committed)
   ```

   Open `curriculum/build/Level2_Curriculum_v5_public.pdf` and check your change. The exam files are in `curriculum/build/exams/`.
   The exam packets are cut out of the book automatically (from the "Week 8: Midterm" and "Week 15: Final Exam" sections),
   so an exam fix is a fix in the main Markdown file.
3. When you are happy, copy the new files into the website's downloads:

   ```bash
   PYTHON=.venv-docs/bin/python curriculum/build.sh --publish
   ```

4. Update the website lesson pages (next section), then publish (section 7).

PDF page layout depends on the fonts installed. The documents use Calibri; on Linux LibreOffice substitutes Carlito, which
has the same measurements. If page breaks look different on your computer, install Carlito or Calibri.

## 2. Update the website lesson pages

The lesson pages, teacher plans, and home-page lesson data come from the Markdown:

```bash
python3 scripts/export_content.py      # rewrites src/content.json and src/sizes.json
npm run dev                            # preview at the address it prints (Ctrl+C to stop)
```

Other page text (home page, About page, Downloads page wording, navigation) lives in `src/App.tsx`, with site settings
and links in `src/config.ts`. Edit those files directly.

## 3. Slides (PowerPoint decks)

The `.pptx` files in `public/downloads/slides/` **are** the editable source. (The decks were first made with a
one-time builder that is not part of this repository; you do not need it.)

1. Open `public/downloads/slides/LessonN_Slides.pptx` in PowerPoint or LibreOffice Impress, edit, and save it with the **same name**
   in PowerPoint format (.pptx). Keep the slide size. Animations (click-to-reveal) are used by the presenter: each "on click"
   animation becomes one reveal step.
2. Update the in-browser presenter for that lesson:

   ```bash
   python3 scripts/export_deck.py public/downloads/slides/LessonN_Slides.pptx N
   python3 scripts/export_content.py     # refreshes download file sizes
   npm run dev                            # check #/present/N
   ```

Pictures in a deck that match a file in `public/images/` are shown from there; other pictures are embedded.

## 4. Add or replace a vocabulary picture

Pictures are 600×420 PNG cards made from Twemoji graphics (CC BY 4.0).

- **Easiest:** make or edit a 600×420 PNG with any image editor and save it in `public/images/` using the naming pattern
  `L<lesson>_<word>.png`. Put it in the lesson's New Words table in the Markdown: `![word](images/L3_cook.png)<br>**cook**`.
- **With the original scripts** (same look as the existing pictures):

  ```bash
  python3 -m venv .venv-img && .venv-img/bin/pip install -r tools/images/requirements.txt
  cd tools/images
  ../../.venv-img/bin/python make_images.py       # Lessons 1–4  (writes PNGs into this folder)
  ../../.venv-img/bin/python make_images_v5.py    # Lessons 5–13
  ```

  Each picture is one entry in the script (which emoji codes, sizes, and labels). Copy a similar entry, change it,
  run the script, then copy the new PNG into `public/images/`. The scripts download the emoji SVGs from the Twemoji
  GitHub repository into `_twemoji_src/` (not committed) and use the DejaVu Sans Bold font.
- **Always** add a line for a new picture to `public/images/CREDITS.md` (which emoji were used). If you use a picture
  from somewhere else, make sure its license allows it and credit it there.

Then rebuild the book (section 1) and the website data (section 2).

## 5. Make or fix listening audio (Chatterbox)

The audio was made with **Chatterbox TTS** (Resemble AI, MIT License) on a normal CPU. The voices are cloned from the short
reference clips in `tools/audio/samples/refs/` (Rosa, Sam, Ana, Carlos, Marco, Kim, N = Narrator, Server, Receptionist, Agent;
those clips were made with Kokoro-82M, Apache 2.0). Every Chatterbox file carries an inaudible **Perth watermark**
marking it as AI-generated. Do not remove it.

**Voice rule:** every voice must be cloned from a synthetic, Kokoro-made reference clip. Never use a voice based on
recordings of real people: no LibriVox / LibriTTS / LibriTTS-R audio, no Piper voices trained on them, and not
Chatterbox's built-in default voice (`processor.py` refuses to run Chatterbox without a reference clip). The
reference clips are plain Kokoro output: `tools/audio/make_refs.py` remakes them, and `make_refs.py --check`
confirms that the committed clips match fresh Kokoro output (it needs `kokoro-onnx` and the Kokoro model files).

**Setup** (Python 3.11, separate environment, downloads about 3 GB of model weights on first run):

```bash
python3.11 -m venv .venv-audio
.venv-audio/bin/pip install -r tools/audio/requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu
```

**Where the words are:** `tools/audio/scripts.py` (Lessons 1–4) and `tools/audio/scripts_v5.py` (Lessons 5–13, `Midterm`, `Final`).
Each entry is the narrator intro plus a list of `(speaker, line)`. Keep these the same as the listening scripts in the Markdown.

**Make one lesson** (example: Lesson 7):

```bash
cd tools/audio
SINGLE=1 TRIES=6 SEED0=2026 EXAG=0.55 CFG=0.45 ../../.venv-audio/bin/python processor.py chatterbox L7
ffmpeg -y -i samples/chatterbox_L7.wav -ac 1 -b:a 96k -metadata "title=Level 2 L7 Listening (chatterbox)" ../../public/audio/L7_listening.mp3
```

What the settings mean:

- `SINGLE=1`: the conversation plays **once** (intro → conversation → "That's the end of the listening."). All published files are single-play;
  teachers press play again if needed. Without it the conversation plays twice.
- `EXAG=0.55`, `CFG=0.45`: Chatterbox expressiveness and pacing. These values were used for all files.
- `TRIES=6`: each short piece (clause) is made up to 6 times until it passes the checks; the best try is kept.
- `SEED0=2026`: the starting random seed (try k uses `SEED0 + k*7919`). A different seed gives a different take.

**Built-in checks.** Every piece is transcribed with Whisper (`small.en`) and checked: first and last word right,
at least 85% of words match, no extra words, and no acoustic problems (`artifacts.py`: humming, long breaths, clicks,
sound before or after the words). Pieces that needed a retry, or still failed after all tries, are listed in
`samples/chatterbox_L7_regen_log.json`. The logs from the published files are in `tools/audio/regen_logs/`.

**Check the finished files:**

```bash
../../.venv-audio/bin/python asr_check_mp3.py L7      # checks public/audio/L7_listening.mp3
```

It writes `asr_mp3_results.json` (in the current folder) with a word-by-word comparison against the script.
`SUFFIX= ../../.venv-audio/bin/python asr_check.py chatterbox L7 --single` checks `samples/chatterbox_L7.wav` the same way. **Always also listen** to the whole file.

**Fixing one bad line** without remaking the whole file: make only that line again with different seeds or slightly different
punctuation, then splice it into the WAV in place of the old one. `tools/audio/repair/` has the scripts used for the October
2026 fixes (`fix6_regen.py` + `fix6_splice.py` for five lines, `fix_lopez.py` for one word). Edit the lesson, speaker, line, and
the start/end times (in seconds, found by listening) before running them.

**Names that come out wrong:** spell them the way they sound. Chatterbox said "Lopez" badly, so the fix used the text
`Lopes.` (it sounds like "Lopez") with `EXAG=0.55 CFG=0.45` and seed 9313. The written script and the workbook still
say **Lopez**. Use the same trick for other names.

**After new audio:** update the durations in the Markdown if they changed (`tools/audio/repair/fix_times.py` shows the
pattern), rebuild (sections 1–2), and publish.

## 6. Check before you publish

```bash
npm run build      # must finish with no errors
npm run preview    # opens the built site locally; click through Lessons, a lesson's Teacher tab, Downloads, Exams, Present
```

Also check the level picker (`#/`), Level 1 (`#/level1`, `#/level1/lesson/1` and its Teacher and Downloads tabs, `#/level1/present/1`),
and that the old Level 2 links still work (`#/lesson/3`, `#/present/3`, `#/downloads`, `#/exams`).

## 7. Publish

```bash
git add -A
git status                         # look at the list: no node_modules, dist, build folders, .wav masters or passwords
git commit -m "Describe your change"
git push origin main
```

For bigger changes you can work on a branch instead (`git switch -c my-change`, push it, open a pull request on GitHub,
and merge it into `main` with **Create a merge commit**). Nothing is published until the change is on `main`.

Pushing to `main` starts the **Deploy to GitHub Pages** workflow (`.github/workflows/pages.yml`). It builds the site and
publishes it to https://sdpursley.github.io/ESL-Curriculum/ in 1–2 minutes. Watch it on the repository's **Actions** tab;
a red X means the build failed (click it to see why) and the old site stays online. The repository's Pages source
must stay set to **GitHub Actions** (Settings → Pages).

You can also make small text edits directly on github.com (open a file, click the pencil, "Commit changes"); that
publishes the same way. Rebuilding the PDF, pictures, or audio needs a computer.

## 8. Level 1

Level 1 (beginner) has **13 lessons, all finished and published** (Lessons 1–13). It was built one lesson at a time; a lesson
whose Markdown file is missing shows as "coming soon" on the website. Level 1 uses the same tools as Level 2, with its files kept apart so names never collide
(Level 1 pictures live in `level1/images/` and `public/level1/images/`: Lesson 1 = `L1_<word>.png`, Lessons 2+ = `L1_L<N>_<word>.png`).

### What is where (Level 1)

| Folder / file | What it is |
|---|---|
| `level1/curriculum/Level1_Scope_and_Sequence.md` | The plan for all 16 weeks. **The website takes the Level 1 lesson list, titles, weeks, semester table, and class routine from here** (section 5 "The Semester at a Glance" and 4.1). |
| `level1/curriculum/Level1_Lesson1.md` … `Level1_Lesson13.md` | **Lesson text**: teacher plan + student pages. The lesson page, the PDF, and the DOCX all come from this file. |
| `level1/curriculum/build.sh`, `md2docx_L1.py` | Build the lesson DOCX + PDF. `md2docx_L1.py` is the Level 2 converter plus one table type (`<!-- grid -->`, for the alphabet grids); a one-picture table prints as one big picture (Lesson 4 family trees). |
| `level1/images/` | Vocabulary pictures (600×420 PNG), `images_L1.json` / `images_L1_L<N>.json` (what each picture shows), `CREDITS.md` (one section per lesson), and `tools/make_images_L1.py`, `tools/make_images_L1_L<N>.py` (the drawing scripts; Lessons 2+ use the helpers in `tools/lib/`). |
| `level1/audio/` | `L1_listening.mp3` and `L1_L<N>_listening.mp3` (**the published audio**), check results and regen logs, `README.md` (Lesson 1) and `L1_L<N>_README.md`, and `tools/` (Lesson 1 scripts; `tools/lessons/` = the shared builder and checker for Lessons 2+, with `script_L1_L<N>.py`). The WAV masters are not committed. |
| `level1/slides/Level1_Lesson<N>_Slides.pptx` | **The editable slide decks** (source for the downloads and the in-browser presenter). |
| `level1/exams/` | **Week 8 Midterm and Week 15 Final**: the four Markdown files (teacher packet + student test for each), `images/` (+ `CREDITS.md`), `audio/` (`L1_Midterm_listening.mp3`, `L1_Final_listening.mp3`, check results, READMEs), and `build/` (`exam_data.py` = every item and key, `make_exam_md.py`, `build_all.sh`, `check_consistency.py`, `audio/` scripts). See "Exams" below. |
| `public/level1/` | What the website serves. **Don't edit here**: it is refreshed from the folders above. |

### Rebuild after a change (any Level 1 file)

```bash
PYTHON=.venv-docs/bin/python level1/curriculum/build.sh 1 --publish    # Lesson 1 DOCX + PDF -> public/level1/downloads/ (2 … 13 for the other lessons)
python3 scripts/export_deck.py level1/slides/Level1_Lesson1_Slides.pptx 1 --level 1   # only if the slides changed (same for Lesson<N>, N)
python3 scripts/export_content.py                                     # lesson pages + copies pictures, MP3, PPTX into public/level1/
npm run dev                                                           # check #/level1/lesson/1 and #/level1/present/1
```

`export_content.py` rebuilds the Level 2 data too; it produces exactly the same Level 2 files if you didn't change Level 2.
Without `--publish`, `build.sh` writes to `level1/curriculum/build/` (not committed) so you can look first.

**Lesson text:** edit `level1/curriculum/Level1_Lesson1.md`. Keep the headings and the `<!-- part: ... -->` comments:
the website finds the teacher plan between `<!-- part: Teacher Plan` and `<!-- part: Student Workbook`, and makes one
student section for each `## ` heading after that (`## Lesson 1 (Week 1): ...` = New Words in Lesson 1; from Lesson 2 on, that first page is named after its first task, e.g. Hello + Review, and `· New Words` holds the pictures; `## Lesson 1 (Week 1) · Listening`, …) up to
`## Picture Credits`. The New Words picture table becomes the word cards (a picture cell is `![word](images/...png)<br>★ **word**`;
the bold is optional); the audio player goes at the top of the Listening section. Lessons 5–13 add pages such as several
`· Talk Time (Student A ...)` pages (the website keeps both full names) and `· Real-World Reading` (Lessons 8–13, in place of Letters & Numbers).

**Slides:** open `level1/slides/Level1_Lesson1_Slides.pptx` in PowerPoint or LibreOffice Impress, edit, save with the same name
(.pptx), then run the deck export and `export_content.py` above. Each "on click" entrance animation is one reveal step.
Pictures in the deck must be identical to a file in `level1/images/` (the export stops and names the picture if not).

**Pictures:** see section 4. For Level 1, run the script from its folder:
`cd level1/images/tools && ../../../.venv-img/bin/python make_images_L1.py` (writes into `level1/images/`), and add a line to `level1/images/CREDITS.md`.

### Swap the listening audio (for example, a new recording)

The website always plays `level1/audio/L1_listening.mp3` (copied to `public/level1/audio/L1_listening.mp3`). To use a different recording:

1. Listen to the whole new file. It should play the conversation **once** (intro → conversation → "That's the end of the listening.").
2. Copy it over the old one with the **same name**: `cp path/to/new_recording.mp3 level1/audio/L1_listening.mp3`
3. Optional but recommended: check it against the script (needs the audio setup from section 5):
   `.venv-audio/bin/python level1/audio/tools/check_L1.py level1/audio/L1_listening.mp3` (writes `L1_check_results.json` in the current folder; move it into `level1/audio/`).
4. If the length changed, update "about 1:16" (the length) in the listening-script heading of `Level1_Lesson1.md`.
5. Run the rebuild commands above (`build.sh 1 --publish` only if you changed the Markdown), then publish (section 7).

**Make the audio from scratch** (same Chatterbox setup as section 5; the words are in `level1/audio/tools/script_L1.py`, keep them the same as the Markdown):

```bash
cd level1/audio/tools
SINGLE=1 TRIES=6 SEED0=2026 EXAG=0.55 CFG=0.45 ../../../.venv-audio/bin/python build_L1_audio.py     # -> out/L1_listening.wav + .mp3 + L1_regen_log.json
LINE_TIMES=out/L1_regen_log.json ../../../.venv-audio/bin/python check_L1.py out/L1_listening.mp3   # -> L1_check_results.json
```

Level 1 differences from Level 2: longer pauses, and spelled names (`{R, U, I, Z.}` in the script) are made as one piece and then
spaced out letter by letter. To redo only pieces that failed (same settings, so the build finds them in its cache):
`SEED0=2026 EXAG=0.55 CFG=0.45 JOBS='[["Ana", "Hello. Thank you."]]' ../../../.venv-audio/bin/python fix_chunks.py`, then run
`build_L1_audio.py` again (it reuses everything else from `cache/`). `out/` and `cache/` are not committed; copy the finished MP3 and the two JSON files into `level1/audio/`.

**The published file (October 2026)** uses more natural voices for Ana and Carlos: `level1/audio/tools/natural/build_natural.py`
makes each of their lines as one whole take (`EXAG=0.72 CFG=0.32`, several seeds, the best take that passes the checks is kept) and
reuses the narrator and receptionist takes from the build above (so run `build_L1_audio.py` once first). Ana's voice reference is
`level1/audio/tools/natural/kokoro_refs/af_jessica.wav`, a synthetic clip made with Kokoro-82M (Apache 2.0; no human recording).
It is committed; `make_ana_ref.py` remakes it (details in `ana_ref.json`). Carlos uses the Kokoro-made `Sam` clip in `tools/audio/samples/refs/`.
The exact command is at the top of `build_natural.py`. Every voice reference must be a synthetic (Kokoro-made) clip, not a recording of a real person.

### Lessons 2–13: pictures and audio

**Pictures:** `cd level1/images/tools && ../../../.venv-img/bin/python make_images_L1_L2.py` (or `_L3` … `_L13`) writes the PNGs and
`images_L1_L<N>.json` into `level1/images/`. The helpers are in `tools/lib/make_images.py` (Twemoji SVGs are downloaded into
`tools/lib/_twemoji_src/`, not committed). `tools/lib/make_credits.py N ../..` drafts that lesson's credits section
(`CREDITS_L1_L<N>.new.md`, not committed); paste it over the lesson's section in `level1/images/CREDITS.md`.

**Audio:** the shared builder is `level1/audio/tools/lessons/build_listening.py`; the words for each lesson are in
`script_L1_L<N>.py` (keep them the same as the Markdown). Every voice is a synthetic Kokoro-82M clip (`refs.py`, `REFS.md`):
the clips in `tools/audio/samples/refs/` and Ana's `level1/audio/tools/natural/kokoro_refs/af_jessica.wav`. `engine.py` refuses any other file.

```bash
cd level1/audio/tools/lessons
python3 script_match.py ../../../curriculum/Level1_Lesson2.md script_L1_L2.py                        # the Markdown script and script_L1_L2.py must match (0 mismatches)
../../../../.venv-audio/bin/python build_listening.py script_L1_L2.py $PWD/out/L1_L2_listening      # -> out/L1_L2_listening.wav/.mp3 + _log.json
../../../../.venv-audio/bin/python check_listening.py script_L1_L2.py out/L1_L2_listening.mp3 out/L1_L2_listening_log.json out/L1_L2_check_results.json
../../../../.venv-audio/bin/python second_opinion.py script_L1_L2.py out/L1_L2_listening.mp3       # optional: Whisper medium.en
../../../../.venv-audio/bin/python verify24.py script_L1_L2.py out/L1_L2_listening.wav out/L1_L2_listening_log.json  # optional: re-check each line on the 24 kHz WAV
```

`canon.py` makes the check fair to numbers, prices, times, and dates (for example "$3.50", "6:30", "o'clock", "March 3rd").
Whisper results vary a little from run to run, so a second check can flag a different word; listen to any flagged line.

Each sentence is one whole Chatterbox take (`EXAG=0.72 CFG=0.32`, several seeds; the best take that passes Whisper, edge,
artifact, and pitch checks is kept). If a take is rejected later, add `EXCLUDE='{"<sentence>": [<seed>]}'` and run the build again
(takes are cached in `cache/`). Copy `out/L1_L<N>_listening.mp3` into `level1/audio/`, the log as `L1_L<N>_regen_log.json` and the
check as `L1_L<N>_check_results.json`; `out/` and `cache/` are not committed. Details for each lesson: `level1/audio/L1_L<N>_README.md`.

**Second checks and the vote.** `takes_medium.py` runs Whisper medium.en on each chosen take, and `vote_takes.py script_L1_L<N>.py out/L1_L<N>_listening_log.json 3`
runs small.en and medium.en (float32, `cpu_threads=1`) three times on each take: a take is OK if **either** model hears it exactly in most runs.
Retake a line only when both checkers fail it, or for pitch (male voices under about 150 Hz) or clipping. Spelled letters and digit strings always score low: check those by ear.
All Level 1 checkers use `cpu_threads=1` (multi-threaded int8 gave different text from run to run on a busy machine).
**Run only one Chatterbox or Whisper process at a time** (two ran out of memory on a 15 GB machine): put `flock /tmp/chatterbox.lock` in front of each command.

### Add or replace a lesson (example: Lesson 5)

All 13 lessons exist, so this is now the recipe for rewriting one.

1. Edit `level1/curriculum/Level1_Lesson5.md` (a new lesson starts from a copy of the one before it), with the same parts and heading pattern
   (`## Lesson 5 (Week 5): ...` = the first page, `## Lesson 5 (Week 5) · New Words` = the picture page, `## Lesson 5 (Week 5) · Listening`, …).
   Use the title and week from the scope and sequence. If there are two Talk Time pages, the website keeps both full names.
2. Pictures: `level1/images/L1_L5_<word>.png` (made by `level1/images/tools/make_images_L1_L5.py`); link them as `images/L1_L5_<word>.png`
   in the Markdown, and add a Lesson 5 section to `level1/images/CREDITS.md`.
3. Audio: `level1/audio/L1_L5_listening.mp3` (write `level1/audio/tools/lessons/script_L1_L5.py` and build it as above).
4. Slides: `level1/slides/Level1_Lesson5_Slides.pptx`, then `python3 scripts/export_deck.py level1/slides/Level1_Lesson5_Slides.pptx 5 --level 1`.
5. `level1/curriculum/build.sh 5 --publish`, then `python3 scripts/export_content.py`.
   The lesson page, presenter (`#/level1/present/5`), downloads, lesson list, and the "ready" notes update by themselves;
   no website code changes are needed.

### Exams (Week 8 Midterm, Week 15 Final)

The website page is `#/level1/exams` (the Week 8 and Week 15 cards on the Level 1 home page link to it). The items, answers, and points
are in `level1/exams/build/exam_data.py`; everything else is made from it.

```bash
IMGPY=.venv-img/bin/python PYTHON=.venv-docs/bin/python level1/exams/build/build_all.sh            # pictures + 4 Markdown files + DOCX/PDF in level1/exams/build/out/ + consistency check
IMGPY=.venv-img/bin/python PYTHON=.venv-docs/bin/python level1/exams/build/build_all.sh --publish  # same, and copies the packets (PDF+DOCX) and student tests (PDF) to public/level1/downloads/exams/
python3 scripts/export_content.py                                                                   # exam cards, parts tables, file sizes; copies the exam MP3s to public/level1/audio/
```

`check_consistency.py` must end with **0 failed**: it checks that the student test, the teacher steps, and the key agree item by item,
that every picture exists, and that no banned word appears (add more with `BANNED_EXTRA="word1,word2"`). Its report is
`level1/exams/build/consistency_report.txt` (not committed). Packets are 14 pages, student tests 4 pages.

**Exam audio** (same Chatterbox setup, `EXAG=0.72 CFG=0.32`; Midterm = Narrator, Receptionist, Marco; Final = Narrator, Kim, Carlos (the `Sam` clip)):

```bash
cd level1/exams/build/audio
bash run_audio.sh Midterm        # Chatterbox build under flock $LOCK (default /tmp/chatterbox.lock) -> out/ (not committed)
bash finish_audio.sh Midterm     # every check + the vote; copies MP3, log, check results and README into level1/exams/audio/
```

If a line fails both checkers, run `EXCLUDE='{"<sentence>": [<seed>]}' bash run_audio.sh Midterm` and `finish_audio.sh` again. The length
("about 1:17") is read from `level1/exams/audio/L1_<Midterm|Final>_check_results.json`, so run `build_all.sh --publish` again afterwards. Every voice is a Kokoro-made clip (see `level1/audio/tools/lessons/REFS.md`).

### Publish

The same as Level 2 (sections 6–7). Before you commit, check that `git status` shows no `.wav` files, no `level1/curriculum/build/`,
no `level1/exams/build/out/`, and no `cache/` or `out/` folders (`.gitignore` already skips them).

## 9. Level 3

Level 3 (low intermediate) works exactly like Level 1 (section 8), with `level3` in place of `level1`. Lesson 1 is finished;
Lessons 2–13 show as "coming soon" until their Markdown file exists. Level 3 pictures are called `L3_L<N>_*.png`
(Level 3, lesson *N*), for example `L3_L1_neighbor.png`.

### What is where (Level 3)

| Folder / file | What it is |
|---|---|
| `level3/curriculum/Level3_Scope_and_Sequence.md` (+ `.docx`, `.pdf`) | The plan for all 16 weeks. **The website takes the Level 3 lesson list, titles, weeks, semester table, and class routine from here.** |
| `level3/curriculum/Level3_Lesson1.md` | **Lesson 1 text**: teacher plan + student pages. The lesson page, the PDF, and the DOCX all come from this file. |
| `level3/curriculum/build.sh`, `md2docx_L3.py` | Build the lesson DOCX + PDF. `md2docx_L3.py` is the same converter as `md2docx_L1.py` (incl. the `<!-- subst -->` grammar boxes). |
| `level3/images/` | Vocabulary pictures (`L3_L1_*.png`), `images_L3_L1.json`, `CREDITS.md`, and `tools/make_images_L3_L1.py` (the drawing script; uses `tools/images/`). |
| `level3/audio/` | `L3_L1_listening.mp3` (**the published audio**), check results and build log, `README.md`, and `tools/` (script, build, and check scripts). The WAV master is not committed. |
| `level3/slides/Level3_Lesson1_Slides.pptx` | **The editable slide deck** (source for the download and the in-browser presenter). |
| `public/level3/` | What the website serves. **Don't edit here**: it is refreshed from the folders above. |

### Rebuild after a change (any Level 3 file)

```bash
PYTHON=.venv-docs/bin/python level3/curriculum/build.sh 1 --publish    # Lesson 1 DOCX + PDF -> public/level3/downloads/
python3 scripts/export_deck.py level3/slides/Level3_Lesson1_Slides.pptx 1 --level 3   # only if the slides changed
python3 scripts/export_content.py                                     # lesson pages + copies pictures, MP3, PPTX into public/level3/
npm run dev                                                           # check #/level3/lesson/1 and #/level3/present/1
```

`export_content.py` rebuilds the Level 1 and Level 2 data too; they come out exactly the same if you didn't change them.
Without `--publish`, `build.sh` writes to `level3/curriculum/build/` (not committed). Lesson text, slides, and pictures follow the
same rules as Level 1 (section 8): keep the headings and `<!-- part: ... -->` comments, each "on click" entrance animation is one
reveal step, and pictures in the deck must be identical to a file in `level3/images/`.

**Pictures:** `cd level3/images/tools && ../../../.venv-img/bin/python make_images_L3_L1.py` (writes into `level3/images/`); add a line to `level3/images/CREDITS.md`.

### Listening audio

The website plays `level3/audio/L3_L1_listening.mp3`. To swap it, copy a new file over it with the same name, update
"about 1:31" in the listening-script heading of `Level3_Lesson1.md`, and run the rebuild commands above.

**Make the audio from scratch** (same Chatterbox setup as section 5; the words are in `level3/audio/tools/script_L3_L1.py`, keep them the same as the Markdown):

```bash
cd level3/audio/tools
PAUSE_SPK=1.2 MAXT=24 ../../../.venv-audio/bin/python build_L3_L1.py                     # -> out/L3_L1_listening.wav + .mp3 + _log.json
LINE_TIMES=out/L3_L1_listening_log.json ../../../.venv-audio/bin/python check_L3_L1.py out/L3_L1_listening.mp3   # -> L3_L1_check_results.json
```

Each line is one whole Chatterbox take (several seeds; the best take that passes Whisper, edge, artifact, and pitch checks is kept).
If the whole-file check rejects a take, run the build again with `EXCLUDE='{"<line text>": [<seed>]}'`; the seed used for every line is in
`L3_L1_listening_log.json`. Copy the finished MP3 and the two JSON files into `level3/audio/`; `out/` and `cache/` are not committed.
Voices: Narrator = `N`, Elena = `Rosa`, David = `Sam`, all synthetic Kokoro-82M clips in `tools/audio/samples/refs/` (no human recordings).
`level3/audio/tools/textnorm.py` is the shared `tools/audio/textnorm.py` plus one fix (Whisper writes "OK" as "okay"); it is found first.
Whisper results can differ slightly between runs; if one line fails the whole-file check, check that line again before re-making it.

### Add the next lesson (example: Lesson 2)

As in section 8: `level3/curriculum/Level3_Lesson2.md`, pictures `level3/images/L3_L2_<word>.png`, audio `level3/audio/L3_L2_listening.mp3`,
slides `level3/slides/Level3_Lesson2_Slides.pptx` (built with `scripts/slides/build_deck.py` from `level3/slides/specs/`, see AGENTS.md section 6; then `export_deck.py ... 2 --level 3`), then `level3/curriculum/build.sh 2 --publish` and
`python3 scripts/export_content.py`. Update the "Lesson 1 is ready" sentence on the Level 3 overview in `src/level3.tsx`.

### Publish

The same as Level 2 (sections 6–7). Before you commit, check that `git status` shows no `.wav` files, no `level3/curriculum/build/`,
and no `cache/` or `out/` folders.

## Licenses (keep these when you change things)

- Course materials: © 2026 the authors, CC BY-NC-SA 4.0.
- Vocabulary pictures: modified Twemoji graphics, CC BY 4.0 (see `public/images/CREDITS.md` and `level1/images/CREDITS.md`, `level1/exams/images/CREDITS.md`, `level3/images/CREDITS.md`).
- Font for slides and the presenter: Lexend Deca, SIL Open Font License 1.1 (`src/assets/fonts/`).
- Audio: made with Chatterbox TTS (Resemble AI, MIT License); synthetic voices with a Perth watermark. Every voice reference is a synthetic Kokoro-82M clip (Apache 2.0), never a recording of a real person.
