import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=11, week=12, title='Time Off',
topic='Asking for time off at work, planning a short trip to visit family or see a new place, packing, and leaving a detailed voicemail. Learners say why with *to* + verb and use verbs + *to* or + *-ing*. The company, the policy, the trips, and the phone numbers are invented.',
cq='Why do you need time off? What do you enjoy doing on a trip?',
builds=[
 ('*enjoy / don\'t mind* + *-ing*; *hope to / plan to*', 'Level 3', 'one chart: verbs + ***to*** and verbs + ***-ing***'),
 ('*Would you mind…?*', 'Level 4 Lesson 5', '***Would you mind covering my shift?***'),
 ('*already / yet*; *going to*', 'Level 3 and Level 4', '*I\'ve already filled out the form. I\'m going to leave on Friday.*'),
],
objectives=['ask for time off and give a reason',
 'say why with *to* + verb (*I\'m going to Houston to see my sister.*)',
 'use verbs + *to* (*want, need, plan, decide, hope, forget, would like*) and verbs + *-ing* (*enjoy, don\'t mind, finish, avoid, keep*)',
 'leave a detailed voicemail and take voicemail notes',
 'write an email (5–8 sentences) to a supervisor asking for time off'],
materials=['Board and markers', 'A phone or a toy phone for Voicemail Relay (optional)', 'A timer (a phone is fine)'],
prep='15 minutes (read the plan; practice reading the listening script; write the two verb lists on the board)',
words=[('time off', 'time_off', True), ('vacation days', 'vacation_days', True), ('request form', 'request_form', True), ('approve', 'approve', True), ('pack', 'pack', True),
 ('suitcase', 'suitcase', True), ('carry-on bag', 'carry_on', True), ('round-trip ticket', 'round_trip', True), ('boarding pass', 'boarding_pass', True), ('toiletries', 'toiletries', True),
 ('voicemail', 'voicemail', True), ('itinerary', 'itinerary', False)],
more_vocab='*Also:* a supervisor, a shift, cover (a shift), a coworker, a policy, ahead, deny, a callback number, a bus station, a surprise.',
clock=clock('', ' (+ My Words)', '', '*to* + verb (why); verbs + *to* / + *-ing*', 'Trip Planner + Voicemail Relay', 'A time-off policy + a packing list; an email',
 talk_group='Pairs, then back-to-back pairs'),
attend='With 5 or fewer, do both rounds in pairs (you are a partner if needed) and check the voicemail notes yourself. Late arrivals join a pair for Trip Planner and leave a voicemail in round 2.',
)
L['steps'] = [
 step1('Opening Talk', '*phrasal verbs + it / them*',
  'you say, "What do you turn off before you go to bed?" The learner answers with *it / them* (*I turn the TV off. I turn it off at 10:00.*). Then you ask, "What do you put on when it\'s cold?" Help them say 3 sentences.',
  'Pairs compare Homework item 1 (*it / them*) and read their 3 home tips (item 3) to each other. Then they fill in the box on the Opening Talk page.',
  '*turn off it* (→ *turn it off*) and *close the light* (→ *turn off the light*)'),
 step2('*time off* (days you don\'t work); *vacation days* (paid days off); *request form*; *approve* (say yes); *pack* (put things in a bag); *suitcase*; *carry-on bag* (a small bag on the plane or bus); *round-trip ticket* (there and back); *boarding pass*; *toiletries* (toothbrush, soap); *voicemail* (a phone message); *itinerary* (the plan for a trip, with times).',
  'ask "Does a supervisor approve or pack a request?" (approve) • "Is a round-trip ticket for one way or there and back?" (there and back) • "Is a toothbrush a toiletry or a boarding pass?" (a toiletry).',
  'I need to pack my toiletries.'),
 step3('Luis asks his supervisor, Ms. Adams, for time off. Then he leaves a voicemail for his sister, Rosa, and she calls back. Listen: why does he need time off?',
  'Point to the script lines. *wanna* = want to: "When do you **want to** take it?" *gonna* = going to: "I\'m **going to** take the bus." Then practice the phone number in groups with pauses: *555 · 214 · 8830*.', '{EST}'),
 step4('*to* + verb (why); verbs + *to* / + *-ing*', 'say, "I\'m going to the store." Ask, "Why?" Answer, "**To buy** milk." Write: *Why? → To + verb.* Then say, "I **enjoy cooking**. I **want to cook** for my family." Write two lists on the board: **+ to:** *want, need, plan, decide, hope, forget, would like*; **+ -ing:** *enjoy, don\'t mind, finish, avoid, keep*.',
  'Box 1: read across: *Why are you taking time off? → To visit my sister.* Box 2: verbs + *to* and verbs + *-ing*. Box 3: the two lists. Box 4: review (*already, Would you mind…?, going to*).',
  '"*for see* or *to see*?" (*to see*) • "*enjoy to travel* or *enjoy traveling*?" (*enjoy traveling*) • "*want to visit* or *want visiting*?" (*want to visit*).',
  'A points to a picture and asks, "Why do you need a **suitcase**?" B answers with *to* + verb: "To pack my clothes." Then B asks, "What do you enjoy doing on a trip?" Switch.'),
 brk('*Why are you taking time off? → To visit my sister. • I want to go. I enjoy traveling. • I\'m calling to ask about my vacation days.*'),
 step5('Trip Planner + Voicemail Relay', 'read trip card A: "Visit family in another state for 4 days." Say, "I\'m going to Dallas to visit my cousins. I want to see the new baby. I enjoy cooking with my aunt." Then model a voicemail: "Hi, it\'s Ms. Lee. I\'m calling to tell you about my trip. I\'m leaving on Friday. Call me back at 555 · 301 · 7720."',
  '**Trip Planner (pairs).** Pairs choose a trip card. They plan why (*to…*), what they want to do and enjoy doing, and what to pack. Then they fill in the time-off request.',
  '**Voicemail Relay (back to back).** A leaves a voicemail of 30–45 seconds: name, reason for calling (*to…*), dates, and an invented callback number. B takes notes and reads them back. Switch.',
  'pairs; then back-to-back rows.', 'pairs; then one rotation.', 'pairs; you check the notes.'),
 step6('A time-off policy + a packing list', 'Learners read the invented company policy and Luis\'s packing list on the Read & Write page and answer the questions.',
  'Learners write an email (5–8 sentences) to a supervisor asking for time off: the dates, the reason (*to…*), who can cover, and thanks. Show the example. **Writing check 4:** collect this email and write one strength and one fix.'),
 step7('Where would you like to go on a trip, and why?', 'I would like to go to the beach to relax. I enjoy swimming in the ocean. It\'s also a good place for my family, because my kids love the water.',
  'item 1: *I / enjoy / travel / by bus → I enjoy traveling by bus.*'),
]
L['listen'] = dict(title='Time Off', voices={'Narrator': 'N', 'Luis': 'Marco', 'Ms. Adams': 'Receptionist', 'Rosa': 'Rosa'},
 female=['Narrator', 'Ms. Adams', 'Rosa'], names=['Luis', 'Adams', 'Rosa', 'Anna', 'Ben', 'San Antonio'], tts={},
 setting='(1) Luis asks his supervisor for three days off to visit his mother, and they check who can cover his shifts. (2) He leaves a voicemail for his sister, and she calls back.',
 intro='Lesson eleven. Luis asks his supervisor for time off. Then he leaves a voicemail for his sister.',
 lines=[
  ('Luis', 'Ms. Adams, do you have a minute? I\'d like to ask for some time off.'),
  ('Ms. Adams', 'Sure. When do you want to take the time off?'),
  ('Luis', 'I need June fifth to June seventh. That\'s three days.'),
  ('Ms. Adams', 'And why are you taking time off?'),
  ('Luis', 'To visit my mother in San Antonio. She is turning seventy.'),
  ('Ms. Adams', 'How nice! Did you fill out the request form?'),
  ('Luis', 'Yes, I\'ve already filled it out. Here it is.'),
  ('Ms. Adams', 'Thanks. Who can cover your shifts?'),
  ('Luis', 'Anna has agreed to cover Thursday and Friday. I\'m still looking for someone for Saturday.'),
  ('Ms. Adams', 'Ask Ben. He doesn\'t mind working on weekends. Then I can approve it.'),
  ('Luis', 'Great. Thank you, Ms. Adams.'),
  ('Luis', 'Hi, Rosa, it\'s Luis. I\'m calling to tell you about my trip. I\'m going to take the bus on Thursday, June fifth. It\'s bus number forty-two, and it gets to San Antonio at six thirty in the evening. Can you pick me up at the bus station? Also, don\'t forget to bring Mom\'s birthday card. I want everyone to sign it. Call me back at five five five, two one four, eight eight three zero. Bye!'),
  ('Rosa', 'Hi, Luis! I got your message. Yes, I can pick you up at six thirty.'),
  ('Luis', 'Thanks, Rosa. Mom doesn\'t know I\'m coming, right?'),
  ('Rosa', 'No, it\'s a surprise. She\'s going to be so happy. I enjoy planning surprises!'),
  ('Luis', 'Me too. See you on Thursday!'),
 ],
 A=dict(q='Why does Luis need time off?', opts=['to visit his mother', 'to see a doctor', 'to move to a new apartment'], ans=0),
 B=dict(head='Complete the notes. Circle the answer.', kind='choice', items=[
  dict(s='Dates: June {{*5 to 7|15 to 17}}', ev='June fifth to June seventh'),
  dict(s='Reason: his mother\'s {{*birthday|wedding}}', ev='She is turning seventy.'),
  dict(s='Anna will cover {{*Thursday and Friday|Saturday}}.', ev='Anna has agreed to cover Thursday and Friday.'),
  dict(s='For Saturday, Ms. Adams says to ask {{*Ben|Rosa}}.', ev='Ask Ben.'),
  dict(s='Bus number: {{*42|24}}', ev='bus number forty-two'),
  dict(s='Arrival time: {{*6:30 p.m.|7:30 p.m.}}', ev='six thirty in the evening'),
 ]),
 C=dict(head='Write *to* or the *-ing* form of the verb.', items=[
  'I\'d like [to] ask for some time off.', 'He doesn\'t mind [working] on weekends.', 'I\'m calling [to] tell you about my trip.',
  'don\'t forget [to] bring Mom\'s birthday card.', 'I want everyone [to] sign it.', 'I enjoy [planning] surprises!']),
 hear='*wanna* = want to: "When do you **want to** take it?" • *gonna* = going to: "I\'m **going to** take the bus." Understand them; you can say *want to* and *going to*. Never write *wanna* or *gonna*. Phone numbers come in groups with pauses: *555 · 214 · 8830*.',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: *to* + verb answers *Why?*

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Why are you taking** | time off? | ‖ | **To visit** | my sister in Houston. |
| **Why are you going** | to Houston? | ‖ | I'm going there **to see** | my family. |
| **Why are you** | calling? | ‖ | I'm calling **to ask** | about my vacation days. |

### Grammar Box 2: verbs + *to* and verbs + *-ing*

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **What do you want** | to do? | ‖ | I **want to visit** | the lake. |
| **What do you enjoy** | doing on a trip? | ‖ | I **enjoy taking** | pictures. |
| **What did you decide** | to do? | ‖ | We **decided to take** | the bus. |
| **Do you mind** | driving? | ‖ | No, I **don't mind driving.** | It's fine. |
''',
rule='There is no rule for which verbs take *to* and which take *-ing*: learn the two short lists in Box 3. *to* + verb also answers *Why?* (***To visit my sister.***)',
explain='''
### Grammar Box 3: the two lists

| + *to* + verb | + *-ing* |
|---|---|
| *want, need, plan, decide* | *enjoy, don't mind* |
| *hope, forget, would like* | *finish, avoid, keep* |
| *I'm planning to leave on Friday.* | *I enjoy traveling by bus.* |

### Grammar Box 4: review

| WORDS | EXAMPLE |
|---|---|
| *already / yet* | *I've already packed. Have you packed yet?* |
| *Would you mind + -ing?* | *Would you mind covering my shift?* |
| *going to* | *I'm going to leave on Friday.* |
''',
qa=[('*for see* or *to see*?', 'Use *to*: ***I\'m going to Houston to see my sister.*** (not *for see*, not *for to see*)'),
 ('*enjoy to travel* or *enjoy traveling*?', '***enjoy traveling.*** After *enjoy*, use *-ing*.'),
 ('How do I know: *to* or *-ing*?', 'Look at the two lists in Box 3. Learn them like vocabulary.')],
A=dict(head='Write one word.', items=['I\'m taking a day off [to] see the doctor.', 'I enjoy [traveling] by train. (travel)',
 'We decided [to] stay for 3 days.', 'Don\'t forget [to] pack your charger.', 'She doesn\'t mind [working] on Saturday. (work)',
 'I\'ve [already] filled out the request form.']),
B=dict(head='Circle the correct words.', items=['I\'m calling {{*to ask|for ask}} about my vacation days.', 'I want {{*to visit|visiting}} my aunt.',
 'Did you finish {{*packing|to pack}}?', 'I hope {{*to see|seeing}} you soon.', 'Try to avoid {{*taking|to take}} too many bags.',
 'Would you mind {{*covering|to cover}} my shift?']),
mistakes=[('I went to Houston for see my sister.', 'I went to Houston **to see** my sister.'), ('I enjoy to travel.', 'I enjoy **traveling**.'),
 ('I want visit my family.', 'I want **to** visit my family.'), ('I\'m planning leave on Friday.', 'I\'m planning **to** leave on Friday.'),
 ('Don\'t forget pack your toiletries.', 'Don\'t forget **to** pack your toiletries.')],
tip='Spanish uses *para* for purpose: *Voy a Houston para ver a mi hermana.* English uses only *to*: *I\'m going to Houston to see my sister* (not *for see*, not *for to see*). After *enjoy*, use *-ing*: *I enjoy traveling* (not *enjoy to travel*). How do you say *why* in your language?')
L['talk'] = dict(pages=[('Trip Planner', '''
### Round 1. Work with a partner. Choose a trip card. Plan the trip together. Then fill in the time-off request.

| TRIP CARDS (invented) | |
|---|---|
| **A.** Visit family in another state for 4 days (by bus). | **B.** A weekend at a lake (by car). |
| **C.** A day in a big city (by train). | **D.** Visit a friend for 3 days (by plane). |

*Example:* "We're going to the lake to relax. We want to go fishing. I enjoy swimming. Don't forget to pack sunscreen!"

| Why? (*to…*) | We want to… | We enjoy… | We need to pack… |
|---|---|---|---|
| | | | |
| | | | |

| TIME-OFF REQUEST (invented) | |
|---|---|
| Name: | Dates: |
| Reason (*to…*): | Who can cover my shift: |
'''), ('Voicemail Relay', '''
### Round 2. Sit back to back. A leaves a voicemail (30–45 seconds). B takes notes and reads them back. Then switch.

**Say:** your name • why you are calling (*I'm calling to…*) • the dates or time • an invented callback number (*555 · ___ · ____*)

*Example:* "Hi, this is Carla. I'm calling to ask about Saturday. I want to switch my shift to Sunday. Call me back at 555 · 301 · 7720. Thanks!"

| VOICEMAIL NOTES | 1 | 2 |
|---|---|---|
| Name | | |
| Why are they calling? | | |
| Dates or time | | |
| Callback number | | |

*Useful:* Hi, this is… • I'm calling to… • I'd like to… • Could you call me back at…? • Thanks. Bye! • (Reading back:) So, your name is… and your number is…
''')])
L['hw'] = dict(one=dict(head='Write the sentence. Use *to* or *-ing*.', example='go / Houston / see my sister → *I\'m going to Houston to see my sister.*',
 items=[('I / enjoy / travel / by bus', 'I enjoy traveling by bus.'), ('we / plan / leave / on Friday (be + -ing)', 'We\'re planning to leave on Friday.'),
  ('I / call / ask / about my vacation days (be + -ing)', 'I\'m calling to ask about my vacation days.'), ('don\'t forget / pack / your charger', 'Don\'t forget to pack your charger.')]),
 three='''### 3. Plan a short trip (real or invented). Write where, why (*to…*), and 3 things to pack.

| Where? | Why? (*to…*) |
|---|---|
| | |

| 3 things to pack | |
|---|---|
| 1. | |
| 2. | |
| 3. | |
''',
 four=dict(head='Review (Lesson 10). Write one word.', items=['The lights are on. Please turn [them] off.', 'Did you take out the trash? Yes, I took [it] out.',
  'It\'s cold. Please turn [up] the heat.', 'Make [sure] you lock the deadbolt.', 'Don\'t forget [to] unplug the charger.']))
L['rw'] = dict(kind='notice', note='Read fast first. Then read again and answer the questions.', box_title='GREENLEAF FOODS · A policy + a packing list (invented)',
 text='''
**TIME-OFF POLICY.** All workers can ask for time off. Please follow these steps. First, ask at least two weeks ahead. For example, to take time off on June 5, ask before May 22. Second, fill out a time-off request form. You can get the form from your supervisor or in the break room. Write the dates and the reason. Third, find a coworker who can cover your shifts, if possible. Your supervisor will approve or deny the request within three days. Full-time workers get 10 vacation days each year. Part-time workers get 5. If you are sick, call your supervisor before your shift starts. You don't need a form for a sick day. Do you have questions? Ask your supervisor, or call Human Resources at extension 210.

**LUIS'S PACKING LIST.** Carry-on bag · 3 shirts and 1 pair of pants · toiletries (toothbrush, toothpaste) · phone charger · Mom's birthday card · round-trip bus ticket.
''',
 qs=[('How early should you ask for time off?', 'At least two weeks ahead.', 'ask at least two weeks ahead'),
  ('Where can you get the form?', 'From your supervisor or in the break room.', 'from your supervisor or in the break room'),
  ('When will the supervisor answer?', 'Within three days.', 'within three days'),
  ('How many vacation days do part-time workers get?', '5.', 'Part-time workers get 5.'),
  ('What is Luis bringing for his mother?', 'A birthday card.', 'Mom\'s birthday card')],
 write_head='Write an email (5–8 sentences) to your supervisor. Ask for time off. Write the dates, the reason (*to…*), who can cover your shift, and thanks.',
 write_short='your email',
 example='*Dear Ms. Adams, I would like to ask for three days off, from June 5 to June 7. I need the time off to visit my mother in San Antonio. It\'s her 70th birthday. I have already filled out the request form. Anna has agreed to cover my shifts on Thursday and Friday. Ben doesn\'t mind working on Saturday. Thank you for your time. Luis Ortega*',
 box_label='My email', checklist=['It has 5–8 sentences.', 'It has the dates.', 'It has a reason with *to* + verb.', 'It says who can cover and says thank you.'])
L['exit'] = dict(q='Where would you like to go on a trip, and why?', s1='where and why, with *to* + verb', s2='something you enjoy, with *enjoy* + *-ing*',
 s3='one more reason, with *because*', key='*A good answer:* "I would like to go to the beach to relax. I enjoy swimming in the ocean. It\'s also a good place for my family, because my kids love the water."')
L['game'] = ('Why do you need it?', 'A points to a picture and asks, "Why do you need a **boarding pass**?" B answers with *to* + verb: "To get on the plane." Then B asks, "What do you enjoy doing on a trip?" Switch.')
L['opening'] = dict(cards=['**A:** What do you turn off before you go to bed?', '**A:** What do you put on when it\'s cold?', '**A:** Did you take out the trash this week?', '**A:** What can you do to save energy at home?'],
 follow='When? • Why? • Did you turn it off?', hw_head='Write your partner\'s name and one home tip from Homework item 3.', hw_cols=['My partner\'s name', 'A home tip (*Turn… / Unplug…*)'])
L['notes'] = [
 '**Trips can be invented:** don\'t assume learners can travel or have paid vacation days. A day trip in the city is always fine.',
 '**No passport, visa, or immigration topics.** Keep trips to visiting family, a lake, or a city.',
 '**Time-off rules vary by employer:** the policy is invented. Learners can check their own workplace rules.',
 '**Writing check 4 (Week 12):** collect the time-off email. Write one strength and one fix on each. Learners keep them in their writing folder.',
 '**Phone numbers are invented** and use 555. Practice saying them in groups with pauses (3-3-4).',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening says *going to* and *want to*. People often say *gonna* and *wanna*. Learners only need to recognize the short forms, and they never write them.']
