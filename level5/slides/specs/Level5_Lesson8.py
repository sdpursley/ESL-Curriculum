"""Level 5 Lesson 8 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 8 (AGENTS.md section 6)."""
from deckspec import *
N = 8
DECK_TITLE = "Level 5 Lesson 8: Do You Know If It's Tonight?"
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L8_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson8.md'
LEN = '2:20'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ['I can ask *Do you know if / whether…?*', 'I can keep statement order after *if*.', 'I can ask *Do you know when / where…?* the Level 4 way.']
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
  'title': "Do You Know If It's Tonight?",
  'title_sz': 34,
  'bullets': [
   'I can ask *Do you know if / whether…?*',
   'I can keep statement order after *if*.',
   'I can ask *Do you know when / where…?* the Level 4 way.',
  ],
  'bullet_sz': 18,
  'pic': I('school_office'),
  'alt': A('school_office'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   'Source: Level5_Lesson8.md (Topic; At a glance: Objectives).',
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
   'I can ask *Do you know if / whether…?*',
   'I can keep statement order after *if*.',
   'I can ask *Do you know when / where…?* the Level 4 way.',
   'I can report the answer with *said* or *told*.',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson8.md (At a glance: Objectives).',
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
   'Work with a partner. A asks a tag',
   'from last week. B answers with a short yes, a short no, or Actually. Then compare one homework sentence.',
  ],
  'box2': [
   'Homework check: read one sentence from',
   'your confirmation email.',
  ],
  'pic': I('counselor'),
  'alt': A('counselor'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson8.md (Step 1; Opening Talk page).',
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
   'Work with a partner. A asks a tag from last',
   'week. B answers with a short yes, a short no, or Actually. Then compare one homework sentence.',
  ],
  'rows': [
   'Add a tag: The class is on Tuesday, .',
   "Answer a tag: Yes, it is. / No, it isn't.",
   'Correct one detail: Actually, ...',
   'Homework check: read one sentence from your confirmation email.',
  ],
  'notes': [
   'Each click shows the next card.',
   'A asks. B answers. Then switch.',
   'Source: Level5_Lesson8.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson8.md (Step 2; New Words page).',
   PCS,
  ],
 },
 {
  'kind': 'words',
  'title': 'More New Words',
  'instr': [
   'Partner game:',
   'Point and ask',
  ],
  'words': W[6:],
  'notes': [
   'A points to a picture. B names it and uses it in one sentence. Then switch.',
   'Source: Level5_Lesson8.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'What do you carry books in?',
    'pic': I('backpack'),
    'alt': A('backpack'),
    'a': 'a backpack',
    'q_sz': 16,
   },
   {
    'q': 'What rings in the hallway?',
    'pic': I('hallway'),
    'alt': A('hallway'),
    'a': 'a bell',
    'q_sz': 16,
   },
   {
    'q': 'What paper does a parent bring for early pickup?',
    'pic': I('permission_slip'),
    'alt': A('permission_slip'),
    'a': 'a permission slip',
    'q_sz': 14,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. a backpack',
   '2. a bell',
   '3. a permission slip',
   'Source: Level5_Lesson8.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'Maya calls the office at Northside School.',
  'context_sz': 18,
  'pic': I('conference'),
  'alt': A('conference'),
  'voices': [
   'Narrator',
   'Mr. Reed',
   'Maya',
  ],
  'listen': [
   'Listen. Why is she calling?',
   '| 6:12–6:32 | Listening: play 1 (Task A), play 2 (Tasks B and C) +',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'Maya calls the office at Northside School.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson8.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. Why is she calling?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 15,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. to ask about the bus',
 'b. to ask about the conference',
 'c. to join the office staff',
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson8.md (Step 3; Listening Task A; Answer key).',
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening B',
  'instr': [
   'B. Listen again. Circle the note.',
  ],
  'instr_sz': 16,
  'ow': 2.45,
  'og': 0.05,
  'osz': 12,
  'sz': 13,
  'right': 13.1,
  'rows': [
   ('1. Day', [
 'tonight',
 'tomorrow',
 'Monday',
], 0),
   ('2. Starts', [
 '6:00',
 '6:30',
 '7:00',
], 1),
   ('3. Bring', [
 'the slip',
 'the signup sheet',
 'the newsletter',
], 1),
   ('4. Arrive', [
 'on time',
 'ten minutes early',
 'after three',
], 1),
   ('5. The window is', [
 'in the library',
 'down the hallway',
 'in the parking lot',
], 1),
   ('6. A slip for Maya', [
 'yes',
 'no',
], 1),
  ],
  'notes': [
   'Click to circle each answer: 1 tonight • 2 6:30 • 3 the signup sheet • 4 ten minutes early • 5 down the hallway • 6 no. Six thirty in the script is 6:30',
   'Source: Level5_Lesson8.md (Step 3; Listening Task B; Answer key).',
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
  'head2': 'Listen again. Write if, whet',
  'sz': 16,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ('Do you know ______ the conference is tonight?', 'if'),
   ('Do you know ______ I should bring the signup sheet?', 'whether'),
   ('Do you know ______ the office window is?', 'where'),
   ('Can you tell me ______ I need a permission slip?', 'if'),
   ('Do you know ______ dismissal is at the usual time?', 'if'),
   ('Do you know ______ I should leave my backpack?', 'where'),
  ],
  'notes': [
   'Click to show each answer: 1 if • 2 whether • 3 where • 4 if • 5 if • 6 where',
   'Source: Level5_Lesson8.md (Step 3; Listening Task C; Answer key).',
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
   'I *want to* ask about the conference.',
   "I'm *going to* put the sheet in my backpack.",
   'Do you know if the conference is tonight?',
   'Do you know where the office window is?',
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson8.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'if or whether',
  ],
  'title_sz': 22,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('permission_slip'),
  'alt': A('permission_slip'),
  'lw': 4.6,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('Do you know **if** the conference is tonight?', "**Yes. It starts at 6:30.** / **I'm not sure.**"),
   ('Do you know **whether** I need a permission slip?', '**Yes. Please bring the slip.**'),
   ('Can you tell me **if** the office is still open?', '**Yes. It closes at seven.**'),
  ],
  'notes': [
   'Grammar Box 1: if or whether. Each click shows the answer side.',
   'Source: Level5_Lesson8.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'when or where',
  ],
  'title_sz': 22,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('dismissal'),
  'alt': A('dismissal'),
  'lw': 4.6,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('Do you know **where** the office is?', "**It's down the hallway, by the office window.**"),
   ('Do you know **when** it starts?', '**It starts at 6:30.**'),
   ('Do you know **where** I sign up?', '**At the office window.**'),
  ],
  'notes': [
   'Grammar Box 2: when or where. Each click shows the answer side.',
   'Source: Level5_Lesson8.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   'said or told',
  ],
  'title_sz': 22,
  'qhead': 'QUESTION',
  'ahead': 'ANSWER',
  'pic': I('pickup'),
  'alt': A('pickup'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('What did he say about the night?', '**He said the conference was tonight.**'),
   ('What did he tell you to bring?', '**He told me to bring the slip.**'),
   ('What did he say about the time?', '**He said it starts at 6:30.**'),
  ],
  'notes': [
   'Grammar Box 3: said or told. Each click shows the answer side.',
   'Source: Level5_Lesson8.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   'statement order',
  ],
  'title_sz': 22,
  'qhead': 'NOT THIS',
  'ahead': 'SAY THIS',
  'pic': I('newsletter'),
  'alt': A('newsletter'),
  'lw': 4.6,
  'lsz': 13,
  'rsz': 14,
  'pitch_max': 1.05,
  'rows': [
   ('Do you know if is the conference tonight?', '**Do you know if the conference is tonight?**'),
   ('Do you know where is the office?', '**Do you know where the office is?**'),
   ('Do you know when does it start?', '**Do you know when it starts?**'),
  ],
  'notes': [
   'Grammar Box 4: statement order. Each click shows the answer side.',
   'Source: Level5_Lesson8.md (Step 4; Grammar Box 4).',
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
   ('Do you know ______ the office is?', 'where'),
   ('Do you know ______ it starts?', 'when'),
   ('Do you know ______ I need a permission slip?', 'whether'),
   ('Can you tell me ______ the office is still open?', 'if'),
   ('Do you know ______ the signup sheet is?', 'where'),
   ('Do you know ______ the bell rings?', 'when'),
  ],
  'notes': [
   'Click to show each answer: 1 where • 2 when • 3 whether • 4 if • 5 where • 6 when',
   'Source: Level5_Lesson8.md (Step 4; Grammar Practice A; Answer key).',
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
   ('1. Do you know if ______ tonight?', [
 'the conference is',
 'is the conference',
], 0),
   ('2. Do you know where ______ ?', [
 'the office is',
 'is the office',
], 0),
   ('3. Do you know when ______ ?', [
 'it starts',
 'does it start',
], 0),
   ('4. He ______ the conference was tonight.', [
 'said',
 'said me',
], 0),
   ('5. He told ______ to bring the slip.', [
 'me',
 'to me',
], 0),
   ('6. Can you tell me if ______ open?', [
 'the office is',
 'is the office',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 the conference is • 2 the office is • 3 it starts • 4 said • 5 me • 6 the office is',
   'Source: Level5_Lesson8.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('backpack'),
  'alt': A('backpack'),
  'sz': 14,
  'rows': [
   ('Do you know if is the office open?', 'Do you know **if the office is** open?'),
   ('Do you know where is the conference?', 'Do you know **where the conference is?**'),
   ('He told to me to bring the slip.', 'He **told me** to bring the slip.'),
   ('He said me the conference was tonight.', 'He **said** the conference was tonight.'),
   ('Do you know when does it start?', 'Do you know **when it starts?**'),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson8.md (Grammar: Common mistakes).',
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
   'Some cards are a parent.',
  ],
  's2_label': 'B answers.',
  's2_body': [
   'Some are a volunteer.',
  ],
  'pic': I('signup'),
  'alt': A('signup'),
  'notes': [
   'Some cards are a parent. Some are a volunteer. Pick either one. | Volunteer card | Parent card | |---|---| | Ask if the conference is tonight. Ask if you should bring the signup sheet. | Ask if you can pick up early.',
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson8.md (Step 4: Pair check).',
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
   'Sit back to back.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('dismissal'),
  'alt': A('dismissal'),
  'steps': [
   [
    'Sit back to back.',
   ],
   [
    'Sit back to back.',
   ],
   [
    'Sit back to back.',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson8.md (Step 5; Talk Time).',
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
   'Find a new partner.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('newsletter'),
  'alt': A('newsletter'),
  'steps': [
   [
    'Find a new partner.',
   ],
   [
    'Find a new partner.',
   ],
   [
    'Find a new partner.',
   ],
  ],
  'notes': [
   'Round 2.',
   'Source: Level5_Lesson8.md (Step 5; Talk Time).',
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
   ('When is the conference?', 'Tonight at 6:30'),
   ('Where is the conference?', 'In the library'),
   ('What does a volunteer bring?', 'The signup sheet'),
   ('What does a parent bring for early pickup?', 'A permission slip'),
   ('How early should people arrive?', 'Ten minutes early'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   'Click to show each answer: 1 Tonight at 6:30 • 2 In the library • 3 The signup sheet • 4 A permission slip • 5 Ten minutes early',
   'Source: Level5_Lesson8.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('office_window'),
  'alt': A('office_window'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'Write the question you would ask the office, and the answer you hope for.'),
   (1, 'Name: Date:'),
   (1, 'Two with Do you know if / whether.'),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, '1. Finish the question. Use statement order.'),
   (1, '2. Finish your email to the office (Read & Write C).'),
   (1, '3. Ask one person Do you know if…? Report the answer with said or'),
   (1, '4. Review (a tag). Write the tag.'),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'Write the question you would ask the office, and the answer you hope for.',
   'Source: Level5_Lesson8.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   'I can ask *Do you know if / whether…?*',
   'I can keep statement order after *if*.',
   'I can ask *Do you know when / where…?* the Level 4 way.',
  ],
  'bullet_sz': 18,
  'pic': I('bell'),
  'alt': A('bell'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson8.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Mr. Reed and Maya', LEN),
]
