from bluetooth.ble import BeaconService
import time

service = BeaconService()

service.start_advertising("11111111-2222-3333-6666-555555555555",
            1, 1, 1, 200)
sleeptime = input("Insert beacon time in seconds: ")
time.sleep(int(sleeptime))

service.stop_advertising()

print("Done.")