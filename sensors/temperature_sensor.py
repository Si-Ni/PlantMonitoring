import adafruit_dht

def create_temperature_sensor(pin):
	return adafruit_dht.DHT11(pin)
