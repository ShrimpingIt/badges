from time import sleep
from neopixel import NeoPixel
from machine import Pin

intensity = 0.1

dataPin = Pin(4)
ledCount = 64
np = NeoPixel(dataPin, ledCount)

def hsb(h, s, b):
    if s == 0.0: return b, b, b
    i = int(h*6.0) # XXX assume int() truncates!
    f = (h*6.0) - i
    p = b*(1.0 - s)
    q = b*(1.0 - s*f)
    t = b*(1.0 - s*(1.0-f))
    if i%6 == 0: rgb = b, t, p
    if i == 1: rgb = q, b, p
    if i == 2: rgb = p, b, t
    if i == 3: rgb = p, q, b
    if i == 4: rgb = t, p, b
    if i == 5: rgb = b, p, q
    return [int(color * intensity * 255 )  for color in rgb]

def blank():
	for pos in range(ledCount):
		np[pos]=(0,0,0)
	np.write();

saturation = 1
brightness = 1
rainbow = [hsb(hue, saturation, brightness) for hue in [x / ledCount for x in range(ledCount)]]

def write_rainbow(start=0):	
	for pos in range(ledCount):
		np[pos] = rainbow[(pos + start) % ledCount]
	np.write()
	
delay = 0
offset = 0
while True:
	write_rainbow(offset)
	offset = (offset + 1) % ledCount
	sleep(delay)
