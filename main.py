import bluetooth
from bluetooth.ble import BeaconService, DiscoveryService
from Beacon import *
from Device import *


class Main:
    def __init__(self):

        print("Loaded! Gattlib works?")
        self._serviceB = BeaconService()
        self._serviceD = DiscoveryService()
        self._beacons = self._serviceB.scan(2)
        self._devices = self._serviceD.discover(2)
        self._devices2 = self._devices
        self._service = BeaconService()
        print(self._devices)
        print("Beacons: \n {}".format(self._beacons))

        for address, data in list(self._beacons.items()):
            print(address)
            print(data)
            b = Beacon(data, address)
            print(b)

        print("Devices: \n {}".format(self._devices))

        i = 0
        for address, name in list(self._devices.items()):
            # print("name: {}, address: {}".format(name, address))
            d = Device(address, name, self._devices2, i)
            i += 1
            print(d)

        print("Successfully Initialized.")
