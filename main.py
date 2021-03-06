import bluetooth
from bluetooth.ble import BeaconService, DiscoveryService
from Beacon import *
from Device import *
from DeviceList import *
from BeaconList import *

print("Loaded! Gattlib works?")
serviceB = BeaconService()
serviceD = DiscoveryService()
beacons = serviceB.scan(2)
beacons2 = beacons
devices = serviceD.discover(2)
devices2 = devices
service = BeaconService()
print("Beacons: \n {}".format(beacons))
beaconsL = BeaconList('Beacons')
i = 0
for address, data in list(beacons.items()):
    b = Beacon(data, address, beacons2, i)
    beaconsL.add(b)
    i += 1
    print(b)

print("Devices: \n {}".format(devices))
devicesL = DeviceList('Devices')
j = 0
for address, name in list(devices.items()):
    # print("name: {}, address: {}".format(name, address))
    d = Device(address, name, devices2, j)
    devicesL.add(d)
    j += 1
    print(d)

print("Successfully Initialized.")
print(devicesL)
print(beaconsL)
