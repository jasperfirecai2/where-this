
class DeviceList:
    def __init__(self, name):
        self._Devices = []
        self._Size = 0
        self._Name = name

    def add(self, device):
        self._Devices.append(device)
        self._Size = len(self._Devices)

    def remove(self, index):
        del self._Devices[index]

    def __str__(self):
        ret = "{COUNT} Devices in list {NAME}:\n".format(COUNT=self._Size, NAME=self._Name)
        for Device in self._Devices:
            ret += "Device:\n" \
                   "\tname: {NAME}\n" \
                   "\taddress: {ADDR}\n" \
                   "\tfloor: {FLOOR} ID: {ID}\n" \
                .format(NAME=Device.name, ADDR=Device.address, FLOOR=Device.floor, ID=Device.id)
        return ret
