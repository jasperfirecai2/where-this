import bluetooth
from bluetooth.ble import BeaconService, DiscoveryService

print("Loaded! Gattlib works?")

class Beacon(object):
    
    def __init__(self, data, address, devices): pass
        self._uuid = data[0]
        self._major = data[1]
        self._minor = data[2]
        self._power = data[3]
        self._rssi = data[4]
        self._address = address
        self._floor = input("What floor xd?")
        self._devices = []
        for address, data in list(devices.items()):
            if not self._uuid == data[0]:
                b = Beacon(data, address)
                self._devices.append(b)
    
    def __init__(self, data, address):
        self._uuid = data[0]
        self._major = data[1]
        self._minor = data[2]
        self._power = data[3]
        self._rssi = data[4]
        self._address = address
        self._floor = input("What floor xD?")

    def __str__(self):
        ret = "Beacon: address:{ADDR} uuid:{UUID} major:{MAJOR}"\
                " minor:{MINOR} txpower:{POWER} rssi:{RSSI}"\
                " floor:{FLOOR} nearby devices:{DEVICES}"\
                .format(ADDR=self._address, UUID=self._uuid, MAJOR=self._major,
                        MINOR=self._minor, POWER=self._power, RSSI=self._rssi,
                        FLOOR=self._floor, DEVICES=self._devices)
        return ret


serviceB = BeaconService()
serviceD = DiscoveryService()
beacons = serviceB.scan(2)
devices = serviceD.scan(2)
print("Beacons: \n {}".format(beacons))

for address, data in list(beacons.items()):
    print(address)
    print(data)
    b = Beacon(data, address)
    print(b)

print("Devices: \n {}".format(devices))

for name, address in list(devices.items()):
    print("name: {}, address: {}".format(name, address))
    #b = Beacon(data, address)
    #print(b)


print("Done.")
