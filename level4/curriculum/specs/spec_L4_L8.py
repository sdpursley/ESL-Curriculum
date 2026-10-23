import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=8, week=9, title='In the News',
topic='Understanding short local news reports and city notices: a road closure, a bus detour, a water pipe repair, a new bus route, a new store. Learners say what might or may happen and ask *Do you know where / when / why…?*. All stories, streets, and cities are invented and neutral.',
cq='Are you sure, or is it maybe?',
builds=[
 ('*maybe, probably*; *will* for predictions', 'Level 3', '***might / may / could*** + base verb for possibility: *It might open next week.*'),
 ('*Where is…? / When does…?* questions', 'Levels 1–3', '***Do you know where the meeting is?*** (statement order; a first look)'),
 ('past continuous + *when*', 'Level 3 Lesson 4', 'news language: *Workers were fixing a pipe when…*'),
],
objectives=['understand the main points of a short local news report',
 'say what might or may happen, and what will happen',
 'ask *Do you know where / when / why…?* with statement order',
 'tell a classmate about a local news story',
 'write a text or email (5–8 sentences) telling a friend the news'],
materials=['Board and markers', 'News cards A and B and a headline (in the workbook Talk Time pages; copy them onto index cards, optional)', 'A local map or a drawing of streets (optional, for the warm-up)'],
prep='15 minutes (read the plan; practice reading the listening script; practice the news reader\'s pauses)',
words=[('news', 'news', True), ('reporter', 'reporter', True), ('headline', 'headline', True), ('road closure', 'road_closure', True), ('detour', 'detour', True),
 ('construction', 'construction', True), ('water pipe', 'water_pipe', True), ('bus route', 'bus_route', True), ('delay', 'delay', True), ('announce', 'announce', True),
 ('update', 'update', True), ('local', 'local', False)],
more_vocab='*Also:* a rider, a stop, a schedule, a website, a transit office, service, replace, connect, expect, post (online).',
clock=clock('', ' (+ My Words)', '', '*might / may / could; Do you know where…?*', 'News Swap + What Might Happen?', 'A local news article; a text to a friend',
 talk_group='Pairs, then groups'),
attend='With 5 or fewer, do News Swap in pairs (you take a card if there is an odd number), then What Might Happen? as one group. Late arrivals get news card A or B and join a pair.',
)
L['steps'] = [
 step1('Opening Talk', '*too / enough; must / mustn\'t / don\'t have to*',
  'you say, "Is 6:55 early enough for a 7:00 shift?" The learner answers with *too* or *enough* and a reason. Then you ask, "What must you wear at your job or school?" Help them say 3 sentences.',
  'Pairs compare Homework item 1 (*too / enough / mustn\'t*) and read their 3 rules (item 3) to each other. Then they fill in the box on the Opening Talk page. Also return the midterm and go over 2 common mistakes.',
  '*It\'s enough big* (→ *It\'s big enough*) and *You don\'t have to smoke here* for a rule (→ *You mustn\'t smoke here*)'),
 step2('*news*, *local* (in our city); *reporter* (the person who tells the news); *headline* (the big words at the top); *road closure* and *detour* (draw a street with an X and an arrow around it); *construction*; *water pipe*; *bus route*; *delay* (the bus is late); *announce* (say it to everyone); *update* (new information).',
  'ask "If the road is closed, does the bus take a detour?" (yes) • "Is a headline long or short?" (short) • "If there is a delay, is the bus early or late?" (late).',
  'The road might be closed until Friday.'),
 step3('First, you\'ll hear a short local news report on the radio. Then two coworkers, Marco and Joy, talk about the news. Listen: what is the news?',
  'Point to the script lines. *gonna* = going to: "The bus is **going to** take a detour." Then practice *might* (the last *t* is very short: *It migh\' be late*) and *Do you know…?* with the voice going up at the end. Listen to the reporter\'s pauses.', '{EST}'),
 step4('*might / may / could; Do you know where…?*', 'draw a cloud. Say, "Will it rain tomorrow? I\'m not sure. It **might** rain. It **may** rain." Draw a sign *ROAD CLOSED MONDAY*: "The road **will** close on Monday. I\'m sure." Then ask a learner, "**Do you know where** the library **is**?" Write it and underline *the library is*: "Statement order."',
  'Box 1: read across: *Will the road be closed tomorrow? → It might be. / It may be closed until Friday.* Box 2: *Do you know where / when / what time / why…?* Box 3: *will* (sure) vs. *might* (maybe). Box 4: from a question to *Do you know…?*',
  '"*It might rains* or *It might rain*?" (*might rain*) • "*Do you know where is the bank* or *where the bank is*?" (*where the bank is*) • "The sign says *Closed Monday*. *will* or *might*?" (*will*).',
  'A points to a picture and asks, "Do you know when the **construction** ends?" B answers with a fact or *I\'m not sure. It might…* Switch.'),
 brk('*It might / may / could + base verb (maybe) • It will… (sure) • Do you know where the meeting is? (statement order)*'),
 step5('News Swap + What Might Happen?', 'hold news card A. Ask a learner, "Do you know when the library will open on Sundays?" Help them find it and answer, "Yes, starting March 3." Then ask, "Do you know why?" Say: "Ask with *Do you know…?* Answer with a fact, or say *I\'m not sure. It might…*"',
  '**News Swap (pairs).** A and B have different news cards. Partners ask *Do you know when / where / why…?* and write the facts. Then they change partners and retell their partner\'s story.',
  '**What Might Happen? (groups).** Groups choose a headline and write 4 predictions with *might*, *may*, and *will probably*. Then they read them to the class.',
  'pairs with one rotation for round 1; then groups of 4.', 'pairs for round 1; then 2 groups.',
  'pairs for round 1 (you take a card if there is an odd number); then one group.'),
 step6('A local news article', 'Learners read the news article on the Read & Write page, find the main idea, and answer the questions.',
  'Learners write a text or email to a friend about the news (5–8 sentences) with one *might* or *may* and one *Do you know…?*. Show the example.'),
 step7('What might change in your neighborhood or at your job next year?', 'A new store might open near my house. My job may change my schedule. I think so because there\'s construction on my street and my company is very busy.',
  'item 1: *the store / may / open / in June → The store may open in June.*'),
]
L['listen'] = dict(title='In the News', voices={'Narrator': 'N', 'Diane Lee': 'Receptionist', 'Marco': 'Marco', 'Joy': 'Kim'},
 female=['Narrator', 'Diane Lee', 'Joy'], names=['Diane', 'Lee', 'Marco', 'Joy', 'Oak', 'Pine'], tts={},
 setting='A short local radio news report about a road closure and a bus detour. Then, at work, two coworkers, Marco and Joy, talk about how it might change their commute.',
 intro='Lesson eight. First, listen to a short news report on the radio. Then two coworkers talk about the news.',
 lines=[
  ('Diane Lee', 'Good morning. This is Diane Lee with your local news. Starting Monday, Oak Street will be closed between First and Fifth Avenue. Workers are going to replace an old water pipe under the street.'),
  ('Diane Lee', 'The city says the construction might take two weeks. It may take longer if it rains.'),
  ('Diane Lee', 'During the road closure, the number twelve bus will take a detour on Pine Street. Riders should expect delays of about fifteen minutes. The city will post updates on its website. I\'m Diane Lee, and that\'s the news.'),
  ('Narrator', 'Later that morning, at work, Marco and Joy talk about the news.'),
  ('Marco', 'Joy, did you hear the news? They\'re closing Oak Street on Monday.'),
  ('Joy', 'Oh no. I take the number twelve bus on Oak Street every day.'),
  ('Marco', 'The bus is going to take a detour on Pine Street. It might be fifteen minutes late.'),
  ('Joy', 'Fifteen minutes? I might be late for work. Do you know when the bus leaves Pine Street?'),
  ('Marco', 'I\'m not sure. You could check the city website.'),
  ('Joy', 'Good idea. Do you know how long the closure is?'),
  ('Marco', 'They said two weeks. But it might take longer if it rains.'),
  ('Joy', 'Hmm. Maybe I\'ll take the earlier bus. I don\'t want to be late.'),
  ('Marco', 'Or I could give you a ride. I drive past your street.'),
  ('Joy', 'Really? That would be great. Do you know where the detour starts?'),
  ('Marco', 'I think it starts at First Avenue. I\'m going to look at the map tonight.'),
  ('Joy', 'Thanks, Marco!'),
 ],
 A=dict(q='What is the news?', opts=['Oak Street will close for a water pipe repair.', 'A new grocery store is opening.', 'The bus will be free next week.'], ans=0),
 B=dict(head='Complete the notes. Circle the answer.', kind='choice', items=[
  dict(s='Where: Oak Street, between First and {{*Fifth|Ninth}} Avenue', ev='between First and Fifth Avenue'),
  dict(s='When: starting {{*Monday|Friday}}', ev='Starting Monday'),
  dict(s='Why: workers will replace an old {{*water pipe|bus stop}}', ev='replace an old water pipe'),
  dict(s='How long: maybe {{*two weeks|two days}}', ev='the construction might take two weeks'),
  dict(s='The bus detour: on {{*Pine Street|Main Street}}', ev='the number twelve bus will take a detour on Pine Street'),
  dict(s='Delays: about {{*fifteen|fifty}} minutes', ev='delays of about fifteen minutes'),
 ]),
 C=dict(head='Write the missing word: *might*, *will*, or a question word.', items=[
  'The city says the construction [might] take two weeks.', 'The city [will] post updates on its website.', 'Do you know [when] the bus leaves Pine Street?',
  'Do you know [how] long the closure is?', 'But it [might] take longer if it rains.', 'Do you know [where] the detour starts?']),
 hear='*gonna* = going to: "The bus is **going to** take a detour." • "I\'m **going to** look at the map tonight." You can say *going to*. In *might*, the last *t* is very short. In *Do you know…?*, the voice goes up at the end. Listen to the reporter: she pauses after each fact.',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: *might / may / could* (maybe)

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Will** the road | **be** closed tomorrow? | ‖ | It **might be**. | I'm not sure. |
| **Will** the repair | **take** two weeks? | ‖ | It **may take** longer. | It depends on the rain. |
| **When will** the road | **open**? | ‖ | I'm not sure. | It **could open** next week. |
| **Will** the bus | **be** on time? | ‖ | It **might not be**. | It **might be** 15 minutes late. |

### Grammar Box 2: *Do you know where…?* (a first look)

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Do you know** | **where** the meeting **is**? | ‖ | Yes, it's | at the library. |
| **Do you know** | **when** the new bus route **starts**? | ‖ | I think | it starts in May. |
| **Do you know** | **what time** the store **opens**? | ‖ | I'm not sure. | It might open at 8:00. |
| **Do you know** | **why** the street **is** closed? | ‖ | Yes. Workers | are fixing a water pipe. |
''',
rule='***might / may / could*** + base verb: never *to*, never *-s* (*It might **rain***). After ***Do you know where / when / why***, use statement order: *where **the meeting is*** (not *where is the meeting*).',
explain='''
### Grammar Box 3: *will* (sure) or *might* (maybe)?

| | HOW SURE? | EXAMPLE |
|---|---|---|
| *will* | sure | *The road will close at 8:00 on Monday.* |
| *will probably* | almost sure | *It will probably take two weeks.* |
| *might / may / could* | maybe | *It might open early.* |
| *might not / may not* | maybe not | *The bus might not be on time.* |

### Grammar Box 4: from a question to *Do you know…?*

| QUESTION | *DO YOU KNOW…?* |
|---|---|
| *Where is the meeting?* | *Do you know where the meeting is?* |
| *When does the bus leave?* | *Do you know when the bus leaves?* (no *does*; add *-s*) |
| *Why is the street closed?* | *Do you know why the street is closed?* |
''',
qa=[('*It might rains* or *It might rain*?', '*might* + base verb: ***It might rain.*** Never *-s*, never *to*.'),
 ('Can I say *Do you know where is the meeting?*', 'Use statement order: ***Do you know where the meeting is?***'),
 ('*will* or *might*?', '***will*** = I\'m sure. ***might*** = maybe. *The road **will** close on Monday. It **might** open early.*')],
A=dict(head='Write the correct word or form.', items=['It\'s very cloudy. It [might] rain later. (might / will)', 'The sign says the road [will] close at 8:00 on Monday. (might / will)',
 'The store might [open] next month. (open)', 'Do you know where the library [is]? (be)', 'Do you know when the bus [leaves]? (leave)',
 'I\'m not sure. The bus may [be] late. (be)']),
B=dict(head='Circle the correct words.', items=['The repair might {{*take|to take}} two weeks.', 'Do you know {{*where the meeting is|where is the meeting}}?',
 'It {{*might not|doesn\'t might}} rain tomorrow.', 'Do you know what time the store {{*opens|does open}}?', 'The schedule says the bus {{*will|might}} leave at 7:05. (sure)',
 'I\'m not sure. It {{*may|will}} open in June. (maybe)']),
mistakes=[('It might rains tomorrow.', 'It might **rain** tomorrow.'), ('The road might to close.', 'The road might **close**.'),
 ('Do you know where is the bank?', 'Do you know where **the bank is**?'), ('Do you know when does the bus leave?', 'Do you know when **the bus leaves**?'),
 ('I\'m sure. The road might close at 8:00.', 'I\'m sure. The road **will** close at 8:00.')],
tip='Spanish *Puede que cierren la calle* uses a special verb form; English uses *might* + base verb: *They might close the street* (not *might to close*, not *might closes*). Spanish *¿Sabes dónde está…?* keeps the verb right after *dónde*; English moves it: *Do you know where the meeting **is**?* What does your language do?')
L['talk'] = dict(pages=[('News Swap', '''
### Round 1. Work with a partner. A reads card A, and B reads card B. Don't show your card. Ask *Do you know when / where / why…?* and write your partner's facts. Then change partners and retell the story.

| NEWS CARD A (invented) | NEWS CARD B (invented) |
|---|---|
| **Hill Street Library open on Sundays** | **Main Street bus stop is moving** |
| When: starting March 3 | When: next Monday |
| Hours: 12:00 to 5:00 | Where: from 2nd Street to 4th Street |
| Why: many families asked for weekend hours | Why: construction on a new grocery store |
| Maybe: free computer classes might start in April | How long: about 6 months |
| Where to learn more: the library website | Maybe: there may be a new crosswalk |

*Example:* A: Do you know when the bus stop is moving? B: Yes, next Monday. A: Do you know why? B: Because there's construction on a new grocery store.

| My partner's news | Facts |
|---|---|
| When? | |
| Where? | |
| Why? | |
| Maybe…? (*might / may*) | |
'''), ('What Might Happen?', '''
### Round 2. Work in groups. Choose a headline. Write 4 predictions with *might*, *may*, and *will probably*. Then read them to the class.

| HEADLINE 1 (invented) | HEADLINE 2 (invented) |
|---|---|
| **New Grocery Store Opening on Main Street** | **Big Snowstorm Coming This Weekend** |

*Example (headline 1):* "There might be more traffic on Main Street. Food prices may go down. The store will probably need workers. Some small stores might close."

| Our predictions | ✓ |
|---|---|
| 1. ___ might ___ <br> | ☐ |
| 2. ___ may ___ <br> | ☐ |
| 3. ___ will probably ___ <br> | ☐ |
| 4. <br> | ☐ |

| A prediction from another group that I liked |
|---|
| <br><br> |

*Useful:* There might be… • People may… • It will probably… • I'm not sure, but… • I think so too. • Maybe, but…
''')])
L['hw'] = dict(one=dict(head='Write the sentence or question. Use the words.', example='the road / might / close / tomorrow → *The road might close tomorrow.*',
 items=[('the store / may / open / in June', 'The store may open in June.'), ('it / might not / rain / this weekend', 'It might not rain this weekend.'),
  ('Do you know / where / the meeting / be?', 'Do you know where the meeting is?'), ('Do you know / when / the bus / leave?', 'Do you know when the bus leaves?')]),
 three='''### 3. Write 3 things that might change in your neighborhood or city. Then write why you think so.

| What might change? (*might / may*) | Why do you think so? |
|---|---|
| 1. <br><br> | <br><br> |
| 2. <br><br> | <br><br> |
| 3. <br><br> | <br><br> |
''',
 four=dict(head='Review (Lesson 7). Write one word.', items=['Is 6:55 early [enough] for a 7:00 shift?', 'There are too [many] people here.',
  'You [mustn\'t] use your phone in the kitchen. (It\'s a rule.)', 'Jeans are [too] casual for an interview.', 'I have too [much] work today.']))
L['rw'] = dict(kind='notice', note='Read fast first: what is the main idea? Then read again and answer the questions.', box_title='MAPLE FALLS NEWS · New Bus Route Will Connect Hospital and College (invented city)',
 text='''
Starting May 6, Maple Falls will have a new bus route, Route 9. The route will go from Riverside Hospital to Maple Falls Community College, with stops at the library, the West Side Market, and the train station. Buses will run every 20 minutes from 6:00 a.m. to 10:00 p.m., Monday to Saturday. A ride will cost $1.50, the same as other city buses.

"Many people asked for this route," said Ana Ruiz from the city transit office. "Nurses and students wanted an easier way to get to work and class." Students are happy too. "Now I don't have to take two buses," said one student.

The city might add Sunday service in the fall. It may also add two more stops near the new apartments on Elm Road, but this isn't decided yet.

Riders can see the map and the schedule on the city website or at the library. For the first week, all rides on Route 9 will be free.
''',
 qs=[('What is the main idea?', 'A new bus route, Route 9, will start on May 6.', 'Starting May 6, Maple Falls will have a new bus route, Route 9'),
  ('How often will the buses run?', 'Every 20 minutes.', 'Buses will run every 20 minutes'),
  ('How much will a ride cost?', '$1.50 (and free for the first week).', 'A ride will cost $1.50'),
  ('What might the city add in the fall?', 'Sunday service.', 'The city might add Sunday service in the fall'),
  ('Where can riders see the map?', 'On the city website or at the library.', 'on the city website or at the library')],
 write_head='Write a text or email to a friend about the news (5–8 sentences). Use one *might* or *may* and one *Do you know…?*',
 write_short='your text or email',
 example='*Hi, Lina! Did you hear the news? There\'s a new bus route, Route 9. It starts on May 6, and it goes to the college. You could take it to class! The city might add Sunday service in the fall. Do you know when your classes start? Talk soon, Joy*',
 box_label='My text or email', checklist=['It has 5–8 sentences.', 'It tells the main news.', 'It has *might* or *may*.', 'It has a *Do you know…?* question.'])
L['exit'] = dict(q='What might change in your neighborhood or at your job next year?', s1='one change, with *might* or *may*', s2='another change, with *might* or *may*',
 s3='a reason, with *because*', key='*A good answer:* "A new store might open near my house. My job may change my schedule. I think so because there\'s construction on my street and my company is very busy."')
L['game'] = ('Do you know…?', 'A points to a picture and asks, "Do you know when the **construction** ends?" B answers with a fact or "I\'m not sure. It might end in May." Switch.')
L['opening'] = dict(cards=['**A:** Is 6:55 early enough for a 7:00 shift?', '**A:** What must you wear at your job or school?', '**A:** Are jeans OK for a job interview?', '**A:** What is too expensive in this city?'],
 follow='Why? • Is it the same in your hometown? • What don\'t you have to do?', hw_head='Write your partner\'s name and one rule from Homework item 3.', hw_cols=['My partner\'s name', 'A rule (*must / mustn\'t / don\'t have to*)'])
L['notes'] = [
 '**Class stories only:** all news is invented and neutral (roads, buses, a library, a store). No politics, crime, injuries, or real current events. If a learner brings up real news, say, "Let\'s keep to our class stories."',
 '**After the midterm:** this is Week 9. Return the midterm in the Opening Talk and put 2 common mistakes on the board.',
 '***Do you know where…?* is a first look:** practice it with *where / when / what time / why* only. Don\'t teach *if / whether* (Level 5).',
 '***might* + base verb:** learners often add *to* or *-s*. Point to the rule: no *to*, no *-s*.',
 '**News Swap:** learners keep their card hidden. If a partner can\'t find a fact, they say, "I\'m not sure. It might…"',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening says *going to*. People often say *gonna*. Learners only need to recognize it; they can always say the full form.']
