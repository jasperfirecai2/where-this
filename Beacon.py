

class Beacon(object):

    def __init__(self, data, address, devices, index):
        self._uuid = data[0]
        self._major = data[1]
        self._minor = data[2]
        self._power = data[3]
        self._rssi = data[4]
        self._address = address
        self._floor = input("What floor?")
        self._devices = list(devices.items())
        self._id = index
        del self._devices[self._id]

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
        ret = "Beacon: address: {ADDR} uuid: {UUID} major: {MAJOR}\n" \
              " minor: {MINOR} txpower: {POWER} rssi: {RSSI}\n" \
              " floor: {FLOOR} nearby devices: {DEVICES}\n" \
            .format(ADDR=self._address, UUID=self._uuid, MAJOR=self._major,
                    MINOR=self._minor, POWER=self._power, RSSI=self._rssi,
                    FLOOR=self._floor, DEVICES=self._devices)
        return ret
