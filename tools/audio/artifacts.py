"""Acoustic artifact detector for one synthesized chunk (mono float, sr). Returns list of flag strings + metrics."""
import re, numpy as np
def detect(a, sr, text, word_times=None):
    flags, m = [], {}
    f = int(0.02*sr); n = len(a)//f
    if n < 3: return ["empty"], m
    fr = a[:n*f].reshape(n, f)
    db = 20*np.log10(np.sqrt((fr**2).mean(1)) + 1e-9); peak = db.max(); rel = db - peak
    spec = np.abs(np.fft.rfft(fr*np.hanning(f), axis=1)) + 1e-9
    flat = np.exp(np.log(spec).mean(1)) / spec.mean(1)
    freqs = np.fft.rfftfreq(f, 1/sr)
    # 1) sustained mid-level non-speech (drone/hum/murmur/breath): >=300 ms at -18..-50 dB below peak
    mid = (rel < -18) & (rel > -50); run = best = 0
    for v in mid: run = run+1 if v else 0; best = max(best, run)
    m['mid_run_ms'] = best*20
    if best*20 >= 300: flags.append(f"sustained non-speech {best*20}ms")
    # 2) energy outside the ASR word span (>=250 ms of audible sound before first / after last word)
    if word_times:
        s0, e0 = word_times
        pre = (rel[:max(0, int((s0-0.15)/0.02))] > -40).sum()*20
        post = (rel[int((e0+0.25)/0.02):] > -40).sum()*20
        m['outside_ms'] = int(pre+post)
        if pre+post >= 250: flags.append(f"sound outside words {int(pre+post)}ms")
    # 3) clicks: isolated sample-jump spikes vs local signal level
    d = np.abs(np.diff(a)); ref = np.percentile(d, 99.5) + 1e-6
    m['click_ratio'] = round(float(d.max()/ref), 1)
    if d.max()/ref > 8: flags.append(f"click x{d.max()/ref:.0f}")
    # 4) noisy/metallic frames: loud frames with high flatness, or strong narrow tone >5 kHz
    loud = rel > -30
    hiflat = (loud & (flat > 0.55)).sum()*20; m['noisy_ms'] = int(hiflat)
    if hiflat >= 300: flags.append(f"noisy/hissy {hiflat}ms")
    hf = spec[:, freqs > 5000]; tone = (hf.max(1)/np.median(hf, 1))
    whine = ((tone > 60) & (rel > -55)).sum()*20; m['whine_ms'] = int(whine)
    if whine >= 200: flags.append(f"HF whine {whine}ms")
    # 5) duration vs text (speech span), ~ 14 chars/s at speed 0.9; flag > 1.8x + 0.6 s
    letters = len(re.sub(r"[^A-Za-z]", "", text)); exp = letters/14.0
    span = ((rel > -40).nonzero()[0]); dur = (span[-1]-span[0]+1)*0.02 if len(span) else 0
    m['dur_s'], m['exp_s'] = round(dur, 2), round(exp, 2)
    if dur > 1.8*exp + 0.8: flags.append(f"too long {dur:.1f}s vs ~{exp:.1f}s")
    return flags, m
