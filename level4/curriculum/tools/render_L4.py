"""Level 4 lesson builder: lessonN/spec_L4_LN.py (one dict L) -> Level4_LessonN.md, plus the listening cast JSON.
Page layout and Markdown conventions are the Level 3 lesson books' (md2docx_L4.py = Level 3 md2docx_L3.py).
Answer keys are generated from the same items the student pages show, so pages and keys always agree:
  [answer]          a write-in blank on the page; the key shows the answer
  {{a|*b|c}}        a circle choice on the page, (**a** / **b** / **c**); the starred option is the key
Every Listening Task B/C item and every Read & Write question carries evidence that must appear in the script / text."""
import re, sys, json, os, importlib.util
BL = '____________'
LONG = '______________________________________________'
def blanks(s):            # page text
    s = re.sub(r'\[([^\]]+)\]', lambda m: BL, s)
    return re.sub(r'\{\{(.+?)\}\}', lambda m: '(' + ' / '.join(f'**{o.lstrip("*")}**' for o in m.group(1).split('|')) + ')', s)
def answers(s):          # key list for one item
    out = re.findall(r'\[([^\]]+)\]', s)
    for m in re.findall(r'\{\{(.+?)\}\}', s):
        st = [o[1:] for o in m.split('|') if o.startswith('*')]; assert len(st) == 1, ('need one *answer', s); out.append(st[0])
    assert out, ('no answer in item', s); return out
def filled(s):
    s = re.sub(r'\[([^\]]+)\]', lambda m: m.group(1), s)
    return re.sub(r'\{\{(.+?)\}\}', lambda m: [o[1:] for o in m.group(1).split('|') if o.startswith('*')][0], s)
def norm(s): return re.sub(r'[^a-z0-9\' ]', '', re.sub(r'\s+', ' ', s.replace('’', "'").replace('*', '').lower())).strip()
def numbered(items): return '\n'.join(f'{i}. {blanks(t)}' for i, t in enumerate(items, 1))
def keylist(items): return ', '.join(f'{i} ' + ' / '.join(answers(t)) for i, t in enumerate(items, 1))
def bullets(xs): return '\n'.join('- ' + x for x in xs)
NUM = 'zero one two three four five six seven eight nine ten eleven twelve thirteen'.split()

def load(path):
    sp = importlib.util.spec_from_file_location('spec', path); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m.L

def render(L):
    N, Wk, T = L['N'], L['week'], L['title']; H = f'Lesson {N} (Week {Wk})'; o = []; a = o.append
    S = L['listen']; script_text = ' '.join(t for _, t in S['lines'])
    chars = [s for s in dict.fromkeys(s for s, _ in S['lines'])]
    # ---------- evidence checks ----------
    for it in S['B']['items']:
        assert norm(it['ev']) in norm(script_text), ('Task B evidence not in script', it['ev'])
    for it in S['C']['items']:
        assert norm(filled(it)) in norm(script_text), ('Task C line not in script', filled(it))
    rw = L['rw']; rtext = re.sub(r'\*\*', '', rw['text'])
    for q in rw['qs']: assert norm(q[2]) in norm(rtext), ('R&W evidence not in text', q[2])
    words = L['words']; assert len(words) == 12
    stars = ' • '.join(('★ ' if st else '') + w for w, _, st in words)
    # ---------- guide header ----------
    a('<!-- mode: guide -->')
    a(f'# Level 4 Adult ESL Curriculum · {H}: {T}\n')
    a('**Status:** Complete lesson (all 13 Level 4 lessons are published).\n')
    a('**Date:** October 2026\n')
    a('**Audience:** Program coordinators and volunteer teachers\n')
    a(f'**Companion files:** `audio/L4_L{N}_listening.mp3`, `images/` (12 vocabulary pictures{L.get("act_pics_note","")} + `images/CREDITS.md`).\n')
    a(f'> **Topic:** {L["topic"]}\n')
    a('### How this lesson is organized\n')
    a('| Part | What\'s inside | Who uses it |\n|---|---|---|')
    a('| **Teacher Plan** | At a glance, clock-time plan, step-by-step boxes, listening script, answer key, teacher notes | Volunteer teachers |')
    a(f'| **Student Pages** | Opening Talk, New Words, My Words, Listening, Grammar, Talk Time, Homework, Read & Write, Exit Ticket{", Can-Do Self-Check" if L.get("cando") else ""}, Task Words (optional). **Print this part for learners** | Learners |')
    a('| **Picture Credits** | Picture, audio, and license credits | Coordinators |\n')
    a(f'### What Lesson {N} builds on and what it adds\n')
    a(f'| Before (review only) | Where | New in Level 4 Lesson {N} |\n|---|---|---|')
    for b in L['builds']: a('| ' + ' | '.join(b) + ' |')
    a('')
    # ---------- teacher ----------
    a(f'<!-- part: Teacher Plan | {H} | {T} ;; At a glance · Clock-time plan · Step by step · Script and answer key | Level 4 ESL · Lesson {N} · TEACHER PLAN -->')
    a('<!-- mode: teacher -->\n## How to Use This Plan\n')
    a('> **You don\'t need to speak Spanish or any other language.** Teach in English. Show, point, and gesture. Some Grammar pages have one short **contrast tip**, only where a common mix-up exists. Learners read it on their own. You never need to read, translate, or explain it.\n')
    a('> **Instructions:** use the same short task words every week: *Listen. Circle. Check. Write. Work with a partner. Work in a group. Ask a follow-up question. Give a reason.* An optional Task Words page is at the back of the workbook for learners who want it.\n')
    a(f'> **Instruction rule:** **Model it** (do it with one learner while everyone watches), **check it** (ask: "{L.get("cq","Do you write or speak? How many sentences?")}"), **then go**. Say less, show more.\n')
    a('> **Grouping toolkit:** *Pairs:* turn to a neighbor; with an odd number, make one group of 3. *Groups:* 3–4 learners. *Inside–outside circles:* the inner circle faces out, the outer circle faces in; the outer circle moves one person to the right each round. *Mingle:* everyone stands and talks to many classmates. The teacher joins a pair only if one learner is left over.\n')
    a('> **When a learner is stuck or speaks another language to you:** (1) show it: the picture, a gesture, or the board; (2) give one more short English example; (3) point to the grammar box on their page; (4) a classmate can help for a few seconds, then back to English. You don\'t need to understand what classmates say to each other.\n')
    a('> **Three sentences, not one:** in Level 4, every Talk Time answer and every exit ticket has about three connected sentences: the answer, a reason, and a detail or example.\n')
    a(f'---\n## {H}: {T}\n\n### At a glance\n')
    a(':::box Objectives: learners can…\n' + bullets(L['objectives']) + '\n:::\n')
    a(':::box Materials\n' + bullets([f'Student Pages for Lesson {N} (print for the number expected + 3 spares)'] + L['materials'] +
       [f'Listening: phone + small speaker, `L4_L{N}_listening.mp3` (about {{EST}}). No speaker? Read the script aloud with a volunteer.',
        f'**Prep time:** {L["prep"]}.']) + '\n:::\n')
    a(':::box Key vocabulary (with pictures on the New Words page)\n' + stars + ('\n\n' + L['more_vocab'] if L.get('more_vocab') else '') + '\n:::\n')
    # clock plan
    C = L['clock']
    a('---\n### Clock-time plan\n\n*Times are loose. If the listening or Talk Time runs long, take the time from Read & Write.*\n')
    a('| Time | Step | Min | Grouping (15 / 7–8) | If running behind |\n|---|---|---|---|---|')
    for r in C: a('| ' + ' | '.join(r) + ' |')
    a('\n> **Skip order if you\'re running behind:** (1) the Read & Write writing task (it becomes homework); (2) the pair check at the end of Grammar; (3) the second round of Talk Time. **Never skip:** the listening tasks, the grammar boxes and the mistakes table, and the exit ticket.\n')
    a(f'> **Attendance (15 → 7–8 → 5 or fewer):** every step lists the sizes. {L.get("attend","With 5 or fewer, sit at one table: pair work stays in pairs, and the teacher joins one pair if needed. Late arrivals join any pair or group right away.")}\n')
    a('---\n### Step by step\n')
    for st in L['steps']:
        a(f':::step {st[0]}\n' + bullets(st[1]) + '\n:::\n')
    # script
    est = L['_est']
    a(f'---\n### Listening script: `L4_L{N}_listening.mp3` (about {{EST}}; the conversation plays once, so press play again for the second listen)\n')
    a(f'> **Audio:** play `L4_L{N}_listening.mp3` from a phone + small speaker. No speaker? Read the script with a volunteer, at a natural, friendly speed. The script says *going to* and *want to*. People often say *gonna* and *wanna*; learners only need to recognize those words.\n')
    a(f'> **Narrator:** {S["intro"]}')
    for s, t in S['lines']: a(f'> **{s}:** {t}')
    a("> **Narrator:** That's the end of the listening.\n")
    # key
    a('### Answer key\n')
    A_ = S['A']; letters = 'abcd'
    a(f'- *Listening Task A:* **{letters[A_["ans"]]}** ({A_["opts"][A_["ans"]]}).')
    a('- *Listening Task B:* ' + taskB_key(S['B']) + '.')
    a('- *Listening Task C:* ' + keylist(S['C']['items']) + '.')
    G = L['grammar']
    a('- *Grammar Practice A:* ' + keylist(G['A']['items']) + '.')
    a('- *Grammar Practice B:* ' + keylist(G['B']['items']) + '.')
    a('- *Talk Time:* answers will vary.')
    hw = L['hw']
    a('- *Homework 1:* ' + ' '.join(f'{i} {x[1]}' for i, x in enumerate(hw['one']['items'], 1)) + ' *Homework 2 and 3:* answers will vary. *Homework 4:* ' + keylist(hw['four']['items']) + '.')
    a('- *Read & Write B:* ' + ' • '.join(f'{i} {q[1]}' for i, q in enumerate(rw['qs'], 1)) + ' • *Writing (C):* answers will vary.')
    a('- *Exit ticket:* answers will vary. ' + L['exit']['key'])
    for k in L.get('extra_key', []): a('- ' + k)
    a('\n### Teacher notes\n'); a(bullets(L['notes']))
    if L.get('board'): a('\n' + L['board'])
    a('')
    # ---------- student ----------
    contents = 'Opening Talk · New Words · Listening · Grammar · Talk Time · Homework · Read & Write · Exit Ticket'
    a(f'<!-- part: Student Workbook | {H} | {T} ;; {contents} | Level 4 ESL · Lesson {N} · STUDENT WORKBOOK -->\n<!-- mode: student -->')
    O = L['opening']
    a(f'## {H} · Opening Talk\n\nName: ______________________________     Date: ________________\n')
    a('### Work with a partner. A asks a question. B answers in 3 sentences: the answer, a reason, and a detail. A asks one follow-up question. Then switch.\n')
    c = O['cards']; a('| | |\n|---|---|\n' + f'| {c[0]} | {c[1]} |\n| {c[2]} | {c[3]} |\n')
    a(f'*Follow-ups:* **{O["follow"]}**\n')
    a(f'### {O["hw_head"]}\n')
    a(f'| {O["hw_cols"][0]} | {O["hw_cols"][1]} |\n|---|---|\n| <br> | |\n')
    # new words
    a(f'---\n## {H}: {T}\n\n*Student Page 1 · Week {Wk}*\n\nName: ______________________________     Date: ________________\n')
    a('### New Words\n\n**Look. Listen. Repeat.** ★ = most important words.\n\n| | | | |\n|---|---|---|---|')
    for r in range(3):
        a('| ' + ' | '.join(f'![{w}](images/L4_L{N}_{sl}.png)<br>' + ('★ ' if st else '') + f'**{w}**' for w, sl, st in words[r*4:r*4+4]) + ' |')
    a(f'\n### Partner game: {L["game"][0]}\n\n*Example:* {L["game"][1]}\n')
    a(f'---\n## {H} · My Words\n\n**My personal word list.** Write each word in your language, if you want. Then write your own example.\n')
    a('| Word | My language | My example |\n|---|---|---|')
    for w, _, _ in words: a(f'| {w} | <br> | <br> |')
    for _ in range(2): a('| <br> | <br> | <br> |')
    a('\n*Add 2 more words from tonight (from the listening, the reading, or your partner).*\n')
    # listening
    a(f'---\n## {H} · Listening\n\n*{S["setting"]}*\n')
    a(f'### A. Listen. {A_["q"]} Circle.\n\n' + '     '.join(f'**{letters[i]}.** {x}' for i, x in enumerate(A_['opts'])) + '\n')
    a(taskB_page(S['B']))
    if S.get('break_before_C'): a('---')
    a(f'### C. Listen again. {S["C"]["head"]}\n\n' + numbered(S['C']['items']) + '\n')
    a(f'### Hear it, say it\n\n{S["hear"]}\n')
    # grammar
    a(f'---\n## {H} · Grammar\n\n**Read across. A reads from the left side. B answers from the right side.** Choose one part from each column.\n')
    a(G['boxes'].strip() + '\n')
    a(f'**Rule of thumb:** {G["rule"]}\n')
    a('---\n' + G['explain'].strip() + '\n')
    a('### Questions and answers\n')
    for q, ans in G['qa']: a(f'**Q: {q}**\n\nA: {ans}\n')
    a(f'---\n### Practice A: {G["A"]["head"]}\n\n' + numbered(G['A']['items']) + '\n')
    a(f'### Practice B: {G["B"]["head"]}\n\n' + numbered(G['B']['items']) + '\n')
    a('### Common mistakes\n\n| ✗ Don\'t say | ✓ Say |\n|---|---|')
    for w_, r_ in G['mistakes']: a(f'| {w_} | {r_} |')
    a('')
    if G.get('tip'): a(f'> **Contrast tip (optional):** {G["tip"]}\n')
    # talk time
    for p in L['talk']['pages']: a(f'---\n## {H} · Talk Time: {p[0]}\n\n' + p[1].strip() + '\n')
    # homework
    a(f'---\n## {H} · Homework\n\n### Homework (about 15–20 minutes). Bring it next week!\n')
    one = hw['one']; a(f'### 1. {one["head"]}\n\n*Example:* {one["example"]}\n')
    a('\n'.join(f'{i}. {x[0]} → {LONG}' for i, x in enumerate(one['items'], 1)) + '\n')
    a(f'### 2. Finish your writing from Read & Write C ({L["rw"]["write_short"]}). Read it one more time. Check ✓ the list in D.\n')
    a('☐ I finished it.     ☐ I checked it with the list.\n')
    a('---\n' + hw['three'].strip() + '\n')
    f4 = hw['four']; a(f'### 4. {f4["head"]}\n\n' + numbered(f4['items']) + '\n')
    # read & write
    a(f'---\n## {H} · Read & Write\n\n### A. Read the {rw["kind"]}. *{rw["note"]}*\n')
    a(f':::box {rw["box_title"]}\n{rw["text"].strip()}\n:::\n')
    a('### B. Answer the questions.\n\n' + '\n'.join(f'{i}. {q[0]} {LONG}' for i, q in enumerate(rw['qs'], 1)) + '\n')
    a(f'---\n### C. {rw["write_head"]}\n\n*Example:* {rw["example"]}\n')
    a(f'| {rw["box_label"]} |\n|---|\n| ' + '<br>' * rw.get('lines', 9) + ' |\n')
    a('### D. Check your writing with a partner.\n\n| | Yes | Not yet |\n|---|---|---|')
    for r in rw['checklist']: a(f'| {r} | ☐ | ☐ |')
    a('')
    # exit ticket
    E = L['exit']
    a(f'---\n## {H} · Exit Ticket\n\nName: ______________________________     Date: ________________\n')
    a(f'### Answer in 3 sentences. Give a reason. Then give this page to your teacher.\n\n**{E["q"]}**\n')
    a(f'*Sentence 1:* {E["s1"]}  •  *Sentence 2:* {E["s2"]}  •  *Sentence 3:* {E["s3"]}\n')
    a('| My answer |\n|---|\n| 1. <br><br> |\n| 2. <br><br> |\n| 3. <br><br> |\n')
    a('| For the teacher | ✓ | almost | not yet |\n|---|---|---|---|\n| 3 sentences, today\'s grammar, a reason | ☐ | ☐ | ☐ |\n')
    if L.get('cando'):
        a(f'---\n## {H} · Can-Do Self-Check\n\nName: ______________________________     Date: ________________\n')
        a('### Listen to the teacher. Check ✓ one face for each line.\n')
        a('| I can… | 😀 I can do it. | 🙂 With a little help. | 😐 Not yet. |\n|---|---|---|---|')
        for x in L['cando']: a(f'| {x} | ☐ | ☐ | ☐ |')
        a('\n### My goal for this class: write one sentence.\n\n______________________________________________________________\n')
    # task words
    a(f'---\n## {H} · Task Words (optional)\n\n*This page is for you if you want it. You can skip it.* Write each task word in your language, if you want.\n')
    a('| Task word | What you do | My language |\n|---|---|---|')
    for tw, wd in TASKS: a(f'| **{tw}** | {wd} | <br> |')
    a('')
    # credits
    a('---\n<!-- mode: guide -->\n## Picture Credits\n')
    a(f'Pictures use Twemoji graphics by Twitter, Inc. and other contributors (https://github.com/jdecked/twemoji), licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/). The graphics were resized and combined, and {L.get("drawn","signs and labels")} were added. The file-by-file list is in `images/CREDITS.md`.\n')
    a('Listening audio: synthetic voices made with Chatterbox TTS (Resemble AI, MIT License), cloned from synthetic reference clips made with Kokoro-82M (Apache License 2.0). No recordings of real people were used. Each file carries an inaudible Perth watermark marking it as AI-generated. The names and the story are invented.\n')
    a('Course materials: © 2026 the authors, licensed under CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/).')
    return '\n'.join(o) + '\n'

TASKS = [('Listen.', 'Use your ears. Don\'t write yet.'), ('Circle.', 'Draw a circle around the answer.'), ('Check ✓.', 'Make a ✓ in the box.'),
         ('Write.', 'Write words or sentences.'), ('Number.', 'Write 1, 2, 3… to show the order.'), ('Match.', 'Find the two parts that go together.'),
         ('Work with a partner.', 'Work with one classmate.'), ('Work in a group.', 'Work with 2 or 3 classmates.'), ('Switch.', 'Change roles: A is B now.'),
         ('Ask a follow-up question.', 'Ask one more question about the answer.'), ('Give a reason.', 'Say why, with *because* or *so*.'), ('Compare.', 'Look at your partner\'s answers. Are they the same?')]

def taskB_page(B):
    k = B['kind']; o = [f'### B. Listen again. {B["head"]}\n']
    if k == 'tf':
        o.append('| | True | False |\n|---|---|---|')
        for i, it in enumerate(B['items'], 1): o.append(f'| {i}. {it["s"]} | ☐ | ☐ |')
    elif k == 'choice':
        for i, it in enumerate(B['items'], 1): o.append(f'{i}. {blanks(it["s"])}')
    elif k == 'order':
        o.append('| Step | Number |\n|---|---|')
        for it in B['shown']: o.append(f'| {it} | ____ |')
    return '\n'.join(o) + '\n'
def taskB_key(B):
    k = B['kind']
    if k == 'tf': return ' • '.join(f'{i} **{"True" if it["a"] else "False"}**' + (f' ({it["fix"]})' if it.get('fix') else '') for i, it in enumerate(B['items'], 1))
    if k == 'choice': return ', '.join(f'{i} ' + ' / '.join(answers(it['s'])) for i, it in enumerate(B['items'], 1))
    if k == 'order':
        order = [it['s'] for it in B['items']]
        return ' • '.join(f'{x} **{order.index(x)+1}**' for x in B['shown'])

def estimate(L):
    S = L['listen']; w = len((S['intro'] + ' ' + ' '.join(t for _, t in S['lines']) + " That's the end of the listening.").split())
    sec = 0.37*w + 1.1*(len(S['lines'])+2); return w, sec

if __name__ == '__main__':
    d = sys.argv[1]; N = int(re.search(r'lesson(\d+)', d).group(1))
    L = load(f'{d}/spec_L4_L{N}.py'); assert L['N'] == N
    w, sec = estimate(L); r_ = round(sec); L['_est'] = f'{r_//60}:{r_%60:02d}'
    gate = os.path.join(os.path.dirname(d), '..', 'audio', f'L4_L{N}_gate.json')
    if os.path.exists(gate):
        gs = round(json.load(open(gate))['duration_s']); L['_est'] = f'{gs//60}:{gs%60:02d}'
    md = render(L).replace('{EST}', L['_est']); assert '{EST}' not in md; open(f'{d}/Level4_Lesson{N}.md', 'w').write(md)
    S = L['listen']; os.makedirs(f'{d}/build', exist_ok=True)
    cast = dict(TITLE=S['title'], VOICES=S['voices'], FEMALE=S['female'], NAMES=S.get('names', {}), SAME=S.get('same', {}),
                TTS=S.get('tts', {}), ESTIMATE=dict(words=w, seconds=round(sec)))
    json.dump(cast, open(f'{d}/build/cast_L4_L{N}.json', 'w'), indent=1, ensure_ascii=False)
    print(f'L{N}: md written, listening {w} words, about {L["_est"]}')
