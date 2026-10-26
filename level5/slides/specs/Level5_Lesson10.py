"""Level 5 Lesson 10 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 10 (AGENTS.md section 6)."""
from deckspec import *
N = 10
DECK_TITLE = 'Level 5 Lesson 10: Can We Meet in the Middle?'
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L10_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson10.md'
LEN = '2:11'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ['I can say what they need and ask what the other person needs', 'I can offer a middle idea', 'I can explain a result with *so… that* or *such… that*']
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
  'title': 'Can We Meet in the Middle?',
  'title_sz': 40,
  'bullets': [
   'I can say what they need and ask what the other person needs',
   'I can offer a middle idea',
   'I can explain a result with *so… that* or *such… that*',
  ],
  'bullet_sz': 18,
  'pic': I('compromise'),
  'alt': A('compromise'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   'Source: Level5_Lesson10.md (Topic; At a glance: Objectives).',
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
   'I can say what they need and ask what the other person needs',
   'I can offer a middle idea',
   'I can explain a result with *so… that* or *such… that*',
   'I can use *work out*, *call off*, or *give in* in a real sentence',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson10.md (At a glance: Objectives).',
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
   'Work with a partner. A asks a card',
   'question. B answers in about four sentences. A asks one follow-up. Then switch.',
  ],
  'box2': [
   'sentences. A asks one follow-up. Then',
   'switch.',
  ],
  'pic': I('offer'),
  'alt': A('offer'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson10.md (Step 1; Opening Talk page).',
   PC,
  ],
 },
 {
  'kind': 'numlist',
  'title': [
   'Opening Talk',
   'Cards',
  ],
  'sz': 15,
  'side': [
   'Work with a partner. A asks a card question. B',
   'answers in about four sentences. A asks one follow-up. Then switch.',
  ],
  'rows': [
   'Work with a partner. A asks a card question. B answers in about four',
   'sentences. A asks one follow-up. Then switch.',
  ],
  'notes': [
   'Each click shows the next card.',
   'A asks. B answers. Then switch.',
   'Source: Level5_Lesson10.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson10.md (Step 2; New Words page).',
   PCS,
  ],
 },
 {
  'kind': 'words',
  'title': 'More New Words',
  'instr': [
   'Partner game:',
   'Say it in a sentence',
  ],
  'words': W[6:],
  'notes': [
   'A points to a picture. B names it and uses it in one sentence. Then switch.',
   'Source: Level5_Lesson10.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'Is a compromise one person winning?',
    'pic': I('compromise'),
    'alt': A('compromise'),
    'a': 'No. A middle idea.',
    'q_sz': 16,
   },
   {
    'q': 'Does *give in* take an object here?',
    'pic': I('offer'),
    'alt': A('offer'),
    'a': 'No.',
    'q_sz': 16,
   },
   {
    'q': 'Which is right: *so busy that*, or *so busy so*?',
    'pic': I('counteroffer'),
    'alt': A('counteroffer'),
    'a': '*so busy that*',
    'q_sz': 14,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. No. A middle idea.',
   '2. No.',
   '3. *so busy that*',
   'Source: Level5_Lesson10.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'Camila and Jon both need Saturday.',
  'context_sz': 18,
  'pic': I('counteroffer'),
  'alt': A('counteroffer'),
  'voices': [
   'Ms. Nguyen',
   'Camila',
   'Jon',
  ],
  'listen': [
   'Listen. What is the problem?',
   '| 6:12–6:32 | Listening (play 1 Task A, play 2 Tasks B and C) + Hear',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'Camila and Jon both need Saturday.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson10.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. What is the problem?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 15,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. Camila wants a new job',
 'b. Both need Saturday off',
 'c. The store is closed',
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson10.md (Step 3; Listening Task A; Answer key).',
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening B',
  'instr': [
   'B. Listen again. Circle the answers.',
  ],
  'instr_sz': 16,
  'ow': 2.45,
  'og': 0.05,
  'osz': 12,
  'sz': 13,
  'right': 13.1,
  'rows': [
   ("1. Camila's priority", [
 'a morning class',
 'an afternoon visit',
 'a second job',
], 0),
   ("2. Jon's limit", [
 'a morning class',
 'an afternoon visit',
 'the whiteboard',
], 1),
   ('3. They swap at', [
 'ten',
 'twelve',
 'four',
], 1),
   ('4. The shift was', [
 'so short',
 'such a long shift',
 'too easy',
], 1),
   ('5. They write the plan on', [
 'a sticky note',
 'a napkin',
 'a menu',
], 0),
   ('6. Ms. Nguyen is going to', [
 'call it off',
 'not call it off',
 'give in',
], 1),
  ],
  'notes': [
   'Click to circle each answer: 1 a morning class • 2 an afternoon visit • 3 twelve • 4 such a long shift • 5 a sticky note • 6 not call it off',
   'Source: Level5_Lesson10.md (Step 3; Listening Task B; Answer key).',
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
  'head2': 'Listen again. Write so or su',
  'sz': 14,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ('The week was ______ busy that we split Saturday.', 'so'),
   ('It was ______ a long shift that we shared it.', 'such'),
   ('The visit is ______ important that I need the afternoon.', 'so'),
   ('Noon is ______ a clear time that nobody has to guess.', 'such'),
   ('The week was ______ busy that we need Saturday.', 'so'),
   ('My class is ______ important that I need the morning.', 'so'),
  ],
  'notes': [
   'Click to show each answer: 1 so • 2 such • 3 so • 4 such • 5 so • 6 so',
   'Source: Level5_Lesson10.md (Step 3; Listening Task C; Answer key).',
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
   'I *want to* take the morning off.',
   'I was *going to* ask for the whole day too.',
   "I'm *going to* work the morning.",
   'What if WE split the day?',
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson10.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'a middle idea',
  ],
  'title_sz': 22,
  'qhead': 'YOU CAN SAY',
  'ahead': 'A MIDDLE IDEA',
  'pic': I('priority'),
  'alt': A('priority'),
  'lw': 4.6,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('What if we split the day?', 'I can take the morning if you take the afternoon.'),
   ("Let's meet in the middle.", 'We can swap at twelve.'),
   ('Say the other idea first.', 'You need the afternoon. I need the morning.'),
  ],
  'notes': [
   'Grammar Box 1: a middle idea. Each click shows the answer side.',
   'Source: Level5_Lesson10.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'so… that / such… that',
  ],
  'title_sz': 20,
  'qhead': 'PATTERN',
  'ahead': 'EXAMPLE',
  'pic': I('shared_task'),
  'alt': A('shared_task'),
  'lw': 4.6,
  'lsz': 13,
  'rsz': 14,
  'pitch_max': 1.05,
  'rows': [
   ('*so* + adjective + *that*', 'The week was so busy that we split Saturday.'),
   ('*such* + *a* + adjective + noun + *that*', 'It was such a long shift that we shared it.'),
   ('*so* + adjective + *that*', 'The visit is so important that Jon needs the afternoon.'),
   ('*such* + *a* + adjective + noun + *that*', 'Noon is such a clear time that nobody has to guess.'),
  ],
  'notes': [
   'Grammar Box 2: so… that / such… that. Each click shows the answer side.',
   'Source: Level5_Lesson10.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   'work out, call off, give',
  ],
  'title_sz': 20,
  'qhead': 'REVIEW',
  'ahead': 'A REAL SENTENCE',
  'pic': I('solution'),
  'alt': A('solution'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('work it out', 'We can work it out.'),
   ('call it off', 'She is not going to call it off.'),
   ('call the shift off', 'Noun after, or *it* in the middle: call it off.'),
   ('give in', "We didn't give in. No object."),
  ],
  'notes': [
   'Grammar Box 3: work out, call off, give in (review). Each click shows the answer side.',
   'Source: Level5_Lesson10.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   "don't mix them",
  ],
  'title_sz': 22,
  'qhead': "DON'T MIX THEM",
  'ahead': 'SAY',
  'pic': I('fairness'),
  'alt': A('fairness'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('*so* + adjective + *that*', 'The week was so busy that we split Saturday.'),
   ('*such a* + adjective + noun', 'It was such a long shift that we shared it.'),
   ('*too* + adjective + *for*', 'The week is too full for one person.'),
  ],
  'notes': [
   "Grammar Box 4: don't mix them. Each click shows the answer side.",
   'Source: Level5_Lesson10.md (Step 4; Grammar Box 4).',
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
   ('The week was ______ busy that we split Saturday.', 'so'),
   ('It was ______ a long shift that we shared it.', 'such'),
   ('The week is ______ full for one person.', 'too'),
   ('The class is ______ important that she needs the morning.', 'so'),
   ('It was ______ a fair plan that they both said yes.', 'such'),
   ('We can work ______.', 'it out'),
  ],
  'notes': [
   'Click to show each answer: 1 so • 2 such • 3 too • 4 so • 5 such • 6 it out',
   'Source: Level5_Lesson10.md (Step 4; Grammar Practice A; Answer key).',
  ],
 },
 {
  'kind': 'choice',
  'title': 'Practice B',
  'instr': [
   'Circle the correct words.',
  ],
  'ow': 2.45,
  'og': 0.12,
  'osz': 16,
  'sz': 15,
  'right': 12.7,
  'rows': [
   ('1. The week was ______ busy that we split it.', [
 'so',
 'such',
], 0),
   ('2. It was ______ a long shift.', [
 'so',
 'such',
], 1),
   ('3. Work ______ .', [
 'it out',
 'out it',
], 0),
   ('4. Call ______ .', [
 'it off',
 'off it',
], 0),
   ("5. We didn't ______ .", [
 'give in',
 'give in the argument',
], 0),
   ('6. The week is ______ full for one person.', [
 'too',
 'such',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 so • 2 such • 3 it out • 4 it off • 5 give in • 6 too',
   'Source: Level5_Lesson10.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('sticky_note'),
  'alt': A('sticky_note'),
  'sz': 14,
  'rows': [
   ('The week was so busy so we split it.', 'The week was **so busy that** we split it.'),
   ('It was so long shift.', 'It was **such a long shift**.'),
   ('Give in the argument.', '**Give in.** No object here.'),
   ('Work out it.', '**Work it out.**'),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson10.md (Grammar: Common mistakes).',
   PC,
  ],
 },
 {
  'kind': 'drill',
  'title': 'Pair Check',
  'sub': 'Then switch.',
  'sub_sz': 18,
  's1_label': 'A says.',
  's1_body': [
   'A says a need: "I need the morning for a class." B says it back, then offers: "You need',
  ],
  's2_label': 'B answers.',
  's2_body': [
   'What if I take the afternoon?" Then switch.',
  ],
  'pic': I('break_time'),
  'alt': A('break_time'),
  'notes': [
   'A says a need: "I need the morning for a class." B says it back, then offers: "You need the morning. What if I take the afternoon?" Then switch. ---',
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson10.md (Step 4: Pair check).',
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
   'Pairs.',
   'Pairs.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('shared_task'),
  'alt': A('shared_task'),
  'steps': [
   [
    'Pairs.',
   ],
   [
    'Pairs.',
   ],
   [
    'Pairs.',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson10.md (Step 5; Talk Time).',
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
   'Pairs.',
   'Groups of 3.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('fairness'),
  'alt': A('fairness'),
  'steps': [
   [
    'Groups of 3.',
   ],
   [
    'Groups of 3.',
   ],
   [
    'Groups of 3.',
   ],
  ],
  'notes': [
   'Round 2.',
   'Source: Level5_Lesson10.md (Step 5; Talk Time).',
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
   ('What is the shared task?', 'The Saturday shift'),
   ("What is Camila's priority?", 'A morning class'),
   ('When do they swap?', 'At noon'),
   ('Where did they copy the plan?', 'On the whiteboard'),
   ('Is Ms. Nguyen going to call the shift off?', 'No. She will not call it off'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   'Click to show each answer: 1 The Saturday shift • 2 A morning class • 3 At noon • 4 On the whiteboard • 5 No. She will not call it off',
   'Source: Level5_Lesson10.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('swap'),
  'alt': A('swap'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'Describe a small compromise.'),
   (1, 'Name: Date:'),
   (1, '1.'),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, '1. Write one so… that sentence.'),
   (1, '2. Finish your message (Read & Write).'),
   (1, '3. Tell a friend a small compromise. Write one sentence they said.'),
   (1, '4. Review: work it out, call it off, give in. Write one real sentence'),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'Describe a small compromise.',
   'Source: Level5_Lesson10.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   'I can say what they need and ask what the other person needs',
   'I can offer a middle idea',
   'I can explain a result with *so… that* or *such… that*',
  ],
  'bullet_sz': 18,
  'pic': I('whiteboard'),
  'alt': A('whiteboard'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson10.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Ms. Nguyen, Camila, and Jon', LEN),
]
