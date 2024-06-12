import requests
from config import flask_base_server_url
import json

def release_from_warehouse(warehouse_release_params):
    response = requests.post(flask_base_server_url + '/warehouse/release', json=warehouse_release_params)
    
    return json.loads(response.text)
