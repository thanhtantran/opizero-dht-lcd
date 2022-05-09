#!/usr/bin/env python
# encoding: utf8

'''opizero-dht-lcd
    Author: Tran Thanh Tan
'''

from pyA20.gpio import gpio
from pyA20.gpio import port
from lcd2usb import LCD
from influxdb import InfluxDBClient

#import RPi.GPIO as GPIO
import dht11
from time import time
import pdb
import random

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

db = InfluxDBClient("localhost", 8086)
db.switch_database("default")

if result.is_valid():
  json = [{
    "measurement": "temperature",
    "time": int(time()) * 1000000000,
    "fields": {
      "temp": result.temperature,
      "location": "default"
    }
  },
  {
    "measurement": "humidity",
    "time": int(time()) * 1000000000,
    "fields": {
      "humid": result.humidity,
      "location": "default"
    }
  }]
  db.write_points(json)

  try:
    lcd = LCD.find_or_die()
    lcd.info()
    lcd.fill("Nhiet do: %d oC" % result.temperature, 0)
    lcd.fill("Do am: %d %%" % result.humidity, 1)
  except:
   print ('Error!')    

else:
    try:
      lcd = LCD.find_or_die()
      lcd.info()
      lcd.fill("Error: %d" % result.error_code, 0)
    except:
     print ('Error!')          