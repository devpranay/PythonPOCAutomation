import pyttsx3
with open("audio.txt") as f:
    engine=pyttsx3.init()
    txt=f.read()
    print(txt)
    engine.say(txt)
    engine.runAndWait()
 
