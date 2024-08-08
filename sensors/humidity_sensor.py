from .sensor import Sensor
import adafruit_dht

class HumiditySensor(Sensor):
    def __init__(self, pin):
        super().__init__(pin)
        self.sensor = adafruit_dht.DHT11(pin)
        
    def read(self, retries):
        return self.sensor.humidity
