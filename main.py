from utils.get_sensor_pins import get_pin2sensor
from sensors.sensors_builder import create_sensors

create_sensors(get_pin2sensor())
