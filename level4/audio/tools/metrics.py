import numpy as np, librosa
def prosody(a, sr=24000):
    f0, vflag, _ = librosa.pyin(a, fmin=65, fmax=400, sr=sr, frame_length=1024)
    f = f0[vflag & np.isfinite(f0)]
    if len(f) < 10: return dict(f0_st_sd=0, f0_range_st=0)
    st = 12*np.log2(f/np.median(f))
    return dict(f0_med=round(float(np.median(f)),1), f0_st_sd=round(float(st.std()),2), f0_range_st=round(float(np.percentile(st,95)-np.percentile(st,5)),2))
