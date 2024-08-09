import time


def generate_dto_azure(plant):
    return {plant: {"ts": time.time(), "sensors": []}}
