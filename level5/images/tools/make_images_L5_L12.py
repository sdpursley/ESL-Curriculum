"""Level 5 Lesson 12 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from l5img import vocab_run
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
I = [
 ('agenda', 'agenda', ['1f4cb'], 'AGENDA', None, 'a clipboard [sign: AGENDA]'),
 ('chairperson', 'chairperson', ['1f9d1', '1f4cb'], 'CHAIR', None, 'a person and a clipboard [sign: CHAIR]'),
 ('minutes', 'minutes', ['1f4d3', '1f58a'], 'MINUTES', None, 'a notebook and a pen [sign: MINUTES]'),
 ('microphone', 'microphone', ['1f3a4'], 'MIC', None, 'a microphone [sign: MIC]'),
 ('handout', 'handout', ['1f4c3'], 'HANDOUT', None, 'a page [sign: HANDOUT]'),
 ('proposal', 'proposal', ['1f4c4', '1f4a1'], 'PROPOSAL', None, 'a document and a light bulb [sign: PROPOSAL]'),
 ('sign_in', 'sign-in sheet', ['1f4dd', '270f'], 'SIGN IN', None, 'a memo and a pencil [sign: SIGN IN]'),
 ('name_tent', 'name tent', ['1f3f7'], 'NAME', None, 'a label [sign: NAME]'),
 ('timer', 'timer', ['23f2'], '4:00', None, 'a timer clock [sign: 4:00]'),
 ('question_card', 'question card', ['1f4c7', '2753'], 'QUESTION', None, 'an index card and a question mark [sign: QUESTION]'),
 ('library', 'library', ['1f4da', '1f3db'], None, None, 'books and a classical building'),
 ('auditorium', 'auditorium', ['1f3ad', '1f4e2'], None, None, 'theater masks and a loudspeaker'),
]
vocab_run(12, OUT, I)
