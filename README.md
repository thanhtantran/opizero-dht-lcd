# opizero-dht-lcd
Orange PI zero with DTH diplay on lcdusb

This code use LCD2USB lib from here https://github.com/thanhtantran/lcd2usb, and DHT library from here https://github.com/thanhtantran/DHT11-Python-library-Orange-PI

To run it you must install the orange pi python gpio from here https://github.com/thanhtantran/orangepi_python_gpio

    apt-get install build-essential python3-dev python3-pip
    git clone https://github.com/thanhtantran/orangepi_python_gpio
    cd orangepi_python_gpio
    python3 setup.py install 
    
then come back to this code and run

    python3 go.py

setup crontab to run it every minute 

    crontab -e
    */1 * * * * python3 /root/zero-dht-lcd/go.py
