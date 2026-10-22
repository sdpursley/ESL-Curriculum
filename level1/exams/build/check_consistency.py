"""Check that the student tests, the answer keys, and the listening scripts agree, and that the house rules hold.
Usage: python3 check_consistency.py [EXAMS_DIR]   Exit code 1 if any check fails. Writes build/consistency_report.txt."""
import os, re, sys, json, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
sys.path.insert(0, os.path.abspath(os.path.join(HERE, '..', '..', 'audio', 'tools', 'lessons')))   # canon.py of the shared Level 1 audio tools
import exam_data as D
from canon import canon
X = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(HERE, '..'))
fails, notes = [], []
def ok(c, msg):
    (notes if c else fails).append(('OK   ' if c else 'FAIL ') + msg)
def load(p):
    spec = importlib.util.spec_from_file_location('S', p); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S); return S
ORD = {'12': 'twelfth'}
def norm_ans(a, same):
    a = a.replace(' + ', ' ')
    if re.fullmatch(r'[A-Z]{3,}', a): return list(a.lower())                      # spelled name: L I M A
    t = canon(a, same)
    return ['i' if w == 'she' else w for w in t]
def contains(seq, sub):
    return any(seq[i:i+len(sub)] == sub for i in range(len(seq)-len(sub)+1))
ALLOWED_IN_AUDIO = {('Final', 'a taco'), ('Final', 'school')}     # distractors that are heard on purpose (Carlos offers a taco; the restaurant is across from the school)
for E in D.EXAMS:
    k = E['key']; S = load(os.path.join(HERE, 'audio', E['script'])); same = getattr(S, 'SAME', {})
    full = [S.INTRO] + [l[1] for l in S.LINES] + [S.END]; fullc = canon(' '.join(full), same)
    stu = open(os.path.join(X, f'Level1_{k}_Student_Test.md')).read(); pk = open(os.path.join(X, f'Level1_{k}_Exam_Teacher_Packet.md')).read()
    # 1 packet script == audio script
    sec = pk[pk.index('### Listening script'):pk.index('### Answer key')]
    got = [(m.group(1), m.group(2).strip()) for m in re.finditer(r'^> \*\*([^*]+):\*\* (.+)$', sec, re.M) if m.group(1) != 'Audio']
    want = [('Narrator', S.INTRO)] + [(l[0], l[1]) for l in S.LINES] + [('Narrator', S.END)]
    ok(got == want, f'{k}: packet listening script = {E["script"]} ({len(got)} lines)')
    # 2 each listening item: evidence is in the audio, answer is in the evidence, wrong options are not heard
    for i, (stem, kind, opts, ans, les, ev) in enumerate(E['listening'], 1):
        evc = canon(ev, same)
        ok(contains(fullc, evc), f'{k} A{i}: evidence "{ev}" is in the audio script')
        a = norm_ans(ans, same)
        if ans == '12' and 'May' in (opts or []): a = ['twelfth']
        if ans.startswith('No,'): a = ["can't"]
        ok(all(w in evc for w in a), f'{k} A{i}: answer "{ans}" is in the evidence')
        if kind in ('pic', 'text', 'text2'):
            names = [(' '.join(o) if kind == 'text2' else (o[0] if isinstance(o, tuple) else o)) for o in opts]
            ok(sum(1 for n in names if n.replace(' ', ' + ') == ans or n == ans) == 1 or (kind == 'text2' and ' + '.join(ans.split(' + ')) in [' + '.join(o) for o in opts]), f'{k} A{i}: exactly one option is the key')
            for n in names:
                if n == ans or n.replace(' ', ' + ') == ans or n == ans.replace(' + ', ' '): continue
                heard = contains(fullc, norm_ans(n, same))
                if (k, n) in ALLOWED_IN_AUDIO: ok(heard, f'{k} A{i}: distractor "{n}" is heard on purpose (allowed)')
                else: ok(not heard, f'{k} A{i}: distractor "{n}" is NOT in the audio')
            for n in names:
                for part in n.split(' '):
                    if part not in stu: ok(False, f'{k} A{i}: option text "{part}" missing from student test')
        ok(stem in stu, f'{k} A{i}: stem on the student test')
    # 3 words, grammar on the student test; key in the packet
    for i, (pic, ch, ans, les) in enumerate(E['words'], 1):
        ok(f'images/{pic}.png' in stu and all(f'^^{c}' in stu for c in ch) and ans in ch, f'{k} B{i}: picture + choices on test, key "{ans}" is a choice')
        ok(os.path.exists(os.path.join(X, 'images', pic + '.png')), f'{k} B{i}: picture file exists')
    for i, (sent, ch, ans, les) in enumerate(E['grammar'], 1):
        ok(f'{i}. {sent}' in stu and f'**{ch[0]}**' in stu and f'**{ch[1]}**' in stu and ans in ch and ch.count(ans) == 1, f'{k} C{i}: "{sent}" on test, key "{ans}" is one of the choices')
    # one-page key table in the packet matches the data
    kp = pk[pk.index('Answer Key (Teacher)'):]
    for i, it in enumerate(E['listening'], 1): ok(f'| {i} | {it[3]} |' in kp, f'{k} key page A{i} = {it[3]}')
    for i, g in enumerate(E['grammar'], 1): ok(f'{i} | {g[2]} |' in kp, f'{k} key page C{i} = {g[2]}')
    for i, w in enumerate(E['words'], 1): ok(f'{i} | {w[2]} |' in kp, f'{k} key page B{i} = {w[2]}')
    for lab, val in E['form']['fields']: ok(f'{lab}: **{val}**' in kp and f'**{lab}**' in stu, f'{k} D: "{lab}" on the form, key "{val}"')
    # form key = card (card values come from make_exam_images.py)
    img_src = open(os.path.join(HERE, 'images', 'make_exam_images.py')).read()
    for lab, val in E['form']['fields']: ok(f"'{val}'" in img_src or val in img_src, f'{k} D: key "{val}" is printed on the practice card')
    # 4 points
    tot = len(E['listening']) + len(E['words']) + len(E['grammar']) + 6
    ok(f'Total ____ /{tot}' in stu and f'= **/{tot}**' in pk, f'{k}: total {tot} points on test and in packet')
    # 5 house rules on the student test
    blocks = [m.start() for m in re.finditer(r'^### ', stu, re.M)]
    for b in blocks:
        chunk = stu[b:b+600].split('\n')
        ok(chunk[2].startswith('*Español:') and chunk[4].startswith('My language: ___'), f'{k}: instruction "{chunk[0][4:50]}…" has a Spanish line and a My language line')
    pk_student = re.findall(r'<!-- mode: student -->(.*?)(?=<!-- mode:|\Z)', pk, re.S)
    for chunk in pk_student:
        for m in re.finditer(r'^### (.*)$', chunk, re.M):
            nxt = chunk[m.end():m.end()+400].split('\n')
            ok(nxt[2].startswith('*Español:') and nxt[4].startswith('My language: ___'), f'{k} packet learner page: "{m.group(1)[:45]}…" has Spanish + My language')
    for name, txt in (('student test', stu), ('packet', pk)):
        low = txt.lower()
        for bad in [w.strip().lower() for w in os.environ.get('BANNED_EXTRA', '').split(',') if w.strip()] + ['secular', 'draft for review', 'church', 'god', 'pray', 'bible', 'christmas', 'easter', 'ramadan', 'religio', 'registered', 'copyright registration']:
            ok(not re.search(r'\b' + re.escape(bad), low), f'{k} {name}: no "{bad}"')
        emo = [c for c in txt if ord(c) >= 0x1F000 or 0x2600 <= ord(c) <= 0x27BF and c not in '✓✗☐']
        ok(not emo, f'{k} {name}: no emoji characters {sorted(set(emo))}')
        ok('© 2026 the authors' in txt or name == 'student test', f'{k} {name}: © 2026 the authors')
    ok('cover' not in stu.lower() and '<!-- part:' not in stu, f'{k}: student test has no cover page')
    # 6 audio check results (if the audio is done)
    cj = os.path.join(X, 'audio', E['audio'].replace('_listening.mp3', '_check_results.json'))
    if os.path.exists(cj):
        ok(os.path.exists(os.path.join(X, 'audio', E['audio'])), f'{k} audio: {E["audio"]} exists')
        ok(os.path.exists(os.path.join(X, 'audio', f'README_L1_{k}.md')), f'{k} audio: README exists')
        c = json.load(open(cj)); n_ok, n_all = map(int, c['lines_ok'].split('/'))
        ok(c['clipped_samples'] == 0, f'{k} audio: no clipped samples')
        ok(60 <= c['duration_s'] <= 95, f'{k} audio: length {c["duration_s"]} s (target about 1:00–1:30)')
        notes.append(f'INFO {k} audio: WER {c["wer"]}, lines {c["lines_ok"]}, pitch {c["pitch_median_hz"]}')
    else: notes.append(f'INFO {k} audio: not built yet')
rep = '\n'.join(fails + notes) + f'\n\n{len(fails)} failed, {len(notes)} ok/info\n'
open(os.path.join(HERE, 'consistency_report.txt'), 'w').write(rep)
print('\n'.join(fails) or 'all checks passed', f'({len(notes)} ok/info, {len(fails)} failed)')
sys.exit(1 if fails else 0)
