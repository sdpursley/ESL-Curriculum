"""Level 5 Lesson 4 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 4 (AGENTS.md section 6)."""
from deckspec import *
N = 4
DECK_TITLE = 'Level 5 Lesson 4: Unless You Call First'
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L4_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson4.md'
LEN = '1:48'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ['I can explain *unless* in their own words', 'I can say what is allowed *as long as* something else is true', 'I can contrast with *even though*']
W = newwords(N)
for w in W:
    if len(w['word']) > 12: w['sz'] = 15
def credits(n, names, length, faces=None):
    """No Progress Check slide, so the faces line is left out."""
    c = credits_slide(n, names, 'The graphics were resized and combined, and signs and labels were added.', [audio_note(n, length, False)])
    c['pictures'] = c['pictures'][:2] + ([(2, f"The faces on the {faces} are standard emoji characters shown with the computer's emoji font.")] if faces else [])
    return c
SLIDES = [
 {
  'kind': 'title',
  'title': 'Unless You Call First',
  'title_sz': 40,
  'bullets': [
   'I can explain *unless* in their own words',
   'I can say what is allowed *as long as* something else is true',
   'I can contrast with *even though*',
  ],
  'bullet_sz': 18,
  'pic': I('policy'),
  'alt': A('policy'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   '- Say this once: "This lesson is not legal advice.',
   'Source: Level5_Lesson4.md (Topic; At a glance: Objectives).',
   PC,
  ],
 },
 {
  'kind': 'goals',
  'title': [
   "Today's",
   'Goals',
  ],
  'sz': 16,
  'side': [
   'By the end of class, you can do these things.',
  ],
  'rows': [
   'I can explain *unless* in their own words',
   'I can say what is allowed *as long as* something else is true',
   'I can contrast with *even though*',
   'I can ask one polite question about a rule they do not understand',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson4.md (At a glance: Objectives).',
  ],
 },
 {
  'kind': 'warmup',
  'kicker': 'OPENING TALK  ·  6:00',
  'title': [
   'Opening Talk',
  ],
  'box_sz': 18,
  'box1': [
   'Work with a partner. A asks a',
   'question. B answers in two or three sentences. A asks one follow-up question. Then switch.',
  ],
  'box2': [
   'Homework check: say one I wish I had',
   'sentence.',
  ],
  'pic': I('notice'),
  'alt': A('notice'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson4.md (Step 1; Opening Talk page).',
   PC,
  ],
 },
 {
  'kind': 'numlist',
  'title': [
   'Opening Talk',
   'Cards',
  ],
  'sz': 16,
  'side': [
   'Work with a partner. A asks a question. B',
   'answers in two or three sentences. A asks one follow-up question. Then switch.',
  ],
  'rows': [
   'What do you wish you had asked last week?',
   'Have you ever read a notice on a door?',
   'What do you do before you visit an office?',
   'Homework check: say one I wish I had sentence.',
  ],
  'notes': [
   'Each click shows the next card.',
   'A asks. B answers. Then switch.',
   'Source: Level5_Lesson4.md (Step 1; Opening Talk page).',
  ],
 },
 {
  'kind': 'words',
  'title': 'New Words',
  'instr': [
   'Look. Listen.',
   'Repeat.',
  ],
  'words': W[:6],
  'notes': [
   'Step 2 · 6:06–6:12 · New Words.',
   'Point to each picture. Learners repeat. ★ = most important.',
   'Source: Level5_Lesson4.md (Step 2; New Words page).',
   PCS,
  ],
 },
 {
  'kind': 'words',
  'title': 'More New Words',
  'instr': [
   'Partner game:',
   'Point and ask.',
  ],
  'words': W[6:],
  'notes': [
   'A points to a picture. B names it and uses it in one sentence. Then switch.',
   'Source: Level5_Lesson4.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'Does *unless* mean *if* or *if not*?',
    'pic': I('policy'),
    'alt': A('policy'),
    'a': 'if not',
    'q_sz': 16,
   },
   {
    'q': 'What must a visitor wear?',
    'pic': I('visitor_badge'),
    'alt': A('visitor_badge'),
    'a': 'a visitor badge',
    'q_sz': 16,
   },
   {
    'q': 'Where do you ask about a rule?',
    'pic': I('front_desk'),
    'alt': A('front_desk'),
    'a': 'the front desk',
    'q_sz': 16,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. if not',
   '2. a visitor badge',
   '3. the front desk',
   'Source: Level5_Lesson4.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'Andre did not call first.',
  'context_sz': 18,
  'pic': I('appointment'),
  'alt': A('appointment'),
  'voices': [
   'Helen',
   'Andre',
   'Mei',
  ],
  'listen': [
   'Listen. Can Andre go in now?',
   '| 6:12–6:32 | Listening: play 1 (Task A), play 2 (Tasks B and C) +',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'Andre did not call first.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson4.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. Can Andre go in now?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 15,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. Yes, he can go in',
 'b. No, not unless he calls',
 'c. The office is closed',
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson4.md (Step 3; Listening Task A; Answer key).',
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening B',
  'instr': [
   'B. Listen again. True or false? Circle.',
  ],
  'instr_sz': 16,
  'ow': 1.8,
  'og': 0.12,
  'osz': 16,
  'sz': 15,
  'right': 12.7,
  'rows': [
   ('1. He called this morning.', [
 'true',
 'false',
], 1),
   ('2. He must wear a visitor badge.', [
 'true',
 'false',
], 0),
   ('3. He can wait as long as the group finishes.', [
 'true',
 'false',
], 0),
   ('4. A guest is OK if he tells the desk.', [
 'true',
 'false',
], 0),
   ('5. Office hours end at four.', [
 'true',
 'false',
], 1),
   ('6. Even though he is on time, he must confirm.', [
 'true',
 'false',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 false • 2 true • 3 true • 4 true • 5 false • 6 true',
   'Source: Level5_Lesson4.md (Step 3; Listening Task B; Answer key).',
  ],
 },
 {
  'kind': 'gaps',
  'title': [
   'Listening C',
  ],
  'side': [
   'Write the missing words.',
   'Then check together.',
  ],
  'head1': 'Listen again.',
  'head2': 'Listen again. Write unless, ',
  'sz': 14,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ("You can't go in ______ you call first.", 'unless'),
   ('______ you are on time, you still need to confirm.', 'Even though'),
   ('You can wait ______ the group finishes on time.', 'as long as'),
   ('You can bring a guest ______ you tell the front desk.', 'as long as'),
   ('______ you confirm, the desk cannot make an exception.', 'Unless'),
   ('The room is closed ______ they finish on time.', 'unless'),
  ],
  'notes': [
   'Click to show each answer: 1 unless • 2 Even though • 3 as long as • 4 as long as • 5 Unless • 6 unless',
   'Source: Level5_Lesson4.md (Step 3; Listening Task C; Answer key).',
  ],
 },
 {
  'kind': 'checksay',
  'title': [
   'Hear It,',
   'Say It',
  ],
  'side': [
   '*gonna* and *wanna* are short forms. This listening uses the full forms.',
   'You can say *going to* and *want to*.',
   'Say each line *two times.*',
  ],
  'head1': 'Hear it: gonna and wanna are short forms',
  'head2': 'Say it: use the full forms',
  'head_chip': None,
  'head_sz': 16,
  'say_sz': 18,
  'says': [
   "I *want to* go to the four o'clock meeting.",
   'I am *going to* call tomorrow.',
   "You can't go in unless you call first.",
   'You can wait as long as the group finishes.',
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson4.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'unless means if not',
  ],
  'title_sz': 20,
  'qhead': 'SENTENCE',
  'ahead': 'MEANING',
  'pic': I('cancel'),
  'alt': A('cancel'),
  'lw': 4.6,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ("You can't go in **unless** you sign the book.", 'if you do **not** sign'),
   ("You can't go in **unless** you call first.", 'if you do **not** call'),
   ('**Unless** you confirm, they will not hold the room.', 'present verb after *unless*'),
  ],
  'notes': [
   'Grammar Box 1: unless means if not. Each click shows the answer side.',
   'Source: Level5_Lesson4.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'as long as',
  ],
  'title_sz': 22,
  'qhead': 'SENTENCE',
  'ahead': 'MEANING',
  'pic': I('confirm'),
  'alt': A('confirm'),
  'lw': 4.6,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('You can bring a guest **as long as** you tell the desk.', 'only if you tell them'),
   ('You can wait **as long as** the group finishes on time.', 'only if that stays true'),
   ('**As long as** you call first, they will hold the room.', 'present verb, same as *if*'),
  ],
  'notes': [
   'Grammar Box 2: as long as. Each click shows the answer side.',
   'Source: Level5_Lesson4.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   'even though',
  ],
  'title_sz': 22,
  'qhead': 'SENTENCE',
  'ahead': 'MEANING',
  'pic': I('visitor'),
  'alt': A('visitor'),
  'lw': 4.6,
  'lsz': 13,
  'rsz': 14,
  'pitch_max': 1.05,
  'rows': [
   ('**Even though** the office is busy, you still need an appointment.', 'the result happens anyway'),
   ('**Even though** you are on time, you still need to confirm.', 'on time does not change the rule'),
   ('**Even though** you have permission, you still sign the book.', 'permission is not enough'),
  ],
  'notes': [
   'Grammar Box 3: even though. Each click shows the answer side.',
   'Source: Level5_Lesson4.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   'have to, must, and if',
  ],
  'title_sz': 20,
  'qhead': 'SENTENCE',
  'ahead': 'MEANING',
  'pic': I('front_desk'),
  'alt': A('front_desk'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('You **have to** sign the book.', 'a requirement'),
   ('You **must** wear the visitor badge.', 'a requirement'),
   ('**If** you call first, they **will** hold the room.', '*if* + present, then *will*'),
  ],
  'notes': [
   'Grammar Box 4: have to, must, and if. Each click shows the answer side.',
   'Source: Level5_Lesson4.md (Step 4; Grammar Box 4).',
   PC,
  ],
 },
 {
  'kind': 'gaps',
  'title': [
   'Practice A',
  ],
  'side': [
   'Write the missing word.',
   'Pairs: check your answers.',
  ],
  'head1': 'Practice A',
  'head2': 'Write.',
  'sz': 14,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ("You can't go in ______ you sign the book.", 'unless'),
   ('You can bring a guest ______ you tell the front desk.', 'as long as'),
   ('______ the office is busy, you still need an appointment.', 'Even though'),
   ('______ you call first, they will not hold the room.', 'Unless'),
   ('You still sign the book ______ you have permission.', 'even though'),
   ('They will hold the room ______ you confirm.', 'as long as'),
  ],
  'notes': [
   'Click to show each answer: 1 unless • 2 as long as • 3 Even though • 4 Unless • 5 even though • 6 as long as',
   'Source: Level5_Lesson4.md (Step 4; Grammar Practice A; Answer key).',
  ],
 },
 {
  'kind': 'choice',
  'title': 'Practice B',
  'instr': [
   'Circle the correct words.',
  ],
  'ow': 1.8,
  'og': 0.12,
  'osz': 16,
  'sz': 15,
  'right': 12.7,
  'rows': [
   ("1. Unless you ______ first, you can't go in.", [
 'call',
 'will call',
], 0),
   ('2. As long as you ______ the desk, you can bring a guest.', [
 'tell',
 'will tell',
], 0),
   ('3. Even though he is on time, he ______ confirm.', [
 'still must',
 "doesn't",
], 0),
   ('4. You ______ wear the visitor badge.', [
 'must',
 'must to',
], 0),
   ('5. If you call first, they ______ the room.', [
 'hold',
 'will hold',
], 1),
   ('6. You have to sign ______ you already have permission.', [
 'unless',
 'even though',
], 1),
  ],
  'notes': [
   'Click to circle each answer: 1 call • 2 tell • 3 still must • 4 must • 5 will hold • 6 even though',
   'Source: Level5_Lesson4.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('office_hours'),
  'alt': A('office_hours'),
  'sz': 14,
  'rows': [
   ('Unless you will call, they will not hold the room.', 'Unless you **call**, they will not hold the room.'),
   ('As long as you will tell them, you can bring a guest.', 'As long as you **tell** them, you can bring a guest.'),
   ('Even though the office is busy, but you need an appointment.', '**Even though** the office is busy, you still need an appointment.'),
   ('You must to wear the badge.', 'You **must** wear the visitor badge.'),
   ('If you will call first, they will hold the room.', '**If you call** first, they will hold the room.'),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson4.md (Grammar: Common mistakes).',
   PC,
  ],
 },
 {
  'kind': 'drill',
  'title': 'Pair Check',
  'sub': 'Work with a partner.',
  'sub_sz': 18,
  's1_label': 'A says.',
  's1_body': [
   '| Strip | Word | |---|---| | 1.',
  ],
  's2_label': 'B answers.',
  's2_body': [
   "You can't go in unless you call first.",
  ],
  'pic': I('requirement'),
  'alt': A('requirement'),
  'notes': [
   "| Strip | Word | |---|---| | 1. You can't go in unless you call first. | <br | | 2. You can wait as long as the group finishes on time. | <br | | 3. Even though you are on time, you still need to confirm. | <br | | 4.",
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson4.md (Step 4: Pair check).',
   PC,
  ],
 },
 {
  'kind': 'talk',
  'head': [
   'Talk Time',
   'Talk Time',
  ],
  'grouping': [
   'Groups.',
   'Match each strip to unless, as long as, or even though.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('confirm'),
  'alt': A('confirm'),
  'steps': [
   [
    'Match each strip to unless, as long as, or',
    'even though.',
   ],
   [
    'Match each strip to unless, as long as, or even though.',
   ],
   [
    'Match each strip to unless, as long as, or even though.',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson4.md (Step 5; Talk Time).',
   PC,
  ],
 },
 {
  'kind': 'talk',
  'head': [
   'Talk Time',
   'Talk Time',
  ],
  'grouping': [
   'Work together.',
   'A is the front desk.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('front_desk'),
  'alt': A('front_desk'),
  'steps': [
   [
    'A is the front desk.',
   ],
   [
    'Then switch.',
   ],
   [
    'Then switch.',
   ],
  ],
  'notes': [
   'Round 2.',
   'Source: Level5_Lesson4.md (Step 5; Talk Time).',
   PC,
  ],
 },
 {
  'kind': 'gaps',
  'title': [
   'Read &',
   'Write',
  ],
  'side': [
   'Read the page.',
   'Answer the questions.',
  ],
  'head1': 'Read.',
  'head2': 'Answer.',
  'sz': 16,
  'aw': 2.8,
  'asz': 13,
  'rows': [
   ('Go in without calling first?', 'No. Call first'),
   ('What must a visitor wear?', 'A visitor badge'),
   ('When can you bring a guest?', 'Tell the front desk first'),
   ('What are the office hours?', 'Nine to five'),
   ('Who explains a rule?', 'The front desk'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   'Click to show each answer: 1 No. Call first • 2 A visitor badge • 3 Tell the front desk first • 4 Nine to five • 5 The front desk',
   'Source: Level5_Lesson4.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('permission'),
  'alt': A('permission'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'Explain one rule from tonight.'),
   (1, 'Name: Date:'),
   (1, 'Sentence 1: the rule • Sentence 2: unless or as long as • Sentence 3: an'),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, '1. Write three sentences: one with unless, one with as long as, and'),
   (1, '2. Finish your 6-sentence note from Read & Write C. Use unless once'),
   (1, '3. Write one polite question about a class rule. Do not write about a'),
   (1, '4. Review. Write have to or must.'),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'Explain one rule from tonight.',
   'Source: Level5_Lesson4.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   'I can explain *unless* in their own words',
   'I can say what is allowed *as long as* something else is true',
   'I can contrast with *even though*',
  ],
  'bullet_sz': 18,
  'pic': I('exception'),
  'alt': A('exception'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson4.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Helen, Andre, and Mei', LEN),
]
