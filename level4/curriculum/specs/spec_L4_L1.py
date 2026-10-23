import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=1, week=1, title='Have You Ever…?',
topic='First night: getting to know classmates through life experiences (places, foods, jobs, things you\'ve tried). Orientation, the personal word list, the first can-do self-check, and the baseline snapshot.',
cq='Do you ask or answer first? How many sentences do you say?',
builds=[
 ('Simple past questions and answers: *What did you do last weekend? → I went to the park.*', 'Level 3 Lessons 2–4', 'The **present perfect for experiences**: *Have you ever worked in a restaurant? → Yes, I have. / No, I\'ve never…*'),
 ('Irregular past forms: *went, saw, ate, ran*', 'Level 3 Lessons 2, 4', '**Past participles** (*been, seen, eaten, ridden, flown…*) with a list of 20'),
 ('*-ed / -ing* adjectives: *It was exciting.*', 'Level 3 Lesson 11', '**Present perfect → simple past** for the details: *Yes, I have. I went there in 2022. → How was it?*'),
],
objectives=['ask *Have you ever…?* and answer *Yes, I have. / No, I haven\'t. / No, never.*',
 'say *I\'ve never… / She\'s lived…* with *have / has* + a past participle',
 'ask a follow-up in the simple past (*When did you…? How was it?*)',
 'tell a classmate about one experience in 3 sentences (the experience, when, how it was)',
 'write a short introduction email to the teacher (5–8 sentences)'],
materials=['Board and markers; tape for a timeline across the board', 'Name tags or folded paper and markers',
 'Can-Do Self-Check page (in the workbook) and the baseline snapshot notes (see Teacher notes)'],
prep='15 minutes (read the plan; draw the "my life → now" timeline on the board; practice reading the listening script)',
words=[('try (a new food)', 'try_food', True), ('travel', 'travel', True), ('fly', 'fly', True), ('snow', 'snow', True), ('ocean', 'ocean', True),
 ('mountain', 'mountain', True), ('desert', 'desert', True), ('win a prize', 'win_prize', True), ('ride a horse', 'ride_horse', True),
 ('run a race', 'run_race', True), ('go camping', 'camping', False), ('see a famous person', 'famous', False)],
more_vocab='*Also:* ever, never, in common, both, a goal, a tent, sushi, a 5K (a 5-kilometer race), exciting, boring.',
clock=clock(' (+ welcome and orientation, 2 min)', ' (+ My Words and the Task Words page)', '', '*Have you ever…?* and the simple past for details',
 'Find Someone Who Has… + Two True, One Invented** (+ baseline snapshot, 5 learners)', 'Meet Our Class + an email to the teacher (+ Can-Do Self-Check, 3 min)',
 talk_group='Mingle, then groups of 3 / one circle, then 2 groups'),
attend='With 5 or fewer, sit at one table and do Talk Time as one group (each person asks every other person 2 prompts). Late arrivals join any pair or group right away, and you show them the workbook after class.',
)
L['steps'] = [
 step1('Welcome, orientation, and Opening Talk', '*Welcome! Level 4 · 6:00–7:30 · Break 6:45 · Homework every week (15–20 minutes)* and the question *What did you do last weekend?*',
  'you ask, "What did you do last weekend?" The learner answers. Help them add a reason and a detail: "*I went to the park. I went because it was sunny. My kids played soccer.*" Then you ask a follow-up: "*How was it?*"',
  'Pairs fill in the box at the bottom of the Opening Talk page: the partner\'s name and one thing the partner did last weekend. Two or three pairs introduce their partner to the class: "*This is Rosa. She went to a birthday party.*"', None,
  extra=['**Welcome and orientation (2 min, first):** say your name and write it on the board. Show the workbook: "This is your book for tonight. Every week has the same parts." Point to the times on the board. Say: "We speak English in class. It\'s OK to make mistakes. Mistakes help us learn." Give out name tags.']),
 step2('*ocean* (a wave, very big water) vs. a lake; *desert* (hot, dry, sand); *win a prize* (first place, a trophy); *ride a horse* (sit on it). Mime *fly*, *run a race*, and *ride*.',
  'ask "Is the ocean salty or sweet?" (salty) • "Is a desert hot and dry or cold and wet?" (hot and dry) • "Do you sleep in a tent when you go camping?" (yes).',
  '*I\'ve seen the ocean. / I\'ve never ridden a horse.*',
  extra=['**Show the two new pages (1 min):** the **My Words** page (a personal word list, optional) and the **Task Words** page at the back (optional). Say: "These pages are for you. Use them if you want."']),
 step3('This is the first night of an English class. Lucía and Ahmed meet. Then the teacher, Ms. Grant, gives them a job. Listen: what have they both done?',
  'Point to the script lines. *gonna* = going to: "Tonight we\'re **gonna** find things we have in common." *wanna* = want to: "I **wanna** go camping." Say: "You will hear *gonna* and *wanna*. You can say *going to* and *want to*." Then practice the weak, short *have* (it sounds like "h\'v"): *Have you ever seen snow?* and the contraction: *I\'ve never ridden a horse.*', '{EST}'),
 step4('present perfect for experiences', 'draw a long line on the board: "my life → now." Put three X\'s on the line with no dates: "I\'ve seen snow. I\'ve run a race. I\'ve never ridden a horse." Then write a date under one X: "I ran a race **in 2023**." Say: "No time → *have* + past participle. A time → simple past."',
  'Box 1: read across: *Have you ever worked in a restaurant? → Yes, I have. / No, I haven\'t.* Point out *Has* with *he / she*. Box 2: the follow-up in the simple past: *When did you go there? → I went in 2022. How was it? → It was exciting.* Box 3: read the 20 verbs together once; learners circle 5 they want to learn first. Box 4: which one? No time or a time.',
  '"*I have seen snow in 2022.* Right or wrong?" (wrong: *I saw snow in 2022.*) • "*Have you ever eat sushi?* Right or wrong?" (wrong: *eaten*) • "*She\'s lived in three cities.* *She\'s* = she is or she has?" (she has).',
  'A asks *Have you ever…?* with a word from the New Words page. B answers *Yes, I have* + a past detail (*I… in…*), or *No, never.* A asks *How was it?* Switch.'),
 brk('*Have you ever…? → Yes, I have. I… (last year). / No, I\'ve never…* and *When did you…? How was it?*'),
 step5('Find Someone Who Has… + Two True, One Invented', 'take the sheet and ask one learner, "Have you ever flown in a plane?" When they say yes, ask two follow-ups: "When did you fly? How was it?" Write their name on your sheet. Say: "Two follow-ups. Then write the name."',
  '**Find Someone Who Has… (mingle).** Learners stand with the Talk Time sheet and ask classmates. When someone says *Yes*, they ask two follow-ups in the past (*When? Where? How was it?*) and write the name and a short note. One name per classmate, then move on.',
  '**Two True, One Invented (groups).** Each learner writes three sentences on the second Talk Time page: two true and one invented (*I\'ve… / I\'ve never…*). The others in the group ask follow-up questions and then guess the invented one.',
  'whole-room mingle for round 1; then 5 groups of 3 for round 2.', 'mingle in one circle for round 1; then 2 groups for round 2.',
  'one group. In round 1, each person asks every other person 2 prompts. Round 2 in the same group.',
  extra=['**Baseline snapshot (during Talk Time):** listen to about 5 learners for 1 minute each (a different 5 each week until you have heard everyone). For each one, note: 3 connected sentences? a follow-up question? any present perfect? Use the snapshot notes in the Teacher notes. This is not a test; don\'t tell learners a score.']),
 step6('Meet Our Class + an email to the teacher', 'Learners read the three profiles on the Read & Write page.',
  'Learners write an email to you (5–8 sentences): who they are, two things they\'ve done, one thing they\'ve never done, and one goal for this class with a reason. Show the example email. Invented details are fine.',
  extra=['**Can-Do Self-Check (3 min, 7:22–7:25):** read each line on the Can-Do Self-Check page aloud. Learners check one face for each line and write one goal. Collect it with the exit ticket. This page comes back in Weeks 8 and 15.']),
 step7('Tell me about something you have done (or never done).', 'I\'ve ridden a horse. I rode one in 2015 on my uncle\'s farm. It was exciting, but I was scared because the horse was big.',
  'item 1: *I / never / see / the ocean → I\'ve never seen the ocean.*'),
]
L['steps'][6][1][2] = L['steps'][6][1][2].replace('(4 min)', '(3 min)')
L['steps'][6][1][4] = L['steps'][6][1][4].replace('(5 min)', '(4 min)')
L['steps'][6] = ('Step 6 · 7:15–7:25 · Read & Write: Meet Our Class + an email to the teacher (+ Can-Do Self-Check) · 10 min', L['steps'][6][1])
L['listen'] = dict(title='Have You Ever…?', voices={'Narrator': 'N', 'Lucía': 'Rosa', 'Ahmed': 'Marco', 'Ms. Grant': 'Kim'},
 female=['Narrator', 'Lucía', 'Ms. Grant'], names=['Lucía', 'Ahmed', 'Grant'], tts={},
 setting='It\'s the first night of an evening English class. Lucía and Ahmed meet. Then the teacher, Ms. Grant, gives them a job.',
 intro='Lesson one. It\'s the first night of an English class at a community center. Lucía and Ahmed meet before class.',
 lines=[
  ('Ahmed', 'Hi, I\'m Ahmed. Is this seat free?'),
  ('Lucía', 'Sure. I\'m Lucía. Nice to meet you. Is this your first class here?'),
  ('Ahmed', 'Yes, it is. Have you ever taken a class at this center?'),
  ('Lucía', 'No, I haven\'t. But my sister has. What kind of work do you do?'),
  ('Ahmed', 'I work at a warehouse. Have you ever worked in a restaurant?'),
  ('Lucía', 'Yes, I have. I worked in a pizza restaurant in 2019. It was hard, but I liked it.'),
  ('Ms. Grant', 'Good evening! I\'m Ms. Grant, your teacher. Tonight we\'re gonna find things we have in common.'),
  ('Ms. Grant', 'Lucía and Ahmed, find two things you\'ve both done.'),
  ('Lucía', 'OK. Ahmed, have you ever seen snow?'),
  ('Ahmed', 'Yes! I saw snow for the first time last winter. It was cold, but beautiful.'),
  ('Lucía', 'Me too. I\'ve seen snow two times. Have you ever ridden a horse?'),
  ('Ahmed', 'No, never. I\'ve never ridden a horse. Have you?'),
  ('Lucía', 'Yes, I have.'),
  ('Ahmed', 'Really? When did you do that?'),
  ('Lucía', 'When I was ten, on my uncle\'s farm. OK, snow is one thing. Have you ever run a race?'),
  ('Ahmed', 'Yes, I ran a 5k last year. I didn\'t win, but I finished!'),
  ('Lucía', 'I\'ve run a race, too. My company has a race every summer.'),
  ('Ahmed', 'Great. So we\'ve both seen snow, and we\'ve both run a race.'),
  ('Ms. Grant', 'Good job! Now, what have you never done, but you wanna try?'),
  ('Ahmed', 'I wanna go camping. I\'ve never slept in a tent.'),
  ('Lucía', 'And I wanna try sushi. I\'ve never eaten it.'),
 ],
 A=dict(q='What have Lucía and Ahmed both done?', opts=['ridden a horse and gone camping', 'seen snow and run a race', 'worked in a restaurant and eaten sushi'], ans=1),
 B=dict(head='Check ✓ True or False.', kind='tf', items=[
  dict(s='Lucía has taken a class at this center before.', a=False, fix='No, she hasn\'t; her sister has', ev='No, I haven\'t. But my sister has.'),
  dict(s='Lucía worked in a pizza restaurant in 2019.', a=True, ev='I worked in a pizza restaurant in 2019'),
  dict(s='Ahmed saw snow for the first time last winter.', a=True, ev='I saw snow for the first time last winter'),
  dict(s='Ahmed has ridden a horse.', a=False, fix='he has never ridden a horse', ev='I\'ve never ridden a horse'),
  dict(s='Ahmed won his race.', a=False, fix='he didn\'t win, but he finished', ev='I didn\'t win, but I finished'),
  dict(s='Lucía has never eaten sushi.', a=True, ev='I wanna try sushi. I\'ve never eaten it.'),
 ]),
 C=dict(head='Write *have*, *has*, or *did*.', items=[
  '[Have] you ever taken a class at this center?', 'No, I haven\'t. But my sister [has].', '[Have] you ever worked in a restaurant?',
  'Really? When [did] you do that?', 'Ahmed, [have] you ever seen snow?', 'I\'ve run a race, too. My company [has] a race every summer.']),
 hear='*gonna* = going to: "Tonight we\'re **gonna** find things we have in common." • *wanna* = want to: "I **wanna** go camping." You can say *going to* and *want to*. Say it: *Have you ever seen snow?* • *I\'ve never ridden a horse.*',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: *Have you ever…?* (sometime in your life)

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Have** you **ever** | worked in a restaurant? | ‖ | Yes, I **have**. | I**'ve** worked in two restaurants. |
| ^ | ^ | ‖ | No, I **haven't**. / No, **never**. | I**'ve never** worked in a restaurant. |
| **Has** she **ever** | seen snow? | ‖ | Yes, she **has**. | She**'s** seen snow two times. |
| **Has** he **ever** | lived in a big city? | ‖ | No, he **hasn't**. | He**'s never** lived in a big city. |

### Grammar Box 2: the details (simple past)

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Have** you **ever** | been to Chicago? | ‖ | Yes, I **have**. | I **went** there in 2022. |
| **When did** you | go there? | ‖ | I **went** | last summer. / in 2022. |
| **How was** | it? | ‖ | It **was** | exciting. / a little boring. |
| **Did** you | like it? | ‖ | Yes, I **did**. / No, I **didn't**. | It was too cold! |
''',
rule='sometime in your life, **no time** → *have / has* + past participle (*I\'ve seen snow*). **Add a time** (*in 2022, last year, when I was ten*) → simple past (*I saw snow last year*).',
explain='''
### Grammar Box 3: 20 verbs to know (verb → past → **past participle**)

| | | | |
|---|---|---|---|
| be → was / were → **been** | go → went → **gone / been** | ride → rode → **ridden** | travel → traveled → **traveled** |
| do → did → **done** | have → had → **had** | run → ran → **run** | try → tried → **tried** |
| drive → drove → **driven** | live → lived → **lived** | see → saw → **seen** | win → won → **won** |
| eat → ate → **eaten** | make → made → **made** | swim → swam → **swum** | work → worked → **worked** |
| fly → flew → **flown** | meet → met → **met** | take → took → **taken** | write → wrote → **written** |

*Regular verbs (live, work, travel): past participle = past form (*-ed*).* • ***I\'ve*** *= I have.* • ***She\'s lived*** *= she **has** lived (not she is).*

### Grammar Box 4: Which one?

| | WHEN? | EXAMPLE |
|---|---|---|
| *have / has* + past participle | sometime in your life; **no time** | *I've ridden a horse. She's never flown.* |
| simple past | a **finished time** (*in 2015, last year, when I was ten*) | *I rode a horse in 2015. She flew to Texas last year.* |
''',
qa=[('Can I say *I have seen snow in 2022*?', 'No. With a finished time, use the simple past: ***I saw snow in 2022.***'),
 ('Why *eaten*, not *eat*?', 'After *have / has*, use the **past participle**: ***Have you ever eaten sushi?*** Look at Box 3.'),
 ('How do I answer *Have you ever…?* short?', '***Yes, I have.*** or ***No, I haven\'t.*** or ***No, never.*** Then add a detail in the past: ***Yes, I have. I went there in 2022.***')],
A=dict(head='Write the past participle.', items=['Have you ever [eaten] sushi? (eat)', 'I\'ve never [ridden] a horse. (ride)', 'She has [lived] in three cities. (live)',
 'Have you ever [flown] in a plane? (fly)', 'We\'ve [seen] the ocean two times. (see)', 'He\'s never [won] a prize. (win)']),
B=dict(head='Circle the correct words.', items=['{{*Have|Did}} you ever tried Thai food?', 'I {{*went|have gone}} to Texas last year.',
 'Have you ever seen the ocean? Yes, I {{*have|have seen}}.', 'When {{*did you go|have you gone}} there?', 'She {{*has never|never have}} eaten sushi.',
 'I {{*saw|\'ve seen}} a famous person in 2023.']),
mistakes=[('I have seen snow last year.', 'I **saw** snow last year.'), ('Have you ever eat sushi?', 'Have you ever **eaten** sushi?'),
 ('Yes, I have seen.', 'Yes, I **have**. (+ a detail: *I saw it in 2022.*)'), ('She have lived in two cities.', 'She **has** lived in two cities.'),
 ('I never have flown.', 'I\'ve **never** flown. / I have **never** flown.')],
tip='Spanish has a similar form (*¿Alguna vez has trabajado…?*), but English never uses a finished time with it: *I worked there in 2020* (not *I\'ve worked there in 2020*). What does your language do?')
FSW = '\n'.join(f'| {i}. Have you ever {p}? | <br> | <br> |' for i, p in enumerate(['tried a food from another country', 'flown in a plane', 'seen the ocean', 'run a race',
 'gone camping', 'won a prize', 'ridden a horse', 'worked at night', 'cooked for 20 people', 'seen a famous person'], 1))
L['talk'] = dict(pages=[('Find Someone Who Has…', '''
### Round 1. Stand up. Ask your classmates. When someone says *Yes*, ask two follow-up questions. Write the name and a short note.

*Example:* A: Have you ever flown in a plane? B: Yes, I have. A: When did you fly? B: Last year. A: How was it? B: It was exciting! → **Name:** Ana **Note:** last year, exciting

| Question | Name | Note (When? Where? How was it?) |
|---|---|---|
''' + FSW + '''

*Follow-ups:* **When did you…? • Where did you…? • How was it? • Did you like it? • Why?**
'''), ('Two True, One Invented', '''
### Round 2. Work in a group. Write 3 sentences: 2 are true and 1 is invented. Read them. Your group asks follow-up questions. Then they guess the invented one.

*Example:* 1. I've ridden a horse. 2. I've never seen snow. 3. I've won a prize for cooking. → *When did you win it? What did you cook?*

| My 3 sentences (*I've… / I've never…*) |
|---|
| 1. <br><br> |
| 2. <br><br> |
| 3. <br><br> |

### Write two follow-up questions you asked a classmate.

| My follow-up questions (*When did you…? How was it?*) |
|---|
| 1. <br><br> |
| 2. <br><br> |

### Write one thing you and a classmate have both done.

*Example:* Ana and I have both seen the ocean.

______________________________________________________________
''')])
L['hw'] = dict(one=dict(head='Write the sentence. Use the words.', example='you / ever / try / Thai food? → *Have you ever tried Thai food?*',
 items=[('I / never / see / the ocean', 'I\'ve never seen the ocean.'), ('she / ever / ride / a horse?', 'Has she ever ridden a horse?'),
  ('we / fly / to Miami / two times', 'We\'ve flown to Miami two times.'), ('he / go / camping / last summer', 'He went camping last summer.')]),
 three='''### 3. Ask a family member or a friend 3 questions with *Have you ever…?* When the answer is *Yes*, ask *When?* and *How was it?* Write the answers.

| Question | Answer (*Yes, I have. I… / No, never.*) |
|---|---|
| 1. <br><br> | <br> |
| 2. <br><br> | <br> |
| 3. <br><br> | <br> |
''',
 four=dict(head='Review (simple past). Write the past form.', items=['I [went] to the park last weekend. (go)', 'We [ate] at my cousin\'s house on Sunday. (eat)',
  'She [didn\'t work] last Saturday. (not work)', '[Did] you [watch] the game? (watch)', 'The movie [was] exciting. (be)']))
L['rw'] = dict(kind='class page', note='Read fast first. Then read again and answer the questions.', box_title='MEET OUR CLASS · Evening English, Room 4',
 text='''
**Marta:** Hi! I'm Marta. I've lived in this city for six years. I've worked in a bakery, a school cafeteria, and now a hospital kitchen. I've never seen the ocean, but I want to see it next summer. I'm in this class because I want to talk more with the nurses at work.

**Joseph:** Hello, my name is Joseph. I drive a truck, so I've traveled to many states. I've seen mountains, deserts, and a lot of snow! I've never flown in a plane. My kids say I need to try it. I want better English for my job and for my kids' school.

**Linh:** Hi, everyone. I'm Linh. I've had many jobs. I've cleaned offices, and I've worked in a nail salon. Last year, I ran my first race, a 5K for a children's hospital. It was hard, but I finished. I've never gone camping. This year, I want to read a whole book in English.
''',
 qs=[('How long has Marta lived in this city?', 'For six years.', 'I\'ve lived in this city for six years'),
  ('Where does Marta work now?', 'In a hospital kitchen.', 'and now a hospital kitchen'),
  ('Why has Joseph traveled to many states?', 'Because he drives a truck.', 'I drive a truck, so I\'ve traveled to many states'),
  ('What has Joseph never done?', 'He\'s never flown in a plane.', 'I\'ve never flown in a plane'),
  ('What did Linh do last year?', 'She ran her first race (a 5K).', 'Last year, I ran my first race')],
 write_head='Write an email to your teacher (5–8 sentences). Say who you are, two things you\'ve done, one thing you\'ve never done, and one goal for this class with a reason.',
 write_short='your email to the teacher',
 example='*Hi, Ms. Grant. My name is Sara. I\'ve worked in a hotel for four years. I\'ve also traveled to New York and Texas. I\'ve never ridden a horse. My goal is to speak English at the doctor\'s office because I want to understand my children\'s doctor. See you next week! Sara*',
 box_label='My email', checklist=['It has 5–8 sentences.', 'It has two things I\'ve done (*I\'ve…*).', 'It has one thing I\'ve never done.', 'It has a goal and a reason (*because…*).'])
L['exit'] = dict(q='Tell me about something you have done (or never done).', s1='the experience (*I\'ve… / I\'ve never…*)', s2='when it happened (*I… in 2020*), or why not',
 s3='how it was, with *because* or *so*', key='*A good answer:* "I\'ve ridden a horse. I rode one in 2015 on my uncle\'s farm. It was exciting, but I was scared because the horse was big."')
L['game'] = ('Yes, I have! / No, never!', 'A points to a picture and asks, "Have you ever **run a race**?" B answers, "Yes, I have. I ran one in 2021." or "No, never." Switch.')
L['opening'] = dict(cards=['**A:** What did you do last weekend?', '**A:** What did you eat last night?', '**A:** Where did you go yesterday?', '**A:** What did you do last summer?'],
 follow='How was it? • Who did you go with? • Why?', hw_head='Write your partner\'s name and one thing your partner did last weekend.', hw_cols=['My partner\'s name', 'One thing my partner did last weekend'])
L['cando'] = ['I can ask *Have you ever…?*', 'I can answer *Yes, I have.* / *No, I\'ve never…*', 'I can ask a follow-up in the past (*When did you…? How was it?*).',
 'I can tell a classmate about one experience in 3 sentences.', 'I can write a short email about myself.']
L['notes'] = [
 '**Learners choose what to share.** Places, foods, and jobs are always safe topics. Never ask how or when learners came to the U.S. Invented answers are fine in every activity.',
 '**The timeline:** keep the "my life → now" line on the board all night. X\'s with no dates = present perfect; a date under an X = simple past.',
 '**Participles:** learners don\'t need all 20 tonight. Ask them to circle 5 in Box 3 and learn those first. The list comes back in Lessons 2 and 3.',
 '**Baseline snapshot:** for each learner you hear (about 5 tonight), note three things: (1) 3 connected sentences? (2) a follow-up question? (3) any present perfect? Keep the notes private. Hear everyone by Week 3. The same notes help in Weeks 8 and 15.',
 '**Can-Do Self-Check:** the faces are 😀 I can do it, 🙂 with a little help, 😐 not yet. Read each line aloud. Keep the pages; learners compare in Week 8.',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening has *gonna* and *wanna*. Learners need to understand them; they can always say *going to* and *want to*.']
