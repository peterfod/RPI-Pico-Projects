from machine import Pin
from utime import sleep

led_red = Pin(0, Pin.OUT)
led_amber = Pin(1, Pin.OUT)
led_green = Pin(2, Pin.OUT)

while True:
    led_red.value(1)
    sleep(5)
    led_amber.value(1)
    sleep(2)
    led_red.value(0)
    led_amber.value(0)
    led_green.value(1)
    sleep(5)
    led_green.value(0)
    led_amber.value(1)
    sleep(3)
    led_amber.value(0)