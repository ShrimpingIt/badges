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

pins[0].init(Pin.OUT)
pins[1].init(Pin.OUT)
pins[2].init(Pin.OUT)
pins[3].init(Pin.OUT)
pins[4].init(Pin.OUT)
pins[5].init(Pin.OUT)
pins[6].init(Pin.OUT)
pins[7].init(Pin.OUT)

pins[0].high()
