import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=5, week=5, title='Would You Mind…?',
topic='Asking a neighbor or coworker for a favor: getting the mail and watering the plants while you\'re away, a spare key, covering or switching a shift, and borrowing something. Learners ask with *Would you mind…?* and *Do you mind if I…?*, and say yes or no politely. All favors, keys, and addresses are invented.',
cq='Is it a problem for you? If not, what do you say?',
builds=[
 ('*Can you…? / Could you…?* for requests', 'Level 2', '***Would you mind* + -ing** for bigger favors: *Would you mind getting my mail?*'),
 ('*I\'d like to…*', 'Level 3 Lesson 7', '*I\'d like to switch my Friday shift.* and permission: ***Do you mind if I…?***'),
 ('*will* for offers; possessive pronouns', 'Level 3', '*Sure, I\'ll do it.* • *Could I borrow **yours**?*'),
],
objectives=['ask for a favor with *Would you mind…?*',
 'answer *No, not at all* (= "Yes, I\'ll help") or say no politely, with a reason and another idea',
 'ask permission with *Do you mind if I…?*',
 'ask a coworker to switch a shift and confirm it in a short text',
 'write a note to a neighbor (5–8 sentences) asking for a favor while they\'re away'],
materials=['Board and markers', 'Favor cards and "my week" cards (in the workbook Talk Time page; copy them onto index cards, optional)', 'A key and an envelope (optional, for the warm-up)'],
prep='15 minutes (read the plan; practice reading the listening script; practice the thumbs-up "No, not at all!")',
words=[('favor', 'favor', True), ('borrow', 'borrow', True), ('water the plants', 'water_the_plants', True), ('feed the cat', 'feed_the_cat', True), ('get the mail', 'get_the_mail', True),
 ('spare key', 'spare_key', True), ('package', 'package', True), ('switch shifts', 'switch_shifts', True), ('cover a shift', 'cover_a_shift', True), ('be away', 'be_away', True),
 ('owe (someone)', 'owe', False), ('thank-you note', 'thank_you_note', False)],
more_vocab='*Also:* a neighbor, a coworker, lend, a ladder, a trip, a package room, a code, a text, ask the supervisor, I owe you one, go ahead.',
clock=clock('', ' (+ My Words)', '', '*Would you mind…? / Do you mind if I…?*', 'Favor Exchange + Shift Switch Text', 'A building notice + a neighbor\'s note; a note to a neighbor',
 talk_group='Mingle, then pairs'),
attend='With 5 or fewer, make a circle for Favor Exchange: each person asks the person on the left. Do the Shift Switch Text in pairs; you join if there is an odd number. Late arrivals join the mingle with a new favor card.',
)
L['steps'] = [
 step1('Opening Talk', 'suggestions: *Why don\'t you…? / You could… / It\'s a good idea to…*',
  'you say, "I sit all day at work. Any ideas?" The learner gives a suggestion. Then you ask, "Why is that a good idea?" Help them say 3 sentences.',
  'Pairs compare Homework item 1 (*for / since* and suggestions) and read their 3 good ideas (item 3) to each other. Then they fill in the box on the Opening Talk page.',
  '*You could to try* (→ *You could try*) and *I have a cough since Sunday* (→ *I\'ve had a cough since Sunday*)'),
 step2('*favor* (help you ask for); *borrow* (take and give back) vs. *lend* (give and get back); *water the plants*, *feed the cat*, *get the mail* (mime each); *spare key* (an extra key: show two keys); *package*; *switch shifts* (you take my Friday, I take your Sunday) vs. *cover a shift* (you work my shift); *be away* (not at home); *owe* (*I owe you one* = I\'ll help you next time); *thank-you note*.',
  'ask "If I borrow your pen, do I give it back?" (yes) • "If you cover my shift, who works?" (you do) • "Is a spare key the first key or an extra key?" (an extra key).',
  'Would you mind getting my mail? → No, not at all.'),
 step3('Patricia is going away for a week. First, she talks to her neighbor, Mr. Wilson. Then, at work, her coworker Omar asks her for a favor. Listen: what favors do they ask for?',
  'Point to the script lines. *gonna* = going to: "I\'m **gonna** be away next week." *wanna* = want to: "I **wanna** help, but I can\'t." Then practice *Would you mind…?* and *Do you mind if I…?* said smoothly, with a friendly rise.', '{EST}'),
 step4('*Would you mind…? / Do you mind if I…?*', 'give a learner your key. Say, "I\'m going to be away. **Would you mind getting** my mail?" Show a thumbs-up and help the learner say, "**No, not at all.**" Write: *Would you mind + -ing?* → *No* = "No problem. I\'ll do it." Then ask, "**Do you mind if I open** the window?" Help them say, "No, go ahead."',
  'Box 1: read across: *Would you mind getting my mail? → No, not at all. I\'ll do it. / Sorry, I can\'t.* Box 2: permission: *Do you mind if I…? → No, go ahead.* Box 3: saying yes and saying no politely. Box 4: how polite?',
  '"*Would you mind helping me?* You want to help. Do you say *yes* or *no*?" (*No, not at all.*) • "*Would you mind to get* or *getting*?" (*getting*) • "*Do you mind if I leaving* or *if I leave*?" (*if I leave*).',
  'A asks a favor from the pictures with *Would you mind…?* B answers with a thumbs-up and *No, not at all*, or *Sorry, I can\'t, because…* Switch.'),
 brk('*Would you mind + -ing? → No, not at all. (= I\'ll help) / Sorry, I can\'t, because… • Do you mind if I…? → No, go ahead.*'),
 step5('Favor Exchange + Shift Switch Text', 'hold up a favor card and ask a learner, "Would you mind getting my mail next week?" Help them check their "my week" card and answer, "No, not at all," or "Sorry, I can\'t, because I\'ll be away. Why don\'t you ask Ana?" Say: "Answer, give a reason, and offer an idea."',
  '**Favor Exchange (mingle).** Each learner has a favor card and a "my week" card. Ask three people. Each person answers *No, not at all* or *Sorry, I can\'t, because…* and offers another idea. Write who said yes.',
  '**Shift Switch Text (pairs).** Pairs write a 3-sentence text that confirms a shift switch (the day, the time, thanks). Then they read it to another pair. Remind them: "Ask your supervisor first."',
  'a whole-room mingle for round 1; then pairs for round 2.', 'two lines face each other; move one place each round. Then pairs.',
  'a circle for round 1: each person asks the person on the left. Then pairs (you join if there is an odd number).'),
 step6('A building notice + a neighbor\'s note', 'Learners read the notice about packages and the note on the Read & Write page and answer the questions.',
  'Learners write a note to a neighbor (5–8 sentences) asking for a favor while they\'re away: the dates, what to do, where the key is, thanks, and an offer to help back. Show the example. Invented details are fine.'),
 step7('Ask a classmate for a favor with *Would you mind…?*', 'Would you mind helping me with my homework? No, not at all. I\'m asking because the last question is hard.',
  'item 1: *you / mind / feed / my cat? → Would you mind feeding my cat?*'),
]
L['listen'] = dict(title='Would You Mind…?', voices={'Narrator': 'N', 'Patricia': 'Kim', 'Mr. Wilson': 'Carlos', 'Omar': 'Sam'},
 female=['Narrator', 'Patricia'], names=['Patricia', 'Wilson', 'Omar', 'Lina'], tts={},
 setting='Patricia is going away for a week. First, she asks her older neighbor, Mr. Wilson, for some favors. The next day at work, her coworker Omar asks her for a favor.',
 intro='Lesson five. Patricia is going away for a week. First, she talks to her neighbor, Mr. Wilson.',
 lines=[
  ('Patricia', 'Hi, Mr. Wilson. Could I ask you a favor?'),
  ('Mr. Wilson', 'Of course, Patricia. What is it?'),
  ('Patricia', 'I\'m gonna be away next week. I\'m visiting my sister. Would you mind getting my mail?'),
  ('Mr. Wilson', 'No, not at all. I\'m home all week.'),
  ('Patricia', 'Thank you! And would you mind watering my plants? Just two times, on Tuesday and Friday.'),
  ('Mr. Wilson', 'No problem. Where will the key be?'),
  ('Patricia', 'I\'m gonna give you my spare key tonight. Oh, and would you mind feeding my cat, too?'),
  ('Mr. Wilson', 'Sure, I\'ll do it. I love cats. Do you mind if I put your packages inside, too?'),
  ('Patricia', 'No, go ahead. That\'s very kind.'),
  ('Mr. Wilson', 'Have a good trip. Don\'t worry about anything.'),
  ('Narrator', 'The next day, at work, Patricia talks to her coworker, Omar.'),
  ('Omar', 'Hey, Patricia. Would you mind covering my Saturday shift? My son has a soccer game.'),
  ('Patricia', 'Oh, I\'m sorry, I can\'t. I\'ll be away on Saturday. I wanna help, but I can\'t.'),
  ('Omar', 'Oh, right. You told me.'),
  ('Patricia', 'Why don\'t you ask Lina? She wants more hours this month.'),
  ('Omar', 'Good idea. Do you mind if I tell her you suggested it?'),
  ('Patricia', 'No, not at all. But ask the supervisor first, OK?'),
  ('Omar', 'Sure. Thanks, Patricia. I owe you one.'),
  ('Patricia', 'You\'re welcome. Good luck with the game!'),
 ],
 A=dict(q='What favors do they ask for?', opts=['get the mail, water the plants, feed the cat, and cover a shift', 'borrow a ladder and switch shifts', 'pick up a package and lend a car'], ans=0),
 B=dict(head='Yes or no, and why? Circle the answer.', kind='choice', items=[
  dict(s='The mail: Mr. Wilson says {{*yes|no}}.', ev='No, not at all. I\'m home all week.'),
  dict(s='The plants: water them on {{*Tuesday and Friday|Monday and Thursday}}.', ev='Just two times, on Tuesday and Friday.'),
  dict(s='The key: Patricia will give him {{*her spare key|her car key}} tonight.', ev='I\'m gonna give you my spare key tonight'),
  dict(s='The packages: Mr. Wilson can put them {{*inside|at the office}}.', ev='Do you mind if I put your packages inside, too?'),
  dict(s='The Saturday shift: Patricia says {{yes|*no}}.', ev='Oh, I\'m sorry, I can\'t.'),
  dict(s='Why? She {{*will be away|has a soccer game}}.', ev='I\'ll be away on Saturday.'),
 ]),
 C=dict(head='Write the missing word: an *-ing* word or *if*.', items=[
  'Would you mind [getting] my mail?', 'And would you mind [watering] my plants?', 'Oh, and would you mind [feeding] my cat, too?',
  'Do you mind [if] I put your packages inside, too?', 'Would you mind [covering] my Saturday shift?', 'Do you mind [if] I tell her you suggested it?']),
 hear='*gonna* = going to: "I\'m **gonna** be away next week." • *wanna* = want to: "I **wanna** help, but I can\'t." You can say *going to* and *want to*. Say *Would you mind…?* and *Do you mind if I…?* smoothly, with a friendly rise at the end. Answer with a thumbs-up: *No, not at all!*',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: *Would you mind* + *-ing*?

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Would you mind** | **getting** my mail? | ‖ | No, **not at all**. | I**'ll** do it. |
| ^ | ^ | ‖ | **Sorry**, I **can't**. | I'll be away too. |
| **Would you mind** | **covering** my shift? | ‖ | No, **not at all**. | I'm free on Saturday. |
| **Would you mind** | **lending** me a ladder? | ‖ | No problem. | You can borrow **mine**. |

### Grammar Box 2: permission: *Do you mind if I…?*

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Do you mind if I** | **open** the window? | ‖ | No, **go ahead**. | It's hot in here. |
| **Do you mind if I** | **leave** early today? | ‖ | **Sorry**, | we need you until 5:00. |
| **Do you mind if I** | **switch** my Friday shift? | ‖ | No, **not at all**. | Ask the supervisor first. |
''',
rule='After ***Would you mind***, use **-ing** (*getting, covering*). After ***Do you mind if I***, use the base verb (*open, leave*). The answer **No** means "No problem. I\'ll help." / "Yes, you can."',
explain='''
### Grammar Box 3: saying yes, saying no

| YOU CAN HELP (say *no*!) | YOU CAN'T HELP (be polite) |
|---|---|
| *No, not at all.* • *No problem.* • *Sure, I'll do it.* | *Sorry, I can't, because…* + another idea: *Why don't you ask Lina?* |

### Grammar Box 4: how polite?

| | WHEN? | EXAMPLE |
|---|---|---|
| *Can you…?* | a small favor, a friend | *Can you pass the salt?* |
| *Could you…?* | more polite | *Could you help me with this box?* |
| *Would you mind …ing?* | the most polite; a **bigger** favor | *Would you mind feeding my cat for a week?* |
''',
qa=[('Someone asks *Would you mind helping me?* I want to help. Do I say *yes*?', 'No! Say ***No, not at all.*** *Mind* asks "Is it a problem?" *No* = no problem.'),
 ('*Would you mind to get* or *Would you mind getting*?', 'After *mind*, use *-ing*: ***Would you mind getting my mail?***'),
 ('How do I say no politely?', 'Say sorry, give a reason, and offer an idea: ***Sorry, I can\'t. I\'ll be away. Why don\'t you ask Lina?***')],
A=dict(head='Write the correct form of the verb.', items=['Would you mind [watering] my plants? (water)', 'Do you mind if I [open] the window? (open)',
 'Would you mind [feeding] the cat on Sunday? (feed)', 'Would you mind [switching] shifts with me? (switch)', 'Do you mind if I [borrow] your ladder? (borrow)',
 'Would you mind [getting] my packages? (get)']),
B=dict(head='Circle the correct words.', items=['Would you mind {{*covering|to cover}} my shift?', 'A: Would you mind helping me? B: {{*No, not at all.|Yes, I do.}} I\'ll help.',
 'Do you mind if I {{*leave|leaving}} early?', 'Could I borrow your pen? I forgot {{*mine|my}}.', 'Sorry, I can\'t. I {{*\'ll be|be}} away.',
 'I\'d like {{*to switch|switching}} my Friday shift.']),
mistakes=[('Would you mind to get my mail?', 'Would you mind **getting** my mail?'), ('Yes, I mind. I\'ll help you.', '**No, not at all.** I\'ll help you.'),
 ('Do you mind if I using your phone?', 'Do you mind if I **use** your phone?'), ('Can I borrow your?', 'Can I borrow **yours**?'),
 ('I like to switch my shift.', 'I**\'d** like to switch my shift.')],
tip='In many languages, a *yes* answer means "I\'ll help." But *Would you mind…?* asks "Is it a problem for you?", so in English **No** means "No problem." Spanish *¿Te importaría…? No, para nada* works the same way. What does your language do?')
L['talk'] = dict(pages=[('Favor Exchange', '''
### Round 1. Take a favor card and a "my week" card. Ask three people for your favor. Answer *No, not at all* or *Sorry, I can't, because…* and offer another idea. Write who said yes.

| FAVOR CARDS (invented) | |
|---|---|
| 1. get my mail for a week | 2. switch my Saturday shift |
| 3. lend me a ladder on Sunday | 4. water my plants on Friday |
| 5. feed my cat this weekend | 6. cover my Monday shift |
| 7. pick up my package today | 8. drive me to work on Tuesday |

| MY WEEK CARD | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---|---|---|---|---|---|---|---|
| Card A | free | busy | free | free | busy | away | away |
| Card B | busy | free | free | busy | free | free | busy |

*Example:* A: Would you mind getting my mail next week? B: No, not at all. I'm home all week. C: Sorry, I can't, because I'll be away. Why don't you ask Ana?

| I asked… | Yes or no? | Their reason or idea |
|---|---|---|
| 1. | | |
| 2. | | |
| 3. | | |
'''), ('Shift Switch Text', '''
### Round 2. Work with a partner. Write a 3-sentence text to a coworker. Confirm the shift switch: the day, the time, and thanks. Then read it to another pair.

*Example:* "Hi, Omar. Thanks for switching shifts with me! I'll work your Sunday shift (9:00–5:00), and you'll work my Friday shift (2:00–10:00). I've told Ms. Diaz, and she says it's OK."

| Our text |
|---|
| <br><br><br><br> |

| CHECK: does your text have…? | ✓ |
|---|---|
| the day and the time | ☐ |
| who works which shift | ☐ |
| thanks | ☐ |

*Useful:* Thanks for… • I'll work your… • You'll work my… • I've told the supervisor. • See you on…

*Remember:* every job has its own rules. Ask your supervisor first.
''')])
L['hw'] = dict(one=dict(head='Write the question or answer. Use the words.', example='you / mind / get / my mail? → *Would you mind getting my mail?*',
 items=[('you / mind / feed / my cat?', 'Would you mind feeding my cat?'), ('do you mind if I / leave / early?', 'Do you mind if I leave early?'),
  ('you / mind / cover / my shift / on Sunday?', 'Would you mind covering my shift on Sunday?'), ('a "yes, I\'ll help" answer: no / not / all', 'No, not at all.')]),
 three='''### 3. Write 3 favors you could ask a neighbor or a coworker. Then write a polite answer for each one.

| My favor (*Would you mind…?*) | A polite answer |
|---|---|
| 1. <br><br> | <br><br> |
| 2. <br><br> | <br><br> |
| 3. <br><br> | <br><br> |
''',
 four=dict(head='Review (Lesson 4). Write one word.', items=['[Why] don\'t you call the clinic?', 'You could [try] a heating pad.',
  'It\'s a good idea [to] get a flu shot every year.', 'I\'ve had a cough [since] Sunday.', 'She\'s had a rash [for] three days.']))
L['rw'] = dict(kind='notice', note='Read fast first. Then read again and answer the questions.', box_title='NOTICE · Maple Court Apartments + a note to a neighbor',
 text='''
**NOTICE: Packages.** Starting June 1, all packages will go to the new package room next to the mailroom. You will get a text with a code when a package arrives. Please pick up your packages within 5 days. If you are going to be away, you can ask a neighbor to pick them up for you. Your neighbor must show your text with the code. Questions? Call the office at (555) 210-4400.

**A NOTE on the door of apartment 3B:**

Hi, Ms. Lee! This is Tomás from 3A. I'm going to be away from June 10 to June 17. Would you mind picking up my packages from the package room? I'll text you the codes. Also, would you mind feeding my cat, Luna, in the evening? Her food is in the kitchen. My spare key will be in an envelope under your door on Sunday. Thank you so much! I owe you one. If you ever need help, just ask. Tomás
''',
 qs=[('Where will all packages go?', 'To the new package room next to the mailroom.', 'the new package room next to the mailroom'),
  ('When must you pick up a package?', 'Within 5 days.', 'within 5 days'),
  ('What must a neighbor show?', 'Your text with the code.', 'Your neighbor must show your text with the code'),
  ('When will Tomás be away?', 'From June 10 to June 17.', 'from June 10 to June 17'),
  ('Where will the spare key be?', 'In an envelope under Ms. Lee\'s door (on Sunday).', 'in an envelope under your door on Sunday')],
 write_head='Write a note to a neighbor (5–8 sentences). Ask for a favor while you\'re away: the dates, what to do, where the key is, thanks, and an offer to help back.',
 write_short='your note',
 example='*Hi, Mr. Ruiz! I\'m going to be away from May 3 to May 8. Would you mind getting my mail? Also, would you mind watering my plants on Wednesday? My spare key will be under your door on Friday. Thank you so much! If you ever need help, just ask. Ana (2C)*',
 box_label='My note', checklist=['It has 5–8 sentences.', 'It has the dates.', 'It has *Would you mind…?* + *-ing*.', 'It has thanks and an offer to help back.'])
L['exit'] = dict(q='Ask a classmate for a favor with *Would you mind…?*', s1='your question (*Would you mind…?*)', s2='their answer',
 s3='the reason, with *because*', key='*A good answer:* "Would you mind helping me with my homework? No, not at all. I\'m asking because the last question is hard."')
L['game'] = ('Favor or no favor?', 'A points to a picture and asks, "Would you mind **getting the mail**?" B gives a thumbs-up and says, "No, not at all," or says, "Sorry, I can\'t, because…" Switch.')
L['opening'] = dict(cards=['**A:** I sit all day at work. Any ideas?', '**A:** I\'m always tired in the afternoon. What can I do?', '**A:** What\'s a good idea for a healthy lunch?', '**A:** How often is it a good idea to get a checkup?'],
 follow='Why? • Have you ever tried it? • How long have you…?', hw_head='Write your partner\'s name and one good idea from Homework item 3.', hw_cols=['My partner\'s name', 'A good idea (*It\'s a good idea to…*)'])
L['notes'] = [
 '**No = yes:** practice the answer first, with a thumbs-up: *No, not at all!* Learners often say *Yes* and mean "I\'ll help." Smile and model it again.',
 '**Invented details:** all favor cards, keys, names, and addresses are invented. Learners never share real addresses or where they keep a key.',
 '**Shift switches:** every employer has its own rules. Add "Ask your supervisor first." It is printed on the Shift Switch Text page.',
 '***mind* + -ing:** *Would you mind getting…?* But *Do you mind if I* + the base verb: *Do you mind if I leave…?*',
 '**Saying no:** model *sorry + a reason + another idea*. A polite no is a good answer.',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening has *gonna* and *wanna*. Learners need to understand them; they can always say *going to* and *want to*.']
