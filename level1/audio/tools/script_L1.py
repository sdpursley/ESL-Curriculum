# Level 1, Lesson 1 listening script (original text written for this curriculum; invented names).
# Format: (speaker, line). Text inside {braces} is spelled letter by letter (made as one piece, then spaced out).
INTRO = "Lesson one. Listening. It's the first night of English class. Ana and Carlos sign in. Listen."
LINES = [
 ("Receptionist", "Hello! Welcome to English class."),
 ("Ana", "Hello. Thank you."),
 ("Receptionist", "What's your name?"),
 ("Ana", "My name is Ana."),
 ("Receptionist", "Hi, Ana. What's your last name?"),
 ("Ana", "It's Ruiz."),
 ("Receptionist", "How do you spell it?"),
 ("Ana", "{R, U, I, Z.}"),
 ("Receptionist", "Thank you, Ana. Next, please!"),
 ("Receptionist", "Hello! What's your name?"),
 ("Carlos", "Hi. I'm Carlos. My last name is Vega."),
 ("Receptionist", "How do you spell it?"),
 ("Carlos", "{V, E, G, A.}"),
 ("Receptionist", "Sorry. Can you repeat, please?"),
 ("Carlos", "Yes, of course. {V, E, G, A.}"),
 ("Receptionist", "Thank you, Carlos. How are you?"),
 ("Carlos", "I'm fine, thanks. And you?"),
 ("Receptionist", "I'm fine, thank you. Here's your book and a pen."),
 ("Carlos", "Thank you. Goodbye!"),
 ("Receptionist", "Goodbye!"),
]
END = "That's the end of the listening."
def plain(line): return line.replace("{", "").replace("}", "")
