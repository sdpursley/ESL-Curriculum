"""Level 4 Lesson 9 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs and marks)."""
import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from l4img import *
I = [
 ('opinion', 'opinion', ['1f9d1', '1f4ac'], 'I THINK…', None, 'a person and a speech bubble [sign: I THINK…]'),
 ('agree', 'agree', ['1f9d1', '1f44d'], None, None, 'a person and a thumbs-up'),
 ('disagree', 'disagree', ['1f9d1', '1f44e'], None, None, 'a person and a thumbs-down'),
 ('point', 'point (I see your point)', ['1f440', '1f4a1'], None, None, 'eyes and a light bulb'),
 ('community_meeting', 'community meeting', ['1f9d1-200d-1f91d-200d-1f9d1', '1fa91'], 'MEETING 7 PM', None, 'two people holding hands and a chair [sign: MEETING 7 PM]'),
 ('empty_lot', 'empty lot', ['1f6a7', '1f33e'], 'EMPTY LOT', None, 'a barrier and tall grass [sign: EMPTY LOT]'),
 ('community_garden', 'community garden', ['1f33b', '1f955'], None, None, 'a sunflower and a carrot'),
 ('parking_lot', 'parking lot', ['1f17f', '1f697'], None, None, 'a parking sign and a car'),
 ('playground', 'playground', ['1f6dd', '1f9d2'], None, None, 'a playground slide and a child'),
 ('survey', 'survey', ['1f4cb', '270f'], 'SURVEY', None, 'a clipboard and a pencil [sign: SURVEY]'),
 ('vote', 'vote (raise your hand)', ['1f64b', '270b'], None, None, 'a person raising a hand and a raised hand'),
 ('advantage', 'advantage / disadvantage', ['2795', '2796'], None, None, 'a plus sign and a minus sign'),
]
vocab_run(9, '/workspace/level4_curriculum/lesson9/images', I)
