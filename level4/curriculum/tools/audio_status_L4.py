"""Write the AUDIO_STATUS.md table rows (all lessons to-do)."""
import re, os, sys
S = '/workspace/level4_curriculum'; R = sys.argv[1]
sc = open(f'{S}/Level4_Scope_and_Sequence.md').read()
head = open(f'{R}/AUDIO_STATUS.md').read().split('| Lesson | Title |')[0]
rows = ['| Lesson | Title | Script | Cast | Audio |', '|---|---|---|---|---|']
for n, t in re.findall(r'^### Lesson (\d+) \(Week \d+\): (.+)$', sc, re.M):
    ok = os.path.exists(f'{R}/audio/tools/scripts/script_L4_L{n}.py')
    rows.append(f'| {n} | {t} | {"`scripts/script_L4_L%s.py`" % n if ok else "to write"} | {"`cast/cast_L4_L%s.json`" % n if ok else "to write"} | to do |')
open(f'{R}/AUDIO_STATUS.md', 'w').write(head + '\n'.join(rows) + '\n')
