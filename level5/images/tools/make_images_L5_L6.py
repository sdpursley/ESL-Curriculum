"""Level 5 Lesson 6 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs and marks)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from l5img import *
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
I = [
 ('message', 'message', ['1f4ac'], 'MESSAGE', None, 'a speech balloon [sign: MESSAGE]'),
 ('note', 'note', ['1f4dd'], 'NOTE', None, 'a memo and a pencil [sign: NOTE]'),
 ('callback', 'callback', ['1f4de'], 'CALL BACK', None, 'a telephone [sign: CALL BACK]'),
 ('nurse', 'nurse', ['1f9d1-200d-2695-fe0f'], 'NURSE', None, 'a health worker with a stethoscope [sign: NURSE]'),
 ('clinic', 'clinic', ['1f3e5'], 'CLINIC', None, 'a hospital building with a cross on it [sign: CLINIC]'),
 ('folder', 'folder', ['1f4c1'], 'FOLDER', None, 'a file folder [sign: FOLDER]'),
 ('detail', 'detail', ['1f50d', '1f4dd'], 'DETAIL', None, 'a magnifying glass and a memo with a pencil [sign: DETAIL]'),
 ('time_change', 'time change', ['1f553', '1f504'], 'NEW TIME', None, 'a clock and circular arrows [sign: NEW TIME]'),
 ('family_member', 'family member', ['1f46a'], 'FAMILY', None, 'a family [sign: FAMILY]'),
 ('relay', 'relay', ['1f4ac', '27a1'], 'PASS IT ON', None, 'a speech balloon and a right arrow [sign: PASS IT ON]'),
 ('phone_log', 'phone log', ['1f4de', '1f4cb'], 'PHONE LOG', None, 'a telephone and a clipboard [sign: PHONE LOG]'),
 ('waiting_room', 'waiting room', ['1f6cb', '1f552'], 'PLEASE WAIT', None, 'a couch with a lamp and a clock [sign: PLEASE WAIT]'),
]
vocab_run(6, OUT, I)
