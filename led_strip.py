# ws2812b灯带跑马灯
import time

import machine
import neopixel


def init_leds():
    num = 30;
    np = neopixel.NeoPixel(machine.Pin(5), num)
    while True:
        for i in range(num):
            np[(29 + i) % 30] = (0, 0, 0)
            np[i % 30] = ((i % 30 + 1) * 8, 0, 0)
            time.sleep(0.05)
            np.write()


init_leds()
