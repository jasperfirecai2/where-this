import speech_recognition as sr
from gtts import gTTS
import os


class Device(object):

    def __init__(self, address, name, devices, index):
        self._address = address
        self._name = name
        self._floor = self.mics(self)
        self._devices = list(devices.items())
        self._id = index
        del self._devices[self._id]

    @staticmethod
    def mics(self):
        r = sr.Recognizer()
        out = "Not assigned"
        with sr.Microphone() as source:
            while True:
                try:
                    print("What floor? (use your voice!)")
                    audio = r.record(source, duration=5)
                    out = r.recognize_google(audio)
                    out = int(out)
                    break
                except ValueError:
                    print("I'm not sure if that was a number")
                except KeyboardInterrupt:
                    print("Cancelling floor input for this device")
                    break
                except:
                    print("I didn't quite catch that, try again")
        return out



    def __str__(self):
        ret = "Device: name: {NAME} address: {ADDR}" \
              " floor: {FLOOR} nearby devices: {DEVICES}\n" \
            .format(NAME=self._name, ADDR=self._address, FLOOR=self._floor, DEVICES=self._devices)
        return ret
