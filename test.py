import bluetooth
from bluetooth.ble import BeaconService, DiscoveryService
from Beacon import *
from Device import *

print("Loaded! Gattlib works?")
serviceB = BeaconService()
serviceD = DiscoveryService()
beacons = serviceB.scan(2)
devices = serviceD.discover(2)
print("Beacons: \n {}".format(beacons))

for address, data in list(beacons.items()):
    print(address)
    print(data)
    b = Beacon(data, address)
    print(b)

print("Devices: \n {}".format(devices))

for name, address in list(devices.items()):
    #print("name: {}, address: {}".format(name, address))
    d = Device(name, address)
    print(d)

print("Done.")
