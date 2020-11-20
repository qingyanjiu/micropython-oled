import time

import dht
import network
from machine import I2C
from machine import Pin

from ssd1306 import SSD1306_I2C


def get_temp_humi():
    d = dht.DHT11(Pin(5))
    d.measure()
    temp = d.temperature()  # eg. 23 (閹虹煰)
    humi = d.humidity()  # eg. 41 (% RH)
    return {'temp': temp, 'humi': humi}


def get_network():
    ssid = 'louis_n'
    passwd = '19831226lc'
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.disconnect()
    wlan.connect(ssid, passwd)
    while not wlan.isconnected():
        time.sleep(1)
    ip, mask, gateway, dns = wlan.ifconfig()
    config = {'ip': ip, 'mask': mask, 'gw': gateway, 'dns': dns}
    return config


def show_wifi_text(config, oled):
    oled.text('IP adress:', 0, 0)
    oled.text(config['ip'], 0, 16)
    oled.text('Gate way:', 0, 32)
    oled.text(config['gw'], 0, 48)


def show_temp_humi_text(temp_humi, oled):
    oled.text('Temperature:', 0, 0)
    oled.text(str(temp_humi['temp']) + ' C', 0, 16)
    oled.text('Humidity:', 0, 32)
    oled.text(str(temp_humi['humi']) + '%', 0, 48)


def init_oled():
    i2c = I2C(scl=Pin(14), sda=Pin(2))
    oled = SSD1306_I2C(128, 64, i2c)
    return oled
    
 
def display(oled, wifi_data, temp_humi_data):
    oled.fill(0x00)
    if wifi_data:
        show_wifi_text(wifi_data, oled)
    elif temp_humi_data:
        show_temp_humi_text(temp_humi_data, oled)
    oled.show()
  

def start():
    # config = get_network()
    # start_oled(wifi_data=config, temp_humi_data=None)
    oled = init_oled()
    while True:
        tm = get_temp_humi()
        display(oled, wifi_data=None, temp_humi_data=tm)
        time.sleep(10)



