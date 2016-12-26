from neopixel import NeoPixel
from machine import Pin
from time import sleep

black = (0,0,0)
white = (255,255,255)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

yellow = (255,255,0)
purple = (255,0,255)
teal = (0,255,255)

def startPixels(newPixelCount = 8, newPinNumber = 4):
	global pixels, pixelCount
	pixelCount = newPixelCount
	outputPin = Pin(newPinNumber)
	pixels = NeoPixel(outputPin, pixelCount)

def blankPixels():
	global pixels, pixelCount
	for pixelNumber in range(pixelCount):
		pixels[pixelNumber]=black
	pixels.write()	
	
def setPixel(pixelNumber, pixelColor):
	global pixels
	pixels[pixelNumber]=pixelColor
	pixels.write()

startPixels()
