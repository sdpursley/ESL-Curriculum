# Voice reference clips for Level 1 Lessons 2–4 (all synthetic, Kokoro-82M, Apache 2.0)

Every Chatterbox voice in Level 1 Lessons 2–4 is cloned from one of these clips. They are all plain Kokoro-82M output:
no recordings of real people, and never Chatterbox's built-in default voice. `refs.py` turns a clip name into its path;
`engine.py` refuses any other file.

| Clip name | File in the repository | Kokoro-82M voice | Used for |
|---|---|---|---|
| `N` | `tools/audio/samples/refs/N.wav` (made by `tools/audio/make_refs.py`) | af_sarah | Narrator |
| `Rosa` | `tools/audio/samples/refs/Rosa.wav` | af_heart | Rosa (Lesson 2) |
| `Marco` | `tools/audio/samples/refs/Marco.wav` | am_adam | Marco (Lesson 2) |
| `Receptionist` | `tools/audio/samples/refs/Receptionist.wav` | af_river | Receptionist (Lesson 3) |
| `Ana_af_jessica` | `level1/audio/tools/natural/kokoro_refs/af_jessica.wav` (made by `make_ana_ref.py`, see `ana_ref.json`) | af_jessica | Ana (Lesson 3; same voice as Lesson 1) |
| `Kim` | `tools/audio/samples/refs/Kim.wav` | af_nova | Kim (Lesson 4) |
| `Sam` | `tools/audio/samples/refs/Sam.wav` | am_michael | Carlos (Lesson 4; same voice as Lesson 1) |
