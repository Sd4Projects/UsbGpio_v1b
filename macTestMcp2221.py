#!/Library/Frameworks/Python.framework/Versions/3.12/bin/python3

# This program released under OHL Version 1.2

# pip3 install adafruit-blinka
# pip3 install adafruit-circuitpython-mcp230xx
# pip3 install adafruit-circuitpython-ads1x15
# pip3 install adafruit-circuitpython-ssd1306
# Install missing font, font5x8.bin from github
# https://github.com/adafruit/Adafruit_CircuitPython_framebuf/blob/master/examples/font5x8.bin
# font5x8.bin must same be in the same directory as program to use adafruit_ssd1306

import os
os.environ['BLINKA_MCP2221'] = '1'
os.environ['BLINKA_MCP2221_RESET_DELAY'] = '0.5'
import sys
import time
import math
import board
import digitalio
import adafruit_ssd1306
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from adafruit_mcp230xx.mcp23008 import MCP23008

button = digitalio.DigitalInOut(board.G0)   # not used
button.direction = digitalio.Direction.INPUT

i2c = board.I2C()

# NTC convert parts
R1 = 10000
Vcc = 3.31
Bc = 3950
Tnom = 25
Rntc = 10000

ads = ADS.ADS1115(i2c)                       # 0x48
time.sleep(0.1)                              # wait for setup to finish
adsChan2 = AnalogIn(ads, ADS.P2)             # NTC 10K Therm
mcp = MCP23008(i2c)                          # 0x20

oled = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3d)
oled.fill(0)
oled.show()

while True:
    Vr2 = adsChan2.voltage
    R2 = Vr2*R1/(Vcc-Vr2)
    steinhart = R2 / Rntc
    steinhart = math.log(steinhart)
    steinhart /= Bc
    steinhart += 1 / (Tnom + 273.15)
    steinhart = 1 / steinhart
    steinhart -= 273.15
    print("C Temp Is: {0:.3f}".format(steinhart))
    gCTempIs = steinhart

    pin6 = mcp.get_pin(6)                        # Switch Test
    pin6.direction = digitalio.Direction.INPUT
    pin6.pull = digitalio.Pull.UP
    switchIs = pin6.value
    pin7 = mcp.get_pin(7)                        # LED Test
    pin7.direction = digitalio.Direction.OUTPUT
    pin7.value = True                            # Turn on LED

    oled.fill(0)
    showText1 = "Ctemp {0:.3f}".format(gCTempIs)
    oled.text(showText1, 30, 10, 1)              # H , V , 1=ON
    if switchIs is True:                         # 1 = Off, 0 = On , pin has pullup
        showText2 = "Switch Off"
    else:
        showText2 = "Switch On "
    oled.text(showText2, 35, 30, 1)              # H , V , 1=ON
    oled.show()

    time.sleep(0.5)
    if switchIs is False:
        pin7.value = False                       # Turn LED off
        oled.text("Done", 50, 50, 1)
        oled.show()
        print("Done")
        sys.exit(0)
