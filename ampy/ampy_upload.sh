#!/bin/sh
killall screen
`dirname $0`/../micropython/upload_image.sh
sleep 3
ampy --port /dev/ttyUSB0 run `dirname $0`/blank_display/main.py
ampy --port /dev/ttyUSB0 put ./main.py
ampy --port /dev/ttyUSB0 reset
