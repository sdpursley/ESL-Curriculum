"""Level 4 Lesson 2 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs and marks)."""
import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from l4img import *
I = [
 ('application', 'application', ['1f4cb', '1f58a'], 'APPLICATION', None, 'a clipboard and a pen [sign: APPLICATION]'),
 ('current_address', 'current address', ['1f3e0'], 'NOW: 418 Elm St.', None, 'a house [sign: NOW: 418 Elm St.]'),
 ('previous_address', 'previous address', ['1f3d8'], 'BEFORE: 9 Lake Rd.', None, 'houses [sign: BEFORE: 9 Lake Rd.]'),
 ('employer', 'employer', ['1f3e2', '1f9d1-200d-1f4bc'], 'EMPLOYER', None, 'an office building and a boss [sign: EMPLOYER]'),
 ('position', 'position (job title)', ['1f9d1-200d-1f527'], 'MECHANIC', None, 'a mechanic [sign: MECHANIC]'),
 ('start_date', 'start date', ['1f4c5', '27a1'], 'START: 03/15/2022', None, 'a calendar and an arrow [sign: START: 03/15/2022]'),
 ('end_date', 'end date', ['1f4c5', '1f6d1'], 'END: 05/30/2024', None, 'a calendar and a stop sign [sign: END: 05/30/2024]'),
 ('reference', 'reference (a person)', ['1f9d1-200d-1f4bc', '1f4de'], 'REFERENCE', None, 'a supervisor and a phone [sign: REFERENCE]'),
 ('for', 'for (two years)', ['23f3'], 'FOR 2 YEARS', None, 'an hourglass [sign: FOR 2 YEARS]'),
 ('since', 'since (2020)', ['1f4c5'], 'SINCE 2020', None, 'a calendar [sign: SINCE 2020]'),
 ('roommate', 'roommate', ['1f9d1', '1f3e0', '1f9d1'], None, None, 'two people and a house'),
 ('lease', 'lease', ['1f4c4', '1f511'], 'LEASE: 1 YEAR', None, 'a document and a key [sign: LEASE: 1 YEAR]'),
]
vocab_run(2, '/workspace/level4_curriculum/lesson2/images', I)
