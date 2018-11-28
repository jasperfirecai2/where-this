from PyInstaller.hooks.hookutils import collect_data_files
datas = collect_data_files('speech_recognition')
import speech_recognition as spch

rec = spch.Recognizer()

with spch.AudioFile("tim_and_eric_it_s_free_real_estate") as source:
    audio = rec.record(source)
try:
    out = rec.recognize_google(audio)
except Exception as e:
    print("Exception: " + str(e))