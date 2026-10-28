"""Level 5 Lesson 1 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5img
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = [
 ('resume', 'résumé', ['1f4c4', '1f4bc'], 'RESUME', None, 'a page and a briefcase [sign: RESUME]'),
 ('interview', 'interview', ['1f5e3', '1f4dd'], 'INTERVIEW', None, 'a speaking head and a memo [sign: INTERVIEW]'),
 ('accomplishment', 'accomplishment', ['1f3c6'], 'I DID IT', None, 'a trophy [sign: I DID IT]'),
 ('example', 'example', ['1f4a1'], 'FOR EXAMPLE', None, 'a light bulb [sign: FOR EXAMPLE]'),
 ('skill', 'skill', ['1f527', '1f4bb'], 'SKILL', None, 'a wrench and a laptop [sign: SKILL]'),
 ('job_offer', 'job offer', ['1f4e8', '1f4bc'], 'JOB OFFER', None, 'an envelope and a briefcase [sign: JOB OFFER]'),
 ('training', 'training', ['1f393'], 'TRAINING', None, 'a graduation cap [sign: TRAINING]'),
 ('portfolio', 'portfolio', ['1f4c1', '1f5bc'], 'PORTFOLIO', None, 'a folder and a framed picture [sign: PORTFOLIO]'),
 ('handshake', 'handshake', ['1f91d'], 'HELLO', None, 'a handshake [sign: HELLO]'),
 ('follow_up', 'follow-up', ['1f4e7', '1f4de'], 'FOLLOW-UP', None, 'an envelope and a phone [sign: FOLLOW-UP]'),
 ('qualification', 'qualification', ['1f4dc'], 'QUALIFIED', None, 'a scroll [sign: QUALIFIED]'),
 ('name_tag', 'name tag', ['1f4db'], 'NAME TAG', None, 'a name badge [sign: NAME TAG]'),
]
l5img.vocab_run(1, OUT, ITEMS)
