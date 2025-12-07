Student Details: 

Name: MOTURI SATISH 

Register Number: 42110825 



&nbsp;

MQTT Topic Used: 

home/satish-2025/sensor



&nbsp;

Project Overview: 

This project demonstrates IoT data flow using Python → MQTT → Home Assistant. 

A Python script publishes sensor data to the Mosquitto MQTT broker, and Home Assistant 

receives, reads, and displays these values in real time on the dashboard. 

The assignment includes: 

• Python code with mandatory name \& register number 

• MQTT broker setup 

• MQTT sensor configuration in Home Assistant 

• Live dashboard demonstration 

• Final recorded video 





Extra Sensor Used:

Vibration Sensor 

The vibration sensor detects movement or shaking. 

It is commonly used in: 

• Machine vibration monitoring 

• Door or window tamper alerts 

• Motion or disturbance detection 





Python Script (mqtt\_publish.py): 

import paho.mqtt.client as mqtt import time import json 

student\_name = "MOTURI SATISH" unique\_id = "42110825" topic = "home/satish

2025/sensor" 

client = mqtt.Client() client.connect("localhost", 1883, 60) 

while True: data = { "student\_name": student\_name, "unique\_id": unique\_id, 

"temperature": 25, "humidity": 60, "vibration": 1 } 

client.publish(topic, json.dumps(data)) 

print("Published:", data) 

time.sleep(5) 





Home Assistant Configuration (configuration.yaml): 

mqtt: sensor: - name: "Satish Temperature" state\_topic: "home/satish-2025/sensor" 

value\_template: "{{ value\_json.temperature }}" unit\_of\_measurement: "°C" - name: "Satish Humidity" 

state\_topic: "home/satish-2025/sensor" 

value\_template: "{{ value\_json.humidity }}" 

unit\_of\_measurement: "%" - name: "Satish Vibration" 

state\_topic: "home/satish-2025/sensor" 

value\_template: "{{ value\_json.vibration }}" 



Steps Followed: 

1\. Installed Home Assistant OS and created an account.

2\. Installed Mosquitto MQTT Broker and ensured it runs on

localhost:1883.

3.Installed paho-mqtt Python library and created mqtt\_publish.py. 

4.Added required fields (student name, register number, topic).

5.Published temperature, humidity, vibration values continuously. 

6.Verified MQTT messages using Node-RED. 

7.Added MQTT sensors in configuration.yaml. 

8.Restarted Home Assistant and verified real-time updates. 

9.Recorded assignment video with face + timestamp + dashboard 

output.

&nbsp;



