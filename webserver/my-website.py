from flask import Flask, render_template
import RPi.GPIO as GPIO
import Adafruit_DHT as dht

import subprocess

import os
import time 
from time import sleep
from datetime import datetime

from multiprocessing import Process, Value

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

DHT22_pin = 4


@app.route("/")

def main():
   return render_template('main.html')

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<pin>/<action>")
def action(pin, action):
   print("A temperature request from the website")
   temperature = ''
   humidity = ''

   if pin == "dhtpin" and action == "get":
      h1, t1 = dht.read_retry(dht.DHT22, 4)
      h2, t2 = dht.read_retry(dht.DHT22, 5)
      h3, t3 = dht.read_retry(dht.DHT22, 26)

      h1 = round(h1, 2)
      t1 = round(t1, 2)

      h2 = round(h2, 2)
      t2 = round(t2, 2)

      h3 = round(h3, 2)
      t3 = round(t3 ,2)

      temperature1 = 'Temperatuur: ' + str(t1)  + u'\xb0' + "C"
      humidity1 =  'Luchtvochtigheid: ' + str(h1) + '%'

      temperature2 = 'Temperatuur: ' + str(t2)  + u'\xb0' + "C"
      humidity2 =  'Luchtvochtigheid: ' + str(h2) + '%'

      temperature3 = 'Temperatuur: ' + str(t3)  + u'\xb0' + "C"
      humidity3 =  'Luchtvochtigheid: ' + str(h3) + '%'

   templateData = {
   't1' : temperature1,
   'h1' : humidity1,
   't2' : temperature2,
   'h2' : humidity2,
   't3' : temperature3,
   'h3' : humidity3
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   print("running logging script")
   subprocess.call(["python","/home/pi/Documents/Script/webserver/logger.py"])
   print("starting flask server")
   app.run(host='0.0.0.0', port=80, debug=True)
   