"""Voice reference clips for the Level 1 lesson builds (Lessons 2+). Every clip is synthetic Kokoro-82M output (Apache 2.0);
no recordings of real people, and no Chatterbox built-in default voice. Names are the clip names used in script_L1_L<N>.py (VOICES).
  N, Rosa, Sam, Marco, Kim, Receptionist, ...  -> <repo>/tools/audio/samples/refs/<name>.wav   (made by tools/audio/make_refs.py)
  Ana_af_jessica                                -> <repo>/level1/audio/tools/natural/kokoro_refs/af_jessica.wav   (Ana, as in Lesson 1)
See REFS.md for which Kokoro voice each clip is."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
SHARED = os.path.join(REPO, 'tools', 'audio', 'samples', 'refs')
SPECIAL = {'Ana_af_jessica': os.path.join(REPO, 'level1', 'audio', 'tools', 'natural', 'kokoro_refs', 'af_jessica.wav')}
def ref_path(name): return SPECIAL.get(name) or os.path.join(SHARED, f'{name}.wav')
def allowed(path):
    p = os.path.realpath(path)
    return os.path.isfile(p) and (os.path.dirname(p) == os.path.realpath(SHARED) or p in {os.path.realpath(x) for x in SPECIAL.values()})
