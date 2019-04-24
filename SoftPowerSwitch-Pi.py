#!/bin/python

import RPi.GPIO as GPIO
import time
import os

GPIO_SHUTDOWN_DET = 3
TIMEOUT_REBOOT    = 0.5
TIMEOUT_SHUTDOWN  = 3.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_SHUTDOWN_DET, GPIO.IN, pull_up_down = GPIO.PUD_UP)


def checkShutdown(gpio):
    start = time.time()

    while time.time() < start + TIMEOUT_SHUTDOWN:
        inp = GPIO.input(gpio)
        if inp == GPIO.HIGH:
            if time.time() > start + TIMEOUT_REBOOT:
                print("reboot !!")
                os.system("sudo reboot")
            return
        time.sleep(0.01)

    print("shutdown now !!")
    os.system("sudo shutdown -h now")

#GPIO.add_event_detect(GPIO_SHUTDOWN_DET, GPIO.FALLING, callback = checkShutdown, bouncetime=100)

while True:
    GPIO.wait_for_edge(GPIO_SHUTDOWN_DET, GPIO.FALLING)
    checkShutdown(GPIO_SHUTDOWN_DET)
