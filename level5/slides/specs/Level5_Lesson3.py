"""Level 5 Lesson 3 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 3 (AGENTS.md section 6)."""
from deckspec import *
N = 3
DECK_TITLE = 'Level 5 Lesson 3: I Wish I Had Asked'
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L3_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson3.md'
LEN = '2:10'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ['I can say I wish I had… for a past regret.', 'I can say I wish I knew… for something I want now.', 'I can say one If I had…, I would have… sentence.']
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
  'title': 'I Wish I Had Asked',
  'title_sz': 40,
  'bullets': [
   'I can say I wish I had… for a past regret.',
   'I can say I wish I knew… for something I want now.',
   'I can say one If I had…, I would have… sentence.',
  ],
  'bullet_sz': 20,
  'pic': I('wish'),
  'alt': A('wish'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   'Source: Level5_Lesson3.md (Topic; At a glance: Objectives).',
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
   'I can say I wish I had… for a past regret.',
   'I can say I wish I knew… for something I want now.',
   'I can say one If I had…, I would have… sentence.',
   'I can say what I will do next time.',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson3.md (At a glance: Objectives).',
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
   'Work with a partner. Ask about',
   'last week. Then switch.',
  ],
  'box2': [
   'Homework check: read one sentence from',
   'your Lesson 2 note.',
  ],
  'pic': I('regret'),
  'alt': A('regret'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson3.md (Step 1; Opening Talk page).',
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
   'Work with a partner. Ask about last week. Then',
   'switch.',
  ],
  'rows': [
   'What had you already finished before class?',
   'Say one earlier event with had.',
   'Say the later event with by the time.',
   'Homework check: read one sentence from your Lesson 2 note.',
  ],
  'notes': [
   'Each click shows the next card.',
   'A asks. B answers. Then switch.',
   'Source: Level5_Lesson3.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson3.md (Step 2; New Words page).',
   PCS,
  ],
 },
 {
  'kind': 'words',
  'title': 'More New Words',
  'instr': [
   'Partner game:',
   'Point and wish',
  ],
  'words': W[6:],
  'notes': [
   'A points to a picture. B names it and uses it in one sentence. Then switch.',
   'Source: Level5_Lesson3.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'Is a calendar a list of dates?',
    'pic': I('calendar'),
    'alt': A('calendar'),
    'a': 'yes',
    'q_sz': 16,
   },
   {
    'q': 'What can wake you up?',
    'pic': I('alarm'),
    'alt': A('alarm'),
    'a': 'an alarm',
    'q_sz': 16,
   },
   {
    'q': 'Where can you ask for help?',
    'pic': I('help_desk'),
    'alt': A('help_desk'),
    'a': 'the help desk',
    'q_sz': 16,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. yes',
   '2. an alarm',
   '3. the help desk',
   'Source: Level5_Lesson3.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'After class, Alicia and Chris talk about a workshop they signed up for late.',
  'context_sz': 18,
  'pic': I('calendar'),
  'alt': A('calendar'),
  'voices': [
   'Narrator',
   'Alicia',
   'Chris',
  ],
  'listen': [
   'Listen. What do they regret?',
   '| 6:12–6:32 | Listening.',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'After class, Alicia and Chris talk about a workshop they signed up for late.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson3.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. What do they regret?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 13,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. They lost a book',
 'b. They signed up for the workshop late',
 'c. They want to leave the class',
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson3.md (Step 3; Listening Task A; Answer key).',
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
   ("1. Alicia's wish", [
 'asked the tutor',
 'left the class',
 'skipped practice',
], 0),
   ("2. Chris's wish", [
 'set an alarm',
 'changed jobs',
 'missed the class',
], 0),
   ('3. Next time Alicia will', [
 'ask on the first day',
 'wait a year',
 'stay quiet',
], 0),
   ('4. The if sentence uses', [
 'would have known',
 'will know',
 'knew',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 asked the tutor • 2 set an alarm • 3 ask on the first day • 4 would have known',
   'Source: Level5_Lesson3.md (Step 3; Listening Task B; Answer key).',
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
  'head2': 'Listen again. Write wish I h',
  'sz': 16,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ('Alicia: "I ______ asked the tutor."', 'wish I had'),
   ('"If I had asked, I ______ known the date."', 'would have'),
   ('Chris: "I ______ set an alarm."', 'wish I had'),
   ('"If I had set one, I ______ arrived on time."', 'would have'),
   ('Alicia: "Then I ______ known."', 'would have'),
   ('Chris: "I ______ put a reminder on the calendar."', 'wish I had'),
  ],
  'notes': [
   'Click to show each answer: 1 wish I had • 2 would have • 3 wish I had • 4 would have • 5 would have • 6 wish I had',
   'Source: Level5_Lesson3.md (Step 3; Listening Task C; Answer key).',
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
   'I *want to* ask the tutor.',
   'I am *going to* sign up on the first day.',
   'I wish I had asked.',
   'If I had asked, I would have known.',
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson3.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'a wish about now',
  ],
  'title_sz': 22,
  'qhead': 'WISH',
  'ahead': 'MEANING',
  'pic': I('reminder'),
  'alt': A('reminder'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('I wish I **knew** the deadline.', 'a wish about now'),
   ('I wish I **had** a reminder.', 'had means owned'),
   ('I wish I **were** on the list.', 'were, for now'),
  ],
  'notes': [
   'Grammar Box 1: a wish about now. Each click shows the answer side.',
   'Source: Level5_Lesson3.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'a wish about the past',
  ],
  'title_sz': 20,
  'qhead': 'WISH',
  'ahead': 'MEANING',
  'pic': I('alarm'),
  'alt': A('alarm'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('I wish I **had asked** the tutor.', 'a past regret'),
   ('I wish I **had set** an alarm.', 'had + participle'),
   ('I wish we **had signed** up on Monday.', 'the sign-up is finished'),
  ],
  'notes': [
   'Grammar Box 2: a wish about the past. Each click shows the answer side.',
   'Source: Level5_Lesson3.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   'one different past',
  ],
  'title_sz': 22,
  'qhead': 'IF',
  'ahead': 'RESULT',
  'pic': I('signup'),
  'alt': A('signup'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('If I **had asked**, I **would have known**.', 'one pattern'),
   ('If he **had set** an alarm, he **would have arrived** on time.', 'same pattern'),
   ('If we **had read** the reminder, we **would have signed** up.', 'same pattern'),
  ],
  'notes': [
   'Grammar Box 3: one different past. Each click shows the answer side.',
   'Source: Level5_Lesson3.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   'should have, and next time',
  ],
  'title_sz': 20,
  'qhead': 'NOW',
  'ahead': 'NEXT',
  'pic': I('tutor'),
  'alt': A('tutor'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('I **should have asked** earlier.', 'same idea as the wish'),
   ('Next time I **will ask** on the first day.', 'a plan'),
   ('If I **had** another chance, I **would ask**.', 'next time'),
  ],
  'notes': [
   'Grammar Box 4: should have, and next time. Each click shows the answer side.',
   'Source: Level5_Lesson3.md (Step 4; Grammar Box 4).',
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
   ('I wish I ______ the deadline.', 'knew'),
   ('I wish I ______ asked the tutor.', 'had'),
   ('If I had asked, I ______ have known.', 'would'),
   ('I ______ have asked earlier.', 'should'),
   ('Next time I ______ ask on the first day.', 'will'),
   ('I wish I ______ a reminder.', 'had'),
  ],
  'notes': [
   'Click to show each answer: 1 knew • 2 had • 3 would • 4 should • 5 will • 6 had',
   'Source: Level5_Lesson3.md (Step 4; Grammar Practice A; Answer key).',
  ],
 },
 {
  'kind': 'choice',
  'title': 'Practice B',
  'instr': [
   'Circle the correct words.',
  ],
  'ow': 2.15,
  'og': 0.12,
  'osz': 16,
  'sz': 15,
  'right': 12.7,
  'rows': [
   ('1. I wish I', [
 'knew',
 'know',
], 0),
   ('2. I wish I', [
 'had asked',
 'would have asked',
], 0),
   ('3. If I', [
 'had asked',
 'would have asked',
], 0),
   ('4. I', [
 'should have asked',
 'should asked',
], 0),
   ('5. Next time I', [
 'will ask',
 'would have ask',
], 0),
   ('6. If I had another chance, I', [
 'would ask',
 'would have asked',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 knew • 2 had asked • 3 had asked • 4 should have asked • 5 will ask • 6 would ask',
   'Source: Level5_Lesson3.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('practice'),
  'alt': A('practice'),
  'sz': 14,
  'rows': [
   ('I wish I would have asked.', '**I wish I had asked.**'),
   ('If I would have asked, I would have known.', '**If I had asked, I would have known.**'),
   ('I wish I know the deadline.', '**I wish I knew the deadline.**'),
   ('I should asked earlier.', '**I should have asked earlier.**'),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson3.md (Grammar: Common mistakes).',
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
   'A says a mild regret from class.',
  ],
  's2_label': 'B answers.',
  's2_body': [
   'B says I wish I had… and Next time I will….',
  ],
  'pic': I('question'),
  'alt': A('question'),
  'notes': [
   'A says a mild regret from class. B says I wish I had… and Next time I will…. Then switch. ---',
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson3.md (Step 4: Pair check).',
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
  'pic': I('alarm'),
  'alt': A('alarm'),
  'steps': [
   [
    'Pairs.',
   ],
   [
    'I missed the sign-up.',
   ],
   [
    'I did not ask for the example.',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson3.md (Step 5; Talk Time).',
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
  'pic': I('tutor'),
  'alt': A('tutor'),
  'steps': [
   [
    'Pairs.',
   ],
   [
    'Say If I had…, I would have….',
   ],
   [
    'The group repeats the clearest sentence.',
   ],
  ],
  'notes': [
   'Round 2.',
   'Source: Level5_Lesson3.md (Step 5; Talk Time).',
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
   ('What did the learner miss?', 'The workshop sign-up'),
   ('Which wish is about now?', 'I wish I knew the deadline'),
   ('Which wish is about the past?', 'I wish I had asked the tutor'),
   ('What is the if sentence?', 'If I had asked, I would have known'),
   ('What will the learner do next time?', 'Ask on the first day'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   'Click to show each answer: 1 The workshop sign-up • 2 I wish I knew the deadline • 3 I wish I had asked the tutor • 4 If I had asked, I would have known • 5 Ask on the first day',
   'Source: Level5_Lesson3.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('choice'),
  'alt': A('choice'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'Write about one mild regret.'),
   (1, 'Name: Date:'),
   (1, 'The wish, the if sentence, what you should have done, and the next step.'),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, '1. Write I wish I knew and one past wish.'),
   (1, '2. Finish the six-sentence note from Read & Write.'),
   (1, '3. Tell a friend one next step. Write the sentence.'),
   (1, '4. Review: had already. Write one sentence from Lesson 2.'),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'Write about one mild regret.',
   'Source: Level5_Lesson3.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   'I can say I wish I had… for a past regret.',
   'I can say I wish I knew… for something I want now.',
   'I can say one If I had…, I would have… sentence.',
  ],
  'bullet_sz': 20,
  'pic': I('help_desk'),
  'alt': A('help_desk'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson3.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Alicia and Chris', LEN),
]
