"""Level 4 Lesson 6 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs and marks)."""
import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from l4img import *
I = [
 ('imagine', 'imagine', ['1f9d1', '1f4ad'], None, None, 'a person and a thought bubble'),
 ('choose', 'choose', ['1f34e', '1f914', '1f34c'], None, None, 'an apple, a thinking face, and a banana'),
 ('honest', 'honest', ['1f9d1', '2705'], 'HONEST', None, 'a person and a check mark [sign: HONEST]'),
 ('tell_the_truth', 'tell the truth', ['1f5e3', '2705'], None, None, 'a person speaking and a check mark'),
 ('keep', 'keep (it)', ['1f932', '1f45b'], 'KEEP IT?', None, 'open hands and a wallet [sign: KEEP IT?]'),
 ('give_back', 'give back', ['1f932', '1f4b5'], 'GIVE IT BACK', None, 'open hands and money [sign: GIVE IT BACK]'),
 ('owner', 'owner', ['1f9d1', '1f45c'], 'OWNER', None, 'a person and a handbag [sign: OWNER]'),
 ('envelope', 'envelope', ['2709'], None, None, 'an envelope'),
 ('extra_money', 'extra money', ['1f4b5', '2795'], '+ $10', None, 'money and a plus sign [sign: + $10]'),
 ('mistake', 'mistake', ['1f9fe', '274c'], 'MISTAKE', None, 'a receipt and an X [sign: MISTAKE]'),
 ('magic_wand', 'magic wand', ['1fa84', '2728'], None, None, 'a magic wand and sparkles'),
 ('dream_job', 'dream job', ['1f4ad', '1f9d1-200d-1f373'], 'DREAM JOB', None, 'a thought bubble and a cook [sign: DREAM JOB]'),
]
vocab_run(6, '/workspace/level4_curriculum/lesson6/images', I)
