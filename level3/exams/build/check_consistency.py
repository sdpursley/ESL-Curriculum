"""Check that the student tests, the teacher packets (answer keys), the listening scripts and casts agree, and that the house rules hold.
Usage: python3 check_consistency.py [EXAMS_DIR]   Exit code 1 if any check fails. Writes build/consistency_report.txt.
The same file is in level3/, level4/ and level5/exams/build/; level differences are in exam_data.py (LEVEL, CFG)."""
import os, re, sys, json, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import exam_data as D
import make_exam_md as G
V = D.LEVEL; C = D.CFG
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
TOOLS = os.path.join(REPO, 'level3', 'drafts', 'audio', 'tools') if V == 3 else os.path.join(REPO, f'level{V}', 'audio', 'tools')
sys.path.insert(0, TOOLS)
from canon import canon
X = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.abspath(os.path.join(HERE, '..'))
FEMALE_REFS = {'N', 'Rosa', 'Kim', 'Receptionist', 'Ana_af_jessica', 'Ana_af_bella'}
refs_md = open(os.path.join(TOOLS, f'REFS_L{V}.md')).read()
fails, notes = [], []
def ok(c, msg): (notes if c else fails).append(('OK   ' if c else 'FAIL ') + msg)
def load(p):
    spec = importlib.util.spec_from_file_location('S', p); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S); return S
def contains(seq, sub): return bool(sub) and any(seq[i:i + len(sub)] == sub for i in range(len(seq) - len(sub) + 1))
STOP = {'a', 'an', 'the', 'it', 's', 'and', 'to', 'at', 'in', 'on', 'of', 'her', 'his', 'he', 'she', 'was', 'is'}
def check_items(k, part, its, body, same, stu, src_name):
    bodyc = canon(body, same)
    for i, t in enumerate(its, 1):
        tag = f'{k} {part}{i}'
        evc = canon(t['ev'], same)
        ok(contains(bodyc, evc), f'{tag}: evidence "{t["ev"][:60]}" is in the {src_name}')
        if t['kind'] == 'tf':
            ok(t['ans'] in ('True', 'False'), f'{tag}: true/false key is True or False')
        else:
            keys = t['keys'] or [w for w in canon(t['ans'], same) if w not in STOP] or canon(t['ans'], same)
            keys = [w for k2 in keys for w in canon(k2, same)]
            ok(all(w in evc for w in keys), f'{tag}: answer "{t["ans"]}" ({" ".join(keys)}) is in the evidence')
        if t['kind'] == 'mc':
            ok(len(t['opts']) == 3 and t['opts'].count(t['ans']) == 1, f'{tag}: 3 options, exactly one is the key')
            if part == 'A':
                for o in t['opts']:
                    if o == t['ans']: continue
                    heard = contains(bodyc, canon(o, same))
                    if o in t['heard']: ok(heard, f'{tag}: wrong option "{o}" is heard on purpose (listed)')
                    else: ok(not heard, f'{tag}: wrong option "{o}" is NOT in the audio')
            line = '   ' + '      '.join(f'**{G.LET[j]}.** {o}' for j, o in enumerate(t['opts']))
            ok(line in stu, f'{tag}: the options are on the student test')
        if t['kind'] == 'write': ok('______' in t['q'] and len(t['ans'].split()) == 1, f'{tag}: write-one-word item has a blank and a one-word key')
        ok(f'{i}. {G.stem(t)}' in stu, f'{tag}: stem on the student test')
for E in D.EXAMS:
    k = E['key']
    stu = open(os.path.join(X, f'Level{V}_{k}_Student_Test.md')).read(); pk = open(os.path.join(X, f'Level{V}_{k}_Exam_Teacher_Packet.md')).read()
    S = load(os.path.join(HERE, 'audio', E['script'])) if 'script' in E else load(os.path.join(HERE, 'audio', f'script_L{V}_{k}.py'))
    cast = json.load(open(os.path.join(HERE, 'audio', 'cast', f'cast_L{V}_{k}.json')))
    same = getattr(S, 'SAME', {})
    # 1 script file == data == packet; cast == script
    want = [('Narrator', S.INTRO)] + [(l[0], l[1]) for l in S.LINES] + [('Narrator', S.END)]
    ok([(l[0], l[1]) for l in S.LINES] == [(l[0], l[1]) for l in E['lines']] and S.INTRO == E['intro'], f'{k}: script_L{V}_{k}.py = exam_data.py')
    sec = pk[pk.index('### Listening script'):pk.index('### Answer key')]
    got = [(m.group(1), m.group(2).strip()) for m in re.finditer(r'^> \*\*([^*]+):\*\* (.+)$', sec, re.M)]
    ok(got == want, f'{k}: packet listening script = {E["audio"].replace("_listening.mp3", "")} script ({len(got)} lines)')
    ok(cast['VOICES'] == S.VOICES and set(cast['FEMALE']) == S.FEMALE, f'{k}: cast JSON = script voices')
    for l in S.LINES:
        if len(l) > 2 and not re.search(r'\d', l[1]): ok(canon(l[1], same) == canon(l[2], same), f'{k}: TTS text says the same words as the line "{l[1][:40]}"')
    # 2 voices and speakers
    spk = G.speakers(E)
    ok(all(s in S.VOICES for s in spk + ['Narrator']), f'{k}: every speaker has a voice')
    for s, ref in S.VOICES.items():
        ok((s in S.FEMALE) == (ref in FEMALE_REFS), f'{k}: {s} ({"female" if s in S.FEMALE else "male"}) uses {ref} ({"female" if ref in FEMALE_REFS else "male"} voice)')
        ok(f'`{ref}.wav`' in refs_md, f'{k}: voice {ref} is one of the Level {V} reference clips')
    scenes, cur = [], set()
    for l in E['lines']:
        if l[0] == 'Narrator' and cur: scenes.append(cur); cur = set()
        elif l[0] != 'Narrator': cur.add(l[0])
    scenes.append(cur)
    ok(all(len(sc) <= 3 for sc in scenes) and len(spk) <= C['max_speakers'], f'{k}: speakers {spk} (max {C["max_speakers"]} in all, 3 per scene)')
    est = G.est_seconds(E); lo, hi = C['length_s']
    ok(lo <= est <= hi, f'{k}: listening estimate {est} s ({G.mmss(est)}) in {lo}-{hi} s ({C["length_target"]})')
    alltxt = ' '.join([S.INTRO, S.END] + [l[1] for l in S.LINES]).lower()
    ok(not re.search(r"\b(gonna|wanna|gotta)\b", alltxt), f'{k}: no gonna/wanna in the script')
    # 3 listening + reading items
    check_items(k, 'A', E['listening'], ' '.join(x[1] for x in want), same, stu, 'audio script')
    R = E['reading']; rtxt = ' '.join(R['text'])
    check_items(k, 'D', R['items'], rtxt, {}, stu, 'reading text')
    nw = G.words_in(rtxt); lo, hi = C['reading_range']
    ok(lo <= nw <= hi, f'{k} D: reading text {nw} words (target {lo}-{hi})')
    for para in R['text']: ok(f'> {para}' in stu, f'{k} D: reading paragraph on the student test')
    # 4 words, grammar, fix
    W = E['words']; box = W['box']; answers = [x[1] for x in W['items']]
    ok(len(set(answers)) == len(answers) and all(a in box for a in answers) and len(box) == len(answers) + 2, f'{k} B: {len(answers)} keys, all different, all in a box of {len(box)}')
    for w in box: ok(f'**{w}**' in stu, f'{k} B: box word "{w}" on the test')
    for i, (s, a, les) in enumerate(W['items'], 1):
        ok(f'{i}. {s}' in stu and s.count('______') == 1, f'{k} B{i}: sentence with one blank on the test')
        ok(canon(s.replace('______', a), {}) != canon(s, {}), f'{k} B{i}: key fills the blank')
    for i, (s, ch, a, les) in enumerate(E['grammar'], 1):
        ok(f'{i}. {s} ( **{ch[0]}** / **{ch[1]}** )' in stu and ch.count(a) == 1 and s.count('______') == 1, f'{k} C{i}: "{s[:40]}" on the test; key "{a}" is one of the two choices')
    nG = len(E['grammar'])
    for i, f in enumerate(E['fix'], nG + 1):
        ok(f'{i}. {f["wrong"]}' in stu, f'{k} C{i}: sentence with a mistake on the test')
        ok(f['mistake'] in f['wrong'] and f['mistake'] not in f['right'].replace(f['mistake'] + 's', '') or f['mistake'] in ('my',), f'{k} C{i}: the mistake "{f["mistake"]}" is in the test sentence and fixed in the key')
        ok(f['right'] != f['wrong'], f'{k} C{i}: key differs from the test sentence')
    # 5 one-page key = data
    kp = pk[pk.index('### Answer Key (Teacher)'):]
    rows = {}
    for m in re.finditer(r'^\| (\d+) \| (.*?) \| (.*?) \| (.*?) \|$', kp, re.M): rows.setdefault(int(m.group(1)), []).append([m.group(2), m.group(3), m.group(4)])
    for i, t in enumerate(E['listening'], 1): ok(rows[i][0][0] == G.key_text(t), f'{k} key page A{i} = {G.key_text(t)}')
    for i, x in enumerate(W['items'], 1): ok(rows[i][0][1] == x[1], f'{k} key page B{i} = {x[1]}')
    for i, t in enumerate(R['items'], 1): ok(rows[i][0][2] == G.key_text(t), f'{k} key page D{i} = {G.key_text(t)}')
    gk = re.findall(r'^\| (\d+) \| (.*?) \| (\d*) ?\| (.*?) \|$', kp[kp.index('C. Grammar'):], re.M)
    cmap = {}
    for a, b, c, d in gk:
        cmap[int(a)] = b
        if c: cmap[int(c)] = d
    allc = [g[2] for g in E['grammar']] + [f['right'] for f in E['fix']]
    for i, a in enumerate(allc, 1): ok(cmap.get(i) == a, f'{k} key page C{i} = {a}')
    # full answer key section = data
    ak = pk[pk.index('### Answer key'):pk.index('### Where the answers are in the audio')]
    for i, t in enumerate(E['listening'], 1): ok(f'- {i}. {G.key_text(t)}' in ak, f'{k} answer key A{i}')
    for i, t in enumerate(R['items'], 1): ok(f'- {i}. {G.key_text(t)}' in ak.split('**D. Reading')[1], f'{k} answer key D{i}')
    # 6 points
    P = G.points(E); tot = G.total(E)
    ok(tot == 50 and f'Total ____ /{tot}' in stu and f'= **/{tot}**' in pk and f'| **Written total** | | **{tot}** |' in pk, f'{k}: total {tot} points on the test and in the packet')
    for part, n in P.items(): ok(f'### {part}. ' in stu and f'({n} points)' in stu, f'{k}: part {part} shows {n} points')
    # 7 writing models
    lo, hi = C['writing_sent_range']
    for j, m in enumerate(E['writing']['models'], 1):
        n = G.sentences_in(m); ok(lo <= n <= hi, f'{k} E: model answer {j} has {n} sentences ({lo}-{hi})')
    # 8 house rules
    for name, txt in (('student test', stu), ('packet', pk), ('script', open(os.path.join(HERE, 'audio', f'script_L{V}_{k}.py')).read())):
        low = txt.lower()
        for bad in [w.strip().lower() for w in os.environ.get('BANNED_EXTRA', '').split(',') if w.strip()] + [
                'secular', 'draft for review', 'intercambio', 'church', 'god', 'pray', 'bible', 'christmas', 'easter', 'ramadan', 'religio',
                'español', 'my language', 'gonna', 'wanna', 'coming soon']:
            ok(not re.search(r'\b' + re.escape(bad), low), f'{k} {name}: no "{bad}"')
        emo = [c for c in txt if ord(c) >= 0x1F000 or (0x2600 <= ord(c) <= 0x27BF and c not in '✓✗☐★')]
        ok(not emo, f'{k} {name}: no emoji {sorted(set(emo))}')
    ok('© 2026 the authors, CC BY-NC-SA 4.0' in pk, f'{k} packet: © 2026 the authors, CC BY-NC-SA 4.0')
    ok(not re.search(r'cover (page|sheet)|^#+ .*cover', stu, re.I | re.M) and '<!-- part:' not in stu and '![' not in stu, f'{k}: student test has no cover page and no pictures')
    ok('(proposed)' in pk and 'proposed' in pk.split('## Scoring Guide')[1], f'{k}: score bands are marked proposed')
    # 9 audio check results (when the audio is done)
    cj = os.path.join(X, 'audio', E['audio'].replace('_listening.mp3', '_check_results.json'))
    if os.path.exists(cj):
        ok(os.path.exists(os.path.join(X, 'audio', E['audio'])), f'{k} audio: {E["audio"]} exists')
        c = json.load(open(cj)); ok(c['clipped_samples'] == 0, f'{k} audio: no clipped samples')
        ok(C['length_s'][0] <= c['duration_s'] <= C['length_s'][1] + 0.4, f'{k} audio: length {c["duration_s"]} s')
    else: notes.append(f'INFO {k} audio: not recorded yet (estimate {G.mmss(est)})')
rep = '\n'.join(fails + notes) + f'\n\n{len(fails)} failed, {len(notes)} ok/info\n'
open(os.path.join(HERE, 'consistency_report.txt'), 'w').write(rep)
print('\n'.join(fails) or 'all checks passed', f'({len(notes)} ok/info, {len(fails)} failed)')
sys.exit(1 if fails else 0)
