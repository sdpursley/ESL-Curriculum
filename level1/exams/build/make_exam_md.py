"""Write the Level 1 exam sources (.md) from exam_data.py and the listening scripts in audio/.
Usage: python3 make_exam_md.py [OUT_DIR]   (default: the exams folder)"""
import os, sys, importlib.util, json
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import exam_data as D
OUT = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(HERE, '..'))
ML = 'My language: ______________________________________________'
NAME = 'Name: ______________________________     Date: ________________'
LIC = ('*© 2026 the authors. CC BY-NC-SA 4.0. Provided as-is, without warranty. Pictures: Twemoji by Twitter, Inc. and others, '
       'CC BY 4.0 (changed), and original drawings; see images/CREDITS.md. Names and numbers are invented.*')

def script(E):
    p = os.path.join(HERE, 'audio', E['script'])
    spec = importlib.util.spec_from_file_location('S', p); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S); return S

def audio_len(E):
    p = os.path.join(OUT, 'audio', E['audio'].replace('_listening.mp3', '_check_results.json'))
    if os.path.exists(p):
        d = json.load(open(p))['duration_s']; return f"{int(d//60)}:{int(round(d % 60)):02d}"
    return '1:15'

def instr(en, sp):
    return [f'### {en}', '', f'*Español: {sp}*', '', ML, '']

def write_n(E):
    return [i for i, it in enumerate(E['listening'], 1) if it[1] == 'write'][0]

def opt_cell(o):
    if isinstance(o, tuple) and len(o) == 2 and o[1].startswith('L1_EX_'):
        return f'![{o[0]} w=1.0](images/{o[1]}.png)<br>{o[0]}'
    if isinstance(o, tuple): return '<br>'.join(f'^^{x}' for x in o)
    return f'^^{o}'

def listening_table(E):
    rows = ['| | | | |', '|---|---|---|---|']
    for i, (stem, kind, opts, ans, les, ev) in enumerate(E['listening'], 1):
        st = f'**{i}.** {stem}'
        if kind == 'write':
            rows.append(f'| {st}<br>Write the number. | ^^{opts[0]} ______ | | |')
        elif kind == 'yesno':
            rows.append(f'| {st} | {opt_cell(opts[0])} | ^^{opts[1]} | ^^{opts[2]} |')
        else:
            rows.append(f'| {st} | ' + ' | '.join(opt_cell(o) for o in opts) + ' |')
    return rows

def words_table(E):
    rows = ['| | | |', '|---|---|---|']; cells = []
    for i, (pic, ch, ans, les) in enumerate(E['words'], 1):
        cells.append(f'![picture {i} w=1.15](images/{pic}.png)<br>**{i}.**<br>' + '<br>'.join(f'^^{c}' for c in ch))
    for k in range(0, len(cells), 3): rows.append('| ' + ' | '.join(cells[k:k+3]) + ' |')
    return rows

def grammar_lines(E):
    out = []
    for i, (sent, ch, ans, les) in enumerate(E['grammar'], 1):
        out += [f'{i}. {sent}        ( **{ch[0]}**   /   **{ch[1]}** )', '']
    return out

def form_lines(E):
    F = E['form']; L = ['| |', '|---|', f'| ![practice card w={F.get("card_w", 4.3)}](images/{F["card"]}.png) |', '']
    L += [f'| {F["title"]} | (write) |', '|---|---|']
    for lab, val in F['fields']: L.append(f'| **{lab}** | <br> |')
    if 'days' in F:
        L.append('| **Days you can work** (check ✓) | ' + '   '.join(f'☐ {d}' for d in F['days']) + ' |')
        L.append('| **Skills** (check ✓) | ' + '   '.join(f'☐ {s}' for s in F['skills']) + ' |')
    return L + ['']

def total(E):
    return len(E['listening']) + len(E['words']) + len(E['grammar']) + 6

def student(E):
    t = E['title']; n = write_n(E)
    L = ['<!-- mode: student -->', f'## {t} · Listening', '', NAME, '']
    L += instr(f'A. Listen. Circle the answer. For number {n}, write the number.', D.SP['listen'].format(n=n))
    L += [f'*{E["scene"]}*', ''] + listening_table(E) + ['']
    L += instr('B. Look at the picture. Circle the word.', D.SP['words']) + words_table(E) + ['', '<!-- pagebreak -->', '']
    L += instr('C. Circle the correct word.', D.SP['grammar']) + grammar_lines(E) + ['<!-- pagebreak -->', '',
          f'## {t} · Form', '']
    if E['key'] == 'Midterm':
        L += instr('D. Look at the practice ID card. Write the information on the form.', D.SP['form_mt'])
    else:
        L += instr('D. Look at the practice card. Write the information on the job application. Check ✓ the days and the skills.', D.SP['form_fn'])
    L += form_lines(E)
    L += [f'**Score:** A ____ /{len(E["listening"])}   B ____ /{len(E["words"])}   C ____ /{len(E["grammar"])}   D ____ /6   **Total ____ /{total(E)}**', '']
    return '\n'.join(L)

# ---------------- teacher packet
def key_text(E):
    L = []
    def letters(it):
        stem, kind, opts, ans, les, ev = it
        if kind == 'write': return f'**{ans}**'
        if kind == 'yesno': return f'**{ans}**'
        if kind == 'text2':
            for k, o in enumerate(opts):
                if ' + '.join(o) == ans: return f'**{" and ".join(o)}** (choice {k+1} of 3)'
        names = [o[0] if isinstance(o, tuple) else o for o in opts]
        return f'**{ans}** (choice {names.index(ans)+1} of 3)'
    return letters

def packet(E):
    S = script(E); t = E['title']; lk = key_text(E); tot = total(E); nL = len(E['listening']); nG = len(E['grammar']); nW = len(E['words'])
    mid = E['key'] == 'Midterm'
    meets = round(tot*0.78); almost = round(tot*0.52)
    L = ['<!-- mode: guide -->', f'# Level 1 · {t}: Teacher Packet', '',
         f'**{"Midterm" if mid else "Final"} Exam · {E["lessons"]}** · Level 1 Adult ESL', '',
         '**Contents**', '',
         '- Step-by-step directions (for any teacher or volunteer)', '- Clock-time plan', '- Speaking interview and rubric',
         '- Listening script', '- Answer key and scoring guide', '- Teacher notes',
         '- Papers to copy: Speaking Interview Card (teacher), Speaking Task Cards, Speaking Score Sheet (teacher), Can-Do Self-Check, one-page Answer Key (teacher)', '',
         '<!-- mode: teacher -->', '## How to Use This Packet', '',
         f'- **The test for learners is a separate file:** `Level1_{E["key"]}_Student_Test.pdf` (no answers). Print 1 per learner + 3 extra.',
         f'- **This packet** is for you: directions, the listening script, the answer key, and the speaking papers.',
         f'- **Audio:** `audio/{E["audio"]}` (about {audio_len(E)}). The conversation is in the file **once**. Press play again for the next listen.',
         '- **No Spanish needed.** The Spanish lines on the test are for learners.', '',
         f'## {t}: Step by Step', '', '### What the test has', '',
         '| Part | What learners do | Points | Time |', '|---|---|---|---|',
         f'| A. Listening | Listen to a short conversation. Circle a picture or a word ({nL - 1} items). Write one number (1 item). | {nL} | 15 min (6:10–6:25) |',
         f'| B. Words | Look at a picture. Circle the word. | {nW} | 20 min for B + C (6:25–6:45) |',
         f'| C. Grammar | Circle the correct word (2 choices). | {nG} | (with B) |',
         f'| D. Form | Copy the information from a practice card onto a {"form" if mid else "job application"}. | 6 | 10 min (7:00–7:10) |',
         f'| **Written total** | | **{tot}** | **45 min** |',
         '| Speaking interview | Pairs (or one-on-one) with the teacher. Scored with the rubric, not added to the written total. | 3–9 | 3 min per pair |', '',
         f'*Covers {E["lessons"]}. Every item uses only words and grammar from these lessons, and the same task types as the lessons (circle, check, write one number, copy onto a form, pair questions).*', '',
         '### Before class (20 minutes)', '',
         f'1. Print the student test (1 per learner + 3). Print this packet\'s Speaking Task Cards (1 per pair), the Score Sheet, and the Self-Check (1 per learner).',
         f'2. Put `{E["audio"]}` on a phone. Connect a small speaker. Play the first seconds to check the volume.',
         '3. Set 2 chairs and 1 chair for you in a quiet corner (for the speaking interviews).',
         '4. Have pencils and a clock or timer.', '',
         ':::step Step 1 · 6:00–6:10 · Warm-up + first interviews · 10 min',
         '- **Say:** "Tonight is the test. Listening, then words and grammar, then a break, then a form. Don\'t worry. I read everything with you."',
         f'- **Pairs** ask and answer the questions on the Speaking Interview Card (write 4 of them on the board).',
         '- **You:** call 2–3 pairs to the quiet corner for their speaking interview (3 minutes per pair).',
         ':::', '',
         ':::step Step 2 · 6:10–6:25 · Listening test (Part A) · 15 min · NEVER SKIP',
         '- Hand out the test. Learners write their name.',
         f'- **Read every item aloud** and point to the pictures: "Number 1. {E["listening"][0][0]}…" Learners only look; they don\'t write yet.',
         f'- **Say:** "Circle **one** answer. Number {write_n(E)}: write the number."',
         '- **Play 1:** learners listen only. **Play 2:** learners circle and write. **Play 3:** learners check. Wait 30 seconds between plays.',
         '- Learners who can\'t read yet: read the choices aloud and let them point; you circle for them.',
         ':::', '',
         ':::step Step 3 · 6:25–6:45 · Words and Grammar (Parts B and C) · 20 min · NEVER SKIP',
         '- **Part B:** say "Look at the picture. Circle the word." Read both words for each picture aloud.',
         f'- **Part C:** read each sentence aloud with "blank" for the missing word, then read the two words: "Number 1. *Blank* you from Mexico? **Are? Is?**" Learners circle. About 1 minute per item.',
         '- Do the first item of each part together on the board as an example (a different sentence, not a test item).',
         ':::', '',
         ':::step Break · 6:45–7:00 · 15 min',
         '- Collect nothing. Learners keep their test face down.',
         ':::', '',
         ':::step Step 4 · 7:00–7:10 · Form (Part D) + interviews · 10 min · NEVER SKIP',
         f'- **Say:** "Look at the card. Write the information on the {"form" if mid else "job application"}." Point to the first line on the card and on the form.',
         '- Learners work alone. They may copy letters one by one; that is OK.',
         '- **You:** start the remaining speaking interviews in the quiet corner.',
         ':::', '',
         ':::step If time · 7:10–7:30 · Interviews, then the Self-Check',
         '- **① Finish all interviews.** Learners who are waiting do the Can-Do Self-Check, then practice the Task Cards with a partner.',
         '- **② Collect** the tests and the self-checks. Say "Thank you! Great work!"',
         '- **③ Go over the listening (5 min, optional):** play the audio once more and say the answers.',
         ':::', '',
         '### Clock-time plan', '',
         '| Time | Step | Min | Grouping | If running behind |', '|---|---|---|---|---|',
         '| 6:00–6:10 | Warm-up (pair questions) + first speaking interviews | 10 | Pairs | Shorten the warm-up |',
         '| 6:10–6:25 | **Part A: Listening** (play 2–3 times) | 15 | Individuals | **Never skip**; 2 plays are OK |',
         '| 6:25–6:45 | **Parts B + C: Words and Grammar** | 20 | Individuals | **Never skip**; slow readers finish Part C after the break |',
         '| 6:45–7:00 | BREAK | 15 | | |',
         '| 7:00–7:10 | **Part D: Form** + speaking interviews | 10 | Individuals | **Never skip** |',
         '| 7:10–7:30 | Finish interviews; Can-Do Self-Check; go over the listening | 20 | | The self-check can go home |', '',
         '> **Written test time:** 15 + 20 + 10 = **45 minutes**. Interviews happen during the warm-up and after the break, while learners work alone.', '',
         '### Speaking interview (3 minutes per pair)', '',
         ':::box How to do it',
         '- **Pairs** come to the quiet corner (or one learner, if there is an odd number; you are the partner).',
         '- **How many:** 15 learners ≈ 8 pairs ≈ 24 minutes: about 3 pairs at 6:00–6:10 and 5 pairs at 7:00–7:30. 7–8 learners ≈ 4 pairs ≈ 12 minutes.',
         f'- **Part 1 (1 minute):** ask each learner **2 questions** from the Speaking Interview Card. Use different questions for each partner.',
         f'- **Part 2 (2 minutes):** give the pair a Task Card: **{E["speaking2"]["name"]}** Learner A asks; Learner B answers. Then switch.',
         '- **Score right away** on the Score Sheet: 3 areas, 1–3 points each (total 3–9). Write one thing the learner did well.',
         '- **Be kind:** smile, repeat a question once, point to the picture. Don\'t correct during the interview.',
         f'- **Target grammar for this interview:** be questions and short answers; {E["speaking2"]["grammar"]}.',
         ':::', '',
         '**Speaking rubric (same 1–3 scale as Level 2, in beginner words):**', '',
         '| Score | Communication | Target grammar | Pronunciation and fluency |', '|---|---|---|---|',
         '| 3 | Answers every question; asks the partner questions | Uses the lesson phrases correctly most of the time | Easy to understand; few long stops |',
         '| 2 | Answers most questions; needs a little help (a repeat, a gesture) | Uses the phrases with mistakes, but the meaning is clear | Mostly easy to understand; some stops |',
         '| 1 | One-word answers or no answer, even with help | Few correct phrases, or mistakes hide the meaning | Hard to understand |', '',
         '*A one-word answer that is correct (for example, "Guatemala.") is fine for Communication 2. Short answers like "Yes, I do." count as correct target grammar.*', '',
         '---', f'### Listening script: `{E["audio"]}` (about {audio_len(E)}; the conversation is in the file once, so press play again for each listen)', '',
         '> **Audio:** play from a phone + small speaker. No speaker? Read the script slowly with a second adult (not a learner). Say numbers as words: '
         + ('*five-five-five, oh-one-eight-six; six thirty; twelve dollars.*' if mid else '*May twelfth; nine thirty.*'), '']
    L.append(f'> **Narrator:** {S.INTRO}')
    for ln in S.LINES: L.append(f'> **{ln[0]}:** {ln[1]}')
    L += [f'> **Narrator:** {S.END}', '']
    # answer key
    L += ['### Answer key', '']
    L.append('- *Part A, Listening:* ' + '; '.join(f'{i} {lk(it)}' for i, it in enumerate(E['listening'], 1)) + '.')
    L.append('- *Part B, Words:* ' + '; '.join(f'{i} **{w[2]}**' for i, w in enumerate(E['words'], 1)) + '.')
    L.append('- *Part C, Grammar:* ' + '; '.join(f'{i} **{g[2]}**' for i, g in enumerate(E['grammar'], 1)) + '.')
    F = E['form']
    fk = '; '.join(f'{lab} **{val}**' for lab, val in F['fields'])
    if 'days' in F: fk += f'; Days ✓ **{", ".join(F["days_key"])}** (no other days); Skills ✓ **{" and ".join(F["skills_key"])}** (no other skills)'
    L.append(f'- *Part D, Form:* {fk}.')
    L += ['', '### Where the answers are in the audio', '', '| # | Answer | The learner hears | Lesson |', '|---|---|---|---|']
    for i, it in enumerate(E['listening'], 1): L.append(f'| {i} | {it[3]} | "{it[5]}" | {it[4]} |')
    L += ['', '### Scoring guide', '',
          f'- **1 point per item.** Part A /{nL} + Part B /{nW} + Part C /{nG} + Part D /6 = **/{tot}**.',
          f'- **Listening item {write_n(E)}** (write): the number alone is enough' + (' (*12* or *$12*).' if mid else ' (*12*, *12th*, or *May 12*).'),
          '- **Circle items:** one clear circle (or a check, a line, or pointing that you saw) = 1 point. Two answers circled = 0.',
          '- **Part D:** 1 point per line. Copying mistakes of one letter or one number are OK if the word is clear (*Rivrside* = 1 point). Capital or small letters both OK. '
          + ('' if mid else 'Days = 1 point only if Mon, Wed, Fri are checked and no other day; Skills = 1 point only if cook and drive are checked and nothing else.'),
          f'- **Suggested levels (written test):** **Meets** {meets}–{tot} · **Almost** {almost}–{meets-1} · **Not yet** 0–{almost-1}. (Same percentages as the Level 2 exams.)',
          '- **Speaking:** **Meets** = 2 or more in all three rubric areas.']
    if not mid:
        L.append('- **Ready for Level 2 (proposed in the Level 1 scope and sequence; the program confirms it):** attended at least 9 of the 13 lessons, took the final, scored 2 or more in all three speaking areas, and got at least 4 of 6 on Part D (no more than 1–2 errors). Learners who are not ready still graduate in Week 16 and are invited to repeat Level 1 or join Level 2 with a study buddy.')
    L += ['', '### Teacher notes', '',
          '- **Read everything aloud.** This is a test of English listening and words, not of reading speed. Reading items aloud is part of the test, not extra help.',
          '- **Learners who can\'t read or write yet:** they point; you circle for them and write "oral" at the top. For Part D, they copy as much as they can; give 1 point for each line with the right first letters or numbers.',
          '- **Extra time is fine.** Slow readers can finish Part C after the break.',
          '- **Absent learners:** give the test next week at 7:10 (play the audio for them with earbuds, 2–3 times). The interview needs a teacher.',
          '- **Privacy:** the form uses an invented practice card. Never ask for a learner\'s real address, phone number, or immigration information.',
          f'- **Return the papers next week** with one strength and one goal for each learner.' + ('' if mid else ' Week 16 is graduation: each learner gives a 30–60 second "All About Me" talk.'), '']
    # papers
    L += ['---', '<!-- mode: teacher -->', f'## {t} · Speaking Interview Card (Teacher)', '', '### Part 1 · Each learner (1 minute)', '',
          '*Ask each learner 2 questions. Use different questions for each partner.*' + ('' if mid else ' These are the same 6 baseline questions as Weeks 1–3, so you can see how much each learner has grown.'), '']
    for i, q in enumerate(E['speaking1'], 1): L.append(f'{i}. {q}')
    L += ['', f'### Part 2 · Pair task (2 minutes): {E["speaking2"]["name"]}', '',
          f'- Learner A: {E["speaking2"]["a"]}', f'- Learner B: {E["speaking2"]["b"]}', f'- {E["speaking2"]["then"]}', '',
          '### Rubric', '', '| Score | Communication | Target grammar | Pronunciation and fluency |', '|---|---|---|---|',
          '| 3 | Answers every question; asks the partner questions | Uses the lesson phrases correctly most of the time | Easy to understand; few long stops |',
          '| 2 | Answers most questions; needs a little help | Mistakes, but the meaning is clear | Mostly easy to understand; some stops |',
          '| 1 | One-word answers or no answer, even with help | Few correct phrases, or mistakes hide the meaning | Hard to understand |', '',
          '---', '<!-- mode: student -->', f'## {t} · Speaking Task Card (cut apart: 1 per pair)', '']
    sp2 = E['speaking2']
    L += instr(f'Learner A: {sp2["a"]}', sp2['a_sp']) + instr(f'Learner B: {sp2["b"]}', sp2['b_sp']) + instr(sp2['then'], sp2['then_sp'])
    L += ['| | | | |', '|---|---|---|---|', '| ' + ' | '.join(f'![{w}](images/{p}.png)<br>{w}' for w, p in sp2['pics']) + ' |', '']
    L += ['---', '<!-- mode: teacher -->', f'## {t} · Speaking Score Sheet (Teacher)', '', 'Teacher: ______________________   Date: ______________', '',
          '| Learner | Comm. (1–3) | Grammar (1–3) | Pron. (1–3) | Total (/9) | One thing done well |', '|---|---|---|---|---|---|']
    L += ['| <br> | | | | | |'] * 10
    L += ['', '*Comm. = Communication · Grammar = Target grammar · Pron. = Pronunciation and fluency. Meets = 2 or more in all three areas. Use a second sheet for more learners.*', '',
          '---', '<!-- mode: student -->', f'## {t} · Can-Do Self-Check', '', NAME, '']
    L += instr('Listen to the teacher. Check ✓ one box for each line.', 'Escucha al profesor. Marca ✓ una casilla en cada línea.')
    L += ['| I can… | Yes | A little | Not yet |', '|---|---|---|---|']
    for s, les in E['selfcheck']: L.append(f'| {s} *(Lesson {les})* | ☐ | ☐ | ☐ |')
    L += ['']
    if mid: L += instr('My goal for the next 7 weeks: write or draw one thing.', 'Mi meta para las próximas 7 semanas: escribe o dibuja una cosa.')
    else: L += instr('My goal for Level 2 (or for next time): write or draw one thing.', 'Mi meta para el Nivel 2 (o para la próxima vez): escribe o dibuja una cosa.')
    L += ['______________________________________________________________', '', '______________________________________________________________', '']
    # one-page key
    L += ['---', '<!-- mode: teacher -->', f'## {t} · Answer Key (Teacher)', '', '### Part A · Listening', '', '| # | Answer | # | Answer |', '|---|---|---|---|']
    A = [(i, it[3]) for i, it in enumerate(E['listening'], 1)]; h = (len(A)+1)//2
    for k in range(h):
        r = A[k]; s2 = A[k+h] if k+h < len(A) else ('', '')
        L.append(f'| {r[0]} | {r[1]} | {s2[0]} | {s2[1]} |')
    L += ['', '### Part B · Words', '', '| # | Answer | # | Answer | # | Answer |', '|---|---|---|---|---|---|']
    Wd = [(i, w[2]) for i, w in enumerate(E['words'], 1)]
    for k in range(2): L.append('| ' + ' | '.join(f'{Wd[k*3+j][0]} | {Wd[k*3+j][1]}' for j in range(3)) + ' |')
    L += ['', '### Part C · Grammar', '', '| # | Answer | # | Answer | # | Answer |', '|---|---|---|---|---|---|']
    G = [(i, g[2]) for i, g in enumerate(E['grammar'], 1)]; rows = (len(G)+2)//3
    for k in range(rows):
        cells = []
        for j in range(3):
            idx = k + j*rows
            cells.append(f'{G[idx][0]} | {G[idx][1]}' if idx < len(G) else ' | ')
        L.append('| ' + ' | '.join(cells) + ' |')
    L += ['', '### Part D · Form', '', ' · '.join(f'{lab}: **{val}**' for lab, val in F['fields'])
          + (f' · Days: **✓ {", ".join(F["days_key"])}** (only these) · Skills: **✓ {", ".join(F["skills_key"])}** (only these)' if 'days' in F else '')]
    L += ['', f'*Total: A /{nL} + B /{nW} + C /{nG} + D /6 = /{tot}. Meets {meets}–{tot} · Almost {almost}–{meets-1} · Not yet 0–{almost-1}. The listening script is in this packet ("Listening script").*', '',
          '<!-- mode: guide -->', '### License and Credits', '',
          '© 2026 the authors. The authors license these materials under CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/). Program names and logos are not covered by this license.', '',
          'Pictures: Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The graphics were resized and combined; the clock faces, price tags, and practice cards are original drawings made in code. The file-by-file list is in `images/CREDITS.md`. All names, phone numbers, addresses, and prices are invented.', '',
          'Listening audio: synthetic voices made with Chatterbox TTS (Resemble AI, MIT License), copied from short reference clips made with Kokoro-82M (Apache 2.0). No recordings of real people were used. Each file carries an inaudible Perth watermark that marks it as AI-generated.', '',
          'These materials are provided as-is for educational use, without warranty of any kind.', '']
    return '\n'.join(L)

if __name__ == '__main__':
    for E in D.EXAMS:
        k = E['key']
        open(os.path.join(OUT, f'Level1_{k}_Student_Test.md'), 'w').write(student(E))
        open(os.path.join(OUT, f'Level1_{k}_Exam_Teacher_Packet.md'), 'w').write(packet(E))
        print('wrote', k, 'total', total(E))
