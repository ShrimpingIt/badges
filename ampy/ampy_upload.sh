#!/bin/sh
MAIN=$1
CURRENT=`dirname $0`
AMPY="ampy --port /dev/ttyUSB0"
"${CURRENT}"/ampy_clean.sh
# send the new main.py file
${AMPY} put "${MAIN}" main.py
# reset the board so it runs the new main.py file
${AMPY} reset
