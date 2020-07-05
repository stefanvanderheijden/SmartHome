#Trail script for DHT temp and moisture sensor

import Adafruit_DHT

h1, t1 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
h2, t2 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 5)
h3, t3 = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 26)

h1 = round(h1, 2)
t1 = round(t1, 2)

h2 = round(h2, 2)
t2 = round(t2, 2)

h3 = round(h3, 2)
t3 = round(t3 ,2)

print('Sensor One: Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t1,h1))
print('Sensor Two: Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(t2,h2))
print('Sensor Three: Temp={0:0.1f}*C Humidity={1:0.01f}%'.format(t3,h3))
