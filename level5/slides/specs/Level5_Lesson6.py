"""Level 5 Lesson 6 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 6 (AGENTS.md section 6)."""
from deckspec import *
N = 6
DECK_TITLE = 'Level 5 Lesson 6: She Told Me to Call'
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L6_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson6.md'
LEN = '1:41'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ['I can report a statement with said and told.', 'I can report a request with asked me to.', 'I can report a yes or no question with asked if.']
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
  'title': 'She Told Me to Call',
  'title_sz': 40,
  'bullets': [
   'I can report a statement with said and told.',
   'I can report a request with asked me to.',
   'I can report a yes or no question with asked if.',
  ],
  'bullet_sz': 20,
  'pic': I('message'),
  'alt': A('message'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   'This lesson is not medical advice.',
   'Source: Level5_Lesson6.md (Topic; At a glance: Objectives).',
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
   'I can report a statement with said and told.',
   'I can report a request with asked me to.',
   'I can report a yes or no question with asked if.',
   'I can write the message so another person can act on it.',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson6.md (At a glance: Objectives).',
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
   'Work with a partner. Say one',
   'passive line from last week. Then switch.',
  ],
  'box2': [
   'Homework check: read one budget line. Use',
   'invented numbers only.',
  ],
  'pic': I('note'),
  'alt': A('note'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson6.md (Step 1; Opening Talk page).',
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
   'Work with a partner. Say one passive line from',
   'last week. Then switch.',
  ],
  'rows': [
   'Say one line from the practice statement with was.',
   'What was added on Tuesday?',
   'What does credit mean on that page?',
   'Homework check: read one budget line. Use invented numbers only.',
  ],
  'notes': [
   'Each click shows the next card.',
   'A asks. B answers. Then switch.',
   'Source: Level5_Lesson6.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson6.md (Step 2; New Words page).',
   PCS,
  ],
 },
 {
  'kind': 'words',
  'title': 'More New Words',
  'instr': [
   'Partner game:',
   'Pass the word',
  ],
  'words': W[6:],
  'notes': [
   'A points to a picture. B names it and uses it in one sentence. Then switch.',
   'Source: Level5_Lesson6.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'What do you write a message on?',
    'pic': I('message'),
    'alt': A('message'),
    'a': 'a note',
    'q_sz': 16,
   },
   {
    'q': 'Where do you sit before the call?',
    'pic': I('waiting_room'),
    'alt': A('waiting_room'),
    'a': 'the waiting room',
    'q_sz': 16,
   },
   {
    'q': 'Who can you pass the message to?',
    'pic': I('family_member'),
    'alt': A('family_member'),
    'a': 'a family member',
    'q_sz': 16,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. a note',
   '2. the waiting room',
   '3. a family member',
   'Source: Level5_Lesson6.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'Jana calls the clinic.',
  'context_sz': 18,
  'pic': I('callback'),
  'alt': A('callback'),
  'voices': [
   'Jana',
   'Nurse Patel',
   'Ken',
  ],
  'listen': [
   'Listen. Did the checkup stay on the same day?',
   '| 6:12–6:32 | Listening.',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'Jana calls the clinic.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson6.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. Did the checkup stay on the same',
   'day?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 13,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. Yes. It stayed on the same day',
 'b. No. It moved to Thursday',
 'c. It was canceled',
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson6.md (Step 3; Listening Task A; Answer key).',
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening B',
  'instr': [
   'B. Listen again. Complete the message.',
  ],
  'instr_sz': 16,
  'ow': 2.45,
  'og': 0.05,
  'osz': 12,
  'sz': 13,
  'right': 13.1,
  'rows': [
   ('1. New day', [
 'Thursday',
 'Monday',
 'Friday',
], 0),
   ('2. Call before', [
 '3:00',
 '5:00',
 '9:00',
], 0),
   ('3. Bring', [
 'the appointment card',
 'a lunch',
 'a photo',
], 0),
   ('4. She tells the message to', [
 'Ken',
 'the nurse',
 'a teacher',
], 0),
   ('5. They will call if', [
 'the room changes',
 'the clinic closes',
 'the class is off',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 Thursday • 2 3:00 • 3 the appointment card • 4 Ken • 5 the room changes',
   'Source: Level5_Lesson6.md (Step 3; Listening Task B; Answer key).',
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
  'head2': 'Listen again. Write said, to',
  'sz': 16,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ('She ______ the checkup was on Thursday.', 'said'),
   ('She ______ me the time had changed.', 'told'),
   ('She ______ me to call before 3:00.', 'asked'),
   ('She ______ if Thursday was OK.', 'asked'),
   ('She ______ they would call me.', 'said'),
   ('She ______ me to bring the card.', 'asked'),
  ],
  'notes': [
   'Click to show each answer: 1 said • 2 told • 3 asked • 4 asked • 5 said • 6 asked',
   'Source: Level5_Lesson6.md (Step 3; Listening Task C; Answer key).',
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
   'I *want to* write the message down.',
   'I am *going to* call before 3:00.',
   'She told me to bring the card.',
   'She said they would call.',
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson6.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'said',
  ],
  'title_sz': 22,
  'qhead': 'DIRECT',
  'ahead': 'REPORTED',
  'pic': I('nurse'),
  'alt': A('nurse'),
  'lw': 4.6,
  'lsz': 13,
  'rsz': 14,
  'pitch_max': 1.05,
  'rows': [
   ('The nurse said, "The checkup is on Thursday."', 'She **said** the checkup **was** on Thursday.'),
   ('"We will call you."', 'She **said** they **would** call me.'),
   ('She said the time had changed.', 'said does not need a person'),
  ],
  'notes': [
   'Grammar Box 1: said. Each click shows the answer side.',
   'Source: Level5_Lesson6.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'told',
  ],
  'title_sz': 22,
  'qhead': 'SAY THIS',
  'ahead': 'NOTE',
  'pic': I('clinic'),
  'alt': A('clinic'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('She **told me** the time had changed.', 'tell needs a person'),
   ('She told me the checkup was on Thursday.', 'told me, not told to me'),
   ('She told Ken the new day.', 'a person after told'),
  ],
  'notes': [
   'Grammar Box 2: told. Each click shows the answer side.',
   'Source: Level5_Lesson6.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   'asked me to',
  ],
  'title_sz': 22,
  'qhead': 'REQUEST',
  'ahead': 'FORM',
  'pic': I('folder'),
  'alt': A('folder'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('She **asked me to** call before 3:00.', 'a request'),
   ('She **asked me to** bring the card.', 'asked me to + verb'),
   ('She asked me to write it in the folder.', 'a request'),
  ],
  'notes': [
   'Grammar Box 3: asked me to. Each click shows the answer side.',
   'Source: Level5_Lesson6.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   'asked if',
  ],
  'title_sz': 22,
  'qhead': 'QUESTION',
  'ahead': 'REPORTED',
  'pic': I('detail'),
  'alt': A('detail'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('She **asked if** Thursday was OK.', 'statement order'),
   ('She asked if I **could** come before 3:00.', 'can becomes could'),
   ('She asked if Ken was at home.', 'yes or no, then statement order'),
  ],
  'notes': [
   'Grammar Box 4: asked if. Each click shows the answer side.',
   'Source: Level5_Lesson6.md (Step 4; Grammar Box 4).',
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
   ('She ______ the checkup was on Thursday.', 'said'),
   ('She ______ me the time had changed.', 'told'),
   ('She ______ me to call before 3:00.', 'asked'),
   ('She ______ if Thursday was OK.', 'asked'),
   ('She said they ______ call me.', 'would'),
   ('She told ______ the new day.', 'me'),
  ],
  'notes': [
   'Click to show each answer: 1 said • 2 told • 3 asked • 4 asked • 5 would • 6 me',
   'Source: Level5_Lesson6.md (Step 4; Grammar Practice A; Answer key).',
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
   ('1. She', [
 'said the day had changed',
 'said me the day had changed',
], 0),
   ('2. She', [
 'told me the new time',
 'told to me the new time',
], 0),
   ('3. She', [
 'asked me to call',
 'asked that I call',
], 0),
   ('4. She asked', [
 'if Thursday was OK',
 'if was Thursday OK',
], 0),
   ('5. She said they', [
 'would call',
 'will call',
], 0),
   ('6. She asked if I', [
 'could come',
 'can come',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 said the day had changed • 2 told me the new time • 3 asked me to call • 4 if Thursday was OK • 5 would call • 6 could come',
   'Source: Level5_Lesson6.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('time_change'),
  'alt': A('time_change'),
  'sz': 14,
  'rows': [
   ('She said me the day.', '**She told me the day.**'),
   ('She told that the time had changed.', '**She said that the time had changed.**'),
   ('She asked me if I can come.', '**She asked if I could come.**'),
   ('She told to me.', '**She told me.**'),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson6.md (Grammar: Common mistakes).',
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
   'A reads one direct sentence.',
  ],
  's2_label': 'B answers.',
  's2_body': [
   'B reports it with said, told, or asked.',
  ],
  'pic': I('family_member'),
  'alt': A('family_member'),
  'notes': [
   'A reads one direct sentence. B reports it with said, told, or asked. Then switch. ---',
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson6.md (Step 4: Pair check).',
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
   'Groups of 3.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('clinic'),
  'alt': A('clinic'),
  'steps': [
   [
    'Groups of 3.',
   ],
   [
    'She said the checkup was on Thursday.',
   ],
   [
    'She asked me to call before 3:00.',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson6.md (Step 5; Talk Time).',
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
   'Groups of 3.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('detail'),
  'alt': A('detail'),
  'steps': [
   [
    'Groups of 3.',
   ],
   [
    'Who called?',
   ],
   [
    'What day is the checkup?',
   ],
  ],
  'notes': [
   'Round 2.',
   'Source: Level5_Lesson6.md (Step 5; Talk Time).',
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
   ('What day is the checkup?', 'Thursday'),
   ('What did the nurse ask Jana to do first?', 'Call before 3:00'),
   ('What should she bring?', 'The appointment card'),
   ('What did the nurse say about a later call?', 'They would call if the room changes'),
   ('Who is the message for?', 'Ken, a family member'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   'Click to show each answer: 1 Thursday • 2 Call before 3:00 • 3 The appointment card • 4 They would call if the room changes • 5 Ken, a family member',
   'Source: Level5_Lesson6.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('relay'),
  'alt': A('relay'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'Report one thing someone said in class tonight.'),
   (1, 'Name: Date:'),
   (1, 'Use said or told, and asked me to or asked if.'),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, '1. Report one sentence with said or told.'),
   (1, '2. Finish the message for a family member. Six to eight sentences.'),
   (1, '3. Read the message to a friend. They name the day and the task.'),
   (1, '4. Review: one passive line from Lesson 5.'),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'Report one thing someone said in class tonight.',
   'Source: Level5_Lesson6.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   'I can report a statement with said and told.',
   'I can report a request with asked me to.',
   'I can report a yes or no question with asked if.',
  ],
  'bullet_sz': 20,
  'pic': I('phone_log'),
  'alt': A('phone_log'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson6.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Jana, Nurse Patel, and Ken', LEN),
]
