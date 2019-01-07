

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
        ret = "{COUNT} Beacons in list {NAME}:\n".format(COUNT=self._Size, NAME=self._Name)
        for Beacon in self._Beacons:
            ret += "Beacon: address: {ADDR} uuid: {UUID} major: {MAJOR}\n" \
                  " minor: {MINOR} txpower: {POWER} rssi: {RSSI}\n" \
                  " floor: {FLOOR} nearby devices: {DEVICES}\n" \
                .format(ADDR=Beacon.address, UUID=Beacon.uuid, MAJOR=Beacon.major,
                        MINOR=Beacon.minor, POWER=Beacon.power, RSSI=Beacon.rssi,
                        FLOOR=Beacon.floor, DEVICES=Beacon.devices)
        return ret
