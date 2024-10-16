# UsbGpio

TK

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
1. MCP23008 chip via I2C interface
2. Two GPIO pins driving 2N7002 Mosfets for output.
3. I2C lines to a JST_SH Connector
4. UART (Serial) lines to a JST_SH Connector
5. Terminal to supply external 5 volts

All data lines use 4-pin Qwiic/JST_SH connectores.
