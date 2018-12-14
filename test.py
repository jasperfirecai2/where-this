import bluetooth
from bluetooth.ble import BeaconService, DiscoveryService
from Beacon import *
from Device import *

print("Loaded! Gattlib works?")

serviceB = BeaconService()
serviceD = DiscoveryService()
beacons = serviceB.scan(2)
devices = serviceD.discover(2)

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
for name, address in list(devices.items()):
    #print("name: {}, address: {}".format(name, address))
    d = Device(name, address, devices, i)
    i += 1
    print(d)

print("Done.")
