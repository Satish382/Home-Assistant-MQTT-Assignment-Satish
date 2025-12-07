import paho.mqtt.client as mqtt
import time
import json

student_name = "MOTURI SATISH"
unique_id = "42110825"


topic = "home/satish-2025/sensor"

client = mqtt.Client()
client.connect("192.168.0.111", 1883, 60)

while True:
    data = {
        "student_name": student_name,
        "unique_id": unique_id,
        "temperature": 25,
        "humidity": 60,
        "vibration": 1
    }

    client.publish(topic, json.dumps(data))
    print("Published:", data)
    time.sleep(5)