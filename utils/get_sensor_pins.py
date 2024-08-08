import json
import os
from .string2pin import get_gpio_pin


def load_pin2sensor(file_path="configs/pin2sensor.json"):
    with open(file_path, "r") as file:
        return json.load(file)


def get_pin2sensor():
    pin2sensor = load_pin2sensor()

    for sensor, config in pin2sensor.items():
        pin_name = config["pin"]
        pin_object = get_gpio_pin(pin_name)
        config["pin"] = pin_object

    return pin2sensor
