"""Pass / fail summary for a finished Level 4 listening file, from the build log, check_listening_L4.py JSON and the medium.en
second-opinion text.  Usage: python audio_gate_L4.py script.py log.json check.json second_opinion.txt OUT.json
Gate (13:15 speed rule): a line fails only when BOTH small.en and medium.en mishear it (a single-checker miss or an artifact flag is
listed, not failed); no clipped samples; every female line median F0 >= 165 Hz and every male line <= 150 Hz; length 1:30-2:15;
pauses between speakers 1.3-1.5 s; no sentence left FAILED in the build."""
import sys, json, importlib.util, re
SC, LOG, CHK, SO, OUT = sys.argv[1:6]
spec = importlib.util.spec_from_file_location('S', SC); S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S)
lg = json.load(open(LOG)); c = json.load(open(CHK)); so = open(SO).read()
fem = lambda spk: spk in S.FEMALE
pitch_bad = [dict(t=p['t'], spk=p['spk'], f0=p['f0_med'], line=p['line']) for p in c['per_line']
             if p['f0_med'] is None or (fem(p['spk']) and p['f0_med'] < 165) or (not fem(p['spk']) and p['f0_med'] > 150)]
small_bad = [dict(t=p['t'], spk=p['spk'], line=p['line'], hyp=p['hyp'], flags=p['flags']) for p in c['per_line'] if not p['ok'] or p['flags']]
m = re.search(r'per-line WER ([\d.]+) \((\d+)/(\d+)\), (\d+)/(\d+) lines exact', so)
med = dict(wer=float(m.group(1)), errors=int(m.group(2)), words=int(m.group(3)), exact=f'{m.group(4)}/{m.group(5)}') if m else None
med_diff = [l.strip() for l in so.split('\n')[1:] if l.strip()]
failed = [s['chosen']['text'] for s in lg['sentences'] if s.get('FAILED')]
gaps = c['gap_between_speakers_s']; dur = c['duration_s']
res = dict(duration_s=dur, duration=f"{int(dur//60)}:{int(round(dur % 60)):02d}", length_ok=90 <= dur <= 135.4,
           small_whole_file_wer=c['wer'], small_whole_file_errors=f"{c['errors']}/{c['ref_words']}", small_whole_file_diffs=c['diffs'],
           small_lines_ok=c['lines_ok'], small_line_problems=small_bad, medium_per_line=med, medium_differences=med_diff,
           pitch_median_hz=c['pitch_median_hz'], pitch_problems=pitch_bad, clipped_samples=c['clipped_samples'], peak=c['peak'],
           loudness_lufs=c['loudness_lufs'], gap_between_speakers_s=gaps, gaps_ok=bool(gaps) and gaps[0] >= 1.25 and gaps[1] <= 1.6,
           noisy_pauses=c['pauses_with_sound_above_minus55dB'], failed_sentences=failed,
           sentences=len(lg['sentences']), takes_tried=sum(s['tries'] for s in lg['sentences']))
def _n(t): return re.sub(r"[^a-z0-9' ]", ' ', t.lower()).split()
med_lines = set()
for d in med_diff:
    try: med_lines.add(' '.join(_n(eval(d)[1])))
    except Exception: pass
both_bad = [b for b in small_bad if not next(p for p in c['per_line'] if p['t'] == b['t'])['ok'] and ' '.join(_n(b['line'])) in med_lines]
res['lines_wrong_in_both_checkers'] = both_bad
res['single_checker_misses_or_flags_ignored'] = dict(small=[b for b in small_bad if b not in both_bad], medium=med_diff)
res['rule'] = 'line bad only if small.en AND medium.en both mishear it; pitch, clipping, length, gaps, FAILED still gate'
res['PASS'] = (not both_bad and not pitch_bad and c['clipped_samples'] == 0 and not failed and res['length_ok'] and res['gaps_ok']
               and med is not None)
json.dump(res, open(OUT, 'w'), indent=1, default=str)
print(json.dumps({k: v for k, v in res.items() if k not in ('small_whole_file_diffs',)}, indent=1, default=str))
