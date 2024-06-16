import eventlet
eventlet.monkey_patch()

from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
api = Api(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Import routes
from routes.cognitive_endurance_routes import CognitiveEnduranceRoutes
from routes.augmented_reality_routes import AugmentedRealityRoutes
from routes.blockchain_supply_chain_routes import BlockchainSupplyChainRoutes
from routes.predictive_maintenance_routes import PredictiveMaintenanceRoutes
from routes.sleep_optimization_routes import SleepOptimizationRoutes
from routes.tire_wear_prediction_routes import TireWearPredictionRoutes
from routes.workload_optimizer_routes import WorkloadOptimizerRoutes

# Add resource routes
api.add_resource(CognitiveEnduranceRoutes, '/cognitive-endurance')
api.add_resource(AugmentedRealityRoutes, '/augmented-reality')
api.add_resource(BlockchainSupplyChainRoutes, '/blockchain-supply-chain')
api.add_resource(PredictiveMaintenanceRoutes, '/predictive-maintenance')
api.add_resource(SleepOptimizationRoutes, '/sleep-optimization')
api.add_resource(TireWearPredictionRoutes, '/tire-wear-prediction')
api.add_resource(WorkloadOptimizerRoutes, '/workload-optimizer')

# WebSocket events
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('start_sending_data')
def handle_start_sending_data():
    print('Start sending data requested')
    socketio.start_background_task(target=send_driver_sensor_data)
    socketio.start_background_task(target=send_tire_sensor_data)

def send_driver_sensor_data():
    while True:
        data = generate_driver_sensor_data()
        socketio.emit('driver_sensor_data', data, namespace='/')
        socketio.sleep(1)

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

def send_tire_sensor_data():
    while True:
        data = generate_tire_sensor_data()
        socketio.emit('tire_sensor_data', data, namespace='/')
        socketio.sleep(1)

def generate_tire_sensor_data():
    return {
        'front_left': {
            'pressure': random.uniform(20, 40),
            'temperature': random.uniform(20, 100),
            'wear_level': random.uniform(0, 100),
            'tread_depth': random.uniform(1, 10),
            'sidewall_integrity': random.choice(['Good', 'Fair']),
            'overall_condition': random.choice(['Good', 'Fair'])
        },
        'front_right': {
            'pressure': random.uniform(20, 40),
            'temperature': random.uniform(20, 100),
            'wear_level': random.uniform(0, 100),
            'tread_depth': random.uniform(1, 10),
            'sidewall_integrity': random.choice(['Good', 'Fair']),
            'overall_condition': random.choice(['Good', 'Fair'])
        },
        'rear_left': {
            'pressure': random.uniform(20, 40),
            'temperature': random.uniform(20, 100),
            'wear_level': random.uniform(0, 100),
            'tread_depth': random.uniform(1, 10),
            'sidewall_integrity': random.choice(['Good', 'Fair']),
            'overall_condition': random.choice(['Good', 'Fair'])
        },
        'rear_right': {
            'pressure': random.uniform(20, 40),
            'temperature': random.uniform(20, 100),
            'wear_level': random.uniform(0, 100),
            'tread_depth': random.uniform(1, 10),
            'sidewall_integrity': random.choice(['Good', 'Fair']),
            'overall_condition': random.choice(['Good', 'Fair'])
        }
    }

if __name__ == '__main__':
    socketio.run(app, debug=True)
