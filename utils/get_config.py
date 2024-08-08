import os
import json
from dotenv import load_dotenv

load_dotenv()

def get_credentials():
	return {
		"azure_servicebus": {
			"uri": os.getenv("SERVICEBUS_URI"),
			"queue_name": os.getenv("QUEUE_NAME")
		}
	}	

def get_config(file_path="configs/config.json"):
    with open(file_path, "r") as file:
        return json.load(file)
	
	
	
