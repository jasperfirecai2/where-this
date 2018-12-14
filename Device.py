
class Device(object):

    def __init__(self, nameP, addressP, devicesP):
        self._name = nameP
        self._address = addressP
        self._floor = input("What floor?")
        self._devices = list(devicesP.items())
        self._index = 0
        for name, address in self._devices:
            if address == self._address:
                del self._devices[self._index]
            self._index += 1

    def __str__(self):
        ret = "Device: name: {NAME} address: {ADDR}" \
              " floor: {FLOOR} nearby devices: {DEVICES}\n" \
            .format(NAME=self._name, ADDR=self._address, FLOOR=self._floor, DEVICES=self._devices)
        return ret
