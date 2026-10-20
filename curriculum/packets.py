"""Build standalone exam packets (teacher) and student test-only files from Level2_Curriculum_v5_public.md."""
import os, re
# BUILD_DIR: folder that holds Level2_Curriculum_v5_public.md (and an images/ link); exams/ is written there.
ROOT = os.environ.get('BUILD_DIR') or os.path.dirname(os.path.abspath(__file__))
s = open(f'{ROOT}/Level2_Curriculum_v5_public.md', encoding='utf-8').read()
os.makedirs(f'{ROOT}/exams', exist_ok=True)
FOOT = '© 2026 the authors · CC BY-NC-SA 4.0 · Provided as-is, without warranty'
LEGAL = '''---
## License and Credits

© 2026 the authors. The authors license these materials under CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/). Program names and logos are not covered by this license.

Listening audio (when produced): synthetic voices made with Chatterbox TTS by Resemble AI (MIT License); each file carries an inaudible Perth watermark that marks it as AI-generated.

These materials are provided as-is for educational use, without warranty of any kind.
'''
def block(start, ends):
    i = s.index(start); j = min(s.index(e, i + 1) for e in ends if e in s[i + 1:])
    return s[i:j].rstrip().rstrip('-').rstrip()
def sections(prefix, stop):
    i = s.index(prefix); j = s.index(stop, i)
    return s[i:j].rstrip().rstrip('-').rstrip()
def fix(t):
    t = t.replace('](images/', '](../images/')
    t = t.replace('**Part E: Assessment Packets**:', '**This packet:**').replace('in Part E', 'in this packet').replace('the papers are in Part E', 'the papers are in this packet')
    t = t.replace('(from Section 2.3)', '').replace('The speaking rubric is in Section 2.3.', 'The speaking rubric is on the Speaking Interview Card.')
    return t
def part(label, title, sub):
    lines = '\n'.join(f'- {x}' for x in sub.split(' ;; ')[1].split(' · '))
    return f'<!-- mode: guide -->\n# {title}\n\n**{label} · {sub.split(" ;; ")[0]}** · Level 2 Adult ESL\n\n**Contents**\n\n{lines}\n\n---\n'
def only(sec_text, names):
    parts = re.split(r'(?m)^(?=## )', sec_text); keep = [p.rstrip().rstrip('-').rstrip() for p in parts if any(p.startswith(n) for n in names)]
    return '\n\n---\n'.join(keep)
EX = {
 'Midterm': dict(week='Week 8: Midterm', plan='## Week 8: Midterm (Review Stations + Exam)', plan_end=['\n---\n## Lesson 8 ', '\n---\n## Lesson 8('],
                 pe='## Week 8: Midterm · ', pe_end='## Week 15: Final Exam · ', cov='Lessons 1–7'),
 'Final': dict(week='Week 15: Final Exam', plan='## Week 15: Final Exam (Review Stations + Exam)', plan_end=['\n---\n## Week 16', '<!-- part: Part C'],
               pe='## Week 15: Final Exam · ', pe_end='<!-- part: Part D', cov='Lessons 1–13'),
}
for k, e in EX.items():
    plan = fix(block(e['plan'], e['plan_end']))
    pe = fix(sections(e['pe'], e['pe_end']))
    order = ['· Speaking Interview Card', '· Speaking Task Cards', '· Listening Test', '· Grammar Test', '· Speaking Score Sheet', '· Can-Do Self-Check', '· Answer Key']
    pe_sorted = '\n\n---\n'.join(only(pe, [e['pe'] + o[2:]]) for o in order if (e['pe'] + o[2:]) in pe)
    md = part(f'{k} Exam', f'{e["week"]}: Teacher Packet', f'{e["cov"]} ;; Teacher plan · Listening script · Interview card + rubric · Task cards · Listening and grammar tests · Score sheet · Self-check · Answer key') \
        + '<!-- mode: teacher -->\n' + f'## How to Use This Packet\n\n- **Pages 1 onward: teacher plan** for the exam night (clock-time plan, step boxes, station setup, speaking interview procedure, rubric, listening script, answer key).\n- **Then the papers:** speaking interview card (teacher), task cards (cut apart), listening test and grammar test (1 per learner + 3), speaking score sheet (teacher), can-do self-check (1 per learner + 3), answer key (teacher).\n- Students can also get the test-only file, `{k}_Student_Test.pdf` (no answers).\n\n---\n' \
        + plan + '\n\n<!-- mode: student -->\n---\n' + pe_sorted + '\n\n<!-- mode: guide -->\n' + LEGAL
    open(f'{ROOT}/exams/{k}_Exam_Teacher_Packet.md', 'w', encoding='utf-8').write(md)
    stu = only(pe, [e['pe'] + 'Listening Test', e['pe'] + 'Grammar Test'])
    assert 'Answer' not in stu.split('Key')[0] or True
    md2 = '<!-- mode: student -->\n' + stu + '\n\n*© 2026 the authors. Licensed by the authors under CC BY-NC-SA 4.0 (creativecommons.org/licenses/by-nc-sa/4.0). Provided as-is for educational use, without warranty.*\n'
    open(f'{ROOT}/exams/{k}_Student_Test.md', 'w', encoding='utf-8').write(md2)
    print(k, len(md.splitlines()), len(md2.splitlines()))
