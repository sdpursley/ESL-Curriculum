"""Level 4 Lesson 4 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs and marks)."""
import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from l4img import *
I = [
 ('checkup', 'checkup', ['1fa7a', '1f4cb'], 'CHECKUP', None, 'a stethoscope and a clipboard [sign: CHECKUP]'),
 ('health_history', 'health history', ['1f4cb', '1f58a'], 'HEALTH HISTORY', None, 'a clipboard and a pen [sign: HEALTH HISTORY]'),
 ('symptom', 'symptom', ['1f912', '1f927'], 'SYMPTOMS', None, 'a person with a fever and a person sneezing [sign: SYMPTOMS]'),
 ('allergy', 'allergy', ['1f95c', '1f927'], 'ALLERGY: PEANUTS', None, 'peanuts and a person sneezing [sign: ALLERGY: PEANUTS]'),
 ('blood_pressure', 'blood pressure', ['1fa7a', '1f4aa'], '120/80', None, 'a stethoscope and an arm [sign: 120/80]'),
 ('rash', 'rash', ['1f91a'], 'RASH', None, 'a hand [sign: RASH]'),
 ('dizzy', 'dizzy', ['1f635-200d-1f4ab'], None, None, 'a dizzy face'),
 ('teeth_cleaning', 'teeth cleaning', ['1f9b7', '1faa5'], 'CLEANING', None, 'a tooth and a toothbrush [sign: CLEANING]'),
 ('cavity', 'cavity', ['1f9b7', '1f50d'], 'CAVITY', None, 'a tooth and a magnifying glass [sign: CAVITY]'),
 ('flu_shot', 'flu shot', ['1f489'], 'FLU SHOT', None, 'a syringe [sign: FLU SHOT]'),
 ('prescription', 'prescription', ['1f48a', '1f4c4'], 'Rx', None, 'pills and a paper [sign: Rx]'),
 ('copay', 'copay', ['1f4b3', '1f4b5'], 'COPAY $20', None, 'a card and money [sign: COPAY $20]'),
]
vocab_run(4, '/workspace/level4_curriculum/lesson4/images', I)
