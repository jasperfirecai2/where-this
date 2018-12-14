
class Device(object):

    def __init__(self, nameP, addressP, devicesP):
        self._name = nameP
        self._address = addressP
        self._floor = input("What floor?")
        self._devices = []
        for name, address in list(devicesP.items()):
            if not address == self._address:
                self._devices.append(address)

    def __str__(self):
        ret = "Device: name: {NAME} address: {ADDR}" \
              " floor: {FLOOR} nearby devices: {DEVICES}\n" \
            .format(NAME=self._name, ADDR=self._address, FLOOR=self._floor, DEVICES=self._devices)
        return ret
