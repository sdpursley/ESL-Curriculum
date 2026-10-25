"""Level 5 Lesson 7 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5img
if not os.path.exists(l5img.F):
    l5img.F = os.path.expanduser('~/.local/share/fonts/DejaVuSans-Bold.ttf')
from l5img import *
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
I = [
 ('spelling', 'spelling', ['1f524', '270f'], 'A B C', None, 'latin letters and a pencil [sign: A B C]'),
 ('email_address', 'email address', ['1f4e7'], 'EMAIL', None, 'an e-mail icon [sign: EMAIL]'),
 ('phone_number', 'phone number', ['1f4f1'], 'PHONE', None, 'a mobile phone [sign: PHONE]'),
 ('schedule', 'schedule', ['1f4c5', '23f0'], 'TUE 6:00', None, 'a calendar and an alarm clock [sign: TUE 6:00]'),
 ('signature', 'signature', ['270d'], 'SIGN HERE', None, 'a writing hand [sign: SIGN HERE]'),
 ('form', 'form', ['1f4cb'], 'FORM', None, 'a clipboard [sign: FORM]'),
 ('checkbox', 'checkbox', ['2611'], 'YES', None, 'a ballot box with a check [sign: YES]'),
 ('correction', 'correction', ['270f', '274c'], 'FIX', None, 'a pencil and a cross mark [sign: FIX]'),
 ('double_check', 'double-check', ['2705', '2705'], 'AGAIN', None, 'two check marks [sign: AGAIN]'),
 ('copy', 'copy', ['1f4c4', '1f4c4'], 'COPY', None, 'two pages [sign: COPY]'),
 ('initial', 'initial', ['270d', '1f4dd'], 'L.P.', None, 'a writing hand and a memo [sign: L.P.]'),
 ('capital_letter', 'capital letter', ['1f520'], 'ABC', None, 'a capital-letters key [sign: ABC]'),
]
vocab_run(7, OUT, I)
