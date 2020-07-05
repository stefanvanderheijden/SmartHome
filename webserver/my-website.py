from flask import Flask, render_template
import RPi.GPIO as GPIO
import Adafruit_DHT as dht

app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

DHT22_pin = 4


@app.route("/")

def main():
   return render_template('main.html')

# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<pin>/<action>")
def action(pin, action):
   temperature = ''
   humidity = ''

   if pin == "dhtpin" and action == "get":
      humi, temp = dht.read_retry(dht.DHT22, DHT22_pin)  # Reading humidity and temperature

      h1, t1 = dht.read_retry(dht.DHT22, 4)
      h2, t2 = dht.read_retry(dht.DHT22, 5)
      h3, t3 = dht.read_retry(dht.DHT22, 26)

      h1 = round(h1, 2)
      t1 = round(t1, 2)

      h2 = round(h2, 2)
      t2 = round(t2, 2)

      h3 = round(h3, 2)
      t3 = round(t3 ,2)

      temperature = 'Temperature: ' + temp 
      humidity =  'Humidity: ' + humi

   templateData = {
   't1' : temperature,
   'h1' : humidity
   }

   return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)