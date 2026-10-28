"""Level 5 Lesson 1 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 1 (AGENTS.md section 6)."""
from deckspec import *
N = 1
DECK_TITLE = 'Level 5 Lesson 1: How Long Have You Been Working Here?'
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L1_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson1.md'
LEN = '1:37'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ['I can answer *How long have you been…?*', "I can also answer with *I've worked… for / since*", 'I can give one example of an accomplishment']
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
  'title': 'How Long Have You Been Working Here?',
  'title_sz': 28,
  'bullets': [
   'I can answer *How long have you been…?*',
   "I can also answer with *I've worked… for / since*",
   'I can give one example of an accomplishment',
  ],
  'bullet_sz': 20,
  'pic': I('resume'),
  'alt': A('resume'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   'Source: Level5_Lesson1.md (Topic; At a glance: Objectives).',
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
   'I can answer *How long have you been…?*',
   "I can also answer with *I've worked… for / since*",
   'I can give one example of an accomplishment',
   'I can ask a follow-up question',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson1.md (At a glance: Objectives).',
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
   'question. B answers in a short summary. A asks one follow-up. Then switch.',
  ],
  'box2': [
   'What have you been doing this week?',
  ],
  'pic': I('interview'),
  'alt': A('interview'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson1.md (Step 1; Opening Talk page).',
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
   'answers in a short summary. A asks one follow-up. Then switch.',
  ],
  'rows': [
   'How long have you lived in this city?',
   'How long have you studied English?',
   'Have you finished a class or a training?',
   'What have you been doing this week?',
  ],
  'notes': [
   'Each click shows the next card.',
   'A asks. B answers. Then switch.',
   'Source: Level5_Lesson1.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson1.md (Step 2; New Words page).',
   PCS,
  ],
 },
 {
  'kind': 'words',
  'title': 'More New Words',
  'instr': [
   'Partner game:',
   'Ask one question',
  ],
  'words': W[6:],
  'notes': [
   'A points to a picture. B names it and uses it in one sentence. Then switch.',
   'Source: Level5_Lesson1.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'Is a résumé a paper about your work?',
    'pic': I('resume'),
    'alt': A('resume'),
    'a': 'yes, a work paper',
    'q_sz': 16,
   },
   {
    'q': 'Is a handshake a follow-up?',
    'pic': I('handshake'),
    'alt': A('handshake'),
    'a': 'no',
    'q_sz': 16,
   },
   {
    'q': 'Does a name tag show a skill?',
    'pic': I('name_tag'),
    'alt': A('name_tag'),
    'a': 'no, it shows a name',
    'q_sz': 16,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. yes, a work paper',
   '2. no',
   '3. no, it shows a name',
   'Source: Level5_Lesson1.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'Nora is practicing for a hotel front-desk job.',
  'context_sz': 18,
  'pic': I('accomplishment'),
  'alt': A('accomplishment'),
  'voices': [
   'Samir',
   'Nora',
   'Ms. Hale',
  ],
  'listen': [
   'Listen. What job is the practice for?',
   '| 6:12–6:32 | Listening (play 1 = Task A; play 2 = Tasks B and C) +',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'Nora is practicing for a hotel front-desk job.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson1.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. What job is the practice for?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 15,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. a bakery job',
 'b. a hotel front-desk job',
 "c. a coach's job",
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson1.md (Step 3; Listening Task A; Answer key).',
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
   ('1. How long with customers?', [
 'three years',
 'two years',
 'since September',
], 0),
   ('2. Accomplishment?', [
 'trained two new cashiers',
 'finished the training',
 'sent a follow-up',
], 0),
   ('3. Example?', [
 'stayed for a week',
 'worked in 2022',
 'a handshake',
], 0),
   ('4. The job in 2022?', [
 'the hotel',
 'a bakery',
 'this class',
], 1),
  ],
  'notes': [
   'Click to circle each answer: 1 three years • 2 trained two new cashiers • 3 stayed for a week • 4 a bakery',
   'Source: Level5_Lesson1.md (Step 3; Listening Task B; Answer key).',
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
  'head2': 'Listen again. Write been wor',
  'sz': 16,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ("I've ______ with customers for three years.", 'been working'),
   ('I ______ at a bakery in 2022.', 'worked'),
   ('You said, "I\'ve ______."', 'been working'),
   ('I ______ at a bakery in 2022. That job is finished.', 'worked'),
  ],
  'notes': [
   'Click to show each answer: 1 been working • 2 worked • 3 been working • 4 worked',
   'Source: Level5_Lesson1.md (Step 3; Listening Task C; Answer key).',
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
   'I *want to* practice for a front-desk job.',
   'Ms. Hale is *going to* ask the questions.',
   "I've been working with customers.",
   'How long have you been working here?',
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson1.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'been + -ing (the',
  ],
  'title_sz': 20,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('example'),
  'alt': A('example'),
  'lw': 4.6,
  'lsz': 13,
  'rsz': 14,
  'pitch_max': 1.05,
  'rows': [
   ('How long **have** you **been working** here?', "I**'ve been working** here **for** two years."),
   ('How long **have** you **been working** at the hotel?', "I**'ve been working** there **for** two years."),
   ('How long **has** she **been taking** this class?', "She**'s been taking** this class **since** September."),
  ],
  'notes': [
   'Grammar Box 1: been + -ing (the activity, still going on). Each click shows the answer side.',
   'Source: Level5_Lesson1.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'have + past participle is',
  ],
  'title_sz': 20,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('skill'),
  'alt': A('skill'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('How long **have** you **worked** here?', "I**'ve worked** here **since** 2024."),
   ('How long **have** you **worked** there?', "I**'ve worked** there **for** two years."),
   ('**Have** you **finished** the training?', 'Yes, I **have**.'),
  ],
  'notes': [
   'Grammar Box 2: have + past participle is also correct for How long. Each click shows the answer side.',
   'Source: Level5_Lesson1.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   'a finished time needs the',
  ],
  'title_sz': 20,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('job_offer'),
  'alt': A('job_offer'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('What **did** you **do** in your last job?', 'I **helped** customers at a store.'),
   ('Where did you work **in 2022**?', 'I **worked** at a bakery **in 2022**.'),
  ],
  'notes': [
   'Grammar Box 3: a finished time needs the simple past. Each click shows the answer side.',
   'Source: Level5_Lesson1.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   'Which form?',
  ],
  'title_sz': 22,
  'qhead': 'FORM',
  'ahead': 'EXAMPLE',
  'pic': I('training'),
  'alt': A('training'),
  'lw': 4.6,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('*been* + *-ing*', "the activity, still going on: I've been working here for two years."),
   ('*have* + past participle', "also correct for *How long*: I've worked here since 2024."),
   ('simple past', 'a finished time (*in 2022*): I worked at a bakery in 2022.'),
  ],
  'notes': [
   'Grammar Box 4: Which form?. Each click shows the answer side.',
   'Source: Level5_Lesson1.md (Step 4; Grammar Box 4).',
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
   ("I've been ______ here for two years.", 'working'),
   ("I've worked here ______ 2024.", 'since'),
   ("I've worked here ______ two years.", 'for'),
   ('I ______ at a bakery in 2022.', 'worked'),
   ('Have you ______ the training?', 'finished'),
   ("She's been ______ this class since September.", 'taking'),
  ],
  'notes': [
   'Click to show each answer: 1 working • 2 since • 3 for • 4 worked • 5 finished • 6 taking',
   'Source: Level5_Lesson1.md (Step 4; Grammar Practice A; Answer key).',
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
   ('1. I ______ here since 2024.', [
 'am working',
 "'ve been working",
], 1),
   ('2. I ______ here in 2022.', [
 "'ve been working",
 'worked',
], 1),
   ('3. How long ______ at the hotel?', [
 'have you been working',
 'you have been working',
], 0),
   ("4. I've ______ there for two years.", [
 'been working',
 'working',
], 0),
   ("5. I've worked there ______ two years.", [
 'for',
 'since',
], 0),
   ("6. She's been taking this class ______ September.", [
 'since',
 'for',
], 0),
  ],
  'notes': [
   "Click to circle each answer: 1 've been working • 2 worked • 3 have you been working • 4 been working • 5 for • 6 since",
   'Source: Level5_Lesson1.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('portfolio'),
  'alt': A('portfolio'),
  'sz': 14,
  'rows': [
   ('I am working here since 2024.', "**I've been working here since 2024. or I've worked here since 2024.**"),
   ("I've been working here in 2022.", '**I worked here in 2022.**'),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson1.md (Grammar: Common mistakes).',
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
   'A says still true or finished in 2022.',
  ],
  's2_label': 'B answers.',
  's2_body': [
   "B makes one sentence (I've been working… or I worked…).",
  ],
  'pic': I('handshake'),
  'alt': A('handshake'),
  'notes': [
   "A says still true or finished in 2022. B makes one sentence (I've been working… or I worked…). Then switch. ---",
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson1.md (Step 4: Pair check).',
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
   'A is the interviewer.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('skill'),
  'alt': A('skill'),
  'steps': [
   [
    'A is the interviewer.',
   ],
   [
    'How long have you been working at your',
    'job?',
   ],
   [
    'How long have you been studying English?',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson1.md (Step 5; Talk Time).',
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
   'Kind Feedback.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('training'),
  'alt': A('training'),
  'steps': [
   [
    'Kind Feedback.',
   ],
   [
    'Kind Feedback.',
   ],
   [
    'Kind Feedback.',
   ],
  ],
  'notes': [
   'Round 2.',
   'Source: Level5_Lesson1.md (Step 5; Talk Time).',
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
   ('What job is the posting for?', 'Front desk at Harbor Hotel'),
   ('How long with customers?', 'For one year or more'),
   ('What example do they give?', 'Stayed for a week'),
   ('A finished job in 2022 uses…?', 'The simple past'),
   ('What does the coach send after?', 'A short follow-up note'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   'Click to show each answer: 1 Front desk at Harbor Hotel • 2 For one year or more • 3 Stayed for a week • 4 The simple past • 5 A short follow-up note',
   'Source: Level5_Lesson1.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('follow_up'),
  'alt': A('follow_up'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'How long have you been studying English (or doing your job)?'),
   (1, 'Name: Date:'),
   (1, '1.'),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, '1. Write the sentence. If the work is still true, been working or'),
   (1, '2. Finish your email from Read & Write. Read it one more time.'),
   (1, '3. Ask one person: How long have you been…? Write the answer in one'),
   (1, '4. Review (for or since).'),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'How long have you been studying English (or doing your job)?',
   'Source: Level5_Lesson1.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   'I can answer *How long have you been…?*',
   "I can also answer with *I've worked… for / since*",
   'I can give one example of an accomplishment',
  ],
  'bullet_sz': 20,
  'pic': I('qualification'),
  'alt': A('qualification'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson1.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Samir, Nora, and Ms. Hale', LEN),
]
