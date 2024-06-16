import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from websocket_server import WebsocketServer
import json
from models.predictive_maintenance import PredictiveMaintenanceModel

pm_model = PredictiveMaintenanceModel()

def new_client(client, server):
    print("New client connected and was given id %d" % client['id'])

def client_left(client, server):
    print("Client(%d) disconnected" % client['id'])

def message_received(client, server, message):
    data = json.loads(message)
    prediction = pm_model.predict([data])
    response = {'sensor_data': data, 'prediction': prediction.tolist()}
    server.send_message(client, json.dumps(response))

server = WebsocketServer(host='0.0.0.0', port=9001)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
