

class Beacon(object):

    def __init__(self, data, address, devices):
        self._uuid = data[0]
        self._major = data[1]
        self._minor = data[2]
        self._power = data[3]
        self._rssi = data[4]
        self._address = address
        self._floor = input("What floor?")
        self._devices = []
        for addresss, dataa in list(devices.items()):
            if not self._uuid == dataa[0]:
                self._devices.append(dataa[0])
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
        ret = "Beacon: address: {ADDR} uuid: {UUID} major: {MAJOR}\n" \
              " minor: {MINOR} txpower: {POWER} rssi: {RSSI}\n" \
              " floor: {FLOOR} nearby devices: {DEVICES}\n" \
            .format(ADDR=self._address, UUID=self._uuid, MAJOR=self._major,
                    MINOR=self._minor, POWER=self._power, RSSI=self._rssi,
                    FLOOR=self._floor, DEVICES=self._devices)
        return ret
