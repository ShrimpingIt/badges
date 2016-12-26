#!/bin/sh
CURRENT=`dirname $0`
AMPY="ampy --port /dev/ttyUSB0"
"${CURRENT}"/ampy_release.sh
"${CURRENT}"/../micropython/upload_image.sh
# blank the display (so people aren't confused and don't have to depower)
${AMPY} run "${CURRENT}"/../regimes/99_blank_display/main.py
