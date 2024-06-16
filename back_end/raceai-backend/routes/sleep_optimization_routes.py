# routes/sleep_optimization_routes.py
from flask_restful import Resource

class SleepOptimizationRoutes(Resource):
    def get(self):
        return {'message': 'Sleep Optimization Route'}
