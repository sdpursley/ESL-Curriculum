"""Level 4 Lesson 8 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs and marks)."""
import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from l4img import *
I = [
 ('news', 'news', ['1f4f0', '1f4fb'], None, None, 'a newspaper and a radio'),
 ('reporter', 'reporter', ['1f9d1', '1f399'], 'NEWS', None, 'a person and a microphone [sign: NEWS]'),
 ('headline', 'headline', ['1f4f0'], 'NEW STORE OPENS', None, 'a newspaper [sign: NEW STORE OPENS]'),
 ('road_closure', 'road closure', ['1f6a7', '1f6e3'], 'ROAD CLOSED', None, 'a construction barrier and a road [sign: ROAD CLOSED]'),
 ('detour', 'detour', ['1f68c', '21aa'], 'DETOUR', None, 'a bus and a turning arrow [sign: DETOUR]'),
 ('construction', 'construction', ['1f477', '1f3d7'], None, None, 'a construction worker and a crane'),
 ('water_pipe', 'water pipe', ['1f6b0', '1f527'], None, None, 'a water tap and a wrench'),
 ('bus_route', 'bus route', ['1f68c', '1f5fa'], 'ROUTE 12', None, 'a bus and a map [sign: ROUTE 12]'),
 ('delay', 'delay', ['1f68f', '23f3'], '+15 MIN', None, 'a bus stop and an hourglass [sign: +15 MIN]'),
 ('announce', 'announce', ['1f9d1', '1f4e2'], None, None, 'a person and a loudspeaker'),
 ('update', 'update', ['1f4f1', '1f504'], 'UPDATE', None, 'a phone and refresh arrows [sign: UPDATE]'),
 ('local', 'local', ['1f3d8', '1f4cd'], None, None, 'houses and a map pin'),
]
vocab_run(8, '/workspace/level4_curriculum/lesson8/images', I)
