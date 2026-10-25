"""Level 5 Lesson 13 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from l5img import vocab_run
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
I = [
 ('outline', 'outline', ['1f4cb', '1f4dd'], 'OUTLINE', None, 'a clipboard and a memo [sign: OUTLINE]'),
 ('notecard', 'notecard', ['1f4c7'], 'NOTECARD', None, 'an index card [sign: NOTECARD]'),
 ('pause', 'pause', ['23f8'], 'PAUSE', None, 'a pause button [sign: PAUSE]'),
 ('eye_contact', 'eye contact', ['1f440'], 'LOOK UP', None, 'a pair of eyes [sign: LOOK UP]'),
 ('introduction', 'introduction', ['1f44b'], 'HELLO', None, 'a waving hand [sign: HELLO]'),
 ('example', 'example', ['1f4a1'], 'EXAMPLE', None, 'a light bulb [sign: EXAMPLE]'),
 ('conclusion', 'conclusion', ['1f3c1'], 'THE END', None, 'a checkered flag [sign: THE END]'),
 ('mentor', 'mentor', ['1f9d1', '1f4ac'], 'MENTOR', None, 'a person and a speech balloon [sign: MENTOR]'),
 ('applause', 'applause', ['1f44f'], 'APPLAUSE', None, 'clapping hands [sign: APPLAUSE]'),
 ('community_center', 'community center', ['1f3eb', '1f465'], 'CENTER', None, 'a school building and two people [sign: CENTER]'),
 ('achievement', 'achievement', ['1f3c6'], None, None, 'a trophy'),
 ('stopwatch', 'stopwatch', ['23f1'], None, None, 'a stopwatch'),
]
vocab_run(13, OUT, I)
