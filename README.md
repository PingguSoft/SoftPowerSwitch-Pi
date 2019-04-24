# SoftPowerSwitch-Pi

## soft power switch for raspberry pi
original article : https://othermod.com/raspberry-pi-soft-onoff-circuit/

![pic](https://github.com/PingguSoft/SoftPowerSwitch-Pi/blob/master/rpi_soft_onoff_MOSFET-DIAGRAM-WITH-DIODE.png?raw=true?raw=true)

### changes
TXD PIN is GPIO14 so its default state is not pull-up at boot time, so it is changed to GPIO4
**GPIO0 ~ GPIO8 : pull-up at boot time, GPIO9 ~ GPIO27 : pull-down at boot time**

To turn it off at shutdown, add below line to config.txt
**dtoverlay=gpio-poweroff,gpiopin=4,active_low="y",export="y"**

### shutdown detection (2 methods are possible)
1. add **power-switch** key for GPIO3
  add **dtoverlay=gpio-shutdown,gpio_pin=3** to config.txt
  if the shutdown button is clicked, shutdown will be executed immediately

2. determine **reset** and **shutdown** event with python script
  **shutdown** if the button is pressed over 3 sec
  **reboot** if the button is pressed over 0.5 sec


