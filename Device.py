
class Device(object):

    def __init__(self, nameP, addressP, devicesP):
        self._name = nameP
        self._address = addressP
        self._floor = input("What floor?")
        self._devices = list(devicesP.items())
        for name, address in list(self._devices.items()):
            if address == self._address:
                self._devices.remove(address)

    def __str__(self):
        ret = "Device: name: {NAME} address: {ADDR}" \
              " floor: {FLOOR} nearby devices: {DEVICES}\n" \
            .format(NAME=self._name, ADDR=self._address, FLOOR=self._floor, DEVICES=self._devices)
        return ret
