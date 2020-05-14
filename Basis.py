# IMPORTS
from gpiozero import DigitalOutputDevice
from gpiozero.pins.pigpio import PiGPIOFactory
import time
from gpiozero import Button

# VARIABLES
factory = PiGPIOFactory(host='192.168.1.55')

# SETUP LED
YELLOW = DigitalOutputDevice(pin=14, pin_factory=factory)
GREEN = DigitalOutputDevice(pin=15,  pin_factory=factory)
RED = DigitalOutputDevice(pin=18,  pin_factory=factory)
ORANJE = DigitalOutputDevice(pin=23,pin_factory=factory)

# SETUP Button
BUTN1 = Button(pin=2,pin_factory=factory)
BUTN2 = Button(pin=3,pin_factory=factory)
BUTN3 = Button(pin=17,pin_factory=factory)
BUTN4 = Button(pin=27,pin_factory=factory)

BUTN1.when_pressed = YELLOW.on
BUTN1.when_released = YELLOW.off
BUTN1.wait_for_press()
print("- Geel licht aan ")

BUTN2.when_pressed = GREEN.on
BUTN2.when_released = GREEN.off
BUTN2.wait_for_press()
print("- Groen licht aan ")

BUTN3.when_pressed = RED.on
BUTN3.when_released = RED.off
BUTN3.wait_for_press()
print("- Rood licht aan ")

BUTN4.when_pressed = ORANJE.on
BUTN4.when_released = ORANJE.off
BUTN4.wait_for_press()
print("- Geel 2.0 licht aan ")
