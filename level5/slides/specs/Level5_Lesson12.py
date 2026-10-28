"""Level 5 Lesson 12 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 12 (AGENTS.md section 6)."""
from deckspec import *
N = 12
DECK_TITLE = 'Level 5 Lesson 12: The Room Where We Meet'
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L12_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson12.md'
LEN = '2:17'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ['I can point to a thing with *which* and a place with *where*', 'I can still use *who* for a person', 'I can ask a question from the agenda']
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
  'title': 'The Room Where We Meet',
  'title_sz': 40,
  'bullets': [
   'I can point to a thing with *which* and a place with *where*',
   'I can still use *who* for a person',
   'I can ask a question from the agenda',
  ],
  'bullet_sz': 18,
  'pic': I('agenda'),
  'alt': A('agenda'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   'Source: Level5_Lesson12.md (Topic; At a glance: Objectives).',
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
   'I can point to a thing with *which* and a place with *where*',
   'I can still use *who* for a person',
   'I can ask a question from the agenda',
   'I can give an opinion with a reason and listen to one other opinion',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson12.md (At a glance: Objectives).',
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
  'pic': I('chairperson'),
  'alt': A('chairperson'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson12.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson12.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson12.md (Step 2; New Words page).',
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
   'Source: Level5_Lesson12.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'Is *which* for a thing or a place?',
    'pic': I('agenda'),
    'alt': A('agenda'),
    'a': 'A thing.',
    'q_sz': 16,
   },
   {
    'q': 'Is *where* for a thing or a place?',
    'pic': I('chairperson'),
    'alt': A('chairperson'),
    'a': 'A place.',
    'q_sz': 16,
   },
   {
    'q': 'Is *who* for a person?',
    'pic': I('minutes'),
    'alt': A('minutes'),
    'a': 'Yes.',
    'q_sz': 16,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. A thing.',
   '2. A place.',
   '3. Yes.',
   'Source: Level5_Lesson12.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'A short library meeting.',
  'context_sz': 18,
  'pic': I('minutes'),
  'alt': A('minutes'),
  'voices': [
   'Ms. Adeyemi',
   'Tom',
   'Grace',
  ],
  'listen': [
   'Listen. What are they deciding?',
   '- Play 1 → Task A.',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'A short library meeting.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson12.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. What are they deciding?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 15,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. A new library building',
 'b. Evening hours',
 'c. The price of a bus pass',
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson12.md (Step 3; Listening Task A; Answer key).',
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
   ('1. Tom wants', [
 'later hours',
 'the current hours',
 'a new bus',
], 0),
   ('2. Grace wants', [
 'later hours',
 'the current hours',
 'no meeting',
], 1),
   ("3. Grace's reason", [
 'the bus stops early',
 'the room is cold',
 'she wants a microphone',
], 0),
   ('4. The decision', [
 'close the library',
 'a one-month try',
 'move to the auditorium',
], 1),
   ('5. The try is on', [
 'Monday',
 'Thursday',
 'Sunday',
], 1),
   ('6. Open until', [
 'six',
 'seven',
 'eight',
], 2),
  ],
  'notes': [
   'Click to circle each answer: 1 later hours • 2 the current hours • 3 the bus stops early • 4 a one-month try • 5 Thursday • 6 eight',
   'Source: Level5_Lesson12.md (Step 3; Listening Task B; Answer key).',
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
  'head2': 'Listen again. Write which or',
  'sz': 14,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ('This is the room ______ we meet.', 'where'),
   ('The agenda, ______ is on your handout, lists the hours.', 'which'),
   ('The proposal ______ I read is on page 2.', 'which'),
   ('The library ______ we use closes at six.', 'which'),
   ('The stop ______ I catch the bus is dark after seven.', 'where'),
   ('This is the place ______ we should meet.', 'where'),
  ],
  'notes': [
   'Click to show each answer: 1 where • 2 which • 3 which • 4 which • 5 where • 6 where',
   'Source: Level5_Lesson12.md (Step 3; Listening Task C; Answer key).',
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
   'This is the room where we meet.',
   'The proposal which I read is on page 2.',
   "I'm *going to* come after work on Thursday.",
   'I *want to* keep the current hours.',
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson12.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'which for a thing',
  ],
  'title_sz': 22,
  'qhead': 'WHICH + THING',
  'ahead': 'NO EXTRA IT',
  'pic': I('microphone'),
  'alt': A('microphone'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('The proposal which the chair read', 'is on page 2.'),
   ('The library which we use', 'closes at six.'),
   ('The agenda which is on the handout', 'lists the hours.'),
  ],
  'notes': [
   'Grammar Box 1: which for a thing. Each click shows the answer side.',
   'Source: Level5_Lesson12.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'where for a place',
  ],
  'title_sz': 22,
  'qhead': 'WHERE REPLACES THE',
  'ahead': 'EXAMPLE',
  'pic': I('handout'),
  'alt': A('handout'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('This is the room where we meet.', 'Not: the room which we meet.'),
   ('The stop where I catch the bus', 'is dark after seven.'),
   ('The place where we should meet', 'is this library room.'),
  ],
  'notes': [
   'Grammar Box 2: where for a place. Each click shows the answer side.',
   'Source: Level5_Lesson12.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   'who for a person',
  ],
  'title_sz': 22,
  'qhead': 'WHO, NOT WHICH',
  'ahead': 'EXAMPLE',
  'pic': I('proposal'),
  'alt': A('proposal'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('The person who takes notes', 'is the secretary.'),
   ('The chairperson who keeps the order', 'is Ms. Adeyemi.'),
   ('The person who rides the bus', 'is Grace.'),
  ],
  'notes': [
   'Grammar Box 3: who for a person. Each click shows the answer side.',
   'Source: Level5_Lesson12.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   'an opinion and a reason',
  ],
  'title_sz': 20,
  'qhead': 'YOU CAN SAY',
  'ahead': 'EXAMPLE',
  'pic': I('sign_in'),
  'alt': A('sign_in'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('I think…', 'I think a one-month try is fair.'),
   ('I see your point, but…', 'I see your point, but I need a safe ride.'),
   ('Which or where', 'Which idea? Where would you say it?'),
  ],
  'notes': [
   'Grammar Box 4: an opinion and a reason. Each click shows the answer side.',
   'Source: Level5_Lesson12.md (Step 4; Grammar Box 4).',
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
   ('This is the room ______ we meet.', 'where'),
   ('The proposal ______ the chair read is on page 2.', 'which'),
   ('The person ______ takes notes is the secretary.', 'who'),
   ('The stop ______ I catch the bus is dark after seven.', 'where'),
   ('The library ______ we use closes at six.', 'which'),
   ('The chairperson ______ keeps the order is Ms. Adeyemi.', 'who'),
  ],
  'notes': [
   'Click to show each answer: 1 where • 2 which • 3 who • 4 where • 5 which • 6 who',
   'Source: Level5_Lesson12.md (Step 4; Grammar Practice A; Answer key).',
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
   ('1. This is the room ______ we meet.', [
 'which',
 'where',
], 1),
   ('2. The proposal ______ the chair read is on page 2.', [
 'which',
 'where',
], 0),
   ('3. The person ______ takes notes is the secretary.', [
 'which',
 'who',
], 1),
   ("4. Don't add ______ after *which the chair read*.", [
 'it',
 'which',
], 0),
   ('5. *Where* replaces ______ .', [
 'there',
 'it',
], 0),
   ('6. I see your point, ______ I need a safe ride.', [
 'but',
 'because',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 where • 2 which • 3 who • 4 it • 5 there • 6 but',
   'Source: Level5_Lesson12.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('name_tent'),
  'alt': A('name_tent'),
  'sz': 14,
  'rows': [
   ('The room which we meet.', 'The room **where** we meet.'),
   ('The proposal which the chair read it.', 'The proposal **which the chair read**.'),
   ('The person which takes notes.', 'The person **who** takes notes.'),
   ('The room where we meet there.', 'The room **where we meet**.'),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson12.md (Grammar: Common mistakes).',
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
   'A says "room," "proposal," or "person." B makes one sentence with where, which, or who.',
  ],
  's2_label': 'B answers.',
  's2_body': [
   'Then switch.',
  ],
  'pic': I('timer'),
  'alt': A('timer'),
  'notes': [
   'A says "room," "proposal," or "person." B makes one sentence with where, which, or who. Then switch. ---',
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson12.md (Step 4: Pair check).',
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
   'Groups of 4.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('handout'),
  'alt': A('handout'),
  'steps': [
   [
    'Groups of 4.',
   ],
   [
    'Groups of 4.',
   ],
   [
    'Groups of 4.',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson12.md (Step 5; Talk Time).',
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
   'The chair keeps the order.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('sign_in'),
  'alt': A('sign_in'),
  'steps': [
   [
    'The chair keeps the order.',
   ],
   [
    'The chair keeps the order.',
   ],
   [
    'The chair keeps the order.',
   ],
  ],
  'notes': [
   'Round 2.',
   'Source: Level5_Lesson12.md (Step 5; Talk Time).',
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
   ('What are they deciding?', 'Evening hours'),
   ('Who is the chairperson?', 'Ms. Adeyemi'),
   ('What does Tom want?', 'Later hours, until eight on Thursday'),
   ('Why does Grace want the current hours?', 'The bus stops early'),
   ('Where is the meeting?', 'In the room where we meet'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   'Click to show each answer: 1 Evening hours • 2 Ms. Adeyemi • 3 Later hours, until eight on Thursday • 4 The bus stops early • 5 In the room where we meet',
   'Source: Level5_Lesson12.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('question_card'),
  'alt': A('question_card'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'Which idea do you support, and where would you say it?'),
   (1, 'Name: Date:'),
   (1, 'Four sentences with which or where, a reason, and one polite phrase.'),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, '1. Write where.'),
   (1, '2. Finish your comment for the chair (Read & Write).'),
   (1, '3. Ask one which or where question at home. Write it.'),
   (1, '4. Review: write one sentence with who for a person.'),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'Which idea do you support, and where would you say it?',
   'Source: Level5_Lesson12.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   'I can point to a thing with *which* and a place with *where*',
   'I can still use *who* for a person',
   'I can ask a question from the agenda',
  ],
  'bullet_sz': 18,
  'pic': I('library'),
  'alt': A('library'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson12.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Ms. Adeyemi, Tom, and Grace', LEN),
]
