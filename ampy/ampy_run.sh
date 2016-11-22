#!/bin/sh
killall screen
ampy --port /dev/ttyUSB0 run `dirname $0`/../regimes/blank_display/main.py
ampy --port /dev/ttyUSB0 run ./main.py
