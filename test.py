import bluetooth
import subprocess
from bluetooth.ble import BeaconService, DiscoveryService
from Beacon import *
from Device import *
print("Fetching updates from github")
subprocess.call(['./GitPull.sh'])
print("Updated from github, loading devices")



serviceB = BeaconService()
serviceD = DiscoveryService()
beacons = serviceB.scan(2)
devices = serviceD.discover(2)
devices2 = devices
service = BeaconService()
print("Loaded! Gattlib works?")
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
    #print("name: {}, address: {}".format(name, address))
    d = Device(address, name, devices2, i)
    i += 1
    print(d)

print("Done.")
