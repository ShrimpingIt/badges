#!/bin/sh
MAIN=$1
CURRENT=`dirname $0`
AMPY="ampy --port /dev/ttyUSB0"
"${CURRENT}"/ampy_clean.sh
# run the file
"${AMPY}" run "${MAIN}"
