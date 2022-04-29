#!/usr/bin/env python
# encoding: utf8

'''opizero-dht-lcd
    Author: Tran Thanh Tan
'''

from pyA20.gpio import gpio
from pyA20.gpio import port
from lcd2usb import LCD

#import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
#gpio.setwarnings(False)
#gpio.setmode(GPIO.BCM)
PIN2 = port.PA6
gpio.init()
#gpio.cleanup()


# read data using pin 14
instance = dht11.DHT11(pin=PIN2)
result = instance.read()
#while True:
#    result = instance.read()
#    if result.is_valid():
#        print("Last valid input: " + str(datetime.datetime.now()))
#        print("Temperature: %d C" % result.temperature)
#        print("Humidity: %d %%" % result.humidity)
#
#    time.sleep(1)

def main(lcd):
  lcd.hello()
  lcd.clear()
  lcd.home()

  if result.is_valid():
    lcd.fill("Nhiet do: %d oC" % result.temperature, 0)
    lcd.fill("Do am: %d %%" % result.humidity, 1)
  else:
    lcd.fill("Error: %d" % result.error_code, 0)
  
  return lcd

if __name__ == '__main__':
    lcd = LCD.find_or_die()
    lcd.info()
    try:
        main(lcd)
    except KeyboardInterrupt:
        pass
