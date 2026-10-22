"""Print the parts of a lesson's Markdown that belong on the slides, in order (the teacher-facing parts that never go on
slides are left out), so you can write or check a deck spec against the lesson page line by line.
Usage: python3 scripts/slides/lesson_outline.py <LevelV_LessonN.md> [--full]
--full prints the listening script speaker lines too (they go in the Before You Listen notes when audio is not ready)."""
import re, sys
path = sys.argv[1]; full = '--full' in sys.argv
L = open(path, encoding='utf-8').read().split('\n')
out = []; skip_level = 0; inscript = False
SKIP_H = ('## How to Use', '### Clock-time plan', '### Questions and answers', '· My Words', '· Read & Write', '### Baseline',
          '## Task Words', '### How this lesson', '### What Lesson', '## Picture Credits', ':::box Materials')
for l in L:
    m = re.match(r'^(#+) ', l)
    if m:
        lvl = len(m.group(1))
        if skip_level and lvl <= skip_level: skip_level = 0
        if not skip_level and any(k in l for k in SKIP_H): skip_level = lvl
        inscript = l.startswith('### Listening script')
    if skip_level: continue
    if inscript and not full and l.startswith('> **') and not l.startswith('> **Narrator'): continue
    if l.strip() in ('', '---') or l.startswith('Name: ___') or re.search(r'_{12,}\s*$', l) or l.startswith('<!--') or '<br>' in l: continue
    if l.startswith('- **Grouping:**') or l.startswith('- **Late arrivals'): continue
    out.append(l)
s = '\n'.join(out)
print(s[s.index('> **Topic'):] if '> **Topic' in s else s)
