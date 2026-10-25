"""Level 5 Lesson 13 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 13 (AGENTS.md section 6)."""
from deckspec import *
N = 13
DECK_TITLE = 'Level 5 Lesson 13: A Short Talk'
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L13_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson13.md'
LEN = '2:20'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ['I can open a talk with one clear sentence', 'I can give two examples', 'I can close with a next step']
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
  'title': 'A Short Talk',
  'title_sz': 40,
  'bullets': [
   'I can open a talk with one clear sentence',
   'I can give two examples',
   'I can close with a next step',
  ],
  'bullet_sz': 20,
  'pic': I('outline'),
  'alt': A('outline'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   'Source: Level5_Lesson13.md (Topic; At a glance: Objectives).',
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
   'I can open a talk with one clear sentence',
   'I can give two examples',
   'I can close with a next step',
   'I can speak for about two minutes from notes',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson13.md (At a glance: Objectives).',
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
  'pic': I('notecard'),
  'alt': A('notecard'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson13.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson13.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson13.md (Step 2; New Words page).',
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
   'Source: Level5_Lesson13.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'Does the introduction name the point?',
    'pic': I('introduction'),
    'alt': A('introduction'),
    'a': 'Yes.',
    'q_sz': 16,
   },
   {
    'q': 'Does each example need a detail?',
    'pic': I('example'),
    'alt': A('example'),
    'a': 'Yes.',
    'q_sz': 16,
   },
   {
    'q': 'Is a conclusion a new story?',
    'pic': I('conclusion'),
    'alt': A('conclusion'),
    'a': 'No.',
    'q_sz': 16,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. Yes.',
   '2. Yes.',
   '3. No.',
   'Source: Level5_Lesson13.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'Imani, a former learner, gives a short talk at a practice night: what she has been learning, one hard moment, one person who helped, and her next step.',
  'context_sz': 16,
  'pic': I('pause'),
  'alt': A('pause'),
  'voices': [
   'Narrator',
   'Imani',
   'Mr. Gordon',
  ],
  'listen': [
   'Listen. What is her main point?',
   '- Play 1 → Task A.',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'Imani, a former learner, gives a short talk at a practice night: what she has been learning, one hard moment, one person who helped, and her next step.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson13.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. What is her main point?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 15,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. the loudest applause',
 'b. speaking up at work',
 'c. a forgotten notecard',
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson13.md (Step 3; Listening Task A; Answer key).',
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
   ('1. "My point is simple" is the', [
 'introduction',
 'example',
 'conclusion',
], 0),
   ('2. The hard moment is an', [
 'introduction',
 'example',
 'conclusion',
], 1),
   ("3. The mentor's question is an", [
 'introduction',
 'example',
 'conclusion',
], 1),
   ('4. The next step is the', [
 'introduction',
 'example',
 'conclusion',
], 2),
   ('5. She is going to practice with', [
 'a stopwatch',
 'a microphone',
 'a whiteboard',
], 0),
   ('6. Applause is for', [
 'finishing',
 'the longest story',
 'a perfect memory',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 introduction • 2 example • 3 example • 4 conclusion • 5 a stopwatch • 6 finishing',
   'Source: Level5_Lesson13.md (Step 3; Listening Task B; Answer key).',
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
  'head2': 'Listen again. Write the four',
  'sz': 16,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ('First: ______', 'Introduction'),
   ('Second: ______', 'Example 1'),
   ('Third: ______', 'Example 2'),
   ('Fourth: ______', 'Conclusion'),
  ],
  'notes': [
   'Click to show each answer: 1 Introduction • 2 Example 1 • 3 Example 2 • 4 Conclusion',
   'Source: Level5_Lesson13.md (Step 3; Listening Task C; Answer key).',
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
   "I've been learning to speak up at work.",
   'I *want to* give two examples.',
   "I'm *going to* practice with a stopwatch.",
   'I am not *going to* memorize the talk.',
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson13.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'introduction',
  ],
  'title_sz': 22,
  'qhead': 'THE INTRODUCTION',
  'ahead': 'IT NAMES THE POINT',
  'pic': I('eye_contact'),
  'alt': A('eye_contact'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ("I've been learning to speak up at work.", 'That is my point.'),
   ('A mentor helped me.', 'That is part of the point.'),
   ('I want to give two examples.', 'Then the examples start.'),
  ],
  'notes': [
   'Grammar Box 1: introduction. Each click shows the answer side.',
   'Source: Level5_Lesson13.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'two examples',
  ],
  'title_sz': 22,
  'qhead': 'THE EXAMPLE',
  'ahead': 'A DETAIL',
  'pic': I('introduction'),
  'alt': A('introduction'),
  'lw': 4.6,
  'lsz': 13,
  'rsz': 14,
  'pitch_max': 1.05,
  'rows': [
   ('Example 1', 'By the time I finished my first month, I had learned to pause.'),
   ('The hard moment', 'I wish I had looked up sooner, so next time I will make eye contact.'),
   ('Example 2', 'My mentor asked one question.'),
  ],
  'notes': [
   'Grammar Box 2: two examples. Each click shows the answer side.',
   'Source: Level5_Lesson13.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   'conclusion',
  ],
  'title_sz': 22,
  'qhead': 'THE CONCLUSION',
  'ahead': 'NOT A NEW STORY',
  'pic': I('example'),
  'alt': A('example'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('Repeat the point in new words.', 'I can speak from notes.'),
   ('Add a next step.', "I'm going to practice one talk a week."),
   ('Stop.', 'Applause is for finishing.'),
  ],
  'notes': [
   'Grammar Box 3: conclusion. Each click shows the answer side.',
   'Source: Level5_Lesson13.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   'review sentences, not a',
  ],
  'title_sz': 20,
  'qhead': 'REVIEW',
  'ahead': 'ONE SENTENCE',
  'pic': I('conclusion'),
  'alt': A('conclusion'),
  'lw': 4.6,
  'lsz': 13,
  'rsz': 14,
  'pitch_max': 1.05,
  'rows': [
   ("I've been learning…", "I've been learning to speak up at work."),
   ('By the time I finished…, I had…', 'By the time I finished my first month, I had learned to pause.'),
   ('I wish I had…, so next time I will…', 'I wish I had looked up sooner, so next time I will make eye contact.'),
   ("I'm going to…", "I'm going to practice with a stopwatch."),
  ],
  'notes': [
   'Grammar Box 4: review sentences, not a new tense. Each click shows the answer side.',
   'Source: Level5_Lesson13.md (Step 4; Grammar Box 4).',
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
   ("My point is simple. I've been learning to speak up. ______", 'Introduction'),
   ('By the time I finished my first month, I had learned to pause. ______', 'Example'),
   ('My mentor asked one question. ______', 'Example'),
   ('I can speak from notes, and my next step is one talk a week. ______', 'Conclusion'),
   ("I'm going to practice with a stopwatch. ______", 'Conclusion'),
   ('I wish I had looked up sooner, so next time I will make eye contact. ______', 'Example'),
  ],
  'notes': [
   'Click to show each answer: 1 Introduction • 2 Example • 3 Example • 4 Conclusion • 5 Conclusion • 6 Example',
   'Source: Level5_Lesson13.md (Step 4; Grammar Practice A; Answer key).',
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
   ('1. The introduction ______ .', [
 'names the point',
 'tells a new story',
], 0),
   ('2. Each example ______ .', [
 'has a detail',
 'has no detail',
], 0),
   ('3. The conclusion ______ .', [
 'is a new story',
 'repeats the point',
], 1),
   ('4. Next step: ______ practice.', [
 "I'm going to",
 'I gonna',
], 0),
   ('5. By the time I finished, I ______ to pause.', [
 'had learned',
 'have learn',
], 0),
   ("6. I've been ______ to speak up.", [
 'learning',
 'learn',
], 0),
  ],
  'notes': [
   "Click to circle each answer: 1 names the point • 2 has a detail • 3 repeats the point • 4 I'm going to • 5 had learned • 6 learning",
   'Source: Level5_Lesson13.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('mentor'),
  'alt': A('mentor'),
  'sz': 14,
  'rows': [
   ('Start with the example and never say the point.', 'Start with the **introduction**. It names the point.'),
   ('A conclusion that is a new story.', 'The conclusion **repeats the point** and adds a next step.'),
   ('I gonna practice.', "**I'm going to** practice."),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson13.md (Grammar: Common mistakes).',
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
   'A says "introduction," "example," or "conclusion." B says what that part must do.',
  ],
  's2_label': 'B answers.',
  's2_body': [
   'Then switch.',
  ],
  'pic': I('applause'),
  'alt': A('applause'),
  'notes': [
   'A says "introduction," "example," or "conclusion." B says what that part must do. Then switch. ---',
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson13.md (Step 4: Pair check).',
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
   'Partners.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('introduction'),
  'alt': A('introduction'),
  'steps': [
   [
    'Partners.',
   ],
   [
    'Partners.',
   ],
   [
    'Partners.',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson13.md (Step 5; Talk Time).',
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
  'pic': I('conclusion'),
  'alt': A('conclusion'),
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
   'Source: Level5_Lesson13.md (Step 5; Talk Time).',
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
   ('What is her main point?', 'She has been learning to speak up at work'),
   ('What happened in example 1?', 'She did not look up'),
   ('Who helped her?', 'Her mentor'),
   ('What is her next step?', 'One short talk a week'),
   ('What does the conclusion do?', 'It repeats the point and adds a next step'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   'Click to show each answer: 1 She has been learning to speak up at work • 2 She did not look up • 3 Her mentor • 4 One short talk a week • 5 It repeats the point and adds a next step',
   'Source: Level5_Lesson13.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('community_center'),
  'alt': A('community_center'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'Write your introduction and your conclusion only.'),
   (1, 'Name: Date:'),
   (1, 'You will say the examples in the rehearsal.'),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, '1. Label the part: Introduction, Example, or Conclusion.'),
   (1, '2. Finish your outline, then the talk in 12–16 sentences.'),
   (1, '3. Say your introduction aloud to a friend. One time is enough.'),
   (1, "4. Review: write I'm going to and your next step."),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'Write your introduction and your conclusion only.',
   'Source: Level5_Lesson13.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   'I can open a talk with one clear sentence',
   'I can give two examples',
   'I can close with a next step',
  ],
  'bullet_sz': 20,
  'pic': I('achievement'),
  'alt': A('achievement'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson13.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Imani and Mr. Gordon', LEN),
]
