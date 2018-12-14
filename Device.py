
class Device(object):

    def __init__(self, name, address, devices):
        self._name = name
        self._address = address
        self._floor = input("What floor?")
        self._devices = []
        for address, data in list(devices.items()):
            if not self._uuid == data[0]:
                b = Device(data, address)
                self._devices.append(b)

    def __init__(self, name, address):
        self._name = name
        self._address = address
        self._floor = input("What floor?")

    def __str__(self):
        ret = "Device: name:{NAME} address:{ADDR}" \
              " floor:{FLOOR} nearby devices:{DEVICES}" \
            .format(NAME=self._name, ADDR=self._address, FLOOR=self._floor, DEVICES=self._devices)
        return ret
