

import network
from machine import I2C
from machine import Pin
from ssd1306 import SSD1306_I2C
import time


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


def start_oled(config):
  i2c = I2C(scl=Pin(5), sda=Pin(2))
  oled = SSD1306_I2C(128, 64, i2c)
  oled.text('IP adress:', 0, 0)
  oled.text(config['ip'], 0, 16)
  oled.text('Gate way:', 0, 32)
  oled.text(config['gw'], 0, 48)
  oled.show()

def start():
  config = get_network()
  start_oled(config)


