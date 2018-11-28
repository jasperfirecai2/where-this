import speech_recognition as spch

rec = spch.Recognizer()
frec = spch.AudioFile('audio.wav')
with frec as source:
    sound = rec.record(source, duration= 5)

rec.recognize_google(sound)