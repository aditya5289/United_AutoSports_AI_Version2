# routes/blockchain_supply_chain_routes.py
from flask_restful import Resource

class BlockchainSupplyChainRoutes(Resource):
    def get(self):
        return {'message': 'Blockchain Supply Chain Route'}
