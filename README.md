# Nikon D200 firmware reverse engineering
Here I'm sharing my findings while reverse engineering the FW and utils I come up with.
Bear in mind I'm a complete newbie to RE. Everyone is welcome to contribute.

# What's currently known about the FW
[incomplete]
Nikon provides these 2 firmware update files (in case of [v2.01](https://downloadcenter.nikonimglib.com/en/products/10/D200.html)):
- A2000201.bin
  - apparently, this is for a Renesas 32bit CPU, that runs a [HI8-2600](http://www.ertl.jp/ITRON/Newsletter-E/itronnews28-e.html) µITRON-specification RTOS
  - interfaces with the hardware
- B2000201.bin
  - this is for a modified version of Fujitsu FR-V, that runs a [Softune](https://en.wikipedia.org/wiki/Softune) RTOS
  - does all the menu UI stuff
  - 0x1ea651 contains the "Firmware Version" UTF string (modifications show up in the menu)
  - IDA does have a Fujitsu FR disassembler and discovers a few functions and register modifications but I haven't looked into them deeply
#### Resources
1. https://www.flickr.com/groups/64315324@N00/discuss/72157606076114795/72157623050785197
2. https://nikonhacker.com/wiki/Understanding_Firmware#The_.22B.22_microcontroller
3. [v2.01 FW](https://downloadcenter.nikonimglib.com/en/products/10/D200.html)
4. [v2.00 FW](https://drivers.softpedia.com/get/FIRMWARE/Others/Nikon-D200-Firmware-20.shtml)

# Utils overview
1. fix_crc.py
    - the last 2 bytes of the B2000201.bin & B2000200.bin FW update binaries is CRC16-CCITT (a.k.a. xmodem) of the whole file
    - calculates the CRC and updates it if it's incorrect
    - usage: `$ fix_crc.py ../FW/B2000201.bin`
    - depends on [crc16](https://pypi.org/project/crc16/)

2. something's coming...
