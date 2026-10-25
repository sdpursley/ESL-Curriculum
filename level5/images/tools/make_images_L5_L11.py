"""Level 5 Lesson 11 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from l5img import vocab_run
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
I = [
 ('claim_form', 'claim form', ['1f4cb', '1f4dd'], 'CLAIM', None, 'a clipboard and a memo [sign: CLAIM]'),
 ('policy_number', 'policy number', ['1f4c4'], 'POLICY NO.', None, 'a document [sign: POLICY NO.]'),
 ('photo', 'photo', ['1f4f7'], 'PHOTO', None, 'a camera [sign: PHOTO]'),
 ('estimate', 'estimate', ['1f9fe', '1f58a'], 'ESTIMATE', None, 'a receipt and a pen [sign: ESTIMATE]'),
 ('complaint', 'complaint', ['1f4e8', '1f4ac'], 'COMPLAINT', None, 'an envelope and a speech balloon [sign: COMPLAINT]'),
 ('attachment', 'attachment', ['1f4ce'], 'ATTACHMENT', None, 'a paperclip [sign: ATTACHMENT]'),
 ('reference_number', 'reference number', ['1f4c4', '1f522'], 'REF. NO.', None, 'a document and a number sign [sign: REF. NO.]'),
 ('customer_service', 'customer service', ['1f3a7', '1f4de'], 'SERVICE', None, 'headphones and a telephone [sign: SERVICE]'),
 ('on_hold', 'on hold', ['1f4de', '23f3'], 'ON HOLD', None, 'a telephone and an hourglass [sign: ON HOLD]'),
 ('resolution', 'resolution', ['2705', '1f4c4'], 'SOLVED', None, 'a check mark and a document [sign: SOLVED]'),
 ('cracked_screen', 'cracked screen', ['1f4f1', '1f4a5'], None, None, 'a mobile phone and a collision mark'),
 ('water_stain', 'water stain', ['1f4a7', '1f4c4'], None, None, 'a drop and a document'),
]
vocab_run(11, OUT, I)
