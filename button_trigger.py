# 电容按钮识别
import time

from machine import Pin


def get_button_signal():
    pin = Pin(4, Pin.IN)
    while True:
        if pin.value() == 1:
            print("button pressed")
            time.sleep(1)


# 判断是否按住按钮1秒后松开
def get_button_pressed_1s_signal():
    pin = Pin(5, Pin.IN)
    # 计时器
    time_sec = 0;
    while True:
        # 如果是高电平，说明是按下按钮状态，此时判断计时器是否为0，
        # 如果为0 说明是从按钮未按下状态过来的，这时候，初始化计时器时间未当前时间（秒）
        # 否则说明之前的状态也是按下状态，不需要重置计时器
        if pin.value() == 1:
            if time_sec == 0:
                time_sec = time.time();
        # 如果是低电平说明是未按下状态，判断如果计时器为0，说明之前的状态也是未按下，什么都不做
        # 如果计时器大于0，说明之前按钮是按下状态，也就是从按下状态到松开状态，那么这时候需要计算按下了多长时间
        # 也就是用当前时间减去计时器开始的时间（第一次检测到按下按钮（高电平）时的时间）如果时间大约1秒，说明是长按，否则就是普通按下。
        # 由于是松开按钮，最后将计时器归0
        elif pin.value() == 0:
            if time_sec > 0:
                if time.time() - time_sec >= 1:
                    print("button pressed 1 sec")
                else:
                    print("button pressed")
                time_sec = 0;
            else:
                pass


get_button_pressed_1s_signal()
