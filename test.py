import bluetooth
from bluetooth.ble import BeaconService
for i in range(1, 10000):
    print("Loading: {0}%: Gattlib is a cunt".format((i+1)/100))

print("Loaded! Gattlib works? Jasper was here")
class Beacon(object):
    
    def __init__(self, data, address, devices):
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
        self._floor = input("What floor xd?")
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

print("Done.")
