from .temperature_sensor import TemperatureSensor
from .humidity_sensor import HumiditySensor


def build_sensors(sensor_config):
    sensors = []
    for sensor, config in sensor_config.items():
        sensors.append(
            {
                "name": sensor,
                "sensor_obj": create_sensor(sensor, config["pin"]),
                "unit": config["unit"],
            }
        )
    return sensors


def create_sensor(sensor_name, pin):
    if sensor_name == "temperature":
        return TemperatureSensor(pin)
    elif sensor_name == "humidity":
        return HumiditySensor(pin)
    else:
        raise ValueError(f"Invalid sensor name: {sensor_name}")
