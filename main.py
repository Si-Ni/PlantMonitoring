from utils.get_sensor_pins import get_pin2sensor
from sensors.sensors_builder import create_sensors

sensors = create_sensors(get_pin2sensor())

temperature = sensors[0]['sensor'].temperature
humidity = sensors[1]['sensor'].humidity




print(temperature, humidity)
