"""Standard Level 4 step boxes and clock rows (the weekly routine in the Level 4 Scope and Sequence, Section 4.1).
Lesson specs import these and pass only what changes from week to week."""
def clock(opening, newwords, listening, grammar, talk, rw, talk_group='Pairs, then groups of 3 / pairs, then 2 groups', talk_behind='Round 1 only',
          rw_name=None):
    return [
        ('6:00–6:08', f'**Opening Talk + Homework Check**{opening}', '8', 'Pairs (7 pairs + 1 trio / 3–4 pairs)', 'One card only'),
        ('6:08–6:15', f'**New Words** (picture page) + pair game{newwords}', '7', 'Whole class, then pairs', 'Teach the ★ words only'),
        ('6:15–6:30', f'**Listening:** play 1 (Task A), play 2 (Tasks B and C) + "Hear it, say it"{listening}', '15', 'Individuals, then pairs check', 'Do Task C together on the board'),
        ('6:30–6:45', f'**Grammar Q&A:** {grammar} + pair check', '15', 'Whole class, then pairs', 'Skip the pair check; Talk Time practices it'),
        ('6:45–7:00', 'BREAK', '15', '', ''),
        ('7:00–7:15', f'**Talk Time: {talk}**', '15', talk_group, talk_behind),
        ('7:15–7:25', f'**Read & Write:** {rw}', '10', 'Pairs read, then individual writing', 'Reading questions only; the writing becomes homework'),
        ('7:25–7:30', '**Exit Ticket + Homework**', '5', 'Individuals', '**Never skip**'),
    ]

def step1(name, board, model, hw_check, errors, extra=()):
    return ('Step 1 · 6:00–6:08 · ' + name + ' · 8 min', [
        '**Grouping:** pairs, the same partner for both parts. 15 learners: 7 pairs + 1 group of 3. 7–8 learners: 3–4 pairs. 5 or fewer: pairs, or one group with you.',
        f'**Before class:** write on the board: {board}',
        '**Opening Talk (5 min):** learners open the **Opening Talk** page. A asks a card question; B answers in **3 sentences** (the answer, a reason, a detail); A asks one follow-up. Switch after each card.',
        f'**Model with one learner:** {model}',
        f'**Homework Check (3 min):** {hw_check} Walk around. Write **2** common errors on the board (often {errors}) and correct them together. Also put up 2 corrections from last week\'s exit tickets.' if errors else f'**Then (3 min):** {hw_check}',
        *extra,
        '**Late arrivals:** join any pair as a group of 3.',
        '**If behind:** one card only.'])

def step2(show, check, pair_ex, extra=()):
    return ('Step 2 · 6:08–6:15 · New Words · 7 min', [
        '**Grouping:** whole class, then pairs. Show the New Words page.',
        '**Do:** point to each picture and say the word. Learners repeat once.',
        f'**Show the hard words:** {show}',
        f'**Check meaning (1 min):** {check}',
        f'**Pairs (2 min):** A says a word; B points to the picture and makes a sentence ({pair_ex}). Switch. **15 learners:** finish with a quick team round (3 teams; you say a clue, the first team with the word gets a point). **7–8:** 2 teams. **5 or fewer:** one team against the clock.',
        '**My Words:** "Write any word you want in your language on the My Words page. It\'s your personal list. It\'s optional." Learners do it at home.',
        *extra,
        '**If behind:** teach the ★ words only.'])

def step3(before, hear, length, extra=()):
    return ('Step 3 · 6:15–6:30 · Listening + "Hear it, say it" · 15 min', [
        '**Grouping:** individuals, then pairs check. With 5 or fewer, check together as a group.',
        f'**Before you listen (2 min):** say: "{before}"',
        '**Play 1 → Task A** (the main idea). Pairs compare. Check together.',
        '**Read Tasks B and C together (1 min)** so learners know what to listen for.',
        '**Play 2 → Tasks B and C.** Pairs compare. Then show the answers (answer key).',
        f'**"Hear it, say it" (3 min):** {hear} The class repeats the two lines twice.',
        f'**The audio plays the conversation once (about {length}).** Press play again for play 2. A third play is fine if the class needs it. The script says *going to* and *want to*. People often say *gonna* and *wanna*; learners only need to recognize those words.',
        *extra,
        '**If behind:** do Task C together on the board, reading the lines yourself.'])

def step4(focus, show, boxes, checks, drill, extra=()):
    return ('Step 4 · 6:30–6:45 · Grammar Q&A · 15 min', [
        '**Grouping:** whole class, then pairs. Show the Grammar page. The **left side is the question. The right side is the answer.**',
        f'**Show it (2 min):** {show}',
        f'**The boxes (5 min):** {boxes}',
        '**Rule of thumb and Questions and answers (2 min):** read the rule of thumb aloud. Read each Q and A; the class reads the right sentence after you.',
        f'**Check questions:** {checks}',
        '**Practice A and B (3 min):** learners write, then pairs check. Go over the answers. Read the Common mistakes table together: "Don\'t say… Say…".',
        f'**Pair check (last 3 min):** {drill} **15 learners:** swap partners once. **5 or fewer:** you join one pair.',
        *extra,
        '**If behind:** skip the pair check. Talk Time practices it.'])

def brk(board): return ('Break · 6:45–7:00 · 15 min', [f'Write on the board: {board}'])

def step5(name, model, r1, r2, v15, v78, v5, extra=()):
    return (f'Step 5 · 7:00–7:15 · Talk Time: {name} · 15 min', [
        f'**Model it first (1 min):** {model}',
        f'**Round 1 (7 min):** {r1}',
        f'**Round 2 (6 min):** {r2}',
        f'**15 learners:** {v15}', f'**7–8 learners:** {v78}', f'**5 or fewer:** {v5}',
        '**Every answer needs a reason; every partner asks a follow-up.** Walk around and listen. Note 2 good sentences to praise and 1 common error for next week.',
        *extra,
        '**If behind:** round 1 only.'])

def step6(name, read, write, extra=()):
    return (f'Step 6 · 7:15–7:25 · Read & Write: {name} · 10 min', [
        '**Grouping:** pairs read and answer; individual writing. With 5 or fewer, read the text aloud together.',
        f'**Read (4 min):** {read} Say: "Read fast first. Then find the answers." Pairs answer questions 1–5 together.',
        '**Check (1 min):** go over the answers (answer key).',
        f'**Write (5 min):** {write} Learners start in class and finish at home (Homework item 2).',
        *extra,
        '**If behind:** questions 1–5 only; the writing becomes homework.'])

def step7(q, example, hw1, extra=()):
    return ('Step 7 · 7:25–7:30 · Exit Ticket + Homework · 5 min · NEVER SKIP', [
        f'**Exit ticket (3 min):** learners open the Exit Ticket page and answer in **3 sentences** with a reason: *{q}* Example on the board: *{example}* With 5 or fewer, a learner can say it to you first and then write it.',
        '**Collect the pages.** After class, sort them into ✓ / almost / not yet. Start next week with 2 corrections on the board (no names).',
        f'**Homework (2 min):** open the Homework page. Do item 1 together ({hw1}). Say: "About 15–20 minutes. Finish your Read & Write writing at home."',
        *extra])
