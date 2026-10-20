"""Download Ana's voice reference clip (LibriTTS-R speaker 1580, CC BY 4.0) and make refs/Ana_LTTSR1580.wav.
Run with the audio environment:  ../../../../.venv-audio/bin/python fetch_ana_ref.py
The WAV is not committed (.gitignore skips *.wav under level1/); this script recreates the same file (sha256 is checked)."""
import os, io, json, hashlib, urllib.request, numpy as np, soundfile as sf, librosa
HERE = os.path.dirname(os.path.abspath(__file__)); meta = json.load(open(f'{HERE}/ana_ref.json'))
u = (f"https://datasets-server.huggingface.co/rows?dataset={meta['hf_dataset']}&config={meta['hf_config']}"
     f"&split={meta['hf_split']}&offset={meta['hf_row_index']}&length=1")
row = json.load(urllib.request.urlopen(u, timeout=60))['rows'][0]['row']
assert row['id'] == meta['utterance_id'], f"row {meta['hf_row_index']} is {row['id']}, expected {meta['utterance_id']}"
a, sr = sf.read(io.BytesIO(urllib.request.urlopen(row['audio'][0]['src'], timeout=120).read()), dtype='float32')
if a.ndim > 1: a = a.mean(1)
if sr != 24000: a = librosa.resample(a, orig_sr=sr, target_sr=24000)
a = (a / (np.abs(a).max() + 1e-9) * 0.9).astype(np.float32)
os.makedirs(f'{HERE}/refs', exist_ok=True); out = f"{HERE}/refs/{meta['name']}.wav"; sf.write(out, a, 24000)
h = hashlib.sha256(open(out, 'rb').read()).hexdigest()
print(out, round(len(a)/24000, 1), 's', 'sha256 OK' if h == meta['sha256_of_processed_wav'] else f'sha256 differs ({h}); the clip is still the same recording')
