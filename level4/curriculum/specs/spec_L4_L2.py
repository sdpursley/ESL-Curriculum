import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=2, week=2, title='How Long Have You Lived Here?',
topic='Housing and job applications: addresses, how long, previous jobs, references, and a lease. Learners answer *How long…?* with *for* and *since* and fill in an application.',
cq='Is it still true now? Is it a length of time or a starting point?',
builds=[
 ('Dates and years: *in 2020, in March, on May 5*', 'Level 3 Lessons 2, 8', '**since** + a starting point: *since 2020, since March, since I was 18*'),
 ('*How long…?* with a length: *It takes 20 minutes.*', 'Level 3 Lesson 6', '**for** + a length of time with the **present perfect**: *I\'ve lived here for two years.*'),
 ('*used to* for past habits', 'Level 3 Lesson 12', '**Still true or finished?** *I\'ve worked here since 2022* vs. *I worked at a bakery for two years.*'),
],
objectives=['ask *How long have you lived / worked…?*',
 'answer with *for* + a length of time and *since* + a starting point',
 'choose the present perfect (still true) or the simple past (finished)',
 'give an address, an employer, a position, and a start date on an application',
 'write 5–8 sentences about how long you have done three things, with one *used to*'],
materials=['Board and markers; a timeline across the board ("2020 → now")', 'One copy of a real-looking blank rental application (optional; the Talk Time page works)',
 'Index cards with times: *2020, March, six months, Monday, ten years, a long time, I was 18, three weeks*'],
prep='15 minutes (read the plan; draw the timeline; write the time cards; practice reading the listening script)',
words=[('application', 'application', True), ('current address', 'current_address', True), ('previous address', 'previous_address', True), ('employer', 'employer', True),
 ('position (job title)', 'position', True), ('start date', 'start_date', True), ('end date', 'end_date', True), ('reference (a person)', 'reference', True),
 ('for (two years)', 'for', True), ('since (2020)', 'since', True), ('roommate', 'roommate', False), ('lease', 'lease', False)],
more_vocab='*Also:* apply, fill out, a leasing office, an agent, move in, a supervisor, a photo ID, a fee, refundable, a medical assistant, a mechanic.',
clock=clock('', ' (+ My Words)', '', '*How long have you…?* with *for* and *since*', 'Timeline Interviews + At the Leasing Office', 'A rental application + sentences about you'),
attend='With 5 or fewer, sit at one table. Do Timeline Interviews as one group (each person interviews the person on their left), then pairs for the leasing office. Late arrivals join any pair right away and take the applicant (B) role.',
)
L['steps'] = [
 step1('Opening Talk', '*How long have you…?* and *Have you ever…?*',
  'you ask, "Have you ever tried a new food?" The learner answers. Then you ask, "When did you try it? How was it?" Help them say 3 sentences: the experience, when, and how it was.',
  'Pairs compare Homework item 1 (sentences with *have / has* + a past participle) and read one answer from item 3 to each other. Then they fill in the box on the Opening Talk page.',
  '*I have seen it last year* (→ *I saw it last year*) and a missing participle (*I\'ve never eat* → *eaten*)'),
 step2('*current address* (now) vs. *previous address* (before); *employer* (the company) vs. *position* (your job title); *start date* and *end date* (point to two dates on the board); *reference* (a person who knows you at work; not family). Show *for* as a length (from one date to another) and *since* as a starting point (one date).',
  'ask "Is your employer a company or a person?" (a company, usually) • "Can your mother be your reference?" (no, usually not) • "Is *2020* a length or a starting point?" (a starting point → *since*).',
  'What\'s your current address? → It\'s 418 Elm Street.'),
 step3('Marisol is at a leasing office. She wants to rent an apartment. Mr. Chen helps her with the application. Listen: what is she applying for?',
  'Point to the script lines. *wanna* = want to: "I **want to** fill out an application." *gonna* = going to: "My mother is **going to** live with me." Then practice the weak, short *for* (it sounds like "fer"): *for two years* • *for three years*, and link the words: *How long have you lived here?*', '{EST}'),
 step4('*How long…?* with *for* and *since*', 'draw a timeline: "2020 ———————→ now." Say: "I moved here in 2020. I still live here. I\'ve lived here **since 2020**. That\'s six years. I\'ve lived here **for six years**." Point to 2020 (since) and the whole line (for).',
  'Box 1: read across: *How long have you lived here? → I\'ve lived here for two years / since 2024.* Box 2: still true or finished? *I\'ve worked at the hotel since 2022* (still true) vs. *I worked at a bakery for two years* (finished). Box 3: sort the time words. Box 4: which one?',
  '"*I live here since 2020.* Right or wrong?" (wrong: *I\'ve lived here since 2020.*) • "*since three years* or *for three years*?" (*for*) • "I worked at a bakery for two years. Do I work there now?" (no).',
  'Use the time cards. A picks a card and says it (*March*). B makes a sentence with *for* or *since*: *I\'ve lived here since March.* Switch.'),
 brk('*How long have you lived / worked…? → I\'ve… for (two years). / I\'ve… since (2020).*'),
 step5('Timeline Interviews + At the Leasing Office', 'ask one learner, "How long have you lived in this city?" When they answer, ask, "Where did you live before? How long did you live there?" Write the answers on the board on a timeline. Say: "Still true → *have lived*. Finished → *lived*."',
  '**Timeline Interviews (pairs).** Learners mark 4 points on their own timeline on the first Talk Time page (moved to this city, started a job or class, a hobby, a phone or car). Then they interview a partner: *How long have you…? Since when?* and write 3 sentences about the partner.',
  '**At the Leasing Office (pairs).** A is the agent and asks the questions on the role card. B is the applicant and answers (invented answers are fine). A fills in the application form. Then switch.',
  'pairs for both rounds; rotate once between rounds.', 'pairs for both rounds; one rotation between rounds.',
  'one group for round 1 (each person interviews the person on their left); pairs or one group of 3 for round 2.'),
 step6('A rental application + sentences about you', 'Learners read the rental application on the Read & Write page and answer the questions.',
  'Learners write 5–8 sentences about how long they (or an invented person) have done three things, with *for* and *since* and one *used to*. Show the example. Invented details are fine.'),
 step7('How long have you lived in this city (or worked at your job)?', 'I\'ve lived in this city for four years. I moved here in 2022. I moved here because my sister lives here.',
  'item 1: *she / work / at the hotel / ___ / March → She\'s worked at the hotel since March.*'),
]
L['listen'] = dict(title='How Long Have You Lived Here?', voices={'Narrator': 'N', 'Marisol': 'Ana_af_jessica', 'Mr. Chen': 'Carlos'},
 female=['Narrator', 'Marisol'], names=['Marisol', 'Chen'], tts={},
 setting='Marisol is at a leasing office. She wants to rent an apartment. Mr. Chen helps her with the application.',
 intro='Lesson two. Marisol is at a leasing office. She wants to rent an apartment, and Mr. Chen helps her.',
 lines=[
  ('Mr. Chen', 'Good afternoon. Welcome to Park View Apartments. How can I help you?'),
  ('Marisol', 'Hi. I\'m here about the two-bedroom apartment. I want to fill out an application.'),
  ('Mr. Chen', 'Great. Let\'s do it together. What\'s your current address?'),
  ('Marisol', 'It\'s 418 Elm Street, apartment 3.'),
  ('Mr. Chen', 'And how long have you lived there?'),
  ('Marisol', 'I\'ve lived there for two years.'),
  ('Mr. Chen', 'OK. And your previous address?'),
  ('Marisol', 'Before that, I lived on Lake Road with my cousins. I lived there for three years.'),
  ('Mr. Chen', 'Why are you moving?'),
  ('Marisol', 'My apartment is too small. My mother is going to live with me.'),
  ('Mr. Chen', 'I see. Now, your job. Who\'s your employer?'),
  ('Marisol', 'Green Valley Clinic. I\'m a medical assistant.'),
  ('Mr. Chen', 'How long have you worked there?'),
  ('Marisol', 'Since March 2022. Before that, I worked at a bakery for two years.'),
  ('Mr. Chen', 'And your start date at the clinic? March what?'),
  ('Marisol', 'March fifteenth.'),
  ('Mr. Chen', 'Thank you. We also need one reference. Not a family member, please.'),
  ('Marisol', 'Can I give my supervisor\'s name? She\'s known me since I started.'),
  ('Mr. Chen', 'Sure, that\'s fine. And will you have a roommate?'),
  ('Marisol', 'No, just my mother. When can we move in?'),
  ('Mr. Chen', 'The apartment is ready on June first. The lease is for one year.'),
 ],
 A=dict(q='What is Marisol applying for?', opts=['a job at a clinic', 'an apartment', 'a class at a bakery'], ans=1),
 B=dict(head='Complete Marisol\'s application. Circle the answers.', kind='choice', items=[
  dict(s='How long at the current address: {{*two years|three years|since 2022}}', ev='I\'ve lived there for two years'),
  dict(s='Previous address: {{Elm Street|*Lake Road|Park View}}', ev='I lived on Lake Road with my cousins'),
  dict(s='Employer: {{a bakery|*Green Valley Clinic|Park View Apartments}}', ev='Green Valley Clinic'),
  dict(s='Position: {{*medical assistant|supervisor|baker}}', ev='I\'m a medical assistant'),
  dict(s='Start date: {{March 5, 2022|*March 15, 2022|June 1, 2022}}', ev='March fifteenth'),
  dict(s='Roommate: {{yes|*no}}', ev='No, just my mother'),
 ]),
 C=dict(head='Write *for* or *since*.', items=[
  'I\'ve lived there [for] two years.', 'I lived there [for] three years.', '[Since] March 2022.',
  'Before that, I worked at a bakery [for] two years.', 'She\'s known me [since] I started.', 'The lease is [for] one year.']),
 hear='*wanna* = want to: "I **want to** fill out an application." • *gonna* = going to: "My mother is **going to** live with me." You can say *want to* and *going to*. Say it with a short *for* ("fer"): *I\'ve lived there for two years.* • *How long have you lived here?*',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: *How long…?* with *for* and *since*

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **How long have** you | lived here? | ‖ | I**'ve lived** here | **for** two years. |
| ^ | ^ | ‖ | ^ | **since** 2024. |
| **How long has** she | worked at the clinic? | ‖ | She**'s worked** there | **since** March. |
| **How long has** he | known his supervisor? | ‖ | He**'s known** her | **since** he started. |

### Grammar Box 2: still true or finished?

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **How long have** you | worked at the hotel? | ‖ | I**'ve worked** there | **since** 2022. (still true) |
| **How long did** you | work at the bakery? | ‖ | I **worked** there | **for** two years. (finished) |
| **When did** you | move here? | ‖ | I **moved** here | in 2021. / five years ago. |
| **Did** you | use to live with family? | ‖ | Yes. I **used to** live with my cousins. | Now I live with my mother. |
''',
rule='**still true now** → *have / has* + past participle (*I\'ve lived here since 2020*). **finished** → simple past (*I lived there for three years*). ***for*** + a length of time; ***since*** + a starting point.',
explain='''
### Grammar Box 3: *for* or *since*?

| ***for*** + a length of time | ***since*** + a starting point |
|---|---|
| for two years • for six months | since 2020 • since March |
| for ten days • for a week | since Monday • since last summer |
| for a long time • for 20 minutes | since I was 18 • since I started |

### Grammar Box 4: Which one?

| | WHEN? | EXAMPLE |
|---|---|---|
| *have / has* + past participle | it started in the past and it is **still true now** | *I've worked at the clinic since 2022.* |
| simple past | it is **finished** | *I worked at a bakery for two years.* |
| simple past + *in / ago* | **when** it started | *I moved here in 2021. / five years ago.* |
''',
qa=[('Can I say *I live here since 2020*?', 'No. Use the present perfect: ***I\'ve lived here since 2020.***'),
 ('*For* or *since* with *March*?', '*March* is a starting point: ***since March***. *Three months* is a length: ***for three months***.'),
 ('*I\'ve worked* or *I worked* at the bakery?', 'Do you work there now? Yes → ***I\'ve worked there for two years.*** No → ***I worked there for two years.***')],
A=dict(head='Write *for* or *since*.', items=['I\'ve lived in this city [since] 2021.', 'She\'s worked at the clinic [for] six months.', 'We\'ve had our car [since] January.',
 'He\'s been a cook [for] ten years.', 'They\'ve known each other [since] they were kids.', 'I\'ve studied English [for] a long time.']),
B=dict(head='Circle the correct words.', items=['How long {{*have you lived|do you live}} here?', 'I {{*worked|\'ve worked}} at a bakery for two years. Then I changed jobs.',
 'She {{*\'s had|has}} her car since 2022.', 'When {{*did you move|have you moved}} here?', 'I {{*moved|\'ve moved}} here three years ago.',
 'He\'s lived here {{*since|for}} last summer.']),
mistakes=[('I live here since 2020.', 'I**\'ve lived** here since 2020.'), ('I\'ve lived here since three years.', 'I\'ve lived here **for** three years.'),
 ('I\'ve moved here in 2021.', 'I **moved** here in 2021.'), ('How long you have worked there?', 'How long **have you** worked there?'),
 ('I am here for two years. (still true)', 'I**\'ve been** here for two years.')],
tip='Spanish says *Vivo aquí desde 2020* (present tense). English uses *have / has* + past participle: *I\'ve lived here since 2020* (not *I live here since 2020*). What does your language do?')
L['talk'] = dict(pages=[('Timeline Interviews', '''
### Round 1. Mark 4 points on your timeline. Then interview a partner. Ask *How long have you…?* and *Since when?* Write 3 sentences about your partner.

*Example:* A: How long have you lived in this city? B: Since 2021. A: Where did you live before? B: In Dallas. I lived there for three years. → *Ana has lived in this city since 2021.*

| My timeline | When did it start? (*in 2021 / three years ago*) | *for* or *since*? |
|---|---|---|
| 1. I moved to this city. | <br> | <br> |
| 2. I started my job (or this class). | <br> | <br> |
| 3. I started a hobby: ______________ | <br> | <br> |
| 4. I got my phone (or car). | <br> | <br> |

*Questions:* **How long have you…? • Since when? • When did you start? • Where did you… before? • How long did you… there?**

| 3 sentences about my partner (*… has… for / since…*) |
|---|
| 1. <br><br> |
| 2. <br><br> |
| 3. <br><br> |
'''), ('At the Leasing Office', '''
### Round 2. A is the agent. B is the applicant. A asks the questions and fills in the application. Then switch. Invented answers are fine.

*Role card (A, the agent):* **What's your current address? • How long have you lived there? • What's your previous address? • How long did you live there? • Who's your employer? • What's your position? • What's your start date? • Who's your reference? • Will you have a roommate?**

| RENTAL APPLICATION | |
|---|---|
| Name | <br> |
| Current address | <br> |
| How long? (*for / since*) | <br> |
| Previous address | <br> |
| How long? | <br> |
| Employer and position | <br> |
| Start date | <br> |
| Reference (not family) | <br> |
| Roommate? | ☐ yes ☐ no |

*Useful:* Can you spell that, please? • Is that with an *e* or an *i*? • Sorry, how long?
''')])
L['hw'] = dict(one=dict(head='Write the sentence. Use *for* or *since*.', example='I / live / here / ___ / 2022 → *I\'ve lived here since 2022.*',
 items=[('she / work / at the hotel / ___ / March', 'She\'s worked at the hotel since March.'), ('we / know / our neighbors / ___ / five years', 'We\'ve known our neighbors for five years.'),
  ('he / have / his car / ___ / 2023', 'He\'s had his car since 2023.'), ('I / work / at a bakery / ___ / two years (finished)', 'I worked at a bakery for two years.')]),
 three='''### 3. Ask a family member or a friend 3 questions with *How long have you…?* Write the answers with *for* or *since*.

| Question | Answer (*… for… / … since…*) |
|---|---|
| 1. <br><br> | <br> |
| 2. <br><br> | <br> |
| 3. <br><br> | <br> |
''',
 four=dict(head='Review (*used to*). Write *used to*, *use to*, or *didn\'t use to*.', items=['I [used to] live with my cousins. Now I have my own apartment.',
  'She [used to] work at night. Now she works in the day.', 'Did you [use to] play soccer?', 'We [didn\'t use to] have a car. We took the bus.',
  'He [used to] take the bus. Now he drives.']))
L['rw'] = dict(kind='form', note='Read fast first. Then read again and answer the questions.', box_title='PARK VIEW APARTMENTS · Rental Application',
 text='''
**Please read:** Fill out every part. Write your addresses for the last five years. If you need more space, use the back of the page. Bring a photo ID. We will call your references, so please check the phone numbers. The application fee is $35, and it is not refundable.

**1. Applicant:** David Morales • **Phone:** (555) 201-3388

**2. Current address:** 77 River Avenue, Apt. 12 • **How long?** Since August 2023 • **Reason for moving:** I need a bigger apartment for my family.

**3. Previous address:** 1520 Hill Street • **How long?** For four years (2019–2023)

**4. Employer:** City Bus Company • **Position:** mechanic • **Start date:** 05/2021 • I've worked here for five years.

**5. Previous employer:** Quick Lube Auto Shop • **Position:** oil change technician • 2017–2021

**6. Reference (not a family member):** Ana Ruiz, my supervisor • She has known me since 2021.

**7. Roommates:** none • **People in the apartment:** 3 (me, my wife, and my son)
''',
 qs=[('How long has David lived at his current address?', 'Since August 2023.', 'Since August 2023'),
  ('How long did he live on Hill Street?', 'For four years (2019–2023).', 'For four years (2019–2023)'),
  ('Who is his employer?', 'City Bus Company.', 'Employer: City Bus Company'),
  ('Who is his reference?', 'Ana Ruiz, his supervisor.', 'Ana Ruiz, my supervisor'),
  ('Why is he moving?', 'He needs a bigger apartment for his family.', 'I need a bigger apartment for my family')],
 write_head='Write about how long you (or an invented person) have done three things (5–8 sentences). Use *for* and *since*. Add one sentence with *used to*.',
 write_short='your sentences',
 example='*I\'ve lived in this city since 2021. I\'ve worked at a hotel for three years. I used to work at a bakery, but I\'ve worked at the hotel since 2023. I\'ve studied English since last fall. I\'ve had my car for six months, so I don\'t take the bus now.*',
 box_label='My sentences', checklist=['It has 5–8 sentences.', 'It has *for* + a length of time.', 'It has *since* + a starting point.', 'It has one sentence with *used to*.'])
L['exit'] = dict(q='How long have you lived in this city (or worked at your job)?', s1='how long (*for* or *since*)', s2='when you started (*I moved / started… in…*)',
 s3='why, with *because*', key='*A good answer:* "I\'ve lived in this city for four years. I moved here in 2022. I moved here because my sister lives here."')
L['game'] = ('Fill out the form!', 'A points to a picture and asks a question: "**employer**: Who\'s your employer?" B answers: "I work for City Hospital." Switch.')
L['opening'] = dict(cards=['**A:** Have you ever tried a new food? What was it?', '**A:** Have you ever seen the ocean? Where?', '**A:** What have you never done, but you want to try?', '**A:** Have you ever won a prize?'],
 follow='When did you…? • How was it? • Why?', hw_head='Write your partner\'s name and one thing your partner has done.', hw_cols=['My partner\'s name', 'One thing my partner has done'])
L['notes'] = [
 '**Learners choose what to share.** Always ask about *this city* or *this job*, never *this country*. Never ask about income, rent, or immigration papers. Invented addresses and answers are fine in every activity.',
 '**The timeline:** keep "2020 → now" on the board all night. The starting point = *since*; the length = *for*. Still true now → *have lived*; finished → *lived*.',
 '**Real forms:** a rental application often asks for 3–5 years of addresses and a reference who is not family. Learners can write *N/A* (not applicable) when a line doesn\'t fit them.',
 '**Spelling and numbers:** in the leasing office role play, the agent asks *Can you spell that?* Encourage learners to say street numbers in pairs: *418* = "four eighteen."',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening says *going to* and *want to*. People often say *gonna* and *wanna*. Learners only need to recognize the short forms; they can always say the full forms.']
