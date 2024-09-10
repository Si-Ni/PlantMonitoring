![image-removebg-preview](https://github.com/user-attachments/assets/ad26022c-f7d8-40ad-9cd6-b70c4216a899)

This is part of the **PlantMonitoring** project, a distributed system designed to monitor environmental data of plants. This specific module focuses on collecting sensor data via a Raspberry Pi, processing it, and then sending it to an Azure Queue for further processing.

# Project Overview
The **PlantMonitoring** project is a distributed system designed to collect, store and analyze environmental data for monitoring plant health. This repository handles the Raspberry Pi module, which reads data from various sensors and sends it to Azure Queue.

The main components of the project include:

- Data Collection: The Raspberry Pi reads environmental data from sensors.
- Data Transmission: The data is transmitted to an Azure Queue.
- Data Storage: A MongoDB database saves the data.
- Data Visualization: The [frontend](https://github.com/Si-Ni/PlantMonitoring-Frontend) processes and visualizes this data.

# System Architecture
## Overall System
Here is the big picture of the entire system, including how the Raspberry Pi module interacts with the cloud services, database and frontend:

![deploymentUML](https://github.com/user-attachments/assets/0f122e69-a8f9-4c18-b034-f0f8c2419426)

## Raspberry Pi Module
This diagram illustrates the specific architecture for the Raspberry Pi module, including sensor integration, data processing and communication with cloud services:

![classUML](https://github.com/user-attachments/assets/7920e360-ee27-445f-bdd9-5f5982a29882)

# Hardware Setup
## Components
- Raspberry Pi: Any version with GPIO pins
- Sensors:
  - Temperature sensor (BMP180)
  - Barometric air pressure sensor (BMP180)
  - Humidity sensor (DHT11)
  - Soil moisture sensor (YL-69) + analog digital converter (ADS1115)
  - Light intensity sensor (BH1750)
- Water pump
- Breadboard and wires for prototyping

Easy to expand by adding additional sensors

## Breadboard Setup

![breadboard](https://github.com/user-attachments/assets/3fcd990a-7d36-4926-857d-2acbd1f52635)

### Initial Real-Life Tests
Here is an image of the setup used during initial real-life tests:

![firstTests](https://github.com/user-attachments/assets/6daf0aa2-08e7-4699-b5fb-d7afdcddc7fe)

# Installation
1. Clone the repository:
```bash
git clone https://github.com/Si-Ni/PlantMonitoring-RaspberryPI.git
cd PlantMonitoring-RaspberryPI
```
2. Install the required dependencies:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```
3. Set up the environment variables for connection to the Azure Queue

### Running the System
To start collecting data and transmitting it to the cloud, run the following command: ```python3 main.py```
