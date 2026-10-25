"""Level 5 Lesson 2 pictures: 12 vocabulary cards (Twemoji, CC BY 4.0, plus drawn signs)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5img
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ITEMS = [
 ('bakery', 'bakery', ['1f956', '1f3ea'], 'BAKERY', None, 'a baguette and a shop [sign: BAKERY]'),
 ('oven', 'oven', ['1f525', '1f35e'], 'OVEN', None, 'a fire and a loaf of bread [sign: OVEN]'),
 ('permit', 'permit', ['1f4c4', '2705'], 'PERMIT', None, 'a page and a check mark [sign: PERMIT]'),
 ('inspector', 'inspector', ['1f9d1', '1f50d'], 'INSPECTOR', None, 'a person and a magnifying glass [sign: INSPECTOR]'),
 ('paint_roller', 'paint roller', ['1f3a8', '1f58c'], 'PAINT ROLLER', None, 'a palette and a paintbrush [sign: PAINT ROLLER]'),
 ('store_sign', 'store sign', ['1f3ea'], 'OPEN', None, 'a shop with a sign on the roof [sign: OPEN]'),
 ('ribbon', 'ribbon', ['1f380'], 'RIBBON', None, 'a ribbon [sign: RIBBON]'),
 ('opening_day', 'opening day', ['1f4c5', '1f389'], 'OPENING DAY', None, 'a calendar and a party popper [sign: OPENING DAY]'),
 ('counter', 'counter', ['1f9d1', '1f950'], 'COUNTER', None, 'a person and a croissant [sign: COUNTER]'),
 ('display_case', 'display case', ['1f370', '1f36a'], 'DISPLAY CASE', None, 'a cake and a cookie [sign: DISPLAY CASE]'),
 ('awning', 'awning', ['26f1', '1f3ea'], 'AWNING', None, 'a beach umbrella and a shop [sign: AWNING]'),
 ('poster', 'poster', ['1f5bc'], 'POSTER', None, 'a framed picture [sign: POSTER]'),
]
l5img.vocab_run(2, OUT, ITEMS)
