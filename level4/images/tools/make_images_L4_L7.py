"""Level 4 Lesson 7 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs and marks)."""
import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from l4img import *
I = [
 ('on_time', 'on time', ['23f0', '2705'], '7:00', None, 'an alarm clock and a check mark [sign: 7:00]'),
 ('early', 'early', ['1f305', '23f0'], '6:50', None, 'a sunrise and an alarm clock [sign: 6:50]'),
 ('late', 'late', ['1f3c3', '23f0'], '7:20', None, 'a person running and an alarm clock [sign: 7:20]'),
 ('dress_code', 'dress code', ['1f4cb', '1f454'], 'DRESS CODE', None, 'a clipboard and a shirt with a tie [sign: DRESS CODE]'),
 ('uniform', 'uniform', ['1f9ba', '1f9e2'], 'UNIFORM', None, 'a safety vest and a cap [sign: UNIFORM]'),
 ('casual', 'casual', ['1f455', '1f456'], None, None, 'a T-shirt and jeans'),
 ('formal', 'formal', ['1f454', '1f45e'], None, None, 'a shirt with a tie and dress shoes'),
 ('closed_toe_shoes', 'closed-toe shoes', ['1f45f', '2705'], 'CLOSED-TOE', None, 'a sneaker and a check mark [sign: CLOSED-TOE]'),
 ('name_badge', 'name badge', ['1f4db'], 'HI, I\'M NADIA', None, 'a name badge [sign: HI, I\'M NADIA]'),
 ('invitation', 'invitation', ['2709', '1f389'], 'PARTY SAT 7:00', None, 'an envelope and a party popper [sign: PARTY SAT 7:00]'),
 ('rsvp', 'RSVP', ['1f4f1', '2705'], 'RSVP BY FRI', None, 'a phone and a check mark [sign: RSVP BY FRI]'),
 ('host', 'host', ['1f9d1', '1f3e0'], 'HOST', None, 'a person and a house [sign: HOST]'),
]
vocab_run(7, '/workspace/level4_curriculum/lesson7/images', I)
