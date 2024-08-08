import adafruit_dht

def create_humidity_sensor(pin):
	return adafruit_dht.DHT11(pin)
