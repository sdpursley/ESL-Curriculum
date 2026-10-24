import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=10, week=11, title='Turn It Off',
topic='Saving energy and keeping a home safe: reading a utility bill, simple ways to use less electricity and water, locking up, and knowing where the fire extinguisher is. Learners give and follow home tips with separable phrasal verbs and *it / them*. The bill, the company, and the program are invented.',
cq='How can you save energy and stay safe at home?',
builds=[
 ('imperatives; *Make sure you… / Don\'t forget to…*', 'Level 3 Lesson 10', '***Make sure you turn the stove off.***'),
 ('object pronouns *it / them*', 'Level 2', '***turn it off / put them away*** (the small word goes after *it / them*)'),
 ('*too much / too many*', 'Level 4 Lesson 7', '*We use too much electricity.*'),
],
objectives=['use phrasal verbs: *turn off, turn down, turn up, put on, put away, take out, throw away, shut off*',
 'put *it / them* in the right place (*turn it off*, not *turn off it*)',
 'give tips to save energy and stay safe at home (*Make sure you… / Don\'t forget to…*)',
 'read the main parts of a utility bill (amount due, due date, usage)',
 'write an email (5–8 sentences) to a roommate or family member about changes at home'],
materials=['Board and markers', 'A light switch, a lamp, or a phone charger to point to (optional)', 'Poster paper or the back of the Talk Time page for Home Tips'],
prep='15 minutes (read the plan; practice reading the listening script; find the light switch and an outlet in the classroom)',
words=[('utility bill', 'utility_bill', True), ('electricity', 'electricity', True), ('thermostat', 'thermostat', True), ('save energy', 'save_energy', True), ('unplug', 'unplug', True),
 ('charger', 'charger', True), ('outlet', 'outlet', True), ('fan', 'fan', True), ('deadbolt', 'deadbolt', True), ('peephole', 'peephole', True),
 ('fire extinguisher', 'fire_extinguisher', True), ('usage', 'usage', False)],
more_vocab='*Also:* an account number, the amount due, a due date, a late fee, the heat, the air conditioner, a light bulb, plugged in, running water, a roommate.',
clock=clock('', ' (+ My Words)', '', '*phrasal verbs + it / them*', 'Energy Detective + Home Tips', 'A utility bill + a flyer; an email',
 talk_group='Pairs, then groups of 3'),
attend='With 5 or fewer, do Energy Detective in pairs (you are a partner if needed), then make one Home Tips poster together. Late arrivals join a pair as the "checker" and then take a turn.',
)
L['steps'] = [
 step1('Opening Talk', '*opinions; agree / disagree politely; as … as*',
  'you say, "What do you think about homework for kids?" The learner gives an opinion and a reason. Then you disagree politely: "I see your point, but…" Help them answer with 3 sentences.',
  'Pairs compare Homework item 1 (*as … as*) and read their opinion and reasons (item 3) to each other. The partner agrees or disagrees politely. Then they fill in the box on the Opening Talk page.',
  '*I am agree* (→ *I agree*) and *not as fast than* (→ *not as fast as*)'),
 step2('*utility bill* (the bill for electricity, gas, or water); *electricity*; *thermostat* (it controls the heat); *save energy* (use less); *unplug* (take the plug out); *charger*; *outlet* (point to one in the room); *fan*; *deadbolt* (a strong lock); *peephole* (a small hole in the door to look out); *fire extinguisher*; *usage* (how much you use).',
  'ask "Do you plug a charger into an outlet or a peephole?" (an outlet) • "Is a deadbolt a lock or a light?" (a lock) • "Does a thermostat control the heat or the water?" (the heat).',
  'Make sure you unplug the charger.'),
 step3('Two roommates, Sofia and Hana, look at a high electric bill and make a plan. Then Sofia calls the electric company. Listen: what is the problem?',
  'Point to the script line. *gonna* = going to: "I\'m **going to** unplug my phone charger." Then practice the stress on the small word: *turn it OFF, put it aWAY*, and the linking: *turn_it_off, take_it_out*.', '{EST}'),
 step4('*phrasal verbs + it / them*', 'point to the lights and say, "Can you **turn off** the lights?" A learner turns them off (or mimes it). You say, "Thank you. You **turned them off**." Turn them on again. Write: *turn off the lights / turn the lights off → turn them off*. Cross out *turn off them*.',
  'Box 1: read across: *Can you turn off the lights? → OK, I\'ll turn them off.* Box 2: the past: *Did you take out the trash? → Yes, I took it out.* Box 3: the 8 phrasal verbs. Box 4: *Make sure you… / Don\'t forget to…*',
  '"*turn off it* or *turn it off*?" (*turn it off*) • "Is *turn the TV off* OK?" (yes) • "It\'s too loud. *Turn it up* or *turn it down*?" (*turn it down*).',
  'A points to a picture and says, "Can you **unplug** the **charger**?" B mimes and answers, "OK, I\'ll unplug it." A says, "Don\'t forget to lock the **deadbolt**." Switch.'),
 brk('*Can you turn off the lights? → OK, I\'ll turn them off. • Did you take out the trash? → Yes, I took it out. • Make sure you lock the deadbolt.*'),
 step5('Energy Detective + Home Tips', 'read the first problem on the Apartment A card: "The lights are on in an empty room." Say to a learner, "Turn them off, please." The learner mimes and says, "OK, I\'ll turn them off." Do one more: "The window is open, and the heat is on." (*Close it. Turn the heat down.*)',
  '**Energy Detective (pairs).** A reads a problem from the Apartment A card and gives an instruction (*Turn them off. Close it. Put it away.*). B mimes and answers with *it / them*. Then switch to the Apartment B card.',
  '**Home Tips (groups of 3).** Groups write 5 tips to save energy or stay safe (*Turn down the heat at night. Unplug the charger.*) and present them in 1 minute.',
  'pairs for round 1; then 5 groups of 3.', 'pairs; then 2 groups.', 'pairs; then one poster together.'),
 step6('A utility bill + a "Save energy, stay safe" flyer', 'Learners read the invented bill and the flyer on the Read & Write page and answer the questions.',
  'Learners write an email (5–8 sentences) to a roommate or family member: what to change at home and why. Show the example. Check for 2 phrasal verbs and one *it* or *them*.'),
 step7('What can people do at home to save energy or stay safe?', 'Turn off the lights when you leave a room. Unplug your charger and put it away. Make sure you lock the deadbolt at night, because it keeps your home safe.',
  'item 1: *turn down / the heat (it) → Turn it down.*'),
]
L['listen'] = dict(title='Turn It Off', voices={'Narrator': 'N', 'Sofia': 'Rosa', 'Hana': 'Ana_af_jessica', 'Paul': 'Server'},
 female=['Narrator', 'Sofia', 'Hana'], names=['Sofia', 'Hana', 'Paul', 'City Power'], tts={},
 setting='Two roommates look at a high electric bill and decide how to save energy. Then Sofia calls the electric company\'s customer line.',
 intro='Lesson ten. The two roommates look at their power bill. Then Sofia calls the electric company.',
 lines=[
  ('Sofia', 'Hana, look at this. Our power bill is $142 this month!'),
  ('Hana', 'Last month it was only $90. Why is it so high?'),
  ('Sofia', 'Well, we use too much electricity. The heat is on all day, and the lights are on in empty rooms.'),
  ('Hana', 'You\'re right. I always forget to turn them off. Oh, the TV is on now, and nobody is watching. I\'ll turn it off.'),
  ('Sofia', 'OK, let\'s make a plan. First, we can turn down the heat at night. Sixty-eight degrees is fine.'),
  ('Hana', 'Good idea. And I\'m going to unplug my phone charger in the morning. It uses electricity all day.'),
  ('Sofia', 'Also, let\'s put on sweaters and not turn up the heat. Can you call the electric company? I have class.'),
  ('Hana', 'Sorry, I have work. Can you call them tonight?'),
  ('Sofia', 'Sure. I\'ll call them now.'),
  ('Paul', 'Thank you for calling City Power. This is Paul. How can I help you?'),
  ('Sofia', 'Hi. I\'m calling about my bill. When is it due?'),
  ('Paul', 'Can I have your account number, please?'),
  ('Sofia', 'Yes. It\'s four, seven, two, one, nine.'),
  ('Paul', 'Thank you. Your bill is due on March fifteenth.'),
  ('Sofia', 'OK. Also, do you have any programs to help us save energy?'),
  ('Paul', 'Yes. We have a free home energy check. Someone visits your apartment and gives you tips. And you can get free light bulbs.'),
  ('Sofia', 'That sounds great. Can I sign up?'),
  ('Paul', 'Sure. Is next Tuesday morning OK?'),
  ('Sofia', 'Yes, that\'s perfect. Thank you.'),
  ('Paul', 'You\'re welcome. And don\'t forget to turn off the lights when you leave a room!'),
 ],
 A=dict(q='What is the problem?', opts=['The electric bill is too high.', 'The heat is broken.', 'The bill is late.'], ans=0),
 B=dict(head='Listen again. Circle the answer.', kind='choice', items=[
  dict(s='The bill this month is {{*$142|$90}}.', ev='$142'),
  dict(s='They will turn {{*down|up}} the heat at night.', ev='we can turn down the heat at night'),
  dict(s='Hana is going to unplug her {{*phone charger|TV}}.', ev='I\'m going to unplug my phone charger'),
  dict(s='They will put on {{*sweaters|coats}}.', ev='put on sweaters'),
  dict(s='The bill is due on {{*March 15|March 5}}.', ev='due on March fifteenth'),
  dict(s='The home energy check is {{*free|$20}}.', ev='We have a free home energy check.'),
 ]),
 C=dict(head='Write the missing word: the phrasal verb or *it / them*.', items=[
  'I always forget to turn [them] off.', 'I\'ll turn [it] off.', 'we can turn [down] the heat at night.',
  'let\'s put [on] sweaters', 'not turn [up] the heat', 'don\'t forget to turn [off] the lights']),
 hear='*gonna* = going to: "I\'m **going to** unplug my phone charger." You can say *going to*. Stress the small word: *turn it OFF, put it aWAY*. Link the words: *turn_it_off, take_it_out*.',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: phrasal verbs + *it / them*

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Can you turn off** | the lights? | ‖ | OK, **I'll turn them off.** | (not *turn off them*) |
| **Can you turn** | the TV **down**? | ‖ | Sure, **I'll turn it down.** | It's loud. |
| **Can you take out** | the trash? | ‖ | Yes, **I'll take it out** | now. |

### Grammar Box 2: the past

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **Did you take out** | the trash? | ‖ | Yes, **I took it out** | this morning. |
| **Did you put away** | the dishes? | ‖ | No, **I didn't put them away** | yet. |
| **Did you shut off** | the water? | ‖ | Yes, **I shut it off** | before I left. |
''',
rule='With a noun, two places are OK: ***turn off the TV / turn the TV off***. With *it / them*, only the middle: ***turn it off*** (not *turn off it*).',
explain='''
### Grammar Box 3: 8 phrasal verbs for home

| VERB | MEANING | EXAMPLE |
|---|---|---|
| *turn off / turn up / turn down* | stop / more / less | *Turn off the lights. Turn the heat down at night.* |
| *put on / put away* | wear / put in its place | *Put on a sweater. Put the dishes away.* |
| *take out / throw away* | take outside / put in the trash | *Take out the trash. Throw away old food.* |
| *shut off* | stop (water, gas) | *Shut off the water.* |

### Grammar Box 4: home tips

| START | EXAMPLE |
|---|---|
| *Make sure you…* | *Make sure you lock the deadbolt at night.* |
| *Don't forget to…* | *Don't forget to unplug the charger.* |
| *We use too much…* | *We use too much electricity.* |
''',
qa=[('*turn off it* or *turn it off*?', '***turn it off.*** With *it / them*, the small word goes after: ***turn it off, put them away.***'),
 ('Is *turn off the TV* OK?', 'Yes. With a noun, both are OK: ***turn off the TV*** and ***turn the TV off***.'),
 ('*turn down* or *turn off*?', '*turn down* = less. *turn off* = stop. ***Turn down the heat. Turn off the lights.***')],
A=dict(head='Write one word.', items=['The lights are on. Please turn [them] off.', 'It\'s hot. Can you turn [up] the fan?',
 'Did you take out the trash? Yes, I took [it] out.', 'It\'s cold. Put [on] a sweater.', 'Make [sure] you lock the deadbolt.',
 'Don\'t [forget] to unplug the charger.']),
B=dict(head='Circle the correct words.', items=['Turn {{*it off|off it}}, please.', 'Can you {{*throw away|throw on}} the old milk?',
 'It\'s late. Please turn {{*down|up}} the music.', 'I {{*put them away|put away them}} yesterday.', 'Don\'t forget {{*to lock|lock}} the door.',
 'We use too {{*much|many}} water.']),
mistakes=[('Turn off it.', 'Turn **it off**.'), ('I put away them.', 'I put **them away**.'),
 ('Close the light.', '**Turn off** the light.'), ('Open the TV.', '**Turn on** the TV.'),
 ('Don\'t forget lock the door.', 'Don\'t forget **to** lock the door.')],
tip='Many languages use one verb where English uses two words: Spanish *apagar* = *turn off*, *bajar* = *turn down*, *tirar* = *throw away*. With *it / them*, the small word goes after the pronoun: *turn it off*. How do you say these in your language?')
L['talk'] = dict(pages=[('Energy Detective', '''
### Round 1. Work with a partner. A reads a problem and gives an instruction. B mimes and answers with *it* or *them*. Then switch: B uses Apartment B.

| APARTMENT A (A reads) | APARTMENT B (B reads) |
|---|---|
| 1. The lights are on in an empty room. | 1. The fan is on, and nobody is home. |
| 2. The window is open, and the heat is on. | 2. The dishes are on the table. |
| 3. The charger is plugged in, but there is no phone. | 3. The thermostat says 80 degrees at night. |
| 4. The front door isn't locked. | 4. The water is running in the bathroom. |
| 5. The TV is on, and nobody is watching. | 5. The trash is full. |
| 6. The music is very loud at 11:00 p.m. | 6. There is old food in the fridge. |

*Example:* A: The lights are on in an empty room. Turn them off, please. B: OK, I'll turn them off.

| Problem number | Instruction (*Turn it off. Put them away.*) |
|---|---|
| | |
| | |
| | |
'''), ('Home Tips', '''
### Round 2. Work in groups of 3. Write 5 tips to save energy or stay safe at home. Then present them in 1 minute.

| OUR 5 HOME TIPS | Why? |
|---|---|
| 1. | |
| 2. | |
| 3. | |
| 4. | |
| 5. | |

*Example:* "Turn down the heat at night, because 68 degrees is fine. Unplug the charger when the phone is full. Make sure you lock the deadbolt."

*Useful:* Turn it off. • Turn it down. • Unplug it. • Put it away. • Take it out. • Shut it off. • Make sure you… • Don't forget to…

| Another group's best tip |
|---|
| <br><br> |
''')])
L['hw'] = dict(one=dict(head='Write the sentence. Use *it* or *them*.', example='turn off / the lights (them) → *Turn them off.*',
 items=[('turn down / the heat (it)', 'Turn it down.'), ('take out / the trash (past: I / it)', 'I took it out.'),
  ('put away / the dishes (them)', 'Put them away.'), ('make sure / you / lock / the door', 'Make sure you lock the door.')]),
 three='''### 3. Look around your home. Write 3 things you can do to save energy or stay safe.

| My tip (*Turn… / Unplug… / Make sure you…*) | Why? |
|---|---|
| 1. | |
| 2. | |
| 3. | |
''',
 four=dict(head='Review (Lesson 9). Write one word.', items=['I [agree] with you. That\'s true.', 'A bus isn\'t [as] fast as a car.',
  'What do you [think] about the plan?', 'I see your [point], but I\'m not sure.', 'In my [opinion], we need a playground.']))
L['rw'] = dict(kind='notice', note='Read fast first. Then read again and answer the questions.', box_title='CITY POWER · A bill + a flyer (invented)',
 text='''
**MONTHLY BILL.** Account number: 47219 · Name: Sofia Ruiz · Service address: 25 Elm Street, Apt. 3 · Billing period: January 28 to February 27 · Usage: 1,050 kWh (last month: 680 kWh) · Amount due: $142.00 · Due date: March 15. Pay online, by phone, or at any City Power office. If you pay late, there is a $10 late fee.

**SAVE ENERGY, STAY SAFE.** Small changes can make your bill lower. Turn down the thermostat at night; 68 degrees is a good temperature in winter. Turn off the lights when you leave a room. Unplug chargers when your phone is full. Wash clothes in cold water. In summer, use a fan, not only the air conditioner. Stay safe, too: lock the deadbolt at night, and look through the peephole before you open the door. Know where your fire extinguisher is. Do you need help with your bill? Call us at 555-0142 and ask about our free home energy check.
''',
 qs=[('How much is the bill?', '$142.00.', 'Amount due: $142.00'),
  ('When is it due?', 'March 15.', 'Due date: March 15'),
  ('What happens if you pay late?', 'There is a $10 late fee.', 'there is a $10 late fee'),
  ('What is a good temperature at night in winter?', '68 degrees.', '68 degrees is a good temperature in winter'),
  ('What should you do before you open the door?', 'Look through the peephole.', 'look through the peephole before you open the door')],
 write_head='Write an email (5–8 sentences) to a roommate or family member: what should you change at home, and why? Use 2 phrasal verbs and *it* or *them*.',
 write_short='your email',
 example='*Hi Hana, Our electric bill was $142 this month. That\'s too much! Let\'s turn down the heat at night, because 68 degrees is fine. Please turn off the lights when you leave a room. I\'m going to unplug my charger and put it away in the morning. Also, make sure you lock the deadbolt at night. Thanks! Sofia*',
 box_label='My email', checklist=['It has 5–8 sentences.', 'It has 2 phrasal verbs.', 'It has *it* or *them* in the right place.', 'It has a reason (*because…*).'])
L['exit'] = dict(q='What can people do at home to save energy or stay safe?', s1='a tip with a phrasal verb', s2='a tip with *it* or *them*',
 s3='a reason, with *because*', key='*A good answer:* "Turn off the lights when you leave a room. Unplug your charger and put it away. Make sure you lock the deadbolt at night, because it keeps your home safe."')
L['game'] = ('Turn it off!', 'A points to a picture and says, "Can you **unplug** the **charger**?" B mimes and answers, "OK, I\'ll unplug it." Then A gives a tip: "Don\'t forget to lock the **deadbolt**." Switch.')
L['opening'] = dict(cards=['**A:** What do you think about homework for kids?', '**A:** How do you feel about a new parking lot downtown?', '**A:** Is a bus as fast as a car?', '**A:** What should change in your neighborhood?'],
 follow='Do you agree? • Why? • I see your point, but…', hw_head='Write your partner\'s name and their opinion from Homework item 3.', hw_cols=['My partner\'s name', 'Their opinion (*In my opinion…*)'])
L['notes'] = [
 '**Safety stays simple and calm:** practical tips only, no fire stories. Point to where the classroom fire extinguisher is.',
 '**Bills are invented:** never ask about learners\' own bills, rent, or money.',
 '**Bill-help programs vary:** list local ones on the "Keep practicing" sheet. Don\'t promise that a program exists in your area.',
 '***it / them* in the middle:** this is the main rule. Keep *turn it off* (not *turn off it*) on the board all evening.',
 '**Energy Detective:** the problem cards replace a picture. Learners can also point to the My Words pictures.',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening says *going to*. People often say *gonna*. Learners only need to recognize it; they can always say the full form.']
