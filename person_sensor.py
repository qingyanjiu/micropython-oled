import time

from machine import Pin


def exist_person():
    # 输入引脚，HC-SR501的高低电平输入，判断是否有人经过
    p = Pin(13, Pin.IN)
    return p.value()


while True:
    v = exist_person()
    if v == 1:
        print('Person!')
    time.sleep(5)
