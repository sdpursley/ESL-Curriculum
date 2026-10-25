"""Level 4 Lesson 11 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from l4img import *
I = [
 ('time_off', 'time off', ['1f4c5', '1f334'], 'DAY OFF', None, 'a calendar and a palm tree [sign: DAY OFF]'),
 ('vacation_days', 'vacation days', ['1f3d6', '1f4c5'], None, None, 'a beach with an umbrella and a calendar'),
 ('request_form', 'request form', ['1f4dd'], 'REQUEST', None, 'a paper and a pencil [sign: REQUEST]'),
 ('approve', 'approve', ['1f9d1-200d-1f4bc', '2705'], None, None, 'an office worker and a check mark'),
 ('pack', 'pack', ['1f455', '1f9f3'], None, None, 'a shirt and a suitcase'),
 ('suitcase', 'suitcase', ['1f9f3'], None, None, 'a suitcase'),
 ('carry_on', 'carry-on bag', ['1f392', '2708'], None, None, 'a backpack and an airplane'),
 ('round_trip', 'round-trip ticket', ['1f3ab', '1f501'], None, None, 'a ticket and a repeat arrow'),
 ('boarding_pass', 'boarding pass', ['1f3ab', '2708'], 'GATE 12', None, 'a ticket and an airplane [sign: GATE 12]'),
 ('toiletries', 'toiletries', ['1faa5', '1f9f4'], None, None, 'a toothbrush and a lotion bottle'),
 ('voicemail', 'voicemail', ['1f4f1', '1f5e3'], None, None, 'a phone and a speaking head'),
 ('itinerary', 'itinerary', ['1f5fa', '1f4cb'], 'FRI 8:00 AM', None, 'a map and a clipboard [sign: FRI 8:00 AM]'),
]
vocab_run(11, '/workspace/level4_curriculum/lesson11/images', I)
