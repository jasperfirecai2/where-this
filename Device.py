import speech_recognition as sr
from gtts import gTTS
import os


class Device(object):


    def __init__(self, name, address, devices, index):
        self._name = name
        self._address = address
        self._floor = self.mics()
        self._devices = list(devices.items())
        self._index = index
        del self._devices[self._index]
        self._index += 1

    @staticmethod
    def mics(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("What floor? (use your voice!)")
            audio = r.record(source, duration=5)
        out = r.recognize_google(audio)
        return out



    def __str__(self):
        ret = "Device: name: {NAME} address: {ADDR}" \
              " floor: {FLOOR} nearby devices: {DEVICES}\n" \
            .format(NAME=self._name, ADDR=self._address, FLOOR=self._floor, DEVICES=self._devices)
        return ret
