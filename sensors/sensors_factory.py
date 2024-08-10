from .temperature_sensor import TemperatureSensor
from .humidity_sensor import HumiditySensor
from .pressure_sensor import PressureSensor
from .light_intensity_sensor import LightIntensitySensor


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
    sensor_types = {
        "temperature": TemperatureSensor,
        "humidity": HumiditySensor,
        "pressure": PressureSensor,
<<<<<<< Updated upstream
=======
        "light_intensity": LightIntensitySensor
>>>>>>> Stashed changes
    }
    if sensor_name in sensor_types:
        return sensor_types[sensor_name](pin)
    else:
        raise ValueError(f"Invalid sensor name: {sensor_name}")
