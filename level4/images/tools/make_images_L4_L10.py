"""Level 4 Lesson 10 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import sys; sys.path.insert(0, '/workspace/level4_curriculum/tools')
from l4img import *
I = [
 ('utility_bill', 'utility bill', ['1f9fe', '26a1'], 'AMOUNT DUE', None, 'a receipt and a lightning bolt [sign: AMOUNT DUE]'),
 ('electricity', 'electricity', ['26a1', '1f4a1'], None, None, 'a lightning bolt and a light bulb'),
 ('thermostat', 'thermostat', ['1f321', '1f3e0'], '68 degrees', None, 'a thermometer and a house [sign: 68 degrees]'),
 ('save_energy', 'save energy', ['1f4a1', '2705'], 'SAVE ENERGY', None, 'a light bulb and a check mark [sign: SAVE ENERGY]'),
 ('unplug', 'unplug', ['1f50c', '274c'], None, None, 'a plug and a red X'),
 ('charger', 'charger', ['1f50c', '1f4f1'], None, None, 'a plug and a phone'),
 ('outlet', 'outlet', ['1f50c'], 'OUTLET', None, 'a plug [sign: OUTLET]'),
 ('fan', 'fan', ['1f32c', '1f4a8'], 'FAN', None, 'a wind face and a puff of air [sign: FAN]'),
 ('deadbolt', 'deadbolt', ['1f512', '1f6aa'], None, None, 'a lock and a door'),
 ('peephole', 'peephole', ['1f441', '1f6aa'], None, None, 'an eye and a door'),
 ('fire_extinguisher', 'fire extinguisher', ['1f9ef'], None, None, 'a fire extinguisher'),
 ('usage', 'usage', ['1f4ca', '26a1'], 'USAGE', None, 'a bar chart and a lightning bolt [sign: USAGE]'),
]
vocab_run(10, '/workspace/level4_curriculum/lesson10/images', I)
