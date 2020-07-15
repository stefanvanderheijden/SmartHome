import RPi.GPIO as GPIO
import Adafruit_DHT as dht

import os
import time 
from time import sleep
from datetime import datetime

file = open("/home/pi/Documents/Script/Data/data_log.csv", "a")
print("opened file")

if os.stat("/home/pi/Documents/Script/Data/data_log.csv").st_size == 0:
   print("added headers to data log file")
   file.write("Tijd,BuitenTemp,BuitenLuchtV,HuiskamerTemp,HuiskamerLuchtV,KantoorTemp,KantoorLuchtV\n")

GPIO.setmode(GPIO.BCM)

DHT22_pin = 4

while True:
    try: 
        h1, t1 = dht.read_retry(dht.DHT22, 4)
        h2, t2 = dht.read_retry(dht.DHT22, 5)
        h3, t3 = dht.read_retry(dht.DHT22, 26)

        h1 = round(h1, 2)
        t1 = round(t1, 2)

        h2 = round(h2, 2)
        t2 = round(t2, 2)

        h3 = round(h3, 2)
        t3 = round(t3 ,2)

        now = datetime.now()
        file.write(str(now)+","+str(t1)+","+str(h1)+","+str(t2)+","+str(h2)+","+str(t3)+","+str(h3)+"\n")
        print("I have logged the temperature to a CSV file")
        time.sleep(5)
    
    except KeyboardInterrupt:
        print "Bye"
        file.close
        sys.exit()