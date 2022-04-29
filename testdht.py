from pyA20.gpio import gpio
from pyA20.gpio import port

import dht11
#initialize GPIO
PIN2 = port.PA6
gpio.init()

#read data using pin port.PA6
instance = dht11.DHT11(pin=PIN2)
result = instance.read()

if result.is_valid():
    print("Temperature: %d C" % result.temperature)
    print("Humidity: %d %%" % result.humidity)
else:
    print("Error: %d" % result.error_code)