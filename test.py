import bluetooth
from bluetooth.ble import BeaconService

print("Loaded! Gattlib works?")

serviceB = BeaconService()
serviceD = DiscoveryService()
beacons = serviceB.scan(2)
devices = serviceD.discover(2)
print("Beacons: \n {}".format(beacons))


    def __str__(self):
        ret = "Beacon: address:{ADDR} uuid:{UUID} major:{MAJOR}"\
                " minor:{MINOR} txpower:{POWER} rssi:{RSSI}"\
                " floor:{FLOOR} nearby devices:{DEVICES}"\
                .format(ADDR=self._address, UUID=self._uuid, MAJOR=self._major,
                        MINOR=self._minor, POWER=self._power, RSSI=self._rssi,
                        FLOOR=self._floor, DEVICES=self._devices)
        return ret

service = BeaconService()
devices = service.scan(2)
print(devices)
for address, data in list(devices.items()):
    print(address)
    print(data)
    b = Beacon(data, address)
    print(b)

print("Devices: \n {}".format(devices))

for name, address in list(devices.items()):
    #print("name: {}, address: {}".format(name, address))
    d = Device(name, address, devices)
    print(d)

print("Done.")
