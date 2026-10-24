import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=13, week=14, title='My Story So Far',
topic='Personal growth and the graduation talk: learners look back at their own learning (when they started, what was hard, what they can do now) and look forward to the next step. They tell a short story with time clauses (*before / after / when*), past ability (*couldn\'t / was able to*), and the past continuous. Every story is the learner\'s choice; "my life in this class" is always enough. All names are invented.',
cq='What can you do now that you couldn\'t do before? What\'s next?',
builds=[
 ('*used to*', 'Level 4 Lesson 2', '*I used to stay home on weekends.*'),
 ('present perfect', 'Level 4 Lessons 1 and 5', '*I\'ve made friends in this class.*'),
 ('past continuous', 'Level 3', '***I was working*** *at a restaurant when I met her.*'),
],
objectives=['tell events in order with *before / after / when* and use a comma when the time clause comes first',
 'use the present after *when / after* for the future (*After I finish this class, I\'ll…*)',
 'talk about past ability with *couldn\'t / was able to*',
 'make a 5-event timeline of my learning and tell it to a group',
 'write an email (5–8 sentences) to my teacher about my story so far, the start of my graduation talk'],
materials=['Board and markers', 'A timeline of your own learning on the board (5 events) for the model', 'The feedback cards on the Talk Time page (copy and cut them, optional)', 'A timer (phone)'],
prep='15 minutes (read the plan; practice reading the listening script; write your own 1-minute story to model)',
words=[('milestone', 'milestone', True), ('challenge', 'challenge', True), ('succeed', 'succeed', True), ('confident', 'confident', True), ('get used to', 'get_used_to', True),
 ('make friends', 'make_friends', True), ('be able to', 'be_able_to', True), ('support', 'support', True), ('celebrate', 'celebrate', True), ('timeline', 'timeline', True),
 ('speech', 'speech', True), ('audience', 'audience', False)],
more_vocab='*Also:* a step, a goal, a success, nervous, proud, advice, a graduation, a certificate, a talk, a shift.',
clock=clock('', ' (+ My Words)', '', '*before / after / when*', 'Story Timeline + Talk Rehearsal', 'A learner story; an email to my teacher',
 talk_group='Pairs, then groups of 3'),
attend='With 5 or fewer, each learner makes a timeline and tells it to the whole group; you give the feedback cards. Late arrivals make a 3-event timeline and listen in a group, then tell it.',
)
L['steps'] = [
 step1('Opening Talk', '*who / that*; warning signs',
  'you say, "Tell me one warning sign of a scam." The learner answers with *who / that* (*A caller who asks for gift cards.*). Then you ask, "What should you do?" Help them say 3 sentences.',
  'Pairs compare Homework item 1 (*who / that*) and read their 3 warning signs (item 3) to each other. Then they fill in the box on the Opening Talk page.',
  '*a man who he called* (→ *a man who called*) and *a text who said* (→ *a text that said*)'),
 step2('*milestone* (an important step in your life); *challenge* (something hard); *succeed* (do it well, get what you wanted); *confident* (sure you can do it); *get used to* (something new becomes normal); *make friends*; *be able to* (can); *support* (help, be there for someone); *celebrate* (have a party, say "great job!"); *timeline* (events in order on a line); *speech* (a talk to many people); *audience* (the people who listen).',
  'ask "Is a challenge easy or hard?" (hard) • "When you are confident, are you sure or not sure?" (sure) • "Do you celebrate a milestone or a problem?" (a milestone).',
  'After I finish this class, I\'ll celebrate.'),
 step3('Mariana was a learner here. Now she is giving a short talk at graduation. Then her old teacher, Mr. Hill, asks her two questions. Listen: what is her main message?',
  'Point to the script line. *gonna* = going to: "I\'m **going to** take a training class." Then practice the pause at the comma: *When I started, (pause) I couldn\'t understand the bus driver.* Stress the key words: *NOW I can…, NEXT…*', '{EST}'),
 step4('*before / after / when*', 'draw a line on the board with 2 events: *I finished school. → I got a job.* Say, "**After I finished school,** I got a job." Point to the comma. Then: "I got a job **after I finished school.**" No comma. Then the future: "**After I finish this class, I\'ll** take Level 5." Cross out *When I will finish*.',
  'Box 1: read across: *What did you do after you finished school? → After I finished school, I worked in a store.* Box 2: *couldn\'t / was able to*, past continuous. Box 3: the comma. Box 4: the talk frame.',
  '"Time clause first: comma or no comma?" (comma) • "*When I will finish* or *When I finish*?" (*When I finish*) • "Last month, *I could call* the clinic one time, or *I was able to call*?" (*I was able to call*).',
  'A points to a picture and asks, "When did you **make friends** here?" B answers with a time clause: "**When I started** this class, I made friends." Switch.'),
 brk('*When I started, I couldn\'t… • After I finished…, I… • Now I can… • After I finish this class, I\'ll…*'),
 step5('Story Timeline + Talk Rehearsal', 'show your own 5-event timeline on the board and tell it in 1 minute: "When I started teaching, I was nervous. After I taught my first class, I felt better…" Then model a feedback card: "One thing I liked: your timeline was clear. One tip: speak a little slower."',
  '**Story Timeline (pairs).** Each learner writes 5 events from their own learning on the timeline (their choice; "my life in this class" is enough). They tell the timeline to a partner with *when / before / after*. The partner asks one question.',
  '**Talk Rehearsal (groups of 3).** Each learner tells their story (1–2 minutes) with the talk frame. The two listeners fill in a feedback card. Switch.',
  'pairs; then groups of 3.', 'pairs; then groups of 3 (or 2 groups of 4).', 'each learner tells the whole group; you give the feedback cards.'),
 step6('A learner story', 'Learners read the invented story on the Read & Write page, mark the time words, and answer the questions.',
  'Learners write an email (5–8 sentences) to their teacher about their story so far, with *when / before / after*. Show the example. This is the start of their graduation talk (Homework item 3).'),
 step7('Write about one change in your life.', 'When I started this class, I couldn\'t talk on the phone in English. I was afraid to call the clinic. Now I can call by myself, because I practiced every week.',
  'item 1: *after / I / finish / work, / I / come / to class (past) → After I finished work, I came to class.*'),
]
L['listen'] = dict(title='My Story So Far', voices={'Narrator': 'N', 'Mariana': 'Ana_af_jessica', 'Mr. Hill': 'Carlos'},
 female=['Narrator', 'Mariana'], names=['Mariana', 'Hill'], tts={},
 setting='A former learner, Mariana, gives a short graduation talk about her learning: then, what was hard, now, and next. Her old teacher, Mr. Hill, asks her two questions.',
 intro='Lesson thirteen. Mariana was a learner at this school. Now she is giving a short talk at graduation. Then her old teacher, Mr. Hill, asks her two questions.',
 lines=[
  ('Mariana', 'Good evening, everyone. My name is Mariana. When I started English classes here, I couldn\'t understand the bus driver. I was afraid to use the phone.'),
  ('Mariana', 'The first year was hard. I had a night job at a restaurant, and I was tired. But my classmates helped me, and I made friends.'),
  ('Mariana', 'After I finished Level 2, I got a new job at a hotel. Before I started that job, I practiced my interview with my teacher. Last year, I was able to call the clinic by myself for the first time. That was a big milestone for me.'),
  ('Mariana', 'Now I can talk to guests at work, and I help my kids with their homework. I\'m more confident.'),
  ('Mariana', 'What is next for me? After I finish Level 5, I\'m going to take a training class. I want a job at the front desk. My advice to you is simple. Come to class, and do not be afraid to make mistakes. Thank you for listening.'),
  ('Mr. Hill', 'Thank you, Mariana. That was wonderful. Can I ask you two questions?'),
  ('Mariana', 'Of course.'),
  ('Mr. Hill', 'What was the biggest challenge for you?'),
  ('Mariana', 'Getting used to the phone. When I called someone, I couldn\'t understand them very well. Now it\'s easy for me.'),
  ('Mr. Hill', 'And what helped you the most?'),
  ('Mariana', 'My classmates. When I was tired, they supported me. After class ended, we often studied together. And we celebrated every small success.'),
  ('Mr. Hill', 'Thank you. Everyone, let\'s celebrate Mariana!'),
 ],
 A=dict(q='What is Mariana\'s main message?', opts=['Come to class, and don\'t be afraid to make mistakes.', 'Hotel jobs are easy.', 'Level 5 is too hard.'], ans=0),
 B=dict(head='Her story in order: circle the answer.', kind='choice', items=[
  dict(s='First, when she started, she couldn\'t understand the {{*bus driver|teacher}}.', ev='I couldn\'t understand the bus driver'),
  dict(s='Then, in her first year, she worked at a {{*restaurant|hotel}} at night.', ev='I had a night job at a restaurant'),
  dict(s='After Level 2, she got a job at a {{*hotel|clinic}}.', ev='After I finished Level 2, I got a new job at a hotel.'),
  dict(s='Last year, she called the {{*clinic|school}} by herself.', ev='I was able to call the clinic by myself'),
  dict(s='Next, after Level 5, she\'s going to take a {{*training class|vacation}}.', ev='take a training class'),
  dict(s='Her biggest challenge was {{*the phone|the bus}}.', ev='Getting used to the phone.'),
 ]),
 C=dict(head='Write *before*, *after*, or *when*.', items=[
  '[When] I started English classes here, I couldn\'t understand the bus driver', '[After] I finished Level 2, I got a new job at a hotel.', '[Before] I started that job, I practiced my interview with my teacher.',
  '[When] I called someone, I couldn\'t understand them very well.', '[When] I was tired, they supported me.', '[After] class ended, we often studied together.']),
 hear='*gonna* = going to: "I\'m **going to** take a training class." You can say *going to*. Listen for the short pause at the comma: *When I started, (pause) I couldn\'t…* Do the same in your talk. Stress the key words: *NOW I can…, NEXT…*',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: *before / after / when*

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **What did you do** | after you finished school? | ‖ | **After I finished school,** | I worked in a store. |
| **How did you feel** | when you started this job? | ‖ | **When I started this job,** | I didn't know anyone. |
| **What couldn't you do** | before this class? | ‖ | **Before I started this class,** | I couldn't fill out a form. |
| **What will you do** | after you finish this class? | ‖ | **After I finish this class,** | I'll take Level 5. |

### Grammar Box 2: *couldn't / was able to*; *was …ing*

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Could you** | understand the bus driver? | ‖ | No, I **couldn't**. | Now I **can**. |
| **Were you able to** | call the clinic? | ‖ | Yes, I **was able to** | call by myself last month. |
| **What were you doing** | when you met your friend? | ‖ | **I was working** at a restaurant | **when** I met her. |
''',
rule='*before / after / when* + a full sentence (*I started*, *I finished*). The time part can come **first** (with a comma) or **second** (no comma). For the future, use the present after *when / after / before*: ***After I finish this class, I\'ll take Level 5.***',
explain='''
### Grammar Box 3: the comma

| TIME PART FIRST: comma | TIME PART SECOND: no comma |
|---|---|
| *When I started, I didn't know anyone.* | *I didn't know anyone when I started.* |
| *After I finish this class, I'll take Level 5.* | *I'll take Level 5 after I finish this class.* |

### Grammar Box 4: the talk frame

| PART | SAY |
|---|---|
| **Then** | *When I started…, I couldn't…* |
| **What was hard** | *It was hard because… But I've…* |
| **Now** | *Now I can… I'm more confident.* |
| **Next** | *After I finish…, I'll… because…* |
''',
qa=[('*When I will finish* or *When I finish*?', '***When I finish this class, I\'ll take Level 5.*** Use the present after *when / after / before*, like after *if*.'),
 ('Do I need a comma?', 'Time part first: comma. ***After I finished school, I worked.*** Time part second: no comma. *I worked after I finished school.*'),
 ('*couldn\'t* or *wasn\'t able to*?', 'Both are OK: ***I couldn\'t drive. / I wasn\'t able to drive.*** For one success in the past, use *was able to*: *I was able to call the clinic.*')],
A=dict(head='Write one word.', items=['[When] I started this job, I didn\'t know anyone.', 'Before I came here, I [couldn\'t] speak English. (can\'t)',
 'After I finish this class, I [will] take Level 5.', 'Last month, I was [able] to call the clinic by myself.', 'I was [working] at a store when I met my friend. (work)',
 'When I [finish] this class, I\'ll celebrate. (finish / will finish)']),
B=dict(head='Circle the correct words.', items=['When I {{*finish|will finish}} the class, I\'ll look for a new job.', '{{*After I finished school,|After I finished school}} I worked in a store.',
 'Before I started class, I {{*couldn\'t|can\'t}} read the bus schedule.', 'I {{*was able to|could to}} fill out the form by myself.', 'I used to {{*work|working}} at night, but now I work days.',
 'I\'ve {{*made|make}} many friends in this class.']),
mistakes=[('When I will finish, I\'ll call you.', 'When I **finish**, I\'ll call you.'), ('Before I came here I couldn\'t drive.', 'Before I came here**,** I couldn\'t drive.'),
 ('I could to fill out the form.', 'I **was able to** fill out the form.'), ('After finish class, I go home.', 'After **I finish** class, I go home.'),
 ('I was work when I met her.', 'I was **working** when I met her.')],
tip='Spanish uses a special verb form after *cuando* for the future: *Cuando termine la clase, voy a celebrar.* English uses the simple present: ***When I finish*** *the class, I\'m going to celebrate* (not *When I will finish*). What do you say in your language?')
L['talk'] = dict(pages=[('Story Timeline', '''
### Round 1. Write 5 events from your learning on the timeline. It's your choice: your life in this class is enough. Then tell a partner with *when / before / after*. Your partner asks one question.

| | When? | What happened? |
|---|---|---|
| **1. Then** | *When I started this class,* | |
| **2.** | | |
| **3.** | | |
| **4. Now** | *Now* | |
| **5. Next** | *After I finish this class,* | |

*Example:* "When I started this class, I couldn't talk on the phone. After I practiced with my partner, I called the clinic. Last month, I was able to fill out a job form. Now I'm more confident. After I finish this class, I'll take Level 5."

| QUESTIONS FOR YOUR PARTNER |
|---|
| What was the hardest part? |
| How did you feel when…? |
| What helped you? |
'''), ('Talk Rehearsal', '''
### Round 2. Work in groups of 3. Tell your story (1–2 minutes) with the talk frame: Then → What was hard → Now → Next. The two listeners fill in a feedback card. Then switch.

| TALK FRAME | |
|---|---|
| **Then** | *When I started…, I couldn't…* |
| **What was hard** | *It was hard because… But I've…* |
| **Now** | *Now I can…* |
| **Next** | *After I finish…, I'll… because…* |

| FEEDBACK CARD | Speaker: | Speaker: |
|---|---|---|
| One thing I liked | | |
| One tip (*slower, louder, pause at the comma*) | | |

*Remember:* you can read from your paper. Look up at the audience at the end of each part.
''')])
L['hw'] = dict(one=dict(head='Write the sentence. Use a comma after the time part.', example='when / I / start / this class, / I / not know / anyone (past) → *When I started this class, I didn\'t know anyone.*',
 items=[('after / I / finish / work, / I / come / to class (past)', 'After I finished work, I came to class.'), ('before / I / start / this job, / I / can\'t / drive (past)', 'Before I started this job, I couldn\'t drive.'),
  ('after / I / finish / this class, / I / take / Level 5 (future)', 'After I finish this class, I\'ll take Level 5.'), ('last month, / I / be able to / call the clinic (past)', 'Last month, I was able to call the clinic.')]),
 three='''### 3. Finish your graduation talk (12–15 sentences, about 2 minutes). Start with your email from Read & Write. Bring it next week.

| PART | My notes |
|---|---|
| **Then** (*When I started…*) | |
| **What was hard** (*It was hard because…*) | |
| **Now** (*Now I can…*) | |
| **Next** (*After I finish…, I'll…*) | |
''',
 four=dict(head='Review (Lesson 12). Write one word.', items=['A scam is a trick [that] takes your money.', 'Don\'t trust a caller [who] asks for gift cards.',
  'Never give your PIN to [anyone].', 'You [mustn\'t] share your password. (must / mustn\'t)', 'Be careful with texts [that] ask for your PIN.']))
L['rw'] = dict(kind='notice', note='Read fast first. Then read again. Underline the time words (*when, before, after, now, last month*). Answer the questions.', box_title='RIVERSIDE ADULT LEARNING · Class Newsletter (invented)',
 text='''
**MY STORY SO FAR, by Tomás R.** When I came to this city four years ago, I didn't know anyone. I couldn't read the bus schedule, and I was afraid to go to the doctor alone. I used to stay at home on weekends because everything was difficult.

Two years ago, my neighbor told me about the free English classes at the library. Before I started, I was very nervous. But on the first night, I met my teacher and three classmates who also worked at night. They became my friends.

The first year was a challenge. I was working at a warehouse, and I was always tired. After I finished my shift, I came to class. Sometimes I fell asleep! But I didn't stop.

Now I can do many things by myself. Last month, I was able to fill out a job application online, and I got an interview. I've made friends at work, and I'm more confident on the phone.

When I finish Level 4, I'm going to take a forklift training class. My advice? Come to class, even when you are tired. Small steps make a big change.
''',
 qs=[('When he came to the city, what couldn\'t he do?', 'He couldn\'t read the bus schedule.', 'I couldn\'t read the bus schedule'),
  ('How did he hear about the classes?', 'His neighbor told him.', 'my neighbor told me about the free English classes'),
  ('What did he do after his shift?', 'He came to class.', 'After I finished my shift, I came to class.'),
  ('What was he able to do last month?', 'He filled out a job application online.', 'I was able to fill out a job application online'),
  ('What will he do when he finishes Level 4?', 'He\'s going to take a forklift training class.', 'I\'m going to take a forklift training class')],
 write_head='Write an email (5–8 sentences) to your teacher about your story so far: when you started, what was hard, what you can do now, and your next step, with a reason. Use *when / before / after*.',
 write_short='your email',
 example='*Dear Mr. Hill, When I started this class in September, I couldn\'t understand the news on TV. The hardest part was the phone. After I practiced with my classmates, I felt more confident. Last week, I was able to call my child\'s school by myself. Now I can help my neighbors with forms. After I finish this class, I\'ll take Level 5, because I want a better job. Thank you for your help! Rosa*',
 box_label='My email', checklist=['It has 5–8 sentences.', 'It has *when / before / after*.', 'It has a comma after the time part.', 'It has my next step and a reason.'])
L['exit'] = dict(q='Write about one change in your life.', s1='when it happened, with *When…*', s2='what you couldn\'t do before',
 s3='what you can do now, with a reason (*because*)', key='*A good answer:* "When I started this class, I couldn\'t talk on the phone in English. I was afraid to call the clinic. Now I can call by myself, because I practiced every week."')
L['game'] = ('When did you…?', 'A points to a picture and asks, "When did you **make friends** here?" B answers with a time clause: "**When I started** this class, I made friends." Switch.')
L['opening'] = dict(cards=['**A:** What is one warning sign of a scam?', '**A:** What should you do with a text that asks for your PIN?', '**A:** Who can you call to check a bill?', '**A:** Is it a scam? "You won a prize! Pay $20 to get it."'],
 follow='Why? • What should you do?', hw_head='Write your partner\'s name and one warning sign from Homework item 3.', hw_cols=['My partner\'s name', 'Their warning sign and what to do'])
L['notes'] = [
 '**Stories are the learner\'s choice.** "My life in this class" or "my job" is always enough. Never ask about migration journeys, family separation, or other hard events. If a learner shares something hard, thank them and move on.',
 '**Model first:** tell your own 1-minute story with the talk frame before learners start. Reading from paper is OK, today and at graduation.',
 '**Writing check 5 (the graduation talk):** the Read & Write email (5–8 sentences) is the first draft. Learners finish the full talk at home (Homework item 3, 12–15 sentences, about 2 minutes). Collect it next week and give one or two tips.',
 '**Next weeks:** Week 15 is the final exam; Week 16 is graduation, where learners can give their talk.',
 '**Pronunciation:** pause at the comma after a time clause: *When I started, (pause) I couldn\'t…*',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening says *going to*. People often say *gonna*. Learners only need to recognize it; they can always say the full form.']
