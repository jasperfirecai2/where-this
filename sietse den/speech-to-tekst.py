import speech_recognition as sr
import pyttsx3
from gtts import gTTS
import os

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.record(source, duration=5)
out = r.recognize_google(audio)
print(out)
tts = gTTS(text=out, lang='nl')
tts.save("speg.mp3")
os.system("speg.mp3")