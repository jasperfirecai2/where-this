
class Device(object):

    def __init__(self, name, address, devices, index):
        self._name = name
        self._address = address
        self._floor = input("What floor?")
        self._devices = list(devices.items())
        self._index = index
        for namee, addresss in self._devices:
            if addresss == self._address:
                del self._devices[self._index]
            self._index += 1

    def __str__(self):
        ret = "Device: name: {NAME} address: {ADDR}" \
              " floor: {FLOOR} nearby devices: {DEVICES}\n" \
            .format(NAME=self._name, ADDR=self._address, FLOOR=self._floor, DEVICES=self._devices)
        return ret
