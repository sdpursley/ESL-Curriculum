"""Level 5 Lesson 11 deck spec. Built from the lesson page. Build: python3 scripts/slides/build_deck.py --level 5 --lesson 11 (AGENTS.md section 6)."""
from deckspec import *
N = 11
DECK_TITLE = "Level 5 Lesson 11: I'd Like to File a Claim"
MOD = 'resized and combined, with signs and labels'
PC = pic_credit(MOD); PCS = pic_credit(MOD, True)
I = lambda stem: f'L5_L11_{stem}.png'
A = lambda stem: alt(N, I(stem))
SRC = 'Source: Level5_Lesson11.md'
LEN = '2:02'
AUDIO = f'Audio: about {LEN}. It plays once.' if CFG['audio'] else f'Audio (about {LEN}): coming soon.'
BUL = ['I can start a sentence with a gerund (*Waiting on hold is tiring*)', 'I can soften a request with *I was wondering if…*', 'I can say what was sent or attached, in the passive']
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
  'title': "I'd Like to File a Claim",
  'title_sz': 40,
  'bullets': [
   'I can start a sentence with a gerund (*Waiting on hold is tiring*)',
   'I can soften a request with *I was wondering if…*',
   'I can say what was sent or attached, in the passive',
  ],
  'bullet_sz': 18,
  'pic': I('claim_form'),
  'alt': A('claim_form'),
  'notes': [
   'Welcome learners as they arrive.',
   'Read the three lines under Today you will.',
   'It is not insurance advice.',
   'Source: Level5_Lesson11.md (Topic; At a glance: Objectives).',
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
   'I can start a sentence with a gerund (*Waiting on hold is tiring*)',
   'I can soften a request with *I was wondering if…*',
   'I can say what was sent or attached, in the passive',
   'I can write a 1–2 paragraph letter',
  ],
  'notes': [
   'Read each goal slowly. Learners repeat.',
   'Source: Level5_Lesson11.md (At a glance: Objectives).',
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
  'pic': I('policy_number'),
  'alt': A('policy_number'),
  'notes': [
   'Step 1 · 6:00–6:06 · Opening Talk.',
   'Work with a partner.',
   'Source: Level5_Lesson11.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson11.md (Step 1; Opening Talk page).',
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
   'Source: Level5_Lesson11.md (Step 2; New Words page).',
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
   'Source: Level5_Lesson11.md (Step 2; New Words page; Partner game).',
   PCS,
  ],
 },
 {
  'kind': 'check',
  'title': 'Check the Meaning',
  'sub': 'Look at the picture. Answer the question.',
  'items': [
   {
    'q': 'Is *Waiting* one activity or many?',
    'pic': I('claim_form'),
    'alt': A('claim_form'),
    'a': 'One.',
    'q_sz': 16,
   },
   {
    'q': 'Does the verb after *Waiting* take *is* or *are*?',
    'pic': I('policy_number'),
    'alt': A('policy_number'),
    'a': '*is*',
    'q_sz': 14,
   },
   {
    'q': 'Was the photo attached, or did Hector forget it?',
    'pic': I('photo'),
    'alt': A('photo'),
    'a': 'It was attached.',
    'q_sz': 14,
   },
  ],
  'notes': [
   'The answers are hidden. Ask, then click.',
   '1. One.',
   '2. *is*',
   '3. It was attached.',
   'Source: Level5_Lesson11.md (Step 2: Check the Meaning).',
   PCS,
  ],
 },
 {
  'kind': 'before',
  'context': 'Hector calls about a cracked-screen claim.',
  'context_sz': 18,
  'pic': I('photo'),
  'alt': A('photo'),
  'voices': [
   'Narrator',
   'Ms. Lane',
   'Hector',
  ],
  'listen': [
   'Listen. What is the claim about?',
   '- Play 1 → Task A.',
  ],
  'audio': AUDIO,
  'notes': [
   'Step 3 · 6:12–6:32 · Listening. Play 1 is Task A. Play 2 is Tasks B and C. A third play is fine.',
   'Hector calls about a cracked-screen claim.',
   'The script says going to and want to. Learners only need to recognize gonna and wanna.',
   'Source: Level5_Lesson11.md (Step 3; Listening page).',
   PC,
  ],
 },
 {
  'kind': 'choice',
  'title': 'Listening A',
  'instr': [
   'Listen. What is the claim about?',
  ],
  'ow': 3.45,
  'og': 0.08,
  'osz': 13,
  'sz': 16,
  'right': 12.85,
  'rows': [
   ('1.', [
 'a. A new phone he wants to buy',
 'b. A cracked phone screen',
 'c. A water stain that is still wet',
], 1),
  ],
  'notes': [
   'Click to circle b.',
   'Source: Level5_Lesson11.md (Step 3; Listening Task A; Answer key).',
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
   ('1. The form', [
 'was received',
 'was lost',
 'was not sent',
], 0),
   ('2. The photo', [
 'was attached',
 'is missing',
 'is a water stain',
], 0),
   ('3. He still must send', [
 'the estimate',
 'the phone',
 'a new complaint',
], 0),
   ('4. Reference number', [
 'seven one',
 'four two eight',
 'nine nine',
], 0),
   ('5. Policy number', [
 'four two eight',
 'seven one',
 'three three',
], 0),
   ('6. He is going to', [
 'send it today',
 'stay on hold',
 'buy a new phone',
], 0),
  ],
  'notes': [
   'Click to circle each answer: 1 was received • 2 was attached • 3 the estimate • 4 seven one • 5 four two eight • 6 send it today',
   'Source: Level5_Lesson11.md (Step 3; Listening Task B; Answer key).',
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
  'head2': 'Listen again. Write the geru',
  'sz': 16,
  'aw': 1.7,
  'asz': 16,
  'rows': [
   ('______ on hold was tiring.', 'Waiting'),
   ('The form ______.', 'was received'),
   ('The photo ______.', 'was attached'),
   ('______ a claim takes time.', 'Filing'),
   ('______ a photo helps.', 'Sending'),
   ('______ the estimate is my next step.', 'Sending'),
  ],
  'notes': [
   'Click to show each answer: 1 Waiting • 2 was received • 3 was attached • 4 Filing • 5 Sending • 6 Sending',
   'Source: Level5_Lesson11.md (Step 3; Listening Task C; Answer key).',
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
   'I *want to* file a claim.',
   'I was wondering if you could look up my claim.',
   "I'm *going to* send it today.",
   'Waiting on hold was tiring.',
  ],
  'notes': [
   'gonna and wanna are short forms. This listening uses the full forms. Say each line two times.',
   'Source: Level5_Lesson11.md (Step 3: Hear it, say it).',
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 1',
   'a gerund is the subject',
  ],
  'title_sz': 20,
  'qhead': 'THE ACTIVITY',
  'ahead': 'THE VERB IS SINGUL',
  'pic': I('estimate'),
  'alt': A('estimate'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('Waiting on hold', 'is tiring.'),
   ('Filing a claim', 'takes time.'),
   ('Sending a photo', 'helps.'),
   ('Sending the estimate', 'is my next step.'),
  ],
  'notes': [
   'Grammar Box 1: a gerund is the subject. Each click shows the answer side.',
   'Source: Level5_Lesson11.md (Step 4; Grammar Box 1).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 2',
   'a soft request',
  ],
  'title_sz': 22,
  'qhead': 'YOU CAN SAY',
  'ahead': 'STATEMENT ORDER',
  'pic': I('complaint'),
  'alt': A('complaint'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('I was wondering if', 'you could check the claim.'),
   ('I was wondering if', 'you could look up the reference number.'),
   ('Would you mind', 'looking up the reference number?'),
  ],
  'notes': [
   'Grammar Box 2: a soft request. Each click shows the answer side.',
   'Source: Level5_Lesson11.md (Step 4; Grammar Box 2).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 3',
   'what was sent',
  ],
  'title_sz': 22,
  'qhead': 'THE THING',
  'ahead': 'PASSIVE',
  'pic': I('attachment'),
  'alt': A('attachment'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('The photo', 'was attached.'),
   ('The form', 'was received.'),
   ('The estimate', 'was not attached yet.'),
  ],
  'notes': [
   'Grammar Box 3: what was sent. Each click shows the answer side.',
   'Source: Level5_Lesson11.md (Step 4; Grammar Box 3).',
   PC,
  ],
 },
 {
  'kind': 'table',
  'head': [
   'Grammar Box 4',
   'have to',
  ],
  'title_sz': 22,
  'qhead': 'YOU HAVE TO',
  'ahead': "YOU DON'T HAVE TO",
  'pic': I('reference_number'),
  'alt': A('reference_number'),
  'lw': 4.2,
  'lsz': 15,
  'rsz': 16,
  'pitch_max': 1.05,
  'rows': [
   ('include the policy number', 'stay on hold'),
   ('send the estimate', 'call again if the letter is complete'),
   ('write the reference number', 'add a different problem'),
  ],
  'notes': [
   'Grammar Box 4: have to. Each click shows the answer side.',
   'Source: Level5_Lesson11.md (Step 4; Grammar Box 4).',
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
   ('Waiting on hold ______ tiring.', 'is'),
   ('The photo was ______.', 'attached'),
   ('Filing a claim ______ time.', 'takes'),
   ('I was wondering if you ______ check it.', 'could'),
   ('The form was ______.', 'received'),
   ('Sending a photo ______.', 'helps'),
  ],
  'notes': [
   'Click to show each answer: 1 is • 2 attached • 3 takes • 4 could • 5 received • 6 helps',
   'Source: Level5_Lesson11.md (Step 4; Grammar Practice A; Answer key).',
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
   ('1. Waiting on hold ______ tiring.', [
 'is',
 'are',
], 0),
   ('2. I was wondering if ______ check.', [
 'could you',
 'you could',
], 1),
   ('3. The photo was ______ .', [
 'attach',
 'attached',
], 1),
   ('4. ______ a claim takes time.', [
 'Filing',
 'File',
], 0),
   ('5. You ______ include the policy number.', [
 'have to',
 'has to',
], 0),
   ('6. Sending a photo ______ .', [
 'help',
 'helps',
], 1),
  ],
  'notes': [
   'Click to circle each answer: 1 is • 2 you could • 3 attached • 4 Filing • 5 have to • 6 helps',
   'Source: Level5_Lesson11.md (Step 4; Grammar Practice B; Answer key).',
  ],
 },
 {
  'kind': 'mistakes',
  'pic': I('customer_service'),
  'alt': A('customer_service'),
  'sz': 14,
  'rows': [
   ('Waiting on hold are tiring.', 'Waiting on hold **is** tiring.'),
   ('I was wondering if could you check.', 'I was wondering if **you could** check.'),
   ('The photo was attach.', 'The photo **was attached**.'),
   ('Waiting are hard.', '**Waiting is** hard.'),
  ],
  'notes': [
   "Read Don't say, then Say. Learners try first. Then click.",
   'Source: Level5_Lesson11.md (Grammar: Common mistakes).',
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
   'A says: "Waiting on hold." B says: "Waiting on hold is tiring." Then switch.',
  ],
  's2_label': 'B answers.',
  's2_body': [
   'Use filing and sending too.',
  ],
  'pic': I('on_hold'),
  'alt': A('on_hold'),
  'notes': [
   'A says: "Waiting on hold." B says: "Waiting on hold is tiring." Then switch. Use filing and sending too. ---',
   'Break · 6:45–7:00.',
   'Source: Level5_Lesson11.md (Step 4: Pair check).',
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
  'pic': I('complaint'),
  'alt': A('complaint'),
  'steps': [
   [
    'Pairs.',
   ],
   [
    'Then switch.',
   ],
   [
    'Then switch.',
   ],
  ],
  'notes': [
   'Round 1.',
   'Source: Level5_Lesson11.md (Step 5; Talk Time).',
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
   'List the two paragraphs before anyone writes full sentences.',
  ],
  'time': '7:00–7:18',
  'sub_sz': 26,
  'grouping_sz': 16,
  'step_sz': 16,
  'pic': I('reference_number'),
  'alt': A('reference_number'),
  'steps': [
   [
    'List the two paragraphs before anyone',
    'writes full sentences.',
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
   'Source: Level5_Lesson11.md (Step 5; Talk Time).',
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
   ('What is the claim about?', 'A cracked phone screen'),
   ('What was attached?', 'The photo'),
   ('What is still missing?', 'The estimate'),
   ('What is the reference number?', 'Seven one'),
   ('What is the policy number?', 'Four two eight'),
  ],
  'notes': [
   'Step 6 · 7:18–7:25 · Read & Write.',
   'Click to show each answer: 1 A cracked phone screen • 2 The photo • 3 The estimate • 4 Seven one • 5 Four two eight',
   'Source: Level5_Lesson11.md (Step 6; Read & Write page; Answer key).',
  ],
 },
 {
  'kind': 'go',
  'pic': I('resolution'),
  'alt': A('resolution'),
  'time': '7:25–7:30',
  'body_sz': 15,
  'compact': True,
  'body1': [
   (0, 'Start a claim letter.'),
   (1, 'Name: Date:'),
   (1, '1.'),
   (4, 'Give this page to your teacher.'),
  ],
  'body2': [
   (0, 'About 20–25 minutes.'),
   (1, '1. Write the verb.'),
   (1, '2. Finish your letter (Read & Write). About 8–12 sentences.'),
   (1, '3. Say I was wondering if to a friend. Write the sentence.'),
   (1, '4. Review: write one passive. The photo was attached. Then write one'),
   (5, 'Bring it next week!'),
  ],
  'notes': [
   'Step 7 · 7:25–7:30 · Exit ticket and homework. Never skip the exit ticket.',
   'Start a claim letter.',
   'Source: Level5_Lesson11.md (Step 7; Exit Ticket page; Homework page).',
   PC,
  ],
 },
 {
  'kind': 'goodbye',
  'title': 'Goodbye! See You Next Week!',
  'title_sz': 36,
  'bullets': [
   'I can start a sentence with a gerund (*Waiting on hold is tiring*)',
   'I can soften a request with *I was wondering if…*',
   'I can say what was sent or attached, in the passive',
  ],
  'bullet_sz': 18,
  'pic': I('cracked_screen'),
  'alt': A('cracked_screen'),
  'notes': [
   'Read the three Now you can lines.',
   'Homework is about 20–25 minutes. Bring it next week.',
   'Source: Level5_Lesson11.md (At a glance: Objectives; Step 7).',
   PC,
  ],
 },
 credits(N, 'Ms. Lane and Hector', LEN),
]
