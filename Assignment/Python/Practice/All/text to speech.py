import pyttsx3 as p

engine = p.init()

voices = engine.getProperty('voices')

for voice in voices:
    print(voice)

engine.setProperty('voice', voices[2].id)

engine.setProperty('rate', 200)

engine.setProperty('volume', 1)

engine.say("Hey There, How are you? ")

engine.runAndWait()
