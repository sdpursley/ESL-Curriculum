import re
ONES="zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS="_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def n2w(n):
    n=int(n)
    if n<20: return ONES[n]
    if n<100: return TENS[n//10]+("" if n%10==0 else " "+ONES[n%10])
    return str(n)
def words(s):
    s=s.lower().replace("’","'").replace("-"," ")
    s=re.sub(r"\b(\d{1,2})[:.](\d\d)\b",lambda m:m.group(1)+" "+m.group(2),s)
    s=re.sub(r"\b([1-9])([0-5]\d)\b",lambda m:m.group(1)+" "+m.group(2),s)  # 530 -> 5 30 (times)
    s=re.sub(r"(\d+):(\d+)",lambda m:m.group(1)+" "+m.group(2),s)
    s=re.sub(r"\d+",lambda m:" "+n2w(m.group())+" ",s)
    s=re.sub(r"\bo'clock\b","",s)
    return ["okay" if w == "ok" else w for w in re.sub(r"[^a-z' ]"," ",s).split()]   # Whisper writes OK as "okay"
