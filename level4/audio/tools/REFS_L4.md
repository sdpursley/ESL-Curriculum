# Voice reference clips for the Level 4 listening builds (all synthetic)

`make_refs_L4.py` writes these clips into `refs/` from their **Kokoro-82M** voice ids (hexgrad, Apache 2.0). The WAVs are **not committed**
(`*.wav` is ignored); they reproduce the committed repo clips exactly (`make_refs_L4.py --check`: same length, correlation 1.0 with
kokoro-onnx 0.6.1 + kokoro-v1.0.onnx + voices-v1.0.bin; checked for the Level 3 drafts on 22 Oct 2026; Level 4 uses the same clips). `make_refs_L4.py --copy` copies those committed clips instead.
Chatterbox clones the voice from the clip. No human recordings, no LibriTTS/LibriVox, no Piper, no Chatterbox default voice.

| Clip in `refs/` | Kokoro-82M voice | Voice | Same as (committed) |
|---|---|---|---|
| `N.wav` | af_sarah | female (Narrator in every Level 4 lesson) | `tools/audio/samples/refs/N.wav` |
| `Rosa.wav` | af_heart | female | `tools/audio/samples/refs/Rosa.wav` |
| `Sam.wav` | am_michael | male | `tools/audio/samples/refs/Sam.wav` |
| `Ana_af_jessica.wav` | af_jessica | female | `level1/audio/tools/natural/kokoro_refs/af_jessica.wav` |
| `Ana_af_bella.wav` | af_bella | female | `tools/audio/samples/refs/Ana.wav` |
| `Kim.wav` | af_nova | female | `tools/audio/samples/refs/Kim.wav` |
| `Receptionist.wav` | af_river | female | `tools/audio/samples/refs/Receptionist.wav` |
| `Marco.wav` | am_adam | male | `tools/audio/samples/refs/Marco.wav` |
| `Server.wav` | am_puck | male | `tools/audio/samples/refs/Server.wav` |
| `Carlos.wav` | am_eric | male | `tools/audio/samples/refs/Carlos.wav` |

(`Agent.wav` = af_kore is not used in Level 4.) Which character uses which clip is in `cast/cast_L4_L<N>.json` (`VOICES`, `FEMALE`) and
in the generated `scripts/script_L4_L<N>.py`; female characters always get a female clip.
