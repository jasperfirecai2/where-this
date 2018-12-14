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
        failcount = 0
        out = "Not assigned"
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                while True:
                    try:
                        if failcount < 5:
                            print("What floor? (use your voice!)")
                            audio = r.record(source, duration=5)
                            out = r.recognize_google(audio)
                        elif failcount < 10:
                            out = input("Please type the floor input (too many failed voice attempts)")
                        else:
                            print("Too many failed attempts, you will have to assign the floor later")
                            out = "Not assigned"
                            break
                        out = int(out)
                        break
                    except ValueError:
                        print("I'm not sure if that was a number")
                        failcount += 1
                    except KeyboardInterrupt:
                        print("Cancelling floor input for this device")
                        break
                    except:
                        print("I didn't quite catch that, try again")
                        failcount += 1

        except OSError:
            print("No microphone could be found, using typed input")
            while True:
                try:
                    if failcount < 5:
                        out = input("Please type the floor input")
                        out = int(out)
                    else:
                        out = "Not assigned"
                        break
                except ValueError:
                    print("I'm not sure if that was a number")
                    failcount += 1
                except KeyboardInterrupt:
                    print("Cancelling floor input for this device")
                    break
                except:
                    print("unknown error, try again")
                    failcount += 1

        return out

    def __str__(self):
        ret = "Device: name: {NAME} address: {ADDR}" \
              " floor: {FLOOR} nearby devices: {DEVICES}\n" \
            .format(NAME=self._name, ADDR=self._address, FLOOR=self._floor, DEVICES=self._devices)
        return ret
