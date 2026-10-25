import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=3, week=3, title='Have You Finished Yet?',
topic='At work: checking what is done and not done, an end-of-shift handoff, and a short, positive check-in with a supervisor. Learners use *already*, *yet*, and *just* and write an update email.',
cq='Is it done? Did it happen a minute ago? Is it a question or a *not* sentence?',
builds=[
 ('*Have you ever…?* and *have / has* + a past participle', 'Level 4 Lessons 1–2', '***already / yet / just*** with the present perfect: *Have you cleaned it yet? → Yes, I\'ve already cleaned it.*'),
 ('Object pronouns *it / them*', 'Level 3 Lesson 2', '*it / them* in short answers: *I\'ve restocked **them**. I haven\'t cleaned **it** yet.*'),
 ('Simple past with a time: *I finished at 3:00.*', 'Level 3 Lessons 2–4', '**Present perfect → simple past** for the time: *I\'ve finished the orders. I finished them at 3:00.*'),
],
objectives=['say what they\'ve already done and what they\'ve just done',
 'ask *Have you… yet?* and answer *Yes, I\'ve already… / No, not yet.*',
 'put *already*, *just*, and *yet* in the right place',
 'answer a supervisor\'s check-in questions in 3 sentences',
 'write a reply email (5–8 sentences) about what is done and not done yet'],
materials=['Board and markers; a 5-line checklist drawn on the board', 'Talk Time Cards A and B (in the workbook); 3 check-in question cards per group (copy them from the Talk Time page onto index cards, optional)',
 'A folder for each learner for the writing checks (Writing Check 1 is tonight)'],
prep='15 minutes (read the plan; draw the checklist; practice reading the listening script)',
words=[('to-do list', 'to_do_list', True), ('task', 'task', True), ('checklist', 'checklist', True), ('supervisor', 'supervisor', True), ('deadline', 'deadline', True),
 ('restock', 'restock', True), ('inventory', 'inventory', True), ('clock in', 'clock_in', True), ('clock out', 'clock_out', True), ('break room', 'break_room', True),
 ('feedback', 'feedback', True), ('check-in (a short meeting)', 'check_in', False)],
more_vocab='*Also:* a shift, a delivery, put away, a cooler, an aisle, a time clock, a training, a reminder, a handoff, a coworker.',
clock=clock('', ' (+ My Words)', '', '*already / yet / just* with the present perfect', 'Shift Handoff + Check-in', 'An email from a supervisor + a reply (Writing Check 1)',
 talk_group='Pairs, then groups of 3'),
attend='With 5 or fewer, do Shift Handoff in pairs (or one group of 3, taking turns), and in the Check-in you play the supervisor first. Late arrivals join any pair and take Card B.',
)
L['steps'] = [
 step1('Opening Talk', '*How long have you…?* and *for / since*',
  'you ask, "How long have you lived in this city?" The learner answers with *for* or *since*. Then you ask, "Where did you live before? How long did you live there?" Help them say 3 sentences.',
  'Pairs compare Homework item 1 (*for / since* sentences) and read one answer from item 3 to each other. Then they fill in the box on the Opening Talk page.',
  '*I live here since 2020* (→ *I\'ve lived here since 2020*) and *since three years* (→ *for three years*)'),
 step2('*to-do list* (things to do) vs. *checklist* (a list with boxes to tick ✓); *restock* (put more on the shelves); *inventory* (count what you have); *clock in / clock out* (start and end work; mime a time clock); *deadline* (the last day); *feedback* (what a supervisor says about your work); *check-in* (a short meeting).',
  'ask "Is a deadline the first day or the last day?" (the last day) • "Do you clock in at the start or the end of your shift?" (the start) • "Is *Great job!* feedback?" (yes, positive feedback).',
  'Have you clocked in yet? → Yes, I\'ve already clocked in.'),
 step3('It\'s the end of the evening shift at a grocery store. Ms. Rivera, the supervisor, talks to two workers, Jamal and Kim. Listen: is all the work finished?',
  'Point to the script lines. *gonna* = going to: "I\'m **going to** clean it before I clock out." *wanna* = want to: "I **want to** finish it this week." Then practice hearing *\'s* = *has*: *It\'s just arrived* (= it has just arrived), the weak *have* in *Have you… yet?*, and the stress: *I\'ve JUST finished it.* • *I\'ve alREADY restocked them.*', '{EST}'),
 step4('*already / yet / just*', 'draw a checklist on the board with 5 tasks. Tick two and say, "I\'ve **already** restocked the shelves. I\'ve **already** clocked in." Tick one now, in front of the class: "I\'ve **just** cleaned the board." Point to an empty box: "I **haven\'t** checked the inventory **yet**."',
  'Box 1: read across: *Have you cleaned the break room yet? → Yes, I\'ve already cleaned it. / No, not yet.* Box 2: add a time → simple past: *I finished them at 3:00.* Box 3: word place (*already* and *just* before the past participle; *yet* at the end). Box 4: which one?',
  '"*I\'ve finished it yesterday.* Right or wrong?" (wrong: *I finished it yesterday.*) • "Where does *yet* go?" (at the end) • "*It\'s just arrived.* *It\'s* = it is or it has?" (it has).',
  'A reads a task from the board checklist and asks *Have you… yet?* B answers *Yes, I\'ve already… / I\'ve just… / No, not yet.* Switch.'),
 brk('*Have you… yet? → Yes, I\'ve already… / I\'ve just… / No, not yet. I haven\'t… yet.*'),
 step5('Shift Handoff + Check-in', 'hold up Card A and ask a learner to ask you, "Have you restocked aisle 3 yet?" Answer, "Yes, I\'ve already restocked it." Then point to a task with no tick: "No, not yet. I\'m going to do it before I clock out." Say: "Answer, then add one more sentence."',
  '**Shift Handoff (pairs, information gap).** A looks at Card A; B covers it. B asks *Have you… yet?* about each task and ticks *done* or *not yet* in the notes. Then switch: A asks about Card B.',
  '**Check-in (groups of 3).** The supervisor reads the 3 question cards. The worker answers with *already* and *yet* (invented answers are fine). The observer ticks each *already / yet / just* they hear. Rotate roles so everyone is the worker once.',
  'pairs for round 1; then 5 groups of 3 for round 2.', 'pairs for round 1; then 2 groups for round 2 (the group of 4 has two workers).',
  'pairs (or one group of 3) for round 1. In round 2, you play the supervisor first; then learners take turns.'),
 step6('An email from a supervisor + a reply', 'Learners read the email from Sandra on the Read & Write page and answer the questions.',
  'Learners write a reply email (5–8 sentences): what they\'ve already done, what they haven\'t done yet, when they\'ll finish it, and one question. Show the example. Invented details are fine. This is **Writing Check 1**: collect it.'),
 step7('What have you done this week, and what haven\'t you done yet?', 'I\'ve already paid my phone bill. I haven\'t done my laundry yet. I haven\'t done it because I worked late every night.',
  'item 1: *you / finish / the checklist / yet? → Have you finished the checklist yet?*'),
]
L['listen'] = dict(title='Have You Finished Yet?', voices={'Narrator': 'N', 'Ms. Rivera': 'Rosa', 'Jamal': 'Sam', 'Kim': 'Kim'},
 female=['Narrator', 'Ms. Rivera', 'Kim'], names=['Rivera', 'Jamal', 'Kim'], tts={'Thank you, Ms Rivera. I will see you tomorrow.': 'Thank you, Miss Rivera. I will see you tomorrow.'},
 setting='It\'s the end of the evening shift at a grocery store. Ms. Rivera, the night supervisor, checks the work with Jamal and Kim.',
 intro='Lesson three. It\'s the end of the evening shift at a grocery store. Ms. Rivera, the supervisor, talks to Jamal and Kim.',
 lines=[
  ('Ms. Rivera', 'OK, team, it\'s almost nine. Let\'s look at the checklist. Jamal, have you restocked the shelves yet?'),
  ('Jamal', 'Yes, I\'ve already restocked them. Those shelves are done.'),
  ('Ms. Rivera', 'Great. And the delivery? Has the truck arrived yet?'),
  ('Jamal', 'Yes, it\'s just arrived. Kim and I are putting it away.'),
  ('Kim', 'We have already put away the milk and the eggs.'),
  ('Ms. Rivera', 'Good. Kim, have you cleaned the cooler yet?'),
  ('Kim', 'No, not yet. I haven\'t cleaned it yet. The delivery came late.'),
  ('Ms. Rivera', 'That\'s OK. Are you going to have time tonight?'),
  ('Kim', 'I think so. I\'m going to start it after the delivery. It takes about twenty minutes.'),
  ('Ms. Rivera', 'Perfect. Jamal, have you checked the bakery inventory?'),
  ('Jamal', 'I\'ve just finished it. I gave you the list at eight.'),
  ('Ms. Rivera', 'Oh, right, I have it here. Thanks. And the break room?'),
  ('Jamal', 'Not yet. I\'m going to clean it before I clock out.'),
  ('Ms. Rivera', 'OK. So the cooler and the break room aren\'t done yet. Everything else is done.'),
  ('Kim', 'Ms. Rivera, have you seen the new training schedule yet?'),
  ('Ms. Rivera', 'Yes, I\'ve just seen it. The deadline for the safety training is Friday.'),
  ('Kim', 'Thanks. I want to finish it this week.'),
  ('Ms. Rivera', 'Good idea. And some quick feedback: you both did great work tonight. The shelves look really good.'),
  ('Jamal', 'Thank you. That means a lot.'),
  ('Kim', 'Thank you, Ms Rivera. I will see you tomorrow.'),
 ],
 A=dict(q='Is all the work finished?', opts=['Yes, everything is done.', 'No, two things aren\'t done yet.', 'No, nothing is done yet.'], ans=1),
 B=dict(head='Look at the checklist. Circle *done* or *not yet*.', kind='choice', items=[
  dict(s='restock the shelves: {{*done|not yet}}', ev='I\'ve already restocked them'),
  dict(s='put away the milk and the eggs: {{*done|not yet}}', ev='We have already put away the milk and the eggs'),
  dict(s='clean the cooler: {{done|*not yet}}', ev='I haven\'t cleaned it yet'),
  dict(s='check the bakery inventory: {{*done|not yet}}', ev='I\'ve just finished it'),
  dict(s='clean the break room: {{done|*not yet}}', ev='Not yet. I\'m going to clean it before I clock out'),
  dict(s='Kim\'s safety training: {{done|*not yet}}', ev='I want to finish it this week'),
 ]),
 C=dict(head='Write *already*, *yet*, or *just*.', items=[
  'Yes, I\'ve [already] restocked them.', 'Has the truck arrived [yet]?', 'Yes, it\'s [just] arrived.',
  'I haven\'t cleaned it [yet].', 'I\'ve [just] finished it.', 'We have [already] put away the milk and the eggs.']),
 hear='*gonna* = going to: "I\'m **going to** clean it before I clock out." • *wanna* = want to: "I **want to** finish it this week." You can say *going to* and *want to*. Listen for *\'s* = *has*: *It\'s just arrived.* Say it with stress: *I\'ve JUST finished it.* • *I\'ve alREADY restocked them.*',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: *already / yet / just*

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Have** you | cleaned the break room **yet**? | ‖ | Yes, I **have**. | I**'ve already** cleaned it. |
| ^ | ^ | ‖ | No, **not yet**. | I **haven't** cleaned it **yet**. |
| **Has** the truck | arrived **yet**? | ‖ | Yes, it **has**. | It**'s just** arrived. |
| **Have** they | restocked the shelves **yet**? | ‖ | Yes, they **have**. | They**'ve already** restocked them. |
| **Has** she | finished the training **yet**? | ‖ | No, she **hasn't**. | She**'s going to** finish it on Friday. |

### Grammar Box 2: done → when? (simple past)

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Have** you | finished the orders? | ‖ | Yes, I **have**. | I**'ve finished** them. |
| **When did** you | finish them? | ‖ | I **finished** them | at 3:00. / an hour ago. |
| **What have** you | done this week? | ‖ | I**'ve checked** the inventory, | and I**'ve cleaned** the cooler. |
''',
rule='***already*** = done (maybe sooner than expected). ***yet*** = in questions and *not* sentences, at the end. ***just*** = a very short time ago. Add a time (*at 3:00, yesterday*) → simple past.',
explain='''
### Grammar Box 3: word place

| WORD | WHERE? | EXAMPLE |
|---|---|---|
| ***already*** | before the past participle | *I've **already** cleaned it.* |
| ***just*** | before the past participle | *The truck has **just** arrived.* |
| ***yet*** | at the end (questions and *not*) | *Have you finished **yet**? I haven't finished **yet**.* |
| ***it / them*** | after the verb | *the cooler → I've cleaned **it**. the shelves → I've restocked **them**.* |

### Grammar Box 4: Which one?

| | WHEN? | EXAMPLE |
|---|---|---|
| *have / has* + past participle | it is done (or not done); **no time** | *I've finished the orders. I haven't called her yet.* |
| simple past | a **finished time** (*at 3:00, yesterday, an hour ago*) | *I finished the orders at 3:00.* |
''',
qa=[('Can I say *I\'ve finished it yesterday*?', 'No. With a finished time, use the simple past: ***I finished it yesterday.***'),
 ('Where does *yet* go?', 'At the end: ***Have you clocked out yet? I haven\'t clocked out yet.***'),
 ('What does *It\'s just arrived* mean?', '*It\'s* = ***it has***. *just* = a very short time ago. The truck arrived a minute ago.')],
A=dict(head='Write *already*, *yet*, or *just*.', items=['Have you clocked out [yet]?', 'The truck arrived one minute ago. It has [just] arrived.',
 'She hasn\'t restocked the shelves [yet].', 'Has the supervisor given you feedback [yet]?', 'The deadline is Friday, but I\'ve [already] finished the training. It\'s only Monday!',
 'I can\'t talk now. I\'ve [just] clocked in, and I need to start work.']),
B=dict(head='Circle the correct words.', items=['I {{*haven\'t|didn\'t}} cleaned the cooler yet.', 'I {{*finished|\'ve finished}} the inventory at 8:00.',
 'The shelves? Yes, I\'ve restocked {{*them|it}}.', '{{*Has|Have}} the truck arrived yet?', 'The delivery {{*has just|just has}} arrived.',
 'When {{*did you clock in|have you clocked in}}?']),
mistakes=[('I\'ve finished it yesterday.', 'I **finished** it yesterday.'), ('I didn\'t finish yet.', 'I **haven\'t finished** yet.'),
 ('Have you yet finished?', 'Have you finished **yet**?'), ('I have already clean it.', 'I\'ve already **cleaned** it.'),
 ('Has arrived the truck?', '**Has the truck** arrived?')],
tip='Spanish *ya* can mean *already* (*Ya terminé* = *I\'ve already finished*) and *yet* in questions (*¿Ya terminaste?* = *Have you finished yet?*). *Todavía no* = *not yet*. In English, *yet* goes at the end. What does your language do?')
CARD = lambda rows: '\n'.join(f'| {t} | {d} |' for t, d in rows)
CARD2 = lambda a, b: '\n'.join(f'| {t} | {d} | {u} | {e} |' for (t, d), (u, e) in zip(a, b))
NOTES = lambda rows: '\n'.join(f'| {t} | ☐ done ☐ not yet |' for t in rows)
A_ = [('restock aisle 3', '✓ done'), ('clean the break room', 'not yet'), ('check the bakery inventory', '✓ done'), ('put away the delivery', '✓ done'), ('empty the trash', 'not yet'), ('write the end-of-shift note', 'not yet')]
B_ = [('count the cash register', '✓ done'), ('clean the cooler', 'not yet'), ('fill the ice machine', '✓ done'), ('mop the floor', '✓ done'), ('call the morning supervisor', 'not yet'), ('turn off the lights in the back', 'not yet')]
L['talk'] = dict(pages=[('Shift Handoff', '''
### Round 1. A looks at Card A. B covers it. B asks *Have you… yet?* and ticks the notes. Then switch: A asks about Card B.

*Example:* B: Have you restocked aisle 3 yet? A: Yes, I've already restocked it. B: Have you cleaned the break room yet? A: No, not yet. I'm going to clean it at 8:00.

| CARD A (A's shift) | | CARD B (B's shift) | |
|---|---|---|---|
''' + CARD2(A_, B_) + '''

| My notes about my partner's shift | |
|---|---|
''' + NOTES(['task 1', 'task 2', 'task 3', 'task 4', 'task 5', 'task 6']) + '''
'''), ('Check-in', '''
### Round 2. Work in a group of 3: a supervisor, a worker, and an observer. The supervisor asks the 3 questions. The worker answers in 3 sentences. The observer ticks the words. Then rotate.

| SUPERVISOR: question cards |
|---|
| 1. What have you done this week? |
| 2. Have you finished the training yet? |
| 3. What's one thing you'd like to learn? |

| OBSERVER: tick each word you hear | Worker 1 | Worker 2 | Worker 3 |
|---|---|---|---|
| *already* | ☐ | ☐ | ☐ |
| *yet* | ☐ | ☐ | ☐ |
| *just* | ☐ | ☐ | ☐ |
| 3 sentences? | ☐ | ☐ | ☐ |

*Example (worker):* "This week I've already restocked the drinks aisle, and I've trained a new coworker. I haven't finished the safety training yet. I'm going to do it on Thursday because the deadline is Friday."

| My answer to question 1 (*I've already… / I haven't… yet*) |
|---|
| <br><br><br> |

*Useful (supervisor):* Great job! • Thanks for your hard work. • When are you going to finish it? • Let me know if you need help.
''')])
L['hw'] = dict(one=dict(head='Write the sentence. Use the words.', example='I / already / clean / the break room → *I\'ve already cleaned the break room.*',
 items=[('you / finish / the checklist / yet?', 'Have you finished the checklist yet?'), ('she / not / clock out / yet', 'She hasn\'t clocked out yet.'),
  ('the truck / just / arrive', 'The truck has just arrived.'), ('we / already / restock / the shelves', 'We\'ve already restocked the shelves.')]),
 three='''### 3. Make a to-do list for this week (at home or at work). Write 3 things you've already done and 2 things you haven't done yet.

| I've already… | I haven't… yet. |
|---|---|
| 1. <br><br> | 1. <br><br> |
| 2. <br><br> | 2. <br><br> |
| 3. <br><br> | <br> |
''',
 four=dict(head='Review (object pronouns). Write *it* or *them*.', items=['The shelves are empty. Can you restock [them]?', 'I\'ve cleaned the cooler. I cleaned [it] at 8:00.',
  'Where are the boxes? I put [them] in the back room.', 'The checklist? I gave [it] to Ms. Rivera.', 'My coworkers are great. I like [them] a lot.']))
L['rw'] = dict(kind='email', note='Read fast first. Then read again and answer the questions.', box_title='EMAIL · From: Sandra Ortiz (Supervisor) · Subject: This week\'s checklist',
 text='''
**To:** Evening team • Hi, team! Thank you for a busy week! The store looks great, and two customers have already written nice comments about the clean aisles.

Here is the checklist for this week. Please reply by Thursday and tell me what you've done and what you haven't done yet.

**Weekly checklist:** ☐ Restock the drinks aisle every night. ☐ Check the inventory in the back room (by Wednesday). ☐ Clean the break room fridge (Friday). ☐ Finish the online safety training.

**Reminder:** the deadline for the safety training is Friday, May 16. It takes about 45 minutes. You can do it on the computer in the break room before you clock in. If you have already finished it, thank you! You don't need to do it again.

Also, our new schedule has just arrived. It's on the wall next to the time clock. Please check your days for next week.

See you tonight, Sandra
''',
 qs=[('Who is the email to?', 'The evening team.', 'To: Evening team'),
  ('When should the workers reply?', 'By Thursday.', 'Please reply by Thursday'),
  ('What is the deadline for the safety training?', 'Friday, May 16.', 'the deadline for the safety training is Friday, May 16'),
  ('Where can workers do the training?', 'On the computer in the break room.', 'on the computer in the break room'),
  ('What has just arrived?', 'The new schedule.', 'our new schedule has just arrived')],
 write_head='Write a reply email to Sandra (5–8 sentences). Say what you\'ve already done, what you haven\'t done yet, when you\'ll finish it, and ask one question.',
 write_short='your reply email',
 example='*Hi, Sandra. Thank you for the checklist. I\'ve already restocked the drinks aisle, and I\'ve checked the inventory in the back room. I haven\'t cleaned the break room fridge yet because that\'s on Friday. I\'m going to finish the safety training on Thursday before I clock in. Can I do it on my phone? Thanks, Leo*',
 box_label='My email', checklist=['It has 5–8 sentences.', 'It has something I\'ve already done (*already*).', 'It has something I haven\'t done yet (*yet*).', 'It has a question.'])
L['exit'] = dict(q='What have you done this week, and what haven\'t you done yet?', s1='something you\'ve already done (*already*)', s2='something you haven\'t done yet (*yet*)',
 s3='a reason, with *because*', key='*A good answer:* "I\'ve already paid my phone bill. I haven\'t done my laundry yet. I haven\'t done it because I worked late every night."')
L['game'] = ('Done or not yet?', 'A points to a picture and asks, "Have you **clocked in** yet?" B answers, "Yes, I\'ve already clocked in." or "No, not yet." Switch.')
L['opening'] = dict(cards=['**A:** How long have you lived in this city?', '**A:** How long have you had your phone?', '**A:** How long have you known your best friend?', '**A:** How long have you studied English?'],
 follow='When did you…? • Where did you… before? • Why?', hw_head='Write your partner\'s name and one *How long…?* answer.', hw_cols=['My partner\'s name', 'How long? (*for / since*)'])
L['notes'] = [
 '**Keep work talk positive and invented.** Learners never discuss real problems with real bosses or coworkers. Any job works in the role plays; invented answers are fine.',
 '**The board checklist:** keep it up all night. A tick = *already* (or *just*, if you tick it now); an empty box = *not yet*.',
 '**Word place:** teach *already* before the past participle. In speaking, *I\'ve cleaned it already* is also common; accept it. *yet* always goes at the end.',
 '**\'s = has:** *It\'s just arrived. She\'s already left.* Ask: "*is* or *has*?" If a past participle comes next, it is *has*.',
 '**Writing Check 1:** collect the reply emails. Write one strength and one fix on each (for example, the place of *yet*). Return them next week; learners keep them in a folder to see progress. No scores.',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening says *going to* and *want to*. People often say *gonna* and *wanna*. Learners only need to recognize the short forms; they can always say the full forms.']
