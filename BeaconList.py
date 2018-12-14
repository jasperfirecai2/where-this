
class BeaconList:
    def __init__(self, name):
        self._Beacons = []
        self._Size = 0
        self._Name = name

    def add(self, beacon):
        self._Beacons.append(beacon)
        self._Size = len(self._Beacons)

    def remove(self, index):
        del self._Beacons[index]

    def __str__(self):
        ret = "{COUNT} Devices in list {NAME}:\n".format(COUNT=self._Size, NAME=self._Name)
        for Beacon in self._Beacons:
            ret += "Device: name: {NAME} address: {ADDR}" \
                  " floor: {FLOOR} \n nearby devices: {DEVICES}\n" \
                .format(NAME=self._name, ADDR=self._address, FLOOR=self._floor, DEVICES=self._devices)
            return ret
