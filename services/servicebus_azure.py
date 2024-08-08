import json
from azure.servicebus import ServiceBusClient, ServiceBusMessage
from utils.get_config import get_credentials

credentials = get_credentials()
uri = credentials["azure_servicebus"]["uri"]
queue_name = credentials["azure_servicebus"]["queue_name"]

def send_data(sensor_data):
    try:
        with ServiceBusClient.from_connection_string(uri) as client:
            with client.get_queue_sender(queue_name) as sender:
                message = ServiceBusMessage(json.dumps(sensor_data))
                sender.send_messages(message)
    except Exception as e:
        print("Error sending data:", str(e))
