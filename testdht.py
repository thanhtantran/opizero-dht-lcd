#!/usr/bin/env python
# encoding: utf8

'''test dht
    Author: Tran Thanh Tan
'''


from pyA20.gpio import gpio
from pyA20.gpio import port
from influxdb import InfluxDBClient

import dht11
from time import time
import pdb
import random
#initialize GPIO
PIN2 = port.PA6
gpio.init()

#read data using pin port.PA6
instance = dht11.DHT11(pin=PIN2)
result = instance.read()

db = InfluxDBClient("localhost", 8086)
db.switch_database("default")

if result.is_valid():
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
    json = [{
      "measurement": "temperature",
      "time": int(time()) * 1000000000,
      "fields": {
        "temp": result.temperature
      }
    },   
    {
      "measurement": "humidity",
      "time": int(time()) * 1000000000,
      "fields": {
        "humid": result.humidity
      }
    }]
    db.write_points(json)    
else:
    print("Error: %d" % result.error_code)