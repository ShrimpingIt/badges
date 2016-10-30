#!/bin/sh
killall screen
esptool.py --port /dev/ttyUSB0 erase_flash
sleep 3
#BASENAME=esp8266-20160503-v1.8.bin
#BASENAME=esp8266-20160603-v1.8.1.bin
#BASENAME=esp8266-20160710-v1.8.2.bin
#BASENAME=esp8266-20160809-v1.8.3.bin
#BASENAME=esp8266-20160909-v1.8.4.bin
BASENAME=esp8266-20161017-v1.8.5.bin
esptool.py --port /dev/ttyUSB0 --baud 115200 write_flash --flash_mode dio --flash_size=32m 0 `dirname $0`/firmware/${BASENAME}


