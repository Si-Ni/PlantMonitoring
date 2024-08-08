from utils.get_sensors_config import get_sensors_config
from utils.get_config import get_config
from utils.scheduler import schedule_task
from sensors.sensors_factory import build_sensors
from sensors.sensors_reader import read_sensors
from services.servicebus_azure import send_data

config = get_config()
sensors = build_sensors(get_sensors_config())


def monitor_and_send():
    try:
        retry_attempts = config["sensors"]["retry_attempts"]
        sensor_data = read_sensors(sensors, retry_attempts)
        send_data(sensor_data)
        print("sensor data has been sent", sensor_data)
    except Exception as error:
        print(error)


if __name__ == "__main__":
    interval = config["azure_servicebus"]["sending_interval"]
    schedule_task(monitor_and_send, interval)
