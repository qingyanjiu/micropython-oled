import oled_and_temp
import time

def start():
    # config = get_network()
    # start_oled(wifi_data=config, temp_humi_data=None)
    oled = oled_and_temp.init_oled()
    while True:
        tm = oled_and_temp.get_temp_humi()
        oled_and_temp.display(oled, wifi_data=None, temp_humi_data=tm)
        time.sleep(300)


