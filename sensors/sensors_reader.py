import time
from utils.generate_dto_azure import generate_dto_azure


def read_sensors(config, sensors):
    retry_attempts = config["sensors"]["retry_attempts"]
    plant = config["plant"]["name"]
    sensors_dto = generate_dto_azure(plant)
    for sensor in sensors:
        try_reading_sensor(sensor, retry_attempts, sensors_dto, plant)
    return sensors_dto


def try_reading_sensor(sensor, retries, sensors_dto, plant):
    value = None
    for attempt in range(1, retries + 1):
        try:
            value = sensor["sensor_obj"].read()
            if value is not None:
                sensors_dto[plant]["sensors"].append(
                    {"type": sensor["name"], "value": value, "unit": sensor["unit"]}
                )
                break
            else:
                time.sleep(1)
        except Exception:
            time.sleep(1)
    if value is None:
        raise Exception(f"Reading sensor '{sensor['name']}' failed")
