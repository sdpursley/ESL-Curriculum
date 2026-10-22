"""Rebuild the PROGRESS.md table from the checker output of every built lesson."""
import json, os, re, subprocess
S = '/workspace/level4_curriculum'; PY = '/workspace/tts/venv_l3img/bin/python'
FEM = {'N', 'Rosa', 'Ana_af_jessica', 'Kim', 'Receptionist'}
p = f'{S}/PROGRESS.md'; s = open(p).read()
head, rest = s.split('| Lesson | Title |', 1); notes = rest[rest.index('\n## Notes'):]
rows = ['| Lesson | Title | Pages | Listening (est.) | Speakers (voice clips) | Check | Pushed |', '|---|---|---|---|---|---|---|']
for n in range(1, 14):
    d = f'{S}/lesson{n}'
    if not os.path.exists(f'{d}/Level4_Lesson{n}.pdf'): continue
    j = json.loads(subprocess.run([PY, f'{S}/tools/check_lesson_L4.py', d, str(n)], capture_output=True, text=True).stdout)
    title = re.search(r'^# .*?: (.+)$', open(f'{d}/Level4_Lesson{n}.md').read(), re.M)
    title = title.group(1) if title else '?'
    sp = ', '.join(f'{c} ({v}, {"F" if v in FEM else "M"})' for c, v in j['speakers'].items())
    pushed = subprocess.run(['git', '-C', '/workspace/l3site', 'cat-file', '-e', f'origin/level4-lessons:level4/curriculum/Level4_Lesson{n}.pdf'], stderr=subprocess.DEVNULL).returncode == 0
    chk = 'pass' if not j['problems'] else 'FAIL: ' + '; '.join(j['problems'])
    rows.append(f"| {n} | {title} | {j['pdf_pages']} | {j['listening_words']} words, about {j['listening_estimate']} | {sp} | {chk} | {'yes' if pushed else 'no'} |")
open(p, 'w').write(head + '\n'.join(rows) + '\n' + notes)
print('\n'.join(rows))
