from .sensor import Sensor
import Adafruit_BMP.BMP085 as BMP085


class PressureSensor(Sensor):
    def __init__(self, pin):
        super().__init__(pin)
        self.sensor = BMP085.BMP085(busnum=1)

    def read(self):
        return self.sensor.read_pressure()
