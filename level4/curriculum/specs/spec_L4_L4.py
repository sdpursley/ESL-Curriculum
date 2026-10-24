import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=4, week=4, title='How Long Have You Had It?',
topic='Health: a new-patient health history form, a mild symptom at a clinic, dental and preventive care, and reading an insurance card. Learners say how long they\'ve had a symptom and make suggestions with *Why don\'t you…? / You could… / It\'s a good idea to…* Everything is invented, practical, and calm.',
cq='Is it still true now? Is it a strong idea or a soft idea?',
builds=[
 ('*How long have you…? for / since*', 'Level 4 Lesson 2', '**present perfect for health**: *How long have you had this rash? → I\'ve had it for three days. / since Monday.*'),
 ('*Have you ever…?* + simple past for the time', 'Level 4 Lesson 1', '**health history**: *Have you ever had surgery? → Yes, I had knee surgery in 2018.*'),
 ('*should* for advice', 'Level 2', '**suggestions**: *Why don\'t you…? / You could… / It\'s a good idea to…* (softer than *should*)'),
],
objectives=['describe a symptom and say how long they\'ve had it (*for / since*)',
 'answer health history questions (*Have you ever had…?*)',
 'make a suggestion with *Why don\'t you…? / You could… / It\'s a good idea to…*',
 'find key information on an insurance card and a clinic letter (copay, deductible)',
 'write an email to a friend (5–8 sentences) with suggestions and reasons'],
materials=['Board and markers', 'Symptom cards and problem cards (in the workbook Talk Time pages; copy them onto index cards, optional)',
 'Optional: an old, blank clinic form or a sample insurance card (invented, no real names or numbers)'],
prep='15 minutes (read the plan; practice reading the listening script; draw a simple form on the board)',
words=[('checkup', 'checkup', True), ('health history', 'health_history', True), ('symptom', 'symptom', True), ('allergy', 'allergy', True), ('blood pressure', 'blood_pressure', True),
 ('rash', 'rash', True), ('dizzy', 'dizzy', True), ('teeth cleaning', 'teeth_cleaning', True), ('cavity', 'cavity', True), ('flu shot', 'flu_shot', True),
 ('prescription', 'prescription', True), ('copay', 'copay', False)],
more_vocab='*Also:* a medical assistant, a receptionist, a backache, a cough, a sore throat, a heating pad, a stretch, surgery, allergic to, an insurance card, a member ID, a deductible.',
clock=clock('', ' (+ My Words)', '', 'Present perfect for health + suggestions', 'Clinic Intake + Good Idea Circle', 'A clinic letter + an insurance card; an email to a friend',
 talk_group='Pairs back to back, then circles of 5'),
attend='With 5 or fewer, do Clinic Intake in pairs (you are a patient if there is an odd number), then one Good Idea Circle; you add problem cards. Late arrivals join a circle and suggest first.',
)
L['steps'] = [
 step1('Opening Talk', '*Have you… yet?* and *already / just*',
  'you ask, "Have you done your laundry yet this week?" The learner answers with *already* or *not yet*. Then you ask, "When did you do it?" Help them say 3 sentences.',
  'Pairs compare Homework item 1 (*already / yet / just* sentences) and read their to-do list (item 3) to each other. Then they fill in the box on the Opening Talk page.',
  '*I\'ve finished it yesterday* (→ *I finished it yesterday*) and *Have you yet…?* (→ *yet* at the end)'),
 step2('*checkup* (a visit when you are well); *health history* (a form: your past illnesses, surgery, allergies); *symptom* (what you feel: a cough, a rash); *allergy* (*I\'m allergic to peanuts*); *blood pressure* (mime the arm cuff: *120 over 80*); *dizzy* (mime the room turning); *teeth cleaning* and *cavity* (a hole in a tooth); *flu shot*; *prescription* (paper from the doctor for medicine); *copay* (the money you pay at each visit).',
  'ask "Do you get a checkup when you are sick or when you are well?" (when you are well; it\'s every year) • "Is a cough a symptom?" (yes) • "Do you pay a copay at the clinic or at home?" (at the clinic).',
  'How long have you had the cough? → I\'ve had it since Sunday.'),
 step3('Amina is at a clinic. First, Daniel, the medical assistant, asks her some questions. Then she talks to Ms. Park, the receptionist. Listen: why is Amina at the clinic?',
  'Point to the script lines. *gonna* = going to: "The doctor\'s **going to** see you in a few minutes." *wanna* = want to: "I **want to** make an appointment." Then practice *Why don\'t you…?* as one smooth group with falling intonation (a suggestion, not a real question), and the stress: *I\'ve had a RASH since MONday.*', '{EST}'),
 step4('present perfect for health + suggestions', 'say, "I have a cough. It started on Sunday. Today is Thursday." Write: *I\'ve **had** a cough **since** Sunday. I\'ve had it **for** four days.* Then hold your back: "My back hurts." Point to a learner and help them say, "**Why don\'t you** call the clinic?" Write three suggestions on the board.',
  'Box 1: read across: *How long have you had this rash? → I\'ve had it for three days.* and *Have you ever had surgery? → Yes, I had knee surgery in 2018.* Box 2: a problem → a suggestion. Box 3: how to say a symptom. Box 4: strong or soft?',
  '"*I have a rash since Monday.* Right or wrong?" (wrong: *I\'ve had a rash since Monday.*) • "*You could to try* or *You could try*?" (*You could try*) • "Is *Why don\'t you call?* a real question?" (no, it\'s a suggestion).',
  'A says a problem from Box 2. B gives a suggestion with *Why don\'t you… / You could…* A says, "Good idea." Switch.'),
 brk('*How long have you had it? → I\'ve had it for… / since… • Why don\'t you…? / You could… / It\'s a good idea to…*'),
 step5('Clinic Intake + Good Idea Circle', 'sit back to back with a learner. You are the medical assistant: "What brings you in today?" The learner reads a symptom card: "I have a rash on my arm." You ask, "How long have you had it?" Then switch: the learner asks you. Say: "Answer, then add one more detail."',
  '**Clinic Intake (pairs, back to back).** A is the medical assistant and asks the 8 form questions; B chooses a symptom card and answers (invented answers). A writes short notes. Then switch, with a new card.',
  '**Good Idea Circle (circles of 5).** One learner reads a problem card. The next two learners each give a suggestion. The first learner chooses one and says why: *"Good idea. I\'m going to… because…"* Then the next learner reads a card.',
  'pairs for round 1; then 3 circles of 5 for round 2.', 'pairs for round 1; then one circle for round 2.',
  'pairs (you join if there is an odd number) for round 1. In round 2, make one circle; you add problem cards and suggest first.'),
 step6('A clinic letter + an insurance card', 'Learners read the letter from the clinic and the insurance card on the Read & Write page and answer the questions. Point to *copay* and *deductible* on the card.',
  'Learners write an email to a friend (5–8 sentences). The friend has had a backache for a week. Ask how long, give two suggestions with reasons, and say what to bring to the clinic. Show the example. Invented details are fine.'),
 step7('A friend has had a backache for a week. What do you say?', 'How long have you had it? Why don\'t you call the clinic? It\'s a good idea because a week is a long time.',
  'item 1: *she / have / a rash / ___ / three days → She\'s had a rash for three days.*'),
]
L['listen'] = dict(title='How Long Have You Had It?', voices={'Narrator': 'N', 'Amina': 'Rosa', 'Daniel': 'Marco', 'Ms. Park': 'Receptionist'},
 female=['Narrator', 'Amina', 'Ms. Park'], names=['Amina', 'Daniel', 'Park'], tts={},
 setting='Amina is at a clinic for back pain. First, Daniel, the medical assistant, asks her health history questions. Then, at checkout, she talks to Ms. Park, the receptionist.',
 intro='Lesson four. Amina is at a clinic. First, she talks to Daniel, the medical assistant.',
 lines=[
  ('Daniel', 'Hi, Amina. I\'m Daniel. I\'m going to ask you a few questions for your health history. What brings you in today?'),
  ('Amina', 'My lower back hurts. It isn\'t very bad, but it hasn\'t stopped.'),
  ('Daniel', 'I\'m sorry to hear that. How long have you had the back pain?'),
  ('Amina', 'I\'ve had it for about two weeks. It started when I moved some heavy boxes.'),
  ('Daniel', 'OK. Have you ever had back problems before?'),
  ('Amina', 'No, never. This is the first time.'),
  ('Daniel', 'Have you ever had surgery?'),
  ('Amina', 'Yes, I had knee surgery in 2018.'),
  ('Daniel', 'Thank you. Do you have any allergies?'),
  ('Amina', 'Yes, I\'m allergic to penicillin. I get a rash.'),
  ('Daniel', 'I\'ll write that down. Have you tried anything for the pain?'),
  ('Amina', 'I\'ve used a heating pad a few times. It helps a little.'),
  ('Daniel', 'Have you felt dizzy?'),
  ('Amina', 'No, I haven\'t.'),
  ('Daniel', 'Good. Now let me check your blood pressure. It looks normal. The doctor\'s going to see you in a few minutes.'),
  ('Narrator', 'Later, at checkout, Amina talks to Ms. Park, the receptionist.'),
  ('Ms. Park', 'Hi, Amina. Your copay today is twenty dollars.'),
  ('Amina', 'OK. Here\'s my new insurance card. I\'ve had it since January.'),
  ('Ms. Park', 'Thank you. Also, you haven\'t had a teeth cleaning for a year, and you haven\'t had a checkup since last spring. It\'s a good idea to get one every six months.'),
  ('Amina', 'You\'re right. I want to make an appointment with the dentist.'),
  ('Ms. Park', 'Why don\'t you call the dental office tomorrow? Here\'s the number. And you could get a flu shot here next week.'),
  ('Amina', 'Good idea. Thank you!'),
 ],
 A=dict(q='Why is Amina at the clinic?', opts=['for a flu shot', 'for back pain', 'for a teeth cleaning'], ans=1),
 B=dict(head='Complete Amina\'s form. Circle the answer.', kind='choice', items=[
  dict(s='Symptom: {{a rash|*back pain|a cough}}', ev='My lower back hurts'),
  dict(s='How long? {{two days|*about two weeks|since January}}', ev='I\'ve had it for about two weeks'),
  dict(s='Back problems before? {{yes|*no}}', ev='No, never. This is the first time.'),
  dict(s='Allergy: {{peanuts|*penicillin|none}}', ev='I\'m allergic to penicillin'),
  dict(s='Dizzy? {{yes|*no}}', ev='No, I haven\'t.'),
  dict(s='Copay today: {{$10|*$20|$40}}', ev='Your copay today is twenty dollars'),
 ]),
 C=dict(head='Write *for*, *since*, or *ever*.', items=[
  'I\'ve had it [for] about two weeks.', 'Have you [ever] had back problems before?', 'Have you [ever] had surgery?',
  'I\'ve had it [since] January.', 'Also, you haven\'t had a teeth cleaning [for] a year', 'and you haven\'t had a checkup [since] last spring.']),
 hear='*gonna* = going to: "The doctor\'s **going to** see you in a few minutes." • *wanna* = want to: "I **want to** make an appointment." You can say *going to* and *want to*. Say *Why don\'t you…?* as one smooth group, with your voice going down at the end: it\'s a suggestion, not a real question. Stress: *I\'ve had a RASH since MONday.*',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: *How long…? / Have you ever…?*

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **How long have** you | **had** this rash? | ‖ | I**'ve had** it | **for** three days. |
| ^ | ^ | ‖ | ^ | **since** Monday. |
| **How long has** your back | **hurt**? | ‖ | It**'s hurt** | **for** about two weeks. |
| **Have** you **ever** | **had** surgery? | ‖ | No, **never**. / Yes, I **have**. | I **had** knee surgery in 2018. |
| **Have** you | **tried** anything for it? | ‖ | Yes, I **have**. | I**'ve used** a heating pad. |

### Grammar Box 2: a problem → a suggestion

<!-- subst -->
| PROBLEM | < | ‖ | SUGGESTION | < |
|---|---|---|---|---|
| My back hurts. | What can I do? | ‖ | **Why don't you** | **call** the clinic? |
| I sit all day at work. | Any ideas? | ‖ | You **could** | **take** a short walk at lunch. |
| I haven't had a checkup | for two years. | ‖ | **It's a good idea to** | **get** one every year. |
| My tooth has hurt | since Friday. | ‖ | You **should** | **see** a dentist soon. |
''',
rule='Use ***have / has* + past participle** + *for / since* for a problem that started in the past and is **still true**. After ***Why don\'t you, You could, It\'s a good idea to,*** and ***should***, use the base verb (*call, try, get*).',
explain='''
### Grammar Box 3: how to say a symptom

| SAY | EXAMPLES |
|---|---|
| *I have / I've had* + a noun | *a rash, a cough, a backache, a sore throat* → *I've had a cough since Sunday.* |
| *My* ___ *hurts / has hurt* | *My back hurts. My tooth has hurt for a week.* |
| *I feel / I've felt* + a word | *dizzy, tired* → *I've felt tired for three days.* |

### Grammar Box 4: strong or soft?

| | HOW STRONG? | EXAMPLE |
|---|---|---|
| *You should…* | **strong** advice | *You should see a doctor.* |
| *It's a good idea to…* | a **general** idea (good for everyone) | *It's a good idea to get a flu shot every year.* |
| *Why don't you…? / You could…* | a **soft** idea; the person chooses | *Why don't you try a heating pad? You could stretch.* |
''',
qa=[('Can I say *I have a rash since Monday*?', 'No. It started in the past and is still true: ***I\'ve had a rash since Monday.***'),
 ('Is *Why don\'t you call the clinic?* a real question?', 'No. It\'s a suggestion. Answer: ***Good idea. / Thanks, I will.*** Your voice goes down at the end.'),
 ('*You could to try* or *You could try*?', 'After *could*, use the base verb: ***You could try a heating pad.***')],
A=dict(head='Write the correct form of the verb.', items=['How long have you [had] the cough? (have)', 'Why don\'t you [call] the clinic? (call)',
 'I\'ve [felt] dizzy since this morning. (feel)', 'You could [try] some easy stretches. (try)', 'It\'s a good idea to [get] a flu shot every year. (get)',
 'Have you ever [had] surgery? (have)']),
B=dict(head='Circle the correct words.', items=['I {{*\'ve had|have}} a rash since Saturday.', 'You could {{*try|to try}} a heating pad.',
 '{{*Why don\'t you|Why you don\'t}} call the dentist?', 'My tooth has hurt {{*for|since}} a week.', 'I {{*had|\'ve had}} knee surgery in 2018.',
 'It\'s a good idea {{*to get|get}} a checkup.']),
mistakes=[('I have a rash since Monday.', 'I**\'ve had** a rash since Monday.'), ('You could to call the clinic.', 'You could **call** the clinic.'),
 ('Why you don\'t try a heating pad?', '**Why don\'t you** try a heating pad?'), ('It\'s a good idea get a checkup.', 'It\'s a good idea **to** get a checkup.'),
 ('I\'ve had surgery in 2018.', 'I **had** surgery in 2018.')],
tip='Spanish *¿Por qué no llamas a la clínica?* = *Why don\'t you call the clinic?* It\'s a suggestion, not a real question, in Spanish and in English. But Spanish *Tengo un sarpullido desde el lunes* is ***I\'ve had** a rash since Monday* in English, not *I have*. What does your language do?')
FORM = lambda rows: '\n'.join(f'| {i}. {q} | |' for i, q in enumerate(rows, 1))
L['talk'] = dict(pages=[('Clinic Intake', '''
### Round 1. Sit back to back. A is the medical assistant and asks the questions. B is the patient: choose a symptom card and answer. A writes short notes. Then switch, with a new card.

| SYMPTOM CARDS (invented) | |
|---|---|
| 1. a rash on your arm, for 3 days | 2. a backache, since Saturday |
| 3. a sensitive tooth, for a week | 4. a cough, since Sunday |

| HEALTH HISTORY FORM | Notes |
|---|---|
''' + FORM(['What brings you in today?', 'How long have you had it?', 'Have you ever had this before?', 'Have you tried anything for it?',
 'Do you have any allergies?', 'Have you ever had surgery?', 'Have you had a flu shot this year?', 'When was your last checkup?']) + '''

*Example:* A: What brings you in today? B: I have a rash on my arm. A: How long have you had it? B: I've had it for three days. A: Have you ever had this before? B: No, never.

*Useful (medical assistant):* I'm sorry to hear that. • I'll write that down. • The doctor's going to see you soon.
'''), ('Good Idea Circle', '''
### Round 2. Work in a circle. One person reads a problem card. The next two people each give a suggestion. The first person chooses one and says why. Then the next person reads a card.

| PROBLEM CARDS | |
|---|---|
| 1. I sit all day at work. | 2. I haven't had a checkup for two years. |
| 3. My tooth has hurt since Friday. | 4. I feel tired every afternoon. |
| 5. I've had a cough for a week. | 6. I want to get a flu shot. Where? |
| 7. My back hurts after work. | 8. I don't understand my insurance card. |

*Suggest:* Why don't you…? • You could… • It's a good idea to…
*Choose:* Good idea. I'm going to… because… • Thanks. I like that idea because…

*Example:* A: I sit all day at work. B: Why don't you take a short walk at lunch? C: You could stand up every hour. A: Good idea. I'm going to walk at lunch because I like being outside.

| My problem card and the idea I chose (and why) |
|---|
| <br><br><br> |

*Remember:* for a real health question, ask your doctor or pharmacist. In an emergency, call 911.
''')])
L['hw'] = dict(one=dict(head='Write the sentence. Use the words.', example='I / have / a cough / ___ / Sunday → *I\'ve had a cough since Sunday.*',
 items=[('she / have / a rash / ___ / three days', 'She\'s had a rash for three days.'), ('why / not / you / call / the dentist?', 'Why don\'t you call the dentist?'),
  ('you / could / try / a heating pad', 'You could try a heating pad.'), ('he / ever / have / surgery?', 'Has he ever had surgery?')]),
 three='''### 3. Write 3 good ideas to stay healthy. Use *It's a good idea to… / You could… / Why don't you…?* and give a reason.

| Good idea | Why? |
|---|---|
| 1. <br><br> | <br><br> |
| 2. <br><br> | <br><br> |
| 3. <br><br> | <br><br> |
''',
 four=dict(head='Review (Lesson 3). Write *already*, *yet*, or *just*.', items=['I\'ve [already] made a dentist appointment. It\'s on Monday.', 'Have you had your flu shot [yet]?',
  'The clinic has [just] called. They called a minute ago.', 'I haven\'t picked up my prescription [yet].', 'We\'ve [already] paid the copay. We paid it this morning.']))
L['rw'] = dict(kind='letter', note='Read fast first. Then read again and answer the questions.', box_title='LETTER · Riverside Family Clinic + an insurance card',
 text='''
**Riverside Family Clinic** • 410 Main Street • (555) 330-2100 • Dear Carmen Lopez,

Our records show that you have not had a yearly checkup since March 2025. It's a good idea to see your doctor once a year, even when you feel well. At a checkup, we check your blood pressure, update your health history, and answer your questions.

**Stay healthy this year:** ✓ Get a checkup every year. ✓ Get a teeth cleaning every six months. ✓ Get a flu shot every fall.

**Please bring:** your insurance card, a photo ID, and a list of any medicines you take.

**Your copay:** look at your insurance card. Your copay is the amount you pay at each visit. Some tests cost more if you have not paid your full deductible yet.

To make an appointment, call us. We are open Monday to Saturday, 8:00 a.m. to 6:00 p.m. Sincerely, Riverside Family Clinic

**INSURANCE CARD (invented):** BlueRiver Health Plan • Member: CARMEN LOPEZ • Member ID: BRH 448 2190 • Copay: Doctor $20 • Specialist $40 • Urgent care $50 • Deductible: $1,000
''',
 qs=[('When did Carmen have her last checkup?', 'In March 2025.', 'since March 2025'),
  ('How often is it a good idea to get a teeth cleaning?', 'Every six months.', 'Get a teeth cleaning every six months'),
  ('What three things should she bring?', 'Her insurance card, a photo ID, and a list of her medicines.', 'your insurance card, a photo ID, and a list of any medicines you take'),
  ('What is her copay for a doctor visit?', '$20.', 'Copay: Doctor $20'),
  ('How much is her deductible?', '$1,000.', 'Deductible: $1,000')],
 write_head='Write an email to a friend (5–8 sentences). Your friend has had a backache for a week. Ask how long, give two suggestions with reasons, and say what to bring to the clinic.',
 write_short='your email',
 example='*Hi, Rosa. I\'m sorry your back hurts. How long have you had the pain? Why don\'t you call the clinic tomorrow? It\'s a good idea because a week is a long time. You could also try a heating pad, because it helps my back. Don\'t forget to bring your insurance card and a photo ID. Feel better soon! Marta*',
 box_label='My email', checklist=['It has 5–8 sentences.', 'It has a question with *How long…?*', 'It has two suggestions.', 'It has a reason with *because*.'])
L['exit'] = dict(q='A friend has had a backache for a week. What do you say?', s1='ask how long (*How long have you…?*)', s2='a suggestion (*Why don\'t you… / You could…*)',
 s3='a reason, with *because*', key='*A good answer:* "How long have you had it? Why don\'t you call the clinic? It\'s a good idea because a week is a long time."')
L['game'] = ('Symptom or suggestion?', 'A points to a picture and says a problem, for example, "I\'ve had a **rash** since Monday." B gives a suggestion: "Why don\'t you call the clinic?" Switch.')
L['opening'] = dict(cards=['**A:** Have you done your laundry yet this week?', '**A:** What have you already done today?', '**A:** Have you paid your bills yet this month?', '**A:** Have you cooked dinner yet today?'],
 follow='When did you…? • What haven\'t you done yet? • Why?', hw_head='Write your partner\'s name and one thing they\'ve already done.', hw_cols=['My partner\'s name', 'Already done (*already / just*)'])
L['notes'] = [
 '**Keep health invented and mild.** All patients and symptoms are invented. Never ask learners about their own health, medicines, or insurance. If a learner shares something, thank them and move on.',
 '**Real health questions:** say, "For a real health question, ask your doctor or pharmacist. In an emergency, call 911." It is printed on the Good Idea Circle page.',
 '**Insurance:** stay at "read the card; know *copay* and *deductible*." A copay is what you pay at each visit; a deductible is what you pay first in a year before the plan pays more. Don\'t explain plans or prices.',
 '**for / since:** *for* + a length of time (*three days*); *since* + a start (*Monday, January*). With a finished time (*in 2018*), use the simple past.',
 '***Why don\'t you…?*** is a suggestion, not a real question. Model falling intonation. Learners answer *Good idea* or *Thanks, I will*, not *Because…*.',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening says *going to* and *want to*. People often say *gonna* and *wanna*. Learners only need to recognize the short forms; they can always say the full forms.']
