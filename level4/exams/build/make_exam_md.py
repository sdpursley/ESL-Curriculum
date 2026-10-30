"""Write the exam sources (.md) and the listening scripts + casts for one level (Levels 3-5) from exam_data.py.
Usage: python3 make_exam_md.py [OUT_DIR]   (default: the exams folder)
The same file is in level3/, level4/ and level5/exams/build/ (copied from the Level 1 exam build and made general);
everything that differs between levels is in exam_data.py.
Writes: OUT/Level{V}_{K}_Student_Test.md, OUT/Level{V}_{K}_Exam_Teacher_Packet.md,
        build/audio/script_L{V}_{K}.py and build/audio/cast/cast_L{V}_{K}.json (the format of the level's lesson audio tools)."""
import os, sys, json, re
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import exam_data as D
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 and not sys.argv[1].startswith('-') else os.path.abspath(os.path.join(HERE, '..'))
V = D.LEVEL; C = D.CFG
os.makedirs(OUT, exist_ok=True)
NAME = 'Name: ______________________________     Date: ________________'
LIC = ('*© 2026 the authors, CC BY-NC-SA 4.0. Provided as-is, without warranty. Names, places and numbers are invented. '
       'No pictures are used in these tests.*')
LET = 'abc'

# ---------- helpers ----------
def words_in(s): return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'’.:$-]*", s))
def sentences_in(s): return len([x for x in re.split(r'(?<!\bMr\.)(?<!\bMs\.)(?<!\bDr\.)(?<!\bMrs\.)(?<=[.!?])\s+', s.strip()) if x])
def est_seconds(E):
    """Length estimate fitted on the recorded Level 3-5 lesson files: 0.331 s per word + 1.446 s per line (pauses)."""
    lines = [E['intro']] + [l[1] for l in E['lines']] + [E['end']]
    return round(0.331 * sum(words_in(x) for x in lines) + 1.446 * len(lines))
def mmss(s): return f'{int(s // 60)}:{int(round(s % 60)):02d}'
def audio_len(E):
    p = os.path.join(OUT, 'audio', E['audio'].replace('_listening.mp3', '_check_results.json'))
    if os.path.exists(p): return mmss(json.load(open(p))['duration_s']), True
    return mmss(est_seconds(E)), False
def speakers(E): return sorted({l[0] for l in E['lines'] if l[0] != 'Narrator'})
def letter(it): return LET[it['opts'].index(it['ans'])] if it['kind'] == 'mc' else ''
def key_text(it):
    if it['kind'] == 'mc': return f'{letter(it)}. {it["ans"]}'
    return it['ans']
def opt_line(it):
    if it['kind'] == 'mc': return '   ' + '      '.join(f'**{LET[k]}.** {o}' for k, o in enumerate(it['opts']))
    if it['kind'] == 'tf': return '   **True**      **False**'
    return None
def stem(it):
    if it['kind'] == 'tf': return f'True or false? {it["q"]}'
    return it['q']
def points(E): return dict(A=len(E['listening']), B=len(E['words']['items']), C=len(E['grammar']) + len(E['fix']),
                           D=len(E['reading']['items']), E=C['writing_points'])
def total(E): return sum(points(E).values())
def score_line(E):
    P = points(E)
    return '**Score:** ' + ' · '.join(f'{k} ____ /{v}' for k, v in P.items()) + f' · **Total ____ /{total(E)}**'
def by_lesson(pairs):
    """[(item, lesson)] -> 'L1: 1, 2 · L2: 3–5'"""
    g = {}
    for i, l in pairs: g.setdefault(l, []).append(i)
    def rng(xs):
        out, a = [], xs[0]
        for j in range(1, len(xs) + 1):
            if j == len(xs) or xs[j] != xs[j - 1] + 1:
                b = xs[j - 1]; out.append(str(a) if a == b else f'{a}–{b}' if b > a + 1 else f'{a}, {b}')
                if j < len(xs): a = xs[j]
        return ', '.join(out)
    return ' · '.join(f'L{l}: {rng(sorted(v))}' for l, v in sorted(g.items(), key=lambda kv: min(kv[1])))
def items(lst, start=1):
    L = []
    for i, it in enumerate(lst, start):
        if it['kind'] == 'tf':   # True / False on the same line as the sentence
            L += [f'{i}. {stem(it)}   ( **True** / **False** )', '']; continue
        L.append(f'{i}. {stem(it)}')
        o = opt_line(it)
        if o: L.append(o)
        L.append('')
    return L

# ---------- student test ----------
def student(E):
    t = E['title']; P = points(E); R = E['reading']; W = E['words']
    L = [f'<!-- mode: {C.get("student_mode", "student")} -->', f'## Level {V} · {t} · Test', '', NAME, '',
         f'### A. Listening ({P["A"]} points)', '',
         f'{E["listen_task"]} You will hear the audio two times.', '', f'*{E["scene"]}*', '']
    L += items(E['listening'])
    L += ['<!-- pagebreak -->', f'### B. Words ({P["B"]} points)', '',
          f'Write a word or phrase from the box in each sentence. Use each one once. You will not use {len(W["box"]) - len(W["items"])} of them.', '',
          '> ' + '  ·  '.join(f'**{w}**' for w in W['box']), '']
    for i, (s, a, les) in enumerate(W['items'], 1): L += [f'{i}. {s}', '']
    nG = len(E['grammar']); nF = len(E['fix'])
    L += [f'### C. Grammar ({P["C"]} points)', '', f'**Part 1.** Circle the correct words ({nG} points).', '']
    for i, (s, ch, a, les) in enumerate(E['grammar'], 1): L += [f'{i}. {s} ( **{ch[0]}** / **{ch[1]}** )', '']
    L += C.get('break_before_fix', []) + [f'**Part 2.** Each sentence has **one** mistake. Write the correct sentence ({nF} points).', '']
    for i, f in enumerate(E['fix'], nG + 1):
        L += [f'{i}. {f["wrong"]}', '   ______________________________________________________________', '']
    L += C.get('break_before_reading', ['<!-- pagebreak -->']) + [f'### D. Reading ({P["D"]} points)', '', 'Read the text. Then answer the questions. Circle the answer or write one word or number.', '',
          f'> **{R["title"]}**', '>']
    for k, para in enumerate(R['text']):
        L.append(f'> {para}')
        if k < len(R['text']) - 1: L.append('>')
    L += ['']
    L += C.get('break_before_reading_q', []) + items(R['items'])
    L += C.get('break_before_writing', ['<!-- pagebreak -->']) + [f'### E. Writing ({P["E"]} points)', '',
          f'Choose **one** task. Write {C["writing_len"]}. Give at least one reason.', '']
    for k, (tt, pr, bl) in enumerate(E['writing']['tasks'], 1):
        L += [f'**Task {k}: {tt}.** {pr}', '']
        L += [f'- {b}' for b in bl] + ['']
    L += ['I chose:   ☐ Task 1     ☐ Task 2', '']
    L += ['______________________________________________________________________', ''] * C['writing_lines']
    L += [score_line(E), '']
    return '\n'.join(L)

# ---------- teacher packet ----------
def rubric_table(rows, cols):
    L = ['| ' + ' | '.join(cols) + ' |', '|' + '---|' * len(cols)]
    L += ['| ' + ' | '.join(r) + ' |' for r in rows]
    return L

def packet(E):
    t = E['title']; K = E['key']; mid = K == 'Midterm'; P = points(E); tot = total(E)
    alen, real = audio_len(E); R = E['reading']; W = E['words']
    nG = len(E['grammar']); nF = len(E['fix'])
    meets = round(tot * 0.78); almost = round(tot * 0.52)
    nxt = C['next']; clk = C['clock']
    L = ['<!-- mode: guide -->', f'# Level {V} · {t}: Teacher Packet', '',
         f'**{K} Exam · {E["lessons"]}** · Level {V} Adult ESL', '',
         '**Contents**', '',
         '- How to use this packet', '- Step-by-step directions and clock-time plan', '- Speaking interview and rubric',
         '- Listening script', '- Answer key (with where each answer is in the audio and in the reading)', '- Scoring guide (proposed score bands)',
         '- Teacher notes',
         '- Papers to copy: Speaking Interview Card (teacher), Speaking Task Cards, Score Sheet (teacher), Can-Do Self-Check, one-page Answer Key (teacher)', '',
         '<!-- mode: teacher -->', '## How to Use This Packet', '',
         f'- **The test for learners is a separate file:** `Level{V}_{K}_Student_Test.pdf` (no answers, no cover page). Print 1 per learner + 3 extra.',
         '- **This packet** is for you: directions, the listening script, the answer key, the scoring guide, and the speaking papers.',
         (f'- **Audio:** `audio/{E["audio"]}` (about {alen}). The recording is in the file **once**. Press play again for the second listen.' if real else
          f'- **Audio:** the recording `{E["audio"]}` is not ready yet (the script is about {alen} long). Until it is ready, read the listening script aloud two times, at a natural speed. Two readers are better: one reads the women\'s lines and one reads the men\'s lines.'),
         '- **All instructions are in English.** Read each instruction aloud once and show an example on the board if learners look unsure.', '',
         f'## {t}: Step by Step', '', '### What the test has', '',
         '| Part | What learners do | Points | Time |', '|---|---|---|---|',
         f'| A. Listening | {E["listen_parts"]} Circle an answer, mark true or false, or write one word ({len(E["listening"])} items). | {P["A"]} | {clk["A"]} |',
         f'| B. Words | Complete sentences with words from a box ({len(W["items"])} items). | {P["B"]} | {clk["BC"]} for B + C |',
         f'| C. Grammar | Part 1: circle the correct words ({nG} items). Part 2: find and fix one mistake in each sentence ({nF} items). | {P["C"]} | (with B) |',
         f'| D. Reading | Read a text of about {words_in(" ".join(R["text"]))} words. Answer {len(R["items"])} questions. | {P["D"]} | {clk["D"]} |',
         f'| E. Writing | Choose one of two tasks. Write {C["writing_len"]}. | {P["E"]} | {clk["E"]} |',
         f'| **Written total** | | **{tot}** | **{C["written_min"]} min** |',
         f'| Speaking interview | Pairs with the teacher, during the written parts. Scored with the rubric, not added to the written total. | 3–9 | {C["speak_min"]} min per pair |', '',
         f'*Covers {E["lessons"]}. {E["covers"]}*', '',
         '### Before class (20 minutes)', '',
         f'1. Print the student test (1 per learner + 3). From this packet, print the Speaking Task Cards (1 set per pair), the Score Sheet, and the Self-Check (1 per learner).',
         (f'2. Put `{E["audio"]}` on a phone. Connect a small speaker. Play the first seconds to check the volume.' if real else
          '2. The recording is not ready yet: ask a second reader to help, and read the listening script through once before class.'),
         '3. Set 2 chairs and 1 chair for you in a quiet corner (for the speaking interviews).',
         '4. Have pencils, a clock or timer, and the class list.', '']
    for st in C['steps']:
        L += [f':::step {st[0]}'] + [f'- {x}' for x in st[1]] + [':::', '']
    L += ['### Clock-time plan', '', '| Time | Whole class | Teacher |', '|---|---|---|']
    L += [f'| {a} | {b} | {c} |' for a, b, c in C['clock_plan']] + ['']
    L += [':::box Speaking interview (' + f'{C["speak_min"]} minutes per pair)',
          '- **Part 1 (about 2 minutes).** Ask each learner 2 of the questions on the Speaking Interview Card. After each answer, ask one follow-up question (Why? When? Who with? What happened next?).',
          '- **Part 2 (about 2 minutes).** Give the pair one Task Card. They read it for 20 seconds and then talk to each other. You listen and only help if they stop.',
          f'- **Score** each learner on the 3 rubric areas (1–3 each, 3–9 in total). Write the score at once, before the next pair.', ':::', '']
    L += ['### Speaking rubric (1–3 in each area)', '']
    L += rubric_table(C['rubric'], ['Area', '1', '2', '3']) + ['']
    L += [f'*{C["rubric_note"]}*', '']
    # listening script
    L += ['## Listening Script', '',
          f'### Listening script: `{E["audio"]}` (about {alen}{"" if real else ", estimated from the script; not recorded yet"}; play it two times)', '',
          f'Speakers: {", ".join(speakers(E))}, and a narrator.', '']
    L += [f'> **Narrator:** {E["intro"]}'] + [f'> **{l[0]}:** {l[1]}' for l in E['lines']] + [f'> **Narrator:** {E["end"]}', '']
    # answer key
    L += ['### Answer key', '', f'**A. Listening ({P["A"]} points: 1 point each)**', '']
    L += [f'- {i}. {key_text(it)}' for i, it in enumerate(E['listening'], 1)] + ['']
    L += [f'**B. Words ({P["B"]} points: 1 point each)**', '']
    L += [f'- {i}. {a}' for i, (s, a, les) in enumerate(W['items'], 1)]
    L += [f'- Not used: {", ".join(w for w in W["box"] if w not in [x[1] for x in W["items"]])}. Small spelling mistakes are OK if the word is clear.', '']
    L += [f'**C. Grammar ({P["C"]} points: 1 point each)**', '', 'Part 1:', '']
    L += [f'- {i}. {a}' for i, (s, ch, a, les) in enumerate(E['grammar'], 1)] + ['', 'Part 2 (1 point if the mistake is fixed and the learner adds no new mistake):', '']
    for i, f in enumerate(E['fix'], nG + 1):
        alt = f' Also correct: {" / ".join(f["also"])}' if f.get('also') else ''
        L.append(f'- {i}. {f["right"]} *(the mistake: "{f["mistake"]}")*{alt}')
    L += ['', f'**D. Reading ({P["D"]} points: 1 point each)**', '']
    L += [f'- {i}. {key_text(it)}' for i, it in enumerate(R['items'], 1)] + ['']
    L += [f'**E. Writing ({P["E"]} points)**: score with the writing rubric in the Scoring Guide. Model answers (what a {C["writing_top"]} answer can look like):', '']
    for k, (tt, pr, bl) in enumerate(E['writing']['tasks'], 1):
        L += [f'> **Task {k} ({tt}):** {E["writing"]["models"][k - 1]}', '']
    L += ['### Where the answers are in the audio', '', '| # | Answer | The learner hears | Lesson |', '|---|---|---|---|']
    L += [f'| {i} | {key_text(it)} | "{it["ev"]}" | {it["les"]} |' for i, it in enumerate(E['listening'], 1)] + ['']
    L += ['### Where the answers are in the reading', '', '| # | Answer | The text says |', '|---|---|---|']
    L += [f'| {i} | {key_text(it)} | "{it["ev"]}" |' for i, it in enumerate(R['items'], 1)] + ['']
    L += ['### Which lesson each item comes from', '',
          '| Part | Items and lessons |', '|---|---|',
          f'| A. Listening | {by_lesson((i, it["les"]) for i, it in enumerate(E["listening"], 1))} |',
          f'| B. Words | {by_lesson((i, x[2]) for i, x in enumerate(W["items"], 1))} |',
          f'| C. Grammar | {by_lesson([(i, x[3]) for i, x in enumerate(E["grammar"], 1)] + [(i, f["les"]) for i, f in enumerate(E["fix"], nG + 1)])} |',
          f'| D. Reading | {by_lesson((i, it["les"]) for i, it in enumerate(R["items"], 1))} |', '', '---', '']
    # scoring guide
    L += ['## Scoring Guide', '', '### Written test: score bands (proposed)', '',
          '| Written score | Band | What it means |', '|---|---|---|',
          f'| {meets}–{tot} | **Meets** | The learner can use most of the {"Lesson 1–7" if mid else "Level " + str(V)} language on their own. |',
          f'| {almost}–{meets - 1} | **Almost** | The learner understands a lot but still needs practice. Look at which part was low. |',
          f'| 0–{almost - 1} | **Not yet** | Talk with the learner. Plan extra practice{" before the final" if mid else ""}. |', '',
          f'*These bands are **proposed** (about 78% and 52%, the same as the Level 1 and Level 2 exams). The program confirms them after the first classes use the test.*', '',
          f'### Writing rubric (Part E, {P["E"]} points)', '']
    L += rubric_table(C['writing_rubric'], ['Area', '0', '1', '2']) + ['']
    L += [f'*{C["writing_note"]}*', '', '### Speaking (3–9, separate from the written score)', '',
          '- 7–9: strong for this level. 5–6: on track. 3–4: needs more speaking practice. *(Proposed.)*', '']
    if mid:
        L += ['### After the midterm', '', '- Give back the tests in the next class. Go over Part C together: learners correct their own mistakes.',
              '- For learners in the **Not yet** band, choose 2 lessons to review with them (the lesson numbers are in the table above).',
              f'- The final exam is in Week 15 and covers all 13 lessons, with more items from Lessons 8–13.', '']
    else:
        L += [f'### {C["gate_title"]}', ''] + [f'- {x}' for x in C['gate']] + ['', f'*{C["gate_note"]}*', '']
    L += ['## Teacher Notes', ''] + [f'- {x}' for x in E['notes'] + C['notes']] + ['', '---', '']
    # papers
    L += ['## Papers to Copy', '', '### Speaking Interview Card (Teacher)', '',
          f'**Part 1. Ask each learner 2 questions{" (the same questions as the first weeks, so you can hear the growth)" if not mid else ""}. Then ask one follow-up question.**', '']
    L += [f'{i}. {q}' for i, q in enumerate(E['speak1'], 1)] + ['', '**Follow-up questions:** Why? When was that? Who were you with? What happened next? How did you feel?', '',
          '**Part 2. Give the pair one Task Card.** Listen for:', '']
    L += [f'- **Card {LET[k].upper()} ({c[0]}):** {c[2]}' for k, c in enumerate(E['speak2'])] + ['', '---', '',
          '<!-- mode: student -->', '### Speaking Task Cards', '', '*Cut out the cards. Give one card to each pair.*', '']
    for k, c in enumerate(E['speak2']):
        L += [f':::box Card {LET[k].upper()}: {c[0]}'] + c[1] + [':::', '']
    L += ['---', '', '<!-- mode: teacher -->', '### Score Sheet', '', f'Class: ______________________   Teacher: ______________________   Date: __________', '',
          '| Name | A /' + str(P['A']) + ' | B /' + str(P['B']) + ' | C /' + str(P['C']) + ' | D /' + str(P['D']) + ' | E /' + str(P['E'])
          + f' | Written /{tot} | Comm. 1–3 | Gram. 1–3 | Pron. 1–3 | Speaking /9 |', '|' + '---|' * 11]
    L += ['| | | | | | | | | | | |'] * 12 + ['']
    if not mid: L += [f'*{C["sheet_note"]}*', '']
    L += ['---', '', '<!-- mode: student -->', f'### Can-Do Self-Check · {t}', '', NAME, '',
          'Read each sentence. Check one box.', '', '| I can… | Yes | A little | Not yet |', '|---|---|---|---|']
    L += [f'| I can {s}. *(Lesson{"s" if "–" in str(l) else ""} {l})* | ☐ | ☐ | ☐ |' for s, l in E['selfcheck']] + ['',
          'My goal for the next weeks: ______________________________________________', '', '---', '',
          '<!-- mode: teacher -->', f'### Answer Key (Teacher) · Level {V} · {t}', '']
    nr = max(len(E['listening']), len(W['items']), len(R['items']))
    L += ['| # | A. Listening | B. Words | D. Reading |', '|---|---|---|---|']
    for i in range(nr):
        a = key_text(E['listening'][i]) if i < len(E['listening']) else ''
        b = W['items'][i][1] if i < len(W['items']) else ''
        d = key_text(R['items'][i]) if i < len(R['items']) else ''
        L.append(f'| {i + 1} | {a} | {b} | {d} |')
    L += ['', '| # | C. Grammar | # | C. Grammar |', '|---|---|---|---|']
    allc = [g[2] for g in E['grammar']] + [f['right'] for f in E['fix']]
    half = (len(allc) + 1) // 2
    for i in range(half):
        r = f'| {i + 1} | {allc[i]} | '
        r += f'{i + 1 + half} | {allc[i + half]} |' if i + half < len(allc) else ' | |'
        L.append(r)
    L += ['', f'**E. Writing:** rubric, {P["E"]} points. **Total:** A {P["A"]} + B {P["B"]} + C {P["C"]} + D {P["D"]} + E {P["E"]} = **/{tot}**. Speaking: 3–9 (separate).', '',
          '---', '', '<!-- mode: guide -->', '## License and Credits', '', LIC, '',
          '*The listening scripts are original text written for this curriculum. When the recordings are made, they use the same tools as the '
          f'Level {V} lesson audio: Chatterbox (Resemble AI, MIT license) with synthetic Kokoro-82M reference voices (Apache 2.0), and every file '
          'carries the Perth watermark. The audio has no real person\'s voice.*', '']
    return '\n'.join(L)

# ---------- listening script + cast (lesson audio tool format) ----------
def write_script(E):
    ad = os.path.join(HERE, 'audio'); os.makedirs(os.path.join(ad, 'cast'), exist_ok=True)
    cast = dict(TITLE=E['audio_title'], VOICES=E['voices'], FEMALE=sorted(E['female']), NAMES=sorted(E['names']), SAME=E['same'],
                TTS={l[1]: l[2] for l in E['lines'] if len(l) > 2})
    json.dump(cast, open(os.path.join(ad, 'cast', f'cast_L{V}_{E["key"]}.json'), 'w'), indent=1, ensure_ascii=False)
    est = est_seconds(E)
    S = [f'# Level {V}, {E["key"]} exam (Week {E["week"]}) listening script (original text written for this curriculum; invented names). NOT RECORDED YET.',
         f'# GENERATED by ../make_exam_md.py from exam_data.py (+ cast/cast_L{V}_{E["key"]}.json). Edit exam_data.py, then re-run build_all.sh.',
         f'# Voices: clip names in {C["refs_md"]} (Kokoro-82M synthetic reference voices, cloned with Chatterbox). Estimated length: {est} s.',
         f'LESSON = {E["key"]!r}', f'TITLE = {E["audio_title"]!r}', f'VOICES = {E["voices"]!r}', 'FEMALE = {' + ', '.join(repr(x) for x in sorted(E["female"])) + '}',
         'NAMES = {' + ', '.join(repr(x) for x in sorted(E["names"])) + '}', f'SAME = {E["same"]!r}',
         f'SETTINGS = {dict(C["settings"], LENGTH_S=C["length_s"])!r}', f'INTRO = {E["intro"]!r}', 'LINES = [']
    for l in E['lines']: S.append(f' {tuple(l)!r},')
    S += [']', f'END = {E["end"]!r}', '']
    open(os.path.join(ad, f'script_L{V}_{E["key"]}.py'), 'w').write('\n'.join(S))
    return est

if __name__ == '__main__':
    for E in D.EXAMS:
        est = write_script(E)
        open(os.path.join(OUT, f'Level{V}_{E["key"]}_Student_Test.md'), 'w').write(student(E))
        open(os.path.join(OUT, f'Level{V}_{E["key"]}_Exam_Teacher_Packet.md'), 'w').write(packet(E))
        print(f'L{V} {E["key"]}: total {total(E)}, listening estimate {est} s ({mmss(est)}), {sum(words_in(l[1]) for l in E["lines"])} words in {len(E["lines"])} lines')
