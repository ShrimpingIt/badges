from neopixel import NeoPixel
from machine import Pin
from time import sleep

count = 8

display = NeoPixel(Pin(4), count)

greenVals = [pos*255//count for pos in range(count)]
redVals = [(count - pos)*255//count for pos in range(count)]
blueVals = [0 for pos in range(count)]

offset = 0
while True:
    for pos in range(count):
        display[(pos + offset) % count] = (greenVals[pos], redVals[pos], blueVals[pos])
    display.write()
    sleep(0.05)
    offset = offset + 1
