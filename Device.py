import speech_recognition as sr
from gtts import gTTS
import os


class Device(object):

    def __init__(self, nameP, addressP, devicesP):
        self._name = nameP
        self._address = addressP
        self._floor = self.mics()
        self._devices = devicesP
        for name, address in list(self._devices.items()):
            if address == self._address:
                self._devices.remove(address)

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
