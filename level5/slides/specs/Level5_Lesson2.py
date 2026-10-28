"""Level 5 Lesson 2 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 2 (AGENTS.md section 6)."""
from deckspec import *
N = 2
DECK_TITLE = 'Level 5 Lesson 2: By the Time We Opened'
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L2_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson2.md'
LEN = '1:39'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ['I can say what had already happened', 'I can use *by the time* and *when* with two past times', 'I can put four events in order']
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
  'title': 'By the Time We Opened',
  'title_sz': 40,
  'bullets': [
   'I can say what had already happened',
   'I can use *by the time* and *when* with two past times',
   'I can put four events in order',
  ],
  'bullet_sz': 20,
  'pic': I('bakery'),
  'alt': A('bakery'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   'Source: Level5_Lesson2.md (Topic; At a glance: Objectives).',
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
   'I can say what had already happened',
   'I can use *by the time* and *when* with two past times',
   'I can put four events in order',
   'I can write a short project note',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson2.md (At a glance: Objectives).',
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
   'Work with a partner. A asks. B',
   'answers in a short summary. A asks one follow-up. Then switch.',
  ],
  'box2': [
   'Give one example from last week.',
  ],
  'pic': I('oven'),
  'alt': A('oven'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson2.md (Step 1; Opening Talk page).',
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
   'Work with a partner. A asks. B answers in a',
   'short summary. A asks one follow-up. Then switch.',
  ],
  'rows': [
   'How long have you been working, or studying English?',
   'What have you been practicing?',
   'Have you finished any training?',
   'Give one example from last week.',
  ],
  'notes': [
   'Each click shows the next card.',
   'A asks. B answers. Then switch.',
   'Source: Level5_Lesson2.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson2.md (Step 2; New Words page).',
   PCS,
  ],
 },
 {
  'kind': 'words',
  'title': 'More New Words',
  'instr': [
   'Partner game:',
   'Which one comes first?',
  ],
  'words': W[6:],
  'notes': [
   'A points to a picture. B names it and uses it in one sentence. Then switch.',
   'Source: Level5_Lesson2.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'Is the oven a person?',
    'pic': I('oven'),
    'alt': A('oven'),
    'a': 'no, it bakes',
    'q_sz': 16,
   },
   {
    'q': 'Who comes before opening day?',
    'pic': I('opening_day'),
    'alt': A('opening_day'),
    'a': 'the inspector',
    'q_sz': 16,
   },
   {
    'q': 'Is an awning a cover or a cake?',
    'pic': I('awning'),
    'alt': A('awning'),
    'a': 'a cover',
    'q_sz': 16,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. no, it bakes',
   '2. the inspector',
   '3. a cover',
   'Source: Level5_Lesson2.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'Priya and Ben work at a new bakery.',
  'context_sz': 18,
  'pic': I('permit'),
  'alt': A('permit'),
  'voices': [
   'Ms. Cole',
   'Priya',
   'Ben',
  ],
  'listen': [
   'Listen. Is the bakery open yet?',
   '| 6:12–6:32 | Listening (play 1 = Task A; play 2 = Tasks B and C) +',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'Priya and Ben work at a new bakery.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson2.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. Is the bakery open yet?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 15,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. Yes. It is open now',
 'b. No. It opens tomorrow',
 'c. No. It failed the visit',
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson2.md (Step 3; Listening Task A; Answer key).',
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening B',
  'instr': [
   'B. Listen again. What happened first,',
   'second, third, fourth, and last? Circle.',
  ],
  'instr_sz': 16,
  'ow': 2.45,
  'og': 0.05,
  'osz': 12,
  'sz': 13,
  'right': 13.1,
  'rows': [
   ('1. First', [
 'cleaned the kitchen',
 'the poster',
 'the inspector',
], 0),
   ('2. Second', [
 'the oven arrived',
 'opening day',
 'the ribbon',
], 0),
   ('3. Third', [
 'we painted',
 'we opened',
 'we failed',
], 0),
   ('4. Fourth', [
 'the poster went up',
 'the oven',
 'the permit',
], 0),
   ('5. Last', [
 'the inspector',
 'the oven',
 'the sign',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 cleaned the kitchen • 2 the oven arrived • 3 we painted • 4 the poster went up • 5 the inspector',
   'Source: Level5_Lesson2.md (Step 3; Listening Task B; Answer key).',
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
  'head2': 'Listen again. Write had or t',
  'sz': 16,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ('We ______ already painted the walls.', 'had'),
   ('You ______ last.', 'arrived'),
   ('Ben ______ already cleaned the kitchen.', 'had'),
   ('The poster ______ up.', 'went'),
   ('We ______ already picked up the permit.', 'had'),
   ('The oven ______ delivered.', 'was'),
  ],
  'notes': [
   'Click to show each answer: 1 had • 2 arrived • 3 had • 4 went • 5 had • 6 was',
   'Source: Level5_Lesson2.md (Step 3; Listening Task C; Answer key).',
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
  'say_sz': 16,
  'says': [
   'We *want to* open tomorrow.',
   'We are *going to* cut the ribbon.',
   'We had already painted the walls.',
   'By the time the inspector arrived, we had painted.',
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson2.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'by the time and when',
  ],
  'title_sz': 20,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('inspector'),
  'alt': A('inspector'),
  'lw': 4.6,
  'lsz': 13,
  'rsz': 14,
  'pitch_max': 1.05,
  'rows': [
   ('What had you done **by the time** the inspector arrived?', 'We **had already painted** the walls.'),
   ('What had Ben done **when** the oven was delivered?', 'Ben **had already cleaned** the kitchen.'),
   ('**Had** you **finished** the sign before the poster went up?', "**Yes, we had.** / **No, we hadn't.**"),
  ],
  'notes': [
   'Grammar Box 1: by the time and when. Each click shows the answer side.',
   'Source: Level5_Lesson2.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'earlier and later',
  ],
  'title_sz': 22,
  'qhead': 'EARLIER: HAD + PAS',
  'ahead': 'LATER: SIMPLE PAST',
  'pic': I('paint_roller'),
  'alt': A('paint_roller'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('we had already painted the walls', 'the inspector arrived'),
   ('Ben had already cleaned the kitchen', 'the oven was delivered'),
   ('we had finished the sign', 'the poster went up'),
  ],
  'notes': [
   'Grammar Box 2: earlier and later. Each click shows the answer side.',
   'Source: Level5_Lesson2.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   "the later moment's",
  ],
  'title_sz': 20,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('store_sign'),
  'alt': A('store_sign'),
  'lw': 4.6,
  'lsz': 13,
  'rsz': 14,
  'pitch_max': 1.05,
  'rows': [
   ('What was the painter doing when the inspector knocked?', 'The painter **was still working**.'),
  ],
  'notes': [
   "Grammar Box 3: the later moment's background. Each click shows the answer side.",
   'Source: Level5_Lesson2.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   'Which time?',
  ],
  'title_sz': 22,
  'qhead': 'FORM',
  'ahead': 'EXAMPLE',
  'pic': I('ribbon'),
  'alt': A('ribbon'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('earlier past', '*had* + past participle: we had already painted'),
   ('later past', 'simple past: the inspector arrived'),
   ('*by the time*', 'marks the later time: By the time the inspector arrived, …'),
  ],
  'notes': [
   'Grammar Box 4: Which time?. Each click shows the answer side.',
   'Source: Level5_Lesson2.md (Step 4; Grammar Box 4).',
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
   ('By the time the inspector arrived, we ______ already painted the walls.', 'had'),
   ('When the oven was delivered, Ben ______ already cleaned the kitchen.', 'had'),
   ('The inspector ______ after the painting.', 'arrived'),
   ('The poster ______ up after the sign.', 'went'),
   ('Had you finished the sign? Yes, we ______.', 'had'),
   ('The painter ______ still working when the inspector knocked.', 'was'),
  ],
  'notes': [
   'Click to show each answer: 1 had • 2 had • 3 arrived • 4 went • 5 had • 6 was',
   'Source: Level5_Lesson2.md (Step 4; Grammar Practice A; Answer key).',
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
   ('1. By the time the inspector ______ , we had already painted.', [
 'arrived',
 'had arrived',
], 0),
   ('2. We ______ the walls.', [
 'already painted',
 'had already painted',
], 1),
   ('3. By the time we ______ , the inspector had arrived.', [
 'had opened',
 'opened',
], 1),
   ('4. When the oven ______ , Ben had cleaned the kitchen.', [
 'was delivered',
 'had delivered',
], 0),
   ('5. Had you finished the sign?', [
 'Yes, we had.',
 'Yes, we did.',
], 0),
   ('6. The painter ______ when the inspector knocked.', [
 'was working',
 'had worked',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 arrived • 2 had already painted • 3 opened • 4 was delivered • 5 Yes, we had • 6 was working',
   'Source: Level5_Lesson2.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('opening_day'),
  'alt': A('opening_day'),
  'sz': 14,
  'rows': [
   ('When the inspector arrived, we already painted.', '**When the inspector arrived, we had already painted.**'),
   ('By the time we had opened, the inspector arrived.', '**By the time we opened, the inspector had arrived.**'),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson2.md (Grammar: Common mistakes).',
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
   'A says a later time: the inspector arrived.',
  ],
  's2_label': 'B answers.',
  's2_body': [
   'B says what had already happened: We had already painted the walls.',
  ],
  'pic': I('counter'),
  'alt': A('counter'),
  'notes': [
   'A says a later time: the inspector arrived. B says what had already happened: We had already painted the walls. Then switch. ---',
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson2.md (Step 4: Pair check).',
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
   'Four picture cards, shuffled.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('paint_roller'),
  'alt': A('paint_roller'),
  'steps': [
   [
    'Four picture cards, shuffled.',
   ],
   [
    'Four picture cards, shuffled.',
   ],
   [
    'Four picture cards, shuffled.',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson2.md (Step 5; Talk Time).',
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
   'Tell the other group.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('ribbon'),
  'alt': A('ribbon'),
  'steps': [
   [
    'Tell the other group.',
   ],
   [
    'Tell the other group.',
   ],
   [
    'Tell the other group.',
   ],
  ],
  'notes': [
   'Round 2.',
   'Source: Level5_Lesson2.md (Step 5; Talk Time).',
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
  'sz': 14,
  'aw': 2.8,
  'asz': 13,
  'rows': [
   ('Is the bakery open yet?', 'No. It opens tomorrow'),
   ('What had Ben done when the oven was delivered?', 'He had cleaned the kitchen'),
   ('What had they done by the time Ms. Cole arrived?', 'They had painted the walls'),
   ('Which went up first?', 'The store sign was first'),
   ('What did she need before she said yes?', 'The permit and dry paint'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   'Click to show each answer: 1 No. It opens tomorrow • 2 He had cleaned the kitchen • 3 They had painted the walls • 4 The store sign was first • 5 The permit and dry paint',
   'Source: Level5_Lesson2.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('display_case'),
  'alt': A('display_case'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'Tell one change, in order.'),
   (1, 'Name: Date:'),
   (1, '1.'),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, '1. Write the sentence.'),
   (1, '2. Finish your project note from Read & Write. This is writing check'),
   (1, '3. Tell the four-sentence story to a friend or a family member. Ask'),
   (1, "4. Review (Lesson 1). Write I've been working, I've worked, worked,"),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'Tell one change, in order.',
   'Source: Level5_Lesson2.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   'I can say what had already happened',
   'I can use *by the time* and *when* with two past times',
   'I can put four events in order',
  ],
  'bullet_sz': 20,
  'pic': I('awning'),
  'alt': A('awning'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson2.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Ms. Cole, Priya, and Ben', LEN),
]
