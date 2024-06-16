import time
import json
import random
from websocket import create_connection

ws = create_connection("ws://localhost:9001")

def generate_sensor_data():
    data = {
        "sensor_data": {
            "front_left": {
                "pressure": random.uniform(20, 35),
                "temperature": random.uniform(60, 100),
                "wear_level": random.uniform(0, 100),
                "tread_depth": random.uniform(5, 10),
                "sidewall_integrity": random.choice(['Good', 'Fair']),
                "overall_condition": random.choice(['Good', 'Fair'])
            },
            "front_right": {
                "pressure": random.uniform(20, 35),
                "temperature": random.uniform(60, 100),
                "wear_level": random.uniform(0, 100),
                "tread_depth": random.uniform(5, 10),
                "sidewall_integrity": random.choice(['Good', 'Fair']),
                "overall_condition": random.choice(['Good', 'Fair'])
            },
            "rear_left": {
                "pressure": random.uniform(20, 35),
                "temperature": random.uniform(60, 100),
                "wear_level": random.uniform(0, 100),
                "tread_depth": random.uniform(5, 10),
                "sidewall_integrity": random.choice(['Good', 'Fair']),
                "overall_condition": random.choice(['Good', 'Fair'])
            },
            "rear_right": {
                "pressure": random.uniform(20, 35),
                "temperature": random.uniform(60, 100),
                "wear_level": random.uniform(0, 100),
                "tread_depth": random.uniform(5, 10),
                "sidewall_integrity": random.choice(['Good', 'Fair']),
                "overall_condition": random.choice(['Good', 'Fair'])
            }
        },
        "prediction": "Maintenance Required Soon"
    }
    return data

while True:
    sensor_data = generate_sensor_data()
    ws.send(json.dumps(sensor_data))
    time.sleep(5)  # Send data every 5 seconds
