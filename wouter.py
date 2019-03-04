import bluetooth
from bluetooth.ble import BeaconService, DiscoveryService
import time
import os



class Beacon(object):
    def __init__(self, data, address, devices, index):
        self._uuid = data[0]
        self._major = data[1]
        self._minor = data[2]
        self._power = data[3]
        self._rssi = data[4]
        self._address = address
        self._id = index

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

    def __str__(self):
        ret = "Beacon:\n" \
              "\taddress: {ADDR}\n" \
              "\tuuid: {UUID}\n" \
              "\tmajor: {MAJOR} minor: {MINOR} txpower: {POWER}\n" \
              "\trssi: {RSSI}\n" \
              .format(ADDR=self._address, UUID=self._uuid, MAJOR=self._major,
                    MINOR=self._minor, POWER=self._power, RSSI=self._rssi)
        return ret

counter = 0
serviceB = BeaconService()

while True:
    beacons = serviceB.scan(2)    
    i = 0
    os.system('clear')
    print(counter)
    print("-"*20)
    for address, data in list(beacons.items()):
        b = Beacon(data, address, beacons, i)
        i += 1
        print(b.rssi)
        print(b.address)
        print("-"*20)

    # time.sleep(1)
    counter += 1