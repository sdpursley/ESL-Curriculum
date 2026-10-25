import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=7, week=7, title='Too Early or On Time?',
topic='Expectations at work and in the community: being on time, dress codes and safety rules, invitations (RSVP, what to bring), and comparing customs respectfully. Learners use *too* and *enough*, *too much / too many*, and *must / mustn\'t / don\'t have to*. The company, the rules, and the people are invented.',
cq='Is it OK, too much, or not enough?',
builds=[
 ('*too small* as a fixed phrase; adjectives', 'Level 3', '***too* + adjective** and **adjective + *enough***: *too casual, not formal enough*'),
 ('count and noncount nouns', 'Level 2', '***too much / too many / enough*** + a noun: *too many people, enough time*'),
 ('*have to / don\'t have to*', 'Level 2', '***must / mustn\'t*** for rules, and *don\'t have to* = not necessary'),
],
objectives=['say what is too early, too late, or on time',
 'use *too* + adjective and adjective + *enough* (*too casual, safe enough*)',
 'use *too much / too many / enough* + a noun',
 'explain a workplace rule with *must / mustn\'t / don\'t have to*',
 'compare customs politely and write first-week tips for a new coworker (5–8 sentences)'],
materials=['Board and markers', 'Customs question cards and the dress code rule card (in the workbook Talk Time pages; copy them onto index cards, optional)', 'A clock or a phone with the time (optional, for the warm-up)'],
prep='15 minutes (read the plan; practice reading the listening script; practice *mustn\'t* (no first *t*) and *eNOUGH*)',
words=[('on time', 'on_time', True), ('early', 'early', True), ('late', 'late', True), ('dress code', 'dress_code', True), ('uniform', 'uniform', True),
 ('casual', 'casual', True), ('formal', 'formal', True), ('closed-toe shoes', 'closed_toe_shoes', True), ('name badge', 'name_badge', True), ('invitation', 'invitation', True),
 ('RSVP', 'rsvp', True), ('host', 'host', False)],
more_vocab='*Also:* an apron, sandals, jewelry, a front counter, a handbook, attendance, a custom, a hometown, a guest, take off (shoes).',
clock=clock('', ' (+ My Words)', '', '*too / enough; too much / too many; must / mustn\'t / don\'t have to*', 'Customs Compare + Dress Code Check', 'An employee handbook page; first-week tips',
 talk_group='Groups, then pairs'),
attend='With 5 or fewer, do Customs Compare as one group, then Dress Code Check in pairs (you join if there is an odd number). Late arrivals join a group and answer the next card.',
)
L['steps'] = [
 step1('Opening Talk', 'imaginary situations: *What would you do if…? / If I had…, I\'d…*',
  'you say, "What would you do if you found $50 at work?" The learner answers with *If I found…, I\'d…* Then you ask, "Why?" Help them say 3 sentences.',
  'Pairs compare Homework item 1 (*If I had…, I\'d…*) and read their 3 dreams (item 3) to each other. Then they fill in the box on the Opening Talk page.',
  '*If I would have time…* (→ *If I had time…*) and *If I found $50, I will…* (→ *I\'d…*)'),
 step2('*on time*, *early*, *late* (draw a clock: 6:50, 7:00, 7:20); *dress code* (the rules about clothes); *uniform*; *casual* (T-shirt, jeans) vs. *formal* (a shirt and tie); *closed-toe shoes* (point to a sneaker, then mime a sandal: "no"); *name badge*; *invitation* (a party card); *RSVP* (tell the host "yes" or "no"); *host* (the person who has the party).',
  'ask "Is a T-shirt casual or formal?" (casual) • "Are sandals closed-toe shoes?" (no) • "If an invitation says *RSVP by Friday*, what do you do?" (tell the host by Friday).',
  'Jeans are too casual for an interview.'),
 step3('It\'s Nadia\'s first week at a bakery. She asks her coworker, Carmen, about the rules. Then the supervisor, Mr. Brooks, comes in. Listen: what are they talking about?',
  'Point to the script lines. *wanna* = want to: "What do you **want to** know?" *gonna* = going to: "I\'m **going to** buy some today." Then practice *too / two / to* (the same sound) and the stress in *TOO late* and *not eNOUGH*.', '{EST}'),
 step4('*too / enough; must / mustn\'t / don\'t have to*', 'draw a clock at 7:10. Say, "My shift starts at 7:00. 7:10 is **too late**." Draw 6:55: "6:55 is **early enough**." Write: *too* = more than OK (a problem); *enough* = OK. Then show a sandal or mime one: "In a kitchen, you **must** wear closed-toe shoes. You **mustn\'t** wear sandals. You **don\'t have to** wear a tie."',
  'Box 1: read across: *Are jeans OK for the interview? → No, they\'re too casual. / They aren\'t formal enough.* Box 2: *too much / too many / enough* + a noun. Box 3: *must / mustn\'t / don\'t have to*. Box 4: comparing customs.',
  '"*enough early* or *early enough*?" (*early enough*) • "*too much people* or *too many people*?" (*too many people*) • "Is a tie a rule here?" (no) "So: *You mustn\'t wear a tie* or *You don\'t have to wear a tie*?" (*don\'t have to*).',
  'A points to a picture and asks, "Are sandals OK for the kitchen?" B answers with *too* or *enough* and a rule with *must / mustn\'t*. Switch.'),
 brk('*too late / early enough • too much work / too many people / enough time • must / mustn\'t (a rule) / don\'t have to (not necessary)*'),
 step5('Customs Compare + Dress Code Check', 'read a card: "A party starts at 7:00. When do people arrive in your hometown?" Help a learner say, "In my hometown, people usually arrive at 8:00, but here many people arrive at 7:15." Say: "Describe; don\'t judge. No place is better."',
  '**Customs Compare (groups).** One person reads a question card. Each person answers. The group writes 2 sentences with *In my hometown…, but here…* No place is "better."',
  '**Dress Code Check (pairs).** Pairs read the rule card and the 6 workers. For each worker, they say *too casual*, *not safe enough*, or *OK*, and the rule with *must / mustn\'t / don\'t have to*.',
  '5 groups of 3 for round 1; then pairs.', '2 groups for round 1; then pairs.',
  'one group for round 1; then pairs (you join if there is an odd number).'),
 step6('An employee handbook page', 'Learners read the handbook page on the Read & Write page and answer the questions.',
  'Learners write "Tips for your first week" for a new coworker (5–8 sentences) with *must*, *don\'t have to*, *too*, and *enough*. Show the example. **Writing check 2:** collect this writing and write one strength and one fix.'),
 step7('What is one custom here that is different from your hometown (or another place you know)?', 'Here, people usually arrive on time for a doctor\'s appointment. In my hometown, people often arrive a little late. I like the custom here because I don\'t wait a long time.',
  'item 1: *6:55 / early / for a 7:00 shift? (enough) → Is 6:55 early enough for a 7:00 shift?*'),
]
L['listen'] = dict(title='Too Early or On Time?', voices={'Narrator': 'N', 'Nadia': 'Ana_af_jessica', 'Carmen': 'Rosa', 'Mr. Brooks': 'Carlos'},
 female=['Narrator', 'Nadia', 'Carmen'], names=['Nadia', 'Carmen', 'Brooks'], tts={},
 setting='It\'s Nadia\'s first week at a bakery. She asks her coworker, Carmen, about the rules. Then the supervisor, Mr. Brooks, joins them.',
 intro='Lesson seven. It\'s Nadia\'s first week at a bakery. She asks her coworker, Carmen, some questions.',
 lines=[
  ('Nadia', 'Carmen, can I ask you a few questions? I\'m still learning the rules.'),
  ('Carmen', 'Sure, Nadia. What do you want to know?'),
  ('Nadia', 'My shift starts at seven. Is six fifty-five early enough?'),
  ('Carmen', 'Yes, that\'s perfect. Here, on time means five minutes early. Seven ten is too late.'),
  ('Nadia', 'OK. And what about the uniform? Do I have to wear the hat?'),
  ('Carmen', 'Yes, you must wear the hat and the apron in the kitchen. But you don\'t have to wear them in the break room.'),
  ('Nadia', 'Got it. What about my phone?'),
  ('Carmen', 'You mustn\'t use your phone in the kitchen. You can use it on your break.'),
  ('Nadia', 'And are these shoes OK? They\'re new.'),
  ('Carmen', 'Hmm, those are sandals. They aren\'t safe enough for the kitchen.'),
  ('Mr. Brooks', 'Carmen\'s right. Good morning, Nadia. I\'m Mr. Brooks, the supervisor. You must wear closed-toe shoes. The trays are too hot, and the floor is sometimes wet.'),
  ('Nadia', 'I\'m sorry. I didn\'t know. I\'m going to buy some today.'),
  ('Mr. Brooks', 'That\'s OK. For today, there are extra shoes in the office. Maybe they\'re too big, but they\'re safe.'),
  ('Nadia', 'Thank you. Is there anything else?'),
  ('Mr. Brooks', 'Just one more thing. If you\'re going to be late, you must call me before your shift.'),
  ('Carmen', 'Don\'t worry, Nadia. Everyone makes mistakes in the first week. There\'s too much to remember!'),
  ('Nadia', 'That\'s true. Thanks, both of you.'),
 ],
 A=dict(q='What are they talking about?', opts=['the rules at work', 'a party invitation', 'a job interview'], ans=0),
 B=dict(head='Check the rules. Circle the answer.', kind='choice', items=[
  dict(s='On time means {{*five minutes early|exactly seven o\'clock}}.', ev='on time means five minutes early'),
  dict(s='In the kitchen, you {{*must|don\'t have to}} wear the hat and the apron.', ev='you must wear the hat and the apron in the kitchen'),
  dict(s='In the break room, you {{must|*don\'t have to}} wear them.', ev='But you don\'t have to wear them in the break room.'),
  dict(s='You {{must|*mustn\'t}} use your phone in the kitchen.', ev='You mustn\'t use your phone in the kitchen.'),
  dict(s='You {{*must|don\'t have to}} wear closed-toe shoes.', ev='You must wear closed-toe shoes.'),
  dict(s='If you\'re going to be late, you must {{*call Mr. Brooks|text Carmen}}.', ev='you must call me before your shift'),
 ]),
 C=dict(head='Write the missing word: *too*, *enough*, or *much*.', items=[
  'Is six fifty-five early [enough]?', 'Seven ten is [too] late.', 'They aren\'t safe [enough] for the kitchen.',
  'The trays are [too] hot, and the floor is sometimes wet.', 'Maybe they\'re [too] big, but they\'re safe.', 'There\'s too [much] to remember!']),
 hear='*wanna* = want to: "What do you **want to** know?" • *gonna* = going to: "I\'m **going to** buy some today." You can say *want to* and *going to*. *too*, *two*, and *to* sound the same: listen to the meaning. Stress: *TOO late* • *not eNOUGH*. In *mustn\'t*, you don\'t hear the first *t*.',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: *too* + adjective, adjective + *enough*

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Are** jeans OK | for the interview? | ‖ | No, they're **too casual**. | They **aren't formal enough**. |
| **Is** 6:55 | **early enough**? | ‖ | Yes, it's **early enough**. | That's perfect. |
| **Is** 7:10 OK | for a 7:00 shift? | ‖ | No, it's **too late**. | Come at 6:55. |
| **Are** sandals | **safe enough**? | ‖ | No, they **aren't safe enough**. | Wear closed-toe shoes. |

### Grammar Box 2: *too much / too many / enough* + a noun

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Do you have** | **enough** time? | ‖ | No, I have **too much** work. | I don't have **enough time**. |
| **Are there** | **enough** chairs? | ‖ | No, there are **too many** people. | We need more chairs. |
| **Do we have** | **enough** food? | ‖ | Yes, we have **enough** food. | Don't buy more. |
''',
rule='*too* = more than OK (a problem). *enough* = OK. *enough* goes **after** an adjective (*early enough*) and **before** a noun (*enough time*). *too many* + things you can count; *too much* + things you can\'t count.',
explain='''
### Grammar Box 3: *must / mustn't / don't have to*

| | MEANING | EXAMPLE |
|---|---|---|
| *must* | it's a rule; do it | *You must wear closed-toe shoes.* |
| *mustn't* | it's against the rules; don't do it | *You mustn't use your phone in the kitchen.* |
| *don't have to* | it's not necessary; you choose | *You don't have to wear a tie.* |

### Grammar Box 4: comparing customs

| TO SAY | EXAMPLE |
|---|---|
| *In my hometown…, but here…* | *In my hometown, guests usually bring food, but here people often ask the host first.* |
| *usually / often / sometimes* | *People usually arrive on time for work.* |
| describe; don't judge | *It's different. I like both.* |
''',
qa=[('*enough early* or *early enough*?', 'After an adjective: ***early enough***. Before a noun: ***enough time***.'),
 ('Are *mustn\'t* and *don\'t have to* the same?', 'No! ***mustn\'t*** = don\'t do it (it\'s a rule). ***don\'t have to*** = not necessary (you can if you want).'),
 ('*too much* or *too many*?', '***too many*** + things you can count (*people, chairs*). ***too much*** + things you can\'t count (*work, time, noise*).')],
A=dict(head='Write *too*, *much*, *many*, or *enough*.', items=['7:10 is [too] late for a 7:00 shift.', 'The room isn\'t big [enough] for 30 people.',
 'There are too [many] cars in the parking lot.', 'I have too [much] work today.', 'We don\'t have [enough] chairs.',
 'Jeans are [too] casual for an interview.']),
B=dict(head='Circle the correct words.', items=['You {{*mustn\'t|don\'t have to}} smoke in the building. (It\'s a rule.)', 'It\'s Friday. You {{mustn\'t|*don\'t have to}} wear a tie. (It\'s not necessary.)',
 'Is 6:55 {{*early enough|enough early}}?', 'There are too {{*many|much}} people here.', 'I don\'t have {{*enough time|time enough}}.',
 'Sandals {{*aren\'t safe enough|are too safe}} for the kitchen.']),
mistakes=[('It\'s enough big.', 'It\'s **big enough**.'), ('There are too much people.', 'There are too **many** people.'),
 ('You don\'t have to use your phone on the floor. (It\'s a rule.)', 'You **mustn\'t** use your phone on the floor.'), ('You must to wear a badge.', 'You must **wear** a badge.'),
 ('I have too many work.', 'I have too **much** work.')],
tip='Spanish *demasiado* covers *too* and *too much / too many*: *demasiado caro* = *too expensive*; *demasiada gente* = *too many people*. *Suficiente* = *enough*. English puts *enough* after an adjective: *big enough* (not *enough big*). What does your language do?')
L['talk'] = dict(pages=[('Customs Compare', '''
### Round 1. Work in groups. One person reads a question card. Each person answers. Then write 2 sentences with *In my hometown…, but here…* No place is "better."

| QUESTION CARDS | |
|---|---|
| 1. A party starts at 7:00. When do people arrive in your hometown? | 2. What do guests bring to a dinner? |
| 3. What do people wear to a job interview? | 4. How early do people arrive for work? |
| 5. Do people take off their shoes in a home? | 6. How do people answer an invitation? |

*Example:* A: A party starts at 7:00. When do people arrive in your hometown? B: In my hometown, people usually arrive at 8:00, but here many people arrive at 7:15. C: In my family, we're always on time!

| Card | In my hometown… | Here… |
|---|---|---|
| | | |
| | | |

| Our 2 sentences (*In my hometown…, but here…*) |
|---|
| 1. <br><br> |
| 2. <br><br> |

*Remember:* customs are different in every country, every city, and every family. Describe; don't judge.
'''), ('Dress Code Check', '''
### Round 2. Work with a partner. Read the rule card. For each worker, say *too casual*, *not safe enough*, or *OK*. Then say the rule with *must / mustn't / don't have to*.

| RIVERSIDE KITCHEN · DRESS CODE (invented) | |
|---|---|
| **Kitchen:** You must wear closed-toe shoes and a hat. You mustn't wear rings or bracelets. | **Front desk:** You must wear a name badge and a collared shirt. You don't have to wear a tie. |

| Worker | too casual / not safe enough / OK | The rule |
|---|---|---|
| 1. A cook wears sandals. | | |
| 2. A cook wears a ring. | | |
| 3. A cook wears sneakers and a hat. | | |
| 4. A front-desk worker wears a T-shirt. | | |
| 5. A front-desk worker wears a collared shirt and no tie. | | |
| 6. A front-desk worker forgets her name badge. | | |

*Example:* "Number 1: sandals aren't safe enough. You must wear closed-toe shoes."

*Useful:* too casual • not formal enough • not safe enough • That's OK. • You must… • You mustn't… • You don't have to…
''')])
L['hw'] = dict(one=dict(head='Write the sentence. Use the words.', example='jeans / casual / for an interview (too) → *Jeans are too casual for an interview.*',
 items=[('6:55 / early / for a 7:00 shift? (enough)', 'Is 6:55 early enough for a 7:00 shift?'), ('there / be / many people / in the store (too)', 'There are too many people in the store.'),
  ('I / not have / time / for lunch (enough)', 'I don\'t have enough time for lunch.'), ('you / use / your phone / in the kitchen (mustn\'t)', 'You mustn\'t use your phone in the kitchen.')]),
 three='''### 3. Write 3 rules from a job, a school, or a place you know. Use *must*, *mustn't*, or *don't have to*. Then write why.

| The rule | Why? (*because…*) |
|---|---|
| 1. <br><br> | <br><br> |
| 2. <br><br> | <br><br> |
| 3. <br><br> | <br><br> |
''',
 four=dict(head='Review (Lesson 6). Write one word.', items=['If I [had] a car, I\'d drive to work. (have)', 'If I [were] you, I\'d tell the truth. (be)',
  'What [would] you do if you found $50?', 'If it rains tomorrow, [I\'ll] take the bus. (I\'ll / I\'d)', 'If I found a wallet, I\'d [give] it back. (give)']))
L['rw'] = dict(kind='notice', note='Read fast first. Then read again and answer the questions.', box_title='SUNRISE BAKERY · Employee Handbook, page 4 (invented company)',
 text='''
**Attendance.** Please arrive 5 to 10 minutes before your shift. Your shift starts when you are in uniform and ready to work. If you are going to be late, you must call your supervisor at least one hour before your shift. A text is not enough. If you are sick, call before 6:00 a.m.

**Dress code.** In the kitchen, you must wear the bakery hat, an apron, and closed-toe shoes. Sandals are not safe enough. You mustn't wear rings or bracelets in the kitchen, but a watch is OK. At the front counter, you don't have to wear a hat, but you must wear your name badge. Clean black pants are fine. Jeans with holes are too casual.

**Breaks.** You get a 15-minute break for every 4 hours of work. You mustn't use your phone in the kitchen. You can use it in the break room. Please wash your hands after every break.

**Questions?** Ask your supervisor. We are happy to help in your first weeks.
''',
 qs=[('When should you arrive?', '5 to 10 minutes before your shift.', 'arrive 5 to 10 minutes before your shift'),
  ('What must you do if you\'re going to be late?', 'Call your supervisor at least one hour before your shift.', 'you must call your supervisor at least one hour before your shift'),
  ('Is a text OK? Why or why not?', 'No. A text is not enough.', 'A text is not enough'),
  ('Do front counter workers have to wear a hat?', 'No, but they must wear a name badge.', 'At the front counter, you don\'t have to wear a hat, but you must wear your name badge'),
  ('Where can you use your phone?', 'In the break room.', 'You can use it in the break room')],
 write_head='Write "Tips for your first week" for a new coworker at a job you know (5–8 sentences). Use *must*, *don\'t have to*, *too*, and *enough*.',
 write_short='your tips',
 example='*Welcome to Green Market! Here are some tips for your first week. You must arrive 5 minutes early, so 8:00 is not early enough for an 8:00 shift. You must wear your name badge every day. You don\'t have to wear a uniform, but jeans with holes are too casual. Don\'t worry if you make a mistake. Ask questions, and you\'ll learn fast!*',
 box_label='My tips', checklist=['It has 5–8 sentences.', 'It has *must* and *don\'t have to*.', 'It has *too* or *enough*.', 'It is friendly and helpful.'])
L['exit'] = dict(q='What is one custom here that is different from your hometown (or another place you know)?', s1='here (*Here, people…*)', s2='there (*In my hometown, people…*)',
 s3='what you think, with *because*', key='*A good answer:* "Here, people usually arrive on time for a doctor\'s appointment. In my hometown, people often arrive a little late. I like the custom here because I don\'t wait a long time."')
L['game'] = ('Too, enough, or OK?', 'A points to a picture and asks, "Are **sandals** OK for the kitchen?" B answers with *too* or *enough* and a rule: "No, they aren\'t safe enough. You must wear closed-toe shoes." Switch.')
L['opening'] = dict(cards=['**A:** What would you do if you found $50 at work?', '**A:** What would you do if you had a free week?', '**A:** If you had a magic wand, what would you do?', '**A:** What would you do if a cashier gave you too much change?'],
 follow='Why? • Would you tell anyone? • What would your family do?', hw_head='Write your partner\'s name and one dream from Homework item 3.', hw_cols=['My partner\'s name', 'A dream (*If I had…, I\'d…*)'])
L['notes'] = [
 '**Describe, don\'t judge:** customs vary inside every country, including the U.S., and inside every family. No place is "better." Model *It\'s different* and *I like both*.',
 '**Rules come from each employer:** the bakery, the kitchen, and their rules are invented. Learners can say "At my job…" if they want; they never have to.',
 '***mustn\'t* vs. *don\'t have to*:** this is the biggest mix-up. Use a thumbs-down for *mustn\'t* (don\'t do it) and a shrug for *don\'t have to* (you choose).',
 '**Writing check 2 (Week 7):** collect the first-week tips. Write one strength and one fix on each. Learners keep them in their writing folder.',
 '**Week 8 is the midterm.** It covers Lessons 1–7. Remind learners to bring their workbook.',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening says *going to* and *want to*. People often say *gonna* and *wanna*. Learners only need to recognize the short forms; they can always say the full forms.']
