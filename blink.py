from machine import Pin
from time import sleep

pin = Pin(25, Pin.OUT)
n = 0
while True:
    pin.toggle()
    sleep(0.5)
    print("n =", n)
    n = n + 1

