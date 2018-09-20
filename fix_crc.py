#!/bin/python3

import crc16
import sys


def usage():
    print("Usage: {} ../path/to/FW.bin".format(sys.argv[0]))
    exit(1)


if len(sys.argv) < 2:
    print("supply the FW file path")
    usage()

try:
    f = open(sys.argv[1], 'rb+')
except FileNotFoundError:
    print("file path incorrect")
    usage()

fw = f.read()
sum = crc16.crc16xmodem(fw[:-2]).to_bytes(length=2, byteorder="big")
print("CRC16 of the FW is 0x{}".format(sum.hex()))

if fw.endswith(sum):
    print("FW has correct CRC")
else:
    f.seek(-2, 2)
    f.write(sum)
    print("Fixed incorrect CRC")

f.close()
