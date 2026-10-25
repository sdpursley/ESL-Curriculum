"""Level 5 Lesson 9 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 9 (AGENTS.md section 6)."""
from deckspec import *
N = 9
DECK_TITLE = 'Level 5 Lesson 9: It Must Be an Ad'
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L9_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson9.md'
LEN = '2:20'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ["I can say how sure I am with *must*, *might*, and *can't*.", 'I can name two clues (author, date, ad, a mismatch).', 'I can say what I would do before I believed the page.']
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
  'title': 'It Must Be an Ad',
  'title_sz': 40,
  'bullets': [
   "I can say how sure I am with *must*, *might*, and *can't*.",
   'I can name two clues (author, date, ad, a mismatch).',
   'I can say what I would do before I believed the page.',
  ],
  'bullet_sz': 18,
  'pic': I('website'),
  'alt': A('website'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   'Source: Level5_Lesson9.md (Topic; At a glance: Objectives).',
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
   "I can say how sure I am with *must*, *might*, and *can't*.",
   'I can name two clues (author, date, ad, a mismatch).',
   'I can say what I would do before I believed the page.',
   'I can tell a classmate, with a reason.',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson9.md (At a glance: Objectives).',
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
   'Work with a partner. A asks Do you',
   'know if…? B keeps statement order and reports one answer. Then compare one homework sentence.',
  ],
  'box2': [
   'Homework check: read one indirect question',
   'from your email.',
  ],
  'pic': I('source'),
  'alt': A('source'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson9.md (Step 1; Opening Talk page).',
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
   'Work with a partner. A asks Do you know if…? B',
   'keeps statement order and reports one answer. Then compare one homework sentence.',
  ],
  'rows': [
   'Ask: Do you know if the office is open?',
   'Keep statement order. Not: if is the office open.',
   'Report the answer: He said… / He told me…',
   'Homework check: read one indirect question from your email.',
  ],
  'notes': [
   'Each click shows the next card.',
   'A asks. B answers. Then switch.',
   'Source: Level5_Lesson9.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson9.md (Step 2; New Words page).',
   PCS,
  ],
 },
 {
  'kind': 'words',
  'title': 'More New Words',
  'instr': [
   'Partner game:',
   "Must, might, or can't?",
  ],
  'words': W[6:],
  'notes': [
   'A points to a picture. B names it and uses it in one sentence. Then switch.',
   'Source: Level5_Lesson9.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'A page with Buy now is what?',
    'pic': I('website'),
    'alt': A('website'),
    'a': 'an ad',
    'q_sz': 16,
   },
   {
    'q': 'Who writes a page?',
    'pic': I('author'),
    'alt': A('author'),
    'a': 'the author',
    'q_sz': 16,
   },
   {
    'q': 'What shows how old a page is?',
    'pic': I('date_stamp'),
    'alt': A('date_stamp'),
    'a': 'the date stamp',
    'q_sz': 16,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. an ad',
   '2. the author',
   '3. the date stamp',
   'Source: Level5_Lesson9.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'Noah shows Aisha a post.',
  'context_sz': 18,
  'pic': I('author'),
  'alt': A('author'),
  'voices': [
   'Narrator',
   'Noah',
   'Aisha',
  ],
  'listen': [
   'Listen. Is the store closing?',
   '| 6:12–6:32 | Listening: play 1 (Task A), play 2 (Tasks B and C) +',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'Noah shows Aisha a post.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson9.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. Is the store closing?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 13,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. Yes. It closes on Friday',
 "b. No. The store's page says it is open",
 'c. No one can tell',
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson9.md (Step 3; Listening Task A; Answer key).',
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening B',
  'instr': [
   'B. Listen again. Circle the clue.',
  ],
  'instr_sz': 16,
  'ow': 2.45,
  'og': 0.12,
  'osz': 16,
  'sz': 15,
  'right': 12.7,
  'rows': [
   ('1. Author on the post', [
 'yes',
 'no',
], 1),
   ('2. Date stamp on the post', [
 'yes',
 'no',
], 1),
   ('3. Store logo', [
 'matches',
 'is different',
], 0),
   ("4. Store's own page", [
 'open',
 'closing',
], 0),
   ('5. The share button', [
 'he shares it',
 'he does not share it',
], 1),
   ('6. The comment', [
 'it is a fact',
 'it is not a fact',
], 1),
  ],
  'notes': [
   'Click to circle each answer: 1 no • 2 no • 3 matches • 4 open • 5 he does not share it • 6 it is not a fact',
   'Source: Level5_Lesson9.md (Step 3; Listening Task B; Answer key).',
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
  'head2': 'Listen again. Write must, mi',
  'sz': 16,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ('Then it ______ be old.', 'might'),
   ('(First guess) It ______ be a rumor.', 'might'),
   ('The closing post ______ be true.', "can't"),
   ('(After the store page) It ______ be a rumor.', 'must'),
   ('That page ______ be the one we trust.', 'must'),
   ('It ______ be a fact.', "can't"),
  ],
  'notes': [
   "Click to show each answer: 1 might • 2 might • 3 can't • 4 must • 5 must • 6 can't",
   'Source: Level5_Lesson9.md (Step 3; Listening Task C; Answer key).',
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
   'We *want to* check a second source first.',
   "I'm *going to* look for the store's own page.",
   'It must be a rumor.',
   "It can't be a fact.",
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson9.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'must be',
  ],
  'title_sz': 22,
  'qhead': 'CLUE',
  'ahead': 'ANSWER',
  'pic': I('advertisement'),
  'alt': A('advertisement'),
  'lw': 4.6,
  'lsz': 13,
  'rsz': 14,
  'pitch_max': 1.05,
  'rows': [
   ('The page has a Buy now button. What is it?', '**It must be an ad.**'),
   ("The store's page says the store is open. What is the closing post?", '**It must be a rumor.**'),
   ('The logo, the author, and the date all match. What is the page?', "**It must be the store's page.**"),
  ],
  'notes': [
   'Grammar Box 1: must be. Each click shows the answer side.',
   'Source: Level5_Lesson9.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'might be',
  ],
  'title_sz': 22,
  'qhead': 'CLUE',
  'ahead': 'ANSWER',
  'pic': I('screenshot'),
  'alt': A('screenshot'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('The date says 2019. What do you think?', '**It might be old.**'),
   ('There is no author. What do you think?', '**It might be a rumor.**'),
   ('The comment has no source. What do you think?', '**It might be a guess.**'),
  ],
  'notes': [
   'Grammar Box 2: might be. Each click shows the answer side.',
   'Source: Level5_Lesson9.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   "can't be",
  ],
  'title_sz': 22,
  'qhead': 'CLUE',
  'ahead': 'ANSWER',
  'pic': I('fact'),
  'alt': A('fact'),
  'lw': 4.6,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ("The logo is different. Is it the city's page?", "**It can't be the city's page.**"),
   ("The store's page says open. Is the store closing?", "**It can't be closing.**"),
   ('The first post has no author and no date. Is it a fact?', "**It can't be a fact.**"),
  ],
  'notes': [
   "Grammar Box 3: can't be. Each click shows the answer side.",
   'Source: Level5_Lesson9.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   'how sure?',
  ],
  'title_sz': 22,
  'qhead': 'HOW SURE?',
  'ahead': 'SAY',
  'pic': I('rumor'),
  'alt': A('rumor'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('You are almost sure.', '**must be**'),
   ('You are less sure.', '**might be**'),
   ('It is not possible.', "**can't be**"),
  ],
  'notes': [
   'Grammar Box 4: how sure?. Each click shows the answer side.',
   'Source: Level5_Lesson9.md (Step 4; Grammar Box 4).',
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
   ('The page has a Buy now button. It ______ be an ad.', 'must'),
   ('The date says 2019. It ______ be old.', 'might'),
   ("The logo is different. It ______ be the city's page.", "can't"),
   ('There is no author. It ______ be a rumor.', 'might'),
   ("The store's own page says the store is open. The post ______ be true.", "can't"),
   ('Aisha is almost sure. She says it ______ be a rumor.', 'must'),
  ],
  'notes': [
   "Click to show each answer: 1 must • 2 might • 3 can't • 4 might • 5 can't • 6 must",
   'Source: Level5_Lesson9.md (Step 4; Grammar Practice A; Answer key).',
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
   ('1. It ______ an ad.', [
 'must',
 'must be',
], 1),
   ('2. It ______ the city page.', [
 'can be not',
 "can't be",
], 1),
   ('3. The date says 2019. It ______ old.', [
 'must be',
 'might be',
], 1),
   ('4. It ______ an ad.', [
 'must to be',
 'must be',
], 1),
   ("5. It can't ______ official.", [
 'be',
 'to be',
], 0),
   ("6. *Can't* here means ______ .", [
 'not able',
 'not possible',
], 1),
  ],
  'notes': [
   "Click to circle each answer: 1 must be • 2 can't be • 3 might be • 4 must be • 5 be • 6 not possible",
   'Source: Level5_Lesson9.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('date_stamp'),
  'alt': A('date_stamp'),
  'sz': 14,
  'rows': [
   ('It must an ad.', 'It **must be** an ad.'),
   ('It can be not the city page.', "It **can't be** the city page."),
   ('It must to be an ad.', 'It **must be** an ad.'),
   ("It can't means she is not able.", "**It can't be** means it is not possible."),
   ('It must be not official.', "It **can't be** official."),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson9.md (Grammar: Common mistakes).',
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
   'Use only these pages.',
  ],
  's2_label': 'B answers.',
  's2_body': [
   '| Page 1 · City bus notice | Page 2 · Amazing deal | Page 3 · Neighborhood post |',
  ],
  'pic': I('logo'),
  'alt': A('logo'),
  'notes': [
   'Use only these pages. | Page 1 · City bus notice | Page 2 · Amazing deal | Page 3 · Neighborhood post | |---|---|---| | Author: the city bus office. Date: this week. Logo: the city bus logo. The evening bus still stops',
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson9.md (Step 4: Pair check).',
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
   'Read the three class pages.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('screenshot'),
  'alt': A('screenshot'),
  'steps': [
   [
    'Read the three class pages.',
   ],
   [
    'Read the three class pages.',
   ],
   [
    'Read the three class pages.',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson9.md (Step 5; Talk Time).',
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
   'Before you share, name one check.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('rumor'),
  'alt': A('rumor'),
  'steps': [
   [
    'Before you share, name one check.',
   ],
   [
    'Before you share, name one check.',
   ],
   [
    'Before you share, name one check.',
   ],
  ],
  'notes': [
   'Round 2.',
   'Source: Level5_Lesson9.md (Step 5; Talk Time).',
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
   ('Which page names an author?', "The library's page"),
   ("What time is on the library's page?", 'Thursday at 6:30'),
   ('What time is on the repost?', 'Thursday at 8:00'),
   ('Which page do you trust?', "The library's page"),
   ('What is one clue?', 'The author and the date'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   "Click to show each answer: 1 The library's page • 2 Thursday at 6:30 • 3 Thursday at 8:00 • 4 The library's page • 5 The author and the date",
   'Source: Level5_Lesson9.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('comment'),
  'alt': A('comment'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'How can you tell that a page might be wrong?'),
   (1, 'Name: Date:'),
   (1, "Use must, might, or can't."),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, "1. Write must, might, or can't."),
   (1, '2. Finish your message to a friend (Read & Write C).'),
   (1, '3. Tell a friend one clue you would check before you shared a class'),
   (1, '4. Review (Do you know if). Finish the question in statement order.'),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'How can you tell that a page might be wrong?',
   'Source: Level5_Lesson9.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   "I can say how sure I am with *must*, *might*, and *can't*.",
   'I can name two clues (author, date, ad, a mismatch).',
   'I can say what I would do before I believed the page.',
  ],
  'bullet_sz': 18,
  'pic': I('reliable'),
  'alt': A('reliable'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson9.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Noah and Aisha', LEN),
]
