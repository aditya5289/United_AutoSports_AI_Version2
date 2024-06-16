# routes/predictive_maintenance_routes.py
from flask_restful import Resource
from models.predictive_maintenance import PredictiveMaintenanceModel
from flask import request, jsonify

class PredictiveMaintenanceRoutes(Resource):
    def __init__(self):
        self.model = PredictiveMaintenanceModel()

    def post(self):
        data = request.get_json()
        prediction = self.model.predict(data)
        return jsonify({'prediction': prediction.tolist()})
