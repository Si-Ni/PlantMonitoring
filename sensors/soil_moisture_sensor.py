import numpy as np
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from .sensor import Sensor

class SoilMoistureSensor(Sensor):
    def __init__(self, pin):
        super().__init__(pin)
        
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
		
        self.sensor = AnalogIn(ads, ADS.P0)

    def read(self):
		# Even in a glass of water I couldn't reach a voltage of 0V, so it starts at 0.5V
        moisture = np.interp(self.sensor.voltage, [0.5, 3.3], [100, 0])
        return float(f"{moisture:.2f}")

