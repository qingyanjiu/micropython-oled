# 电容按钮识别
import time

from machine import Pin


def get_button_signal():
    pin = Pin(4, Pin.IN)
    while True:
        if pin.value() == 1:
            print("button pressed")
            time.sleep(1)


get_button_signal()
