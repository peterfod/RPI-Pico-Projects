from machine import Pin
from utime import sleep

led_external = Pin(17, Pin.OUT)

while True:
    led_external.toggle()
    sleep(0.2)