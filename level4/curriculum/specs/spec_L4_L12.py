import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from std import *
L = dict(N=12, week=13, title='Is It a Scam?',
topic='Consumer protection, calm and practical: recognizing common scams by phone, text, and email (a fake prize, a fake bank text, a fake "pay your bill today" call, payment with gift cards) and what to do: stop, don\'t pay, check with the real company, and tell someone. Learners describe people and messages with *who / that*. All messages, names, and numbers are invented.',
cq='Is it real or is it a scam? What should you do?',
builds=[
 ('*something / anyone*', 'Level 3 Lesson 12', '***Never give your PIN to anyone.***'),
 ('*must / mustn\'t, should*', 'Level 3', '*You mustn\'t share your password. You should tell someone.*'),
 ('describing people and things', 'Levels 2–3', '***who / that***: *a man who called, a text that came*'),
],
objectives=['describe a person or a message with *who / that* (*a caller who asks for gift cards*)',
 'name 4 warning signs of a scam',
 'say what to do with a suspicious call or text (stop, don\'t pay, check, tell someone)',
 'give a safe answer on the phone (*I don\'t give information on the phone. Goodbye.*)',
 'write a message (5–8 sentences) to warn a family member about a scam'],
materials=['Board and markers', 'The 10 message cards on the Talk Time page (copy and cut them, optional)', 'A local consumer-help phone number for the "Keep practicing" sheet (check it locally)'],
prep='15 minutes (read the plan; practice reading the listening script; find and check a local consumer-help number)',
words=[('scam', 'scam', True), ('warning sign', 'warning_sign', True), ('suspicious', 'suspicious', True), ('fake', 'fake', True), ('official', 'official', True),
 ('gift card', 'gift_card', True), ('prize', 'prize', True), ('link', 'link', True), ('PIN', 'pin', True), ('hang up', 'hang_up', True),
 ('block (a number)', 'block', True), ('trust', 'trust', False)],
more_vocab='*Also:* a trick, a caller, information, a password, an account, pushy, hurry, a package, a real bill, a consumer.',
clock=clock('', ' (+ My Words)', '', '*who / that*', 'Real or Scam? + Safe Answer', 'A consumer tips flyer + a sample text; a message',
 talk_group='Pairs, then groups of 4, then pairs'),
attend='With 5 or fewer, sort the message cards together as one group, then do Safe Answer in pairs (you are the caller if needed). Late arrivals join the sort and take a caller card in round 2.',
)
L['steps'] = [
 step1('Opening Talk', '*to* + verb (why); *enjoy* + *-ing*',
  'you say, "Where would you like to go on a trip?" The learner answers with *to* + verb (*I\'d like to go to Chicago to see the lake.*). Then you ask, "What do you enjoy doing there?" Help them say 3 sentences.',
  'Pairs compare Homework item 1 (*to / -ing*) and read their trip plan (item 3) to each other. Then they fill in the box on the Opening Talk page.',
  '*for see* (→ *to see*) and *enjoy to travel* (→ *enjoy traveling*)'),
 step2('*scam* (a trick that takes your money); *warning sign* (something that tells you to be careful); *suspicious* (strange, maybe not true); *fake* (not real); *official* (real, from the company); *gift card*; *prize*; *link* (you click it in a text or email); *PIN* (your secret number); *hang up* (end the call); *block (a number)*; *trust*.',
  'ask "Is a fake message real or not real?" (not real) • "Do you give your PIN to a caller or to nobody?" (nobody) • "When a call is suspicious, do you hang up or pay?" (hang up).',
  'Never give your PIN to anyone.'),
 step3('Mrs. Lopez gets a phone call from a man who says he\'s from the electric company. Later, she talks to her son, Daniel. Listen: was it a scam?',
  'Point to the script line. *gonna* = going to: "We\'re **gonna** turn off your power." Then practice the weak *that* (it sounds like "thut"): *a text that asks*. Stress the key words: *NEVER, GIFT cards*. Practice a calm, firm voice: *No, thank you. Goodbye.*', '{EST}'),
 step4('*who / that*', 'hold up your phone and say, "This morning I got a text. The text said I won a prize. → I got a text **that** said I won a prize." Then: "A man called. The man wanted my PIN. → A man **who** called wanted my PIN." Write: *who* = people, *that* = things (and people). Cross out *a man who he called*.',
  'Box 1: read across: *What\'s a scam? → It\'s a trick that takes your money.* Box 2: what to do: *Hang up on a caller who asks for gift cards.* Box 3: *never… anyone, must / should*. Box 4: the 4 steps.',
  '"*who* or *that* for a text?" (*that*) • "*a man who he called* or *a man who called*?" (*a man who called*) • "Are most calls scams?" (no, most are real).',
  'A points to a picture and asks, "What\'s a **gift card** scam?" B answers with *who / that*: "It\'s a call **that** asks you to pay with gift cards." Switch.'),
 brk('*It\'s a trick that takes your money. • Don\'t trust a caller who asks for gift cards. • Stop. Don\'t pay. Check. Tell someone.*'),
 step5('Real or Scam? + Safe Answer', 'read card 1: "Your package is late. Click this link and pay $2.99 today." Say, "I think it\'s probably a scam. It\'s a text **that** has a strange link, and it asks for money today." Then model a safe answer: a learner reads caller card 1, and you say calmly, "I don\'t give information on the phone. I\'ll call the number on my card. Goodbye."',
  '**Real or Scam? (pairs).** Pairs sort the 10 invented message cards into *probably real* and *probably a scam* and explain with *It\'s a text that… / It\'s from someone who…* Then they compare with another pair.',
  '**Safe Answer (pairs).** A is a caller with a pushy (but polite) card. B gives a safe answer. Switch.',
  'pairs; then groups of 4 to compare; then pairs.', 'pairs; then one group to compare.', 'the whole group sorts together; then pairs.'),
 step6('A consumer tips flyer + a sample scam text', 'Learners read the invented flyer and the sample text on the Read & Write page and answer the questions.',
  'Learners write a message (5–8 sentences) to a family member about a scam text, with *that / who* and *Don\'t…*. Show the example.'),
 step7('What is one warning sign of a scam, and what should you do?', 'A caller who asks for gift cards is a warning sign. You should hang up and call the real company. Don\'t pay, because real companies don\'t take gift cards.',
  'item 1: *don\'t trust / a caller / ask for gift cards (who) → Don\'t trust a caller who asks for gift cards.*'),
]
L['listen'] = dict(title='Is It a Scam?', voices={'Narrator': 'N', 'Mrs. Lopez': 'Kim', 'Caller': 'Carlos', 'Daniel': 'Sam'},
 female=['Narrator', 'Mrs. Lopez'], names=['Lopez', 'Daniel', 'Mike', 'City Power'], tts={},
 setting='A man calls Mrs. Lopez and says he is from the electric company. She must pay today with gift cards. She says no and hangs up. Then she tells her adult son, and they check her real account. No money is lost.',
 intro='Lesson twelve. Mrs. Lopez gets a phone call. Later, she talks to her son, Daniel.',
 lines=[
  ('Caller', 'Hello, is this Mrs. Lopez? This is Mike from the electric company. Your bill is late. You must pay today, or we\'re gonna turn off your power in one hour.'),
  ('Mrs. Lopez', 'What? My bill is late? I paid it last week.'),
  ('Caller', 'No, ma\'am. You owe two hundred dollars. Go to the store and buy gift cards. Then call me back and read me the numbers.'),
  ('Mrs. Lopez', 'Gift cards? That\'s strange.'),
  ('Caller', 'Please hurry. This is your last chance. Don\'t tell anyone.'),
  ('Mrs. Lopez', 'No, thank you. I\'m going to call the number that is on my real bill. Goodbye.'),
  ('Daniel', 'Hi, Mom. You look worried. What\'s wrong?'),
  ('Mrs. Lopez', 'The man who called me knew my name. He said he was from the electric company. He wanted me to pay with gift cards.'),
  ('Daniel', 'Gift cards? That\'s a warning sign. A company that asks for gift cards is a scam. What did you do?'),
  ('Mrs. Lopez', 'I said no, and I hung up.'),
  ('Daniel', 'Good! You did the right thing. Scammers are people who want your money. Did you give him any information?'),
  ('Mrs. Lopez', 'No. I didn\'t tell him anything.'),
  ('Daniel', 'Great. Let\'s check your account on the City Power website. OK, here it is. Your account is fine. You don\'t owe any money.'),
  ('Mrs. Lopez', 'Oh, good. I\'m glad I didn\'t pay.'),
  ('Daniel', 'Me too. Next time, you can block the number. Be careful with texts that ask for your password, too. And never trust a caller who tells you to hurry.'),
  ('Mrs. Lopez', 'You\'re right. Thanks, Daniel.'),
 ],
 A=dict(q='Was it a scam?', opts=['Yes, it was a scam.', 'No, the bill was really late.', 'We don\'t know.'], ans=0),
 B=dict(head='Which warning signs did you hear? Circle the answer.', kind='choice', items=[
  dict(s='The caller said she must pay {{*today|next month}}.', ev='You must pay today'),
  dict(s='He wanted her to pay with {{*gift cards|a check}}.', ev='buy gift cards'),
  dict(s='He said, "{{*Don\'t tell anyone.|Call your son.}}"', ev='Don\'t tell anyone.'),
  dict(s='He said they would turn off her power in {{*one hour|one week}}.', ev='in one hour'),
  dict(s='Mrs. Lopez {{*hung up|paid $200}}.', ev='I said no, and I hung up.'),
  dict(s='Her real account is {{*fine|late}}.', ev='Your account is fine.'),
 ]),
 C=dict(head='Write *who* or *that*.', items=[
  'I\'m going to call the number [that] is on my real bill.', 'The man [who] called me knew my name.', 'A company [that] asks for gift cards is a scam.',
  'Scammers are people [who] want your money.', 'Be careful with texts [that] ask for your password, too.', 'never trust a caller [who] tells you to hurry.']),
 hear='*gonna* = going to: "We\'re **gonna** turn off your power." You can say *going to*. The word *that* is short and weak: *a text that asks* ("thut"). Stress the key words: *NEVER, GIFT cards*. Say *No, thank you. Goodbye.* in a calm, firm voice.',
)
L['grammar'] = dict(boxes='''
### Grammar Box 1: describing with *who / that*

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **What's** | a scam? | ‖ | It's a trick | **that takes** your money. |
| **Who** | called you? | ‖ | A man | **who said** he was from the bank. |
| **What's** | a warning sign? | ‖ | It's something | **that tells** you to be careful. |

### Grammar Box 2: what to do

<!-- subst -->
| QUESTION | < | ‖ | ANSWER | < |
|---|---|---|---|---|
| **What about** | a text that wants my PIN? | ‖ | **Don't answer** texts | **that ask** for your PIN. |
| **What about** | a caller who wants gift cards? | ‖ | **Hang up** on a caller | **who asks** for gift cards. |
| **Who** | can I trust? | ‖ | Call the company | at the number **that is** on your card. |
''',
rule='*who* for people; *that* for things (and also people). The *who / that* part tells you **which** person or thing. Don\'t add *he / it* after it: ***a man who called*** (not *a man who he called*).',
explain='''
### Grammar Box 3: *anyone, something, must, should*

| WORDS | EXAMPLE |
|---|---|
| *Never… anyone* | *Never give your PIN to anyone.* |
| *If something…* | *If something sounds too good to be true, it probably is.* |
| *mustn't / should* | *You mustn't share your password. You should tell someone you trust.* |

### Grammar Box 4: 4 steps

| STEP | WHAT TO DO |
|---|---|
| **Stop.** | Don't answer or click right away. |
| **Don't pay.** | Never pay with gift cards. |
| **Check.** | Call the number on your real bill or card. |
| **Tell someone.** | Talk to a family member or friend you trust. |
''',
qa=[('*who* or *that*?', '*who* for people, *that* for things. *that* is OK for people too: ***a man who called / a text that came***.'),
 ('*a man who he called* or *a man who called*?', '***a man who called.*** Don\'t add *he* or *it* after *who / that*.'),
 ('Are all calls and texts scams?', 'No. ***Most calls and texts are real. A few are scams. Stop, check, and ask.***')],
A=dict(head='Write one word.', items=['A scam is a trick [that] takes your money.', 'Don\'t trust a caller [who] asks for gift cards.',
 'Be careful with links [that] look strange.', 'Never give your PIN to [anyone].', 'If [something] sounds too good to be true, it probably is.',
 'You [mustn\'t] share your password. (must / mustn\'t)']),
B=dict(head='Circle the correct words.', items=['I got a text {{*that|who}} said I won a prize.', 'The woman {{*who|what}} called was from my bank.',
 'A man {{*who called|who he called}} asked for my PIN.', 'Don\'t click on links {{*that|who}} look strange.', 'You {{*should|shouldn\'t}} tell someone you trust.',
 '{{*Hang up|Hang on}} if the caller is pushy.']),
mistakes=[('the man who he called', 'the man who called'), ('a text who said', 'a text **that** said'),
 ('Never give your PIN to nobody.', 'Never give your PIN to **anyone**.'), ('Don\'t trust a caller asks for money.', 'Don\'t trust a caller **who** asks for money.'),
 ('You must to call the bank.', 'You **must call** the bank.')],
tip='Spanish uses *que* for people and things: *el hombre que llamó, el mensaje que llegó.* English uses *who* (or *that*) for people and *that* for things: *the man who called, the message that came.* Many languages repeat the pronoun (*the man who he called*); English doesn\'t. What do you say in your language?')
L['talk'] = dict(pages=[('Real or Scam?', '''
### Round 1. Work with a partner. Read the 10 invented messages. Is each one probably real or probably a scam? Say why with *It's a text that… / It's from someone who…*

| MESSAGE CARDS (invented) | |
|---|---|
| **1. Text:** Your package is late. Click this link and pay $2.99 today. | **2. Email:** Hi, this is your son's school. Parent conferences are on May 3. |
| **3. Call:** You won a free trip! Just pay $100 for taxes. | **4. Text:** Your bank account is locked. Send your PIN to unlock it. |
| **5. Text:** Reminder: your dentist appointment is Friday at 10:00. Reply C to confirm. | **6. Call:** This is the electric company. Pay with gift cards in one hour. |
| **7. Email:** Your library book is due tomorrow. | **8. Text:** Hi Grandma, it's me. I lost my phone. Send money now and don't tell Mom. |
| **9. Call:** This is the pharmacy. Your prescription is ready. | **10. Email:** You got the job! Send $50 for training. |

*Example:* "Card 1 is probably a scam. It's a text that has a strange link, and it wants money today."

| Probably real (numbers) | Probably a scam (numbers) | One reason |
|---|---|---|
| | | |
'''), ('Safe Answer', '''
### Round 2. Work with a partner. A is the caller: read a card in a pushy but polite voice. B gives a safe answer. Then switch.

| CALLER CARDS (invented) |
|---|
| **1.** "Hello, I'm from your bank. There's a problem with your account. Please tell me your PIN." |
| **2.** "Congratulations! You won a $1,000 prize! I just need your address and $50 for shipping." |
| **3.** "This is the water company. Pay today with gift cards, or we'll shut off your water." |

| SAFE ANSWERS (choose one or two) |
|---|
| "I don't give information on the phone." |
| "I'll call the number on my card." |
| "No, thank you. Goodbye." (Then hang up.) |

| Card | The warning sign (*It's a caller who…*) | My safe answer |
|---|---|---|
| | | |
| | | |

*Remember:* a calm, firm voice. You don't need to explain. You can hang up.
''')])
L['hw'] = dict(one=dict(head='Write the sentence. Use *who* or *that*.', example='a scam / a trick / take your money (that) → *A scam is a trick that takes your money.*',
 items=[('don\'t trust / a caller / ask for gift cards (who)', 'Don\'t trust a caller who asks for gift cards.'), ('be careful with / texts / ask for your password (that)', 'Be careful with texts that ask for your password.'),
  ('never / give / your PIN / anyone', 'Never give your PIN to anyone.'), ('a warning sign / something / tell you to be careful (that)', 'A warning sign is something that tells you to be careful.')]),
 three='''### 3. Write 3 warning signs of a scam. What should you do?

| Warning sign (*a caller who… / a text that…*) | What to do |
|---|---|
| 1. | |
| 2. | |
| 3. | |
''',
 four=dict(head='Review (Lesson 11). Write one word.', items=['I\'m going to the store [to] buy milk.', 'I enjoy [traveling] by bus. (travel)',
  'We decided [to] leave on Friday.', 'Don\'t forget [to] pack your charger.', 'Would you mind [covering] my shift? (cover)']))
L['rw'] = dict(kind='notice', note='Read fast first. Then read again and answer the questions.', box_title='RIVERSIDE COMMUNITY OFFICE · A flyer + a sample text (invented)',
 text='''
**SMART CONSUMER TIPS.** Most calls, texts, and emails are real. But some are scams: tricks that take your money or your information. Here are 5 warning signs. 1. Someone says you must pay today, or something bad will happen. 2. A caller wants you to pay with gift cards. Real companies don't take gift cards for bills. 3. A message says you won a prize, but you must pay to get it. 4. A text has a strange link and asks for your password or PIN. 5. Someone tells you, "Don't tell anyone." What should you do? Stop: don't answer or click right away. Don't pay. Check: call the company at the number that is on your real bill or card. Tell someone you trust. You can also block the number.

**SAMPLE TEXT (a scam).** "ALERT! Your bank card is locked. Click the link and enter your PIN in 30 minutes, or you will lose your money."
''',
 qs=[('Are most calls and texts scams?', 'No. Most are real.', 'Most calls, texts, and emails are real.'),
  ('Do real companies take gift cards for bills?', 'No, they don\'t.', 'Real companies don\'t take gift cards for bills.'),
  ('What is the first step?', 'Stop. Don\'t answer or click right away.', 'Stop: don\'t answer or click right away'),
  ('Which number should you call to check?', 'The number on your real bill or card.', 'the number that is on your real bill or card'),
  ('What are two warning signs in the sample text?', 'It asks for your PIN, and it says you must hurry (30 minutes).', 'enter your PIN in 30 minutes')],
 write_head='Write a message (5–8 sentences) to a family member about a scam text. Use *who* or *that* and *Don\'t…*.',
 write_short='your message',
 example='*Hi Mom, I want to tell you about a scam. Some people get texts that say their bank card is locked. The texts ask for your PIN. Don\'t click on the link, and don\'t answer. If you aren\'t sure, call the number that is on your bank card. Also, never trust a caller who asks for gift cards. Love, Ana*',
 box_label='My message', checklist=['It has 5–8 sentences.', 'It has *who* or *that*.', 'It has *Don\'t…*.', 'It says what to do.'])
L['exit'] = dict(q='What is one warning sign of a scam, and what should you do?', s1='a warning sign, with *who* or *that*', s2='what to do',
 s3='a reason, with *because*', key='*A good answer:* "A caller who asks for gift cards is a warning sign. You should hang up and call the real company. Don\'t pay, because real companies don\'t take gift cards."')
L['game'] = ('Who or that?', 'A points to a picture and asks, "What\'s a **fake prize**?" B answers with *who / that*: "It\'s a message **that** says you won, but you must pay." Switch.')
L['opening'] = dict(cards=['**A:** Where would you like to go on a trip?', '**A:** What do you enjoy doing on the weekend?', '**A:** Why do people take time off?', '**A:** What do you need to pack for a short trip?'],
 follow='Why? • What do you enjoy doing there?', hw_head='Write your partner\'s name and their trip from Homework item 3.', hw_cols=['My partner\'s name', 'Their trip (where and why)'])
L['notes'] = [
 '**Keep it calm and practical:** "Most calls and texts are real. A few are scams. Stop, check, and ask." No scary stories.',
 '**Never ask learners whether they lost money** or got a scam call. Learners can share if they want to.',
 '**All messages are invented,** with no real numbers or links. List a local consumer-help line on the "Keep practicing" sheet (check it locally first).',
 '**Teacher-only:** if a learner asks about "legal help" or "immigration help" services that ask for money, point only to local legal aid. Don\'t give advice yourself.',
 '**Listening:** in the scope, a real utility agent confirms the account. To keep 3 speakers, Daniel checks the account on the company website instead. The message is the same: no money is lost.',
 '**Spanish and other languages:** the contrast tip on the Grammar page is optional. Learners read it on their own. You never need to read, translate, or explain it.',
 '**Reductions:** the listening has *gonna*. Learners need to understand it; they can always say *going to*.']
