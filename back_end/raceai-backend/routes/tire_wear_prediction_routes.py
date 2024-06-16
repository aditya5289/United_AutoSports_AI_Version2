from flask_restful import Resource

class TireWearPredictionRoutes(Resource):
    def get(self):
        # Mock data for tire attributes with additional attributes
        tire_data = {
            'front_left': {
                'pressure': 32,
                'temperature': 75,
                'wear_level': 20,
                'tread_depth': 7.5,  # in mm
                'sidewall_integrity': 'Good',
                'overall_condition': 'Fair'
            },
            'front_right': {
                'pressure': 32,
                'temperature': 76,
                'wear_level': 21,
                'tread_depth': 7.4,  # in mm
                'sidewall_integrity': 'Good',
                'overall_condition': 'Fair'
            },
            'rear_left': {
                'pressure': 30,
                'temperature': 74,
                'wear_level': 18,
                'tread_depth': 7.8,  # in mm
                'sidewall_integrity': 'Good',
                'overall_condition': 'Good'
            },
            'rear_right': {
                'pressure': 30,
                'temperature': 73,
                'wear_level': 19,
                'tread_depth': 7.7,  # in mm
                'sidewall_integrity': 'Good',
                'overall_condition': 'Good'
            }
        }
        return tire_data
