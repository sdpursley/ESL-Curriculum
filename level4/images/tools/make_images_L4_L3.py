"""Level 4 Lesson 3 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs and marks)."""
import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from l4img import *
I = [
 ('to_do_list', 'to-do list', ['1f4dd'], 'TO DO', None, 'a note and a pencil [sign: TO DO]'),
 ('task', 'task', ['1f9f9', '1f9fd'], 'TASK: CLEAN', None, 'a broom and a sponge [sign: TASK: CLEAN]'),
 ('checklist', 'checklist', ['1f4cb'], None, 'check', 'a clipboard with a check mark'),
 ('supervisor', 'supervisor', ['1f469-200d-1f4bc'], 'SUPERVISOR', None, 'a woman at work [sign: SUPERVISOR]'),
 ('deadline', 'deadline', ['1f4c5', '23f0'], 'DUE: FRIDAY', None, 'a calendar and an alarm clock [sign: DUE: FRIDAY]'),
 ('restock', 'restock', ['1f6d2', '1f96b'], 'RESTOCK', None, 'a shopping cart and cans [sign: RESTOCK]'),
 ('inventory', 'inventory', ['1f4e6', '1f522'], 'INVENTORY', None, 'a box and numbers [sign: INVENTORY]'),
 ('clock_in', 'clock in', ['1f558', '27a1'], 'IN 9:00', None, 'a clock and an arrow [sign: IN 9:00]'),
 ('clock_out', 'clock out', ['1f554', '2b05'], 'OUT 5:00', None, 'a clock and an arrow [sign: OUT 5:00]'),
 ('break_room', 'break room', ['2615', '1fa91'], 'BREAK ROOM', None, 'coffee and a chair [sign: BREAK ROOM]'),
 ('feedback', 'feedback', ['1f44d', '1f4ac'], 'GOOD JOB!', None, 'a thumbs-up and a speech bubble [sign: GOOD JOB!]'),
 ('check_in', 'check-in (a short meeting)', ['1f469-200d-1f4bc', '1f4ac', '1f9d1'], None, None, 'a supervisor and a worker talking'),
]
vocab_run(3, '/workspace/level4_curriculum/lesson3/images', I)
