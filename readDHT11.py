import os
import time
import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage
import adafruit_dht
from board import D21
from dotenv import load_dotenv

load_dotenv()

SERVICEBUS_URI = os.getenv("SERVICEBUS_URI")
QUEUE_NAME = os.getenv("QUEUE_NAME")

dht_device = adafruit_dht.DHT11(D21)


def get_sensor_data(retries=5):
    for attempt in range(1, retries):
        try:
            temperature = dht_device.temperature
            humidity = dht_device.humidity

            if temperature is not None and humidity is not None:
                sensor_data = {
                    "ts": time.time(),
                    "sensors": [
                        {"type": "temperature", "value": temperature, "unit": "°C"},
                        {"type": "humidity", "value": humidity, "unit": "%"},
                    ],
                }
                return sensor_data, None
            else:
                if attempt < retries:
                    time.sleep(1)
                else:
                    return None, "Failed to retrieve data from humidity sensor"

        except RuntimeError as error:
            if attempt < retries:
                time.sleep(1)
            else:
                return None, f"Sensor error: {error}"
        except Exception as error:
            if attempt < retries:
                time.sleep(1)
            else:
                return None, f"Unexpected error: {error}"


def send_data(sensor_data):
    try:
        with ServiceBusClient.from_connection_string(SERVICEBUS_URI) as client:
            with client.get_queue_sender(QUEUE_NAME) as sender:
                message = ServiceBusMessage(json.dumps(sensor_data))
                sender.send_messages(message)
    except Exception as e:
        print("Error sending data:", str(e))


def main():
    while True:
        sensor_data, error = get_sensor_data()

        if error:
            print("Error retrieving sensor data:", error)
        else:
            print("Retrieved sensor data:", sensor_data)
            # send_data(sensor_data)

        break


if __name__ == "__main__":
    main()
