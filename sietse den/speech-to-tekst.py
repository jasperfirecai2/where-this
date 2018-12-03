import speech_recognition as sr
import pyttsx3
from gtts import gTTS
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.record(source, duration=5)
out = r.recognize_google(audio)
print(out)
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say(out)
    engine.runAndWait()
    engine.stop()