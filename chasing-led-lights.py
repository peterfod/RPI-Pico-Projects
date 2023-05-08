from machine import Pin
from utime import sleep

leds = [Pin(i, Pin.OUT) for i in range(0,5)]

while True:
    for n in range(0,5):
        leds[n].value(1)
        sleep(0.5)
        leds[n].value(0)
    for n in range(3,0,-1):
        leds[n].value(1)
        sleep(0.5)
        leds[n].value(0)