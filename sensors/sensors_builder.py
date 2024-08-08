from .temperature_sensor import create_temperature_sensor
from .humidity_sensor import create_humidity_sensor

def create_sensors(sensor_config):
	sensors = []
	for sensor, config in sensor_config.items():
		sensors.append({ 
			'name': sensor, 
			'sensor': build_sensor(sensor, config['pin'])
		})
	return sensors

def build_sensor(sensor_name, pin):
	if sensor_name == 'temperature_sensor':
		return create_temperature_sensor(pin)
	elif sensor_name == 'humidity_sensor':
		return create_humidity_sensor(pin)
	else:
		raise ValueError(f"Invalid sensor name: {sensor_name}")
	
