

class Beacon(object):

    @staticmethod
    def check(self):
        failcount = 0
        out = "Not assigned"
        while True:
            try:
                if failcount < 5:
                    out = input("Please type the floor input\n")
                    out = int(out)
                    break
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

    def __init__(self, data, address, devices, index):
        self._uuid = data[0]
        self._major = data[1]
        self._minor = data[2]
        self._power = data[3]
        self._rssi = data[4]
        self._address = address
        self._floor = ""
        self._devices = list(devices.items())
        self._id = index
        del self._devices[self._id]
        self._floor = self.check(self)

    @property
    def uuid(self):
        return self._uuid

    @property
    def major(self):
        return self._major

    @property
    def minor(self):
        return self._minor

    @property
    def power(self):
        return self._power

    @property
    def rssi(self):
        return self._rssi

    @property
    def address(self):
        return self._address

    @property
    def floor(self):
        return self._floor

    @property
    def devices(self):
        return self._devices





    #
    # def __init__(self, data, address):
    #     self._uuid = data[0]
    #     self._major = data[1]
    #     self._minor = data[2]
    #     self._power = data[3]
    #     self._rssi = data[4]
    #     self._address = address
    #     self._floor = input("What floor?")

    def __str__(self):
        ret = "Beacon:\n" \
              "\taddress: {ADDR}\n" \
              "\tuuid: {UUID}\n" \
              "\tmajor: {MAJOR} minor: {MINOR} txpower: {POWER}\n" \
              "\trssi: {RSSI}\n" \
              "\tfloor: {FLOOR}\n" \
              "\tnearby devices: {DEVICES}\n" \
            .format(ADDR=self._address, UUID=self._uuid, MAJOR=self._major,
                    MINOR=self._minor, POWER=self._power, RSSI=self._rssi,
                    FLOOR=self._floor, DEVICES=self._devices)
        return ret
