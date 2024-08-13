import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from utils.get_config import get_credentials
from collections import deque

credentials = get_credentials()
uri = credentials["azure_servicebus"]["uri"]
queue_name = credentials["azure_servicebus"]["queue_name"]

messages_queue = deque()


def send_data(sensor_data):
    global messages_queue

    messages_queue.append(json.dumps(sensor_data))

    try:
        with ServiceBusClient.from_connection_string(uri) as client:
            with client.get_queue_sender(queue_name) as sender:
                process_message_queue(sender)

    except Exception as e:
        print("Error sending data:", str(e))


def process_message_queue(sender):
    global messages_queue

    messages = [ServiceBusMessage(message) for message in messages_queue]

    sender.send_messages(messages)

    for message in messages_queue:
        print("sensor data has been sent", message)
    messages_queue.clear()
