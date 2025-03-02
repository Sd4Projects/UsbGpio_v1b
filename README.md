# UsbGpio_v1b

Add gpio pins for (Mac, MiniPC, etc) via USB that do not have gpio pins to use.
If you only need a few gpio pins you may want to check out the Adafruit MCP2221 Breakout board Product ID: 4471.

UsbGpio board licensed under CERN OHL v.1.2 (Open Hardware Licence)

See CERN OHL v.1.2 for applicable conditions

http://ohwr.org/cernohl

USB Gpio Expansion board

Testing board design:

![alt text](https://github.com/Sd4Projects/UsbGpio/blob/main/UsbGpioTestSetup.png?raw=true "finishedboard")

Top view of board:

![alt text](https://github.com/Sd4Projects/UsbGpio/blob/main/UsbGpioTop.png?raw=true "TopView")

Bottom view of board:

![alt text](https://github.com/Sd4Projects/UsbGpio/blob/main/UsbGpioBot.png?raw=true "BottomView")

Schematic PDF file: UsbGpio_v1b.SCH.pdf

Board PDF file: UsbGpio_v1b.PCB.pdf

BOM PDF file: UsbGpio_v1b.BOM.pdf

Designed with KiCad Version 8.0.4

UsbGpio source files included.

UsbGpio board features:
1. Four 16bit AtoD lines using an ADS1115 chip via I2C interface
2. MCP23008 chip via I2C interface
3. Two GPIO pins driving 2N7002 Mosfets for output.
4. I2C lines to a JST_SH Connector
5. UART (Serial) lines to a JST_SH Connector
6. USB C connector, USB 2.0

All data lines use 4-pin Qwiic/JST_SH connectores.

Bare board can be ordered from: https://oshpark.com/shared_projects/wGhxM2sL

Python 3 test program run on a Mac from Terminal window: macTestMcp2221.py (There are python libraries for other types of systems.)

Parts used for testing:
1. 10K Precision Epoxy Thermistor - 3950 NTC From adafruit Product ID: 372
2. Monochrome 1.3" 128x64 OLED graphic display - STEMMA QT / Qwiic From adafruit Product ID: 938
3. Mini Panel Mount SPDT Toggle Switch From adafruit Product ID: 3221
4. STEMMA QT / Qwiic JST SH 4-Pin Cable - 50mm Long From adafruit Product ID: 4399
