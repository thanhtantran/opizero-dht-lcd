#!/usr/bin/env python
# encoding: utf8

'''opizero-dht-lcd
    Author: Tran Thanh Tan
'''

from pyA20.gpio import gpio
from pyA20.gpio import port
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

#import RPi.GPIO as GPIO
import dht11
from datetime import datetime

#cloud token
token = "3jl-yNsU2X1NvDGQBy7XAuCr_axI2JsmcLLHaZipmKTmPQS2iUj6P4KJ9ow3dPiazN-ulpvkBqQtET5R7Bfbvw=="
org = "thanhtan.tran@gmail.com"
bucket = "orangepizero"

PIN2 = port.PA6
gpio.init()
#gpio.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=PIN2)
result = instance.read()

#create client 
with InfluxDBClient(url="https://ap-southeast-2-1.aws.cloud2.influxdata.com", token=token, org=org) as client:
  if result.is_valid():
      write_api = client.write_api(write_options=SYNCHRONOUS)
      print("Temperature: %d C" % result.temperature)
      print("Humidity: %d %%" % result.humidity)
      point = Point("orangepizero") \
          .field("temp", result.temperature) \
          .field("humid", result.humidity) \
          .time(datetime.utcnow(), WritePrecision.NS)
  
      write_api.write(bucket, org, point)
      
  else:
      print("Error: %d" % result.error_code)
      
client.close()