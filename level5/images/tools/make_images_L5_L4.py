"""Level 5 Lesson 4 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs and marks)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from l5img import *
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
I = [
 ('policy', 'policy', ['1f4dc', '1f3e2'], 'POLICY', None, 'a scroll and an office building [sign: POLICY]'),
 ('notice', 'notice', ['1f4cc', '1f4c4'], 'NOTICE', None, 'a pushpin and a page [sign: NOTICE]'),
 ('appointment', 'appointment', ['1f4c5', '1f553'], '4 PM', None, 'a calendar and a clock [sign: 4 PM]'),
 ('cancel', 'cancel', ['1f4c5'], 'CANCEL', 'cross', 'a calendar with a red cross [sign: CANCEL]'),
 ('confirm', 'confirm', ['1f4c5'], 'CONFIRMED', 'check', 'a calendar with a green check [sign: CONFIRMED]'),
 ('visitor', 'visitor', ['1f9d1', '1f6aa'], 'VISITOR', None, 'a person and a door [sign: VISITOR]'),
 ('front_desk', 'front desk', ['1f6ce', '1f3e2'], 'FRONT DESK', None, 'a desk bell and an office building [sign: FRONT DESK]'),
 ('office_hours', 'office hours', ['1f558'], '9 AM-5 PM', None, 'a clock [sign: 9 AM-5 PM]'),
 ('requirement', 'requirement', ['1f4cb'], 'REQUIRED', 'check', 'a clipboard with a green check [sign: REQUIRED]'),
 ('permission', 'permission', ['1f4c4', '1f511'], 'YOU MAY', None, 'a page and a key [sign: YOU MAY]'),
 ('exception', 'exception', ['2b50'], 'ONE TIME', None, 'a star [sign: ONE TIME]'),
 ('visitor_badge', 'visitor badge', ['1f4db'], 'VISITOR', None, 'a name badge [sign: VISITOR]'),
]
vocab_run(4, OUT, I)
