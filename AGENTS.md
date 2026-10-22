# AGENTS.md: how to build and check new lessons, audio, and exams

This file is for anyone who continues this curriculum without the owner at the keyboard: another AI coding tool or a person.
Follow it exactly. When this file and another doc disagree, this file wins for the rules, and [MAINTAINING.md](MAINTAINING.md) has the longer how-to.
All commands run from the repository root unless a step says `cd`.

**Get the owner's approval before you publish anything** (before merging into `main`: a push to `main` deploys the public website).

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
| Level 3 drafts (Lessons 2–13, not on the website) | | | `level3/drafts/` (`curriculum/`, `images/`, `audio/`, `audio/tools/`); status `level3/AUDIO_STATUS.md`; see section 6 |
| Voice reference clips | `tools/audio/samples/refs/*.wav` and `level1/audio/tools/natural/kokoro_refs/af_jessica.wav` (list: `level1/audio/tools/lessons/REFS.md`) | `tools/audio/samples/refs/` | `tools/audio/samples/refs/` |
| Slide decks (source) | `level1/slides/Level1_Lesson<N>_Slides.pptx` | `public/downloads/slides/Lesson<N>_Slides.pptx` | `level3/slides/Level3_Lesson<N>_Slides.pptx` |
| Website files (generated, don't edit by hand) | `public/level1/` (images, audio, downloads, downloads/slides, downloads/exams) | `public/images/`, `public/audio/`, `public/downloads/` | `public/level3/` |
| Website data (generated) | `src/content_level1.json`, `src/decks/level1/lesson<N>.json` | `src/content.json`, `src/sizes.json`, `src/decks/lesson<N>.json` | `src/content_level3.json`, `src/decks/level3/lesson<N>.json` |
| Page code | `src/level1.tsx` | `src/App.tsx` | `src/level3.tsx` |

Shared scripts:

- `scripts/export_content.py`: writes all the website data (`src/content*.json`, `src/sizes.json`) and copies the Level 1 / Level 3 pictures, MP3s, and PPTX from `level1/`, `level3/` into `public/level1/`, `public/level3/`. It also copies the Level 1 exam MP3s and lists the exam files. It rebuilds Level 2 data too; unchanged sources give byte-identical files.
- `scripts/export_deck.py <pptx> <N> [--level 1|3]`: PowerPoint deck → presenter JSON. It stops if a picture in the deck is not identical to a file in the level's `public/.../images/`.
- `scripts/check_slides.py <pptx ...>`: every click animation targets a shape that exists.
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
6. **Slides.** Make or edit `level1/slides/Level1_Lesson<N>_Slides.pptx`. **Presenter rules:**
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
10. **PR.** Follow section 8 and ask the owner for approval before you merge.

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

---

## 6. Running audio locally (Level 3 Lessons 2–13 drafts)

Lessons 2–13 of Level 3 are **drafts** in `level3/drafts/` (`curriculum/`, `images/`, `audio/`, `audio/tools/`). The website does not read
this folder, so nothing here changes the live site. Which lessons still need audio is in [`level3/AUDIO_STATUS.md`](level3/AUDIO_STATUS.md):
**done**, **partial**, or **to-do**, with the lines that remain. Work on the branch `level3-L2-13-audio-handoff`.
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
   git switch level3-L2-13-audio-handoff && git pull
   git add level3/drafts/audio/L3_L<N>_* level3/AUDIO_STATUS.md level3/drafts/curriculum/Level3_Lesson<N>.md
   git status --short | grep -iE '\.wav|\.onnx|\.bin|\.pt|venv|cache/|out/' && echo STOP   # must print nothing
   git commit -m "Level 3 Lesson <N> draft listening audio" && git push origin level3-L2-13-audio-handoff
   ```
   A normal push only, never force-push. Moving drafts onto the website (into `level3/curriculum/`, `level3/images/`, `level3/audio/`) is a separate step that needs the owner's approval.

---

## 7. Never commit

- `node_modules/` or `dist/`
- Python environments (`.venv*`)
- Model weights (`models/`, `*.onnx`, `*.bin`, `*.pt`, `*.safetensors`)
- WAV files, except the committed reference clips in `tools/audio/samples/refs/` and `level1/audio/tools/natural/kokoro_refs/`
- `cache/`, `out/`, or `build/` output folders
- `_twemoji_src/`
- `__pycache__/`
- Secrets or tokens of any kind

`.gitignore` covers most of these. Still check `git status` before every commit.

## 8. Repository rules

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
