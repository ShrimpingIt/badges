from neopixel import NeoPixel
from machine import Pin
from time import sleep

count = 8

display = NeoPixel(Pin(4), count)

for pos in range(count):
	display[pos] = (0,0,0)
display.write()
