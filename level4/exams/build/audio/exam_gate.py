"""Re-check the lesson gate result against the exam's own length window (SETTINGS['LENGTH_S'] in the exam script).
The lesson gate (audio_gate_L<V>.py) uses the lesson window; every other rule (both-checker misses, pitch, clipping,
failed sentences, gaps, medium.en present) stays exactly as the lesson gate decided it.
Usage: exam_gate.py script_L<V>_<K>.py <K gate.json>   (rewrites the gate JSON; prints PASS)"""
import json, sys, importlib.util
spec = importlib.util.spec_from_file_location('S', sys.argv[1]); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
g = json.load(open(sys.argv[2])); lo, hi = S.SETTINGS['LENGTH_S']; d = g['duration_s']
lesson_ok = g['length_ok']; g['lesson_length_ok'] = lesson_ok
g['length_ok'] = lo <= d <= hi + 0.4; g['length_window_s'] = [lo, hi]
others = (not g['lines_wrong_in_both_checkers'] and not g['pitch_problems'] and g['clipped_samples'] == 0   # same rule as audio_gate
          and not g['failed_sentences'] and g['gaps_ok'] and g['medium_per_line'] is not None)
g['PASS'] = bool(others and g['length_ok'])
g['rule'] += f'; exam length window {lo}-{hi} s (exam_gate.py)'
json.dump(g, open(sys.argv[2], 'w'), indent=1, default=str)
print('duration', g['duration'], '| PASS', g['PASS'], '| both-checker misses', len(g['lines_wrong_in_both_checkers']), '| pitch problems',
      len(g['pitch_problems']), '| clipped', g['clipped_samples'], '| failed sentences', len(g['failed_sentences']), '| gaps', g['gaps_ok'],
      f'| length {d:.1f} s in {lo}-{hi}: {g["length_ok"]}')
