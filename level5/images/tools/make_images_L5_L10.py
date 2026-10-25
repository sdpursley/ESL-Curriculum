"""Level 5 Lesson 10 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from l5img import vocab_run
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
I = [
 ('compromise', 'compromise', ['1f91d'], 'COMPROMISE', None, 'a handshake [sign: COMPROMISE]'),
 ('offer', 'offer', ['1f4ac', '1f381'], 'OFFER', None, 'a speech balloon and a gift [sign: OFFER]'),
 ('counteroffer', 'counteroffer', ['1f504', '1f4ac'], 'COUNTEROFFER', None, 'swap arrows and a speech balloon [sign: COUNTEROFFER]'),
 ('priority', 'priority', ['2b50'], 'PRIORITY', None, 'a star [sign: PRIORITY]'),
 ('shared_task', 'shared task', ['1f465', '1f4cb'], 'SHARED TASK', None, 'two people and a clipboard [sign: SHARED TASK]'),
 ('solution', 'solution', ['1f4a1'], 'SOLUTION', None, 'a light bulb [sign: SOLUTION]'),
 ('fairness', 'fairness', ['2696'], 'FAIR', None, 'a balance scale [sign: FAIR]'),
 ('sticky_note', 'sticky note', ['1f4dd', '1f4cc'], 'NOTE', None, 'a memo and a pushpin [sign: NOTE]'),
 ('break_time', 'break time', ['2615', '23f0'], 'BREAK', None, 'a coffee cup and an alarm clock [sign: BREAK]'),
 ('swap', 'swap', ['1f504'], 'SWAP', None, 'swap arrows [sign: SWAP]'),
 ('whiteboard', 'whiteboard', ['1f4ca', '1f58a'], None, None, 'a chart and a pen'),
 ('middle', 'middle', ['2b05', '2b50', '27a1'], None, None, 'a left arrow, a star, and a right arrow'),
]
vocab_run(10, OUT, I)
