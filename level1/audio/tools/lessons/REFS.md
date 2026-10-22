# Voice reference clips for Level 1 Lessons 2–13 (all synthetic, Kokoro-82M, Apache 2.0)

Every Chatterbox voice in Level 1 Lessons 2–13 is cloned from one of these clips. They are all plain Kokoro-82M output:
no recordings of real people, and never Chatterbox's built-in default voice. `refs.py` turns a clip name into its path;
`engine.py` refuses any other file.

| Clip name | File in the repository | Kokoro-82M voice | Used for (lesson) |
|---|---|---|---|
| `N` | `tools/audio/samples/refs/N.wav` (made by `tools/audio/make_refs.py`) | af_sarah | Narrator (all) |
| `Rosa` | `tools/audio/samples/refs/Rosa.wav` | af_heart | Rosa (2, 5, 10, 12) |
| `Marco` | `tools/audio/samples/refs/Marco.wav` | am_adam | Marco (2, 5, 9, 11, 12) |
| `Receptionist` | `tools/audio/samples/refs/Receptionist.wav` | af_river | Receptionist (3, 6, 9), Operator (12) |
| `Kim` | `tools/audio/samples/refs/Kim.wav` | af_nova | Kim (4, 6, 9) |
| `Sam` | `tools/audio/samples/refs/Sam.wav` | am_michael | Carlos (4; same voice as Lesson 1), Manager (13) |
| `Server` | `tools/audio/samples/refs/Server.wav` | am_puck | phone message (6), Server (8) |
| `Carlos` | `tools/audio/samples/refs/Carlos.wav` | am_eric | Cashier (7) |
| `Agent` | `tools/audio/samples/refs/Agent.wav` | af_kore | Agent (10) |
| `Ana_af_jessica` | `level1/audio/tools/natural/kokoro_refs/af_jessica.wav` (made by `make_ana_ref.py`, see `ana_ref.json`) | af_jessica | Ana (3, 7, 8, 11, 12, 13; same voice as Lesson 1) |
