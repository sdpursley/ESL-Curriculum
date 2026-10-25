"""Level 5 Lesson 9 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5img
if not os.path.exists(l5img.F):
    l5img.F = os.path.expanduser('~/.local/share/fonts/DejaVuSans-Bold.ttf')
from l5img import *
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
I = [
 ('website', 'website', ['1f310', '1f4bb'], 'WEB', None, 'a globe and a laptop [sign: WEB]'),
 ('source', 'source', ['1f4da'], 'SOURCE', None, 'a stack of books [sign: SOURCE]'),
 ('author', 'author', ['270d', '1f9d1'], 'AUTHOR', None, 'a writing hand and a person [sign: AUTHOR]'),
 ('advertisement', 'advertisement', ['1f4e3', '1f6d2'], 'AD', None, 'a megaphone and a shopping cart [sign: AD]'),
 ('screenshot', 'screenshot', ['1f4bb', '1f4f7'], 'SCREEN', None, 'a laptop and a camera [sign: SCREEN]'),
 ('fact', 'fact', ['1f4c4', '2705'], 'FACT', None, 'a page and a check mark [sign: FACT]'),
 ('rumor', 'rumor', ['1f4ac', '2753'], 'RUMOR?', None, 'a speech balloon and a question mark [sign: RUMOR?]'),
 ('date_stamp', 'date stamp', ['1f4c6'], '2019', None, 'a tear-off calendar [sign: 2019]'),
 ('logo', 'logo', ['1f3f7', '1f3e2'], 'LOGO', None, 'a label and an office building [sign: LOGO]'),
 ('comment', 'comment', ['1f4ac'], 'COMMENT', None, 'a speech balloon [sign: COMMENT]'),
 ('reliable', 'reliable', ['1f6e1', '2705'], 'SURE', None, 'a shield and a check mark [sign: SURE]'),
 ('share_button', 'share button', ['1f517', '27a1'], 'SHARE', None, 'a link and a right arrow [sign: SHARE]'),
]
vocab_run(9, OUT, I)
