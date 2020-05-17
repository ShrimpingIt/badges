from machine import Pin
from time import sleep

pins = [
    Pin(16),
    Pin(5),
    Pin(4),
    Pin(0),
    Pin(2),
    Pin(14),
    Pin(12),
    Pin(13),
    Pin(15),
    Pin(3),
    Pin(1),
]

byteCount = 1


dataPin = pins[1]
latchPin = pins[2]
clockPin = pins[3]

dataPin.init(Pin.OUT)
latchPin.init(Pin.OUT)
clockPin.init(Pin.OUT)

dataPin.low()
latchPin.low()
clockPin.low()

backBytes = [0 for pos in range(byteCount)]

def latchBytes():
    latchPin.high()
    latchPin.low()

def writeByte(val, latch=True):
    bit = 1
    for step in range(8):
        if val & bit != 0:
            dataPin.high()
        else:
            dataPin.low()
        clockPin.high()
        clockPin.low()
        bit = bit << 1
    if latch:
        latchBytes()
        
def sendLights():
    for pos in range(len(backBytes)):
        writeByte(backBytes[pos], False)
    latchBytes()

def setLight(pos, lit, send=True):
    bytePos = pos // 8
    bitPos = pos % 8
    if lit:
        backBytes[bytePos] = backBytes[bytePos] | (1 << bitPos)
    else:
        backBytes[bytePos] = backBytes[bytePos] & ~(1 << bitPos)
    if send:
		sendLights()

def turnOff(lights):
    for pos in range(len(lights)):
        setLight(lights[pos], 0)

def sequence(lights, delay=0.1, count=1):
    while True:
        for outer in range(len(lights)):
            for inner in range(len(lights)):
                setLight(pos=lights[inner], lit=(inner==outer), send=False)
            sendLights()
            sleep(delay)


doSend()
