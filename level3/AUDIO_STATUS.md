# Level 3 Lessons 2-13: listening audio status

Draft for review. These lessons live in `level3/drafts/` and are **not on the website** (`scripts/export_content.py` reads only
`level3/curriculum`, `level3/images`, `level3/audio` and `level3/slides`). How to record a lesson: AGENTS.md, section
"Running audio locally". Update this file in the same commit as each finished MP3.

Status as of 22 Oct 2026, 23:43 CDT. Lessons marked **done** below passed the gate on this computer (CPU, faster-whisper float32).
**Takes from the build computer are not in the repo and cannot be reused:** the take cache is keyed by file paths, and the same seed gives a
different take on another computer or device. Every lesson that is not "done" must be recorded **from line 1** on the local
computer. The notes below only say which lines gave trouble there, so watch them closely.

| Lesson | Topic voices (cast) | Lines | Status | Result / what remains |
|---|---|---|---|---|
| 2 | Narrator, Linda (F, af_jessica), Omar (M, am_adam) | intro + 17 + end | **done** | `drafts/audio/L3_L2_listening.mp3`, 1:28, gate PASS. Recorded from line 1 on this computer with local retakes. Human listen still outstanding. |
| 3 | Narrator, Daniel (M, am_puck), Teresa (F, af_bella) | intro + 15 + end | **done** | `drafts/audio/L3_L3_listening.mp3`, 1:15, gate PASS. Recorded from line 1 on this computer. Human listen still outstanding. |
| 4 | Narrator, Elena (F, af_heart), Mark (M, am_adam) | intro + 16 + end | **done** | `drafts/audio/L3_L4_listening.mp3`, 1:18, gate PASS (two-checker rule). |
| 5 | Narrator, Carmen (F, af_river), David (M, am_michael) | intro + 14 + end | **done** | `drafts/audio/L3_L5_listening.mp3`, 1:17, gate PASS. |
| 6 | Narrator, Nadia (F, af_jessica), Ben (M, am_puck) | intro + 11 + end | **done** | `drafts/audio/L3_L6_listening.mp3`, 1:16, gate PASS. Recorded from line 1 on this computer. Human listen still outstanding. |
| 7 | Narrator, Lina (F, af_heart), Clerk (M, am_puck) | intro + 16 + end | **done** | `drafts/audio/L3_L7_listening.mp3`, 1:17, gate PASS. Recorded from line 1 on this computer. Human listen still outstanding. |
| 8 | Narrator, Joan (F, af_river), David (M, am_michael) | intro + 15 + end | **done** | `drafts/audio/L3_L8_listening.mp3`, 1:17, gate PASS. Recorded from line 1 on this computer. Human listen still outstanding. |
| 9 | Narrator, Lucia (F, af_jessica), Mr. Hall (M, am_michael) | intro + 14 + end | **done** | `drafts/audio/L3_L9_listening.mp3`, 1:20, gate PASS. Recorded from line 1 on this computer. Human listen still outstanding. |
| 10 | Narrator, Maria (F, af_heart), Tom (M, am_adam) | intro + 13 + end | **done** | `drafts/audio/L3_L10_listening.mp3`, 1:11, gate PASS. Recorded from line 1 on this computer. Human listen still outstanding. |
| 11 | Narrator, Elena (F, af_heart), Luis (M, am_adam) | intro + 13 + end | **done** | `drafts/audio/L3_L11_listening.mp3`, 1:17, gate PASS. Recorded from line 1 on this computer. Human listen still outstanding. |
| 12 | Narrator, Sara (F, af_river), Mr. Grant (M, am_michael) | intro + 12 + end | **done** | `drafts/audio/L3_L12_listening.mp3`, 1:16, gate PASS. Recorded from line 1 on this computer. Human listen still outstanding. |
| 13 | Narrator, Mr. Novak (M, am_puck), Sofia (F, af_heart) | intro + 11 + end | to-do | all lines |

The Narrator is always the `N` clip (Kokoro af_sarah, female). The full line text of every lesson is in
`drafts/audio/tools/scripts/script_L3_L<N>.py` (`INTRO`, `LINES` = speaker + line, `END`), generated from the lesson Markdown by
`make_script_L3.py`; voices and settings are in `drafts/audio/tools/cast/cast_L3_L<N>.json` and the AGENTS.md rules.

**Summary:** done 11 (Lessons 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12) · partial 0 · to-do 1 (Lessons 13).

## Notes from the build-computer runs

### Lesson 2 (partial)
Run 1 (before the script was trimmed) failed the gate for four reasons:
- length 1:34 (limit 1:30). The script has since been cut to 17 lines (about 175 words), but it was never rebuilt;
- the narrator sentence "His supervisor, Linda, tells him about two coworkers. Listen." FAILED (no passing take);
- a high-frequency whine on Linda's line "Nora is the short woman with long, straight hair.";
- small.en dropped "Oh, I see him." in line 16.
On the build computer, "Nora is the short woman with long, straight hair." and "She's a little shy." were rejected with seed 2026. It never
recorded "Yes. She's quiet, but she's really hardworking." or "She's very patient.". Remaining work: everything (intro, lines 1-17,
end), then the checks and gate. If the file is still over 1:30, shorten the script (lesson Markdown first, then
`make_script_L3.py 2`). Do not speed up the audio.

### Lesson 3 (partial)
The gate at 12:53 CDT FAILED at 1:15. Passing takes existed for the intro and lines 1-8 (through "Yes. It was far, so we used to
walk for an hour."); a retake of lines 9-15 and the end was stopped. These takes were rejected:
`{"We used to do our chores.": [2026], "Yes. We used to live on a farm near a river.": [33702], "Wow. Did you use to walk to school?": [2026]}`.
(The seeds only matter on the build computer. On your computer, start without EXCLUDE and add your own rejected seeds.)
Remaining work: everything (intro, lines 1-15, end), then the checks and gate. Listen closely to line 10 ("We used to do our chores.
Then we used to climb trees and swim in the river.").

### Lessons 4 and 5 (done)
- Lesson 4: 1:18. small.en heard "Elena" as "Alana" in one line, but medium.en got all 18 lines right, so the line passes under the
  two-checker rule. One retake: "Good. Did the police come?" (seed 17864). The build-computer Whisper ran with int8 compute; checks on the
  local computer use float32 (`whisper_cfg.py`).
- Lesson 5: 1:17, gate PASS at 14:05 CDT.
Each one's README, log, check results, gate and medium.en second opinion are next to the MP3 in `drafts/audio/`.
