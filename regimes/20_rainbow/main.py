import webrepl
webrepl.start(password='shrimping')

from time import sleep
from neopixel import NeoPixel
from machine import Pin

global np, count, default_color
count = None
default_color = None

def init_pixel_count(num):
	global count
	count = num

def init_star():
	init_pixel_count(7)

def init_line():
	init_pixel_count(8)
	
def init_grid():
	init_pixel_count(64)

init_grid()
default_color = (64,64,0)
np = NeoPixel(Pin(4), count)

def wheel(wheelByte):
    wheelByte = 255 - wheelByte
    if wheelByte < 85:
        return (255 - wheelByte * 3, 0, wheelByte * 3)
    if wheelByte < 170:
        wheelByte = wheelByte - 85
        return (0, wheelByte * 3, 255 - wheelByte * 3)
    wheelByte = wheelByte - 170
    return (wheelByte * 3, 255 - wheelByte * 3, 0)

def blank():
	global count
	for pixel_id in range(0, count):
		np[pixel_id] = (0,0,0)
	np.write()
    
def star_fortune(step = 0.1):
	global count, default_color
	blank()
	
	lit_pixel = 0
	offset_count = count - 1
	while True:
		#Iterate over each LED in the strip
		for pixel_id in range(0, offset_count):
			if pixel_id == lit_pixel:
				np[pixel_id + 1] = default_color
			else:
				np[pixel_id + 1] = (0,0,0)

		# Display the current pixel data on the Neopixel strip
		np.write()
		
		lit_pixel = (lit_pixel + 1) % count

		sleep(step)

def rainbow_cycle(step=0.01, brightness=0.25, spread=32):
	global count
	blank()
	wheelPos = 0
	while True:
		#Iterate over each LED in the strip
		for pixel_id in range(0, count):
			# Assign the current LED a color value from the rainbow sequence, with current offset
			color = wheel((wheelPos + (pixel_id * spread )) % 255)
			color = [int(val * brightness) for val in color]
			np[pixel_id] = color
		# Display the current pixel data on the Neopixel strip
		np.write()
		wheelPos = (wheelPos + 1) % 255
		sleep(step)
		
def drop():
	for pos in range(count):
		blank()
		np[pos] = (0,0,255)
		np.write()
		sleep(0.1)

rainbow_cycle()
