import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=9, week=10, title='I See Your Point',
topic='Giving, asking for, and politely disagreeing with an opinion at a neighborhood meeting about an empty lot (a playground, a parking lot, or a community garden), and writing a short opinion paragraph. Learners use opinion phrases, *as … as / not as … as*, and paragraph words. All places, people, and plans are invented and local.',
cq='Do you agree? How do you say it politely?',
builds=[
 ('*I think…*; *because*', 'Level 3', 'opinion phrases: ***In my opinion… / I see your point, but…***'),
 ('comparatives (*cheaper than, more expensive than*)', 'Level 2', '***as … as / not as … as***: *A garden isn\'t as expensive as a parking lot.*'),
 ('second conditional', 'Level 4 Lesson 6', '*If we had a playground, kids would play outside more.*'),
],
objectives=['give an opinion with a reason',
 'ask for someone\'s opinion (*What do you think about…? / How do you feel about…?*)',
 'agree and disagree politely (*I agree. / I see your point, but…*)',
 'compare two ideas with *as … as / not as … as*',
 'write an opinion paragraph (5–8 sentences) with *First… Also… That\'s why…*'],
materials=['Board and markers', 'Role cards (in the workbook Talk Time page; copy them onto index cards, optional)', 'Three signs for the room: AGREE, NOT SURE, DISAGREE (for Opinion Lines)'],
prep='15 minutes (read the plan; practice reading the listening script; put the three signs on the walls)',
words=[('opinion', 'opinion', True), ('agree', 'agree', True), ('disagree', 'disagree', True), ('point (I see your point)', 'point', True), ('community meeting', 'community_meeting', True),
 ('empty lot', 'empty_lot', True), ('community garden', 'community_garden', True), ('parking lot', 'parking_lot', True), ('playground', 'playground', True), ('survey', 'survey', True),
 ('vote (raise your hand)', 'vote', True), ('advantage / disadvantage', 'advantage', False)],
more_vocab='*Also:* a neighbor, a plan, a flyer, a newsletter, a parking space, a bench, a bus shelter, fair, take care of, a topic sentence.',
clock=clock('', ' (+ My Words)', '', '*opinions; agree / disagree politely; as … as*', 'Community Meeting + Opinion Lines', 'A meeting flyer + two letters; an opinion paragraph',
 talk_group='Groups of 4, then the whole room'),
attend='With 5 or fewer, do Community Meeting as one group; you take a role card. Do Opinion Lines with everyone. Late arrivals take a role card and join a group.',
)
L['steps'] = [
 step1('Opening Talk', '*might / may / could; Do you know where…?*',
  'you say, "Do you know when the library opens?" The learner answers with a fact or *I\'m not sure. It might…* Then you ask, "What might change in this city next year?" Help them say 3 sentences.',
  'Pairs compare Homework item 1 (*might* and *Do you know…?*) and read their 3 changes (item 3) to each other. Then they fill in the box on the Opening Talk page.',
  '*It might rains* (→ *It might rain*) and *Do you know where is the bank?* (→ *where the bank is*)'),
 step2('*opinion* (what you think); *agree* (thumbs-up) and *disagree* (thumbs-down, with a smile); *I see your point* (I understand you); *community meeting*; *empty lot* (land with nothing on it); *community garden*, *parking lot*, *playground*; *survey* (questions for many people); *vote* (raise your hand); *advantage* (a plus) and *disadvantage* (a minus).',
  'ask "Is an empty lot full or empty?" (empty) • "If you agree, do you say *That\'s true* or *That\'s wrong*?" (*That\'s true*) • "Is a survey for one person or many people?" (many people).',
  'In my opinion, we need a playground.'),
 step3('Neighbors are at a community meeting. Mrs. Okafor is the leader. Ray and Lynn give their opinions about the empty lot on Cedar Street. Listen: what are they deciding?',
  'Point to the script lines. *wanna* = want to: "Tonight we **want to** talk about the empty lot." *gonna* = going to: "Who\'s **going to** take care of it?" Then practice *I see your POINT, but…* (the voice goes down on *point*, then a short pause) and the stress in *It isn\'t as EXpensive*.', '{EST}'),
 step4('*opinions; agree and disagree politely; as … as*', 'say, "In my opinion, summer is the best season." Ask a learner, "Do you agree?" Model two answers: a thumbs-up, "**I agree.** That\'s true," and a smile, "**I see your point, but** I like fall." Write: *something positive first, then* but. Then draw two prices: "A garden is $2,000. A parking lot is $20,000. A garden **isn\'t as expensive as** a parking lot."',
  'Box 1: read across: *What do you think about the empty lot? → I think we need a playground.* Box 2: agreeing and disagreeing politely. Box 3: *as … as / not as … as*. Box 4: the words in an opinion paragraph.',
  '"*I am agree* or *I agree*?" (*I agree*) • "Which is more polite: *That\'s wrong* or *I see your point, but…*?" (*I see your point, but…*) • "*not as expensive as* or *not as expensive than*?" (*as … as*).',
  'A points to a picture and asks, "What do you think about a **playground** for the lot?" B gives an opinion and a reason. A agrees or disagrees politely. Switch.'),
 brk('*What do you think about…? → In my opinion… • I agree. / I see your point, but… • A garden isn\'t as expensive as a parking lot.*'),
 step5('Community Meeting + Opinion Lines', 'take the parent role card. Say, "In my opinion, the lot should be a playground. First, kids need a safe place to play." Ask a learner with the store owner card, "Do you agree?" Help them say, "I see your point, but customers can\'t find parking." Say: "Polite language is the goal, not winning."',
  '**Community Meeting (groups of 4).** Each person has a role card with a plan and 2 reasons. Each person gives an opinion; the others agree or disagree politely. The group chooses one plan and writes 3 reasons.',
  '**Opinion Lines (whole room).** Read a statement. Learners stand by the AGREE, NOT SURE, or DISAGREE sign and explain. Someone on another side answers with *I see your point, but…*',
  '4 groups (one of 3) for round 1; then whole-room lines.', '2 groups for round 1; then lines.',
  'one group for round 1: you take a role card. Then lines.'),
 step6('A meeting flyer + two letters', 'Learners read the flyer and the two letters on the Read & Write page and answer the questions.',
  'Learners write an opinion paragraph (5–8 sentences) about the empty lot: a topic sentence, two reasons (*First… Also…*), an example, and a closing (*That\'s why…*). Show the example. **Writing check 3:** collect this paragraph and write one strength and one fix.'),
 step7('Which is better for an empty lot: a playground or a parking lot?', 'In my opinion, a playground is better. Kids need a safe place to play because the park is far. I see the other point, but parking isn\'t as important as kids.',
  'item 1: *playground / important / parking (as … as) → A playground is as important as parking.*'),
]
L['listen'] = dict(title='I See Your Point', voices={'Narrator': 'N', 'Mrs. Okafor': 'Kim', 'Ray': 'Sam', 'Lynn': 'Ana_af_jessica'},
 female=['Narrator', 'Mrs. Okafor', 'Lynn'], names=['Okafor', 'Ray', 'Lynn', 'Cedar'], tts={},
 setting='A short neighborhood meeting. The leader, Mrs. Okafor, asks for opinions about the empty lot on Cedar Street. Ray and Lynn give their opinions.',
 intro='Lesson nine. Neighbors are at a community meeting. They are talking about the empty lot on Cedar Street.',
 lines=[
  ('Mrs. Okafor', 'Good evening, everyone, and welcome. Thank you for coming. Tonight we want to talk about the empty lot on Cedar Street. The city says we can choose a plan. Ray, what do you think about it?'),
  ('Ray', 'Thanks, Mrs. Okafor. In my opinion, we need a parking lot. There aren\'t enough parking spaces on our street. I drive around for twenty minutes every night.'),
  ('Mrs. Okafor', 'Yes, the parking problem is serious. Lynn, how do you feel about it?'),
  ('Lynn', 'I see your point, Ray, but I\'m not sure I agree. I think a community garden is a better idea.'),
  ('Ray', 'A garden? Why?'),
  ('Lynn', 'First, a garden isn\'t as expensive as a parking lot. Also, if we had a garden, families would grow vegetables, and kids would spend more time outside.'),
  ('Ray', 'That\'s a good idea, but a garden is a lot of work. Who\'s going to take care of it?'),
  ('Lynn', 'I\'d help, and I think many neighbors would help too.'),
  ('Mrs. Okafor', 'Ray, do you agree with that?'),
  ('Ray', 'Well, I agree that a garden is nice. But for me, parking is as important as a garden.'),
  ('Mrs. Okafor', 'OK. Those are two good ideas. Let\'s do a survey. We\'ll ask every neighbor on Cedar Street.'),
  ('Lynn', 'I agree. That\'s fair.'),
  ('Ray', 'Yes, that\'s a good plan. I\'ll help with the survey.'),
  ('Mrs. Okafor', 'Great. We\'ll vote at the next meeting, on May twelfth. Thank you, everyone.'),
 ],
 A=dict(q='What are they deciding?', opts=['what to do with the empty lot', 'when to have a street party', 'where to put a new bus stop'], ans=0),
 B=dict(head='Match the person, the opinion, and the reason. Circle the answer.', kind='choice', items=[
  dict(s='Ray wants {{*a parking lot|a community garden}}.', ev='In my opinion, we need a parking lot.'),
  dict(s='Ray\'s reason: there {{*aren\'t enough parking spaces|are too many trees}} on the street.', ev='There aren\'t enough parking spaces on our street.'),
  dict(s='Lynn wants {{a parking lot|*a community garden}}.', ev='I think a community garden is a better idea.'),
  dict(s='Lynn\'s first reason: a garden {{*isn\'t as expensive as|is more expensive than}} a parking lot.', ev='First, a garden isn\'t as expensive as a parking lot.'),
  dict(s='Ray\'s question: who\'s going to {{*take care of it|pay for it}}?', ev='take care of it'),
  dict(s='The plan: they will {{*do a survey|build the garden}}.', ev='Let\'s do a survey.'),
 ]),
 C=dict(head='Write the missing word in the polite phrase.', items=[
  'In my [opinion], we need a parking lot.', 'how do you [feel] about it?', 'I see your [point], Ray, but I\'m not sure I agree.',
  'That\'s a good [idea], but a garden is a lot of work.', 'Well, I [agree] that a garden is nice.', 'I agree. That\'s [fair].']),
 hear='*wanna* = want to • *gonna* = going to. You can say *want to* and *going to*. In *I see your POINT, but…*, the voice goes down on *point*. Stress: *It isn\'t as EXpensive.*',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: asking for and giving an opinion

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **What do you think** | about the empty lot? | ‖ | **I think** | we need a playground. |
| **How do you feel** | about a parking lot? | ‖ | **In my opinion,** | it's a good idea. |
| **What's your opinion** | about the bus stop? | ‖ | **I'm not sure, but** | maybe it's too far. |

### Grammar Box 2: agreeing and disagreeing politely

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Do you agree** | with Ray? | ‖ | Yes, **I agree** with him. | **That's true.** Parking is a problem. |
| **Do you agree** | with Lynn? | ‖ | **I see your point, but** | a garden is a lot of work. |
| **Do you agree** | about the survey? | ‖ | **I'm not sure I agree,** | **because** it takes a long time. |
''',
rule='To disagree politely, say something positive first: ***I see your point, but… / That\'s a good idea, but…*** Say ***I agree*** (not *I am agree*) and ***I don\'t agree*** (not *I am not agree*).',
explain='''
### Grammar Box 3: *as … as / not as … as*

| | MEANING | EXAMPLE |
|---|---|---|
| *as important as* | the same | *A playground is as important as parking.* |
| *not as expensive as* | less | *A garden isn't as expensive as a parking lot.* |
| *more … than* (review) | more | *A parking lot is more expensive than a garden.* |

### Grammar Box 4: an opinion paragraph

| PART | WORDS | EXAMPLE |
|---|---|---|
| topic sentence | *In my opinion, / I think* | *In my opinion, the lot should be a playground.* |
| reason 1 and reason 2 | *First, … Also, …* | *First, kids need a safe place to play. Also, it isn't as expensive as a parking lot.* |
| example | *For example,* | *For example, the nearest park is two miles away.* |
| closing | *That's why* | *That's why I think a playground is the best plan.* |
''',
qa=[('*I am agree* or *I agree*?', '***I agree.*** *agree* is a verb, so there is no *am*. The negative is ***I don\'t agree.***'),
 ('How do I disagree politely?', 'Say something positive first: ***I see your point, but…*** or ***That\'s a good idea, but…***'),
 ('*not as expensive as* or *not as expensive than*?', 'Use *as … as*: ***A garden isn\'t as expensive as a parking lot.***')],
A=dict(head='Write one word.', items=['I [agree] with you. That\'s true.', 'A garden isn\'t [as] expensive as a parking lot.',
 'What do you [think] about the new bus stop?', 'I see your [point], but I\'m not sure.', 'In my [opinion], we need more trees.',
 'If we [had] a playground, kids would play outside more. (have)']),
B=dict(head='Circle the correct words.', items=['{{*I agree|I am agree}} with Lynn.', 'A playground is as important {{*as|than}} parking.',
 '{{*That\'s a good idea, but|That\'s wrong, and}} it\'s a lot of work. (polite)', 'How do you {{*feel|think}} about the plan?', 'A garden isn\'t as {{*expensive|more expensive}} as a parking lot.',
 'If we had a garden, families {{*would|will}} grow vegetables.']),
mistakes=[('I am agree.', 'I **agree**.'), ('I am not agree.', 'I **don\'t** agree.'),
 ('A garden isn\'t as expensive than parking.', 'A garden isn\'t as expensive **as** parking.'), ('What do you think the plan?', 'What do you think **about** the plan?'),
 ('No, that\'s wrong. (in a meeting)', '**I see your point, but** I\'m not sure.')],
tip='In some languages, a direct "No, that\'s wrong" is normal in a discussion. In English, people usually soften it: *I see your point, but…* (Spanish: *Entiendo, pero…*). What do people say in your language?')
L['talk'] = dict(pages=[('Community Meeting', '''
### Round 1. Work in groups of 4. You are neighbors at a meeting about the empty lot. Take a role card. Give your opinion with 2 reasons. The others agree or disagree politely. Then choose one plan.

| ROLE CARDS (invented) | |
|---|---|
| **A parent:** a playground. Kids need a safe place to play. The nearest park is 2 miles away. | **A store owner:** a parking lot. Customers can't find parking. More customers means more jobs. |
| **A retired neighbor:** a community garden. Older neighbors can meet. Fresh vegetables are healthy. | **A bus rider:** a bus shelter and benches. It's cold at the bus stop in winter. People wait 20 minutes. |

*Example:* A: In my opinion, the lot should be a playground. First, kids need a safe place to play. B: I see your point, but customers can't find parking. C: That's true, but a garden isn't as expensive as a parking lot.

| Name | Plan | Reason | Agree or disagree? |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Our group's plan and 3 reasons (*First… Also… That's why…*) |
|---|
| <br><br><br> |
'''), ('Opinion Lines', '''
### Round 2. Listen to the statement. Stand by the sign: AGREE, NOT SURE, or DISAGREE. Say why. Then answer someone on another side with *I see your point, but…*

| STATEMENTS | |
|---|---|
| 1. Every job should have a uniform. | 2. Kids should have less homework. |
| 3. Stores should close at 9:00 p.m. | 4. Everyone should learn to cook. |
| 5. Summer is the best season. | 6. It's a good idea to live near your job. |

*Example:* "I agree, because a uniform is easy. You don't have to choose clothes." • "I see your point, but some jobs don't need a uniform."

| Statement | Where I stood | My reason |
|---|---|---|
| | | |
| | | |
| | | |

*Useful:* I agree because… • I'm not sure. • I see your point, but… • That's a good idea, but… • That's true. • It isn't as … as …

*Remember:* the goal is polite language, not winning.
''')])
L['hw'] = dict(one=dict(head='Write the sentence or question. Use the words.', example='garden / not / expensive / parking lot → *A garden isn\'t as expensive as a parking lot.*',
 items=[('playground / important / parking (as … as)', 'A playground is as important as parking.'), ('bus / not / fast / car (not as … as)', 'A bus isn\'t as fast as a car.'),
  ('what / you / think / about / the new store?', 'What do you think about the new store?'), ('I / agree / with you (negative)', 'I don\'t agree with you.')]),
 three='''### 3. What should change in your neighborhood? Write your opinion and 3 reasons.

| My opinion (*In my opinion, …*) |
|---|
| <br><br> |

| My reasons (*First… Also… For example…*) |
|---|
| 1. <br> |
| 2. <br> |
| 3. <br> |
''',
 four=dict(head='Review (Lesson 8). Write one word.', items=['It might [rain] tomorrow. (rain)', 'Do you know where the meeting [is]? (be)',
  'The sign says the road [will] close on Monday. (will / might)', 'The repair may [take] two weeks. (take)', 'Do you know when the bus [leaves]? (leave)']))
L['rw'] = dict(kind='notice', note='Read fast first. Then read again and answer the questions.', box_title='CEDAR STREET NEIGHBORS · A flyer + two letters (invented)',
 text='''
**COMMUNITY MEETING.** What should we do with the empty lot at 400 Cedar Street? Come and share your opinion! Thursday, May 12, 7:00 p.m., Cedar Street Library, Room B. Free childcare. Please bring your survey.

**A playground, please!** In my opinion, the lot should be a playground. First, our kids don't have a safe place to play. The nearest park is two miles away. Also, a playground isn't as expensive as a parking lot. If we had a playground, families would spend more time outside together. That's why I think a playground is the best plan. *Maria G.*

**What about parking?** I see the point about a playground, but I'm not sure I agree. Every night, I drive around for 20 minutes to find a space. Many neighbors work late, and the street is very dark at night. A small parking lot with good lights would help everyone. Maybe we could also put two benches and a small garden next to it. *Ray T.*
''',
 qs=[('When is the meeting?', 'Thursday, May 12, at 7:00 p.m.', 'Thursday, May 12, 7:00 p.m.'),
  ('What does Maria want?', 'A playground.', 'In my opinion, the lot should be a playground'),
  ('What is Maria\'s first reason?', 'Kids don\'t have a safe place to play.', 'First, our kids don\'t have a safe place to play'),
  ('Does Ray agree with Maria?', 'No. He sees her point, but he isn\'t sure he agrees.', 'I see the point about a playground, but I\'m not sure I agree'),
  ('What could go next to the parking lot?', 'Two benches and a small garden.', 'two benches and a small garden')],
 write_head='Write an opinion paragraph (5–8 sentences): what should the empty lot be? Use a topic sentence, two reasons (*First… Also…*), an example, and a closing sentence (*That\'s why…*).',
 write_short='your paragraph',
 example='*In my opinion, the empty lot should be a community garden. First, a garden isn\'t as expensive as a parking lot. Also, neighbors could meet and work together. For example, my grandmother loves to grow tomatoes, but she doesn\'t have a yard. I see the point about parking, but a garden helps more people. That\'s why I think a garden is the best plan.*',
 box_label='My paragraph', checklist=['It has 5–8 sentences.', 'It has a topic sentence and a closing sentence.', 'It has *First…* and *Also…*.', 'It has an example.'])
L['exit'] = dict(q='Which is better for an empty lot: a playground or a parking lot?', s1='your opinion (*In my opinion, …*)', s2='a reason, with *because*',
 s3='*I see the other point, but…*', key='*A good answer:* "In my opinion, a playground is better. Kids need a safe place to play because the park is far. I see the other point, but parking isn\'t as important as kids."')
L['game'] = ('What do you think?', 'A points to a picture and asks, "What do you think about a **community garden**?" B gives an opinion and a reason. A says, "I agree," or "I see your point, but…" Switch.')
L['opening'] = dict(cards=['**A:** Do you know when the library opens?', '**A:** What might change in this city next year?', '**A:** Do you know where the nearest bus stop is?', '**A:** Will it rain this weekend?'],
 follow='Are you sure, or is it maybe? • How do you know? • Why?', hw_head='Write your partner\'s name and one change from Homework item 3.', hw_cols=['My partner\'s name', 'A change (*might / may*)'])
L['notes'] = [
 '**Local and practical:** topics stay with parks, parking, store hours, bus stops, and homework. No elections or political parties.',
 '**Praise polite language, not who "wins."** Model disagreeing with a smile. Write good phrases you hear on the board.',
 '***I agree*, not *I am agree*:** this is very common. Point to the Q&A box and keep it on the board all evening.',
 '**Opinion Lines:** learners who can\'t stand or move can hold up a sign or raise a hand from their seat.',
 '**Writing check 3 (Week 10):** collect the opinion paragraph. Write one strength and one fix on each. Learners keep them in their writing folder.',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening says *going to* and *want to*. People often say *gonna* and *wanna*. Learners only need to recognize the short forms; they can always say the full forms.']
