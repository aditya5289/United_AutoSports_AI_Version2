# routes/augmented_reality_routes.py
from flask_restful import Resource

class AugmentedRealityRoutes(Resource):
    def get(self):
        return {'message': 'Augmented Reality Route'}
