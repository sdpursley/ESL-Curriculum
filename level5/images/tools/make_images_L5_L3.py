"""Level 5 Lesson 3 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5img
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = [
 ('wish', 'wish', ['1f31f'], 'I WISH', None, 'a glowing star [sign: I WISH]'),
 ('regret', 'regret', ['1f614'], 'REGRET', None, 'a pensive face [sign: REGRET]'),
 ('calendar', 'calendar', ['1f4c5'], 'DATE', None, 'a calendar [sign: DATE]'),
 ('reminder', 'reminder', ['1f4cc', '1f4dd'], 'REMINDER', None, 'a pushpin and a memo [sign: REMINDER]'),
 ('alarm', 'alarm', ['23f0'], 'ALARM', None, 'an alarm clock [sign: ALARM]'),
 ('signup', 'sign-up sheet', ['1f4cb', '270d'], 'SIGN-UP', None, 'a clipboard and a writing hand [sign: SIGN-UP]'),
 ('tutor', 'tutor', ['1f9d1-200d-1f3eb'], 'TUTOR', None, 'a teacher [sign: TUTOR]'),
 ('practice', 'practice', ['1f4dd', '270f'], 'PRACTICE', None, 'a memo and a pencil [sign: PRACTICE]'),
 ('question', 'question', ['2753'], 'QUESTION', None, 'a question mark [sign: QUESTION]'),
 ('choice', 'choice', ['2b05', '27a1'], 'A OR B', None, 'a left arrow and a right arrow [sign: A OR B]'),
 ('help_desk', 'help desk', ['1f9d1', '1f4de'], 'HELP DESK', None, 'a person and a phone [sign: HELP DESK]'),
 ('next_time', 'next time', ['1f4c5', '27a1'], 'NEXT TIME', None, 'a calendar and a right arrow [sign: NEXT TIME]'),
]
l5img.vocab_run(3, OUT, ITEMS)
