# routes/cognitive_endurance_routes.py
from flask_restful import Resource
import random

class CognitiveEnduranceRoutes(Resource):
    def get(self):
        return generate_driver_sensor_data()

def generate_driver_sensor_data():
    return {
        'heart_rate': random.uniform(60, 100),
        'blood_pressure': {
            'systolic': random.uniform(110, 130),
            'diastolic': random.uniform(70, 90)
        },
        'oxygen_saturation': random.uniform(95, 100),
        'reaction_time': random.uniform(0.2, 0.4),
        'cognitive_load': random.uniform(0, 1),
        'body_temperature': random.uniform(36.5, 37.5),
        'respiration_rate': random.uniform(12, 20),
        'electrodermal_activity': random.uniform(0, 10),
        'pupil_dilation': random.uniform(2, 8)
    }
