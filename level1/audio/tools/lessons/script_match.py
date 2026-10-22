"""Check that the listening script in LessonN.md matches script_L1_LN.py. Usage: python script_match.py lesson.md script.py"""
import sys, re, importlib.util
spec = importlib.util.spec_from_file_location('S', sys.argv[2]); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
md = open(sys.argv[1]).read(); sec = md[md.index('### Listening script'):md.index('### Answer key')]
got = [(m.group(1), re.sub(r'\s*\*\([^)]*\)\*', '', m.group(2)).strip()) for m in re.finditer(r'^> \*\*([^*]+):\*\* (.+)$', sec, re.M) if m.group(1) != 'Audio']
want = [('Narrator', S.INTRO if isinstance(S.INTRO, str) else ' '.join(S.INTRO))] + [(l[0], l[1]) for l in S.LINES] + [('Narrator', S.END)]
bad = [(i, g, w) for i, (g, w) in enumerate(zip(got, want)) if g != w]
print('lines md', len(got), 'script', len(want), 'mismatches', len(bad))
for b in bad: print(' ', b)
