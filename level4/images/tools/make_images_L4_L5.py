"""Level 4 Lesson 5 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs and marks)."""
import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from l4img import *
I = [
 ('favor', 'favor', ['1f64b', '1f91d'], 'A FAVOR?', None, 'a person raising a hand and a handshake [sign: A FAVOR?]'),
 ('borrow', 'borrow', ['1fa9c'], 'BORROW', None, 'a ladder [sign: BORROW]'),
 ('water_the_plants', 'water the plants', ['1fab4', '1f4a7'], None, None, 'a plant and a drop of water'),
 ('feed_the_cat', 'feed the cat', ['1f408', '1f963'], None, None, 'a cat and a bowl'),
 ('get_the_mail', 'get the mail', ['1f4ec', '2709'], None, None, 'a mailbox and a letter'),
 ('spare_key', 'spare key', ['1f511', '1f511'], 'SPARE', None, 'two keys [sign: SPARE]'),
 ('package', 'package', ['1f4e6'], None, None, 'a package'),
 ('switch_shifts', 'switch shifts', ['1f4c5', '1f504'], 'SAT → SUN', None, 'a calendar and arrows [sign: SAT → SUN]'),
 ('cover_a_shift', 'cover a shift', ['1f64b', '1f550'], 'COVER: SAT', None, 'a person raising a hand and a clock [sign: COVER: SAT]'),
 ('be_away', 'be away', ['1f9f3', '2708'], None, None, 'a suitcase and a plane'),
 ('owe', 'owe (someone)', ['1f91d'], 'I OWE YOU ONE', None, 'a handshake [sign: I OWE YOU ONE]'),
 ('thank_you_note', 'thank-you note', ['1f4dd', '1f490'], 'THANK YOU!', None, 'a note and flowers [sign: THANK YOU!]'),
]
vocab_run(5, '/workspace/level4_curriculum/lesson5/images', I)
