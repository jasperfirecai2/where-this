
class Device(object):

    def __init__(self, name, address, devices):
        self._name = name
        self._address = address
        self._floor = input("What floor?")
        self._devices = []
        for namee, addresss in list(devices.items()):
            if not addresss == self._address:
                self._devices.append(addresss)

    def __str__(self):
        ret = "Device: name: {NAME} address: {ADDR}" \
              " floor: {FLOOR} nearby devices: {DEVICES}\n" \
            .format(NAME=self._name, ADDR=self._address, FLOOR=self._floor, DEVICES=self._devices)
        return ret
