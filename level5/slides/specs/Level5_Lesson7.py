"""Level 5 Lesson 7 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 7 (AGENTS.md section 6)."""
from deckspec import *
N = 7
DECK_TITLE = "Level 5 Lesson 7: You Sent It, Didn't You?"
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L7_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson7.md'
LEN = '1:30'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ['I can add a tag to a statement I think is true.', 'I can answer a tag with a short yes or no.', 'I can correct a wrong detail politely.']
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
  'title': "You Sent It, Didn't You?",
  'title_sz': 40,
  'bullets': [
   'I can add a tag to a statement I think is true.',
   'I can answer a tag with a short yes or no.',
   'I can correct a wrong detail politely.',
  ],
  'bullet_sz': 20,
  'pic': I('spelling'),
  'alt': A('spelling'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   'Do not collect real Social Security numbers, immigration papers, bank numbers, or medical record numbers.',
   'Source: Level5_Lesson7.md (Topic; At a glance: Objectives).',
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
   'I can add a tag to a statement I think is true.',
   'I can answer a tag with a short yes or no.',
   'I can correct a wrong detail politely.',
   'I can write a confirmation email.',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson7.md (At a glance: Objectives).',
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
   'Work with a partner. A asks last',
   "week's question. B answers with a short summary. Then compare one homework sentence.",
  ],
  'box2': [
   'Homework check: read one sentence from',
   'your Lesson 6 message.',
  ],
  'pic': I('email_address'),
  'alt': A('email_address'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson7.md (Step 1; Opening Talk page).',
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
   "Work with a partner. A asks last week's",
   'question. B answers with a short summary. Then compare one homework sentence.',
  ],
  'rows': [
   'What did the person say? Use said or told.',
   'What did the person ask you to do? Use asked me to.',
   'What yes/no question did the person ask? Use asked if.',
   'Homework check: read one sentence from your Lesson 6 message.',
  ],
  'notes': [
   'Each click shows the next card.',
   'A asks. B answers. Then switch.',
   'Source: Level5_Lesson7.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson7.md (Step 2; New Words page).',
   PCS,
  ],
 },
 {
  'kind': 'words',
  'title': 'More New Words',
  'instr': [
   'Partner game:',
   'Check the form',
  ],
  'words': W[6:],
  'notes': [
   'A points to a picture. B names it and uses it in one sentence. Then switch.',
   'Source: Level5_Lesson7.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'Is this a phone number or an email address?',
    'pic': I('email_address'),
    'alt': A('email_address'),
    'a': 'an email address',
    'q_sz': 14,
   },
   {
    'q': 'What small box do you mark on a form?',
    'pic': I('checkbox'),
    'alt': A('checkbox'),
    'a': 'a checkbox',
    'q_sz': 16,
   },
   {
    'q': 'Is the L in Leah small or capital?',
    'pic': I('spelling'),
    'alt': A('spelling'),
    'a': 'capital',
    'q_sz': 16,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. an email address',
   '2. a checkbox',
   '3. capital',
   'Source: Level5_Lesson7.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'Leah is at a community center desk.',
  'context_sz': 18,
  'pic': I('phone_number'),
  'alt': A('phone_number'),
  'voices': [
   'Narrator',
   'Mr. Ortiz',
   'Leah',
  ],
  'listen': [
   'Listen. Is every detail correct at the start?',
   '| 6:12–6:32 | Listening: play 1 (Task A), play 2 (Tasks B and C) +',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'Leah is at a community center desk.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson7.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. Is every detail correct at the',
   'start?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 15,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. Yes. Every detail is correct',
 'b. No. The room is wrong',
 'c. She did not send the form',
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson7.md (Step 3; Listening Task A; Answer key).',
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening B',
  'instr': [
   'B. Listen again. Mark each detail',
   'correct or wrong.',
  ],
  'instr_sz': 16,
  'ow': 1.8,
  'og': 0.12,
  'osz': 16,
  'sz': 15,
  'right': 12.7,
  'rows': [
   ('1. Class ID C-42', [
 'Correct',
 'Wrong',
], 0),
   ('2. Email leah@mail.example', [
 'Correct',
 'Wrong',
], 0),
   ('3. Day: Tuesday', [
 'Correct',
 'Wrong',
], 0),
   ('4. Time: 6:00', [
 'Correct',
 'Wrong',
], 0),
   ('5. Room on his copy: A', [
 'Correct',
 'Wrong',
], 1),
  ],
  'notes': [
   'Click to circle each answer: 1 Correct • 2 Correct • 3 Correct • 4 Correct • 5 Wrong. C forty-two is class ID C-42. Tuesday at six is 6:00. The room on his copy is A; the schedule says room C',
   'Source: Level5_Lesson7.md (Step 3; Listening Task B; Answer key).',
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
  'head2': 'Listen again. Write the tag.',
  'sz': 14,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ('You sent the form, ______?', "didn't you"),
   ('Your class ID is C forty-two, ______?', "isn't it"),
   ('The email address is leah at mail dot example, ______?', "isn't it"),
   ('You wrote a phone number on line three, ______?', "didn't you"),
   ('The class is on Tuesday at six, ______?', "isn't it"),
   ("Your friend isn't in this class, ______?", 'is she'),
  ],
  'notes': [
   "Click to show each answer: 1 didn't you • 2 isn't it • 3 isn't it • 4 didn't you • 5 isn't it • 6 is she",
   'Source: Level5_Lesson7.md (Step 3; Listening Task C; Answer key).',
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
   'I *want to* double-check every line.',
   "I'm *going to* come straight from work.",
   "You sent the form, didn't you?",
   "Actually, it isn't.",
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson7.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'a negative tag',
  ],
  'title_sz': 22,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('schedule'),
  'alt': A('schedule'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ("You sent the form, **didn't you?**", '**Yes, I did.**'),
   ("The class is on Tuesday, **isn't it?**", '**Yes, it is.**'),
   ("She signed the copy, **didn't she?**", '**Yes, she did.**'),
  ],
  'notes': [
   'Grammar Box 1: a negative tag. Each click shows the answer side.',
   'Source: Level5_Lesson7.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'a positive tag',
  ],
  'title_sz': 22,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('signature'),
  'alt': A('signature'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ("She **isn't** on the list, **is she?**", "**No, she isn't.**"),
   ("The room **isn't** A, **is it?**", "**No, it isn't.**"),
   ("You **didn't** initial it, **did you?**", '**Actually, I did.**'),
  ],
  'notes': [
   'Grammar Box 2: a positive tag. Each click shows the answer side.',
   'Source: Level5_Lesson7.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   'do, does, or did',
  ],
  'title_sz': 22,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('form'),
  'alt': A('form'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ("You need a copy, **don't you?**", '**Yes, I do.**'),
   ("The schedule starts at six, **doesn't it?**", '**Yes, it does.**'),
   ("Leah checked the spelling, **didn't she?**", '**Yes, she did.**'),
  ],
  'notes': [
   'Grammar Box 3: do, does, or did. Each click shows the answer side.',
   'Source: Level5_Lesson7.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   'correct a detail',
  ],
  'title_sz': 22,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('checkbox'),
  'alt': A('checkbox'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ("The room is A, **isn't it?**", "**Actually, it's room C.**"),
   ("The class is on Wednesday, **isn't it?**", "**Actually, it's on Tuesday.**"),
   ("Your email ends in mail.example, **doesn't it?**", '**Yes, it does.**'),
  ],
  'notes': [
   'Grammar Box 4: correct a detail. Each click shows the answer side.',
   'Source: Level5_Lesson7.md (Step 4; Grammar Box 4).',
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
   ('You sent the form, ______?', "didn't you"),
   ('The class is on Tuesday, ______?', "isn't it"),
   ("She isn't on the list, ______?", 'is she'),
   ('You need a copy, ______?', "don't you"),
   ('The schedule starts at six, ______?', "doesn't it"),
   ('Leah checked the spelling, ______?', "didn't she"),
  ],
  'notes': [
   "Click to show each answer: 1 didn't you • 2 isn't it • 3 is she • 4 don't you • 5 doesn't it • 6 didn't she",
   'Source: Level5_Lesson7.md (Step 4; Grammar Practice A; Answer key).',
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
   ("1. You sent it, didn't you?", [
 'Yes, I did.',
 "Yes, I didn't.",
], 0),
   ('2. The room is A, ______?', [
 "isn't it",
 'is it',
], 0),
   ("3. She isn't on the list, ______?", [
 "isn't she",
 'is she',
], 1),
   ('4. You checked the spelling, ______?', [
 "didn't you",
 'did you',
], 0),
   ('5. The class ID is C forty-two, ______?', [
 "isn't it",
 'is it',
], 0),
   ("6. You didn't sign it, did you?", [
 "No, I didn't.",
 "Yes, I didn't.",
], 0),
  ],
  'notes': [
   "Click to circle each answer: 1 Yes, I did • 2 isn't it • 3 is she • 4 didn't you • 5 isn't it • 6 No, I didn't",
   'Source: Level5_Lesson7.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('correction'),
  'alt': A('correction'),
  'sz': 14,
  'rows': [
   ("Yes, I didn't.", '**Yes, I did.**'),
   ('You sent it, did you?', "You sent it, **didn't you?**"),
   ("The class is on Tuesday, doesn't it?", "The class is on Tuesday, **isn't it?**"),
   ("She isn't on the list, isn't she?", "She isn't on the list, **is she?**"),
   ("You need a copy, doesn't you?", "You need a copy, **don't you?**"),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson7.md (Grammar: Common mistakes).',
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
   "Model: It's Tuesday, isn't it?",
  ],
  's2_label': 'B answers.',
  's2_body': [
   '| Detail | Copy A | Copy B | |---|---|---| | Day | Tuesday | Wednesday | | Time | 6:00 |',
  ],
  'pic': I('double_check'),
  'alt': A('double_check'),
  'notes': [
   "Model: It's Tuesday, isn't it? Actually, it's Wednesday. | Detail | Copy A | Copy B | |---|---|---| | Day | Tuesday | Wednesday | | Time | 6:00 | 6:00 | | Room | C | C | | Email | leah@mail.example | leah@mail.example |",
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson7.md (Step 4: Pair check).',
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
   'A has four details.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('signature'),
  'alt': A('signature'),
  'steps': [
   [
    'A has four details.',
   ],
   [
    'A has four details.',
   ],
   [
    'A has four details.',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson7.md (Step 5; Talk Time).',
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
   'B says two sentences.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('checkbox'),
  'alt': A('checkbox'),
  'steps': [
   [
    'B says two sentences.',
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
   'Source: Level5_Lesson7.md (Step 5; Talk Time).',
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
  'aw': 2.3,
  'asz': 14,
  'rows': [
   ("What is Leah's class ID?", 'C-42'),
   ('What day and time is the class?', 'Tuesday at 6:00'),
   ('What room is on the form?', 'Room C'),
   ('What room is in the email?', 'Room A'),
   ('What is the mismatch?', 'The room'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   'Click to show each answer: 1 C-42 • 2 Tuesday at 6:00 • 3 Room C • 4 Room A • 5 The room',
   'Source: Level5_Lesson7.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('copy'),
  'alt': A('copy'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'Confirm two details about this class.'),
   (1, 'Name: Date:'),
   (1, 'Two of them are tags.'),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, '1. Add the tag.'),
   (1, '2. Finish your confirmation email (Read & Write C). Read it one more'),
   (1, '3. Confirm two details with a friend or a family member. Use a tag.'),
   (1, '4. Review (said / told). Report one sentence from Lesson 6. Use said'),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'Confirm two details about this class.',
   'Source: Level5_Lesson7.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   'I can add a tag to a statement I think is true.',
   'I can answer a tag with a short yes or no.',
   'I can correct a wrong detail politely.',
  ],
  'bullet_sz': 20,
  'pic': I('initial'),
  'alt': A('initial'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson7.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Mr. Ortiz and Leah', LEN),
]
