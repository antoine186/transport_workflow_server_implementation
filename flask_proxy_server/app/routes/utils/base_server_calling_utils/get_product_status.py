import requests
from config import flask_base_server_url
import json

def get_product_status(product_status_request_params):
    response = requests.get(flask_base_server_url + '/warehouse/product/status', json=product_status_request_params)
    
    return json.loads(response.text)
