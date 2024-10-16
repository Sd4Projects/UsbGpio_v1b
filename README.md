# UsbGpio

Gpio pins via USB for some systems (Mac, MiniPC, etc) that do not have gpio support.
If you only need a few gpio pins you may want to check out the Adafruit MCP2221 Breakout board Product ID: 4471.

Licensed under CERN OHL v.1.2 (Open Hardware Licence)

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

Python 3 test program for a Mac: macTestMcp2221.py There are python libraries for other types of systems.
