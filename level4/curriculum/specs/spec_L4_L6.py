import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=6, week=6, title='What Would You Do?',
topic='Imagining situations and making choices: finding money, getting too much change, a free week, a magic wand, a dream job. Learners talk about imaginary situations with *If I had / found / were…, I\'d…*, give reasons, and give advice with *If I were you, I\'d…*. All situations are invented and everyday.',
cq='If it happened to you, what would you do?',
builds=[
 ('*If* + present, *will* (possible future)', 'Level 3 Lesson 11', '***If* + past, *would*** for imaginary situations: *If I found $50, I\'d give it back.*'),
 ('simple past forms (*found, had, won*)', 'Levels 2–3', 'the same forms after *if* for "not real now": *If I **had** a car…*'),
 ('suggestions (*Why don\'t you…? / You could…*)', 'Level 4 Lesson 4', 'advice with ***If I were you, I\'d…***'),
],
objectives=['ask and answer *What would you do if…?*',
 'talk about an imaginary situation with *If I + past, I\'d + verb*',
 'give advice with *If I were you, I\'d…* and a reason',
 'tell a possible situation (*If it rains, I\'ll…*) from an imaginary one (*If I had…, I\'d…*)',
 'write a reply to an advice letter (5–8 sentences)'],
materials=['Board and markers', 'Situation cards (in the workbook Talk Time page; copy them onto index cards, optional)', 'A pencil or a stick as a "magic wand" (optional, for Talk Time)'],
prep='15 minutes (read the plan; practice reading the listening script; practice *I\'d* and *wouldn\'t*)',
words=[('imagine', 'imagine', True), ('choose', 'choose', True), ('honest', 'honest', True), ('tell the truth', 'tell_the_truth', True), ('keep (it)', 'keep', True),
 ('give back', 'give_back', True), ('owner', 'owner', True), ('envelope', 'envelope', True), ('extra money', 'extra_money', True), ('mistake', 'mistake', True),
 ('magic wand', 'magic_wand', False), ('dream job', 'dream_job', False)],
more_vocab='*Also:* a situation, a cashier, change (money back), a caller, a radio show, a wallet, a lie, probably, feel bad, advice.',
clock=clock('', ' (+ My Words)', '', '*If I had…, I\'d… / What would you do if…?*', 'What Would You Do? + Magic Wand Chain', 'An advice column; a reply to a letter',
 talk_group='Groups of 3–4, then a circle'),
attend='With 5 or fewer, do What Would You Do? as one group: you read the card and everyone answers. Do the Magic Wand Chain as one circle. Late arrivals join a group and answer the next card.',
)
L['steps'] = [
 step1('Opening Talk', 'favors: *Would you mind…? / Do you mind if I…?*',
  'you say, "Would you mind lending me a pen?" The learner answers, "No, not at all," or "Sorry, I can\'t, because…" Then they ask you a favor. Help them say 3 sentences.',
  'Pairs compare Homework item 1 (*Would you mind* + *-ing*) and ask each other their 3 favors (item 3). Then they fill in the box on the Opening Talk page.',
  '*Would you mind to get…?* (→ *Would you mind getting…?*) and *Yes, I\'ll help* as the answer (→ *No, not at all*)'),
 step2('*imagine* (point to your head: a picture in your mind); *choose* (hold up two things: pick one); *honest* and *tell the truth* (you don\'t lie); *keep it* vs. *give it back* (mime with a coin); *owner* (the person it belongs to); *envelope*; *extra money* (more than you should get); *mistake*; *magic wand* (wave a pencil); *dream job* (the job you want most).',
  'ask "If a cashier gives you extra money, is it a mistake?" (yes) • "Is the owner the person who found it or the person it belongs to?" (it belongs to) • "If you tell the truth, are you honest?" (yes).',
  'If I found a wallet, I\'d give it back to the owner.'),
 step3('This is a radio show called *What Would You Do?* Mike is the host. He tells a situation, and two people call the show with their answers. Listen: what is the situation?',
  'Point to the script lines. *wanna* = want to: "I **wanna** hear your ideas." *gonna* = going to: "If you\'re **gonna** call, call early!" Then practice *I\'d* (say the *d*): *I\'d give it back*, and *What would you DO?* with the stress on *do*.', '{EST}'),
 step4('*What would you do if…? / If I had…, I\'d…*', 'hold up a pencil as a magic wand. Say, "I don\'t have a magic wand. But **if I had** a magic wand, **I\'d** fix all the potholes in this city." Write it in two halves: *If I **had** a magic wand, | I**\'d fix** the potholes.* Say: "It\'s not real. We use the past form after *if* and *would* in the other half."',
  'Box 1: read across: *What would you do if you found $50 at work? → If I found $50, I\'d give it to my supervisor.* Box 2: possible (*If it rains, I\'ll…*) vs. imaginary (*If I had a car, I\'d…*). Box 3: *I\'d* and *wouldn\'t*. Box 4: *If I were you, I\'d…* for advice.',
  '"Do I have a magic wand?" (no) "So do I say *If I have* or *If I had*?" (*If I had*) • "*If I would have time* or *If I had time*?" (*If I had time*) • "*If I were you* or *If I am you*?" (*If I were you*).',
  'A reads a situation from the pictures: "What would you do if you found an envelope with money?" B answers with *If I found…, I\'d…* and a reason. Switch.'),
 brk('*What would you do if you found $50? → If I found $50, I\'d give it back. • If I were you, I\'d… • If it rains, I\'ll… (possible)*'),
 step5('What Would You Do? + Magic Wand Chain', 'read a card: "You find $50 on the floor at work. What would you do?" Help a learner say, "If I found $50, I\'d give it to my supervisor because it isn\'t mine." Say: "Your answer, then *because*."',
  '**What Would You Do? (groups of 3–4).** One person reads a situation card. Each person answers with *If I…, I\'d…* and a reason. The group writes the most common answer. Then the next person reads a card.',
  '**Magic Wand Chain (circle).** Pass the "magic wand." Each person says, "If I had a magic wand, I\'d…" One more round: "If I had my dream job, I\'d…" Classmates can ask one follow-up question.',
  'groups of 3–4 for round 1; then two circles for round 2.', 'two groups for round 1; then one circle.',
  'one group for round 1: you read the cards. Then one circle.'),
 step6('An advice column', 'Learners read a letter to an advice column and the answer on the Read & Write page and answer the questions.',
  'Learners read a short letter about a noisy neighbor and write a reply (5–8 sentences) with *If I were you, I\'d… because…*. Show the example. Invented details are fine.'),
 step7('What would you do if you had a free week?', 'If I had a free week, I\'d visit my sister in Chicago. I\'d also cook a big dinner for my family. I\'d do that because I don\'t see them very often.',
  'item 1: *if I / have / a free week, I / visit / my cousin → If I had a free week, I\'d visit my cousin.*'),
]
L['listen'] = dict(title='What Would You Do?', voices={'Narrator': 'N', 'Mike': 'Server', 'Grace': 'Ana_af_jessica', 'Teresa': 'Rosa'},
 female=['Narrator', 'Grace', 'Teresa'], names=['Mike', 'Grace', 'Teresa'], tts={},
 setting='A radio show called *What Would You Do?* The host, Mike, tells a situation. Two callers, Grace and Teresa, give their answers.',
 intro='Lesson six. This is a radio show called What Would You Do? Mike is the host. Two people call the show.',
 lines=[
  ('Mike', 'Good afternoon, and welcome to What Would You Do? Here\'s today\'s situation. You buy groceries, and the cashier gives you ten dollars too much change. You see it in the parking lot. What would you do?'),
  ('Mike', 'Our first caller is Grace. Hi, Grace!'),
  ('Grace', 'Hi, Mike. If that happened to me, I\'d go back inside and give the money back.'),
  ('Mike', 'Really? Why would you go back?'),
  ('Grace', 'Because the cashier made a mistake. If I kept the money, she would have a problem at the end of her shift.'),
  ('Mike', 'That\'s very honest. Thanks, Grace. Our next caller is Teresa. Teresa, what would you do?'),
  ('Teresa', 'Well, Mike, this really happened to me once. A cashier gave me twenty dollars too much.'),
  ('Mike', 'Really? What did you do?'),
  ('Teresa', 'I gave it back the next day. I was in a hurry, so I couldn\'t go back that day.'),
  ('Mike', 'Was the cashier happy?'),
  ('Teresa', 'Yes, she was very happy. She said thank you three times!'),
  ('Mike', 'And what would you do if it were only one dollar?'),
  ('Teresa', 'Hmm. If it were one dollar, I\'d probably keep it. But I\'d feel a little bad.'),
  ('Mike', 'Ha! That\'s an honest answer, too. Thank you, Teresa.'),
  ('Mike', 'Next week\'s question is this: what would you do if you found an envelope with money at work? I wanna hear your ideas. And if you\'re gonna call, call early!'),
 ],
 A=dict(q='What is the situation?', opts=['A cashier gives you too much change.', 'You find money on the floor at work.', 'A friend asks you to tell a small lie.'], ans=0),
 B=dict(head='Who says it, and what? Circle the answer.', kind='choice', items=[
  dict(s='Grace would {{*give the money back|keep the money}}.', ev='I\'d go back inside and give the money back.'),
  dict(s='Grace\'s reason: the cashier {{*made a mistake|was her friend}}.', ev='Because the cashier made a mistake.'),
  dict(s='Teresa once got {{$10|*$20}} too much.', ev='A cashier gave me twenty dollars too much.'),
  dict(s='Teresa gave it back {{the same day|*the next day}}.', ev='I gave it back the next day.'),
  dict(s='If it were one dollar, Teresa would {{*probably keep it|give it back}}.', ev='If it were one dollar, I\'d probably keep it.'),
  dict(s='Next week\'s situation: {{*an envelope with money at work|a lost phone on the bus}}.', ev='if you found an envelope with money at work'),
 ]),
 C=dict(head='Write the missing word: *would*, *were*, *I\'d*, or a past verb.', items=[
  'Really? Why [would] you go back?', 'If I [kept] the money, she would have a problem at the end of her shift.', 'And what would you do if it [were] only one dollar?',
  'If it were one dollar, [I\'d] probably keep it.', 'But [I\'d] feel a little bad.', 'what would you do if you [found] an envelope with money at work?']),
 hear='*wanna* = want to: "I **wanna** hear your ideas." • *gonna* = going to: "If you\'re **gonna** call, call early!" You can say *want to* and *going to*. Listen for *I\'d* (= I would): the *d* is short but it is there. In *What would you **do**?*, the stress is on *do*.',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: *What would you do if…?*

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **What would** you **do** | if you **found** $50 at work? | ‖ | If I **found** $50, | I**'d give** it to my supervisor. |
| **What would** you **do** | if you **had** a free week? | ‖ | If I **had** a free week, | I**'d visit** my cousin. |
| **Would** you **keep** | the extra money? | ‖ | No, I **wouldn't**. | I**'d give** it back. |
| **What would** you **do** | if you **were** me? | ‖ | If I **were** you, | I**'d call** the owner. |

### Grammar Box 2: possible or imaginary?

<!-- subst -->
| POSSIBLE (maybe it will happen) | < | ‖ | IMAGINARY (not real now) | < |
|---|---|---|---|---|
| If it **rains** tomorrow, | I**'ll take** the bus. | ‖ | If I **had** a car, | I**'d drive** to work. |
| If I **get** the job, | I**'ll buy** a new phone. | ‖ | If I **won** $1,000, | I**'d pay** my bills. |
| If you **find** my keys, | **will** you **call** me? | ‖ | If I **found** a wallet, | I**'d look** for the owner. |
''',
rule='Imaginary: use the **past form** after *if* (*found, had, were*). Use ***would* / *\'d* + base verb** in the other half (*I\'d give, I\'d visit*). Never put *would* right after *if*.',
explain='''
### Grammar Box 3: *would* short forms

| LONG | SHORT | EXAMPLE |
|---|---|---|
| I would | **I'd** | *I'd give it back.* |
| she would | **she'd** | *She'd keep it.* |
| would not | **wouldn't** | *I wouldn't keep it.* |

### Grammar Box 4: advice with *If I were you…*

| | USE | EXAMPLE |
|---|---|---|
| *If I were you, I'd…* | advice | *If I were you, I'd talk to the supervisor.* |
| *were* for every person | imaginary | *If it were one dollar, I'd keep it.* |
| *If I was…* | you hear it in speaking; it's OK | in writing, use *If I were* |
''',
qa=[('Can I say *If I would have time, I\'d take a class*?', 'No. Never put *would* right after *if*: ***If I had time, I\'d take a class.***'),
 ('*If I was you* or *If I were you*?', 'Write ***If I were you***. In speaking, many people say *If I was you*. That\'s OK.'),
 ('*If it rains* or *If it rained*?', 'Possible (maybe tomorrow): *If it **rains**, I\'ll stay home.* Imaginary (not real now): *If I **had** a car, I\'d drive.*')],
A=dict(head='Write the correct form of the verb.', items=['If I [found] a wallet, I\'d look for the owner. (find)', 'If I had more time, I\'d [take] a computer class. (take)',
 'If I [were] you, I\'d tell the truth. (be)', 'What would you [do] if you won $500? (do)', 'If she [had] a car, she\'d drive to work. (have)',
 'If it rains tomorrow, [I\'ll] take the bus. (I\'ll / I\'d)']),
B=dict(head='Circle the correct words.', items=['If I {{*had|have}} a magic wand, I\'d fix all the potholes.', 'If I found $50, I {{*would|will}} give it back.',
 'If I {{*were|would be}} you, I\'d call the owner.', 'If it {{*rains|rained}} tomorrow, I\'ll stay home.', 'Would you keep it? No, I {{*wouldn\'t|don\'t}}.',
 '{{*What would you do|What you would do}} if you had a free week?']),
mistakes=[('If I would have time, I\'d take a class.', 'If I **had** time, I\'d take a class.'), ('If I found $50, I will give it back.', 'If I found $50, I**\'d** give it back.'),
 ('What you would do?', '**What would you** do?'), ('If I am you, I\'d call.', 'If I **were** you, I\'d call.'), ('I\'d to give it back.', 'I\'d **give** it back.')],
tip='Spanish says *Si tuviera…, haría…* with special verb forms. English is easier: use the **past** after *if* (*If I **had**…*) and *would* in the other half (*I**\'d** go*). Never put *would* after *if*. What does your language do?')
L['talk'] = dict(pages=[('What Would You Do?', '''
### Round 1. Work in groups of 3–4. One person reads a situation card. Each person answers with *If I…, I'd…* and a reason. Write your group's most common answer.

| SITUATION CARDS (invented) | |
|---|---|
| 1. You find $50 on the floor at work. | 2. A cashier gives you too much change. |
| 3. Your neighbor's door is open late at night. | 4. A friend asks you to tell a small lie. |
| 5. A coworker is late every day. | 6. You find a phone on the bus. |
| 7. A restaurant forgets to charge you for a drink. | 8. A friend asks, "Do you like my new haircut?" You don't. |

*Example:* A: What would you do if you found $50 on the floor at work? B: If I found $50, I'd give it to my supervisor because it isn't mine. C: I'd ask my coworkers first.

| Card | Our most common answer (*We'd…*) | Our reason (*because…*) |
|---|---|---|
| | | |
| | | |
| | | |
'''), ('Magic Wand Chain', '''
### Round 2. Sit in a circle. Pass the "magic wand." Each person says one sentence: *If I had a magic wand, I'd…* Then do one more round: *If I had my dream job, I'd…* Classmates can ask one question: *Why?*

*Example:* "If I had a magic wand, I'd fix all the potholes in this city." "Why?" "Because my car hates them!" • "If I had my dream job, I'd be a chef, and I'd cook food from my country."

| My magic wand sentence | My dream job sentence |
|---|---|
| If I had a magic wand, I'd <br><br> | If I had my dream job, I'd <br><br> |

| A classmate's idea I liked | Their name |
|---|---|
| <br> | |
| <br> | |

*Useful:* If I had…, I'd… • I'd also… • because… • Why? • Me too! • That's a great idea.
''')])
L['hw'] = dict(one=dict(head='Write the sentence. Use the words.', example='if I / find / a wallet, I / call / the owner → *If I found a wallet, I\'d call the owner.*',
 items=[('if I / have / a free week, I / visit / my cousin', 'If I had a free week, I\'d visit my cousin.'), ('if I / be / you, I / tell / the truth', 'If I were you, I\'d tell the truth.'),
  ('what / you / do / if you / win / $500?', 'What would you do if you won $500?'), ('if she / have / a car, she / drive / to work', 'If she had a car, she\'d drive to work.')]),
 three='''### 3. Write 3 sentences about your dreams. Use *If I had…, I'd…* and a reason.

| If I had… | I'd… because… |
|---|---|
| 1. <br><br> | <br><br> |
| 2. <br><br> | <br><br> |
| 3. <br><br> | <br><br> |
''',
 four=dict(head='Review (Lesson 5). Write one word.', items=['Would you mind [watering] my plants? (water)', 'Do you mind [if] I open the window?',
  'A: Would you mind helping me? B: No, not [at] all.', 'Could I borrow your pen? I forgot [mine].', 'Would you mind [covering] my shift on Friday? (cover)']))
L['rw'] = dict(kind='notice', note='Read fast first. Then read again and answer the questions.', box_title='ADVICE COLUMN · Ask Gloria: Work and Life',
 text='''
**Dear Gloria,** I work at a busy restaurant. My coworker, Leo, is very friendly, and everyone likes him. But he takes long breaks every day. Sometimes his break is 30 minutes, not 15. When he's on break, I do his work and mine. I don't want to make him angry. What would you do? *Tired in Texas*

**Dear Tired,** You are a good coworker, but you shouldn't do two jobs every day. If I were you, I'd talk to Leo first. I'd be friendly, and I'd talk to him alone, not in front of other people. You could say, "When you take a long break, I have a lot of extra work. Could you come back after 15 minutes?" Maybe he doesn't know there is a problem. If he still took long breaks after that, I'd talk to the supervisor. I wouldn't be angry. I'd just explain the problem. Good luck! *Gloria*
''',
 qs=[('Where does the writer work?', 'At a busy restaurant.', 'I work at a busy restaurant'),
  ('How long are Leo\'s breaks sometimes?', '30 minutes, not 15.', 'Sometimes his break is 30 minutes, not 15'),
  ('What would Gloria do first?', 'She\'d talk to Leo.', 'If I were you, I\'d talk to Leo first'),
  ('Where would she talk to him?', 'Alone, not in front of other people.', 'I\'d talk to him alone, not in front of other people'),
  ('When would she talk to the supervisor?', 'If Leo still took long breaks after that.', 'If he still took long breaks after that, I\'d talk to the supervisor')],
 write_head='Read this letter: *"Dear Gloria, My neighbor plays loud music every night until midnight. I start work at 6:00 a.m. What would you do? Sleepy"* Write a reply (5–8 sentences). Use *If I were you, I\'d… because…*',
 write_short='your reply',
 example='*Dear Sleepy, I\'m sorry you can\'t sleep. If I were you, I\'d talk to your neighbor first. I\'d be friendly because maybe he doesn\'t know about the problem. You could say, "I start work very early. Could you turn the music down after 10:00?" If he didn\'t stop, I\'d write a note to the building manager. Good luck! Gloria*',
 box_label='My reply', checklist=['It has 5–8 sentences.', 'It has *If I were you, I\'d…*.', 'It has a reason with *because*.', 'It has a polite idea and a second idea.'])
L['exit'] = dict(q='What would you do if you had a free week?', s1='an *if*-sentence (*If I had a free week, I\'d…*)', s2='a second idea (*I\'d also…*)',
 s3='the reason, with *because*', key='*A good answer:* "If I had a free week, I\'d visit my sister in Chicago. I\'d also cook a big dinner for my family. I\'d do that because I don\'t see them very often."')
L['game'] = ('What would you do?', 'A points to a picture and asks, "What would you do if you found an **envelope** with money?" B answers, "If I found…, I\'d…" and gives a reason. Switch.')
L['opening'] = dict(cards=['**A:** Would you mind lending me a pen?', '**A:** Would you mind opening the window?', '**A:** Do you mind if I sit here?', '**A:** Would you mind helping me with my homework?'],
 follow='Answer *No, not at all* or *Sorry, I can\'t, because…* • Then switch.', hw_head='Write your partner\'s name and one favor from Homework item 3.', hw_cols=['My partner\'s name', 'A favor (*Would you mind…?*)'])
L['notes'] = [
 '**Past form, present meaning:** *If I had a car* is about **now**, not the past. Say it: "I don\'t have a car. It\'s imaginary."',
 '***If I were* / *If I was*:** teach *If I were*. Accept *If I was* in speaking. In writing, gently show *If I were*.',
 '**Situation cards:** all situations are invented and everyday. No answer is wrong. Learners choose and give a reason; never judge a learner\'s choice.',
 '**Personal topics:** learners never need to talk about real money problems. *If I won $1,000* is just a game.',
 '***I\'d*:** learners often drop the *d*. Model *I\'d give* slowly, then smoothly.',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening has *gonna* and *wanna*. Learners need to understand them; they can always say *going to* and *want to*.']
