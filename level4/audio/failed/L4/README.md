# Level 4 Lesson 4 listening draft (gate did not pass)

Lesson 4, "How Long Have You Had It?", was recorded on this computer (CPU, faster-whisper float32) and did not pass the gate. It was not recorded again. The other Level 4 lessons continue on `level4-audio`.

A person has not listened to this file.

- Duration: 1:59 (119.0 s). The Level 4 length gate is 1:30–2:15, so length passed.
- Pauses between speakers: 1.3 s. Pitch passed. Clipped samples: 0.
- Gate `PASS`: false.
- 40 sentences, 82 takes.

Sentences that used all 16 seeds and still failed:

1. "It's one eighteen over seventy-six." Seed 112892. Heard as "it's 118 over 76" (lowest word probability 0.35). After `canon.py` the words match. The take rule still rejects a word probability under 0.5.
2. "You're right. I wanna make an appointment with the dentist." Seed 104973. Heard as "you're right i want to make an appointment with the dentist" (lowest word probability 0.95). `canon.py` does not treat "wanna" as "want to".

On the assembled file, both checkers heard "I'm gonna ask..." as "going to". An isolated take of "I'm gonna ask you a few questions for your health history." passed on seed 9945 and was heard as "gonna".

These files are the MP3 and the check outputs. The WAV master is not included.

Do not treat this file as a finished lesson.
