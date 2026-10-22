"""Level 4 Lesson 1 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs and marks)."""
import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from l4img import *
I = [
 ('try_food', 'try (a new food)', ['1f9d1', '1f363'], 'NEW!', None, 'a person and sushi [sign: NEW!]'),
 ('travel', 'travel', ['1f9f3', '1f5fa'], None, None, 'a suitcase and a map'),
 ('fly', 'fly', ['2708'], None, None, 'an airplane'),
 ('snow', 'snow', ['2603', '2744'], None, None, 'a snowman and a snowflake'),
 ('ocean', 'ocean', ['1f30a'], None, None, 'an ocean wave'),
 ('mountain', 'mountain', ['1f3d4'], None, None, 'a snowy mountain'),
 ('desert', 'desert', ['1f3dc', '1f335'], None, None, 'a desert and a cactus'),
 ('win_prize', 'win a prize', ['1f3c6'], '1st PRIZE', None, 'a trophy [sign: 1st PRIZE]'),
 ('ride_horse', 'ride a horse', ['1f3c7'], None, None, 'a person riding a horse'),
 ('run_race', 'run a race', ['1f3c3', '1f3c5'], '5K', None, 'a runner and a medal [sign: 5K]'),
 ('camping', 'go camping', ['1f3d5'], None, None, 'a tent at a campsite'),
 ('famous', 'see a famous person', ['1f9d1-200d-1f3a4', '1f4f7'], 'FAMOUS!', None, 'a singer and a camera [sign: FAMOUS!]'),
]
vocab_run(1, '/workspace/level4_curriculum/lesson1/images', I)
