import bluetooth
from bluetooth.ble import BeaconService, DiscoveryService
from Beacon import *
from Device import *

print("Loaded! Gattlib works?")
serviceB = BeaconService()
serviceD = DiscoveryService()
beacons = serviceB.scan(2)
devices = serviceD.discover(2)
devices2 = devices
service = BeaconService()
print(devices)
print("Beacons: \n {}".format(beacons))

for address, data in list(beacons.items()):
    print(address)
    print(data)
    b = Beacon(data, address)
    print(b)

print("Devices: \n {}".format(devices))

i = 0
for address, name in list(devices.items()):
    # print("name: {}, address: {}".format(name, address))
    d = Device(address, name, devices2, i)
    i += 1
    print(d)

print("Successfully Initialized.")
