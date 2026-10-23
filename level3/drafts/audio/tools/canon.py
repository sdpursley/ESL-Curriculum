"""Canonical word list for comparing a script line with Whisper output: lower case, no punctuation,
number words and digits turned into one digit string (five five five oh one four two = 555-0142 = 5550142)."""
import re
N = {'zero': '0', 'oh': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
     'ten': '10', 'eleven': '11', 'twelve': '12', 'thirteen': '13', 'fourteen': '14', 'fifteen': '15', 'sixteen': '16', 'seventeen': '17',
     'eighteen': '18', 'nineteen': '19', 'twenty': '20', 'thirty': '30', 'forty': '40', 'fifty': '50', 'sixty': '60', 'seventy': '70',
     'eighty': '80', 'ninety': '90'}
TENS = {'20', '30', '40', '50', '60', '70', '80', '90'}
def canon(s, same=None):
    same = same or {}
    s = s.lower().replace('’', "'")
    s = re.sub(r'\s+', ' ', s)                                   # Whisper word pieces already include a space, so a join leaves two
    s = re.sub(r"\bco[- ](worker|workers)\b", r"co\1", s)        # Level 3: Whisper writes co-workers / co workers
    s = re.sub(r"\$(\d+)(?:\.00)?\b", r"\1 dollars", s)               # $12 -> 12 dollars (same as "twelve dollars")
    s = re.sub(r"\b(\d{1,2}):00\b", r"\1 o'clock", s)                # 7:00 -> 7 o'clock
    s = re.sub(r"\b(\d{1,2}):(\d\d)\b", r"\1 \2", s)                 # 6:30 -> 6 30 (same as "six thirty")
    s = s.replace("o 'clock", 'oclock').replace("o'clock", 'oclock').replace('o clock', 'oclock')
    # ordinals: Whisper often writes 10th / 5th while the script has tenth / fifth
    import re as _re
    _ord = {'1st':'first','2nd':'second','3rd':'third','4th':'fourth','5th':'fifth','6th':'sixth','7th':'seventh','8th':'eighth','9th':'ninth','10th':'tenth','11th':'eleventh','12th':'twelfth','13th':'thirteenth','14th':'fourteenth','15th':'fifteenth','16th':'sixteenth','17th':'seventeenth','18th':'eighteenth','19th':'nineteenth','20th':'twentieth','21st':'twenty first','22nd':'twenty second','23rd':'twenty third','24th':'twenty fourth','25th':'twenty fifth','26th':'twenty sixth','27th':'twenty seventh','28th':'twenty eighth','29th':'twenty ninth','30th':'thirtieth','31st':'thirty first'}
    s = _re.sub(r'\b(\d+)(st|nd|rd|th)\b', lambda m: _ord.get(m.group(0), m.group(0)), s)

    s = re.sub(r"\b(\d+) ?(a\.? ?m\.?|p\.? ?m\.?)", r"\1", s)
    s = re.sub(r"(?<=\d)[-.,\s]+(?=\d)", '', s)            # 555-0142 / 555 0142 -> 5550142
    s = re.sub(r"[^a-z0-9' ]", ' ', s.replace('-', ' '))
    toks = ' '.join(same.get(t, t) for t in s.split()).split()   # a SAME value may be two words (saferoad -> safe road)
    out = []; i = 0
    while i < len(toks):
        t = toks[i]
        # 'oh' is a number only next to another number
        isnum = t.isdigit() or (t in N and t != 'oh') or (t == 'oh' and ((i+1 < len(toks) and (toks[i+1] in N or toks[i+1].isdigit())) or (out and out[-1].isdigit() and i > 0 and (toks[i-1] in N or toks[i-1].isdigit()))))
        if isnum:
            v = t if t.isdigit() else N[t]
            # twenty one -> 21
            if v in TENS and i+1 < len(toks) and toks[i+1] in N and N[toks[i+1]] in '123456789' and len(N[toks[i+1]]) == 1 and toks[i+1] != 'oh':
                v = v[0] + N[toks[i+1]]; i += 1
            if out and out[-1].isdigit() and (i > 0 and (toks[i-1] in N or toks[i-1].isdigit() or v)):
                out[-1] += v
            else: out.append(v)
        else: out.append(t)
        i += 1
    return out
if __name__ == '__main__':
    for x in ["It's $12.", "It's twelve dollars.", "It's 6:30.", "It's six thirty.", "at seven o'clock", "at 7:00", "at 7 o'clock", "It's five five five, oh one four two.", "It's 555-0142.", "Oh, nice!", "He's twelve.", "He's 12.", "two ten Pine Street", "210 Pine Street", "twenty-one", "ZIP code is 6 0 6 1 4"]:
        print(x, canon(x))
