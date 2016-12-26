from time import sleep
from neopixel import NeoPixel
from machine import Pin

dataPin = Pin(4)
ledCount = 64
np = NeoPixel(dataPin, ledCount)

fontColumns = [95,95,3,3,0,0,3,3,20,127,127,20,20,127,127,20,36,46,107,107,58,18,99,51,24,12,102,99,50,127,77,77,119,114,80,4,6,3,1,28,62,99,65,65,99,62,28,8,42,62,28,28,62,42,8,8,8,62,62,8,8,128,224,96,8,8,8,8,8,8,96,96,64,96,48,24,12,6,2,62,127,73,69,127,62,64,68,127,127,64,64,98,115,81,73,79,70,34,99,73,73,127,54,24,24,20,22,127,127,16,39,103,69,69,125,57,62,127,73,73,123,50,3,3,121,125,7,3,54,127,73,73,127,54,38,111,73,73,127,62,99,99,128,227,99,8,28,54,99,65,65,20,20,20,20,20,20,65,65,99,54,28,8,2,3,81,89,15,6,62,127,65,77,79,46,124,126,11,11,126,124,127,127,73,73,127,54,62,127,65,65,99,34,127,127,65,99,62,28,127,127,73,73,65,65,127,127,9,9,1,1,62,127,65,73,123,58,127,127,8,8,127,127,65,127,127,65,32,96,65,127,63,1,127,127,28,54,99,65,127,127,64,64,64,64,127,127,6,12,6,127,127,127,127,14,28,127,127,62,127,65,65,127,62,127,127,9,9,15,6,30,63,33,97,127,94,127,127,25,57,111,70,38,111,73,73,123,50,1,1,127,127,1,1,63,127,64,64,127,63,31,63,96,96,63,31,127,127,48,24,48,127,127,99,119,28,28,119,99,7,15,120,120,15,7,97,113,89,77,71,67,127,127,65,65,2,6,12,24,48,96,64,65,65,127,127,4,6,127,127,6,4,64,64,64,64,64,64,64,64,1,3,6,4,32,116,84,84,124,120,126,126,72,72,120,48,56,124,68,68,68,48,120,72,72,126,126,56,124,84,84,92,24,8,124,126,10,10,152,188,164,164,252,124,127,127,4,4,124,120,68,125,125,64,128,128,250,122,127,127,16,56,104,64,65,127,127,64,124,124,24,56,28,124,120,124,124,4,4,124,120,56,124,68,68,124,56,252,252,36,36,60,24,24,60,36,36,252,252,124,124,4,4,12,8,72,92,84,84,116,36,4,4,62,126,68,68,60,124,64,64,124,124,28,60,96,96,60,28,28,124,112,56,112,124,28,68,108,56,56,108,68,156,188,160,224,124,60,68,100,116,92,76,68,8,8,62,119,65,65,127,127,65,65,119,62,8,8]
fontOffsets = [0, 2, 8, 16, 22, 28, 35, 39, 43, 47, 55, 61, 64, 70, 72, 79, 85, 91, 97, 103, 110, 116, 122, 128, 134, 140, 142, 145, 151, 157, 163, 169, 175, 181, 187, 193, 199, 205, 211, 217, 223, 227, 233, 239, 245, 252, 258, 264, 270, 276, 282, 288, 294, 300, 306, 313, 319, 325, 331, 335, 342, 346, 352, 360, 364, 370, 376, 381, 387, 393, 398, 404, 410, 414, 418, 424, 428, 435, 441, 447, 453, 459, 465, 471, 477, 483, 489, 496, 502, 508, 514, 520, 522, 528]

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
intensity = 0.1

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
		np[pos]=black
	np.write()

def get_columns(letter):
	letterIndex = -33 + ord(letter)
	startColumn = fontOffsets[letterIndex]
	endColumn = fontOffsets[letterIndex+1]
	return fontColumns[startColumn:endColumn]
	
def get_bits(column):
	return [(column & 1<<pos) != 0 for pos in range(8) ]
	
def set_pixel(x,y,color,write=True):
	np[(y*8) + x] = color
	if write:
		np.write()

def writeLetter(letter, color=white):
	for x,column in enumerate(get_columns(letter)):
		for y, bit in enumerate(get_bits(column)):
			if bit:
				set_pixel(x,y,color,False)

saturation = 1
brightness = 1
rainbow = [hsb(hue, saturation, brightness) for hue in [x / ledCount for x in range(ledCount)]]

def write_rainbow(start=0):	
	for pos in range(ledCount):
		np[pos] = rainbow[(pos + start) % ledCount]
	
message = "Light Up Lancaster"
letterCount = len(message)
tick = 0
delay = 0
messageOffset = 0
while True:
	write_rainbow(tick % ledCount)
	letterTick = tick // 4
	wordTick = letterTick // letterCount
	if(wordTick % 4 == 0):
		writeLetter(message[letterTick % letterCount], (64,64,64))
	np.write()
	tick += 1
	sleep(delay)
