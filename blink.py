from machine import Pin
from time import sleep

led = Pin("LED", Pin.OUT)
while True:
    led.value(not led.value())
    sleep(0.5)

try:
    led = Pin("LED", Pin.OUT)
    while sleep(0.5):
        led.value(not led.value())
        sleep(0.5)
finally:
    led.value(0)
