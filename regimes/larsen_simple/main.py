from neopixel import NeoPixel
from machine import Pin
display = NeoPixel(Pin(4), 8)
red = (255,0,0)
display[0] = red
for pos in range(len(display)):
	display[pos]=
