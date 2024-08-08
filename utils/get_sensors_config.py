import json
import os
from .string2pin import get_gpio_pin


def load_sensors_config(file_path="configs/sensors_config.json"):
    with open(file_path, "r") as file:
        return json.load(file)


def get_sensors_config():
    sensors_config = load_sensors_config()

    for sensor, config in sensors_config.items():
        pin_name = config["pin"]
        pin_object = get_gpio_pin(pin_name)
        config["pin"] = pin_object

    return sensors_config
