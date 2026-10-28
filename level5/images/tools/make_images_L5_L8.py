"""Level 5 Lesson 8 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5img
if not os.path.exists(l5img.F):
    l5img.F = os.path.expanduser('~/.local/share/fonts/DejaVuSans-Bold.ttf')
from l5img import *
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
I = [
 ('school_office', 'school office', ['1f3eb', '1f3e2'], 'OFFICE', None, 'a school and an office building [sign: OFFICE]'),
 ('counselor', 'counselor', ['1f9d1-200d-1f4bc', '1f4ac'], 'TALK', None, 'an office worker and a speech balloon [sign: TALK]'),
 ('conference', 'conference', ['1f5d3', '1f465'], 'MEET', None, 'a calendar and two people [sign: MEET]'),
 ('permission_slip', 'permission slip', ['1f4cb', '2705'], 'SLIP', None, 'a clipboard and a check mark [sign: SLIP]'),
 ('dismissal', 'dismissal', ['1f3eb', '1f6aa'], 'GO', None, 'a school and a door [sign: GO]'),
 ('pickup', 'pickup', ['1f697', '1f3eb'], 'PICKUP', None, 'a car and a school [sign: PICKUP]'),
 ('newsletter', 'newsletter', ['1f4f0'], 'NEWS', None, 'a newspaper [sign: NEWS]'),
 ('backpack', 'backpack', ['1f392'], None, None, 'a backpack'),
 ('signup', 'sign-up', ['1f4dd', '270f'], 'SIGN UP', None, 'a memo and a pencil [sign: SIGN UP]'),
 ('office_window', 'office window', ['1fa9f', '1f3e2'], 'WINDOW', None, 'a window and an office building [sign: WINDOW]'),
 ('bell', 'bell', ['1f514'], None, None, 'a bell'),
 ('hallway', 'hallway', ['1f6aa', '1f6b6'], 'HALL', None, 'a door and a person walking [sign: HALL]'),
]
vocab_run(8, OUT, I)
