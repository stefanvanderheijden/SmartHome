


# Importing the flask module
from flask import Flask
import Adafruit_DHT

# Create a flask object named app
app = Flask(__name__)

# When someone will enter the IP address of Raspberry Pi in the browser, below code will run.
@app.route("/")
def main():
	h1, t1 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
	h2, t2 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 5)
	h3, t3 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 26)

	h1 = round(h1, 2)
	t1 = round(t1, 2)

	h2 = round(h2, 2)
	t2 = round(t2, 2)

	h3 = round(h3, 2)
	t3 = round(t3 ,2)

	return ('Sensor One: Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t1,h1))
	return "Test"
#if code is run from terminal
if __name__ == "__main__":
	# Server will listen to port 80 and will report any errors.
   app.run(host='0.0.0.0', port=80, debug=True)

