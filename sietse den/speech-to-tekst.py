import speech_recognition as spch

rec = spch.Recognizer()
sound = spch.AudioFile("tim_and_eric_it_s_free_real_estate.mp3")
with sound as source:
    audio = rec.record(source,duration= 6)
type(audio)
try:
    out = rec.recognize_google(spch.AudioFile("tim_and_eric_it_s_free_real_estate.mp3"))
except Exception as e:
    print("Exception: " + str(e))