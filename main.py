from utils.get_sensors_config import get_sensors_config
from sensors.sensors_factory import build_sensors
from sensors.sensors_reader import read_sensors

sensors = build_sensors(get_sensors_config())
try:
    print(read_sensors(sensors, 5))
except Exception as error:
    print(error)
