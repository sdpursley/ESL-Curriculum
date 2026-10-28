"""Level 5 Lesson 5 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 5 (AGENTS.md section 6)."""
from deckspec import *
N = 5
DECK_TITLE = 'Level 5 Lesson 5: It Was Posted on Tuesday'
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L5_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson5.md'
LEN = '1:43'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ['I can say what is done with is or are and was or were plus a participle.', 'I can add by when the doer matters.', 'I can find the amount due, the due date, and one charge.']
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
  'title': 'It Was Posted on Tuesday',
  'title_sz': 40,
  'bullets': [
   'I can say what is done with is or are and was or were plus a participle.',
   'I can add by when the doer matters.',
   'I can find the amount due, the due date, and one charge.',
  ],
  'bullet_sz': 18,
  'pic': I('statement'),
  'alt': A('statement'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   'This lesson is not financial advice.',
   'Source: Level5_Lesson5.md (Topic; At a glance: Objectives).',
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
   'I can say what is done with is or are and was or were plus a participle.',
   'I can add by when the doer matters.',
   'I can find the amount due, the due date, and one charge.',
   'I can write a three-line budget with invented numbers.',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson5.md (At a glance: Objectives).',
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
   'Work with a partner. Ask about a',
   'mild regret from last week. Then switch.',
  ],
  'box2': [
   'Homework check: read one sentence from',
   'your note.',
  ],
  'pic': I('charge'),
  'alt': A('charge'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson5.md (Step 1; Opening Talk page).',
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
   'Work with a partner. Ask about a mild regret',
   'from last week. Then switch.',
  ],
  'rows': [
   'Say one I wish I had sentence from Lesson 3.',
   'Say one next step you wrote.',
   'Which wish was about now?',
   'Homework check: read one sentence from your note.',
  ],
  'notes': [
   'Each click shows the next card.',
   'A asks. B answers. Then switch.',
   'Source: Level5_Lesson5.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson5.md (Step 2; New Words page).',
   PCS,
  ],
 },
 {
  'kind': 'words',
  'title': 'More New Words',
  'instr': [
   'Partner game:',
   'Point and say the word',
  ],
  'words': W[6:],
  'notes': [
   'A points to a picture. B names it and uses it in one sentence. Then switch.',
   'Source: Level5_Lesson5.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'Is a statement a bill you can read?',
    'pic': I('statement'),
    'alt': A('statement'),
    'a': 'yes',
    'q_sz': 16,
   },
   {
    'q': 'What do you keep to show you paid?',
    'pic': I('receipt'),
    'alt': A('receipt'),
    'a': 'a receipt',
    'q_sz': 16,
   },
   {
    'q': 'What word means money back on this page?',
    'pic': I('credit'),
    'alt': A('credit'),
    'a': 'credit',
    'q_sz': 16,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. yes',
   '2. a receipt',
   '3. credit',
   'Source: Level5_Lesson5.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'Diego calls customer service about a statement.',
  'context_sz': 18,
  'pic': I('payment'),
  'alt': A('payment'),
  'voices': [
   'Narrator',
   'Diego',
   'Ms. Brooks',
  ],
  'listen': [
   'Listen. Why is he calling?',
   '| 6:12–6:32 | Listening.',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'Diego calls customer service about a statement.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson5.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. Why is he calling?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 13,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. The store is closed',
 'b. A fee was added, and a payment was posted',
 'c. His phone was lost',
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson5.md (Step 3; Listening Task A; Answer key).',
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening B',
  'instr': [
   'B. Listen again. Circle the amount or',
   'the day.',
  ],
  'instr_sz': 16,
  'ow': 2.45,
  'og': 0.05,
  'osz': 12,
  'sz': 13,
  'right': 13.1,
  'rows': [
   ('1. The fee was added', [
 'on Tuesday',
 'on Friday',
 'in May',
], 0),
   ('2. The payment was received', [
 'on Friday',
 'on Tuesday',
 'not yet',
], 0),
   ('3. The fee was', [
 '$6',
 '$60',
 '$600',
], 0),
   ('4. Credit on this page means', [
 'money back',
 'a new phone',
 'a late day',
], 0),
   ('5. Due today', [
 '$0',
 '$40',
 '$90',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 on Tuesday • 2 on Friday • 3 $6 • 4 money back • 5 $0',
   'Source: Level5_Lesson5.md (Step 3; Listening Task B; Answer key).',
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
  'head2': 'Listen again. Write the pass',
  'sz': 16,
  'aw': 2.3,
  'asz': 14,
  'rows': [
   ('The fee ______ on Tuesday.', 'was added'),
   ('The payment ______ on Friday.', 'was received'),
   ('The credit ______ by the phone company.', 'was posted'),
   ('The bill ______ on the first of the month.', 'is mailed'),
   ('The calls ______ on the statement.', 'are listed'),
   ('No, the fee ______.', "wasn't removed"),
  ],
  'notes': [
   "Click to show each answer: 1 was added • 2 was received • 3 was posted • 4 is mailed • 5 are listed • 6 wasn't removed",
   'Source: Level5_Lesson5.md (Step 3; Listening Task C; Answer key).',
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
   'I *want to* understand this statement.',
   'I am *going to* check the due date.',
   'The fee was added on Tuesday.',
   'The payment was received on Friday.',
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson5.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'is, are, was, were',
  ],
  'title_sz': 22,
  'qhead': 'SENTENCE',
  'ahead': 'FORM',
  'pic': I('balance'),
  'alt': A('balance'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('The bill **is mailed** on the first.', 'present passive'),
   ('The fee **was added** on Tuesday.', 'past passive'),
   ('The payment **was received** on Friday.', 'past passive'),
  ],
  'notes': [
   'Grammar Box 1: is, are, was, were. Each click shows the answer side.',
   'Source: Level5_Lesson5.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'add by when you need the',
  ],
  'title_sz': 20,
  'qhead': 'SENTENCE',
  'ahead': 'WHY',
  'pic': I('fee'),
  'alt': A('fee'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('The credit **was posted by** the phone company.', 'by names the doer'),
   ('The fee **was added by** the company.', 'use by when you need the name'),
   ('The payment **was received**.', 'no by: start with the thing'),
  ],
  'notes': [
   'Grammar Box 2: add by when you need the name. Each click shows the answer side.',
   'Source: Level5_Lesson5.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   'yes and no',
  ],
  'title_sz': 22,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('receipt'),
  'alt': A('receipt'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('**Are** the calls **listed**?', 'Yes, they are.'),
   ('**Was** the fee **removed**?', "No, it wasn't."),
   ('**Was** the payment **received**?', 'Yes, it was.'),
  ],
  'notes': [
   'Grammar Box 3: yes and no. Each click shows the answer side.',
   'Source: Level5_Lesson5.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   'start with the thing',
  ],
  'title_sz': 20,
  'qhead': 'SAY THIS',
  'ahead': 'NOT THIS IDEA',
  'pic': I('refund'),
  'alt': A('refund'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('The fee **is too high**.', 'one review line'),
   ('The payment **was posted**.', 'start with the thing'),
   ('The company **posted** the payment.', 'active, when the person matters'),
  ],
  'notes': [
   'Grammar Box 4: start with the thing. Each click shows the answer side.',
   'Source: Level5_Lesson5.md (Step 4; Grammar Box 4).',
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
  'sz': 16,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ('The fee was ______ on Tuesday.', 'added'),
   ('The payment was ______ on Friday.', 'received'),
   ('The credit was ______ by the phone company.', 'posted'),
   ('The bill is ______ on the first.', 'mailed'),
   ('The calls are ______.', 'listed'),
   ('The fee is too ______.', 'high'),
  ],
  'notes': [
   'Click to show each answer: 1 added • 2 received • 3 posted • 4 mailed • 5 listed • 6 high',
   'Source: Level5_Lesson5.md (Step 4; Grammar Practice A; Answer key).',
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
  'osz': 13,
  'sz': 15,
  'right': 12.7,
  'rows': [
   ('1. The fee', [
 'was added',
 'was add',
], 0),
   ('2. The payment', [
 'was received',
 'received',
], 0),
   ('3. The company', [
 'posted the payment',
 'was posted the payment',
], 0),
   ('4. The credit was posted', [
 'by the phone company',
 'for the phone company',
], 0),
   ('5. Are the calls listed?', [
 'Yes, they are.',
 'Yes, they listed.',
], 0),
   ('6. Was the fee removed?', [
 "No, it wasn't.",
 "No, it didn't.",
], 0),
  ],
  'notes': [
   "Click to circle each answer: 1 was added • 2 was received • 3 posted the payment • 4 by the phone company • 5 Yes, they are • 6 No, it wasn't",
   'Source: Level5_Lesson5.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('budget'),
  'alt': A('budget'),
  'sz': 14,
  'rows': [
   ('The fee was add on Tuesday.', '**The fee was added on Tuesday.**'),
   ('The company was posted the payment.', '**The payment was posted.**'),
   ('The credit was posted for the company.', '**The credit was posted by the company.**'),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson5.md (Grammar: Common mistakes).',
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
   'A says a line from the statement.',
  ],
  's2_label': 'B answers.',
  's2_body': [
   'B says it again with was or were and a participle.',
  ],
  'pic': I('deposit'),
  'alt': A('deposit'),
  'notes': [
   'A says a line from the statement. B says it again with was or were and a participle. Then switch. ---',
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson5.md (Step 4: Pair check).',
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
  'pic': I('fee'),
  'alt': A('fee'),
  'steps': [
   [
    'Pairs.',
   ],
   [
    'What was charged?',
   ],
   [
    'When was the payment received?',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson5.md (Step 5; Talk Time).',
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
  'pic': I('refund'),
  'alt': A('refund'),
  'steps': [
   [
    'Pairs.',
   ],
   [
    'Money in, two bills, and what is left.',
   ],
   [
    'The rent was paid.',
   ],
  ],
  'notes': [
   'Round 2.',
   'Source: Level5_Lesson5.md (Step 5; Talk Time).',
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
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ('When was the fee added?', 'On Tuesday'),
   ('When was the payment received?', 'On Friday'),
   ('How much was the fee?', '$6'),
   ('What does credit mean here?', 'Money back'),
   ('What is due today?', '$0'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   'Click to show each answer: 1 On Tuesday • 2 On Friday • 3 $6 • 4 Money back • 5 $0',
   'Source: Level5_Lesson5.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('due_date'),
  'alt': A('due_date'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'Explain one line from a statement.'),
   (1, 'Name: Date:'),
   (1, 'Use two passive sentences, and say one reason you would call the company.'),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, '1. Write two passive sentences about the practice statement.'),
   (1, '2. Finish the note and the three-line budget. This is writing check 2.'),
   (1, '3. Read one passive sentence to a friend.'),
   (1, '4. Review: I wish I had. Write one sentence from Lesson 3.'),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'Explain one line from a statement.',
   'Source: Level5_Lesson5.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   'I can say what is done with is or are and was or were plus a participle.',
   'I can add by when the doer matters.',
   'I can find the amount due, the due date, and one charge.',
  ],
  'bullet_sz': 18,
  'pic': I('account_number'),
  'alt': A('account_number'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson5.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Diego and Ms. Brooks', LEN),
]
