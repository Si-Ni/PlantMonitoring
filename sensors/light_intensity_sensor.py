import smbus
from .sensor import Sensor

DEVICE_ADDRESS = 0x23

POWER_DOWN = 0x00
POWER_ON = 0x01
RESET = 0x07

CONTINUOUS_LOW_RES_MODE = 0x13
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
ONE_TIME_HIGH_RES_MODE_1 = 0x20
ONE_TIME_HIGH_RES_MODE_2 = 0x21
ONE_TIME_LOW_RES_MODE = 0x23

bus = smbus.SMBus(1)


class LightIntensitySensor(Sensor):
    def __init__(self, pin):
        super().__init__(pin)

    def convertToNumber(self, data):
        result = (data[1] + (256 * data[0])) / 1.2
        return result

    def read(self):
        data = bus.read_i2c_block_data(DEVICE_ADDRESS, ONE_TIME_HIGH_RES_MODE_1)
        light_intensity = self.convertToNumber(data)
        return float(f"{light_intensity:.2f}")
