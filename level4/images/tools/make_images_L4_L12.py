"""Level 4 Lesson 12 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from l4img import *
I = [
 ('scam', 'scam', ['1f3a3', '1f4b8'], None, None, 'a fishing pole and flying money'),
 ('warning_sign', 'warning sign', ['26a0'], None, None, 'a warning triangle'),
 ('suspicious', 'suspicious', ['1f914', '1f4f1'], None, None, 'a thinking face and a phone'),
 ('fake', 'fake', ['1f4b5', '274c'], 'FAKE', None, 'a dollar bill and a red X [sign: FAKE]'),
 ('official', 'official', ['1f3db', '2705'], None, None, 'an official building and a check mark'),
 ('gift_card', 'gift card', ['1f381', '1f4b3'], None, None, 'a gift and a card'),
 ('prize', 'prize', ['1f3c6', '1f389'], None, None, 'a trophy and a party popper'),
 ('link', 'link', ['1f4f1', '1f517'], None, None, 'a phone and a link'),
 ('pin', 'PIN', ['1f4b3', '1f522'], None, None, 'a card and numbers'),
 ('hang_up', 'hang up', ['1f4de', '1f44b'], None, None, 'a phone and a waving hand'),
 ('block', 'block (a number)', ['1f4f1', '1f6ab'], None, None, 'a phone and a no sign'),
 ('trust', 'trust', ['1f91d', '2705'], None, None, 'a handshake and a check mark'),
]
vocab_run(12, '/workspace/level4_curriculum/lesson12/images', I)
