from time import sleep

from gpiozero import LED

led = LED(17)

btFound = True
distanceToBeacon = 5

while btFound:
    led.on()
    sleep(distanceToBeacon)
    led.on()
    sleep(distanceToBeacon)
