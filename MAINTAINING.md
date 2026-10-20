# Maintaining the Level 2 ESL Curriculum

This guide explains how to change and rebuild everything in this repository: the curriculum book (PDF/DOCX),
the exams, the website, the slide decks, the vocabulary pictures, and the listening audio.
You do not need to be a programmer. Copy the commands as written, and run them from the repository folder.

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

> **Known difference:** `src/content.json` currently has one sentence that was updated by hand and is not yet in the
> Markdown: in the Teacher Guide introduction, "Audio files are in `audio/` (L1_listening.mp3 … L13_listening.mp3, plus the
> exam files …)". The Markdown (and the PDF) still say audio exists only for Lessons 1–4. Before you run
> `export_content.py`, fix that sentence in the Markdown (search for "Audio files are in"), or the website will go back
> to the old wording. The Markdown also still says "the audio is coming later" in "0. About This Edition" and
> "Lessons 5–13 and exam audio are not produced yet" in section 6; update those at the same time.

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

## 7. Publish

```bash
git add -A
git status                         # look at the list: no node_modules, dist, build folders, .wav masters or passwords
git commit -m "Describe your change"
git push origin main
```

Pushing to `main` starts the **Deploy to GitHub Pages** workflow (`.github/workflows/pages.yml`). It builds the site and
publishes it to https://sdpursley.github.io/ESL-Curriculum/ in 1–2 minutes. Watch it on the repository's **Actions** tab;
a red X means the build failed (click it to see why) and the old site stays online. The repository's Pages source
must stay set to **GitHub Actions** (Settings → Pages).

You can also make small text edits directly on github.com (open a file, click the pencil, "Commit changes"); that
publishes the same way. Rebuilding the PDF, pictures, or audio needs a computer.

## Licenses (keep these when you change things)

- Course materials: © 2026 the authors, CC BY-NC-SA 4.0.
- Vocabulary pictures: modified Twemoji graphics, CC BY 4.0 (see `public/images/CREDITS.md`).
- Font for slides and the presenter: Lexend Deca, SIL Open Font License 1.1 (`src/assets/fonts/`).
- Audio: made with Chatterbox TTS (Resemble AI, MIT License); synthetic voices with a Perth watermark.
