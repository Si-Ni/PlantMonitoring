from utils.generate_dto_azure import generate_dto_azure

sensors_dto = generate_dto_azure()

def read_sensors(sensors, retries):
	for sensor in sensors:
		
		try_reading_sensor(sensor, retries)
		
		if sensor["value"] is None:
			raise Exception(f"Reading sensor: {sensor[name]} failed")

def try_reading_sensor(sensor, retries):
	for attempt in range(1, retries):
		try:
			value = sensor.read()
			
			if value is not None:
				sensors_dto["sensors"].append({
					"type": sensor["name"], "value": value, "unit": sensor[value]
				})
				break
		except Exception:
			
